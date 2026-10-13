---
title: Import contributions
category: how-to
topic: data-management
subtopic: importing-contributions
component: CiviContribute
audiences:
- fundraising-manager
- operations-user
level: intermediate
journey_stage: manage-and-automate
summary: Prepare contribution import data and match contributions to existing contacts.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: contributions/manual-entry-of-contributions-part4.md
destination_path: contributions/manual-entry-of-contributions-part4.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/contributions/manual-entry-of-contributions-part4/
civicrm_version:
- latest
last_modified: '2026-10-06'
---

# Import contributions

If you have not imported data before, read [Importing data into CiviCRM](../common-workflows/importing-data-into-civicrm.md).

## Required fields

Include these fields in your CSV import file:

- Financial Type
- Total Amount
- One of the following:
    - Contact ID (Match to Contact) OR
    - Email (Match to Contact) OR
    - External Identifier (Match to Contact)

Note: Financial Type is the full text of the Financial Type Name, not the Financial Type ID.

## Matching contributions to contacts

The import tool for contributions is similar to that of contacts, but contributions cannot be imported unless the contributors already exist in the database as contacts. If you need to import contributions for contacts that are not yet available, run a contact import first, preferably including a unique external identifier (most often an ID assigned by the database or application you are importing records from).

There are two ways to match a contribution to a contact:

- Use the external ID of the contact by including the ID in a column of the CSV file. If this ID was not imported with contacts, but you have them on record, a second contact import could be run to update this field, after which you may import contributions.
- Alternatively, match contributions to contacts based on your contact de-dupe rules, e.g. by including the first name, last name and email address of the donor against each contribution in the file. If a contact matches these three fields, the contribution will be assigned to it.

## CSV file size

CSV files must be less than 2MB in size. If a file exceeds this, create multiple CSV files and distribute the data between them.

<!-- Source: contributions/manual-entry-of-contributions-part4.md -->
