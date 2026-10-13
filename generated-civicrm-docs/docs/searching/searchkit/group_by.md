---
title: Group by
category: explanation
topic: searchkit
subtopic: grouping-search-results
component: SearchKit
audiences:
- operations-user
- fundraising-manager
level: basic
journey_stage: reports-and-review
summary: Understand how Group By organizes search results and supports analysis of grouped data.
extensions: []
related: []
review_priority: low
review_notes:
- The example grouping by both Country and Address (primary) State/Province says there is one row for each State/Province,
  but does not clarify how Country affects those rows.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: searching/searchkit/group_by.md
destination_path: searching/searchkit/group_by.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/searching/searchkit/group_by/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Group by

“Group By” organizes data around one or more common elements of the selected entity. When you execute the search, the results display one row per value of the selected “Group By” fields.

For example, searches of Contacts can group results by **Created Date**, **Contact Subtype**, and **Location** information, among other options. Searches of **Contributions** can group results by **Contribution Date**, **Amount**, and **Payment Method**, among other options.

![Group by example](../../img/search-kit/group-by-01-group-results-by.png)

## Analyze grouped results

“Group By” can help you analyze patterns and relationships in your data by counting, totalling or averaging numeric information, or concatenating data in other fields.

For example, if you’re looking at contacts and their addresses, you can group the results by **Country**.

![Group by Country example](../../img/search-kit/group-by-02-%20group-results-by-country.png)

In this use case, the results display a count of contacts per **Country**, because search results display one row per element selected.

If you add more than one “Group By” option, additional rows will display upon clicking “Search” for the elements selected. For example, if you group results of your search by **Country** and “**Address (primary) State/Province**”, one row will display for each State/Province of data in the system.

You can drag search result columns left or right to change their display order. If you change the order of the columns, click “Search” again for your results to display.

<!-- Source: searching/searchkit/group_by.md -->
