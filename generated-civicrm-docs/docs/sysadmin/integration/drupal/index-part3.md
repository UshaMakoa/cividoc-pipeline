---
title: Synchronize CiviCRM groups with Drupal roles
category: how-to
topic: system-administration
subtopic: group-to-role-synchronization
component: CiviGroup Roles Sync
audiences:
- technical
- operations-user
- administrator
- event-manager
level: intermediate
journey_stage: manage-and-automate
summary: Prepare group-to-role associations and configure CiviGroup Roles Sync.
extensions: []
related: []
review_priority: medium
review_notes:
- The page alternates between “CiviGroup Roles Sync” and “CiviGroup Role Sync”; the source does not clarify whether these
  refer to the same name.
- The preparation section says “Group Types” when discussing which groups and roles to create; the intended distinction is
  unclear.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: integration/drupal/index-part3.md
destination_path: sysadmin/integration/drupal/index-part3.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/integration/drupal/index-part3/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# Synchronize CiviCRM groups with Drupal roles

The CiviGroup Roles Sync module lets administrators of Drupal Websites:

- Allow board members, committees, staff, and volunteers to access specific content or perform specific tasks.
- Provide customized experiences for users of specific groups when they access the website. For example, when a major donor logs in, the website could display a letter from the President thanking the donor for his contribution and participation, or provide major donors with pre-registration access to upcoming events and exclusive news or resources.

Assess how different users interact with your website. Consider whether their experience depends on organized groups, teams, committees, or task forces; whether a contact meets specific criteria; or whether you should apply roles manually.

In essence, the module synchronizes Drupal users who have a certain role with CiviCRM contacts in a certain group.

## Preparation

Before using CiviGroup Roles Sync module, prepare the following:

- Create your organization’s Groups.
- Create the roles needed for each use case in Drupal.
- If you use additional modules to fine-tune access, install and configure all the modules you need.

When determining what Groups and what Drupal Roles you should create, remember that multiple Group Types may grant the same Drupal Role and each Group can be used to grant multiple Drupal roles.

Enable the module from the Drupal module administration screen.

## Syncing CiviCRM groups to Drupal roles

1. Navigate to the CiviGroup Role Sync configuration screen.
2. Click **Add Association Rule.**
3. Under **CiviCRM Group**, select the Group that you want a user to have in order to be granted a specific Drupal Role.
4. Under **Drupal Role**, select the Drupal Role that should be granted.
5. Click **Add Association Rule** when you have finished configuring the new association rule.

You can edit or delete existing association rules from the same configuration screen.

The next time a user whose contact is in the CiviCRM group logs in, they will be granted the role associated with the group. If you remove them from the group, the role will be removed the next time they log in.

!!! note
    Unlike CiviMember Role Sync, which has configureable options for when synchronization happens, CiviGroup Role Sync only synchronizes on user login. If you have really long cookies on your site and don’t close users sessions, a user could stay logged in and continue to have a role in Drupal even after you have removed the user from the associate group in CiviCRM.

<!-- Source: integration/drupal/index-part3.md -->
