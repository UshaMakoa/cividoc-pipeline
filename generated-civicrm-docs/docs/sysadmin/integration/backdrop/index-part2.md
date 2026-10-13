---
title: Sync CiviCRM groups to Backdrop roles
category: how-to
topic: system-administration
subtopic: group-role-sync
component: CiviGroup Roles Sync
audiences:
- technical
- operations-user
- administrator
- event-manager
level: intermediate
journey_stage: manage-and-automate
summary: Prepare and configure associations that synchronize CiviCRM groups with Backdrop roles.
extensions: []
related: []
review_priority: low
review_notes:
- The source uses both CiviGroup Roles Sync and CiviGroup Role Sync for the module or its configuration screen.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: integration/backdrop/index-part2.md
destination_path: sysadmin/integration/backdrop/index-part2.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/integration/backdrop/index-part2/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# Sync CiviCRM groups to Backdrop roles

The CiviGroup Roles Sync module allows administrators of Backdrop Websites to:

- Allow board members, committees, staff, and volunteers to access specific content or perform specific tasks.
- Provide customized experiences for users of specific groups when they access the website. For example, when a major donor logs in, the website could display a letter from the President thanking the donor for his contribution and participation, or give major donors pre-registration access to upcoming events and exclusive news or resources.

Assess how different users interact with your website. Consider whether their experience depends on organized groups, teams, committees, or task forces; whether a contact meets specific criteria; or whether you should apply roles to users manually.

CiviGroup Roles Sync synchronizes Backdrop users who have a certain role with CiviCRM contacts in a certain group.

## Preparation

Before using CiviGroup Roles Sync module:

- Create your organization's Groups.
- Create the Backdrop roles needed for each use case.
- If you use additional modules to fine-tune access, install and configure all the modules you need.

When deciding which Groups and Backdrop Roles to create, remember that multiple Group Types may grant the same Backdrop Role, and each Group can grant multiple Backdrop roles.

Enable the module from the Backdrop module administration screen.

## Sync CiviCRM Groups to Backdrop Roles

1. Navigate to the CiviGroup Role Sync configuration screen.
2. Click **Add Association Rule.**
3. Under **CiviCRM Group**, select the Group a user must be in to receive a specific Backdrop Role.
4. Under **Backdrop Role**, select the Backdrop Role to grant.
5. Click **Add Association Rule** when you have finished configuring the new association rule.

You can edit or delete existing association rules from the same configuration screen.

The next time a user whose contact is in the CiviCRM group logs in, they will be granted the role associated with that group. If you remove them from the group, the role will be removed the next time they log in.

!!! note
    Unlike CiviMember Role Sync, which has configureable options for when synchronization happens, CiviGroup Role Sync only synchronizes on user login. If your site has really long cookies and you don't close users sessions, a user could stay logged in and continue to have a Backdrop role after you have removed them from the associated CiviCRM group.

<!-- Source: integration/backdrop/index-part2.md -->
