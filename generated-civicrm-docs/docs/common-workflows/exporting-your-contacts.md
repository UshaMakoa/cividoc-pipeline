---
title: Exporting your contacts
category: how-to
topic: contacts
subtopic: exporting-contacts
component: CiviCRM contacts
audiences:
- operations-user
- administrator
level: basic
journey_stage: everyday-tasks
summary: Export contact data to a CSV file using primary fields or a reusable selection of fields.
extensions: []
related:
- ../searching/searching.md
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: common-workflows/exporting-your-contacts.md
destination_path: common-workflows/exporting-your-contacts.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/common-workflows/exporting-your-contacts/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Exporting your contacts

Exporting provides a copy of CiviCRM data in comma separated value (CSV) format for use in external applications. You can view and edit a CSV file in a spreadsheet application, import it into another database application, or merge it with a word processing document.

You can export a predefined set of fields or create a custom export mapping and save it for reuse.

Exporting is available:

- In any of the search tools.
- When viewing contacts in a group.
- In component-based search results, where the records reflect component-specific data rather than only core contact data. For example, from **Contributions &gt; Find Contributions**, you could export donors and their contact information for a thank-you letter that includes the total amount donated.

## Export contact information

1. Search for contacts using your desired criteria in Quick search, Find Contacts, Advanced search, Search Builder, or a custom search. For more information, see [Searching](../searching/searching.md).
2. Select all records, or use the check-boxes to the left of each record to select individual contacts.
3. From the **- actions -** dropdown menu, choose **Export Contacts**. This opens the export wizard.

    ![ExportFromSearch](../img/CiviCRM_update-CiviCore-ExportFromSearch-en.png &quot;ExportFromSearch&quot;)

4. Choose whether to export the primary fields or select your own fields.

    ![ContactExportOptions](../img/contact-export-options.png &quot;ContactExportOptions&quot;)

    A primary fields export contains 80 fields: core contact fields with primary email, phone, and address data. Selecting your own fields lets you include non-primary email, phone, and address data, custom contact fields, and data from related contacts. You can also use a previously saved export mapping, if you have one.

    - For mailing labels, choose whether to export one record per household or one per address. If you choose one record per address, you can specify the format for Addressee and the postal greeting.
    - You can exclude contacts with &quot;do not mail&quot; privacy, no street address, or who are deceased.
    - You can add contacts from an additional group to the export.

5. Click **Continue**. If you chose the primary fields, the export happens immediately; go to step 7. If you chose your own fields or a saved field mapping, continue to step 6.
6. Select the fields to export.

    ![ContactExportFieldSelection](../img/contact-export-field-selection.png &quot;ContactExportFieldSelection&quot;)

    - If you chose a saved export mapping, its fields are displayed. You can use the mapping as is or modify it. If you modify it, you can update the existing field mapping or save the changes as a new field mapping.
    - If you are creating a new mapping, choose the fields you want, then decide whether to **Save this field mapping** for later use.
    - When the fields and other options are correct, click **Export**.

7. The file is exported in .CSV format. By default, a comma is used as the field separator for import and export functions. If required, change the separator at **Administer &gt; Localization &gt; Languages, Currency, Locations** by selecting the appropriate **Import/Export Field Separator**.

<!-- Source: common-workflows/exporting-your-contacts.md -->
