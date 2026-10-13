---
title: Install CiviCRM on WordPress with Composer
category: how-to
topic: installation
subtopic: composer
component: CiviCRM
audiences:
- technical
- administrator
level: intermediate
journey_stage: plan-and-configure
summary: Add CiviCRM to a Composer-based WordPress site and configure its asset path and resource URL.
extensions: []
related: []
review_priority: low
review_notes:
- The composer.json example is missing a comma after the "url" value, so it cannot be used as valid JSON without a correction;
  the source example is unchanged.
guide: installation
source_repository: https://lab.civicrm.org/documentation/docs/installation.git
source_path: wordpress/composer.md
destination_path: installation/wordpress/composer.md
legacy_urls:
- https://docs.civicrm.org/installation/en/latest/wordpress/composer/
civicrm_version:
- latest
source_commit: 5a8b870477f63bea90551acb2f7516df67784b19
last_modified: '2026-08-20'
---

# Install CiviCRM on WordPress with Composer

## Get the code (alternative method - Composer) {:#composer}

Composer is a *dependency management* tool which can add, upgrade and remove software *packages* for your site.

If `composer` is properly installed and setup to install WordPress via `composer`, then these example commands will add latest CiviCRM version to WordPress:

```
cd /var/www/wp.example.org
composer config extra.enable-patching true
composer require civicrm/civicrm-{core,packages,wordpress,asset-plugin}
composer require civicrm/cli-tools
```

??? info "More detail: Enable patching"

    A handful of packages used by CiviCRM require extra patch-files.

    This is possible with the popular [cweagans/composer-patches](https://github.com/cweagans/composer-patches)
    plugin. However, you must [opt-in to enable it](https://github.com/cweagans/composer-patches#allowing-patches-to-be-applied-from-dependencies).

### CiviCRM Asset Plugin {:#asset-plugin}

[CiviCRM Asset Plugin](https://lab.civicrm.org/dev/civicrm-asset-plugin) is used to copy css/js and other static assets from the vendor directory to the plugin directory.

Configure the paths that CiviCRM Asset Plugin copies files to in the "extra" section of the composer.json. You must set the path to the location of the 'civicrm' directory inside the CiviCRM Wordpress plugin directory.

For example, for the [Bedrock Wordpress](https://roots.io/bedrock/) composer template, set as:

```
"extra": {
    "civicrm-asset": {
        "path": "web/app/plugins/civicrm/civicrm",
        "url": "/app/plugins/civicrm/civicrm"
        "assets:packages": {
            "+include": ["kcfinder/**.php"]
        }
    }
}
```

After adding this and requiring the civicrm packages, execute the command:

```
composer civicrm:publish
```

### civicrm.settings.php userFrameworkResourceURL

Currently one modification to one setting is necessary in the civicrm.settings.php after installation with a composer based codebase.

For the 'userFrameworkResourceURL' setting add ```/core``` to the end of the path that CiviCRM generates in the civicrm.settings.php.

The example below is for a [Bedrock](https://roots.io/bedrock/) composer template directory structure.

```
// Just add "/core" to what civicrm generates here.
$civicrm_setting['domain']['userFrameworkResourceURL'] = 'https://mysite.org/app/plugins/civicrm/civicrm/core';
```

<!-- Source: wordpress/composer.md -->
