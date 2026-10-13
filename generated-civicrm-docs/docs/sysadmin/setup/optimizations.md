---
title: Optimize CiviCRM performance
category: how-to
topic: system-administration
subtopic: settings-and-caching
component: CiviCRM
audiences:
- administrator
- technical
- operations-user
level: advanced
journey_stage: manage-and-automate
summary: Review search, template, cache, directory-scanning, and database options that may improve CiviCRM performance.
extensions:
- RPOW
related:
- ../setup/jobs.md
- https://docs.civicrm.org/user/en/latest/initial-set-up/customizing-the-user-interface/#customizing-search-preferences
- https://github.com/totten/rpow
review_priority: medium
review_notes:
- Directory-exclusion guidance includes claims specific to version 5.29.
- The contact_smart_group_display description says users can see “all the contacts the person is a member of”; the intended
  meaning is unclear, so the wording is retained.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/optimizations.md
destination_path: sysadmin/setup/optimizations.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/optimizations/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Optimize CiviCRM performance

This page describes tips and tricks for optimizing a CiviCRM system.

## Search settings

There is a trade-off between convenience and performance when searching. Altering some search settings, especially the automatic wildcard, may improve performance. [See the user guide](https://docs.civicrm.org/user/en/latest/initial-set-up/customizing-the-user-interface/#customizing-search-preferences).

## Smarty

### Disable compile check

By default, the Smarty option `compile_check` is set to `TRUE`, which forces Smarty templates to be recompiled on every call. Recompiling is unnecessary unless a template or config file has changed. Typically, you enable this during development and disable it for production.

To disable it in CiviCRM, edit this constant in `civicrm.settings.php`:

```php
define('CIVICRM_TEMPLATE_COMPILE_CHECK', FALSE);
```

## Smart group and ACL performance

CiviCRM has caching for smart groups and ACLs. The configuration that works best is site-specific. If you take no action, you will get the following behaviour:

1. Every time a contact is edited, the ACL caches (`civicrm_acl_cache`, `civicrm_acl_contact_cache`) will be emptied, regardless of whether you use ACLs.
1. Every time a contact is edited, any smart groups that were created more than 5 minutes ago will be deleted from the `civicrm_group_contact_cache` table.
1. Whenever a smart group is accessed, the cache for that group is rebuilt.
1. Whenever a user who does not have 'edit all contacts' and 'view all contacts' attempts to do anything in CiviCRM, the ACL cache for that contact will be rebuilt.

This is likely not optimal for your site. There are settings and jobs you can adjust.

### Decide whether the caches need to be populated

- If your site does not use ACLs, CiviCRM will still attempt to populate the ACL caches but will have no data to put in them. In this case, there is no advantage to cleaning up the ACL caches. Clearing them, even when empty, is a known cause of deadlocks, which means the server cannot handle all requests and some fail.
- For smart groups, the choice is less clear-cut. Sites generally use smart groups, but use them differently. The smart group cache helps when you frequently use the same groups within the smart group timeout period, or when you want users to see all the groups a contact is a member of. The smart group cache (`civicrm_group_contact_cache`) was added for the latter scenario. Populating and clearing it have a high performance cost. This might be worth it on sites with a few thousand contacts but is likely to crash medium-sized or larger sites.

### Settings and cron jobs you can adjust

Not all these settings are exposed in the UI, but they can all be accessed through API Explorer.

- `contact_smart_group_display` (**Administer > Customize Data and Screens > Display Preferences**). By default, this is set to 'Show Smart groups on demand'. This means the group will show as a closed accordian and if the user wants to see all the contacts the person is a member of they can click to expand it from their groups tab. Depending on the size of your site and whether you have the cron set up to rebuild smart groups, this will either show the groups the contact is a member of or crash your site. Each smart group is a query, and the only way to know if a contact is in a given query is to run it. Every smart group query therefore needs to run to determine whether a contact is a member. Smart group caching was added to support this accordian. The ability to disable the accordian, but not to fully disable smart group caching, was added when it was discovered that it can bring a server to its knees. This is also why smart groups are not included when you export groups and are not shown on the My Contact dashboard.

- Rebuild Smart Group Cache [scheduled job](../setup/jobs.md). If the smart group accordian is enabled **and** used frequently, it may make sense to enable this job. It populates the smart group cache by running the query for every smart group. It only makes sense to run it if people expand the accordian more often than your smart group cache timeout. This cron can take a long time, crash other processes, and make cache clearing slower and more likely to crash because the cache holds more data.

- `smart_group_cache_refresh_mode` is not exposed in the UI. If you have access to set up cron jobs, you can set this to `TRUE` and set up a cron. Instead of attempting to clean up caches every time you edit a contact, it will do so when the cron runs. In general, queries that clear out `civicrm_group_contact_cache` are more likely to crash your site than those that build it, unless users are expanding the smart group accordian. This setting can change how often the clearing queries run from many times a second to every few minutes.

- Flush smart group cache job. In conjunction with the setting above, you can add a [scheduled job](../setup/jobs.md). Manually enter the entity ('Job') and the action ('group_cache_flush'). This should run slightly more often than you smart group cache timeout is set to.

- `acl_cache_refresh_mode` is not exposed in the UI. It works like `smart_group_cache_refresh_mode`, but for the ACL cache. Busy sites in particular will benefit from fewer deadlocks with this set. Constant conflicting attempts to clear this cache are a major source of deadlocks, even on sites with no ACLs configured.

- Flush ACL cache job. This is the same as the smart group cache flush job, but its action is `acl_cache_flush`. If you do not use ACLs, you do not need to configure this job, but you still need to add the setting above to get the performance benefit.

- `smartGroupCacheTimeout` (**Administer > Customize Data and Screens > Search Preferences**) controls how long the resolved contacts in a given group remain in the cache table before being cleaned out, on edit or via cron. Traditional wisdom is to set this between 5 and 10 minutes, but many sites will get better performance by setting it to zero. Consider how often your contacts access the same smart group more than once within 5 minutes. If a group is already cached, it may be quicker to retrieve, depending on how fast its query runs. However, more rows in the smart group cache table make it slower to resolve new groups into the table and to clear it out. The official recommendation to set this to 'at least 5 minutes' was written without testing on a real site. Experiment with this setting, including zero as an option.

## Exclude directories that do not need to be scanned

This was introduced in 5.29.

CiviCRM uses `CRM_Utils_File::findFiles()` to locate glob patterns of files, such as `*.info` files to find extensions and `*.xml` files. By default, it searches every directory under the docroot except those beginning with a dot, such as `.git`. Some directories may be large but will never contain what CiviCRM is looking for. Excluding them can make this process more efficient.

Provide a regex in the `CIVICRM_EXCLUDE_DIRS_PATTERN` constant in your `civicrm.settings.php` file. The regex matches file system *absolute* paths, such as `/var/www/example.org/sites/default/files/civicrm/ext`.

For example, depending on your environment, you might exclude:

- All directories starting with a dot (`.git`, `.svn`, `.secret`, `.env`, etc.).
- All `node_modules` directories, which can be enormous.
- All `js` and `css` directories, if you are sure CiviCRM does not need to look in them (it does not as of 5.29).
- All `bower_components`, `packages`, and `vendor` directories, which contain third-party library code.
- The `sites/default/files/private` directory, a local example of where Drupal's private managed files might be kept.

```php
<?php
if (strtoupper(substr(PHP_OS, 0, 3)) !== 'WIN' && !defined('CIVICRM_EXCLUDE_DIRS_PATTERN')) {
  define('CIVICRM_EXCLUDE_DIRS_PATTERN', '@/(\.|node_modules|js/|css/|bower_components|packages/|sites/default/files/private)@');
}
```

Depending on local factors, this can significantly speed up cache clears and extension installs; for example, a 10× improvement has been measured.

## If you use mysql replication, consider RPOW to reduce queries on production

The [RPOW](https://github.com/totten/rpow) extension can redirect read-only queries to another DB server. This can help if an occasional slow search causes hangs on your main server. Consider using REDIS as your cache methodology if you use RPOW, or if you can use it anyway.

<!-- Source: setup/optimizations.md -->
