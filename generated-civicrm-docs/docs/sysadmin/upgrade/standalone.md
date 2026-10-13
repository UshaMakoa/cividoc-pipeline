---
title: Upgrade CiviCRM Standalone
category: how-to
topic: system-administration
subtopic: upgrade-procedure
component: CiviCRM Standalone
audiences:
- technical
level: intermediate
journey_stage: manage-and-automate
summary: Upgrade CiviCRM Standalone to the latest CiviCRM release.
extensions: []
related: []
review_priority: low
review_notes: []
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: upgrade/standalone.md
destination_path: sysadmin/upgrade/standalone.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/upgrade/standalone/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Upgrade CiviCRM Standalone

Follow these steps to upgrade CiviCRM Standalone to the latest CiviCRM release.

!!! caution "Before upgrading"
    Make sure you have done the steps listed in [before upgrading](index.md#before-upgrading) first.

## Download the latest code

1. Go to the [CiviCRM website](https://civicrm.org/download).
1. Select the latest currently available CiviCRM Standalone archive, such as `civicrm-x.y.z-standalone.tar.gz`.

If you are installing directly on the command line, you will probably find it easier to download directly to the target directory on your server with the following command, corrected for your version:

`wget https://download.civicrm.org/civicrm-x.y.z-standalone.tar.gz`

## Unpack the archive file

Unpack the archive somewhere other than where you did the original install to avoid unintentionally overwriting files:

`tar xzf civicrm-x.y.z-standalone.tar.gz`

## Perform the upgrade

1. Back up the `core` directory in your installation by copying it to another location.
1. Copy the `core` directory from the new download into your installation directory.
1. Visit your CiviCRM database upgrade page and click the "upgrade now" button:

    `https://example.org/civicrm/upgrade?reset=1`

    You should see an **Upgrade successful** message when the upgrade completes.

1. If you receive any errors during the process, note the exact error message and check for solutions on [Stack Exchange](https://civicrm.stackexchange.com/) or [Mattermost](https://chat.civicrm.org).
1. Click the **Return to CiviCRM home page** or **Return to CiviCRM status page** link.
1. Confirm that you are running the latest CiviCRM version by checking the version and revision in the page footer. You may need to refresh the browser screen a couple times to clear out your local cache and ensure the layout loads correctly.
1. Browse the CiviCRM features that your organization uses. If you notice unexpected behaviors or error messages, refer to the trouble-shooting section below.

See these steps to take [after upgrading](index.md#after-upgrading).

<!-- Source: upgrade/standalone.md -->
