---
title: Upgrading CiviCRM for Joomla
category: how-to
topic: system-administration
subtopic: upgrade
component: CiviCRM Core
audiences:
- technical
- administrator
- operations-user
level: basic
journey_stage: everyday-tasks
summary: Use this document to upgrade CiviCRM installations on Joomla to the latest CiviCRM release.
extensions: []
related: []
review_priority: low
review_notes: []
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: upgrade/joomla.md
destination_path: sysadmin/upgrade/joomla.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/upgrade/joomla/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Upgrading CiviCRM for Joomla

Use this document to upgrade CiviCRM installations on Joomla to the latest CiviCRM release.

!!! caution "Before upgrading"
    Make sure you have done the steps listed in [before upgrading](index.md#before-upgrading) first.

!!! bug "Known Issues"
    If using a version prior to 4.7.29 you need to apply the following two PRs after installation but before running the upgrader:

    * [#11062](https://github.com/civicrm/civicrm-core/pull/11062) (If using Joomla > 3.8.1 otherwise CRON/CLI won't work).
    * [#11236](https://github.com/civicrm/civicrm-core/pull/11236) (If using Paypal IPN).

## Download the latest code

1. Go to the [CiviCRM website](https://civicrm.org/download)
1. Select the latest currently available CiviCRM tarball for Joomla.

    Example: `civicrm-x.x.x-joomla.zip`

    !!! note
        You may notice a file on the named something like `civicrm-x.x.xx-joomla-alt.zip` the `-alt` version does not require `.zip` functions compiled into PHP by your hosting company. If you get errors like _"Your PHP version is missing zip functionality"_, then try the `-alt` version.

1. Save this file in `<joomla_root>/tmp/`.
1. Unzip and check that it created a directory called `com_civicrm` in `<joomla_root>/tmp`.

## Backup your settings files

The [before upgrading](index.md#before-upgrading) steps describe steps for backing _everything_ up in case something goes wrong during the upgrade.  In particular, note that Joomla has two settings files for CiviCRM and they should both be backed up:

* `<joomla_root>/components/com_civicrm/civicrm.settings.php`
* `<joomla_root>/administrator/components/com_civicrm/civicrm.settings.php`

Copy these files to a location outside your Joomla project.

## Install the Extension

1. Login to your Joomla Administrator site.
1. From the menu choose Extensions » Manage » Install
1. Use the **Install from Folder** tab and enter the full path to the un-zipped **com_civicrm** directory, which should be something like **JOOMLA.x_ROOT/tmp/com_civicrm**. If your temp directory is configured correctly you should only need to add "com_civicrm" to the prepopulated path.
1. You should see "CiviCRM successfully installed" message.

The steps above will install CiviCRM directly on top of your existing installation, overwriting existing files. This means that files from previous releases that are no longer required are not removed.  Generally this is not a problem but it can cause failures. If this happens you can either:

* Find and manually remove the outdated files.  Check on StackExhange or Chat to see if others are reporting the same problem.  The CiviCRM log may indicate which files are causing the problem, or you can look at the modification timestamp of the files.  Obviously keep a copy of anything you remove in case you need to revert.
* Uninstall and reinstall CiviCRM.  This will not affect your CiviCRM data but:

    1. You will need to save your two `civicrm.settings.php` files before you uninstall, then copy them back after reinstalling.
    1. It will reset all the CiviCRM permissions assigned to your Joomla groups.  Make a record of those first so you can reapply them.  If however you didn't do that and are now regretting it, you can reload a backup of your Joomla database, or [start again from the settings](https://docs.civicrm.org/user/en/latest/initial-set-up/permissions-and-access-control/#anonymous-and-authenticated-roles).

## Update localisation files
1. If using localization, also download the latest version of the localization files. See the [CiviCRM Localisation](https://wiki.civicrm.org/confluence/display/CRMDOC/i18n+Administrator%27s+Guide%3A+Using+CiviCRM+in+your+own+language) page about how to install files for running CiviCRM in languages other than American English.

    Go to `<joomla_root>/administrator/components/com_civicrm` and extract `civicrm-x.x.x-l10n.tar.gz`

## Clear the file cache

Delete all cache files in `<joomla_root>/media/civicrm/templates_c` on your server before proceeding with the update script.

## Upgrade the database

**After the component installation completes click the link to run the database upgrade script.** You may also point your web browser to the following URL (you should already be logged in to Joomla with administrator-level permissions):

```
http://example.org/administrator/index.php?option=com_civicrm&task=civicrm/upgrade&reset=1
```

You should see an **Upgrade successful** message when the upgrade completes.

1. If you receive any errors during the process, please note the exact error message and check for solutions on [Stack Exchange](https://civicrm.stackexchange.com/) or [Mattermost](https://chat.civicrm.org).
1. Now click the **Return to CiviCRM home page** link.
1. You should be up and running with the latest CiviCRM version. Confirm by checking the version and revision in the page footer. Note that you may need to refresh the browser screen a couple times to clear out your local cache and ensure the layout loads correctly.
1. Take some time to browse the CiviCRM features that your organization uses. If you notice unexpected behaviors or error messages, refer to the trouble-shooting section below.

## Restore settings file changes

Review the backup versions of the files below and compare them with the new versions just installed. In particular, make sure your site key value was retained and any of the configuration options found in those files are still intact.

1. <joomla_root>/components/com_civicrm/civicrm.settings.php
1. <joomla_root>/administrator/components/com_civicrm/civicrm.settings.php

## Post upgrade

See these steps to take [after upgrading](index.md#after-upgrading).

<!-- Source: upgrade/joomla.md -->
