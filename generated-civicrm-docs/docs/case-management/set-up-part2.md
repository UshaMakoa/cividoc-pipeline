---
title: Custom fields for cases and activities
category: how-to
topic: activities
subtopic: custom-fields
component: CiviCase
audiences:
- operations-user
level: intermediate
journey_stage: plan-and-configure
summary: Create custom field sets for case types or activity types and choose where structured data belongs.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: case-management/set-up-part2.md
destination_path: case-management/set-up-part2.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/case-management/set-up-part2/
civicrm_version:
- latest
last_modified: '2026-10-06'
---

# Custom fields for cases and activities

You may want to collect structured data in a case. Custom fields can be connected to a specific activity type or to the case type. For example, an Employment Counselling case might include a Skills Assessment activity in which an employment counsellor records client job skills, perhaps using a set of checkboxes. Alternatively, a generalized application case might need a custom field indicating the type of application being tracked.

Custom fields attached to a case are visible inside the case management screen. Fields attached to an activity are visible only when the user views details of that activity.

If you are transitioning from a paper-based system, refer to existing forms to determine which information is relevant to include. Please review the section on configuring custom data fields prior to beginning these steps.

1. Go to **Administer > Customize Data and Screens > Custom Fields**.
2. Click **Add a Set of Custom Fields**.
3. Under **Used For**, select **Activities** or **Cases**.
4. Select one or more specific activity type(s) or case type(s) for which this set of fields will be used.
5. Enter any help information you want displayed to your users.
6. Click **Save**.
7. Enter one or more custom fields for this set.
8. Repeat these steps for each activity type or case type that requires custom data.

If you need many fields for one activity type, consider dividing them into logically related sets that make sense to users and avoid an endless tunnel of fields.

<!-- Source: case-management/set-up-part2.md -->
