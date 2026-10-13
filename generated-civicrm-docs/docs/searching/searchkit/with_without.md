---
title: With (Optional) / With (Required) / Without
category: explanation
topic: search
subtopic: entity-joins
component: Search Kit
audiences:
- operations-user
level: intermediate
journey_stage: plan-and-configure
summary: Understand how joining additional entities changes the rows returned by a Search Kit search.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: searching/searchkit/with_without.md
destination_path: searching/searchkit/with_without.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/searching/searchkit/with_without/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# With (Optional) / With (Required) / Without

![Clause location](../../img/search-kit/with-without-clause-location.png)

When creating a new search, you first choose a starting entity. You can then add zero or more entities to include their fields as columns or to adjust which rows the search returns. For example, you might start with contacts and add addresses.

Each additional entity is *joined* to the starting entity and any entities already added. The join can be **With (optional)**, **With (required)**, or **Without**. Your choice determines which rows are returned: you might use a join to find contacts who have bought tickets for the Annual General Meeting, or contacts who have not yet bought tickets.

## With (optional)

**With (optional)** returns rows from the earlier entity or entities even when there is no match in the new entity. For Contacts With (optional) Contact Addresses, a Contact with no addresses still has a row in the results. Its Contact Addresses fields are empty/NULL.

![Contact search](../../img/search-kit/with-without-contact-search.png)

## With (required)

**With (required)** returns rows only when the earlier entity or entities have a match in the new entity. Contacts With (required) Contact Addresses excludes Contacts with no addresses and returns a row for every combination of a Contact and one of its addresses.

![Search result](../../img/search-kit/with-without-without-result.png)

## Without

**Without** returns rows only when the earlier entity or entities have no match in the new entity. Contacts Without Contact Addresses returns a row for each Contact with no Contact Address.

![Additional entity](../../img/search-kit/with-without-additional-entity.png)

For each entity you add, the choice of **With (optional)**, **With (required)**, or **Without** determines whether rows are added to or removed from the search results.

<!-- Source: searching/searchkit/with_without.md -->
