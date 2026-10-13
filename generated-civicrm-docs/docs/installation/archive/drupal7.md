---
title: Install CiviCRM on Drupal 7
category: how-to
topic: installation
subtopic: drupal-7-installation
component: Drupal 7
audiences:
- technical
- administrator
level: intermediate
journey_stage: plan-and-configure
summary: Download CiviCRM, run the Drupal 7 installer, and find troubleshooting and post-installation guidance.
extensions: []
related: []
review_priority: high
review_notes:
- Drupal 7 is End of Life and not recommended for new sites; this installation page may mislead readers who miss the opening
  notice.
- The Drupal web UI warning refers to CiviCRM 5.13–5.30 and says installation should work again in 5.31. The version-specific
  wording and its associated TODO appear dated and have been left unchanged.
guide: installation
source_repository: https://lab.civicrm.org/documentation/docs/installation.git
source_path: archive/drupal7.md
destination_path: installation/archive/drupal7.md
legacy_urls:
- https://docs.civicrm.org/installation/en/latest/archive/drupal7/
civicrm_version:
- latest
source_commit: 5a8b870477f63bea90551acb2f7516df67784b19
last_modified: '2026-08-20'
---

# Install CiviCRM on Drupal 7

???+ tldr "About this document"

    Drupal 7 is now officially End of Life and is *not recommended for new sites*.

    If you are still using Drupal 7 [this list of options will help you evaluate your best course of action](https://civicrm.org/drupal-7-options).

## Get the code {:#drupal7-download}

The [CiviCRM download page](https://civicrm.org/download) provides a pre-built archive for use with Drupal 7. A typical archive file is ~20mb and looks like `civicrm-X.Y.Z-drupal.tar.gz`. It contains a folder named `civicrm/`.

In Drupal 7, there is a folder for storing add-on modules: `DRUPAL_ROOT/sites/all/modules`.

Download the archive and extract it into this folder. Here are a few ways to do that:

??? example "Download via web-browser"

    This method does not require shell access on the server. You may adapt it based on your server's arrangement.

    * On the [CiviCRM download page](https://civicrm.org/download), click the link for CiviCRM / Drupal 7. Save the file locally.
    * Extract the archive locally. For example, on a Linux workstation, one might say:
      ```bash
      cd ~/Downloads
      tar xvzf civicrm-X.Y.Z-drupal.tar.gz
      ```
    * Observe the new folder `civicrm/`.
    * Using your preferred file-transfer system (SSH/SFTP, `rsync`, `git`, `mv`, etc), transfer the `civicrm/` folder to `DRUPAL_ROOT/sites/all/modules`.

??? example "Download via curl + tar"

    This method requires shell access to the Drupal server.

    * On the [CiviCRM download page](https://civicrm.org/download), note the current version.
    * In the shell, navigate to the Drupal module folder (*adjust as appropriate*):
      ```bash
      cd DRUPAL_ROOT/sites/all/modules
      ```
    * In the shell, run the `curl` and `tar` commands. Adjust the version `X.Y.Z` to the appropriate value.
      ```bash
      curl -L "https://download.civicrm.org/civicrm-X.Y.Z-drupal.tar.gz" | tar xvz
      ```

??? example "Download via Drupal web UI"

    This is the easiest way for a new administrator. However, it may not work in all deployments or all versions. For example, if the Drupal server has a locked-down configuration, then it may encounter permission errors or timeouts. The only way to find out is to try.

    * On the [CiviCRM download page](https://civicrm.org/download), right-click the link for CiviCRM / Drupal 7. Copy the URL.
    * Login to your Drupal site with *administrator* permissions.
    * Navigate to **Modules &gt;&gt; Install new module**.
    * Paste the URL
    * Click "Install"

    ??? warning "This may not work with CiviCRM 5.13-5.30"

        In CiviCRM versions 5.13 - 5.30, the prebuilt tarball included a symlink which is not accepted by the Drupal 7 installer. This should work again in 5.31.

        <!-- TODO: After 5.31 has been out for a while, we can move this option higher up and remove/downgrade the notice. -->

    ??? warning "The "Upload"/"Browse" option is unlikely to work."

        The **Install new module** page provides another option for uploading the archive from your local computer. In a default PHP configuration, the upload limits are too conservative to accept the CiviCRM archive.

In all cases, the final outcome should be the creation of a new folder:

```
DRUPAL_ROOT/sites/all/modules/civicrm
```

## Get the translations for Drupal 7 {:#drupal7-i18n}

The basic CiviCRM release includes support for US English (`en_US`). To use another language or dialect, please [download and extract the translation files](../general/i18n_l10n.md).

## Run the installer for Drupal 7 {:#drupal7-installer}

The installer verifies requirements, prepares the database, and initializes the configuration file. You may run the installer through the web interface (*which is simpler*) or the command-line interface (*which has more options*).

??? example "Run installer via Drupal 7 web UI"

    1. Enable the "CiviCRM" module:
        * Login to your Drupal site with *administrator* permissions.
        * Navigate to the "Modules" page (`admin/modules`).
        * Find "CiviCRM" and enable it.
        * At the bottom, click "Save Configuration".
    2. After enabling, the status message will display a link to "configure CiviCRM". Click it.

        ??? question "What if I didn't notice the link?"
            Use the URL bar. Navigate to the `civicrm` page (e.g. `https://example.com/civicrm`).

    3. The CiviCRM installer will open.
        * *If there are unmet requirements*, the installer will list them. Consult the [Requirements](../requirements/index.md) documentation for additional advice.
        * *If all the requirements are met*, proceed through the brief questionnaire.
        * *If you have [a separate MySQL database for CiviCRM](../requirements/index.md#mysql-connection)*, then locate "Environment: CiviCRM Database". Click the edit icon and enter the [database URL](../requirements/index.md#mysql-connection).
        * Finally, click "Install CiviCRM".

??? example "Run installer via the command-line"

    CiviCRM has a command-line administration tool, `cv`, which can perform installation. For details, see [command-line installer](../general/cli-cv.md).

## Troubleshooting {:#troubleshooting}

* Review the [Troubleshooting](../troubleshooting/index.md) page for help with problems you may encounter during the installation.

## Post-installation {:#post-install}

See [the main Drupal page for Post-installation steps](../drupal/index.md#post-install).

<!-- Source: archive/drupal7.md -->
