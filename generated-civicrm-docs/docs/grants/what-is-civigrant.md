---
title: What is CiviGrant?
category: explanation
topic: grants
subtopic: civigrant-overview
component: CiviGrant
audiences:
- operations-user
- administrator
level: basic
journey_stage: overview
summary: Learn what CiviGrant tracks and how an organisation might use it to manage a grant programme.
extensions:
- CiviGrant
related: []
review_priority: medium
review_notes:
- The statement about CiviGrant shipping as an extension is tied to CiviCRM version 5.46 and may need review.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: grants/what-is-civigrant.md
destination_path: grants/what-is-civigrant.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/grants/what-is-civigrant/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# What is CiviGrant?

CiviGrant is designed for organisations that distribute funds to others, such as foundations and grant givers. As of CiviCRM version 5.46, CiviGrant ships as an extension which can be enabled from the extensions screen.

CiviContribute tracks money going *into* your organisation; CiviGrant tracks money going *out of* your organisation. CiviGrant provides a data structure and workflows for the grant application process, including managing the amount applied for, the amount received and any reports necessary for the process.

If your grant application process has multiple pathways, you may wish to use CiviGrant in conjunction with CiviCase.

## Scenario: Wookie Hole

Wookie Hole Community Action is a small umbrella organisation that distributes funds to support the annual Wookie Hole Community Festival, held each year in Wookie Hole Cave.

Each year, it makes a £40,000 grant pool available to local organisations participating in the festival. The pool comes from local businesses and other grant giving organisations. Each applicant completes an eligibility questionnaire, which is entered into the applicant's contact record, and an application detailing how they will spend the money, which is attached to the grant. Staff also fill in certain fields for each grant and attach a read-only PDF copy of the original application form for future reference.

Ineligible applications are rejected. Eligible applications are scored according to pre-defined criteria. The grant committee members then look at the total amount applied for by all applicants. If it exceeds £40,000, they review all eligible projects again to decide which ones to fund fully or partially. CiviGrant has fields they can use to store and search on this information.

Once the funds have been granted, Wookie Hole Community Action uses CiviGrant with CiviMail to solicit feedback and reports from funded organisations. When feedback arrives, they mark the grant as "feedback received". Getting feedback often takes multiple emails. To send them, they use an email template and search for contacts who have successfully received a grant but have not yet sent feedback.

Finally, once all reports are in, a staff member compiles a report and thank-you and emails them to all organisations that gave funds toward the festival. The report details how their funds benefited the local community. Wookie Hole Community Action also prints a certificate for each local business and funder directly from CiviCRM, which they can display on their premises.

<!-- cividoc:popular-extensions:start -->
## Popular extensions

These are widely used extensions in the relevant category of the official CiviCRM Extensions Directory. Usage is a popularity signal, not a compatibility or suitability guarantee.

- [Grant Application Pages](https://civicrm.org/extensions/grant-application-pages) — reported usage: 62
- [CiviGantt](https://civicrm.org/extensions/civigantt) — reported usage: 7
- [Batch Update of Grants via Profile](https://civicrm.org/extensions/batch-update-grants-profile) — reported usage: 6
- [Grant Prefill](https://civicrm.org/extensions/grant-prefill) — reported usage: 2
- [Print Grant PDFs](https://civicrm.org/extensions/print-grant-pdfs) — reported usage: 2

[All extensions for this component](https://civicrm.org/extensions?category=101)

Check development status, current CiviCRM compatibility, CMS requirements, and release notes before installation.

Usage snapshot reviewed: 2026-10-13.
<!-- cividoc:popular-extensions:end -->

<!-- Source: grants/what-is-civigrant.md -->
