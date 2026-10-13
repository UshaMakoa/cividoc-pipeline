---
title: Soft credits
category: explanation
topic: contributions
subtopic: attribution-and-honorees
component: CiviCRM contributions
audiences:
- fundraising-manager
- operations-user
- administrator
level: basic
journey_stage: overview
summary: Understand how soft credits attribute contributions to people other than the donor.
extensions: []
related:
- personal-campaign-pages.md
review_priority: low
review_notes:
- The contribution detail report passage does not identify which optional columns should be checked or where to select them.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: contributions/soft-credits.md
destination_path: contributions/soft-credits.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/contributions/soft-credits/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Soft credits

Soft credits help your organisation understand the sources of its contributions. They let you assign credit for a donation to one or more people who are not the donor.

## Soft credit types

CiviCRM's soft crediting allows users to assign Soft Credit Types to contributions. Assigning an appropriate reserved or custom Soft Credit Type enables administrators to properly attribute contributions received through one or more charitable contribution types (such as Donor Advised Funds, Scholarships, Family Bequests, etc) whether solicited (P2P) or not.

CiviCRM uses the following reserved Soft Credit Types:

- In Honor of
- In Memory of
- Solicited
- Personal Campaign Page
- Gift

For example, if an active member of your organisation encourages 10 other people to contribute, soft credits let you credit that member and each actual donor without counting a contribution twice. You can also credit parts of a donation to multiple people.

In the screenshot below, Magan Cooper's contribution of $1,500.00 is credited to three different people.

![A contribution of $1,500 with three soft contributions of $500.](../img/soft-credit-donation-1.png)

Soft Credit Types can also attribute contributions in more complicated situations. For example, Joe is an active member of a community foundation that regularly contributes to your organisation. Joe solicits a contribution from Jane on behalf of the foundation, and your organisation receives a check from the foundation. The contribution can be attributed without duplicating it:

- The community foundation is the donor.
- Joe would receive the solicited Soft Credit.
- Jane would receive the donor advised Soft Credit.

This scenario is illustrated below.

![A contribution with a soft contribution from Joe, and one from Jane.](../img/soft-credit-donation-2.png)

As well as recording Soft Credits, we can also report on them. The contribution detail report has optional columns which show Soft Credit details. When checked, these will show four extra columns in CiviReport, which can be used to view soft credit information.

![Screenshot of the report.](../img/z_sprint14_contributions_soft_credit.png)

## Honoree information and profiles

When creating a contribution page, you can allow end users to make a contribution on behalf of an Honoree. To do so, select the **Honoree Section Enabled** checkbox. This reveals additional fields for specifying the Honor Types and Profile to include in the section.

![The form in CiviCRM.](../img/z-sprint14_honoree_section.png)

Once configured, end users can enter Honoree info for online contributions. CiviCRM checks whether the Honoree already exists using your site's default duplicate checking rules. If no duplicate is found, it creates a new contact record. A soft credit is added to the Honoree's contact record.

![The form as the user will see it on the website.](../img/soft-credit-honoree-info.png)

## Soft credits and personal campaign pages

Soft credits are closely related to [Personal Campaign Page](personal-campaign-pages.md). When someone donates by a Personal Campaign Page, their donation is soft credited to the owner of the Personal Campaign Page.

<!-- Source: contributions/soft-credits.md -->
