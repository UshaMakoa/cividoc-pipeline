---
title: What is CiviMail?
category: explanation
topic: mailings
subtopic: civimail-overview
component: CiviMail
audiences:
- communications-manager
- administrator
- operations-user
level: basic
journey_stage: overview
summary: Learn what CiviMail does and how organisations use it for mass email campaigns.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: email/what-is-civimail.md
destination_path: email/what-is-civimail.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/email/what-is-civimail/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# What is CiviMail?

CiviMail handles mass email campaigns. It can reliably deliver a high volume of email and provide detailed reports on the results and effectiveness of those emails. It can complement other CiviCRM components: for example, you can email non-members to encourage them to become members, or people who have not yet registered for an event.

CiviMail, like all of CiviCRM's mail features, interacts with your mail server. Configuring the mail server and properly setting up CiviMail are system administrator tasks, and you may require professional assistance. You also need to check that your web hosting provider meets the configuration requirements and find out whether they limit how many emails you can send per day.

A misconfigured mail server is a liability. If you do not know what you are doing, you could end up on a spam black list, which is much harder to get off than to get on. For more information about configuring your mail server, see the *Email system configuration* chapter in the *Initial set up* section.

## Scenario: managing email lists

St Ethelburga's Centre for Peace and Reconciliation uses CiviEvent to run a yearly event programme on different themes. They have set up a mailing list page where people can sign up to hear about events that interest them. They use CiviMail to email people based on those interests. When someone unsubscribes from an event theme mailing list, CiviCRM keeps a record of it.

St Ethelburga's also automatically subscribes anyone who has attended an event on a specific theme to receive emails about that theme. CiviCRM remembers who has unsubscribed from a thematic event mailing list and does not re-subscribe them.

From time to time, St. Ethelburga's sends other emails to a mailing list that includes nearly all contacts in their database. These contain personal messages from the centre director highlighting particular issues. To test which message formats are more effective, they often send two similar versions of an email to different groups. They send the first version to half the contacts in a particular group, then send the second version while excluding contacts who received the first.

## Scenario: mobilising with email

The Townsville Organisation For Tenants (TOFT) held a survey and petition to gather data and support for the campaign Demand Affordable Public Housing. Volunteers conducted the survey by visiting selected constituents in their homes. The petition was widely promoted to the public, who could sign it and answer questions online.

Early in the campaign, the TOFT volunteer coordinator searched for contacts in the group Volunteers and used the Send Email action to ask for help with the survey. A small group of those who said they were available were trained to conduct home visits and record survey responses.

After the online petition was created using tools in CiviCampaign, the TOFT communications officer created an email with text, images and links to promote the campaign and encourage people to complete the petition online. They sent it to the entire database using CiviMail and included a forwarding link so recipients could distribute the email through their own networks.

CiviMail enabled TOFT to track responses to the mass email. Reports showed that 89% of recipients clicked through to sign the petition, and 75% forwarded the email to others. TOFT compared this data with previous offline petition and survey efforts to demonstrate the campaign's increased reach through using CiviCRM.

<!-- cividoc:popular-extensions:start -->
## Popular extensions

These are widely used extensions in the relevant category of the official CiviCRM Extensions Directory. Usage is a popularity signal, not a compatibility or suitability guarantee.

- [Mosaico CiviCRM Integration](https://civicrm.org/extensions/email-template-builder) — reported usage: 4,729
- [E-mail API](https://civicrm.org/extensions/e-mail-api) — reported usage: 3,072
- [Fuzion Tokens](https://civicrm.org/extensions/fuzion-tokens) — reported usage: 1,489
- [PDF Creation API](https://civicrm.org/extensions/pdf-creation-api) — reported usage: 438
- [Mosaico Tweaks](https://civicrm.org/extensions/mosaico-tweaks) — reported usage: 253

[All extensions for this component](https://civicrm.org/extensions?category=95)

Check development status, current CiviCRM compatibility, CMS requirements, and release notes before installation.

Usage snapshot reviewed: 2026-10-13.
<!-- cividoc:popular-extensions:end -->

<!-- Source: email/what-is-civimail.md -->
