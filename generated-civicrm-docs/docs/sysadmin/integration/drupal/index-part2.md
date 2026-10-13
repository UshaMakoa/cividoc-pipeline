---
title: CiviCRM Organic Groups Sync
category: explanation
topic: system-administration
subtopic: organic-groups-synchronization
component: Organic Groups CiviCRM module
audiences:
- technical
level: intermediate
journey_stage: manage-and-automate
summary: Understand which groups the Organic Groups CiviCRM module creates and how one-way synchronization works.
extensions: []
related: []
review_priority: low
review_notes: []
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: integration/drupal/index-part2.md
destination_path: sysadmin/integration/drupal/index-part2.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/integration/drupal/index-part2/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# CiviCRM Organic Groups Sync

The [Organic Groups CiviCRM module](http://drupal.org/project/og_civicrm) integrates Organic Groups from a Drupal site with CiviCRM groups. It is useful for groups that require Organic Group functionality on their website but also need to be tracked within CiviCRM. Once a Drupal Organic Group is integrated into CiviCRM, the Drupal group can be used for mailings, tracking address information, tracking activities, or anything else normally done with CiviCRM contacts.

Once the Organic Groups CiviCRM module is installed and enabled in Drupal, it automatically creates two CiviCRM groups for each existing Drupal Organic Group:

- A normal group containing a contact record for each corresponding user in the Organic Group. This group has the same name as the linked Organic Group.
- An access control group containing the contact record of the corresponding Organic Group’s administrator. This gives the OG group admin the ability to view and edit members of their group in CiviCRM.

The groups are synchronized **one way only**, from Drupal Organic Groups to CiviCRM groups. When a new user is added to or signs up for an Organic Group, they are automatically added to the corresponding CiviCRM group. If they leave the Organic Group, they are removed from the CiviCRM group. If an Organic Group is deleted, the CiviCRM group is also deleted.

The reverse does not happen: adding a contact to the CiviCRM group does not add them to the Drupal Organic Group; removing a contact from the CiviCRM group does not remove them from the Drupal Organic Group; and deleting the CiviCRM group does not delete the Drupal Organic Group. This integration is therefore meant to be used when you administer the group from the Drupal side.

<!-- Source: integration/drupal/index-part2.md -->
