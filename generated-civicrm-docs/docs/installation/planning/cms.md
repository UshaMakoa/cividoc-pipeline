---
title: Choosing a CMS for CiviCRM
category: explanation
topic: installation
subtopic: choosing-a-cms
component: CiviCRM CMS integration
audiences:
- technical
- administrator
- membership-manager
- operations-user
level: basic
journey_stage: plan-and-configure
summary: Compare CMS options and consider how your website needs to integrate with CiviCRM.
extensions: []
related: []
review_priority: medium
review_notes:
- Testing and adoption comparisons are dated 2019, and several CMS references are version-specific; review whether these descriptions
  remain current.
guide: installation
source_repository: https://lab.civicrm.org/documentation/docs/installation.git
source_path: planning/cms.md
destination_path: installation/planning/cms.md
legacy_urls:
- https://docs.civicrm.org/installation/en/latest/planning/cms/
civicrm_version:
- latest
source_commit: 5a8b870477f63bea90551acb2f7516df67784b19
last_modified: '2026-08-20'
---

# Choosing a CMS for CiviCRM

CiviCRM works with several popular open source Content Management Systems (CMS), or as a Standalone web application.

In general, you should probably choose a CMS because you already know how to use it or it is already used by your organisation. Each CMS has different advantages and disadvantages, and different people will give you views on which is better. There are also resources that help organizations choose a CMS for their content strategy and website.

Factors other than differences in CiviCRM integration will often determine your choice. Your website may already use a CMS, and reimplementing it in another could involve expense and hassle. Your CMS project may also have other reasons to prefer one option. Even so, your plans for CiviCRM integration may affect—or be crucial to—your decision.

Before starting a project, consider how you plan to use CiviCRM now and in the future:

1. How much information from CiviCRM do we want to display on our website (e.g. A live list of our current members)?
2. What information, collected through our website, do we want to store in CiviCRM (e.g. Family data from a public form with the family relationships automatically added)?

This is known as integration. The type and amount of integration you require may help you determine which CMS is best for you.

## CMS options

**Drupal** is the most flexible and has the best integration with CiviCRM. If you have complex CMS needs or envisage a lot of interaction between users on your website and your CRM, then Drupal might be the CMS for you. The main negative is that this flexibility makes it harder for new site builders to get to grips with.

**Backdrop** is very similar to Drupal 7, with many improvements making it slick and lightweight. It started as a fork (that is, a copy) of Drupal 7, aimed at users for whom Drupal 9 or Drupal 10 was likely to be too complex either to use, or to migrate to from Drupal 7. Drupal 7 modules and themes require modifications to work with Backdrop CMS, though many have already been ported and are actively maintained.

**Joomla** isn't as popular as WordPress, though it is more popular than Drupal. Joomla is easier to learn than Drupal. The amount of integration available is lower than then when using Drupal.

**WordPress** is by a wide margin the most popular of the four options. It is considered to be very easy to build sites using WordPress, especially for people that are not familiar with web technology. A lot of people know WordPress as a blogging platform rather than a CMS, but it is becoming more powerful and flexible with each release. The amount of integration available is lower than when using Drupal.

Differences at a CMS level are mentioned elsewhere through this guide. The following chapters in this section go into more detail about what is offered for each CMS.

## Availability of extensions

There are historical reasons why different CMS options have different levels of integration with CiviCRM. In 2005, CiviCRM launched without its own extension mechanism, but it was possible to write custom integrations in the form of Drupal modules or Joomla plugins, the two CMSes supported at that time. Partly as a result of the ethos of the Drupal community members participating in the CiviCRM ecosystem, a larger variety of Drupal modules to integrate with CiviCRM were created and matured.

Support for running CiviCRM with WordPress was added in 2012, which allowed WordPress plugins to implement custom integrations. 2012 also saw CiviCRM roll out its own native extension system: flexible, cross-CMS support aiming to reduce the development and maintenance effort involved in creating customizations to extend and modify core CiviCRM functionality. In recent years a large number of CiviCRM native extensions have been released, though there continue to be CMS-specific integrations, particularly around permissions and forms. So the reasons for choosing one CMS over another based on the available functionality and integration levels continue to decline.

## Integration features

Broadly there are some differences which arise because of distinctive features/norms in each CMS community, e.g.

* In WordPress, it's pretty common to embed content in your web-pages using short-codes. CiviCRM has several short-codes in WP.
* In Backdrop CMS/Drupal 7/Drupal 9/Drupal 10, it's pretty common to embed content in your web-pages using blocks. CiviCRM has several blocks in Drupal.
* In Backdrop CMS/Drupal 7/Drupal 9/Drupal 10, CiviCRM makes use of the CMS's "roles" and "permissions" using the CMS's interfaces and approaches, and there are modules to synchronize CiviCRM groups and membership types to them.
* In Joomla/WordPress, "roles" and "permissions" can also be managed using the CMS's interfaces and approaches, and there are plugins to synchronize groups and membership types to them.

## Installation process

The installers are a bit different - web-based installation is easier in Joomla, but it's more flexible in Drupal or WordPress. Command line based installation is easier in Drupal or WordPress.

## Testing

The core system is the same across all CMS options, but occasionally there are bugs in the CMS integration code. For historical reasons, the most robust automated testing is performed on Drupal7 though as of 2019 there are very active WordPress manual testers and a growing numbers of WordPress tests are being added.

The size of the install base shown [on the CiviCRM Stats site](https://stats.civicrm.org/?tab=sites) also affects how well reported issues are and how quickly fixes are tested and merged. While trends are subject to change, as of 2019, Joomla shows the least growth and WordPress the most.

Therefore it may take a bit longer to identify/resolve bugs in the BackDrop, Drupal, Joomla and WordPress integrations but automated testing on these platforms is being continually improved.

## Users and contacts

* Anonymous site visitors and those with a website login are website **Users**
* Individuals and organisations with a CiviCRM record are **Contacts**

<!-- Source: planning/cms.md -->
