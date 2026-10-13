---
title: What is CiviMember
category: explanation
topic: memberships
subtopic: overview
component: CiviMember
audiences:
- membership-manager
- operations-user
- fundraising-manager
level: basic
journey_stage: overview
summary: Understand what CiviMember supports and how an organisation can use it to manage memberships.
extensions: []
related: []
review_priority: low
review_notes:
- The final scenario paragraph has an unclosed parenthesis in its explanation of improved retention; the passage is left unchanged.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: membership/what-is-civimember.md
destination_path: membership/what-is-civimember.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/membership/what-is-civimember/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# What is CiviMember

CiviMember is the CiviCRM component that supports and automates membership management. It allows you to:

- Define membership types and pricing schemes that meet your needs.
- Create self-service options for online membership sign-up and renewal, utilising CiviContribute.
- Manage memberships manually through the administrative interface.
- Create and schedule automated messages to welcome new members, remind them about upcoming renewal, and more.
- Track and report on contacts through the membership cycle.
- Grant additional website privileges for members.

The chapters in this section cover how to use CiviMember. If you are new to it, review the entire section while considering your organisation's membership scheme and how best to model it within CiviCRM. CiviMember can be configured to meet most requirements.

Adopting CiviCRM will normally require some changes in working practices. As you develop your plans, work closely with the people in your organisation who will manage memberships day to day.

Memberships can last from a day to a lifetime. They can be free or paid, with simple or complex pricing structures. They can be set up to auto-renew where a compatible payment processor is enabled.

A contact's memberships are visible on the contact's summary screen and on the membership dashboard. You can find them through the Membership Search or Advanced Search. CiviMember also provides four membership reports, each of which can be customised to better meet your needs.

Conceptually, members are contacts in your CiviCRM database with one or more memberships. A contact may be an individual, a household, an organisation, or another contact sub-type; the membership is always applied to a contact.

## Scenario: Driving membership forward

The Atlantic Region Public Transit Association (ARPTA) has four membership categories:

- **Regular Members:** Public transit systems. This category has three tiered levels based on the size of the system. Membership is organization-based, and all employees of the member organization receive access to member benefits, such as discounted rates at Association events.
- **Affiliate Members:** Businesses providing goods and services to the transit industry. Fees are the same for all Affiliate Members. Membership is organization-based, and up to 10 employees of the member organization receive access to member benefits, such as discounted rates at Association events.
- **Associate Members:** Students, government representatives, public interest groups, research institutions, and other interested parties. Fees are the same for all Associate Members. Membership is individual-based.
- **Honorary Members:** Retired transit system executives and others who have made a notable contribution to the industry and Association. Membership is individual-based and free for life.

When ARPTA's membership administrator, Sue, initially configured CiviMember, she created a separate membership type for each of the four categories. CiviMember managed this easily. At first, ARPTA continued to process renewals and new sign-ups manually while the system bedded in.

Last year, ARPTA's board agreed that they needed to increase membership income by improving recruitment and renewal rates. They also wanted to keep tight control of the time spent on membership administration and, if possible, reduce it.

To help achieve this, ARPTA used CiviContribute and CiviMember to set up online sign-up and renewal pages for Regular and Affiliate Members. They ran targeted recruitment campaigns linking to the sign-up pages so potential members could join online. Existing members were encouraged to renew online by logging in to the member section of the ARPTA website.

These changes streamlined sign-up and eliminated much of the administrative work. They also gave Sue a clear view of new sign-ups, recent renewals, and expired members who needed to be chased. Through CiviContribute, she can produce a monthly spreadsheet of membership fees received for the accounts department to import into its accounting software. With less paperwork, she can engage more with members and take a greater part in the annual conference, which ARPTA manages using CiviEvent.

ARPTA's board were also pleased with the results of the move to online
sign-up and renewal, which, in conjunction with their marketing
campaign, led to a 30% jump in new members over a year. Their analysis
also showed a 40% improvement in membership retention (in part because
Sue was able to devote more time to contacting lapsed and expired
members, and in part because members reported that they found it easy
and convenient to renew online, and were prompted to do so by the
reminder emails that Sue had set up using the Schedule Reminders
feature. Their market research also showed that members appreciated the
fact that they were being contacted more regularly by Sue, and felt more
engaged with ARPTA as a result.

<!-- cividoc:popular-extensions:start -->
## Popular extensions

These are widely used extensions in the relevant category of the official CiviCRM Extensions Directory. Usage is a popularity signal, not a compatibility or suitability guarantee.

- [CiviDiscount](https://civicrm.org/extensions/cividiscount) — reported usage: 1,834
- [Fuzion Tokens](https://civicrm.org/extensions/fuzion-tokens) — reported usage: 1,489
- [Line Item Editor](https://civicrm.org/extensions/line-item-editor) — reported usage: 565
- [Percentage Price Field](https://civicrm.org/extensions/percentage-price-field) — reported usage: 385
- [Membership Extras](https://civicrm.org/extensions/membership-extras) — reported usage: 295

[All extensions for this component](https://civicrm.org/extensions?category=97)

Check development status, current CiviCRM compatibility, CMS requirements, and release notes before installation.

Usage snapshot reviewed: 2026-10-13.
<!-- cividoc:popular-extensions:end -->

<!-- Source: membership/what-is-civimember.md -->
