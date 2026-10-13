---
title: Install CiviCRM on WordPress
category: how-to
topic: installation
subtopic: standard-installation
component: CiviCRM on WordPress
audiences:
- technical
- administrator
- operations-user
level: intermediate
journey_stage: plan-and-configure
summary: Install CiviCRM on an existing WordPress site, then back up its settings file and review the new installation.
extensions: []
related:
- ../requirements/index.md
- ./composer.md
- ../general/permissions.md
- ../general/mysql_tls.md
- ../troubleshooting/index.md
review_priority: medium
review_notes:
- The translation-files sentence has malformed link syntax; it is preserved for review.
- The source questions whether its settings-file backup guidance applies to newer installations; the guidance is preserved
  for review.
- The installer instructions refer to version 4.7 and above and describe both clicking the install button and rechecking requirements
  before continuing; this sequence is preserved for review.
guide: installation
source_repository: https://lab.civicrm.org/documentation/docs/installation.git
source_path: wordpress/index.md
destination_path: installation/wordpress/index.md
legacy_urls:
- https://docs.civicrm.org/installation/en/latest/wordpress/
civicrm_version:
- latest
source_commit: 5a8b870477f63bea90551acb2f7516df67784b19
last_modified: '2026-08-20'
---

# Install CiviCRM on WordPress

???+ tldr "About this document"

    This guide covers standard installation of CiviCRM on an existing WordPress site. It assumes that you previously completed these tasks:

    1. [Install WordPress](https://wordpress.org/support/article/how-to-install-wordpress/), and...
    1. [Review the CiviCRM requirements](../requirements/index.md)

??? tldr "Alternative: Composer based installation"

    As of CiviCRM 6.16 you can optionally use [composer](https://getcomposer.org/) to download CiviCRM with Wordpress. See [details](./composer.md).

??? tldr "Alternative: Civibuild for developers"

    If you plan to develop patches for CiviCRM on WordPress, then please read the [Developer Guide](https://docs.civicrm.org/dev/en/latest) for information about [Buildkit](https://docs.civicrm.org/dev/en/latest/tools/buildkit/) and [civibuild](https://docs.civicrm.org/dev/en/latest/tools/civibuild/).

!!! note "Path for WordPress"
    The rest of these instructions assume that you have WordPress installed in `/var/www/wordpress`. Adjust paths as needed.

## Get the code {:#download}

All CiviCRM code and packages used by CiviCRM (such as PEAR libraries) are included in the compressed CiviCRM distribution files ('zips'). Follow these steps to download and install the codebase:

1. Download the appropriate zip file from the [CiviCRM website](https://civicrm.org/download) with your browser. The zip file-names include the CiviCRM version. For example, **civicrm-x.x.x-wordpress.zip.**

2. Copy or ftp the zip file to your WordPress installation's `/wp-content/plugins` directory. You may have to change the "File Permissions" setting of `/wp-content/plugins/civicrm` directory to allow for "Write" Access. Just remember to change it back to default when done.

    You can upload the zip file that was downloaded via your WordPress admin panel at `wp-admin/plugin-install.php`

    !!! information "Downloading Directly to Your Server with wget"
        If you have command-line access, you may prefer to download the zip file directly to your server using wget:

        1. Move into WordPress's plugin directory

            ``` bash
            cd /var/www/wordpress/wp-content/plugins
            ```

        1. wget the file (modify this line to use the current zip file name for the version you want)

            ``` bash
            wget https://download.civicrm.org/civicrm-x.x.x-wordpress.zip
            ```

3. Extract (aka: unzip, unpack) the codebase into the wordpress/wp-content/plugins directory.

    1. Move to the wordpress/wp-content/plugins directory (if not already there)

        ``` bash
        cd /var/www/wordpress/wp-content/plugins
        ```

    1. Un-zip the file (modify this line with the actual downloaded filename)

        ``` bash
        unzip civicrm_download_file.zip
        ```

You should now have a `/var/www/wordpress/wp-content/plugins/civicrm` directory containing `civicrm.php`, `README.txt` and another civicrm directory (which in turn contains bin, CRM, sql, templates, etc.).

## Get the translations {:#i18n}

The basic CiviCRM release includes support for US English (`en_US`). To use another language or dialect, please [download and extract the translation files. A guide to help install these can be found [in the System Administration Guide](https://docs.civicrm.org/sysadmin/en/latest/upgrade/wordpress/#install-localization-files-optional).

## Run the installer

The installer will verify that you've downloaded the correct version of CiviCRM, and will check your server environment to make sure it meets CiviCRM requirements. It will then create and populate a database for CiviCRM as well as create your CiviCRM settings file `civicrm.settings.php`.

1. Login to your WordPress site with Administrator level permissions.

2. Go to plugins page: `https://example.org/wp-admin/plugins.php`.

3. Click the **Activate** link to activate the CiviCRM plugin.

4. Then go to **Settings > CiviCRM Installer**: `https://example.org/wp-admin/options-general.php?page=civicrm-install`

    In version 4.7 and above you will see a link on the wp-admin page to the Installer screen.

5. You should see the **CiviCRM Installer** screen.

    If you see any errors, check the **Requirements** details at the bottom of the page for more information. You will need to correct any issues before continuing.

6. CiviCRM Database Settings.

    Initially, the installer will default to using the existing WP database for the CiviCRM data. You can change this if you require.

    !!! tip "Where Should I Store CiviCRM Data?"
        CiviCRM may be configured to use your existing WordPress database, or a separate (new) database. Using a separate database is generally preferred - as it makes backups and upgrades easier. The installer will create a new database for CiviCRM automatically if you enter a database name that doesn't already exist on your database server AND the database user you enter has permission to create databases. In case the installer does not automatically create a new database, simply create a new one following the same process as creating a new database for WordPress.

7. Fill in the WordPress Database Settings for your existing WordPress database. CiviCRM will fill in the WP database settings, you can change these if you want to use a separate database.

    !!! tip "Loading Sample Data"
        The Installer includes an option to load a set of sample contact, group, and relationship data by default. Sample data can provide a useful head-start in learning to use CiviCRM. However, if you do NOT want the sample data to be loaded, just uncheck **Load sample data** under **Other Settings**.

8. Select the appropriate language for the base installation. You will be able to add other languages after the installation for multi-lingual sites.

9. Click the **Check Requirements and Install CiviCRM** button.

    - The installer will configure your databases, create the settings file and will redirect to success message.
    - If you still see a red bar with the message "These database details don't appear to be correct." - check the Database Details section below your settings for specific errors and problems. Once you correct these problems, click "Recheck requirements" to verify your settings before continuing.
    - If you are on a Windows machine and get the message:
        > "The user account used by your web-server needs to be granted write access to the following directory in order to configure the CiviCRM settings file: `C:<wordpress path>/wp-content/plugins/civicrm/`"
        even after changing directory permission in Explorer, see [the permissions page](../general/permissions.md) for instructions on how to set permissions on Linux, MacOS and Windows.
    - Once you see the green "You're ready to install!" message - you can click **Check Requirements and Install CiviCRM**

## Backup the settings file

The installer created a configuration file at `<wordpress>/wp-content/uploads/civicrm/civicrm.settings.php`

It is critical you make a copy of this file and save as a backup in a safe location. This file contains passwords and other critical information, take precautions to secure the copy from prying eyes.

Should an upgrade fail, you will need this backup copy to restore your site.

## Synchronize the users {:#contacts-users}

Once installed, CiviCRM keeps your WordPress Users synchronized with corresponding CiviCRM contact records. The 'rule' is that there will be a matched contact record for each WordPress user record. Conversely, only contacts who are authenticated users of your site will have corresponding WordPress user records.

When CiviCRM is installed on top of an existing WordPress site, a special CiviCRM Administrative feature allows you to automatically create CiviCRM contacts for all existing WordPress users:

1. Login to your WordPress site with an administrator-level login
2. Click the **CiviCRM** link in the main navigation block
3. (If your WordPress site makes use of the `db_prefix` setting (in `settings.php`), in de top bar click **Administer » System Settings » CMS Database Integration** , and update the box for the WordPress Users Table Name so that it includes the prefix.)
4. Click **Administer** in the menu bar
5. Click **Users and Permissions** from the drop-down menu, then select **Synchronize Users to Contacts**.

## Review the checklist {:#checklist}

The **Configuration Checklist** provides a convenient way to work through the settings that need to be reviewed and configured for a new site. You can link to this checklist from the installation success page AND you can visit it at any time from **Administer** » **Administration Console** » **Configuration Checklist**.

## Test-drive CiviCRM

There should now be a **CiviCRM** link in your WordPress menu. Click that link and the CiviCRM Menu, Shortcuts, Search and New Individual Blocks should appear. You can now explore CiviCRM end-user features and begin configuring CiviCRM for your site/organization needs.

## Addenda

### TLS for MySQL

If your MySQL database is hosted on a different machine than your web server, or if your host requires it, you can use TLS to encrypt the connection between the database and the web server.

See [TLS for MySQL](../general/mysql_tls.md) for introductory concepts and the settings for the CiviCRM database. For the Wordpress database you can add the following line to wp-config.php:

* `define('MYSQL_CLIENT_FLAGS', MYSQLI_CLIENT_SSL);`

### Troubleshooting {:#troubleshooting}

* Review the [troubleshooting](../troubleshooting/index.md) page for help with problems you may encounter during the installation.

<!-- Source: wordpress/index.md -->
