---
title: Override paths
category: how-to
topic: system-administration
subtopic: path-overrides
component: CiviCRM paths
audiences:
- operations-user
level: intermediate
journey_stage: plan-and-configure
summary: Identify the CiviCRM paths that can be overridden and see how to set a path or URL override.
extensions: []
related: []
review_priority: high
review_notes:
- The override section names civicrm.settings.php in its heading but civicrm.civicrm.php in its instructions; the source does
  not resolve this contradiction.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: customize/paths.md
destination_path: sysadmin/customize/paths.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/customize/paths/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Override paths

CiviCRM tries to calculate the correct path and URL for a number of system folders. Sometimes it cannot calculate them correctly. System administrators can override these path variables in the CiviCRM settings file.

## Acceptable paths

The following paths can be overridden in civicrm.settings.php:

* `civicrm.log` - Path to the directory where CiviCRM is to store its log files - default: `[civicrm.private]/ConfigAndLog`
* `civicrm.private` - Location where private CiviCRM files, such as log files, should be stored. By default, this is the civicrm folder in the upload files directory of your CMS.
* `civicrm.compile` - Location of the Smarty compile directory - default: `[civicrm.private]/templates_c`
* `civicrm.packages` - Location where CiviCRM 3rd party packages are installed - default: `[civicrm.root]/packages`
* `civicrm.bower` - Location where the 3rd party Javascript code is installed - default: `[civicrm.root]/bower_components/`
* `civicrm.files` - Location where CiviCRM upload files are stored.
* `civicrm.root` - Location of the civicrm library code.
* `civicrm.l10n` - Location of the CiviCRM l10n directory - default: `[civicrm.root]/l10n`

## Override paths in civicrm.settings.php

To override paths within your civicrm.civicrm.php you need to include code like. You can override one or both of the 2 path variables either the system path or the url to find the contents.

```php
global $civicrm_paths;
$civicrm_paths['civicrm.packages']['path'] = '/var/www/testing/vendor/civicrm/civicrm-packages/';
$civicrm_paths['civicrm.packages']['url'] = 'https://example.com/vendor/civicrm/civicrm-packages/';
```

<!-- Source: customize/paths.md -->
