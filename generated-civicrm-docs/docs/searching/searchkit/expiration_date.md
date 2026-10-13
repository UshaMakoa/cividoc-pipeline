---
title: Expiration date
category: explanation
topic: search
subtopic: expiration-dates
component: Search Kit
audiences:
- operations-user
level: basic
journey_stage: manage-and-automate
summary: Understand how an expiration date affects the display of a saved search.
extensions: []
related: []
review_priority: low
review_notes:
- The images are needed to understand where the expiration date is set; the page does not describe the control in text.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: searching/searchkit/expiration_date.md
destination_path: searching/searchkit/expiration_date.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/searching/searchkit/expiration_date/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Expiration date

Some searches are useful only for a defined period. You can set a date for a saved search to be removed from the list instead of manually cleaning up saved searches.

## How expiration works

The expiration date is set:

![Expiration date](../../img/search-kit/expiration-date-01-date-set.png)

The search is given an expiration date:

![Search is given an expiration date](../../img/search-kit/expiration-date-02-expiration-date-set.png)

Searches are not deleted after the expiry date; they are only hidden from the display. They can only be restored to the display by deleting the expiry date via the API explorer or SQL statement.

<!-- Source: searching/searchkit/expiration_date.md -->
