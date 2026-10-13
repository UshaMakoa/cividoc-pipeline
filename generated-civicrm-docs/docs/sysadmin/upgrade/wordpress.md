---
title: Upgrade CiviCRM for WordPress
category: how-to
topic: system-administration
subtopic: wordpress-upgrades
component: CiviCRM for WordPress
audiences:
- technical
level: intermediate
journey_stage: manage-and-automate
summary: Upgrade a CiviCRM installation on WordPress to the latest CiviCRM release.
extensions: []
related:
- index.md#before-upgrading
- index.md#after-upgrading
review_priority: medium
review_notes:
- The localization instructions refer to a tar.gz file, but the download instructions specify a zip file; the relationship
  between these files is unclear.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: upgrade/wordpress.md
destination_path: sysadmin/upgrade/wordpress.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/upgrade/wordpress/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Upgrade CiviCRM for WordPress

Use this document to upgrade CiviCRM installations on WordPress to the latest CiviCRM release.

!!! caution "Before upgrading"
    Make sure you have done the steps listed in [before upgrading](index.md#before-upgrading) first.

## Download the latest code

1. Go to the [CiviCRM website](https://civicrm.org/download).
2. Select the latest currently available CiviCRM zip file for WordPress. For example: `civicrm-x.x.x-wordpress.zip`
3. Save this file in `<wordpress_root>/wp-content/plugins/`.

If using localization, also download the latest version of the localization files. See the [CiviCRM Localisation](https://lab.civicrm.org/dev/translation/-/wikis/Administrator-Guide) page about how to install files for running CiviCRM in languages other than American English.

## Prepare WordPress

Make sure you have logged in to WordPress as an administrator. Do not log out until the entire process is complete.

## Back up CiviCRM files and the database

1. Back up your existing `<wordpress_root>/wp-content/plugins/civicrm` directory by creating an archive or FTPing it to your local computer.
2. Back up your existing database using your Control Panel or other method so that you can recreate the database if required.
3. Find your `civicrm.settings.php` file. CiviCRM needs to use the `civicrm.settings.php` file during the upgrade. The default location is `<wordpress_root>/<content-dir>/uploads/civicrm/civicrm.settings.php`. If the file is there, proceed. If not, the settings file may be in its legacy location, `<wordpress_root>/wp-content/plugins/civicrm/civicrm.settings.php`. If you find it there, move it to `<wordpress_root>/<content-dir>/uploads/civicrm/civicrm.settings.php` and then proceed.
4. Check whether you are using a custom `settings_location.php` file at `<wordpress_root>/wp-content/plugins/civicrm/civicrm/settings_location.php`. If so, make a copy of this file; you will need to restore it after upgrading.

## Upgrade the filesystem

### Remove old CiviCRM files

CiviCRM will not run properly if files from a previous version are present after the upgrade.

1. Make sure you have a good backup of your complete previous version installation.
2. Delete `<wordpress_root>/wp-content/plugins/civicrm`.

### Install new CiviCRM files

Unpack the files:

```bash
$ cd <wordpress_root>/<content-dir>/plugins
$ unzip <civicrm_download_file>.zip
```

### Install localization files (optional)

There are two folders (`l10n` and `sql`) in the tar.gz file. Copy the whole `l10n` folder to `<wordpress_root>/wp-content/plugins/civicrm/civicrm/` (for example, via FTP). Note that `civicrm` appears twice in a row in this path.

Copy the *content* of the `sql` folder—or at least the 2 files referring to the language that you want to install CiviCRM in—into `<wordpress_root>/wp-content/plugins/civicrm/civicrm/sql/`. The `sql` folder is already there: copy the files into it, and do not replace the whole `sql` folder.

Note: If you are in the process of Installing CiviCRM you might need to deactivate the plugin and activate it again before you can select the new languages on the installer page in the WP backend.

### Clear cached files

Delete all files in your `<wordpress_root>/<content-dir>/uploads/civicrm/templates_c` directory and, if it exists, all files in `<wordpress_root>/<content-dir>/plugins/files/civicrm/templates_c`.

## Upgrade the database

1. Point your web browser to the following URL:

    ```
    http://example.org/wp-admin/admin.php?page=CiviCRM&amp;q=civicrm/upgrade&amp;reset=1
    ```

2. You should see the Upgrade screen.
3. If you are ready to upgrade, click the **Upgrade Now** button.
4. You should see the message **Upgrade successful** when the upgrade completes. If you receive any errors during the process, note down the exact error message and check for solutions on [Stack Exchange](https://civicrm.stackexchange.com/) or [Mattermost](https://chat.civicrm.org).
5. Click the **Return to CiviCRM home page** link. This will rebuild CiviCRM menus automatically and return you to the CiviCRM home dashboard.

## Post upgrade

See these steps to take [after upgrading](index.md#after-upgrading).

<!-- Source: upgrade/wordpress.md -->
