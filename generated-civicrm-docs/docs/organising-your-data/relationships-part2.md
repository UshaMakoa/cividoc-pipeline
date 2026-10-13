---
title: Managing relationship types
category: how-to
topic: general
subtopic: relationship-types
component: CiviCRM relationships
audiences:
- administrator
- operations-user
level: intermediate
journey_stage: plan-and-configure
summary: Create relationship types, add custom relationship fields, and disable or delete types that are no longer needed.
extensions: []
related:
- creating-custom-fields.md
review_priority: high
review_notes:
- The source gives different navigation paths to Relationship Types for creating a type and for disabling or deleting one;
  both paths are preserved.
- The disabling procedure says to click the Delete button after reviewing either the Disable or Delete confirmation; this
  potentially misleading instruction is preserved.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: organising-your-data/relationships-part2.md
destination_path: organising-your-data/relationships-part2.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/organising-your-data/relationships-part2/
civicrm_version:
- latest
last_modified: '2026-10-06'
---

# Managing relationship types

## Creating new relationship types

CiviCRM comes with a set of common relationship types that can be used to indicate relationships between contacts. If you need to track different types of relationships between your contacts, you can create your own custom relationship types.

!!! tip "Special Relationship Types"
    * **Employee <-> Employer relationship** is created anytime the 'Current Employer' field is filled in, either in the Contact Summary form or via a Profile. When filled in, it will create an Organisation if one does not already exist with that name.
    * **Household relationship** enables household members to have the 'household address' applied to their record. Again, if a Household already exists then the individual will have a relationship created with it, if none exists then a new household will be created.

1. In the navigation menu, go to: **Administer > Customize Data and Screens > Relationship Types**.
2. Review the list of existing relationship types to ensure that you are not creating a duplicate.
3. If the relationship type you need does not already exist, click the **New Relationship Type** button.
4. Enter descriptive labels for the relationship type you are creating in the **Relationship Label-A to B** and **Relationship Label-B to A** fields. The **Relationship Label-A to B** field describes the relationship between Contact A and Contact B; the **Relationship Label-B to A** field describes the relationship between Contact B and Contact A.
   - Some relationships can be described by the same label in both directions; in these cases you can enter the Relationship Label once in the **Relationship Label-A to B** field. For example, when describing the relationship between two domestic partners named Sylvia and Audre, you can say that Sylvia is the "Partner of" Audre and Audre is the "Partner of" Sylvia. Therefore you would enter the "Partner of" label only in **Relationship Label-A to B** field, leaving the **Relationship Label-B to A** field blank.
   - In other situations one Relationship Label cannot be applied in both directions; in these cases you need to enter different Relationship Labels in each of the Relationship Label fields. For example, you can say that Kiyoshi is the "Grandparent of" Yuki but you cannot say that Yuki is the "Grandparent of" Kiyoshi. Therefore you would enter the "Grandparent of" label in the **Relationship Label-A to B** field and either "Grandchild of" or "Grandparent is" in the **Relationship Label-B to A** field.
5. Use the **Contact Type A** and **Contact Type B** fields to designate which contact types are being linked by your relationship. Remember to check that the contact types you select for Contact A and Contact B make sense when corresponded to your Relationship Labels.
6. Optionally enter **Description** for this relationship type. This is especially useful if the intended purpose of this relationship type may not be obvious to other users.
7. Leave the **Enabled** box checked unless you intend to create this relationship type but not allow users to utilise it until a future date.
8. Click **Save**. You will see a message telling you that the relationship type has been saved and you will see your new Relationship Type in the list below.

## Creating custom fields on relationships

CiviCRM provides a number of standard relationship fields, described above. You may decide there is other information you want to store, either on all relationships, or just on given relationship types. Additionally, custom fields can be used as a tool to further distinguish relationships without creating inordinate numbers of types (e.g. you could track which department an employee works in using a custom field, rather than creating a new relationship type for each). You can add custom fields that display on the relationship types of your choosing. See [creating custom fields](creating-custom-fields.md) for detailed instructions.

## Disabling or deleting unneeded relationship types

If an existing relationship type is no longer useful or relevant for your organisation, you can either disable or delete it so it is no longer presented as an option for new relationships. Disabling rather than deleting the relationship type has two significant advantages: you will still be able to see existing data on relationships of this type, and you can easily enable the relationship type again should you find you need it later.

1. In the navigation menu, go to: **Administer > Option Lists > Relationship Types**.
2. Click the **More** link in the row of the relationship type that you'd like to disable or delete.
3. Select either **Disable** or **Delete** from the pop-up menu.
4. If you select Disable, a pop-up confirmation bubble will appear. If you select Delete, you will be directed to an additional screen that provides a more serious warning and requests confirmation. Review the information provided in either confirmation message and if you are sure you'd like to complete this action, click the **Delete** button otherwise **Cancel**.
5. If you have chosen to disable the relationship type it will appear in red in the Relationship Types list and relationships of this type will still be visible when viewing contacts. If you have chosen to delete the relationship type it will no longer appear in the Relationship Types list or in contact relationships data. In either case users will no longer be able to create new relationships of this type.
6. To enable a previously disabled relationship type, follow steps 1 and 2 above and select **Enable** from the **more** pop-up menu.

<!-- Source: organising-your-data/relationships-part2.md -->
