---
title: Custom data for events
category: explanation
topic: events
subtopic: choosing-records-and-field-availability
component: Events
audiences:
- event-manager
- operations-user
- administrator
level: intermediate
journey_stage: plan-and-configure
summary: Understand where to store custom data for events and participants and which participant field options are available.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: events/custom-data-for-events.md
destination_path: events/custom-data-for-events.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/events/custom-data-for-events/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Custom data for events

You may want to collect extra information about events and their participants as part of the event management process. A general understanding of how custom data works in CiviCRM will help you use this page. The chapter on *Custom fields* in *Organising Your Data* provides that background.

## Choose where to store custom data

The key question is *where* the custom data should go. There are three typical places:

- The participant record
- The contact record
- The event record

Putting data in the wrong place can cause problems later. For example:

- Add dietary preference to the contact's record, since it is unlikely to change between events.
- Add session preference to the participant record, since it is only of interest in the context of the event.

The event record should collect information about the event itself, not its participants.

## Custom data for events

Custom fields can be added to events. For example, an organisation that holds training workshops throughout the year could create a checkbox style field to track six common workshop topics. It could add the list of topic options as custom data for events of the type workshop. The field would then be available when creating an event of type Workshop.

You do not have to select a specific event type. Leaving the dropdown set to Any makes the field available to all events, regardless of type.

## Custom data for participants

There are several options for adding custom data to participants:

- **Participants:** Adds the field to all participant records. Use this for information that applies to all participants.
- **Participants (Event Name):** Works like Participants, but lets you assign a group of custom fields to a specific event. This is useful for complex registration data for one event without cluttering up all events.
- **Participants (Role):** Makes fields available only for particular types of participants. For example, you could collect biographical profile details from speakers and record them with their event registration.

## Add custom data

Adding custom data requires the administrator permission. To add custom data for participants, add new custom fields through **Administer &gt; Customize Data and Screens &gt; Custom Data**. To create custom fields for events, first add the **custom field set** on the appropriate record, and then add the fields themselves.

Alternatively, you can create custom fields on the fly during the event creation process—see the chapter *Creating an event*.

<!-- Source: events/custom-data-for-events.md -->
