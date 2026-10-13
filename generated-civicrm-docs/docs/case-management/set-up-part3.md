---
title: Filing emails on cases
category: explanation
topic: mailings
subtopic: case-email
component: CiviCase
audiences:
- communications-manager
- operations-user
level: intermediate
journey_stage: manage-and-automate
summary: Understand the ways case-related emails and other activities can be filed on a case.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: case-management/set-up-part3.md
destination_path: case-management/set-up-part3.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/case-management/set-up-part3/
civicrm_version:
- latest
last_modified: '2026-10-06'
---

# Filing emails on cases

Some organizations find it useful to record case-related emails in CiviCase. For example, the coordinator of a work disability case might send an inquiry to a state agency representative and want both the sent email and the reply to become part of the case story.

You can send outbound emails directly from the Manage Case screen. You can also set up CiviCRM to integrate with your usual email client, so you can send and receive emails as usual and have them filed in CiviCRM.

The CiviMail chapter describes the Email Processor as a way to get inbound and outbound emails into CiviCRM as non-case activities. When you enable CiviCase, a new action becomes available to file any non-case activity onto a case. If the Email Processor has been set up, replies to email activities sent from the Manage Case screen will automatically be filed directly onto the case.

You can also record an email or an activity on a case by adding the string "case" to the subject field, followed by a space and the case's #id in square braces. For example, an activity or email with the subject **"[case #123] Any subject"** would be recorded under case id = 123.

<!-- Source: case-management/set-up-part3.md -->
