---
title: Install, upgrade, and uninstall extensions
category: how-to
topic: extensions
subtopic: installation-and-maintenance
component: CiviCRM extensions
audiences:
- technical
- administrator
- operations-user
level: intermediate
journey_stage: manage-and-automate
summary: Install extensions from available sources, upgrade them, and uninstall them.
extensions: []
related: []
review_priority: low
review_notes: []
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: customize/extensions-part2.md
destination_path: sysadmin/customize/extensions-part2.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/customize/extensions-part2/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# Install, upgrade, and uninstall extensions

## How to install an extension

You need to put the extension's code in a directory on your server configured for this purpose. You can see/change this from **Administer » System Settings » Directories**. Each extension lives in its own directory.

### Installing extensions that are available in-app

Clicking Install on one of the extensions listed from the **Administer » System Settings » Extensions** page will download the code to your extensions directory and then enable it.

This list is automatically downloaded from available and compatible native extensions on the CiviCRM server. To find out more about a specific extension, click the arrow on the left side of the extension name. This will reveal more details about this extension including the author, release version, release date and licensing.

The Manage Extensions function on your site lists and provides automatic installation only for extensions that:

- Are "native CiviCRM" extensions (not CMS specific)
- Have been "approved for automated distribution" by one of our moderators
- Have a "stable" release which is compatible with your version of CiviCRM

!!! note
    Systems Administrators need to know that for this to work, the extensions directory needs to be writable by the user that the webserver runs as (e.g. `www-data`)

### Installing from the command line

This process involves:

1. Getting the code.
   This is covered in the following two sections following,

2. Enabling the extension.
   Once the extension is in place you can either visit **Administer » System Settings » Extensions**, click Refresh, and then your extension should then be listed ready for you to click Install, or you can enable the extension from the command line using `cv en <EXTENSION_NAME>`.

A shortcut command line process is

```shell
cv dl <http://URL.zip>
```

This command will locate the appropriate location, download and unzip the code, and then enable the extension.

### Installing from a .zip file

For example, that you downloaded manually from *civicrm.org/extensions*. Simply unzip the file in your extensions directory to make it available to be enabled.

### Installing from a code repository (GitLab, CodeBerg, GitHub, ...)

Code repositories hold the source code for extensions as it changes over time ("version control"), and they usually offer a means to track bugs/issues and features to help co-ordinate teams of people working to improve the code. Most of them are based around a version control system (VCS) called Git.

They all share similar concepts. The best place to look for a .zip file you can download that bundles up all the files you need is the **Releases** page (sometimes you find this via a **Tags** page). Releases are deliberately published snapshots of the code, e.g. "version 1.2". It's important to grab a .zip from the releases page if you can because:

- The developer might have included some important information, such as version compatibility, change notes, warnings, stability notices or other important notes on the releases page that you might miss if just downloading the latest code. The latest version might require a different version of CiviCRM to yours.
- The .zip archives available from the releases pages might include files that are not to be found in the code repository itself (e.g. it might include 3rd party libraries.)

If there are no releases published and you want to try the code, these code repositories will offer a download button to download the latest version ("head" of a "main" or "master" branch) of the code, but it's much safer to use a published release whenever possible.

If you're a developer wanting to work on the code, or you just prefer to use `git` on the commandline to manage your extensions, you probably know that you can `git clone <URL>` to get the source code, and to read the README or other instructions in case there are further steps (e.g. to bring in 3rd party dependencies).

## Upgrading extensions

Extensions upgrades require replacing the current code with new code, and then, where necessary, applying database upgrades.

!!! tip
    Because upgrading extensions may change your database, it's a good idea to backup your database before applying upgrades, and ideally try the upgrade on a test copy of your CiviCRM instance before applying on your production/live server.

If new version of an extension installed in your system and published on *civicrm.org/extensions* becomes available, you will see an "Upgrade" link next to it. Clicking this will upgrade the extension's source code and if there are database changes required an alert will provide a link for you to click to apply them as well. All done!

!!! warning
    If you installed an extension published on civicrm.org/extensions but you did so from the commandline, there is a chance that the in-app upgrade fails due to file permissions. Read on.

### Upgrading extensions installed from the command line

Replace the extension's code (by downloading a new .zip and replacing the original directory with the unzipped new archive, or using git pull/merge/checkout), then run `cv ext:upgrade-db` to do the database migrations.

## Uninstalling extensions

In order to uninstall extension, you need to disable it first - once disabled, you will see the "Uninstall" link. Click it in order to completely remove the extension from your system, including permanent deletion all of its custom data. To preserve the data, take a backup before uninstalling.

<!-- Source: customize/extensions-part2.md -->
