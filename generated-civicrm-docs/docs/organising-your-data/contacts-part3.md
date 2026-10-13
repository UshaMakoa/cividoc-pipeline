---
title: Configure contact subtypes and the contact view
category: how-to
topic: contacts
subtopic: contact-types-and-display
component: Contacts
audiences:
- operations-user
- administrator
level: intermediate
journey_stage: plan-and-configure
summary: Define contact subtypes and choose which contact information appears on editing and summary screens.
extensions: []
related:
- creating-custom-fields.md
- ../initial-set-up/customizing-the-user-interface.md#changing-display-preferences
review_priority: low
review_notes:
- The source calls the three default contact types “individuals, households and contacts” here, but lists Individuals, Organisations
  and Households earlier. The conflicting wording has not been corrected.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: organising-your-data/contacts-part3.md
destination_path: organising-your-data/contacts-part3.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/organising-your-data/contacts-part3/
civicrm_version:
- latest
last_modified: '2026-10-06'
---

# Configure contact subtypes and the contact view

## Contact subtypes

In addition to the three default contact types (individuals, households
and contacts), you can define additional contact types (sometimes
referred to as contact subtypes) to suit your needs.

Each contact subtype is based on one of the three core contact types. For example, &#39;Student&#39; would be based on &#39;Individual&#39;. &#39;Farm&#39; could be based on &#39;Organization&#39; or perhaps &#39;Household&#39;, depending on your use case.

Contact types are useful when you need different sets of custom data for different contacts. For example, you might collect subject areas and qualifications for teachers but not for other individuals. To do this, you would create a contact type called Teacher, based on Individual, and a custom data set that extends only Individuals of the type Teacher. See custom data for more information.

Core contact types are mutually exclusive: a contact cannot be both an organisation and an individual. A contact can, however, have more than one user-defined subtype—for example, Teacher and Parent.

To edit existing contact types or create new ones, go to **Administer > Customize Data and Screens > Contact Types**. You cannot delete the inbuilt contact types, but you can change their names and associated images.

To add custom fields to specific contact subtypes, see [custom fields](creating-custom-fields.md).

## Customizing the view of contacts

If sections or fields on the contact editing and summary screens are not useful to your organisation, you can hide some of them. For example, you can remove demographics information by configuring Site Preferences. Using an account with Administer CiviCRM privileges:

1. Go to **Administer > Customize Data and Screens > Display Preferences**.
2. Clear the Demographics box under Editing Contacts.
3. Click Save.

You can also use this screen to rearrange the order in which information is displayed. For more detail, see [Customizing the user interface](../initial-set-up/customizing-the-user-interface.md#changing-display-preferences).

To remove or add fields in the postal address section:

1. Go to **Administer > Localization > Address Settings**.
2. Check or uncheck fields under Address Editing.
3. Click Save.

You can disable or enable specific tabs from **Administer > Customize Data and Screens > Display Preferences**. If you do not see some of the tabs described on the contacts page, you may need to enable them. Some tabs also depend on enabled components; for example, the Contributions tab is hidden if the CiviContribute component is disable.

<!-- Source: organising-your-data/contacts-part3.md -->
