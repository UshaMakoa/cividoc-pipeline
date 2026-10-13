---
title: Upgrades
category: how-to
topic: system-administration
subtopic: upgrade-process
component: CiviCRM
audiences:
- technical
- administrator
level: intermediate
journey_stage: plan-and-configure
summary: Prepare for a CiviCRM upgrade and complete the checks needed afterward.
extensions: []
related: []
review_priority: medium
review_notes:
- The version numbers in the upgrade examples and the guidance for versions prior to 4.5.9 may need review.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: upgrade/index.md
destination_path: sysadmin/upgrade/index.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/upgrade/
civicrm_version:
- 4.7.2
- 4.7.3
- 4.7.20
- 4.7.31
- 5.49.0
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Upgrades

Keeping CiviCRM up-to-date helps you take advantage of new features and is critically important when [security updates](https://civicrm.org/security) are issued.

In general:

* The upgrade steps differ depending on your CMS.
* The upgrade steps are the same no matter which versions of CiviCRM you are moving _from_ and _to_ ([with some exceptions](version-specific.md)).
* The steps are the same for small upgrades (e.g. 5.49.0 to 5.49.1) and large upgrades (4.7.31 to 5.49.0).
* You can make big jumps in one upgrade (e.g. 4.7.20 to 5.49.0) without applying all the upgrades in between.
* If you are starting from a version prior to 4.5.9, [upgrade to 4.7](https://sourceforge.net/projects/civicrm/files/civicrm-stable/4.7.31/) as an interim step. The latest version does not contain upgrade code going back that far.

This page covers steps before and after an upgrade. For the upgrade itself, follow the CMS-specific page in this chapter.

## Before upgrading {:#before-upgrading}

1. Ensure that your system meets all the [requirements](https://docs.civicrm.org/installation/en/latest/general/requirements/) for the CiviCRM version to which you are upgrading.
1. Check for any [version-specific upgrade instructions](version-specific.md).
1. **[Backup your site](../setup/backups.md). Very important!**
1. Use your backup to create a _copy_ of your site (directories and database), and ensure that it works correctly. This tests your backup and restore procedure and gives you a low-stakes environment for testing the upgrade.
1. Test the upgrade process on your _copied site_ to ensure that it succeeds.
1. [Troubleshoot](../troubleshooting.md) any upgrade problems.
1. Once the *test* upgrade succeeds, apply the same steps on your live site.

## Upgrading

The steps vary depending on your CMS. Find the appropriate page in this chapter and follow its steps.

## After upgrading {:#after-upgrading}

### Flush caches

If you ran the upgrade on the command-line, flush caches by running `cv flush`. The upgrade web interface does this automatically.

### Evaluate new permissions

The CiviCRM post-upgrade messages should alert you if new CMS permissions are added. If so, [review and configure the CMS permissions](https://docs.civicrm.org/user/en/latest/initial-set-up/permissions-and-access-control/#cms-permissions).

### Update resource settings

If you ran the upgrade in a different directory from your previous version, you may need to update the configured **CiviCRM Resource URL** and **Extension Resource URL** settings. Missing icons and images, or problems with javascript functions and stylesheets, are symptoms that these settings need to be updated.

1. Go to **Administer CiviCRM » System Settings » Resource URLs**.
1. Refer to the field help on that screen for instructions.

### Update system workflow message templates

If users have customized system workflow message templates, merge their customizations with CiviCRM's template changes for each version upgrade.

<!-- Source: upgrade/index.md -->
