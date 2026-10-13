---
title: Import requirements for activities, contributions, memberships, participants and tags
category: reference
topic: activities
subtopic: other-record-types
component: CiviCRM imports
audiences:
- operations-user
- event-manager
- fundraising-manager
- membership-manager
level: intermediate
journey_stage: reference-and-troubleshooting
summary: Find the CSV fields and import options described for activities, contributions, memberships, participants and tags.
extensions:
- Civi-Import
- API csv Import GUI
related:
- ../contributions/importing.md
- ../membership/manual-entry-of-memberships.md#importing-memberships
- https://civicrm.org/extensions/api-csv-import-gui
review_priority: medium
review_notes:
- The contribution instructions depend on a “recent version” of CiviCRM without identifying a version.
- The contribution instructions use both “Civi-Import” and “CiviImport” for the extension.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: common-workflows/importing-data-into-civicrm-part3.md
destination_path: common-workflows/importing-data-into-civicrm-part3.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/common-workflows/importing-data-into-civicrm-part3/
civicrm_version:
- latest
last_modified: '2026-10-06'
---

# Import requirements for activities, contributions, memberships, participants and tags

## Import activities

To **insert new activities**, the CSV file must include at least:

- Activity Date
- Activity Type ID
- Target Contact ID (Match to Contact)
- Subject

To **update existing activities**, the CSV file must include at least:

- Activity ID
- Activity Date
- Activity Type ID
- Target Contact ID (Match to Contact)
- Subject

Target Contact ID attaches the activity to the contact the activity is done on. Import contacts before running the activity import; these are separate import jobs.

## Import contributions

You can insert new contributions or update existing ones. If you are on a recent version of CiviCRM and enable the Civi-Import extension, you can also create or update the contact and any soft credit contacts in the same import.

To **insert new contributions**, the CSV file must include at least:

- Fields to match (or create) the contact.
- Financial Type
- Total Amount

The contact fields required depend on whether Civi-Import is enabled. If it is not, you need:

- Contact ID or External Identifier or all the fields used in your Unsupervised Duplicate Matching rule (to match to an existing contact)

If CiviImport is enabled, the above still applies to matching contacts, but you can specify which Dedupe rule to use.

!!! tip "See also"
    [Importing contributions](../contributions/importing.md) in the Contributions chapter.

To **update existing contributions**, the CSV file must include at least:

- Transaction ID or Invoice ID or Payment ID (to match to an existing contribution)
- Financial Type
- Total Amount

You can also use **update existing contributions** to import new data or change existing data in other core or custom contribution fields. Include an ID to match the existing contribution, plus Financial Type and Total Amount in the CSV file, even if the values for those fields have not changed.

## Import memberships

You can insert new memberships or update existing memberships.

To **insert new memberships**, the CSV file must include at least:

- Contact Id or External Identifier or all the fields used in your Unsupervised Duplicate Matching rule (to match to an existing contact)
- Membership Type
- Membership Start Date

To **update existing memberships**, the CSV file must include at least:

- Membership Id (to match to an existing membership)
- Membership Type
- Membership Start Date

You can also use **update existing memberships** to import new data or change existing data in other core or custom membership fields. Include Membership ID to match the existing membership, plus Membership Type and Membership Start Date in the CSV file, even if the values for those fields have not changed.

!!! tip "See also"
    [Importing memberships](../membership/manual-entry-of-memberships.md#importing-memberships) in the Memberships chapter.

## Import participants

In each import session, you can either insert new registrations or update existing participant records.

To **insert new registrations**, decide whether to restrict registrations for each event to one per person (set **On duplicate entries** to **Skip)** or allow duplicate registrations for the same event from a contact (set **On duplicate entries** to **No Duplicate Checking)**. In either case, the CSV file must include at least:

- Contact Id or External Identifier or all the fields used in your Unsupervised Duplicate Matching rule (to match to an existing contact)
- Event ID
- Participant Status

To **update existing registrations**, set **On duplicate entries** to **Update**. The CSV file must include at least:

- Participant ID (to match to an existing registration)
- Event ID or Event Title
- Participant Status

You can also use **update existing registrations** to import new data or change existing data in custom participant fields. Include Participant ID to match the existing registration, plus Event ID or Event Title and Participant Status in the CSV file, even if the values for those fields have not changed.

## Import tags

There is currently no inbuilt way to import tags or tag sets. You can use [this advanced extension](https://civicrm.org/extensions/api-csv-import-gui "API csv Import GUI").

To assign individual tags during a contact import, either:

- Split the CSV file by individual tags and import each subset separately as described above.
- Create temporary custom fields and import tags into them as standard data. After import, use advanced searches to isolate contacts with particular values and mass tag them. You can remove the custom fields when finished.

<!-- Source: common-workflows/importing-data-into-civicrm-part3.md -->
