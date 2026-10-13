---
title: What is CiviReport?
category: explanation
topic: reporting
subtopic: civireport-overview
component: CiviReport
audiences:
- operations-user
- administrator
- fundraising-manager
- membership-manager
level: basic
journey_stage: overview
summary: Learn what CiviReport does and how organisations use reports for fundraising, financial tracking, and household contributions.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: reporting/what-is-civireport.md
destination_path: reporting/what-is-civireport.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/reporting/what-is-civireport/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# What is CiviReport?

Reporting helps your organisation evaluate its impact and achieve its mission. Funders or other stakeholders may require reports. CiviReport lets you create, run and schedule reports based on the data CiviCRM holds about your contacts and their interactions with your organisation.

Reports query the database using the criteria and fields available in a report template. You can view a report on the page when you run it, display it as a dashlet on the dashboard, or receive it by scheduled email. An emailed report can include a CSV file or PDF.

## Scenario: a simple report to help with fundraising

1two3, a support organisation for street workers, has launched a capital campaign to raise money for a new shelter. Anne, the development director, wants to contact donors who made a large donation last year but have not given this year.

Anne creates an instance of the LYBUNT report (“Last year but unfortunately not this”) and filters it to show people who gave more than €500 last year. She runs the report and uses the Add to Group button to put these donors in a new group. She can then email everyone in the group about the capital campaign.

She also adds the report to her CiviCRM Dashboard to review progress in getting these prior donors to contribute. Anyone who donates automatically drops off the list because they no longer meet the criteria. The people remaining in the dashlet can be contacted by phone or through other personalised follow-up.

## Scenario: a regular financial report

WAM is an academic membership organisation with about 1,500 members. Members renew online and pay either online by card or offline by direct debit. Mark, the finance officer, needs several reports to track incoming money. Automating these reports was a key reason for implementing CiviCRM.

Mark receives the regular reports by email with CSV attachments. He imports the details into either the organisation’s accounting software or its online banking interface. WAM’s requirements were fairly complex, so some custom report templates were needed alongside the standard ones.

Every Monday morning, Mark receives a list of all completed online payments from the previous week to import into Sage. The report includes each payment’s amount and time, what it was for (membership or event), and a reference ID that links it back to the record in CiviCRM.

At the end of each month, he receives a list of members who pay by direct debit and whose memberships are due to expire the following month. He imports part of the list into the online banking interface to set up direct debit payments for those renewals.

These email reports save Mark several hours a month, allowing him to focus on other issues affecting the management of WAM’s financial resources.

## Scenario: determining total contributions for a household

A non-profit organisation in Ohio keeps records of individuals organised by household. For example, a husband may have attended several paid events while his wife has registered for other events and made separate donations.

Staff want to see the total contributions received from everyone in a household. If someone calls to ask about a donation or event payment made by another family member, staff can run the Donation Summary Report (Household) using the household’s name. The report gives them the contributions and related information they need to answer the caller’s questions.

<!-- cividoc:popular-extensions:start -->
## Popular extensions

These are widely used extensions in the relevant category of the official CiviCRM Extensions Directory. Usage is a popularity signal, not a compatibility or suitability guarantee.

- [Extended Reports](https://civicrm.org/extensions/extended-reports) — reported usage: 2,399
- [SearchKit Tokens](https://civicrm.org/extensions/searchkit-tokens) — reported usage: 1,733
- [Chart Kit](https://civicrm.org/extensions/chart-kit) — reported usage: 1,187
- [Export to native Excel](https://civicrm.org/extensions/export-native-excel) — reported usage: 959
- [Civisualize](https://civicrm.org/extensions/civisualize-missing-data-visualization-extension) — reported usage: 718

[All extensions for this component](https://civicrm.org/extensions?category=126)

Check development status, current CiviCRM compatibility, CMS requirements, and release notes before installation.

Usage snapshot reviewed: 2026-10-13.
<!-- cividoc:popular-extensions:end -->

<!-- Source: reporting/what-is-civireport.md -->
