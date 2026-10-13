---
title: Adding new relative date filters
category: how-to
topic: search
subtopic: adding-filters
component: CiviCRM
audiences:
- operations-user
level: intermediate
journey_stage: plan-and-configure
summary: Use the supported patterns to add relative date filters.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: searching/relative-date-formats-part2.md
destination_path: searching/relative-date-formats-part2.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/searching/relative-date-formats-part2/
civicrm_version:
- latest
last_modified: '2026-10-06'
---

# Adding new relative date filters

The code for some of the patterns supports the addition of more filters (via the api or the URL `civicrm/admin/options/relative_date_filters`).

Making other patterns more flexible is generally 'patch-welcome'—the hardest part is the non-code part: figuring out what the definition is and how it relates to the other patterns.

## ending

The trick to the `ending` prefix is that it is a 'count backwards from now' type filter. If you are in the middle of a month and you use `ending`, it will start from the middle of the relevant month (if it's the 15th today then it would start from the 16th of the month).

Additional filters can be added with the syntax below, where 3 can be any number you choose:

- `ending_3.day` - Last 3 days, including today
- `ending_3.week` - Last 3 weeks, including today, equivalent to `ending_21.day`
- `ending_3.month` - Last 3 months, including today, e.g if today is 25 Dec 2021 then from 26 Sep 2021)
- `ending_3.quarter` - Last 3 quarters, including today - equivalent to `ending_9.month`
- `ending_3.year` - Last 3 years, including today (e.g if today is 25 Dec 2021 then from 26 Dec 2018)

## this

The `this` term works in full date units—for example, `this_3.year` starts from 1 Jan and ends on 31 December. So if today is 25 December 2021 then `this_3.year` runs from 1 Jan 2019 to 31 December 2021.

- `this_3.day` - Last 3 days, including today - equivalent to ending_3.day
- `this_3.week` - From start of two weeks ago to end of this week (total of 3)
- `this_3.month` - From start of two months ago to end of this month (total of 3)
- `this_3.quarter` - From start of two quarters ago to end of this quarter (total of 3)
- `this_3.year` - From start of two years ago to end of this year (total of 3)
- `this_3.fiscal_year` - From start of 2 fiscal years ago to end of this fiscal year (total of 3 years)

<!-- Source: searching/relative-date-formats-part2.md -->
