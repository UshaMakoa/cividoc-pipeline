---
title: Where
category: reference
topic: searchkit
subtopic: where-filters
component: SearchKit
audiences:
- operations-user
level: intermediate
journey_stage: reference-and-troubleshooting
summary: Understand how Where filters SearchKit results and how its comparison operators behave.
extensions: []
related:
- having.md
review_priority: low
review_notes:
- The final example describes primary and billing addresses, but its image alt text says "different email addresses"; verify
  the example before changing either.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: searching/searchkit/where.md
destination_path: searching/searchkit/where.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/searching/searchkit/where/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Where

**Where** filters data in the database before it is returned to SearchKit. To filter data after it is returned from the database, use [Having](having.md).

![Elements locations](../../img/search-kit/where-elements-locations.png)

## Description

A Where comparison has four main components:

1. The element you want to compare.
2. The “operator.”
3. The value (or field) to compare against.
4. Whether to compare with a value or a field.

In general, the operators are the same as the similarly-named arithmetic or SQL operators.

- **Matches Pattern** matches a regular expression pattern.
- **Is Like** matches a complete field, so you usually want to use it with wildcards to find parts of the field, like **%search term%**.
- **Contains** is useful for searching in serialized fields (fields that store multiple values together, such as *Contact Subtype*, which could be **Parent**, **Volunteer**, **Staff**). It matches only a full value like **Parent**, not parts of a value.
- Negated operators such as **Not Like**, **≠**, or **Doesn&#39;t Contain** won&#39;t match **NULL** fields that have no value. They only match fields that have a value and the value doesn&#39;t match the criteria. If you want **NULL** fields as well, you can search for **≠ searchterm** OR **Is Empty**.

This example only includes contacts whose email address contains ‘.gov’:

![Example email address .gov](../../img/search-kit/where-email-address-dot-gov.png)

This example includes contacts whose primary address is not the same as their billing address:

![Example different email addresses](../../img/search-kit/where-email-addresses-differ.png)

<!-- Source: searching/searchkit/where.md -->
