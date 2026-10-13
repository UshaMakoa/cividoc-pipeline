---
title: What you need to know about CiviReport
category: explanation
topic: reporting
subtopic: planning-reports
component: CiviReport
audiences:
- operations-user
- administrator
- membership-manager
- fundraising-manager
level: basic
journey_stage: plan-and-configure
summary: Understand CiviReport concepts and the questions to consider when planning reports.
extensions: []
related: []
review_priority: medium
review_notes:
- The statements about what future versions may include and what the current report interface supports are time-sensitive
  and should be reviewed.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: reporting/what-you-need-to-know.md
destination_path: reporting/what-you-need-to-know.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/reporting/what-you-need-to-know/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# What you need to know about CiviReport

This page explains ideas that are useful when planning your use of CiviReport. System administrators should read it before configuring CiviReport for daily use. It is also useful for anyone who wants to understand the thinking behind CiviReport. If you only want to use reports already configured by your administrator, you can skip it.

CiviReport can support organisational planning and analysis of membership or donor development. It can produce tabular or graphical output, and reports can be set up to email specific people on a schedule.

The questions an organisation might ask about its data are almost unlimited. CiviCRM aims to cover 90% of scenarios while allowing administrators and developers to extend the system for the remaining 10%.

## Key concepts

### Report templates

A report template is the basis for creating any number of reports. CiviCRM includes predefined report templates for creating specific reports. For example, the Membership Report(Detail) template can be used to create one report showing student members who joined your organisation in the past quarter and another showing memberships cancelled this year.

These templates address basic needs of non-profits and organisations, and future versions of CiviCRM are likely to include more. You can create templates for your organisation’s requirements and contribute them to the CiviCRM community for others with the same reporting needs. Writing a new report template requires PHP and SQL skills. See the Developer Guide for details.

### Reports vs. searches

CiviCRM’s inbuilt search functionality covers most scenarios. CiviReport helps users display complex information about their data and present answers to questions in accessible ways. It is useful when you need to ask the same question, or similar questions, repeatedly.

The current report interface does not support most common batch actions, such as Update via Batch Profile and Smart Group creation. If you want to perform an action against a result set, use search rather than a report.

Reports can be more flexible than searches in some cases, and each has its own features. For example, reports let you change the columns displayed. In summary reports, you can order by whichever display results you choose.

### Report options

- **Run the report:** Use **Print Report** to view it in a browser, generate a PDF, or Export to CSV. Each option runs the report once when you hit the button and lets you work with the result.
- **Dashlet:** If you make a report **Available for Dashboard**, users with appropriate permissions can add it to their dashboard. This is useful for information they want to see regularly, such as new members or donations this month. The report runs every time the dashboard loads.
- **Email:** Schedule a regular email of a report. For example, a finance office could receive a monthly report of event fees received, or a membership administrator could receive a weekly report of overdue renewals.

### Detail and summary reports

Reports often come in pairs: one shows a summary and the other shows detail. They can be linked so users can see information at a glance and drill down into a report for more detail.

## Questions to consider

- Should you use CiviReport for this task, or would a search work better?
- What reports are available? The list is constantly growing. For a complete list available in your version, with explanations of how to use them, see **Create reports from templates** in the **Reports** dropdown menu.
- What do you want to ask about your data? For example, how many new members joined in a certain period, or how much money was collected during a fundraising campaign?
- What fields do you need to include?
- Does the report provide enough options, or will you need to analyse the results further in a spreadsheet?
- Is this a one-off report, or will you run it regularly? Could you make a report template to streamline future reports?
- Who needs to see the report? Does it contain sensitive information that should be available only to privileged users, or useful daily updates for everyone?

Details of available report templates and comparisons with searches appear for each component throughout the rest of this book. Refer to the relevant section for more about component-specific reports.

<!-- Source: reporting/what-you-need-to-know.md -->
