---
title: URL filter support in searches
category: reference
topic: search
subtopic: url-filters-and-date-formats
component: CiviCRM search
audiences:
- event-manager
- administrator
- operations-user
level: advanced
journey_stage: reference-and-troubleshooting
summary: Look up supported search URL parameters and the date formats used in their values.
extensions: []
related:
- ../searching/searchkit/connecting-searchkit-to-formbuilder.md#url-filters-in-search-forms
- ../the-user-interface/formbuilder/pre-filling-custom-forms.md
- ../searching/relative-date-formats.md
review_priority: medium
review_notes:
- The example URL repeats reset=1; verify whether the repetition is intentional.
- The invoice_number row uses invoice_number_reason in its example, the cancel_reason row describes a contribution source,
  and the participant_registration_date_relative row uses a different parameter spelling in its example; verify these discrepancies
  without changing the supplied values.
- The version-specific table entries and statement about the Automatic Wildcard performance setting may need verification.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: searching/searching-part2.md
destination_path: searching/searching-part2.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/searching/searching-part2/
civicrm_version:
- latest
last_modified: '2026-10-06'
---

# URL filter support in searches

In some cases, you can bookmark search URLs with parameters to revisit searches quickly. This page covers Advanced Search and component searches, such as 'Find Contributions'. URL filtering for SearchKit is discussed on the [SearchKit interface page.](../searching/searchkit/connecting-searchkit-to-formbuilder.md#url-filters-in-search-forms) and the [FormBuilder form page](../the-user-interface/formbuilder/pre-filling-custom-forms.md).

To construct a parameterised URL:

1. Ensure the URL contains 'reset=1&force=1' after the question mark.
2. Add supported parameters.

!!! note "Date/Time Parameters"
    Date/time parameters require that, either, the time component is omitted entirely `20200101` or specified with a full **six digit** time `20200101235959`

For example, the following URL works on Drupal *(with Clean URL support)* to find contributions made by a person with a name like `Bob`, a contribution source like `dad`, and a contribution date on or before `01 Jan 2018`:

`civicrm/contribute/search?reset=1&reset=1&force=1&sort_name=bob&receive_date_high=20180101&contribution_source=dad`

The following parameters work in a standardised way for contribution searches:

| Field | Example | Comments | Min version (where known) |
|-----|-------|-------|-------|
| sort_name | sort_name=bob | Sort name is like `bob%` or `%bob%` depending on your site config \* | |
| contribution_source | contribution_source=dad | Contribution source like `%dad%` or 'dad%' \* | |
| cancel_reason | cancel_reason=dunno | Contribution source like `%dunno%` or `dunno%` \* | |
| invoice_number | invoice_number_reason=xyz | Invoice Number like `%xyz%` or `xyz%` \* | |
| contribution_page_id | contribution_page_id=1 | | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15785) |
| receive_date_high | receive_date_high=20180101132323 | Contribution received on or before 01 Jan 2018, 1.23 pm | |
| receive_date_low | receive_date_low=20161001 | Contribution received on or after 01 Oct 2016 | |
| receive_date_relative | receive_date_relative=this.year | Contribution received this year | |
| contribution_cancel_date_high | contribution_cancel_date_high=20180101132323 | Contribution cancelled on or before 01 Jan 2018, 1.23 pm | |
| contribution_cancel_date_low | contribution_cancel_date_low=20161001 | Contribution cancelled on or after 01 Oct 2016 | |
| contribution_cancel_date_relative | contribution_cancel_date_relative=this.year | Contribution cancelled this year | |
| event_high | event_high=20190101000000 | Event end date on or before 1 January 2019 | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15791) |
| event_low | event_low=20190101000000 | Event Start date on or after 1 January 2019 | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15791) |
| event_relative | event_relative=this.year | Event Start Date on or after ths start of this year and the event end date on or before the end of the year | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15791) |
| participant_registration_date_high | participant_registration_date_high=20190101000000 | Participant Registration Date on or before 1 January 2019 | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15791) |
| participant_registration_date_low | participant_registration_date_low=20190101000000 | Participant Registration date on or after 1 January 2019 | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15791) |
| participant_registration_date_relative | participant_registration__date_relative=this.year | Participant Registration Date on or after ths start of this year and the event end date on or before the end of the year | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15791) |
| participant_status_id | participant_status_id=1,2 | Participant Status in Registered and Pending Pay Later | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15791) |
| participant_role_id | participant_role_id=1,2 | Participant Role IN (Attendee, Host) | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15791) |
| case_start_date_high | case_start_date_high=20190101000000 | Case Start Date on or before 1 January 2019 | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15920) |
| case_start_date_low | case_start_date_low=20190101000000 | Case Start Date on or after 1 January 2019 | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15920) |
| case_start_date_relative | case_start_date_relative=this.year | Case Start Date on or after the start of this year and on or before the end of the calendar year | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15920) |
| case_end_date_high | case_end_date_high=20190101000000 | Case End Date on or before 1 January 2019 | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15920) |
| case_end_date_low | case_end_date_low=20190101000000 | Case End Date on or after 1 January 2019 | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15920) |
| case_end_date_relative | case_end_date_relative=this.year | Case End Date on or after the start of this year and on or before the end of the calendar year | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15920) |
| case_type_id | case_type_id=1,2 | Case Type is one of Housing Support or Adult Care Support | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15920) |
| case_status_id | case_status_id=1 | Case Status is Opened | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15920) |
| case_subject | case_subject=test | Case subject like `%test%` | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15920) |
| case_deleted | case_deleted=1 | Case is deleted | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15920) |
| case_id | case_id=1 | Case id = 1 | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15920) |
| case_owner | case_owner=2 | Only My Cases | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15920) |
| case_tags | case_tags=1,2 | Case Tags in (1,2) | 5.21 [PR](https://github.com/civicrm/civicrm-core/pull/15920) |

\* Whether text fields search for LIKE `%dad%` or LIKE `dad%` depends on the site wide setting 'Automatic Wildcard' under **Administer CiviCRM -> Customize Data and Screens -> Search Preferences**. For large sites turning this off gives a significant performance improvement but it means that searching for 'dad' will return 'daddy' but not 'grandad'.

## Date formats

In general, there are two types of date formats to use:

1. `_high` or `_low` fields take an 8- or 14-digit number representing Year, Month, Day and, optionally, Hour, Minute and Second. For example, `20180921235959` means 21 September 2018 at 23 hours, 59 minutes and 59 seconds. Leaving off `235959` means zero o’clock—that is, midnight.
2. Relative date fields. See [the list](../searching/relative-date-formats.md).

<!-- Source: searching/searching-part2.md -->
