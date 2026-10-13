---
title: Configure extension locations and installation options
category: how-to
topic: extensions
subtopic: configuration
component: CiviCRM extensions
audiences:
- technical
- administrator
- operations-user
level: advanced
journey_stage: plan-and-configure
summary: Configure extension locations, resource URLs, and repository-based installation options.
extensions: []
related: []
review_priority: medium
review_notes:
- The repository URL example refers to versions 4.5 and 4.6; its applicability is not established by the source.
- Backdrop is named among platforms with suggested default directories, but no Backdrop default location is listed.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: customize/extensions-part3.md
destination_path: sysadmin/customize/extensions-part3.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/customize/extensions-part3/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# Configure extension locations and installation options

## Advanced: Configuring the location of the extensions directory

Each CMS platform (WordPress, Drupal, Joomla, Backdrop ...) has a suggested default directory, but you can use a different location if you prefer/need.

- Go to: "Administer » System Settings » Directories"
- fill in "CiviCRM Extensions Directory" field and click "Save" at the bottom of the page.

!!! tip
    It's important to put your extensions directory outside of the $civicrm_home directory (the one where your codebase is installed) in order to avoid problems during upgrade. The extensions directory must be readable (so it can execute the extension code) and write-able (so it can download initial and updated versions of extensions) by your web server.

The default locations are:

- **Drupal**: `<docroot>/sites/<mysite>/files/civicrm/ext` Remembering that `<mysite>` is 'default' for most single site installs:
- **Joomla**: `<docroot>/media/civicrm/ext`
- **WordPress**: `<docroot>/wp-content/uploads/civicrm/ext`

### Configure the extensions resource URL

This is the base URL through which resources (css, js) of your extensions are accessible to the web; it corresponds to the same location as the "Extensions Directory" above.

- Go to **Administer » System Settings » Resource URLs**.
- Fill in **Extension Resource URL** and click **Save**.

If you positioned your extensions directory outside of the docroot, you'll need to put in place some special server configuration to make extensions' public assets accessible by http.

## Advanced: Other Extension Locations

CiviCRM will find, use and (via the web interface) manage extensions in the url and path location defined above, the "default" extension location for your install.

But CiviCRM will also find and use extensions in other locations. These locations might be populated by other mechanisms - e.g. a vetted subset of all extensions that are made available by default by a hosting provider. Specifically, CiviCRM will scan three directories and their subdirectories for info.xml files, similar to the mechanism that Drupal uses to automatically detect modules. The three directories correspond to three extension 'containers', as defined in the function "getFullContainer" of the file "CRM/Extension/System.php"

1. default : the one identified the settings. But note that although CiviCRM will only manage the extensions in the immediate directory location, it will still find them in subdirectories.
1. civiroot : the civicrm module code root, i.e. where the civicrm-version.php file is. This allows CiviCRM to be distributed with extensions (e.g. SearchKit), and different 'distributions' of CiviCRM to be created.
1. cmsvendor : a subdirectory 'vendor' of the CMS root (typically, the docroot of the web service). Analagous to the (core) module directory of the CMS. This one is not available for WordPress, only Drupal and Joomla, as noted in the code.

## Advanced: Using unstable (alpha/beta/pre-releases etc.) through the Manage Extensions screens.

You can change the _extension repository URL_. This is the URL used by CiviCRM to fetch the list of available extensions, and it can be customized by editing "civicrm.settings.php":

```
<?php
...
global $civicrm_setting;
// NB: for both Option A and Option B, you can use 4.5 or 4.6 etc as the {ver}
// Option A: Default repository URL; civicrm.org will make its best recommendation for stable/compatible extensions
$civicrm_setting['Extension Preferences']['ext_repo_url'] = 'http://civicrm.org/extdir/ver={ver}|cms={uf}';
// Option B: Customized repository URL which filters on "any release status" (stable, alpha, beta, etc)
$civicrm_setting['Extension Preferences']['ext_repo_url'] = 'http://civicrm.org/extdir/ver={ver}|cms={uf}|status=';
...
```

## Advanced: Disable automatic installations of extension

For security and policy reasons, you might want to disable the option to download extensions and only rely on the manual installation described above. It has the benefit of also suppressing a couple of possible warning messages: a message if you want to let this folder read only and one if your server does not have the PHP-ZIP extension - "You will not be able to install extensions at this time because your installation of PHP does not support ZIP archives".

To do so, you need to add this following line on your civicrm.settings.php

```
global $civicrm_setting;$civicrm_setting['Extension Preferences']['ext_repo_url'] = false;
```

As a result of disabling the automatic installations of extensions, on the New Extensions page `civicrm/admin/extensions?reset=1` (Drupal), you will see a message "The system administrator has disabled this feature."

<!-- Source: customize/extensions-part3.md -->
