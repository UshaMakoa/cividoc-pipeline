---
title: 'Example: Show events attended by employees on an Organization’s contact record'
category: how-to
topic: contacts
subtopic: contact-record-display
component: SearchKit and FormBuilder
audiences:
- operations-user
- administrator
- event-manager
level: intermediate
journey_stage: plan-and-configure
summary: Show events attended by an Organization’s employees on the Organization’s contact record.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: searching/searchkit/example-display-employees-participant-records.md
destination_path: searching/searchkit/example-display-employees-participant-records.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/searching/searchkit/example-display-employees-participant-records/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Example: Show events attended by employees on an Organization’s contact record

Use FormBuilder and SearchKit to show all the events attended by the employees of an Organization on the Organization’s contact record.

## Step 1: Create the saved search

1. Navigate to **Search &gt; SearchKit**.
2. On the Submission Forms tab, click the **New Search** link.

## Step 2: Add SearchKit settings

1. Give the search a **title** ‘Events Attended By Employees’.
2. On the **Search For** tab on the left:
   - Click **+ Entity** and choose **Contact Related Contacts**, change it to **With (required)**.
   - Click and change the **Relationship to Contact** value to **Employee of**.
   - Click **+ Entity** and choose **Contact Related Contacts - Contact Participants**, change it to **With (required)**.
   - Click **+ Entity** and choose **Contact Related Contacts - Contact Participants - Participant Event**, change it to **With (required)**.
3. On the **Select Fields** tab on the left:
   - Click on the **x symbol** to remove Contact ID, Sort Name, Contact Type, Contact Subtype.
   - Leave **Event Title**.
4. Still on the Select Fields tab, use the **+ Add Field** drop down to include:
   - Contact related contacts - Contact Participants - Participant Event - **Start Date**
   - Contact related contacts - **First Name**
   - Contact related contacts - **Last Name**
   - Contact related contacts - **Primary Email**
5. To add a display, click on **+ Add** on the lower left hand side of the screen and choose **Table**.
   - Give the Table a name. This name will show on the contact screen as the tab title.
   - Click **Sorting**, choose Contact related contacts - Contact Participants - Participant Event - **Start Date** and change the order to **Descending**.
   - Click **Columns &gt; Use Custom Columns**.
   - Click the down arrow on **Event Title** and edit the Header text to be **Event Name**.
   - Click the down arrow on **Start Date** and edit the Header text to be **Event Date**.
6. Click **Save** at the top of the screen.

## Step 3: Complete the form

1. At the top right of the page, click the **Forms** link.
2. Choose **Create form for Events Attended By Employees**. This will open FormBuilder in a new browser tab.
3. In the newly opened tab, use the configuration pane on the left side to configure these settings:
   - **Title**: Events Attended By Employees
   - **Placement**: Contact Summary Tab
   - **Contact Type**: Organization
4. Click **Save** at the top of the screen.

If you go to an Organization Contact record that has employees who have attended an event, they will be displayed in a new tab on the record, ‘Events Attended By Employees’.

<!-- Source: searching/searchkit/example-display-employees-participant-records.md -->
