---
title: Importing memberships
category: how-to
topic: memberships
subtopic: importing
component: CiviMember
audiences:
- membership-manager
- operations-user
level: intermediate
journey_stage: manage-and-automate
summary: Prepare and import membership records from outside CiviCRM or update existing memberships.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: membership/manual-entry-of-memberships-part2.md
destination_path: membership/manual-entry-of-memberships-part2.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/membership/manual-entry-of-memberships-part2/
civicrm_version:
- latest
last_modified: '2026-10-06'
---

# Importing memberships

Use **Importing Memberships** for a large set of membership records from outside CiviCRM or to update large numbers of existing memberships with new information.

!!! tip "See also"
    The [Importing Data](../common-workflows/importing-data-into-civicrm.md) page explains the import process generally and has a section specifically on [importing memberships](../common-workflows/importing-data-into-civicrm.md#import-memberships).

Before importing:

- Contact records must exist. If the contacts are not yet in CiviCRM, first import the Contact data. Make sure it has an External ID that you can include with the membership data to associate the records. For existing contacts, use the Internal Contact ID or the fields from your Unsupervised Duplicate Matching Rule to associate the membership data with the correct contact.
- The membership import file MUST contain both Membership Type and Start Date. Membership types must exactly match those set up by your CiviCRM Administrator, and the start date must use the date format specified for your CiviCRM installation. Without these fields, you cannot import the file.
- Import membership data for different contact types separately; files with more than one contact type will not work. Import new memberships and renewals separately as well.

To import the membership data:

1. Navigate to **Memberships > Import Memberships**.
2. On the Upload Data screen:
    - Select your import data file. It must be a CSV file.
    - Select the checkbox if your source data contains column headers.
    - Specify the contact type you are importing.
    - Indicate what date format you are using.
    - Click **Continue >>**.
3. On the Match Fields screen, map your membership data to the appropriate CiviCRM fields under the Matching CiviCRM Field column. You can **Save this field mapping** for future imports.
4. On the Preview screen, review the table showing Total Rows in the uploaded file, rows with errors, and valid rows. If you continue, rows with errors will be skipped. You can download a file containing just the problem records, continue with the import, correct those records, and import them again. Alternatively, correct your original CSV file and restart the import.
5. If there are no errors or you do not want to correct the errors found, click **Import Now>>**. You will see the import progress and, when it is complete, a summary of the activity and results.

<!-- Source: membership/manual-entry-of-memberships-part2.md -->
