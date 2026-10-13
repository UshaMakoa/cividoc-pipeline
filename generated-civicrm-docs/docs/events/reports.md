---
title: Reports
category: reference
topic: events
subtopic: event-and-participant-analysis
component: CiviEvent
audiences:
- event-manager
- operations-user
- administrator
level: basic
journey_stage: reports-and-review
summary: Compare ways to analyse event and participant data, and learn how to display an event report on the home dashboard.
extensions: []
related: []
review_priority: medium
review_notes:
- The Attendee List instructions contain the unclear phrase "and tone, two or three at the right of the list"; it has been
  left unchanged.
- The dashboard instructions refer to a "following chapter Reports and Analysis" without a link or a clear location.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: events/reports.md
destination_path: events/reports.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/events/reports/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Reports

There are several ways to report on and analyse events and participants.

The **event dashboard** gives a quick overview of upcoming events. For each event, it shows the number of registrations and their statuses: how many are registered, how many are counted, and how many are pending for different reasons. The dashboard is limited to 12 events scheduled to start at a date closest to today. This is most likely not to be sufficient to organizations with many scheduled events.

CiviCRM's search features and CiviReport provide more detailed and customised analysis. If you are interested in the financial aspects of events, you may also find the *Reports and analysis* chapter in *Contributions* useful.

## Searching based on participant data

CiviCRM distinguishes between contacts and event participants. Sometimes an event-related question is best answered in terms of contacts—for example, which contacts came to events in 2011. At other times, participants are more useful—for example, how many training sessions did we deliver as part of our sexual health education programme this year. Consider this distinction when searching for event attendees.

**Find participants** searches based on participant data and returns participant data. **Advanced search** searches based on most participant information, can combine it with other contact information, and returns contacts. You can also choose **Participant** from the **Display Results As** column to show participants rather than contacts.

These searches give you simple totals. You can also export the results as CSV for further analysis in spreadsheet software.

## Event and participant reports

Reports can do things that searches cannot. For instance, a search cannot aggregate data from multiple events at once or limit the date of registration very flexibly. Repeating the same searches can also be time consuming. Searches can be set as Smart Groups, but this leads to a proliferation of groups.

You can instead set up reports for an event or a collection of events. Reports can be automatically assigned to a designated submenu (e.g. under **Events > Reports**) or made available as dashlets for the main dashboard, as described below.

Out of the box, CiviCRM comes with four reports designed to help you analyse events:

- **Event Participants List** displays participant and individual data, as well as all custom data. All of these can also be used as filters.
- **Attendee List** provides a list of event attendees and can be filtered to show just one event. You add one blank column on the left of the list and tone, two or three at the right of the list and so create an event sign up sheet.
- **Event Income Detail** and **Event Income Summary** work together to show details of revenue from events. The summary can show total income for a series of events, such as all of your conferences in 2011. Clicking on one of those events gives you more detail about its income breakdown per role and per status. It can also be displayed in graphical form as Pie Chart or Bar Chart.

### Create an event report from a template

See [Reporting Set-up](../reporting/set-up.md) for details.

## More analysis

If you can't do what you want with a built in report or search, consider commissioning a new report or custom search. Read the *CiviReport* section for more information.

## Displaying an event report on CiviCRM's home dashboard

If you haven't already created any Event Reports, see the following chapter Reports and Analysis for instructions on how to create reports. Then make the report available for the dashboard:

1. From the navigation menu, click **Reports** and select the report you wish to display.
2. In the Report Settings area, check the **Available for Dashboard?** box.
3. Click **Update Report**.

Once the report is available for the dashboard:

1. Navigate to **Home** to view the dashboard.
2. Click **Configure Your Dashboard**.
3. Drag the desired report from the Available Dashlets area into either the Left Column or Right Column of the dashboard area, and click **Done**.
4. You should now see your report on your home dashboard. To view the latest updated information for your report and any other items you've included on your dashboard, click **Refresh Dashboard Data**.

<!-- Source: events/reports.md -->
