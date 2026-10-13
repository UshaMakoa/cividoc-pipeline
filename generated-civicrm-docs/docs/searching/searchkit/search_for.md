---
title: Search For
category: reference
topic: searchkit
subtopic: search-for-entities
component: SearchKit
audiences:
- operations-user
- event-manager
- fundraising-manager
- membership-manager
level: basic
journey_stage: reference-and-troubleshooting
summary: Identify the primary entities available in Search For and the optional ways to modify or group a search.
extensions: []
related: []
review_priority: medium
review_notes:
- The Activity description says “Past of future actions”; its intended meaning is unclear, so the wording has been retained.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: searching/searchkit/search_for.md
destination_path: searching/searchkit/search_for.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/searching/searchkit/search_for/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Search For

Specify the primary entity (contact, activity, contribution, etc) that you’d like to include in this searchkit query.

![Search For - specify primary entity](../../img/search-kit/search-for-01-specify-entity.png)

## Primary entities

The primary entities available through the Search For command are:

* **Activity** - Past of future actions concerning one or more contacts.
* **Contacts** - Individuals, organizations, households, etc.
* **Contributions** - Financial records consisting of transactions, line-items, etc.
* **Events** - Scheduled in-person or online events which contacts can register for and attend.
* **Grants** - Funds applied for and given out by this organization.
* **Individuals** - Contacts of type Individual.
* **Memberships** - Records of contacts belonging to an organization’s membership program.
* **Organizations** - Contacts of type Organization.
* **Participants** - Records of contacts’ attendance and roles in events.
* **Pledges** - Promises to contribute [to an organization] at a future time, either in full, or at regular intervals until a total goal is reached.
* **More** - Other, less-commonly search entities:
    * A long list of less-commonly searched entities.
    * See the list for explanations of the entities, similar to the above.

## Modifiers and grouping

Once a Search For entity is selected, optional modifier entities are available to be selected, per top-level entity. Each has an appropriate description that assists with construction of the full search capability.

In addition, the results of the searched for entity can be (optionally) grouped, again, with options that depend on the top level entity selected. Each has an appropriate description that assists with construction of the full search capability.

<!-- Source: searching/searchkit/search_for.md -->
