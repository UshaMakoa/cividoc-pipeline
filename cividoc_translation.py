"""Intégration locale de LibreTranslate et lexique protégé CiviCRM."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

def install_translator(
    site: Path,
    config: Dict[str, Any],
    endpoint: str,
    target_languages: List[str],
    source_language: str = "en",
) -> None:
    """Install a runtime LibreTranslate language switcher."""

    base_url = endpoint.strip().rstrip("/")

    if base_url.endswith("/translate"):
        base_url = base_url[: -len("/translate")]

    translator_config = {
        "baseUrl": base_url,
        "sourceLanguage": source_language,
        "targetLanguages": target_languages,
        "batchSize": 20,
    }

    js_directory = site / "docs" / "js"
    css_directory = site / "docs" / "css"

    js_directory.mkdir(parents=True, exist_ok=True)
    css_directory.mkdir(parents=True, exist_ok=True)

    javascript = r"""
(() => {
  "use strict";

  const config = __TRANSLATOR_CONFIG__;
  const translateEndpoint = `${config.baseUrl}/translate`;
  const languagesEndpoint = `${config.baseUrl}/languages`;
  const storageKey = "cividoc-language";

  const originalText = new WeakMap();
  const translationCache = new Map();

  const excludedSelector = [
    "script",
    "style",
    "pre",
    "code",
    "kbd",
    "samp",
    "textarea",
    "svg",
    "[data-no-translate]",
    ".no-translate",
    ".cividoc-language-switcher"
  ].join(",");

  let activeRequest = 0;
  let supportedLanguages = [];

  function storedLanguage() {
    try {
      return window.localStorage.getItem(storageKey) || config.sourceLanguage;
    } catch (_) {
      return config.sourceLanguage;
    }
  }

  function storeLanguage(language) {
    try {
      window.localStorage.setItem(storageKey, language);
    } catch (_) {
      // The switcher still works when storage is unavailable.
    }
  }

  async function loadSupportedLanguages() {
    try {
      const response = await fetch(languagesEndpoint, {
        headers: {
          "Accept": "application/json"
        }
      });

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }

      const payload = await response.json();

      if (!Array.isArray(payload)) {
        throw new Error("Invalid languages response");
      }

      const allowed = new Set([
        config.sourceLanguage,
        ...config.targetLanguages
      ]);

      supportedLanguages = payload
        .filter(item => item && allowed.has(item.code))
        .map(item => ({
          code: item.code,
          name: item.name || item.code,
          targets: Array.isArray(item.targets) ? item.targets : []
        }));

    } catch (error) {
      console.warn(
        "Could not load LibreTranslate languages:",
        error
      );

      supportedLanguages = [
        {
          code: config.sourceLanguage,
          name: "English",
          targets: config.targetLanguages
        },
        ...config.targetLanguages.map(code => ({
          code,
          name: code.toUpperCase(),
          targets: []
        }))
      ];
    }

    if (
      !supportedLanguages.some(
        language => language.code === config.sourceLanguage
      )
    ) {
      supportedLanguages.unshift({
        code: config.sourceLanguage,
        name: "English",
        targets: config.targetLanguages
      });
    }
  }

  function translatableTextNodes() {
    const roots = document.querySelectorAll(
      ".md-content, .md-nav, .md-header__topic"
    );

    const nodes = [];

    for (const root of roots) {
      const walker = document.createTreeWalker(
        root,
        NodeFilter.SHOW_TEXT,
        {
          acceptNode(node) {
            if (!node.nodeValue || !node.nodeValue.trim()) {
              return NodeFilter.FILTER_REJECT;
            }

            const parent = node.parentElement;

            if (!parent || parent.closest(excludedSelector)) {
              return NodeFilter.FILTER_REJECT;
            }

            return NodeFilter.FILTER_ACCEPT;
          }
        }
      );

      while (walker.nextNode()) {
        const node = walker.currentNode;

        if (!originalText.has(node)) {
          originalText.set(node, node.nodeValue);
        }

        nodes.push(node);
      }
    }

    return nodes;
  }

  function splitWhitespace(value) {
    const match = value.match(/^(\s*)([\s\S]*?)(\s*)$/);

    return {
      prefix: match ? match[1] : "",
      text: match ? match[2] : value,
      suffix: match ? match[3] : ""
    };
  }

  function restoreEnglish(nodes) {
    for (const node of nodes) {
      const original = originalText.get(node);

      if (typeof original === "string") {
        node.nodeValue = original;
      }
    }

    document.documentElement.lang = config.sourceLanguage;
  }

  async function requestTranslations(texts, targetLanguage) {
    const response = await fetch(translateEndpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify({
        q: texts,
        source: config.sourceLanguage,
        target: targetLanguage,
        format: "text"
      })
    });

    if (!response.ok) {
      const details = await response.text();

      throw new Error(
        `LibreTranslate returned HTTP ${response.status}: ${details}`
      );
    }

    const payload = await response.json();
    const translated = payload.translatedText;

    if (Array.isArray(translated)) {
      return translated;
    }

    if (typeof translated === "string" && texts.length === 1) {
      return [translated];
    }

    throw new Error("LibreTranslate returned an invalid response");
  }

  async function translatePage(targetLanguage) {
    const requestId = ++activeRequest;
    const nodes = translatableTextNodes();

    if (targetLanguage === config.sourceLanguage) {
      restoreEnglish(nodes);
      return;
    }

    const pending = [];

    for (const node of nodes) {
      const original = originalText.get(node);

      if (typeof original !== "string") {
        continue;
      }

      const parts = splitWhitespace(original);

      if (!parts.text.trim()) {
        continue;
      }

      pending.push({
        node,
        original,
        ...parts
      });
    }

    for (
      let start = 0;
      start < pending.length;
      start += config.batchSize
    ) {
      if (requestId !== activeRequest) {
        return;
      }

      const batch = pending.slice(
        start,
        start + config.batchSize
      );

      const missingTexts = [];
      const missingIndexes = [];

      batch.forEach((item, index) => {
        const cacheKey = `${targetLanguage}\u0000${item.text}`;

        if (!translationCache.has(cacheKey)) {
          missingTexts.push(item.text);
          missingIndexes.push(index);
        }
      });

      if (missingTexts.length) {
        const translations = await requestTranslations(
          missingTexts,
          targetLanguage
        );

        translations.forEach((translation, index) => {
          const batchIndex = missingIndexes[index];
          const sourceText = batch[batchIndex].text;
          const cacheKey = `${targetLanguage}\u0000${sourceText}`;

          translationCache.set(cacheKey, translation);
        });
      }

      if (requestId !== activeRequest) {
        return;
      }

      for (const item of batch) {
        const cacheKey = `${targetLanguage}\u0000${item.text}`;
        const translation = translationCache.get(cacheKey);

        if (typeof translation === "string") {
          item.node.nodeValue =
            item.prefix + translation + item.suffix;
        }
      }
    }

    document.documentElement.lang = targetLanguage;
  }

  function createLanguageSwitcher() {
    let wrapper = document.getElementById(
      "cividoc-language-switcher"
    );

    if (wrapper) {
      return wrapper.querySelector("select");
    }

    wrapper = document.createElement("div");
    wrapper.id = "cividoc-language-switcher";
    wrapper.className = "cividoc-language-switcher";
    wrapper.setAttribute("data-no-translate", "true");

    const label = document.createElement("label");
    label.className = "cividoc-language-label";
    label.setAttribute("for", "cividoc-language-select");
    label.textContent = "Language";

    const select = document.createElement("select");
    select.id = "cividoc-language-select";
    select.className = "cividoc-language-select";
    select.setAttribute("aria-label", "Select documentation language");

    for (const language of supportedLanguages) {
      select.add(
        new Option(
          language.name,
          language.code
        )
      );
    }

    const status = document.createElement("span");
    status.className = "cividoc-language-status";
    status.setAttribute("role", "status");
    status.setAttribute("aria-live", "polite");

    select.value = storedLanguage();

    select.addEventListener("change", async () => {
      const targetLanguage = select.value;

      storeLanguage(targetLanguage);
      select.disabled = true;
      status.textContent = "Translating…";

      try {
        await translatePage(targetLanguage);
        status.textContent = "";
      } catch (error) {
        console.error(
          "LibreTranslate translation failed:",
          error
        );

        status.textContent =
          error instanceof Error
            ? `Translation failed: ${error.message}`
            : "Translation failed";

        select.value = config.sourceLanguage;
        storeLanguage(config.sourceLanguage);
        restoreEnglish(translatableTextNodes());
      } finally {
            select.disabled = false;
      }
    });

    wrapper.append(label, select, status);

    const header =
      document.querySelector(".md-header__inner") ||
      document.body;

    header.appendChild(wrapper);

    return select;
  }

  async function initialiseTranslator() {
    if (!supportedLanguages.length) {
      await loadSupportedLanguages();
    }

    const select = createLanguageSwitcher();
    const language = storedLanguage();

    if (
      !supportedLanguages.some(
        item => item.code === language
      )
    ) {
      storeLanguage(config.sourceLanguage);
      select.value = config.sourceLanguage;
      restoreEnglish(translatableTextNodes());
      return;
    }

    select.value = language;

    if (language !== config.sourceLanguage) {
      try {
        await translatePage(language);
      } catch (error) {
        console.error(
          "LibreTranslate translation failed:",
          error
        );

        select.value = config.sourceLanguage;
        storeLanguage(config.sourceLanguage);
        restoreEnglish(translatableTextNodes());
          }
  }

  function startTranslator() {
    initialiseTranslator().catch(error => {
      console.error(
        "LibreTranslate initialisation failed:",
        error
      );
    });
  }

  if (
    typeof document$ !== "undefined" &&
    document$ &&
    typeof document$.subscribe === "function"
  ) {
    document$.subscribe(startTranslator);
  } else if (
    document.readyState === "loading"
  ) {
    document.addEventListener(
      "DOMContentLoaded",
      startTranslator,
      { once: true }
    );
  } else {
    startTranslator();
  }
})();
""".replace(
        "__TRANSLATOR_CONFIG__",
        json.dumps(
            translator_config,
            ensure_ascii=False,
        ),
    )

    stylesheet = """
.cividoc-language-switcher {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  margin-left: auto;
  padding: 0 0.5rem;
  color: var(--md-primary-bg-color);
  font-size: 0.7rem;
}

.cividoc-language-label {
  white-space: nowrap;
}

.cividoc-language-select {
  min-height: 2rem;
  max-width: 10rem;
  padding: 0.2rem 1.7rem 0.2rem 0.5rem;
  border: 1px solid currentColor;
  border-radius: 0.2rem;
  color: var(--md-default-fg-color);
  background: var(--md-default-bg-color);
}

.cividoc-language-select:focus-visible {
  outline: 2px solid var(--md-accent-fg-color);
  outline-offset: 2px;
}

.cividoc-language-status {
  min-width: 1rem;
  white-space: nowrap;
  font-size: 0.65rem;
}

@media screen and (max-width: 44.984375em) {
  .cividoc-language-label,
  .cividoc-language-status {
    display: none;
  }

  .cividoc-language-switcher {
    padding: 0;
  }

  .cividoc-language-select {
    max-width: 7rem;
  }
}
""".strip()

    javascript_path = (
        js_directory
        / "libretranslate-language-switcher.js"
    )

    stylesheet_path = (
        css_directory
        / "libretranslate-language-switcher.css"
    )

    javascript_path.write_text(
        javascript + "\n",
        encoding="utf-8",
    )

    stylesheet_path.write_text(
        stylesheet + "\n",
        encoding="utf-8",
    )

    extra_javascript = config.setdefault(
        "extra_javascript",
        [],
    )

    script_name = (
        "js/libretranslate-language-switcher.js"
    )

    if script_name not in extra_javascript:
        extra_javascript.append(script_name)

    extra_css = config.setdefault(
        "extra_css",
        [],
    )

    stylesheet_name = (
        "css/libretranslate-language-switcher.css"
    )

    if stylesheet_name not in extra_css:
        extra_css.append(stylesheet_name)
