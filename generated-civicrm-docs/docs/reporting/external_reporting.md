---
title: External reporting
category: explanation
topic: reporting
subtopic: reporting-outside-civicrm
component: CiviCRM reporting
audiences:
- operations-user
- administrator
level: basic
journey_stage: overview
summary: Understand when reporting outside CiviCRM may be useful and how external tools can access CiviCRM data.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: reporting/external_reporting.md
destination_path: reporting/external_reporting.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/reporting/external_reporting/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# External reporting

Reporting within CiviCRM generally assumes that:

- You want to report directly on your "production" CiviCRM database with real-time data.
- You only want to report on data in CiviCRM, rather than data from other applications or combined data from many applications.

You can also create reports, dashboards, or data transformations outside CiviCRM using tools such as Metabase, Tableau, Power BI, RapidMiner, and Pentaho. These tools can access the CiviCRM database through a direct link to the MySQL or Maria database, or potentially through the CiviCRM API.

How to use these tools is outside the scope of this document. If your organization does not have the necessary skills, contact your CiviCRM experts or whoever supports you with CiviCRM or reporting.

<!-- Source: reporting/external_reporting.md -->
