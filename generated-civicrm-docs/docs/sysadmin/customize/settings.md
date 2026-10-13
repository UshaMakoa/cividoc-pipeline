---
title: Override CiviCRM settings
category: how-to
topic: system-administration
subtopic: settings-overrides
component: CiviCRM settings
audiences:
- technical
level: intermediate
journey_stage: plan-and-configure
summary: Override settings in civicrm.settings.php when managing copies of a CiviCRM site.
extensions: []
related: []
review_priority: low
review_notes:
- The Temporary Files example uses customFileUploadDir, while the table lists uploadDir for Temporary Files and customFileUploadDir
  for Custom Files. The source does not explain the difference.
- The Temporary Files override in the table ends with l=;, which appears to make the example invalid. It has been preserved
  as written.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: customize/settings.md
destination_path: sysadmin/customize/settings.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/customize/settings/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Override CiviCRM settings

CiviCRM provides a web-based interface for configuring its settings. This is easy to use for new administrators who maintain a single site, but it presents challenges for administrators who manage many copies of CiviCRM. CiviCRM 4.1 introduced a settings system that allows administrators to override some settings by managing a custom PHP file.

For further information, see the [Settings Reference](https://docs.civicrm.org/dev/en/latest/framework/setting/).

## Use copied databases by overriding server directory and URL settings

Some organizations run separate copies of CiviCRM for "production" ("live"), "testing", and/or "development." For example, a developer might copy the production database to a development system to test a new feature without interrupting normal users. Most settings should be copied exactly, but server-specific settings—such as directory and URL settings—will differ.

These server-specific settings are *usually* determined automatically during installation. If you copy the database, an administrator must fix them to match the new system. Two administrative forms allow administrators to edit them manually:

- Administer > System Settings > Directories
- Administer > System Settings > Resource URLs

## Hidden settings

Some settings cannot be set from the administration user interface but can be overridden using the same technique. These include the Community Messages URL and whether users can download extensions. For more details, see [Disable automatic installation of extensions](extensions.md).

## Override settings in civicrm.settings.php

If you regularly copy a production database to a test or development server, editing server-specific settings manually may become cumbersome and error-prone. Instead, you can override settings such as directory and URL paths in a local copy of the CiviCRM settings file (*civicrm.settings.php*).

First, ensure this line exists in civicrm.settings.php before any override settings:

```
global $civicrm_setting;
```

## Override the Temporary Files directory

To override the Temporary Files directory for a test site, add these lines to *civicrm.settings.php*:

```
// Override the Temporary Files directory
$civicrm_setting['domain']['customFileUploadDir'] = '/var/www/testing/sites/default/files/civicrm/upload';
```

The example has three parts:

1. **Entity** (`'domain'`): This is a `domain`-level setting. The vast majority of settings are `domain`-level; a handful are `contact`-level. *Note: In CiviCRM <=4.6, this field used longer expressions such as `Directory Preferences` or `URL Preferences`. For backward compatibility, these are treated as aliases for `domain`.*
2. **Name** (`'customFileUploadDir'`): The name of the setting.
3. **Value** (`'/var/www/testing/sites/default/files/civicrm/upload'`): The new value of the setting.

## Additional settings

The table shows some settings file "constants" that override the database value if present in *civicrm.settings.php*, alongside their administrative settings fields.

| Admin Field (Form) | Settings File Override Example |
| --- | --- |
| **Temporary Files** (System Settings > Directories) | `$civicrm_setting['domain']['uploadDir'] = '/path/to/upload-dir'l=;` |
| **Images** (System Settings > Directories) | `$civicrm_setting['domain']['imageUploadDir'] = '/path/to/image-upload-dir';` |
| **Custom Files** (System Settings > Directories) | `$civicrm_setting['domain']['customFileUploadDir'] = '/path/to/file-upload-dir';` |
| **Custom Templates** (System Settings > Directories) | `$civicrm_setting['domain']['customTemplateDir'] = '/path/to/template-dir';` |
| **Custom PHP Path Directory** (System Settings > Directories) | `$civicrm_setting['domain']['customPHPPathDir'] = '/path/to/custom-php-dir';` |
| **Extensions Directory** (System Settings > Directories) | `$civicrm_setting['domain']['extensionsDir'] = '/path/to/extensions-dir';` |
| **CiviCRM Resource URL** (System Settings > Resource URLs) | `$civicrm_setting['domain']['userFrameworkResourceURL'] = 'http://example.com/example-resource-url/';` |
| **Image Upload URL** (System Settings > Resource URLs) | `$civicrm_setting['domain']['imageUploadURL'] = 'http://example.com/example-image-upload-url';` |
| **Custom CiviCRM CSS URL** (System Settings > Resource URLs) | `$civicrm_setting['domain']['customCSSURL'] = 'http://example.com/example-css-url';` |
| **Extensions Resource URL** (System Settings > Resource URLs) | `$civicrm_setting['domain']['extensionsURL'] = 'http://example.com/pathtoextensiondir';` |
| **Disable display of Community Messages on home dashboard** | `$civicrm_setting['domain']['communityMessagesUrl'] = false;` |
| **Disable automatic download / installation of extensions** | `$civicrm_setting['domain']['ext_repo_url'] = false;` |
| **Set How long HTTP Requests could last for before timing out** | `$civicrm_setting['domain']['http_timeout'] = '0.5';` |
| **Enable SSL** | `$civicrm_setting['domain']['enableSSL'] = false;` |
| **Verify SSL** | `$civicrm_setting['domain']['verifySSL'] = false;` |

For a full list of settings, see [the master settings PHP files](https://github.com/civicrm/civicrm-core/tree/master/settings).

!!! warning "Incorrect Paths May Cause Unexpected Behaviors"

    Review the path values you are saving to these override constants carefully before saving the file. Incorrect path definitions may cause display issues and / or other unexpected behavior in CiviCRM pages and forms. If you've browsed to your site when an incorrect Resource URL or Custom CSS value has been set, you'll probably need to do a forced refresh with your browser. You may also need to empty the browser cache to make sure the correct CSS and Javascript files get loaded.

!!! notice "HTTP Timeout Setting"

    From CiviCRM 5.15 onwards there is a hidden setting for the HTTP request timeout in seconds. The default for this is 5 seconds. Adjusting the timeout will affect both the page load times (lower time, pages will load faster), too low a timeout and CiviCRM status checks may not complete in time resulting in users seeing an incorrect status alert check failed warning message.

<!-- Source: customize/settings.md -->
