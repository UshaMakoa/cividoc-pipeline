---
title: Plan for CiviCRM adoption
category: how-to
topic: installation
subtopic: organizational-needs-and-internal-support
component: CiviCRM
audiences:
- technical
- administrator
- operations-user
- communications-manager
level: basic
journey_stage: plan-and-configure
summary: Identify your organization's CRM needs, build internal support, and prepare a recommendation.
extensions: []
related: []
review_priority: medium
review_notes:
- The data vulnerability example says 'we challenges ensuring data is secure'; the intended wording is unclear, so it has
  been left unchanged.
- The sample data inventory contains filenames and dates from 2005–2010; confirm whether the examples remain useful.
guide: installation
source_repository: https://lab.civicrm.org/documentation/docs/installation.git
source_path: planning/index.md
destination_path: installation/planning/index.md
legacy_urls:
- https://docs.civicrm.org/installation/en/latest/planning/
civicrm_version:
- latest
source_commit: 5a8b870477f63bea90551acb2f7516df67784b19
last_modified: '2026-08-20'
---

# Plan for CiviCRM adoption

This page covers basic strategies for identifying your organizational needs and considering how CiviCRM could meet them. It does not go into detail about CiviCRM functionality or how CiviCRM stores data; you will find that in other chapters. First, take a step back and think about your organisation.

Building internal support for a new Constituent Relationship Management (CRM) solution is a complex task, but it can yield great rewards if done right.

Some organizations appoint an internal team to do this work, while others rely on outside consultants. The following recommendations can help you evaluate your organization’s needs and build internal support.

## Goal

Start by articulating the goal of adopting a CRM. For example:

> Investing in our organization’s database of 12,000 constituents will allow our team to better focus on raising funds and awareness to fulfill our mission now and in the future.

## Evaluation

Evaluate your organization's specific CRM needs by interviewing key stakeholders. This might include development, communications, marketing, events and programs staff, as well as board members.

**Identify the constituents** stakeholders interact with routinely, and ask them to articulate key challenges in managing constituent information: collecting, updating, sharing and using contact information.

**Identify specific inefficiencies** that a comprehensive CRM solution could address.

**Enumerate the resulting lost productivity.** For example:

* **Incoherent view of our constituents:** *We are unable to see a holistic record of our constituents eg: who is a donor, volunteer and e-newsletter subscriber.*
* **Inability to include all prospective donors in all outreach efforts:** *With fractured constituent lists we are unable to include all constituents in our efforts to raise funds, awareness and promote events.*
* **Inefficient use of staff:** *Staff time is not used well when re-keying information originally received digitally, importing, exporting and de-duping records.*
* **Lack of communication:** *We struggle to communicate consistently across departments about their various interactions with the same constituent.*
* **Data vulnerability:** *When contact data is distributed across systems, it is a challenge to reliably protect our complete dataset against loss and we challenges ensuring data is secure when held in multiple systems.*

**Lastly, inventory current data sources** that could be consolidated and shared across departments. For example:

| Owner  | Department | Count  | Constituents              | Description / filename  |
|--------|------------|--------|---------------------------|------------------------ |
| Kris   | Comms      | 245    | short-lead media contacts | comms campaigns / comms2010.doc |
| Katie  | Dev        | 79,000 | donors                    | donors active since 2005 / donors2005-2010.xls |
| Martha | Marketing  | 233    | corporate partners        | active partners / (Outlook) |
| Dan    | Marketing  | 134    | grassroots partners       | all grassroots partners / grasspartners05-10 (Google docs) |
| Carole | Volunteers | 3450   | volunteers                | all MLK day volunteers, skills / mlk_volunteers_10.xls |

This initial inventory will help you identify common sources. When consolidating or migrating data, also plan to discover other existing sources in your organization along the way.

## Benefits

Enumerate the specific benefits of investing in a holistic CRM solution. For example:

* **Accessible to the entire staff** from inside and outside the office (with granular permissions from entry level to super-users).
* **Holistic record for each constituent** showing all their contact information and interactions with our organization.
* **Dynamic creation of constituent groups** allowing us to create groups of constituents based on criteria such as ‘all donors of over $100 in Massachusetts’ or ‘all donors whose gifts have amounted to major gifts this year’.
* **Dynamic creation of top donor and other reports**
* **Constituents' self-service creation and management** of their contact/contribution/subscription/activity records.

## Recommendations

When recommending your CRM solution, enumerate and compare its features and costs with other market solutions. Share case studies of other organizations that use the recommended solution.

**Implementation costs:** Include a budget for implementation that contemplates:

* discovery and project management
* data clean up, consolidation and migration
* system configuration
* post implementation training and documentation

**Maintenance costs:** Include a budget for ongoing maintenance that contemplates:

* pro-active server maintenance
* incremental data backups
* operating system and software upgrades
* ongoing training

<!-- Source: planning/index.md -->
