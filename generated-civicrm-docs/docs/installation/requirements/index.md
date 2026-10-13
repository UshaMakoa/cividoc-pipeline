---
title: Installation requirements
category: reference
topic: installation
subtopic: server-and-software-requirements
component: CiviCRM installation
audiences:
- technical
- administrator
- operations-user
level: intermediate
journey_stage: plan-and-configure
summary: Check the server, software, and database requirements before installing or upgrading CiviCRM.
extensions: []
related:
- ../planning/hosting.md
- ../planning/cms.md
- ../general/mysql_tls.md
review_priority: medium
review_notes:
- The historical PHP table has overlapping CiviCRM version ranges with different recommended PHP versions. The ranges are
  preserved as supplied.
- The MySQL 8 section describes CMS compatibility using version-specific and potentially outdated statements. These are preserved
  for review.
guide: installation
source_repository: https://lab.civicrm.org/documentation/docs/installation.git
source_path: requirements/index.md
destination_path: installation/requirements/index.md
legacy_urls:
- https://docs.civicrm.org/installation/en/latest/requirements/
civicrm_version:
- latest
source_commit: 5a8b870477f63bea90551acb2f7516df67784b19
last_modified: '2026-08-20'
---

# Installation requirements

Ensure that your system meets the following requirements before installing or upgrading CiviCRM.

If you are curious what technologies other organizations are using to run CiviCRM, you can look at the [CiviCRM Stats](https://stats.civicrm.org/?tab=technology).

## Summary {:#summary}

A recommended server environment should typically meet these guidelines:

* **Operating system**: Linux
* **PHP**: PHP 8.3, 8.4 or 8.5 is recommended (8.4 runs with CiviCRM 6.12-6.15, 8.5 with 6.16+)
* **MySQL**: MySQL 5.7.5+ (8+ is recommended) or MariaDB 10.2+ (11.4+ is recommended) -- with configuration requirements
* **CMS**: CiviCRM StandAlone supported since Jan 2025. Optional CMS support for Backdrop, Drupal 7 (not recommended as official security support not available), Drupal 10, Drupal 11, Joomla 5 or WordPress 6.3+.

Other environments may also meet the system requirements. The following sections present requirements more precisely.

## Server environment {:#server}

### Operating system {:#os}

If your server meets all of the requirements described on this page, CiviCRM *should* function correctly. There are no explicit operating system requirements. However, it's worth noting that CiviCRM is far more widely deployed and tested on UNIX-based operating systems, in particular Linux (e.g. Ubuntu, Debian, etc.), than with Microsoft Windows. You can still use CiviCRM fine from Windows desktops when the hosting environment runs Linux.

### Hosting

In general, CiviCRM is a demanding web application which requires substantial server resources. It may not perform well on all hosting platforms. Learn more about [choosing your hosting platform](../planning/hosting.md).

## CMS (= Content Management System) {:#cms}

CiviCRM Standalone has been available since January 2025, allowing CiviCRM to run without a CMS. Remote forms allow CiviCRM forms to be used from other sites.

CiviCRM can be installed as plugin/module for the following CMSes: Drupal, Wordpress, Backdrop and Joomla.

See the page on [choosing a CMS](../planning/cms.md) for more information about the advantages and disadvantages of each compatible CMS platform.

Each CMS has specific details of which versions are supported or receiving only security support - see the CMS-specific install instructions for details.

## PHP {:#php}

### PHP version on the command line

The PHP version used on the command line is important and should match the version used by the web server. For example, using PHP 8.0 (or lower) on the command line and using PHP 8.3 (or higher) on the web server has been known to cause issues.

It is also important to ensure that the same PHP extensions/modules are loaded and enabled on both the command line version of PHP and the web server version.

### PHP version

The following recommendations relate to the CiviCRM core codebase. CiviCRM native extensions, and modules and plugins that integrate CiviCRM with CMSes are maintained and released on other schedules. As they typically lag in supporting newer versions of PHP, it is recommended that you test your full site including this other software extensively as part of migrating to a newer version of PHP.

You can find the lifecycle of current PHP versions [here](https://www.php.net/supported-versions.php).

**CiviCRM 6.16+**

| PHP Version | PHP Minimum Version | PHP Recommended Version |
| ------------------------ | ------------------- | ----------------------- |
| PHP 8.5 | **compatible and recommended** | **compatible and recommended** |
| PHP 8.4 | **compatible and recommended** | **compatible and recommended** |
| PHP 8.3 | **compatible and recommended** | **compatible and recommended** |
| PHP 8.2 | **compatible** | **compatible** |
| PHP 8.1 | compatible but **not recommended** due to [PHP end-of life](http://php.net/eol.php) | compatible but **not recommended** due to [PHP end-of life](http://php.net/eol.php) |
| PHP 8.0 | **not compatible** | **not compatible** |
| PHP <= 7.4 | **not compatible** | **not compatible** |

**CiviCRM 6.10 ESR or stable**

| PHP Version | PHP Minimum Version | PHP Recommended Version |
| ------------------------ | ------------------- | ----------------------- |
| PHP 8.4 | not compatible | not compatible |
| PHP 8.3 | **compatible and recommended** | **compatible and recommended** |
| PHP 8.2 | **compatible** | **compatible** |
| PHP 8.1 | compatible but **not recommended** due to [PHP end-of life](http://php.net/eol.php) | compatible but **not recommended** due to [PHP end-of life](http://php.net/eol.php) |
| PHP 8.0 | compatible but **not recommended** due to [PHP end-of life](http://php.net/eol.php) in Nov 2023 | compatible but **not recommended** due to [PHP end-of life](http://php.net/eol.php) in Nov 2023 |
| PHP <= 7.4 | **not compatible** | **not compatible** |

**Historical PHP versions**

The table below gives information on PHP minimum and recommended version compatibility for old versions of CiviCRM:

| CiviCRM Version | PHP Minimum Version | PHP Recommended Version |
| ------------------------ | ------------------- | ----------------------- |
| 5.1 - 5.5 | 5.5 | 7.0 |
| 5.6 - 5.9 | 5.5 | 7.1 |
| 5.10 - 5.13 | 5.6 | 7.2 |
| 5.14 - 5.23 | 7.0 | 7.2 |
| 5.24 | 7.0 | 7.3 |
| 5.25 - 5.34 | 7.1 | 7.3 |
| 5.35 - 5.36 | 7.2 | 7.3 |
| 5.37 - 5.45 | 7.2 | 7.4 |
| 5.46 - 5.69 | 7.3 | 7.4 |
| 5.70 - 5.77 | 7.4 | 8.1 |
| 5.70 - 6.0 | 7.4 | 8.3 |
| 6.0 - 6.11 | 8.0 | 8.3 |
| 6.12 - 6.15 | 8.1 | 8.4 |
| 6.16+ | 8.2 | 8.5 |

### PHP extensions

To install these extensions, you will typically install a separate package within your server's package manager (e.g. `apt-get` on Ubuntu).

#### Required for CiviCRM core

* [PHP BCMath](https://www.php.net/bcmath) - required for calculating financial values in CiviCRM Core.
* [PHP Curl](https://www.php.net/curl) - required for many payment processors, the extension manager, and the CiviCRM News dashlet.
* [PHP DOM XML](https://www.php.net/manual/en/dom.setup.php) - required by CiviCase.
* [PHP Multibyte](https://php.net/manual/en/ref.mbstring.php) - required for internationalisation and proper encoding of fields.
* [PHP Zip](https://php.net/manual/en/book.zip.php) - required for unzipping auto-downloaded extensions so they can be installed from the browser.
* [PHP INTL](https://www.php.net/intl) - required for outputting localized formatted number strings from CiviCRM 5.28 onwards
* [PHP File Information](https://www.php.net/manual/en/book.fileinfo.php) - required for spreadsheet support from 5.44 onwards
* [PHP MySQL PDO](https://www.php.net/manual/en/ref.pdo-mysql.php) - required for running tests and working with Drupal

### PHP configuration

The following PHP directives is the recommended minimum. These are defined in the [php.ini file](https://www.php.net/manual/ini.list.php).

* [`memory_limit`](https://www.php.net/manual/ini.core.php#ini.memory-limit) 256M
* [`max_execution_time`](https://www.php.net/manual/info.configuration.php#ini.max-execution-time) 240
* [`max_input_time`](https://www.php.net/manual/info.configuration.php#ini.max-input-time) 120
* [`post_max_size`](https://www.php.net/manual/ini.core.php#ini.post-max-size) and [`upload_max_filesize`](https://www.php.net/manual/ini.core.php#ini.upload-max-filesize) 50M

    !!! warning "Don't use MAMP XCache"
        Several people have reported "white screen of death" trying to run CiviCRM with MAMP's XCache enabled (check MAMP > Preferences > PHP > Cache).

## MySQL

CiviCRM requires MySQL (or compatible) database software.

[MariaDB](https://mariadb.org/) and [Percona](https://www.percona.com/software/mysql-database/percona-server) are forks of the MySQL project and can be used as drop-in replacements for MySQL.

Other database servers (such as PostgreSQL) are not compatible with CiviCRM.

### MySQL version

Your MySQL version should be **5.7.5 or greater** or MariaDB **10.2 or greater**.

??? info "Historical MySQL Versions"
    The table below gives information on MySQL minimum and recommended version compatibility for old versions of CiviCRM:

    | CiviCRM Version          | MySQL Minimum Version | MySQL Recommended Version | MariaDB Minimum Version | MariaDB Recommended Version |
    | ------------------------ | --------------------- | ------------------------- | ----------------------- | ------------------- |
    | 5.26 - 5.27              | 5.5                   | 5.7                       |                         |      |
    | 5.28 - 5.33              | 5.6.5                 | 5.7                       |                         | 10.4 |
    | 5.34 - 5.51              | 5.7 (unenforced)      | 5.7                       | 10.0.2                  | 10.4 |
    | 5.52 - Latest            | 5.7 (enforced)        | 5.7                       | 10.2                    | 10.4 |

#### MySQL 8

As of version 5.24 CiviCRM has been shown to be able to run on MySQL 8 through the execution of our test matrix. All of the Content Management Systems support MySQL 8, CiviCRM MySQL 8 support was being tracked in this [issue for MySQL 8 support](https://lab.civicrm.org/dev/core/issues/392). [Backdrop supports MySQL 8 as of 1.17.2](https://github.com/backdrop/backdrop/releases/tag/1.17.2), [Drupal 7 as of 7.76 Supports MySQL 8](https://www.drupal.org/node/3185889), All versions of [Drupal 9](https://www.drupal.org/docs/system-requirements/database-server-requirements) support MySQL 8, Current versions of WordPress and [Joomla](https://docs.joomla.org/Joomla_and_MySQL_8) appear to be compatible with MySQL 8.

### MySQL connection {:#mysql-connection}

By default, new installations of CiviCRM will copy the MySQL connection details from the CMS, creating a shared database. It is also possible to install CiviCRM on a separate database. As a rule of thumb:

* *A shared database* works well for small deployments (eg a few thousand records and a single administrator or developer).
* *Separate databases* work well for large deployments (eg a million records and multiple administrators/developers).

If you are unsure which style fits better, consider some trade-offs:

* _Initial setup_: The shared database can be setup automatically. To use a separate database, you must create the second one.
* _"Views" integration_: On Drupal 7 / Backdrop, the "Views" integration can query MySQL data from both CMS and Civi. This works easily with a shared database, but it requires effort with separate databases.
* _Backups_: If you have a small data-set and a good backup mechanism, the shared database is easier to backup -- it's only one job.
* _Large datasets_: If the CMS dataset and Civi dataset grow large (eg millions of records), then separating the databases will allow better resource-management.
* _Development/staging process_: If you have different people working on the system code or system configuration, then they may need to work with different subsets of the data. (Ex: A theme developer may need access to the CMS data but not the Civi data. For an application developer, that could be reversed.) With separate databases, it may be easier to negotiate the workflow.

If your choose to use separate databases, then you need connection details for the second database. Connections are represented in URL format. For example:

```
mysql://dbuser:dbpassword@localhost:3306/dbname
```

The example URL captures several pieces of information:

| Setting | Example Value |
| ------- | ----- |
| Database User Name | `dbuser` |
| Database User Password | `dbpassword` |
| Database Server | `localhost` |
| Database Port | `3306` |
| Database Name | `dbname` |

Additional URL parameters may be added to support [MySQL with TLS](../general/mysql_tls.md).

### MySQL configuration

* Support for the `innodb` storage engine is required.
* The `thread_stack` configuration variable should be set to 192k or higher.
* Trigger support is required.
* `ANSI` or `ANSI_QUOTES` is not a supported `sql_mode`.
* The `ONLY_FULL_GROUP_BY` mode should be turned off on production sites - although this is mostly precautionary now.
    * In MySQL 5.7+ the SQL mode `ONLY_FULL_GROUP_BY` is enabled by default which causes some errors due to some of CiviCRM's SQL queries that were written with the assumption that this mode would be disabled.
    * Administrators are advised to turn off this SQL mode by removing the string `ONLY_FULL_GROUP_BY` from the `sql_mode` variable. The following SQL query will do the trick.

        ```sql
        SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
        ```

    * See also:
        * A popular [Stack Exchange question](https://stackoverflow.com/a/36033983/895563) discussing this issue
        * [MySQL documentation on `sql_mode`](https://dev.mysql.com/doc/refman/5.7/en/sql-mode.html#sql-mode-setting)
* If you plan to have multiple languages used in your CiviCRM installation it is strongly recommended that you ensure that `locale` is set to a UTF8 locale and also ensure that you set utf8 as the standard encoding for MySQL. To alter locale you can configure as per [Ubuntu instructions](https://www.thomas-krenn.com/en/wiki/Configure_Locales_in_Ubuntu), [Debian](https://wiki.debian.org/Locale), [CentOS](https://www.rosehosting.com/blog/how-to-set-up-system-locale-on-centos-7/). To set the default encoding for MySQL you should follow the steps provided in this [Stack Overflow post](https://stackoverflow.com/questions/3513773/change-mysql-default-character-set-to-utf-8-in-my-cnf)
* In order to support a future data migration from `utf8` to the `utf8mb4` character set, it is recommended, though not yet required, to add the following configuration directives on MySQL 5.5 or 5.6 (these are the default values on MySQL 5.7):

    ```ini
    [mysqld]
    innodb_large_prefix=true
    innodb_file_format=barracuda
    innodb_file_per_table=true
    ```

* In MySQL 8 the default authentication plugin changes from `mysql_native_password` to `caching_sha2_password`. This may cause issues with your PHP layer. Fortunately you can revert this change by specifying your chosen authentication plugin in your MySQL configuration:

  ```ini
   [mysqld]
   default_authentication_plugin=mysql_native_password
  ```

  Also in MySQL 8 the following variables, used fairly extensively in CiviCRM installs, have been removed `innodb_large_prefix` and `innodb_file_format`. In MySQL 8 binary logging is also turned on by default which many users may want to turn off, this can be achieved by adding to your MySQL configuration file:

  ```ini
   [mysqld]
   skip-log-bin
  ```

### MySQL time

#### Synchronization {:#mysql-time-sync}

CiviCRM performs various operations based on dates and times – for example, deactivating expired records or triggering scheduled reminders. To perform these operations correctly, the dates and times reported by PHP and MySQL should match. If the dates or times are mismatched, then one or more of the following may be the problem:

* PHP and MySQL may be running on different servers, and the clocks may be out-of-sync. Configuring automatic clock synchronization is the best solution.
* PHP, MySQL, and/or the operating system may be configured to use different default timezones. Verify the configuration of each.
* The content management system (Drupal, Joomla, or WordPress) or one of its plugins may manipulate the timezone settings without informing CiviCRM's. You may wish to post to [Stack Exchange](https://civicrm.stackexchange.com/) or [Mattermost](https://chat.civicrm.org) about your problem. Please include any available details about the timezone settings in the operating system, PHP, MySQL, and the CMS; if you have any special CMS plugins or configuration options which may affect timezones, please report them.

!!! tip "WordPress Settings"

    If you get a MySQL/PHP mismatch warning, under `Settings > General` set the timezone to a City, not UTC offset. For example, use `London` not `UTC+0`.

#### Timezones {:#mysql-timezones}

To support full and consistent display of timestamps, the MySQL server requires timezone data. Many servers include this data by default, but others require you to load it.

??? info "Survey of MySQL Servers and Timezone Support"

    <!-- Sorted by `Status,Environment` -->

    | Status | Environment | Comment |
    | -- |  -- |  -- |
    | ✅ | CiviHosting | |
    | ✅ | Digital Ocean | Specifically tested w/[managed MySQL 8.0](https://www.digitalocean.com/products/managed-databases-mysql) |
    | ✅ | Docker `mysql` | Specifically tested w/[8.0, 8.0-oracle, and 5.7](https://hub.docker.com/_/mysql) |
    | ✅ | Docker `mariadb` | Specifically tested w/[10.3 and 10.4](https://hub.docker.com/_/mariadb) |
    | ✅ | Google Cloud SQL | Specifically tested w/5.6. Warning from docs: ["not guaranteed to provide up-to-date time settings"](https://cloud.google.com/sql/docs/mysql/known-issues) |
    | 🛠 | Azure Database | Use [`az_load_timezone()`](https://docs.microsoft.com/en-us/azure/mysql/howto-server-parameters#working-with-the-time-zone-parameter)  |
    | 🛠 | CentOS MariaDB/MySQL | Use `mysql_tzinfo_to_sql` |
    | 🛠 | cPanel/WHM (with root access) | Use `mysql_tzinfo_to_sql` |
    | 🛠 | Debian/Ubuntu MariaDB/MySQL | Use `mysql_tzinfo_to_sql` |
    | 🛠 | Nix MariaDB/MySQL | Use `mysql_tzinfo_to_sql` |
    | ❓ | Amazon RDS | Needs testing/clarification. There are old google-cached forum posts which imply gradual evolution toward support. The current ["Local time zone" page](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html#MySQL.Concepts.LocalTimeZone) seems to affirm, so probably ✅ ... but the docs don't specifically mention session-scoped timezones. |
    | ❓ | cPanel/WHM (without root access) | Needs testing/clarification. If you lack access to `mysql_tzinfo_sql` (SSH) but have other ways to perform MySQL administration, then you may be able to load [pre-generated MySQL timezone data](https://github.com/civicrm/tzdata-mysql). Key question is whether you have MySQL admin rights. |
    | ❓ | Pantheon | Needs testing/clarification. |
    | ❓ | WP Engine | Needs testing/clarification. |

    Definitions:

    * (✅) Already support MySQL timezones
    * (🛠) Can support MySQL timezones, with extra setup
    * (❓) Status is not certain
    * (🛑) Cannot support MySQL timezones

To determine if your server currently supports timezones, you can run a test with the `CONVERT_TZ()` function.

```sql
mysql> SELECT CONVERT_TZ("2001-02-03 04:05:00", "GMT", "America/New_York");
+--------------------------------------------------------------+
| CONVERT_TZ("2001-02-03 04:05:00", "GMT", "America/New_York") |
+--------------------------------------------------------------+
| 2001-02-02 23:05:00                                          |
+--------------------------------------------------------------+
```

If this doesn't perform a proper conversion, then you probably need to load the timezone data.

* On a self-hosted instance of MySQL or MariaDB, the standard technique is to run [`mysql_tzinfo_to_sql`](https://dev.mysql.com/doc/refman/8.0/en/mysql-tzinfo-to-sql.html).
* If you cannot run `mysql_tzinfo_to_sql` but have administrative access through another medium, you may load the [pre-generated MySQL timezone data](https://github.com/civicrm/tzdata-mysql/tree/master/sql).
  Be sure to load the appropriate SQL file into the database named `mysql`.
* Some managed hosts require their own process. For example, "Azure Database" has a special procedure ([`az_load_timezone()`](https://docs.microsoft.com/en-us/azure/mysql/howto-server-parameters#working-with-the-time-zone-parameter)).
  For managed hosts, you may need to consult their documentation or inquire with support.

??? info "Global organizations and service-providers should consider automation."

    Timezone definitions change, albeit infrequently. For example, in 1996, Mexico adopted Daylight Savings Time (for most of its timezones); then,
    in 2022, they dropped DST. For computer-based clocks supporting users in Mexico, those changes require an update to the timezone data. But it's
    rare -- for Mexico, that represents two major changes (circa 1996 and 2022) over the span of 26 years.

    The significance of timezone change is circumstantial. Compare:

    * A local organization may go 20 years without needing an update. When there is a local or national change, it will be covered in the local news.
      You may get by with infrequent/ad-hoc updates.
    * Globally, in any given year, there will be several locales which do change their rules, and you may not be specifically aware of every change.
      A global organization or service-provider should consider automatic updates. For example, you might define a system-startup script or a
      monthly cron-job to run `mysql_tzinfo_to_sql`.

### MySQL permissions

The permissions you'll need to assign to the MySQL user that CiviCRM uses will **depend on your version of MySQL**. The following example assumes you have a database called `civicrm` and a MySQL user called `civicrm_user`.

```sql
GRANT
  SELECT,
  INSERT,
  UPDATE,
  DELETE,
  CREATE,
  DROP,
  INDEX,
  ALTER,
  CREATE TEMPORARY TABLES,
  LOCK TABLES,
  TRIGGER,
  CREATE ROUTINE,
  ALTER ROUTINE,
  REFERENCES,
  CREATE VIEW,
  SHOW VIEW
ON civicrm.*
TO 'civicrm_user'@'localhost'
IDENTIFIED BY 'realpasswordhere';
```

#### Binary logging

If you want to enable binary logging you will need to choose one of the following. Either:

* Add the following line to your configuration file. The location of the configuration file depends on your operating system and database server you can find more information [for MySQL here](https://dev.mysql.com/doc/refman/5.7/en/option-files.html) and [for MariaDB here](https://mariadb.com/kb/en/configuring-mariadb-with-option-files/).

    ```ini
    log_bin_trust_function_creators = 1
    ```

    (See the [MySQL manual reference](http://dev.mysql.com/doc/refman/5.1/en/server-system-variables.html#sysvar_log_bin_trust_function_creators) for more information.)

* Or give the `SUPER` permission (even if your MySQL version is greater than 5.1.6).

    ```sql
    GRANT SUPER ON *.* TO 'civicrm_user'@'localhost';
    ```

    (More information on triggers is available in the MySQL documentation about [Binary Logging of Stored Programs](http://dev.mysql.com/doc/refman/5.1/en/stored-programs-logging.html).)

#### Installing on certain cloud providers

When installing on certain cloud providers (AWS, Azure) where you are using database as a service, you will not have access to the my.cnf but you can generally use [Database Parameter Groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html) or in [Azure](https://docs.microsoft.com/bs-cyrl-ba/azure/mysql/howto-server-parameters) to set the parameters such as the `log_bin_trust_function_creators` as appropriate. On Azure running with DB as a service there needs to be a change made to the installation code as per the answer on [Stack Exchange here](https://civicrm.stackexchange.com/questions/31794/civicrm-on-azure-not-finding-the-server). This is due to Azure not permitting connections to databases without credentials.

<!-- Source: requirements/index.md -->
