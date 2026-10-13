---
title: What is CiviContribute?
category: explanation
topic: contributions
subtopic: overview
component: CiviContribute
audiences:
- fundraising-manager
- operations-user
- administrator
- event-manager
level: basic
journey_stage: overview
summary: Learn what CiviContribute records and how an arts group uses it to manage workshop income.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: contributions/what-is-civicontribute.md
destination_path: contributions/what-is-civicontribute.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/contributions/what-is-civicontribute/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# What is CiviContribute?

CiviContribute is the component that lets you record and report on financial and in-kind contributions to your organization. It allows you to:

- accept donations and other financial or in-kind contributions
- process membership signups and renewals
- accept and manage events fees
- run specific fundraising campaigns
- let your supporters fundraise for you through personalised campaign pages
- quickly enter contribution and membership payments using "batches"
- export batches of financial transactions to import to your accounting software
- report and evaluate fundraising results and trends

Throughout CiviCRM, the term *contribution* refers to any financial transaction or payment taking place in the system, such as a donation, event fee payment or membership fee payment. It also includes in-kind contributions.

## Scenario: contributing to leadership

A community arts group, Arts in Action, conducts leadership workshops for youth under 25 throughout the year. They use CiviCRM extensively to plan and run the workshops, combining CiviEvent and CiviContribute to make administration as efficient as possible.

The workshops are funded in three ways: participant fees, local arts funding, and donations. Most donations come from previous workshop participants who have continued as Arts in Action constituents.

Twice a year, Arts in Action sends a call for workshop donations using CiviMail, with a link to a donations page on the site. Some donors make recurring donations; others make one-off donations. A thank-you email and receipt is automatically sent to every donor when a payment is successfully processed. All donations are tagged for the workshops, so staff can report on total workshop donations and look at individual contact records to see who has donated.

Participants register and pay for workshops through an online form. Registration has a flat fee, with additional fees for optional workshops, food and lodging preferences. Participants make their choices in the form and pay by credit card. If a participant is not already a contact in the database, a new record is created at registration. The payment is recorded in that contact's contribution record, which is also linked to the workshop event.

Arts in Action also lets participants pay later. Many do not have a credit card and need to pay in cash at the workshop. CiviContribute distinguishes an actual payment from a commitment to pay. That information appears in the registrants report, which is printed and used on the day to check attendance and payment. At the workshop registration desk, a computer is used to manually enter cash and cheque payments in each participant's contribution record.

Arts in Action has assessed that word of mouth and participants bringing friends are the most effective ways to publicise the workshops. They enable participants to forward the registration link to friends through the "tell-a-friend" mechanism. After completing the registration form, participants can forward it by email or social networking platforms to friends and colleagues who may also be interested in attending.

After every workshop, the Arts in Action accountant uses a report template to generate a report showing the workshop's total income from each of the three sources. Staff also track donation trends and make sure the Board knows who the larger donors are. Key statistics are displayed graphically on staff members' CiviCRM dashboard.

<!-- cividoc:popular-extensions:start -->
## Popular extensions

These are widely used extensions in the relevant category of the official CiviCRM Extensions Directory. Usage is a popularity signal, not a compatibility or suitability guarantee.

- [CiviSEPA — SEPA Direct Debit Extension](https://civicrm.org/extensions/civisepa-sepa-direct-debit-extension) — reported usage: 925
- [no overwrite](https://civicrm.org/extensions/no-overwrite) — reported usage: 918
- [Summary Fields](https://civicrm.org/extensions/summary-fields) — reported usage: 663
- [Line Item Editor](https://civicrm.org/extensions/line-item-editor) — reported usage: 565
- [Percentage Price Field](https://civicrm.org/extensions/percentage-price-field) — reported usage: 385

[All extensions for this component](https://civicrm.org/extensions?category=94)

Check development status, current CiviCRM compatibility, CMS requirements, and release notes before installation.

Usage snapshot reviewed: 2026-10-13.
<!-- cividoc:popular-extensions:end -->

<!-- Source: contributions/what-is-civicontribute.md -->
