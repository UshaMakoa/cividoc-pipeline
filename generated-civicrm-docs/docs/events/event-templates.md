---
title: Event templates
category: how-to
topic: events
subtopic: create-and-use
component: Events
audiences:
- event-manager
- operations-user
- administrator
level: basic
journey_stage: plan-and-configure
summary: Create an event template and use it to pre-fill the configuration of a new event.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: events/event-templates.md
destination_path: events/event-templates.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/events/event-templates/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Event templates

If you need to set up a number of events with similar configurations, you can streamline the process using event templates. Creating a template is similar to creating an event, with two differences:

- Assign a descriptive template title that identifies the type of event it is used for, such as Monthly community meetup with online registration.
- The template form has no starting or ending dates. Those dates are specific to an actual event instance.

## Create an event template

1. Navigate to **Events &gt; Event Templates** and click **Add Event Template**.
2. Enter a template title and event type.
3. Select a campaign if all events created from the template should be associated with a Campaign.
4. Continue the normal event set-up process, using settings that will be constant across events created from the template. Common characteristics might include location, event fees, online registration settings, and tell-a-friend settings.

![screenshot](../img/event_template_setup.png)

## Use an event template

When you start to create a new event, select the template. The new event will be pre-filled with the saved configuration properties.

![On the new event form, the first listbox is "From template".](../img/event_template_new.png)

<!-- Source: events/event-templates.md -->
