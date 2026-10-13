---
title: Explore CiviCRM before installing
category: explanation
topic: installation
subtopic: evaluation-options
component: CiviCRM
audiences:
- technical
- administrator
level: basic
journey_stage: plan-and-configure
summary: Compare public demo sites, a local test installation, CiviCRM Spark, and supplier guidance as ways to explore CiviCRM.
extensions: []
related: []
review_priority: low
review_notes:
- The page says the demo sites run the latest master of CiviCRM, but the note says this is true only for the most part.
- The list of supported CMSs includes Drupal 7; verify whether that claim remains current.
guide: installation
source_repository: https://lab.civicrm.org/documentation/docs/installation.git
source_path: planning/demo.md
destination_path: installation/planning/demo.md
legacy_urls:
- https://docs.civicrm.org/installation/en/latest/planning/demo/
civicrm_version:
- latest
source_commit: 5a8b870477f63bea90551acb2f7516df67784b19
last_modified: '2026-08-20'
---

# Explore CiviCRM before installing

## Demonstration sites

CiviCRM hosts several demo sites—at least one for each of the supported **Content Management Systems** (CMS): Backdrop, Drupal 7, Joomla, and WordPress. The demo sites present a working copy of the latest master of CiviCRM with sample data.

You can use them to explore CiviCRM, but they are publicly viewable, so do not enter personal data.

!!! note
    These sites run on `master` for the most part (some CMSs are harder to automate!). The code is bleeding edge, and the "official" demo sites are intended for issue reproduction and testing. Although they demonstrate CiviCRM functionality, that is not their primary purpose: consider them **sandboxes** rather than demos.

A list of available demos is at [https://civicrm.org/demo](https://civicrm.org/demo).

Other users may change these public sites, so you may find unexpected configurations, missing functionality, or different languages. You cannot send emails from the demo sites, set permissions for Drupal users, or fully explore online payment options.

If you have trouble using a demo site, contact the CiviCRM [Core Team](https://civicrm.org/teams/core-team). For a more controlled environment, consider your own test site.

## A local test installation

You can download and set up CiviCRM on your local computer rather than on a server on the Internet. You will still access it through a browser, but it will be visible only on your computer.

A test installation lets you configure CiviCRM and experiment with your data. This option works if you are familiar with configuring a webhosting environment, but it requires some technical knowledge.

## CiviCRM Spark

If you are not comfortable setting up a webhosting environment, you can sign up for [CiviCRM Spark](https://civicrm.org/spark). This hosted CiviCRM platform is provided by CiviCRM LLC and helps sustain CiviCRM development.

## Contact a supplier

If you would prefer guidance at this early stage, consider contacting a CiviCRM provider who can advise you on how to achieve what you need. The CiviCRM website has a [find an expert](https://civicrm.org/partners-contributors) feature to help you find people to work with.

<!-- Source: planning/demo.md -->
