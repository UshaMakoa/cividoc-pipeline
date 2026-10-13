---
title: Repeating events
category: how-to
topic: events
subtopic: configure-repeating-events
component: Events
audiences:
- event-manager
- operations-user
- administrator
level: basic
journey_stage: plan-and-configure
summary: Set an Event to repeat at specified intervals and exclude dates from the repetition.
extensions: []
related: []
review_priority: low
review_notes:
- The source does not explain the distinction between Event end date and occurrence end date.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: events/repeating-events.md
destination_path: events/repeating-events.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/events/repeating-events/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Repeating events

You can set an Event to repeat on a certain day and time with a specific end date, and include dates to exclude from the repetition.

## Set up a repeating event

1. Go to **Manage Events**. Under **Configure**, select **Repeat** from the dropdown.

    ![Manage events screen with two events, and the expanded context menu: info and settings, location, fees... and repeat.](../img/repeating_events.png)

2. On the **Repeat Event Screen**, specify the Repeating intervals (in hours, days, weeks, months, or years), Event end date, and occurrence end date. It is also recommended that you specify the Repetition Start Date and Excluded Dates.

    ![screenshot](../img/repeating_event_page.png)

    !!! note
        If you would like your Scheduled Reminders to repeat, make sure you have setup Scheduled Reminders on the Event that you are repeating. You can edit this later. It is also recommended that you do not setup your reminders to repeat on specific days, but rather have them sent two weeks or a few days before the Event.

3. Once you have filled out all the appropriate fields, click **Save**. A popup window will prompt you to Continue with your selection.

![&quot;Repeat&quot; tab of an event. The event is set to end after 7 occurences. The section &quot;Connected Repeated Events&quot; lists the 7 occurences with their respective event id, start date, end date...](../img/repeated_event.png)

<!-- Source: events/repeating-events.md -->
