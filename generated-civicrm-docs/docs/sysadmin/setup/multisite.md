---
title: CiviCRM multisite
category: explanation
topic: system-administration
subtopic: domains-and-settings
component: CiviCRM multisite
audiences:
- administrator
- operations-user
- communications-manager
- membership-manager
level: intermediate
journey_stage: overview
summary: Understand how CiviCRM domains relate to sites, settings, and levels of multisite support.
extensions: []
related: []
review_priority: medium
review_notes:
- The settings guidance refers to version 4.1 and should be reviewed for age.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/multisite.md
destination_path: sysadmin/setup/multisite.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/multisite/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# CiviCRM multisite

## What is multisite / multi domain

CiviCRM has built-in support for multisite access: several separate sites accessing the same CiviCRM database. This differs from the Drupal concept of multisite, which means a shared codebase. In most cases, a site is defined by a distinct URL.

These sites could be:

* Part of a Drupal 'domain module' install, hosted within the same database
* In separate databases sharing a user table (if you do this, you probably want the [multisite permissioning extension](https://lab.civicrm.org/extensions/multisite) or another piece of code to help you keep uf matches in sync)
* In separate databases with their own user table
* In dissimilar databases, e.g. Drupal 7 & Drupal 8 multisites (this can be a good migration technique)

CiviCRM has no idea which of these configurations you are using and does not need to know.

You can select from different levels of multisite-ness:

| Level | impact |
| ---- | ---- |
| Separate domain records but the database is not configured as a multisite | This basically means you specify the domain in your civicrm.settings.php file. CiviCRM is not really aware of this. Where a table is domain specific it will select the rows that relate to that domain. |
| Separate domain records with the site configured as a multisite | In addition to the above you select the box that defines the site as a multisite and specify a domain group. Contacts created on this site will be added to this group & groups created on this site will be made sub-groups of this group or associated with the group via a shared group organisation. You do not need to make the top level site multisite-aware unless you specifically want contacts on that site to be added to a group (large hierarchical groups can affect performance) |
| Separate domain records with multisite permissioning | By installing the multisite module on top you cause people on each domain who don't have 'view all contacts' permission or 'edit all contacts' to only see contacts in that domain |

## Multisite v settings management

Since 4.1 it has been possible to manage having different urls and other settings per site by over-riding settings (those which are stored in civicrm_settings.php) in the civicrm.settings.php file.

Setting overrides can handle:

* different urls
* different directories
* different WysiWIG editors
* different search options

Use different domains if you want:

* domain specific membership types
* domain specific payment processors
* domain specific different from addresses from CiviMails
* domain specific link back URLS in CiviMails
* domain specific domain contact details
* domain specific SMS Providers

<!-- Source: setup/multisite.md -->
