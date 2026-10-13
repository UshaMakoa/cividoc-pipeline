---
title: Field transformations
category: reference
topic: search
subtopic: transformation-categories
component: Search Kit
audiences:
- operations-user
level: basic
journey_stage: reference-and-troubleshooting
summary: Learn what field transformations do and which categories are available in Search Kit.
extensions: []
related: []
review_priority: low
review_notes:
- The source links to MySQL documentation but does not identify which MySQL functions are implemented in Search Kit.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: searching/searchkit/field_transformations.md
destination_path: searching/searchkit/field_transformations.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/searching/searchkit/field_transformations/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Field transformations

Field transformations are formulas applied to fields in your result set. Examples include displaying another field if a value is missing, rounding a numeric value, counting occurrences, and summing values.

## Transformation categories

Transformations are organized into four categories:

- Comparison
- Text
- Math
- Aggregate (only available if you used Group By)

## Option details

See the MySQL documentation for more information:

- https://dev.mysql.com/doc/refman/8.0/en/built-in-function-reference.html
- https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html

Not all MySQL functionality has been implemented in the Search Kit.

<!-- Source: searching/searchkit/field_transformations.md -->
