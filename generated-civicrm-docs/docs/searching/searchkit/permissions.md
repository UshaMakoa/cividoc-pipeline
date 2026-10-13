---
title: Permissions
category: reference
topic: permissions
subtopic: searchkit-and-formbuilder
component: SearchKit and FormBuilder
audiences:
- administrator
level: intermediate
journey_stage: plan-and-configure
summary: Understand how SearchKit display settings and FormBuilder form settings affect permissions.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: searching/searchkit/permissions.md
destination_path: searching/searchkit/permissions.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/searching/searchkit/permissions/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Permissions

Permissions for SearchKit and FormBuilder combine settings in:

- SearchKit
- FormBuilder
- CMS user roles (CiviCRM functionalities)
- ACL roles (fine-grained permissions)

## SearchKit

Every display you create in a search, such as a table or grid, has an “Enforce Permissions/ Bypass permissions” button at the top. It is a toggle, and its displayed text indicates the current state:

- `Enforce permissions` respects existing permissions defined in CiviCRM. Access control can be set at various levels, including roles in your content management system (CMS) and specific actions controlled by CiviCRM’s more detailed ACL controls. For more information, see [Permissions and Access Control](../../initial-set-up/permissions-and-access-control.md).
- `Bypass permissions` lets anyone who can view the display see all results, regardless of their permission level. This can be useful, but be careful what you expose.

![Enforce permissions](../../img/search-kit/permissions-01-enforce%20permissions.png)

![Bypass permissions](../../img/search-kit/permissions-02-bypass%20permissions.png)

## FormBuilder

For both Search forms and Submission forms:

- The form settings tab has a permission setting that determines who can view the form.
- Multiple permissions can be joined using “and” to require all of them, or “or” to require only one of them.
- Available permissions include CMS role permissions (e.g. WordPress : delete_pages) and CiviCRM permissions (e.g. CiviContribute: Access CiviContribute). Either or both can be used in this field.
- For more examples, see [who can use a form](../../the-user-interface/formbuilder/creating-data-entry-forms.md#choose-who-can-use-the-form) and the [additional permissions](../..//the-user-interface/formbuilder/creating-data-entry-forms.md#additional-permissions) that control whether a form autofills with data from the database.

<!-- Source: searching/searchkit/permissions.md -->
