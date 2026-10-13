---
title: Upgrading CiviCRM for Drupal 8/9/10
category: how-to
topic: system-administration
subtopic: drupal-8-9-10
component: CiviCRM for Drupal
audiences:
- technical
level: intermediate
journey_stage: manage-and-automate
summary: Upgrade CiviCRM code and its database on a Drupal 8/9/10 site using Composer.
extensions: []
related:
- index.md#before-upgrading
review_priority: medium
review_notes:
- The version examples refer to CiviCRM 5.29 and 5.31, and the database upgrade options specify drush v8; review whether these
  examples remain useful.
- The instruction that the asset plugin "needs the first update" is unclear about why that update must come first.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: upgrade/drupal8.md
destination_path: sysadmin/upgrade/drupal8.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/upgrade/drupal8/
civicrm_version:
- 5.29.0
- 5.30.0
- 5.31.0
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Upgrading CiviCRM for Drupal 8/9/10

???+ tldr "About this document"

    Use this document to upgrade CiviCRM installations on Drupal 8/9/10 to the latest CiviCRM release.

    The document assumes that:

    * CiviCRM and Drupal 8/9/10 are already installed and working.
    * You are able to run `composer` and manage `composer.json`.
    * You have identified the root of your Drupal project -- such as `/var/www/example.org`.

!!! caution "Before upgrading"
    Make sure you have done the steps listed in [before upgrading](index.md#before-upgrading) first.

Drupal 8/9/10 (D10) sites are typically administered with [Composer](https://www.getcomposer.org). Composer is a *dependency management* tool which can add, upgrade, and remove software *packages* for your site.

CiviCRM is published as a suite of related packages. The goal is to use Composer to update CiviCRM's code, then upgrade the database.

## Review `composer.json`

The file `composer.json` lists a series of *required* packages. Each package has a *version constraint*. For example, a typical file might specify:

```javascript
{
  "require": {
    "civicrm/civicrm-core": "~5.29.0",
    "civicrm/civicrm-packages": "~5.29.0",
    "civicrm/civicrm-drupal-8": "~5.29.0",
    "civicrm/civicrm-asset-plugin": "~1.0.0"
  }
}
```

Look at your configuration and answer these questions:

??? question "What is the version constraint?"

    In the above example, it uses a version constraint: `~5.29.0`. This matches `5.29.0` and roughly equivalent versions (`5.29.1`, `5.29.2`, etc). However, it does *not* match `5.30.0`.

    A common alternative might be `~5.29`. This matches `5.29` and roughly equivalent versions (`5.30`, `5.31`, etc). However, it does *not* match `6.0`.

    If the constraint looks unfamiliar, review [Composer: Writing Version Constraints](https://getcomposer.org/doc/articles/versions.md#writing-version-constraints).

??? question "Which plugin is responsible for CiviCRM's JS+CSS files?"

    CiviCRM-Drupal (8/9/10) requires a *composer plugin* to handle JS+CSS assets. There are two common plugins. `composer.json` may specify:

    * **[civicrm/civicrm-asset-plugin](https://lab.civicrm.org/dev/civicrm-asset-plugin/)**: Used on newer deployments. Better compatibility with different variations of Drupal 8/9/10.
    * **[roundearth/civicrm-composer-plugin](https://gitlab.com/roundearth/civicrm-composer-plugin)**: Used on older deployments. Better compatibility with older versions of CiviCRM.
    * **Neither**: The significance of omission depends on the version. For CiviCRM v5.31+ (Nov 2020), omission implies `civicrm/civicrm-asset-plugin`. In older versions, omission is likely a misconfiguration.

    For our purposes, we assume that you should keep the current plugin. Switching to a different plugin requires extra effort.
    <!-- TODO: When there's a migration guide, link to it. -->

    ??? note "What if both plugins are listed in `composer.json`?"

        This is most likely a mistake. The significance depends on the versions:

        * If `civicrm/civicrm-asset-plugin` is `1.1.1` (Oct 2020) or newer, it will defer to `roundearth/civicrm-composer-plugin`.
        * If `civicrm/civicrm-asset-plugin` is older, then the behavior is unknown/undefined/unsupported.

## Upgrade the plugin

If `composer.json` lists `civicrm/civicrm-asset-plugin` as `~1.0.0`, then it needs the first update.

```bash
composer require civicrm/civicrm-asset-plugin:~1.1
```

Otherwise, continue to the next step.

## Upgrade the code {:#download}

Choose one of the following methods:

* Run the command `composer update`. This finds the newest version which *matches the current constraint*. For example, if the constraint specifies `~5.29.0`, then `composer update` will find `5.29.2` or `5.29.3` or similar.

    ```bash
    composer update civicrm/civicrm-{core,packages,drupal-8} --with-dependencies
    ```

* Run the command `composer require`. This *changes the current constraint*. For example, to switch to `~5.31.0`, run:

    ```bash
    composer require civicrm/civicrm-{core,packages,drupal-8}:~5.31.0
    ```

## Upgrade the translations

In some workflows for internationalized deployments, you would need [re-download the translations](https://docs.civicrm.org/installation/en/latest/drupal8/#i18n).

<!-- FIXME when https://lab.civicrm.org/documentation/docs/installation/-/issues/4 is closed -->

## Upgrade the database

Choose one of the following methods:

* Run the following `cv` command from within your site:

    ```bash
    cv upgrade:db
    ```

    !!! tip "Tip: Preview upgrade steps"

        The `cv upgrade:db` command accepts a `--dry-run` option to show what changes will be executed.
        For the maximum detail, use `cv upgrade:db --dry-run -vv`.

* Or, run the following `drush` (v8) command from within your site:

    ```bash
    drush civicrm-upgrade-db
    ```

* Or, point your web browser to the following URL and follow the on-screen instructions.

    ```
    http://example.org/civicrm/upgrade?reset=1
    ```

## Additional cleanup

The upgrade must reset various resources (such as file-caches, database-caches, and public-assets). Several of these steps are automatic, but automation isn't perfect. You may find it advantageous to manually reset some resources after an upgrade.

At various times, these additional cleanup steps have been useful:

* Delete cache files with `rm`

    ```bash
    rm -rf sites/default/files/civicrm/templates_c/
    ```

* Clear database caches with `drush` or `cv`

    ```bash
    drush cache-clear civicrm
    ```

    ```bash
    cv flush
    ```

* Re-publish static assets (`*.js`, `*.css`, etc) with `composer`

    ```bash
    composer civicrm:publish
    ```

The above steps should not normally be necessary, but they may help with customized workflows or with unresolved bugs. If you identify a scenario where these steps are necessary, please [report an issue](https://civicrm.org/bug-reporting). (For example, [dev/core#4754](https://lab.civicrm.org/dev/core/-/issues/4754) reports about a scenario with asset publication.)

Finally, recall if you did any special modifications during the upgrade. If so, you may need to undo them. For example:

* If you enabled maintenance mode, then you should switch back to production mode.
* If you disabled any conflicted modules, then you may want to re-enable them.

<!-- Source: upgrade/drupal8.md -->
