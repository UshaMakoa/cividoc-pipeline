---
title: Configure the front-end Contact Dashboard in Joomla
category: how-to
topic: system-administration
subtopic: joomla-front-end-menu
component: CiviCRM Dashboard
audiences:
- technical
- administrator
- membership-manager
level: basic
journey_stage: plan-and-configure
summary: Add the Contact Dashboard to a Joomla front-end menu and verify access to it.
extensions: []
related: []
review_priority: medium
review_notes:
- The permissions instruction contains the unclear text “Under Registered, l ook”; verify the intended wording before changing
  it.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: integration/joomla/dashboard.md
destination_path: sysadmin/integration/joomla/dashboard.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/integration/joomla/dashboard/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Configure the front-end Contact Dashboard in Joomla

CiviCRM can expose a **Contact Dashboard** where logged-in front-end users can view their subscribed groups, membership(s), contribution(s), and registered events. To make the dashboard available, add a link to a front-end site menu.

## Verify the Contact Dashboard in the Joomla Administrator interface

1. Navigate to **My Contact Dashboard** from the **CiviCRM Shortcuts** block on any CiviCRM page.
2. Check that you see contact-related information for the contact linked to your administrator record.

## Add “My Contact Dashboard” as a menu item

1. Login to Administrator if not already logged in.
2. Click **Menu** on the top navigation bar and select the menu you want to add the link to (for example, **mainmenu**).
3. Click the **New** icon (top right).
4. Click **Menu Item Type** and select **CiviCRM Dashboard** from the civicrm section.
5. Enter a **Name** for the menu item (e.g. “Contact Dashboard”).
6. Complete the remaining fields (Parent Item, Access Level, Published).

    !!! caution ""
        Do NOT use PUBLIC Access Level for this menu item. Users must be logged in to the front-end for this feature to work. Otherwise CiviCRM has no way to identify the person's contact record.

7. Click **Save & Close.**

## Verify permissions in CiviCRM

1. Navigate to your CiviCRM Home.
2. From the **Administer** menu, choose **Users & Permissions**, then **Permissions (Access Control)**.
3. Select **Joomla Access Control**.
4. Under **Registered, l** ook for **CiviCRM: Access Contact Dashboard.** Make sure this is set to **Allowed.**
5. Scroll to the top and click **Save & Close.**

## Test the front-end menu item

Navigate to your front-end site and test your new menu item.

<!-- Source: integration/joomla/dashboard.md -->
