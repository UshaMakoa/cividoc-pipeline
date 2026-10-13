---
title: Install CiviCRM on Drupal
category: how-to
topic: installation
subtopic: composer-installation
component: CiviCRM for Drupal
audiences:
- technical
- administrator
- operations-user
- communications-manager
level: intermediate
journey_stage: plan-and-configure
summary: Install CiviCRM on Drupal and review the post-installation settings.
extensions: []
related: []
review_priority: medium
review_notes:
- The permissions tip says permissions are enabled during installation but also instructs readers to enable individual permissions;
  the intended default state is unclear.
guide: installation
source_repository: https://lab.civicrm.org/documentation/docs/installation.git
source_path: drupal/index.md
destination_path: installation/drupal/index.md
legacy_urls:
- https://docs.civicrm.org/installation/en/latest/drupal/
civicrm_version:
- latest
source_commit: 5a8b870477f63bea90551acb2f7516df67784b19
last_modified: '2026-08-20'
---

# Install CiviCRM on Drupal

CiviCRM tries to follow Drupal community's decisions around which versions of Drupal receive support. The current supported versions are Drupal 10 and Drupal 11, simply called "Drupal" from here on.

Before starting, you must have completed these tasks:

1. [Installed Drupal](https://www.drupal.org/docs/getting-started/installing-drupal) and...
1. [Reviewed the CiviCRM requirements](../requirements/index.md)

Drupal 7 is now officially End of Life and is *not recommended for new sites*. Instructions for installing CiviCRM on Drupal 7 have now been [archived](../archive/drupal7.md).

## Get the code for Drupal {:#drupal-download}

Drupal's code base is handled by [Composer](https://getcomposer.org), a *dependency management* tool which can add, upgrade and remove software *packages* for your site. Composer is included in [DDEV](https://www.drupal.org/docs/getting-started/installing-drupal/install-drupal-using-ddev-for-local-development), the recommended tool for local Drupal development.

If Composer is properly installed, then the example commands below will add latest CiviCRM version to Drupal.

!!! warning "Install CiviCRM before Drush"
    You need to install CiviCRM packages before installing Drush to avoid dependency issues with `symfony/finder` or `symfony/filesystem`. Remove Drush if it's already installed, install CiviCRM, and then re-install Drush.

Run these commands inside your Drupal installation:

```
cd /var/www/drupal.example.org
composer config extra.enable-patching true
composer require civicrm/civicrm-{core,packages,drupal-8}
composer require civicrm/cli-tools
```

??? info "More detail: Enable patching"

    A handful of packages used by CiviCRM require extra patch-files.

    This is possible with the popular [cweagans/composer-patches](https://github.com/cweagans/composer-patches) plugin. However, you must [opt-in to enable it](https://github.com/cweagans/composer-patches/tree/1.x#allowing-patches-to-be-applied-from-dependencies) during the installation above, when it asks `Do you trust "cweagans/composer-patches" to execute code and wish to enable it now?`.

## Install CiviCRM

### Install CiviCRM in a shared database

We use the command line tool `cv` to install the CiviCRM Core and CiviCRM Theme modules, and create the required tables in Drupal's database.

By default, new installations of CiviCRM will copy the MySQL connection details from the CMS, creating a shared database, which is the simplest method.

It is also possible to install CiviCRM in a [separate database](https://docs.civicrm.org/installation/en/latest/general/requirements/#mysql-connection), see below.

This command installs CiviCRM:

`cv core:install --cms-base-url="https://drupal.example.org"`

To run in [DDEV](https://ddev.readthedocs.io/), prepend the command with `ddev exec`.

### Install in a separate database

Change the following in the command below:

* `https://drupal.example.org` change this to your civicrm url
* `database_user` change this to your database user
* `database_pass` change this to the password of your database user
* `civicrm_database` change this to name of your civicrm database

```
cv core:install --cms-base-url="https://drupal.example.org" --db="mysql://database_user:database_pass@localhost:3306/civicrm_database"
```

### Install a translated CiviCRM {:#i18n}

To install a translated CiviCRM on Drupal requires the following first downloading the translation files.

Change the following in the command below:

* `nl_NL` to your language, e.g. fr_FR, or nl_BE etc...
* `https://drupal.example.org` change this to your civicrm url
* `database_user` change this to your database user
* `database_pass` change this to the password of your database user
* `civicrm_database` change this to name of your civicrm database

```
mkdir -p web/sites/default/files/civicrm/l10n/nl_NL/LC_MESSAGES
curl -Lss -o web/sites/default/files/civicrm/l10n/nl_NL/LC_MESSAGES/civicrm.mo https://download.civicrm.org/civicrm-l10n-core/mo/nl_NL/civicrm.mo
export CIVICRM_L10N_BASEDIR=/var/www/drupal.example.org/web/sites/default/files/civicrm/l10n
cv core:install --cms-base-url="https://drupal.example.org" --db="mysql://database_user:database_pass@localhost:3306/civicrm_database" --lang="nl_NL"
```

## Troubleshooting {:#troubleshooting}

* Review the [Troubleshooting](../troubleshooting/index.md) page for help with problems you may encounter during the installation.

## Post-installation {:#post-install}

Recommended steps to perform after installing CiviCRM on Drupal.

### Review the permissions {:#permissions}

!!! note ""
    Drupal will create the `/files/` directory (and make it writeable), but only when saving `admin/settings`. Same holds for `/temp` directory, and a `/uploads/` directory in the CiviCRM module root. On a brand-new Drupal install, this directory may be missing. Even on an existing installation, if file permissions are not set properly, the directory may be missing. If enabling the **CiviCRM** module generates errors regarding the files directory, you must create it (writeable) manually.

* Go to the CiviCRM dashboard to see the CiviCRM menus:
  `https://example.org/civicrm` (or `https://example.org/index.php?q=civicrm` if you don't have Clean URLs enabled)
* Go to **Administer » User management » Permissions**
* Verify that the Roles that you want to have access to CiviCRM have the appropriate permissions checked. CiviCRM is installed with a number of fixed permissions (such as "edit contacts" and "administer CiviCRM").

!!! tip "Permissions for the Anonymous Role"
    Many sites want anonymous visitors to have access to certain CiviCRM functionality. These permissions are enabled during installation for the Anonymous role. You should review them and modify if needed based on your requirements:

    * **access all custom data** : If you plan on collecting "custom" data from visitors in standalone forms or as they make a contribution - enable this permission.
    * **access CiviMail subscribe/unsubscribe pages** : If you are planning on using CiviMail, enable this permission to allow anonymous users to subscribe and unsubscribe from mailing lists via the web.
    * **access uploaded files** : If you plan on allowing visitors to upload or view photos or other files - enable this permission.
    * **make online contributions** : If you plan on soliciting online contributions from visitors, enable this permission for the "anonymous" role.
    * **profile listings and forms** : If you plan on collecting name and address or other information from visitors, enable this permission for the "anonymous" role.
    * **view event info** and **register for events** : If you plan to use CiviEvent and want to allow un-authenticated visitors to view event information and register for events online - enable these permissions for the "anonymous" role.
    * **view event participants** : Enable this permission to allow anonymous users to access participant listing pages for events.

### Synchronize the users {:#contacts-users}

Once installed, CiviCRM keeps your Drupal Users synchronized with corresponding CiviCRM contact records. The 'rule' is that there will be a matched contact record for each Drupal user record. Conversely, only contacts who are authenticated users of your site will have corresponding Drupal user records.

When CiviCRM is installed on top of an existing Drupal site, a special CiviCRM Administrative feature allows you to automatically create CiviCRM contacts for all existing Drupal users:

1. Login to your Drupal site with an administrator-level login
1. Click the **CiviCRM** link in the main navigation block
1. If your Drupal site makes use of the `db_prefix` setting (in `settings.php`), in the top bar click **Administer » System Settings » CMS Database Integration** , and update the box for the Drupal Users Table Name so that it includes the prefix.
1. Click **Administer** in the menu bar
1. Click **Users and Permissions** from the drop-down menu, then select **Synchronize Users to Contacts**

### Review the checklist {:#checklist}

The **Configuration Checklist** provides a convenient way to work through the settings that need to be reviewed and configured for a new site. You can link to this checklist from the installation success page and you can visit it at any time from **Administer** » **Administration Console** » **Configuration Checklist**.

### Test-drive CiviCRM {:#test-drive}

There should now be a **CiviCRM** link in your Drupal menu. Click that link and the CiviCRM Menu, Shortcuts, Search and New Individual Blocks should appear. You can now explore CiviCRM end-user features and begin configuring CiviCRM for your site/organization needs.

## Addenda

### TLS for MySQL

If your MySQL database is hosted on a different machine than your web server, or if your host requires it, you can use TLS to encrypt the connection between the database and the web server.

Full instructions on installing drupal are out of scope for this guide, but one method is to install into a test database first without MySQL encryption and then move the database to the live server and update settings.php to enable MySQL encryption.

See [TLS for MySQL](../general/mysql_tls.md) for introductory concepts and the settings for the CiviCRM database. For the Drupal database you have several options for updating settings.php:

1. The simplest, which doesn't require a client certificate, but doesn't verify the server certificate.

    ``` php
    $databases = array (
      'default' =>
      array (
        'default' =>
        array (
          'database' => 'drupal',
          'username' => 'dbuser',
          'password' => 'dbpassword',
          'host' => 'db435.examplehost.com',
          'port' => '',
          'driver' => 'mysql',
          'prefix' => '',
          'pdo' => array(
              PDO::MYSQL_ATTR_SSL_CA => TRUE,
              PDO::MYSQL_ATTR_SSL_VERIFY_SERVER_CERT => FALSE,
          ),
        ),
      ),
    );
    ```

2. Verifies the server certificate, and doesn't require a client certificate.

    !!! warning "Host name must match certificate name"
        Note that the DATABASE SERVER certificate would have to have a CN (common name field) that matches exactly the `host` you are using in `$databases['default']['default']['host']`. So if the host is `db435.examplehost.com`, then that must be the name on the SERVER certificate.

    ``` php
    'pdo' => array(
        // A certificate authority bundle.
        // If you are using a self-signed server certificate in a development
        // or testing environment, then this would be the same as the server
        // certificate.
        PDO::MYSQL_ATTR_SSL_CA => '/path/to/ca.crt',
    ),
    ```

3. Client certificate/key pair (not self-signed), and do not verify the server certificate.

    ``` php
    'pdo' => array(
        PDO::MYSQL_ATTR_SSL_VERIFY_SERVER_CERT => FALSE,
        PDO::MYSQL_ATTR_SSL_KEY => '/path/to/your.key',
        PDO::MYSQL_ATTR_SSL_CERT => '/path/to/your.crt',
    ),
    ```

4. Client certificate/key pair (could be self-signed), and verify the server certificate.

    ``` php
    'pdo' => array(
        // The SSL_CA can be the same as your.crt if self-signed, but note
        // that it would also have to be a certificate authority for the
        // server certificate. Self-signed would only be for local
        // development testing.
        PDO::MYSQL_ATTR_SSL_CA => '/path/to/ca.crt',
        PDO::MYSQL_ATTR_SSL_KEY => '/path/to/your.key',
        PDO::MYSQL_ATTR_SSL_CERT => '/path/to/your.crt',
    ),
    ```

### Integration modules {:#integration-modules}

**Webform CiviCRM module**

* [Webform project page on drupal.org](https://www.drupal.org/project/webform_civicrm)
* [Webform documentation on civicrm.org](https://docs.civicrm.org/webform-civicrm/en/latest)

**CiviCRM Entity module**

* [Project page on Drupal.org](https://www.drupal.org/project/civicrm_entity)

<!-- Source: drupal/index.md -->
