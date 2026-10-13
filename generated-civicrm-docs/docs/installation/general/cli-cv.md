---
title: Install CiviCRM with cv
category: how-to
topic: installation
subtopic: command-line-installation
component: cv
audiences:
- technical
- administrator
- operations-user
- membership-manager
level: advanced
journey_stage: plan-and-configure
summary: Install CiviCRM from the command line with cv, then configure the site and troubleshoot common installation problems.
extensions: []
related: []
review_priority: medium
review_notes:
- The limitations name Drupal 7/8/9 as primarily tested, and one error note applies specifically to Drupal 9; these version-specific
  statements may be outdated.
- The extension download example uses `EXTESION_KEY@ZIP_URL`, which appears inconsistent with the other extension placeholders.
  The command is preserved as written.
- A source comment marks multisite options as unfinished.
guide: installation
source_repository: https://lab.civicrm.org/documentation/docs/installation.git
source_path: general/cli-cv.md
destination_path: installation/general/cli-cv.md
legacy_urls:
- https://docs.civicrm.org/installation/en/latest/general/cli-cv/
civicrm_version:
- latest
source_commit: 5a8b870477f63bea90551acb2f7516df67784b19
last_modified: '2026-08-20'
---

# Install CiviCRM with cv

Before using this guide:

1. Install a supported CMS.
2. [Review the CiviCRM requirements](../requirements/index.md).
3. Download the CiviCRM code. See “*Get the code*” for [Backdrop](../backdrop/index.md#download), [WordPress](../wordpress/index.md#download) or [Drupal](../drupal/index.md).

The installer verifies requirements, prepares the database, and initializes the configuration file.

Each Civi-CMS integration has an option to install through the web interface, which is intended for new and casual administrators. For more advanced administrators, the general-purpose command-line interface (CLI) is useful for:

- Automating installation
- Accessing uncommon or hidden options
- Debugging or developing changes to the installer

**Limitations:** At time of writing, the CLI installer is primarily tested with Backdrop, Drupal 7/8/9, and WordPress. It is primarily tested with single-site deployments. For other configurations (e.g. Joomla; e.g. multisite), it may require extra variables/options/patches.

If you are using the CLI for debugging or development, the __CiviCRM Developer Guide__ has additional guidance. See [Setup Reference: Overview](https://docs.civicrm.org/dev/en/latest/framework/setup/) and [Setup Reference: Getting Started](https://docs.civicrm.org/dev/en/latest/framework/setup/getting-started/).

## Download "cv"

The CLI installer is part of [cv](https://github.com/civicrm/cv), a general-purpose tool for managing CiviCRM on the command-line. `cv` is distributed in PHAR format, which is a portable executable file for PHP. It should run in most Unix-like environments that support PHP.

Download [cv.phar](https://download.civicrm.org/cv/cv.phar) and put it somewhere in the `PATH`. For example:

```bash
sudo curl -LsS https://download.civicrm.org/cv/cv.phar -o /usr/local/bin/cv
sudo chmod +x /usr/local/bin/cv
```

## Change directory

To run `cv`, navigate into the base folder of the CMS. For example:

```bash
cd /var/www/example.org
```

## Run the installer

A typical installation command looks like this:

```bash
cv core:install --url="URL" --lang="LANG"
```

For example:

```
$ cv core:install --url="https://example.org" --lang="fr_CA"

Found code for civicrm-core in /var/www/example.org/wp-content/plugins/civicrm/civicrm
Found code for civicrm-setup in /var/www/example.org/wp-content/plugins/civicrm/civicrm/setup
Creating file /var/www/example.org/wp-content/uploads/civicrm/civicrm.settings.php
Creating civicrm_* database tables in hydrawpcms_p7urq
```

### Installer options

<!-- FIXME: Options for multisite ... -->

#### CMS Base URL

```
cv core:install ... --url="https://example.org"
```

The "CMS Base URL" is the public URL of the website. It is required for most CLI installations. Setting this option ensures that CiviCRM's background jobs (e.g. email-blasts and membership-reminders) can generate correct URLs.

#### Database URL

```
cv core:install ... --db="mysql://user:pass@hostname:port/db"
```

The "Database URL" points to the MySQL database where we will install CiviCRM.

By default, CiviCRM will use the same database as the CMS. However, some administrators prefer to use a separate database. See [Requirements: MySQL: Connection](../requirements/index.md#mysql-connection) for more discussion.

#### Language

```
cv core:install ... --lang=fr_CA
```

The "Language" is the primary language used by the organization.

Based on the language, the installer loads a set of *default configuration data*. This includes common activity types ("Meeting" or "Phone Call"), common location types ("Home" or "Office"), and so on.

__Note__: For a specific language to work, there *must* be corresponding data in the `l10n` folder.

#### Sample data

```
cv core:install ... -m loadGenerated=1
```

The sample data provides a number of fake, auto-generated records -- i.e. sample contacts, contributions, activities, etc. The sample data is useful for testing or reviewing CiviCRM.

__Note__: At time of writing, the sample data is only supported in the default locale, `en_US`.

#### Admin User (Standalone)

```
cv core:install ... -m extras.adminUser=USERNAME \
  -m extras.adminPass=SECRET \
  -m extras.adminEmail=ME@EXAMPLE.COM
```

When installing CiviCRM Standalone, you should specify the credentials for the first administrative user. If omitted, the credentials will be auto-generated and stored in the CiviCRM log.

#### Verbose output

```bash
## Verbose
cv core:install ... -v

## Very verbose
cv core:install ... -vv
```

The "verbose" option provides more details about how the installer works. Enabling the verbose option helps one identify problems.

## Troubleshoot installation

The installer may report a problem. Some common ones are:

### CMS Base URL

On most systems, the `--url` cannot be detected automatically. You must explicitly set it.

### File write permission

The installer needs to create some files and folders. However, if the parent folder is locked-down, then you will need to relax permissions.

For example: in a Drupal site, the installer creates a file `web/sites/<sitename>/civicrm.settings.php`. You may need to mark the parent folder (`web/sites/default` or `web/sites/example.org`) as writeable, e.g.:

```bash
## Grant write-access for the owner-user
chmod 755 web/sites/default

## Grant write-access for all users
chmod 777 web/sites/default
```

### PHP or MySQL configuration

The PHP or MySQL configuration may require an update - e.g. to expand the PHP memory limit, to enable a PHP extension, or to enlarge a MySQL buffer. Common issues are discussed in the [Requirements](../requirements/index.md).

### Error: Call to undefined method Drupal::entityManager

This error appears installing with the `--user` option under Drupal 9. Avoid this error simply by not using the `--user` option.

For common problems, you can fix the problem and re-run the installer.

For unusual problems, enable verbose output (`-v` or `-vv`). It may also help to [inspect the model, plugins, or requirements](https://docs.civicrm.org/dev/en/latest/framework/setup/getting-started/).

## Configure the site

After running `core:install`, you can login to the CMS, open CiviCRM, and configure additional details. The [System Administrator Guide](https://docs.civicrm.org/sysadmin/en/latest/) has more advice on how to configure CiviCRM.

If you are automating the installation, you may wish to automate some common configuration steps:

### Manage extensions

To view available extensions:

```bash
cv ext:list
```

To download extensions from the [Extension Directory](https://civicrm.org/extensions/):

```bash
cv dl EXTENSION_1 EXTENSION_2 ...
```

By default, it downloads stable releases. To download pre-releases (alphas/betas), use dev feed or an explicit URL:

```bash
## Download from the "dev" feed
cv dl --dev EXTENSION_1 EXTENSION_2 ...

## Download from an explicit URL
cv dl EXTESION_KEY@ZIP_URL
```

Alternatively, if you downloaded an extension by other means, you may enable it:

```bash
cv en EXTENSION_1 EXTENSION_2 ...
```

### Manage settings

Many options are managed through the [Settings](https://docs.civicrm.org/dev/en/latest/framework/setting/) framework. These may be configured in the CLI:

```bash
## List current settings
cv api setting.get

## Update specific settings
cv api setting.create KEY_1=VALUE_1 KEY_2=VALUE_2 ...
```

### Clear caches

```bash
cv flush
```

<!--
??? example "Example: Install Mosaico and Shoreditch"

    Here's an example bringing the pieces together:

    ```
    cv dl --dev mosaico shoreditch
    cv api setting.create theme_backend=shoreditch
    ```
-->

<!-- Source: general/cli-cv.md -->
