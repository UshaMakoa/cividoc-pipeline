---
title: Offline fundraising
category: how-to
topic: contributions
subtopic: postal-appeals
component: CiviCRM Contributions
audiences:
- fundraising-manager
- operations-user
- administrator
level: basic
journey_stage: everyday-tasks
summary: Create a contact list and postal mailing materials for an offline appeal, then enter the contributions received.
extensions: []
related:
- manual-entry-of-contributions.md
review_priority: medium
review_notes:
- The export instructions say that choosing primary fields generates the CSV file when Continue is clicked, but a later step
  also instructs the reader to click Export. The source does not clarify which steps apply to each choice.
- The final note refers to a "research results page"; it is unclear whether this means the search results page.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: contributions/offline-fundraising.md
destination_path: contributions/offline-fundraising.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/contributions/offline-fundraising/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Offline fundraising

Your organisation may collect donations at events, through postal mailings, and by other offline methods. Money raised through offline activities needs to be manually entered into CiviCRM so that final reporting is accurate.

Offline fundraising in CiviCRM has three steps: creating your lists, creating your mailings, and [manually entering Contributions](manual-entry-of-contributions.md).

## Creating your lists

If you are familiar with CiviCRM's search capabilities, this process is fairly straightforward.

Go to **Search &gt; Find Contacts** to create a list of records to receive your offline postal mail appeal. The list could include your entire database.

If you want to track the success of a mailing or who receives certain appeals, save the search results as a group. Use the check box to select all, then choose **Group - add contacts** or **Group - create smart group** from the **Action** dropdown menu. Later, you can mark everyone in that group as recipients of the appeal using **Add Activity** under the **Actions** dropdown menu.

To create letters for postal mailings, use CiviCRM's internal **PDF letters - print** feature, or export the list as a CSV file and use mail merge with a word processor.

To export a list:

1. Select all records or a subset using the checkboxes, and choose **Export Contacts** from the **Actions** dropdown menu.
2. Choose whether to **Export PRIMARY fields** or **Select fields for Export**. If you elect to export primary fields, the CSV file will be immediately generated when you click **Continue**. If you opt to select which fields you want to export, click **Continue** and a list of dropdown options will appear.
3. Select the required fields. To save the list of exported fields as an export mapping for future use, check **Save this field mapping**.
4. Click **Export** to generate the CSV file.
5. Click **Done** when you have finished to return to the contact list.

## Creating postal mailings

Once your spreadsheet is created, you can do a mail merge using any word processing software, such as OpenOffice, the free software word processor, to insert the fields you want in the letter.

CiviCRM can also create mailing labels. Perform the same search you used to create your list of recipients, then:

1. From the **Actions** dropdown menu, select **Mailing labels - print**.
2. Select the mailing label number. Decide whether to exclude people with "do not mail" checked in their privacy options (checked by default and recommended), and whether to merge two records with the same mailing address into one label. Merging is useful when mailing a household or organization and you do not want them to receive duplicate mailings. When the records are merged, each name at that address appears on its own line on the label.
3. Click **Make Mailing Labels** to create a printable PDF document.

Note that CiviCRM prints labels in the order shown on the research results page in a column-by-column pattern.

<!-- Source: contributions/offline-fundraising.md -->
