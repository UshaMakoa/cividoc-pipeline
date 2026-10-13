---
title: Manage detailed logging
category: how-to
topic: system-administration
subtopic: configuration-and-review
component: CiviCRM logging
audiences:
- technical
- operations-user
- administrator
level: intermediate
journey_stage: plan-and-configure
summary: Enable or disable detailed logging, review changes, and manage log tables.
extensions:
- Extended Logging Report
- nz.co.fuzion.innodbtriggers
- at.greenpeace.advancedlogtables
related: []
review_priority: medium
review_notes:
- The separate-database example names `mydatabase_civicrm_logging` but uses `db_name` in the DSN; the relationship between
  them is not explained.
- The source describes multilingual compatibility as experimental as of 4.7 and discusses storage-engine changes starting
  with 5.16; these version-specific statements need review.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/logging-part2.md
destination_path: sysadmin/setup/logging-part2.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/logging-part2/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# Manage detailed logging

## System requirements

- **MySQL Storage Engines** - Starting with version 5.16, CiviCRM uses the InnoDB storage engine to store logging data. Prior to 5.16, the Archive engine was used. Existing installations may continue to use the Archive engine, but migration to InnoDB is recommended for performance and reliability reasons. Existing systems can be migrated by following the steps [below](#migrating-engine-to-innodb).
- **MySQL database permissions** - Logging requires [MySQL Triggers](https://dev.mysql.com/doc/en/triggers.html), so your MySQL database user needs permission to use them. In most cases, you will need to grant the [Trigger Privilege](https://dev.mysql.com/doc/en/privileges-provided.html#priv_trigger). However, depending on your system or if you have enabled binary logging, you may need the [Super Privilege](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_super).

!!! note
    Previously, logging was not compatible with multilingual installations. As of 4.7, it should be compatible, but it's still experimental.

## Turning on logging

1. Make a complete backup of your database, just in case anything goes wrong.
1. If you wish to store your log tables in a separate MySQL database:
    1. Create the new database.
    1. Edit your `civicrm.settings.php` file to add information for the new logging database under `CIVICRM_LOGGING_DSN`. If you create a new database called `mydatabase_civicrm_logging`, the line in `civicrm.settings.php` might look similar to this:

        ```php
        define(
           &#39;CIVICRM_LOGGING_DSN&#39; ,
           &#39;mysql://user:pass@localhost/db_name?new_link=true&#39;
        );
        ```

1. Go to **Administer › System Settings › Misc (Undelete, PDFs, Limits, Logging, etc.)**
1. Set Logging to **Yes**.
1. Alternatively, using the [`cv`](https://docs.civicrm.org/installation/en/latest/general/cli-cv/) command line utility, enable logging with `cv api setting.create logging=1`.

## Turning off logging

1. Go to **Administer › System Settings - Misc (Undelete, PDFs, Limits, Logging, Captcha, etc.)**
1. Set Logging to **No**.
1. Alternatively, using the [`cv`](https://docs.civicrm.org/installation/en/latest/general/cli-cv/) command line utility, disable logging with `cv api setting.create logging=0`.

If you turn logging on again after it has been off for some time, you will not lose any previous log data. New log data will be appended to the log tables.

## Inspecting small changes

1. View a contact record that has been altered after logging was enabled.
1. Go to the **Change Log** tab to view a table of changes.
1. For one update, click **Update** to view the fields that were updated.

## Migrating engine to InnoDB

CiviCRM 5.16 and above use the InnoDB engine. Prior to this, the Archive engine was used.

InnoDB is a better option for most sites, and the changed `log_conn_id` methodology is better for all sites. This change was not implemented in the upgrade script because it could take a long time. Converting and altering all the log tables on a large site is likely to require a planned outage.

To migrate log tables to the InnoDB engine, use the `System.updatelogtables` API call with the `forceEngineMigration` parameter set. For smaller sites, this can be done in the UI using the API Explorer v3, but using `cv` on the command line is better for avoiding timeouts:

```sh
cv api System.updatelogtables forceEngineMigration=1
```

The conversion is a one-way process. Sites that wish to revert to the Archive engine would need to do that through MySQL. There is no API call for this, and it seems unlikely to be a good idea.

!!! warning
    Migrating existing log tables may take a long time, especially on larger installations. Disk usage may also increase significantly when switching from Archive to InnoDB because data is not compressed. Refer to [Advanced Options](#advanced-options) for solutions that enable compression.

## Reporting on multiple changes

### Reports in CiviCRM core

1. Go to **Administer &gt; CiviReport &gt; Create New Report From Template**.
1. With logging turned on, two new report templates are available:
    - Contact Logging Report (Summary)
    - Contact Logging Report (Detail)
1. Use these report templates to create reports as needed. See [CiviReport](https://docs.civicrm.org/user/en/latest/reporting/what-is-civireport/) for more information.

### Extensions

- The [Extended Logging Report](http://civicrm.org/extensions/extended-logging-report) offers additional features over the built-in reports, which are designed to investigate individual transactions and do not cope with Batch or long-running transactions. For example, the extended logging report lets you view all email address changes made this month or changes made by an import job.

## Advanced options

By default, detailed logging does not compress log tables or create indexes on any columns. On larger sites, this could cause log tables to use large amounts of disk space and might affect the performance of change log reports.

CiviCRM allows extension developers to modify the schema definition of log tables, making it possible to address some of these problems:

- The [nz.co.fuzion.innodbtriggers](https://github.com/eileenmcnaughton/nz.co.fuzion.innodbtriggers) extension can enable InnoDB table compression and create indexes on columns that improve the performance of built-in change log reports.
- [at.greenpeace.advancedlogtables](https://github.com/greenpeace-cee/at.greenpeace.advancedlogtables) works like nz.co.fuzion.innodbtriggers and ships with the same defaults, but allows dynamic configuration of the table engine, engine configuration, and indexes via settings. This extension can restore the storage engine to Archive (the previous default, which had some performance and durability issues) or use more specialized engines like TokuDB.

<!-- Source: setup/logging-part2.md -->
