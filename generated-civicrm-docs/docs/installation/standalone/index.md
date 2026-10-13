---
title: Install CiviCRM Standalone
category: how-to
topic: installation
subtopic: installation
component: CiviCRM Standalone
audiences:
- technical
- administrator
- operations-user
level: intermediate
journey_stage: plan-and-configure
summary: Install CiviCRM Standalone from a release tarball and complete the initial site setup.
extensions: []
related:
- ../requirements/index.md
- ../general/cli-cv.md
- ../troubleshooting/index.md
review_priority: medium
review_notes:
- Steps 2 and 3 both use the explicit heading ID download, and Steps 6 and 7 both use webserver; duplicate IDs may make links
  ambiguous.
- The source says Adminster in the users-and-permissions menu path; it is retained as written.
- The source describes Standalone as new and names Download CiviCRM 6.x.x; review whether that wording remains current.
guide: installation
source_repository: https://lab.civicrm.org/documentation/docs/installation.git
source_path: standalone/index.md
destination_path: installation/standalone/index.md
legacy_urls:
- https://docs.civicrm.org/installation/en/latest/standalone/
civicrm_version:
- latest
source_commit: 5a8b870477f63bea90551acb2f7516df67784b19
last_modified: '2026-08-20'
---

# Install CiviCRM Standalone

!!! tip "New release"

    Standalone is a new way to use CiviCRM. You can help continue to improve it by reporting any issues you experience [on the issue tracker](https://lab.civicrm.org/dev/core/-/issues/?label_name%5B%5D=comp%3AStandalone).

???+ tldr "About this document"

    This guide covers installation of CiviCRM Standalone (without a parent CMS). It assumes that you previously
    [reviewed the CiviCRM requirements](../requirements/index.md).

## Step 1. Choose an install method

There are a variety of ways to install and use CiviCRM Standalone. If in doubt, Option 1 is the recommended method for most sites.

??? example "Option 1. Download a release tarball - recommended"

    This is the recommended install method for most sites. The rest of this page assumes you are installing this way.

??? example "Option 2. Using composer - complex sites"

    Using composer allows more automated management of site installation and packages. It may be useful in some contexts, such as automated deployments. It requires shell access and is *not* recommended if you are new to CiviCRM. The [CiviCRM Standalone Composer Project Template](https://github.com/civicrm/civicrm-standalone#install-with-composer) can help you get started.

??? example "Option 3. Using CiviCRM Buildkit - for developers"

    If you are a developer contributing to CiviCRM Core, then it is recommend to use [CiviCRM Buildkit](https://docs.civicrm.org/dev/en/latest/tools/buildkit/) to create Standalone sites. The primary site template is called `standalone-clean`. A composer-style alternative is called `standalone-composer`.

    Using Buildkit is recommended for test and development sites. For production installations, follow Option 1 or 2.

??? example "Option 4. Using Docker"

    If you have used Docker before, this can be a quick way to get up and running. You can find install instructions on the [CiviCRM Docker project repo](https://github.com/civicrm/civicrm-docker).

The rest of this page assumes you are installing from a release tarball (Option 1).

## Step 2. Get the code {:#download}

The latest CiviCRM release is available from [the CiviCRM download page](https://civicrm.org/download). Select "Download CiviCRM 6.x.x" from the list of options.

The release contains all the code for your site in a compressed tarball file (`.tar.gz`).

## Step 3. Deploy the code to your web server/hosting {:#download}

At this step you need transfer the CiviCRM files your web server.

If you are using web hosting, you may be able to upload the compressed tarball file to your server and then extract it, or extract it on your computer and then upload the extracted files. It depends a bit on your hosting configuration. If your hosting has a control panel with a file manager, it should have an option to uncompress archives.

The key thing is to maintain the folder structure from the release archive. Your main folder should contain at least a `civicrm.standalone.php` file, as well as `core`, `public` and `private` subfolders.

You need to make sure this folder is located somewhere your webserver can point to it. Take a note of this folder path (e.g. `/var/www/example.org` or `/mywebhost/user123124019231/sites/civicrm`) as you will need it later.

Note: you should point a domain or subdomain directly at the Standalone project root. Installing to a URL subdirectory (e.g. https://mysite.com/projects/standalone) is not currently supported.

??? info "More detail: CiviCRM Standalone folder structure"

    Standalone sites should have a main folder which in Standalone is known as the _"project root"_.

    After the system has been fully installed and used, you can expect the contents of that folder to look like this:

    | File/Folder | Contents |
    | -- | -- |
    | `civicrm.standalone.php` | Standalone boot file. This identifies the Standalone Project Root, and identifies the locations of the CiviCRM code and settings files. |
    | `core/`                     | Core source code for CiviCRM |
    | `private/`                          | Private site files which should not be accessible over the web |
    | `private/civicrm.settings.php`      | Configuration file with low level settings for CiviCRM. |
    | `private/log/`             | Log files |
    | `private/cache/`             | Cache files for CiviCRM's template compiler |
    | `private/l10n/`             | Translation files |
    | `private/attachment/`             | Private files uploaded to your CiviCRM site - such as files uploaded to a specific contact |
    | `public/`                          | Public site files which *should* be accessible over the web |
    | `public/media/`                  | Public files uploaded to your site, like images that appear on a contribution page or in a mass email |
    | `public/ang/`                  | Angular templates - e.g. for custom forms added to your site with FormBuilder |
    | `ext/`                  | CiviCRM extensions you have added to your site |

    <!-- FIXME: Describe more items from `web/upload/` -->

## Step 4. Get translations if needed {:#i18n}

The default CiviCRM language is US English (`en_US`). You can select a different language or locale during the web installation step, and the chosen translations will be downloaded for you.

Alternatively, if you need the web installer in another language you can manually download all the translation files now. Head to the [CiviCRM download page](https://civicrm.org/download) and choose "Internationalisation files" from the Download options, then copy the `l10n` directory from the download into the `private` directory of your site (so you should end up with folders like `private/l10n/es_ES`).

## Step 5. Configure MySQL {:#mysql}

CiviCRM stores data in MySQL (or, equivalently, MariaDB). You will need to provide a new database and determine key details:

* MySQL hostname/IP (*and, optionally, port number*)
* MySQL database name
* MySQL username
* MySQL password

??? example "_MySQL_: Set up a new database on your webhosting"

    If you are using a webhost, they will often provide a UI for this, from which you can get these details.

    Alternatively, they may provide _phpmyadmin_ or _cpanel_ access to your database server. You can find guides for these tools online, e.g. https://phppot.com/mysql/phpmyadmin-create-database/ or https://support.cpanel.net/hc/en-us/articles/360057550753-How-to-create-a-database-and-database-user-in-cPanel

    <!-- Might be good to have more specific pointers for phpmyadmin or cpanel? -->

??? example "_MySQL_: Create database via command-line"

    Open the `mysql` command-line interface. You may need to run one of these commands:

    ```bash
    mysql
    mysql -u root
    mysql -u root -p
    mysql -u root -p --host=db.example.com --port=3306
    ```

    This should display a welcome message:

    ```
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 6879
    Server version: 8.0.29 Source distribution

    Copyright (c) 2000, 2022, Oracle and/or its affiliates.

    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    mysql>
    ```

    Now, you can configure a database (`civicrm`), user (`civicrm`), and password (`__TOP_SECRET__`):

    ```sql
    mysql> CREATE DATABASE civicrm CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    Query OK, 1 row affected (0.00 sec)

    mysql> CREATE USER 'civicrm'@'localhost' IDENTIFIED BY '__TOP_SECRET__';
    Query OK, 0 rows affected (0.01 sec)

    mysql> GRANT ALL on civicrm.* to 'civicrm'@'localhost';
    Query OK, 0 rows affected (0.01 sec)
    ```

## Step 6. Configure your webserver {:#webserver}

Now you need to configure your webserver to point to your CiviCRM Standalone project folder.

The exact steps vary based on your specific environment. Here are some typical tasks for common environments:

??? example "_Web hosting_: Point a new subdomain to your Standalone project folder"

    If you are using web hosting and your release code is in e.g. `/mywebhost/user123/my-sites/civicrm`, then you should just need to point a domain or subdomain from your hosting to this directory.

    You will need to make sure PHP is enabled, including the php modules detailed in the Installation Requirements. Your web host may provide a UI, or you may need to add a `php.ini` file specifying options.

    You should specify that the `private` folder should *not* be web accessible.

??? example "_Apache_: Configure a virtual-host on Debian-based server"

    If you created a folder like `/var/www/example.com/web`, then you probably need to configure the web-server to read this folder.

    The essence is to create a configuration file underneath `/etc/apache2/sites-*` with a `<VirtualHost>` declaration, such as:

    ```
    <VirtualHost *:80>
      ServerAdmin me@example.com
      DocumentRoot /var/www/example.com/web
      ServerName example.com
      ...
    </VirtualHost>
    ```

    For a complete example, see [Installing virtual hosts for Drupal sites](https://www.drupal.org/node/111238). (This example is for Drupal,
    but similar steps should work for CiviCRM Standalone - simply adjust the `DocumentRoot` and `ServerName`.)

??? example "_nginx_: Configure a virtual-host on Debian-based server"

    An example starting point for nginx virtual host configuration is available in the [CiviCRM Standalone repository](https://github.com/civicrm/civicrm-standalone).

## Step 7. Configure webserver permissions {:#webserver}

Your webserver will need to be able to write to at least your `public` and `private` directories. If you wish to install extensions through the web UI on your site, the webserver will also need to write to the `ext` directory.

On many webhosts the webserver will be able to write to all directories, and you won't need to do anything.

If you have `ssh` access to your server, you may need to set the user permissions directly.

??? example "_Permissions_: Grant write access to `public`, `private` and `ext` directories on Linux server"

    In most Linux distributions, the web server runs with a special user+group (such as `www-data` or `www`).

    You must specifically grant access for this user to write to data folders. Typically you will want to grant access for the group `www-data` to `private`, `public` and `ext` folders.

    ```bash
    cd /var/www/example.com/web

    chmod 2770 private public ext
    chmod g+rwX -R private public ext
    chgrp -R www-data private public ext
    ```

    <!-- Should we recommend `setfacl` (Linux) and `chmod +a` (MacOS)? Or is this assuming that current-user is also in `www-data`? -->
    <!-- These are the configs I've liked: https://github.com/amp-cli/amp/blob/0.7.3/app/defaults/services.yml#L189-L199 -->

## Step 8. Run the installer {:#installer}

The installer verifies requirements, prepares the database, and initializes the configuration file. You may run the installer through the web interface (*which is simpler*) or the command-line interface (*which has more options*).

??? example "Run installer via web UI"

    1. Head to the `/civicrm` page on your website. This may look like:
        * `https://example.com/civicrm`
        * `http://localhost:8000/civicrm`
        * `http://example.127.0.0.1.nip.io:8001/civicrm`
    2. The CiviCRM installer will open.
        * You will need to provide the details for the database you created earlier
        * You also have to provide a username, password and e-mail address for the site adminstrator user. Note: this login is totally separate from the database username and password in step 1.
        * *If there are unmet requirements*, the installer will list them. Consult the [Requirements](../requirements/index.md) documentation for additional advice.
        * *If all the requirements are met*, proceed through the questionnaire.
        * You can select another language if you want CiviCRM to be installed in another language then English US. The installer will then download the translation files for you.
        * Finally, click "Install CiviCRM".
    3. After installing, you should see a confirmation page confirming installation has completed correctly.

??? example "Run installer via command-line"

    CiviCRM has a command-line administration tool, `cv`, which can perform installation. For a local dev site, a typical install command might be:

    ```bash
    cd /path/to/standalone-service-root
    cv core:install -v \
      --cms-base-url=http://localhost:8000 \
      --db=mysql://USER:PASS@HOST:PORT/DATABASE \
      -m extras.adminUser=USERNAME \
      -m extras.adminPass=SECRET \
      -m extras.adminEmail=ME@EXAMPLE.COM
    ```

    For full details, see [command-line installer](../general/cli-cv.md).

The installer will verify that you've downloaded the correct version of CiviCRM, and will check your server environment to make sure it meets CiviCRM requirements. It will then create and populate a database for CiviCRM as well as create your CiviCRM settings file (civicrm.settings.php).

<!-- Do we need to suggest reviewing permissions at the start -- given that we control defaults and given that there's a general checklist?  -->

## Log in and review users and permissions {:#users}

You should now be able to log in to your site at e.g. `https://your-site.test/civicrm/login`. Use the administrator username and password you created during install.

Head to **Adminster** >> **Users and Permissions** to configure users and roles for your site.

## Review the checklist {:#checklist}

The **Configuration Checklist** provides a convenient way to work through the settings that need to be reviewed and configured for a new site. You can link to this checklist from the installation success page AND you can visit it at any time from **Administer** » **Administration Console** » **Configuration Checklist**.

## Test-drive CiviCRM {:#test-drive}

Start exploring your new CiviCRM Standalone site. Please report any issues you find in the [Issue Tracker](https://lab.civicrm.org/dev/core/-/issues/?label_name%5B%5D=comp%3AStandalone)

## Addenda

### Troubleshooting {:#troubleshooting}

* If Apache's `mod_negotation` Multiviews is enabled (e.g. when using cPanel hosting) you may get an "Unexpected error" which prevents login to your new site. Adding `Options -Multiviews` to your `.htaccess` file may help - see [dev/core#5640](https://lab.civicrm.org/dev/core/-/issues/5640#note_175340).

* Review the [General Troubleshooting](../troubleshooting/index.md) page for help with general problems you may encounter during CiviCRM installation.

<!-- Source: standalone/index.md -->
