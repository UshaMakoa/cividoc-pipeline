---
title: Importing related contact data
category: how-to
topic: contacts
subtopic: contact-relationships
component: Contacts
audiences:
- operations-user
- administrator
- membership-manager
level: intermediate
journey_stage: everyday-tasks
summary: Import related contacts in separate files and link them using an external identifier.
extensions: []
related: []
review_priority: medium
review_notes:
- The parent–child example describes linking a father to a child using the ‘Child of’ relationship type; the intended relationship
  direction is unclear.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: common-workflows/importing-data-into-civicrm-part2.md
destination_path: common-workflows/importing-data-into-civicrm-part2.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/common-workflows/importing-data-into-civicrm-part2/
civicrm_version:
- latest
last_modified: '2026-10-06'
---

# Importing related contact data

Import a separate CSV file for each type of related data, such as organisational addresses with employees, parent–child relationships, activities or contributions.

CiviCRM has specific tools for importing related contact data, and specific import tools for contributions, memberships and event participation. See their respective chapters for details. To import relationships, run multiple contact imports.

For example, importing a child and both parents takes three imports: one for the child, one for the father and one for the mother.

1. Import the child with an external identifier that can be used to match the child to the parents.
2. Import the father as a related contact, linking him to the child using the child’s external identifier.
3. Import the mother as a related contact in the same way.

In the example below, one CSV file contains both father and mother information. It is used twice during the import. The images show the fields used.

![Parent1a](../img/CiviCRM-AddingImporting-Parent1a-en.png "Parent1a")

![Parent1b](../img/CiviCRM-AddingImporting-Parent1b-en.png "Parent1b")

The father is linked to the original child using the external identifier, and the related father name is imported using the ‘Child of’ relationship type.

After the import, search for the parent and examine the relationship tab. The parent should have a relationship linking them to the child. Repeat the process for the mother and for other relationships as necessary.

<!-- Source: common-workflows/importing-data-into-civicrm-part2.md -->
