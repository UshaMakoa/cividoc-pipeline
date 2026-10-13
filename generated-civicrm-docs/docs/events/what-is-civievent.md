---
title: What is CiviEvent?
category: explanation
topic: events
subtopic: civievent-overview
component: CiviEvent
audiences:
- event-manager
- operations-user
- administrator
- fundraising-manager
level: basic
journey_stage: overview
summary: Learn what CiviEvent does and how events, participants, roles, and statuses fit together.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: events/what-is-civievent.md
destination_path: events/what-is-civievent.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/events/what-is-civievent/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# What is CiviEvent?

CiviEvent provides tools for running events and reducing the administration involved. It supports both simple and complicated registration processes. Key features include:

- Self-registration for participants, including online credit card payments
- Tracking sign-ups, cancellations, and attendance
- Promoting events on your website
- Streamlining set-up for similar, recurring events with event templates and event copy functionality
- Checking in participants on-site from any computer with an internet connection

## Scenario: Youth leadership workshop

Arts in Action, a community arts group, conducts leadership workshops for people under age 25 throughout the year. The group wants to attract new youth to its workshops and enlist past attendees to volunteer and teach. It invites youth from local schools and theater groups. Youth speakers, volunteers, and other speakers also take part in the training workshops.

Arts in Action communications staff use CiviEvent to manage each workshop from planning through evaluation. A staff member creates an event page with an online registration form. Because the workshops are regular events, a staff member has already created an event template that fills in much of the information needed during event set-up.

Registration has a flat fee, with additional fees for optional workshops. Attendees can select what they are registering for and pay online. The form also gathers participants' food and lodging preferences using a CiviCRM feature called a profile.

Staff draw a targeted list of youth and groups from existing contacts and send personalised invitations using CiviMail. The invitations also use a template, so information can be reused for future events. Each invitation links directly to the event page, allowing participants to reach online registration with a single click. Staff also announce the event on the Arts in Action website and enable the "Tell-a-friend" function so people can share it through their networks.

A designated staff person manages self-registration. They periodically check that payments are being made, manage the wait list when sign-ups exceed the maximum number of participants, and answer questions.

On the day of the event, organisers check in attendees on-site to track attendance and no-shows in real time. They can also ask participants with outstanding fees to pay. The database is updated immediately, freeing up spaces for those on the wait list and recording payments.

After each workshop, staff evaluate the event and use CiviEvent to generate reports, such as the number of attendees, total event fees paid, and total amount still due. They can update and save the event and mail templates for the next event.

## Some key concepts

These concepts provide context for the step-by-step event tasks in the following chapters.

### Events, participants and contacts

CiviCRM lets you create one or more **events** in which your **contacts** can participate. When a contact participates in an event, they are called a **participant**.

### Event types

CiviCRM lets you define Event Types, such as Conferences, Meetings and Fundraisers, according to your organization's needs.

Event Types are useful when different types of events have different requirements. For example, you can create custom fields to store and display additional data about an event based on its Event Type. See [*Custom data on events*](https://docs.civicrm.org/user/en/latest/events/custom-data-for-events/) for more information.

You can also use Event Types to categorise and segment events and attendees. For example, you could find all contacts who attended one of your Workshops or Fundraising events.

### Participant default roles

Every contact who participates in an event is assigned a Participant Default Role. Attendee is a common role; others include Volunteer, Host and Speaker. Participant roles are fully customisable to match the events your organization conducts.

Roles let you segment participants by their involvement. For example, you could email Volunteers only or generate a list of past table captains for fundraisers. You can also create custom fields that apply only to specific roles, such as fields for collecting availability from Volunteers only.

### Participant statuses

Participant statuses, such as Registered, No-show, Attended and Cancelled, track a contact's stage in their 'event journey'. Statuses are fully customisable to match the way your organization handles event registration.

You can use statuses to segment participants by their behaviour with respect to an event—for example, to generate sign-in sheets, track how many people are likely to attend, or tailor emails to registrants.

## Other parts of CiviCRM that work with CiviEvent

CiviEvent works with other parts of CiviCRM. You can use CiviMail to promote an event to a targeted list and email participants before and after the event. For more information, see the *Email* section, particularly [Set-up](../email/set-up.md) and [Scheduled Reminders](../email/scheduled-reminders.md).

CiviEvent works with CiviContribute to accept event payments online. To do this, you must enable CiviContribute and set up a payment processor. See the [*Contributions*](https://docs.civicrm.org/user/en/latest/contributions/what-is-civicontribute/) section for more information.

<!-- cividoc:popular-extensions:start -->
## Popular extensions

These are widely used extensions in the relevant category of the official CiviCRM Extensions Directory. Usage is a popularity signal, not a compatibility or suitability guarantee.

- [CiviDiscount](https://civicrm.org/extensions/cividiscount) — reported usage: 1,834
- [no overwrite](https://civicrm.org/extensions/no-overwrite) — reported usage: 918
- [Summary Fields](https://civicrm.org/extensions/summary-fields) — reported usage: 663
- [Line Item Editor](https://civicrm.org/extensions/line-item-editor) — reported usage: 565
- [CiviMobileAPI](https://civicrm.org/extensions/civimobileapi) — reported usage: 406

[All extensions for this component](https://civicrm.org/extensions?category=98)

Check development status, current CiviCRM compatibility, CMS requirements, and release notes before installation.

Usage snapshot reviewed: 2026-10-13.
<!-- cividoc:popular-extensions:end -->

<!-- Source: events/what-is-civievent.md -->
