---
title: Install CiviCRM on Joomla
category: how-to
topic: installation
subtopic: standard-installation
component: CiviCRM for Joomla
audiences:
- technical
- administrator
level: intermediate
journey_stage: plan-and-configure
summary: Install CiviCRM on an existing Joomla site and synchronize existing Joomla users with CiviCRM contacts.
extensions: []
related:
- ../requirements/index.md
- ../troubleshooting/index.md
review_priority: medium
review_notes:
- The installer menu path and the register_globals configuration examples may be outdated; verify them before updating these
  instructions.
- The troubleshooting instruction to delete `~/media/civicrm directories` is unclear and has been left unchanged.
guide: installation
source_repository: https://lab.civicrm.org/documentation/docs/installation.git
source_path: joomla/index.md
destination_path: installation/joomla/index.md
legacy_urls:
- https://docs.civicrm.org/installation/en/latest/joomla/
civicrm_version:
- latest
source_commit: 5a8b870477f63bea90551acb2f7516df67784b19
last_modified: '2026-08-20'
---

# Install CiviCRM on Joomla

This guide covers standard installation of CiviCRM on an existing Joomla site. Before you begin:

1. [Install Joomla](https://docs.joomla.org/J4.x:Installing_Joomla).
2. [Review the CiviCRM requirements](../requirements/index.md).

!!! note "Path for Joomla"
    The instructions assume that you have Joomla installed in `/var/www/JOOMLA_ROOT`. Adjust paths as needed.

## Get the code {:#download}

All CiviCRM code and packages used by CiviCRM, such as PEAR libraries, are included in the compressed CiviCRM distribution files (“tarballs”).

1. Download the appropriate tarball from the [CiviCRM website](https://civicrm.org/download) in your browser. Tarball file names include the CiviCRM version; for example, `civicrm-x.x.x-joomla.zip`. If you have command line access to your server, you can use `wget` and the URL of the file to pull a copy directly to your server. Then skip the next step.
2. Upload the file to a folder in your root Joomla directory. The recommended location is `JOOMLA_ROOT/tmp/`.
3. Unzip the package to create a directory called `com_civicrm`. On cPanel, you can use the File Manager’s Extract function to unzip the file you uploaded.

When installing a new version over an old one, first check the [troubleshooting resources](#troubleshooting) below.

## Run the installer {:#installer}

1. Log in to your Joomla Administrator site.
2. Go to **Extensions >> Install/Uninstall**.
3. Use **Install from Directory** and enter the full path to the unzipped `com_civicrm` directory, which should be something like `JOOMLA_ROOT/tmp/com_civicrm`. In most Joomla installations, the root directory and /tmp/ folder will already populate the “install from directory” field. Add the /com_civicrm/ subfolder at the end, then click Install. If that does not work, enter the full file system path to `com_civicrm`, such as `/var/www/JOOMLA_ROOT/tmp/com_civicrm/`.
4. You should see a “Component successfully installed” message.

!!! warning
    If you get the following error when installing or upgrading CiviCRM for Joomla, download the alternate Joomla install file, `civicrm-x.x.x-joomla-alt.zip`, which does not require built-in unzip functionality on your server. Then repeat the install steps starting with [running the installer](#installer).

    > Your PHP version is missing zip functionality. Please ask your system administrator / hosting provider to recompile PHP with zip support.

    Missing PHP Zip functionality *will* prevent CiviCRM from installing extensions via the GUI.

## Synchronize the users {:#contacts-users}

Once installed, CiviCRM keeps your Joomla Users synchronized with corresponding CiviCRM contact records. There will be a matched contact record for each Joomla user record. Conversely, only contacts who are authenticated users of your site will have corresponding Joomla user records.

When CiviCRM is installed on an existing Joomla site, a CiviCRM Administrative feature lets you create CiviCRM contacts for all existing Joomla users:

1. Log in to your Joomla site with an administrator-level login.
2. Click the **Components > CiviCRM > CiviCRM Home** link in the main navigation block.
3. Click **Administer > Users and Permissions > Synchronize Users-to-Contacts**.

## Troubleshooting {:#troubleshooting}

- If the CiviCRM component does not install correctly—for example, you get a blank screen instead of the confirmation page—delete the `~/components/com_civicrm` and `~/administrator/components/com_civicrm` and `~/media/civicrm directories` manually. Then try each of the following before attempting to reinstall:

    - In your `php.ini` file or in `.htaccess` in the Joomla root folder, if your server allows it, increase `max_execution_time` to `600` and the memory limit to more than 64M. Add the following to the `.htaccess` file in your Joomla root folder:

      <!-- markdownlint-disable MD046 -->
      ``` htaccess
      php_value memory_limit 128M
      php_value register_globals off
      php_value max_execution_time 600
      ```

      If you cannot change `.htaccess`, you can add a php.ini (or `.user.ini`) file in the Joomla root folder or all directories, depending on your web server or hosting company:

      ``` ini
      memory_limit = 128M
      register_globals = off
      max_execution_time = 600
      ```
      <!-- markdownlint-enable MD046 -->

    - CiviCRM is packaged with all the libraries, including PEAR, that it uses. However, a misconfigured or overly restrictive `open_basedir` directive on your web server might interfere with CiviCRM’s ability to access required files or directories. To turn `open_basedir` off, add `php_admin_value open_basedir none` to your `vhost.conf` file. Alternatively, ask your host to turn it off or ensure that it does not prevent access to required directories—for example, if you move configuration files or temp folders outside your web root. The configuration of sub domains might cause related issues: try installing in the main domain root or a sub folder instead.

- If CiviCRM screens are not displaying properly or javascript widgets are not functioning, check your CiviCRM Resource URL (**Administer >> System Settings >> Resource URLs**). For Joomla installs, it should be something like `http://example.org/administrator/components/com_civicrm/civicrm`.

- Review the [Troubleshooting](../troubleshooting/index.md) page for help with problems you may encounter during installation.

<!-- Source: joomla/index.md -->
