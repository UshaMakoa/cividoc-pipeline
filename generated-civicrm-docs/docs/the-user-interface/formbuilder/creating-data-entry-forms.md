---
title: Creating custom data entry forms
category: how-to
topic: forms
subtopic: data-entry-forms
component: FormBuilder
audiences:
- administrator
- operations-user
- technical
level: basic
journey_stage: plan-and-configure
summary: Create, configure, and preview a custom form for collecting data in CiviCRM.
extensions: []
related: []
review_priority: low
review_notes:
- The Permission section says 'the following three' but lists four options.
- The field-tab example says 'Inidividual 1', while the settings examples say 'Individual 1'; verify the label.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: the-user-interface/formbuilder/creating-data-entry-forms.md
destination_path: the-user-interface/formbuilder/creating-data-entry-forms.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/the-user-interface/formbuilder/creating-data-entry-forms/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Creating custom data entry forms

Your organisation can design custom forms to collect information from members, supporters, or staff. Using CiviCRM's form tool **FormBuilder**, you can build interactive forms for manual data entry, such as creating new contacts or logging specific activities, without needing any technical knowledge.

## Create a new data entry form

1. Look for the **New Submission Form** button at the top of the FormBuilder interface.
2. Click the small downward-pointing arrow to the right of the button text. This reveals a dropdown menu listing the types of items (entities) you can collect data for, such as Activities, Contacts, Cases, etc.
3. Click the type of item you want your form to create. CiviCRM will automatically open the form design workspace.

## Set up your form's settings

The form workspace is split into two halves. Use the configuration pane on the left side to define how your form behaves, where it lives, and who can see it.

### Choose who can use the form

Under the **Form Settings** section, locate the **Permission** dropdown. Choose the rule that matches your specific purpose - the following three are :

- The default option is **Access CiviCRM backend and API**, which means that all users with access to CiviCRM will be able to access the form.
- Select **Generic: Allow any authenticated contact** if you want to limit entries to supporters who are logged into your website or accessing the form via a verified email link.
- Select **Generic: Anyone with secret link** if you intend to share this form strictly via direct, private email invitations.
- Select **Generic: Allow all users (including anonymous)** if the form is public and open to anyone on your website (such as a generic sign-up page).

### Publish the form to your website

To make your form a standalone page that people can visit:

1. Scroll down to the **Placement** options on the left pane.
2. In the **Page Route** box, type a clear web path starting with `civicrm/` (for example, `civicrm/volunteer-signup`).
3. Check the box labeled **Accessible on front-end of web site** to ensure regular visitors can view the page.
4. If you want this form to be easily found by your staff, check the option to add the form directly to your CiviCRM navigation menu.

## Add fields and layout elements

Once your settings are configured, use the second tab in the left-hand configuration pane to add content fields to your form layout. This tab lists the standard fields and custom fields relevant to the entity type you chose, for example 'Inidividual 1'.

1. Browse the list of available fields in the left pane.
2. Click and hold the field you want to use, then drag it over to the layout view on the right side of the screen.
3. Release your mouse button to drop the field into place. You can drag fields up and down to change their order.
4. Click the small **Settings icon** directly on any field in the layout pane to customize its specific behavior, like changing the text label or making it a required field.
5. To structure your form, look under the **Elements** list in the left pane. Drag and drop structural blocks, text containers, or HTML areas to add instructions and section breaks for your users.

### Additional permissions

Each entity tab on the left-hand configuration pane also has additional options and settings. For example, if you are building a form to capture information for an Individual, these would be the options:

- **Individual 1: Security**: you can choose whether the autofill options work based on the form permissions or the user's permissions
- **Individual 1: Autofill**: There are a list of option, for example Current User or the Contact being Viewed.
- **Individual 1: Allowed Actions**: The options are create, update or both.
- **Individual 1: Accept ID from URL**: If 'Update' is specified for allowed actions, it is possible to pull the ID from the URL to autofill the fields.

## Save and review your form

When your layout looks correct and all settings are complete:

1. Click the **Save** button in the upper-right area of the screen.
2. Once saved, a **View** button will appear next to your saving options. Click it to preview exactly how your live form will look to users, and to copy its website link for distribution.

<!-- Source: the-user-interface/formbuilder/creating-data-entry-forms.md -->
