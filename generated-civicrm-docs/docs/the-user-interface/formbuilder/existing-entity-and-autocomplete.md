---
title: Creating a custom autocomplete search list
category: how-to
topic: search
subtopic: existing-records-in-forms
component: SearchKit and FormBuilder
audiences:
- administrator
- membership-manager
- operations-user
level: intermediate
journey_stage: plan-and-configure
summary: Create a filtered autocomplete list with identifying details and add it to a form.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: the-user-interface/formbuilder/existing-entity-and-autocomplete.md
destination_path: the-user-interface/formbuilder/existing-entity-and-autocomplete.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/the-user-interface/formbuilder/existing-entity-and-autocomplete/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Creating a custom autocomplete search list

Create a filtered list of existing records with extra details, such as a street address, to help your team identify the right person in a dropdown list.

For example, if you organize an event, you might want to assign certain activities only to contacts with the Volunteer subtype. Showing each volunteer’s name, street, and city in the dropdown can help users choose the right person.

## Create your search list

1. Navigate to **Search** in your main CiviCRM menu and click on **SearchKit**.
2. Click the **New Search** button.
3. In the **Search for** field, choose Contact (or another specific record type you need to display, such as volunteers).
4. Use the **Where** section to filter the list if you only want specific people to appear, such as those matching availability, age, or group membership criteria.

## Set up the autocomplete display

1. Click the **+ Add** button on the left-hand side and choose **Autocomplete**.
2. Put your main searchable field—usually the contact's name—first in the list layout.
3. Add informative fields below it, such as **Street Address** and **City**. These appear alongside the name in the dropdown to help users distinguish people with similar names.
4. Select an **Ascending** sort order for the contact name field to display the list alphabetically.
5. Give the autocomplete display a clear name and **save** your progress.

## Add the autocomplete field to a form

After creating the autocomplete list in SearchKit, add it to a form using FormBuilder.

### Add the contact field

1. Open your desired form layout in **FormBuilder**.
2. Find the **Existing Contact** field under **Add** in the left-hand panel.
3. **Click and drag** the Existing Contact field onto the form canvas where you want it to appear.

### Connect your custom autocomplete list

1. Click the **settings wheel** for the Existing Contact field on the form canvas to open its properties panel.
2. If relevant, change the **Type** to Autocomplete.
3. Under the **Saved Search** drop-down, select the **custom search** list and autocomplete display you created.

### Configure the field settings

1. Check **Required** if your team must select a record before submitting the form.
2. Turn on **Auto-open** so the dropdown expands when someone clicks inside the field.
3. Choose the appropriate **permission** type:
   - Choose **Form-based** for most standard administrative forms where anyone filling out the form should be able to see the full list of options.
   - Choose **User-based** if your organisation uses Access Control Lists (ACLs) to limit which contacts staff members can view based on their user accounts.
4. **Save** your form changes.

<!-- Source: the-user-interface/formbuilder/existing-entity-and-autocomplete.md -->
