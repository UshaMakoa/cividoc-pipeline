---
title: Drupal to Backdrop
category: how-to
topic: system-administration
subtopic: switching-cms
component: CiviCRM Core
audiences:
- technical
- administrator
- operations-user
level: basic
journey_stage: everyday-tasks
summary: For some use cases, instead of a Drupal 7 to Drupal 8 migration, a migration from Drupal 7 to Backdrop is a great
  alternative.
extensions: []
related: []
review_priority: low
review_notes: []
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: misc/switching-cms/drupal-to-backdrop.md
destination_path: sysadmin/misc/switching-cms/drupal-to-backdrop.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/misc/switching-cms/drupal-to-backdrop/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Drupal to Backdrop

For some use cases, instead of a Drupal 7 to Drupal 8 migration, a migration from Drupal 7 to Backdrop is a great alternative.

## Methods

There are several methods you can use, including:

1) If you have Drupal 7 content you want to preserve (including webforms and views) then clone your D7 site and follow the [Upgrading from Drupal 7](https://backdropcms.org/upgrade-from-drupal) guide on the Backdrop website.  This will preserve your content, users, passwords, permissions etc.  You will need to do some work on Layouts since these are a change from D7 and control how content is presented.

2) If your Drupal 7 site is nothing more than a shell for holding CiviCRM then you might prefer to do a fresh installation of Backdrop and CiviCRM then import a dump from your old CiviCRM database. You will need to set up users, passwords, permissions from scratch which is more work but maybe it's time for a review of those anyway!

If CiviCRM is in a separate database from Drupal then you can point to this from your new Backdrop site.

## Method 1 - upgrade from Drupal

Follow the [Upgrading from Drupal 7](https://backdropcms.org/upgrade-from-drupal) guide on the Backdrop site.  Some common Drupal modules are in Backdrop core, others are replaced by Backdrop equivalents.  The details look tedious but the [backdrop_upgrade_status](https://www.drupal.org/project/backdrop_upgrade_status/releases/7.x-1.3) module makes this much easier.  Install this on your existing Drupal site and it will tell you what to do with each module and provide download links where appropriate.

Treat CiviCRM like other modules - ie replace the Drupal version of the CiviCRM core code with the equivalent Backdrop version.

Make sure you copy or move the `files` directory from your D7 site. By default, it has a different location.  See the options discussed [here - Step 5](https://docs.backdropcms.org/documentation/step-3-upgrade-the-drupal-site).

CiviCRM provides a Layout suitable for CiviCRM pages.  If you do not see `Default CiviCRM Layout` under **Structure > Layouts** then disable, uninstall and reinstall the `civicrmtheme` module from **Functionality > List Modules**.

## Method 2 - install to new or existing Backdrop

### Preparing for the Migration

* Backup the CiviCRM database that was set up for Drupal.
* Backup the Backdrop site before making any changes to it.
* Set up CiviCRM in your Backdrop site

    !!! check
            When downloading the CiviCRM package get the same version of the CiviCRM package for Backdrop as the version you used in Drupal. If you want to upgrade to a newer version of CiviCRM, upgrade it before or after – not during – the migration.

    Refer to the [Backdrop Installation Guide](https://docs.civicrm.org/installation/en/latest/backdrop/) for details on obtaining and setting up CiviCRM for Backdrop.

### Relocate Custom Files

* Copy any extension directories from the previous Drupal directory to the new Backdrop directory at `<backdrop_root>/files/civicrm/ext`
* Copy any sensitive uploads/attachments from the previous Drupal directory to the new Backdrop directory at `<backdrop_root>/files/civicrm/custom`
* Copy any template overrides from the previous Drupal directory to the new Backdrop directory at `<backdrop_root>/files/civicrm/templates`
* Copy any uploaded media from the previous Drupal directory to the new Backdrop directory at `<backdrop_root>/files/civicrm/persist`

### Restore the CiviCRM database backup to the desired location

* The installation process would have set up new database tables for CiviCRM. If this is where you want your CiviCRM database to be, then you may overwrite these tables by restoring your old database over it.
* Alternatively you can restore your CiviCRM database somewhere else and modify **CIVICRM_DSN** in `<backdrop_root>/civicrm.settings.php` to point to this new database.

### Empty the `civicrm_uf_match` table

This table is used for mapping your CMS users with CiviCRM contacts. At this stage those mappings will be according to users from your Drupal site. You will need to delete these mappings so that Backdrop can then automatically rebuild them from the new users table.

``` sql
TRUNCATE TABLE `<civicrm_database>`.`civicrm_uf_match`;
```

### Update the Directory Path and URL

* Log in to Backdrop with a username that has administrator access to CiviCRM
* Go to **http://example.org/civicrm/admin/setting/updateConfigBackend?reset=1**
    * Set your base directory to `<backdrop_root>/files/`
    * Ensure your base URL is correct
    * Click **Save**

### Update the Resource URLs

Up to this stage, CiviCRM screens are missing all of its CSS formatting and images because the paths to these resources are incorrect. This step is to set the correct paths to these resources.

* Go to http://example.org/civicrm/admin/setting/url?reset=1
    * Set CiviCRM Resource URL to `[civicrm.root]/`
    * Set Image Upload URL to `[civicrm.files]/persist/contribute/`
    * Set extension Resource URL to `[cms.root]/civi/extensions/`
    * Click **Save**

### Rebuild the menus

The menu links in the `civicrm_menu` table contain full URL links and need to be updated with the new domain. Navigate to _http://example.org/civicrm/admin/menu/rebuild&reset=1_

### Disable MultiViews

If menus still don't appear, try adding this line to the `.htaccess` file at the webroot:

```
Options -MultiViews
```

### Review other Admin settings

As a result of your migration, many of your site's other configuration settings have been reset, for instance Available Countries in "Localization" and reCaptcha keys. Page through the _Configuration Checklist_ at **Administer > Administration Console > Configuration Checklist** to be sure that all your settings are once again set to their correct values.

## If your URL has changed

If your URL has changed, please review the documentation on [this page](../switch-servers.md) under the heading "Additional Steps if your URL has changed".

<!-- Source: misc/switching-cms/drupal-to-backdrop.md -->
