---
title: Relative date filters
category: reference
topic: search
subtopic: available-filters
component: CiviCRM
audiences:
- operations-user
level: intermediate
journey_stage: reference-and-troubleshooting
summary: Look up the relative date filters that ship with CiviCRM and the date boundaries they define.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: searching/relative-date-formats.md
destination_path: searching/relative-date-formats.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/searching/relative-date-formats/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Relative date filters

The following relative date filters ship with CiviCRM. You can see the list on your site at the URL `civicrm/admin/options/relative_date_filters`. Some additional filters can be added within fairly tight constraints.

| value | Means | Defines |
| ---- | ---- | ---- |
| `current.month` | Current calendar month to-date | start and end |
| `current.year` | Current calendar year to-date | start and end |
| `current.quarter` | Current quarter to-date | start and end |
| `current.week` | Current week to-date | start and end |
| `previous_before.day` | Day prior to yesterday | start and end |
| `greater_previous.month` | From end of previous calendar month | start |
| `greater_previous.year` | From end of previous calendar year | start |
| `greater_previous.quarter` | From end of previous quarter | start |
| `greater_previous.week` | From end of previous week | start |
| `greater.month` | From start of current calendar month | start |
| `greater.year` | From start of current calendar year | start |
| `greater.day` | From start of current day | start |
| `greater.quarter` | From start of current quarter | start |
| `greater.week` | From start of current week | start |
| `ending.year` | Last 12 months including today | start and end (now) |
| `ending_2.year` | Last 2 years including today | start and end (now) |
| `ending_3.year` | Last 3 years including today | start and end (now) |
| `ending_30.day` | Last 30 days including today | start and end (now) |
| `ending_60.day` | Last 60 days including today | start and end (now) |
| `ending.week` | Last 7 days including today | start and end (now) |
| `ending_90.day` | Last 90 days including today | start and end (now) |
| `previous_before.month` | Month prior to previous calendar month | start and end |
| `starting.year` | Next 12 months including today | start (now) and end |
| `starting.month` | Next 30 days including today | start (now) and end |
| `starting_2.month` | Next 60 days including today | start (now) and end |
| `starting.week` | Next 7 days including today | start (now) and end |
| `starting.quarter` | Next 90 days including today | start (now) and end |
| `next.month` | Next calendar month | start and end |
| `next.year` | Next calendar year | start and end |
| `next.fiscal_year` | Next fiscal year | start and end |
| `next.quarter` | Next quarter | start and end |
| `next.week` | Next week | start and end |
| `previous_2.month` | Previous 2 calendar months | start and end |
| `previous_2.year` | Previous 2 calendar years | start and end |
| `previous_2.fiscal_year` | Previous 2 fiscal years | start and end |
| `previous_2.day` | Previous 2 days | start and end |
| `previous_2.quarter` | Previous 2 quarters | start and end |
| `previous_2.week` | Previous 2 weeks | start and end |
| `previous.month` | Previous calendar month | start and end |
| `previous.year` | Previous calendar year | start and end |
| `previous.fiscal_year` | Previous fiscal year | start and end |
| `previous.quarter` | Previous quarter | start and end |
| `previous.week` | Previous week | start and end |
| `previous_before.quarter` | Quarter prior to previous quarter | start and end |
| `this.month` | This calendar month | start and end |
| `this.year` | This calendar year | start and end |
| `this.fiscal_year` | This fiscal year | start and end |
| `this.quarter` | This quarter | start and end |
| `this.week` | This week | start and end |
| `less.month` | To end of current calendar month | end |
| `less.year` | To end of current calendar year | end |
| `less.quarter` | To end of current quarter | end |
| `less.week` | To end of current week | end |
| `earlier.month` | To end of previous calendar month | end |
| `earlier.year` | To end of previous calendar year | end |
| `earlier.quarter` | To end of previous quarter | end |
| `earlier.week` | To end of previous week | end |
| `earlier.day` | To end of yesterday | end |
| `this.day` | Today | start and end |
| `starting.day` | Tomorrow | start and end |
| `previous_before.week` | Week prior to previous week | start and end |
| `previous_before.year` | Year prior to previous calendar year | start and end |
| `previous_before.fiscal_year` | Fiscal year prior to previous fiscal year | start and end |
| `previous.day` | Yesterday | start and end |

<!-- Source: searching/relative-date-formats.md -->
