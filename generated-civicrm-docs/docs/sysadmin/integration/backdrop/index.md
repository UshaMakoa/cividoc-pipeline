---
title: Integrating with Backdrop
category: explanation
topic: system-administration
subtopic: roles-and-access
component: Backdrop integration
audiences:
- technical
- administrator
- operations-user
level: basic
journey_stage: overview
summary: Understand how Backdrop modules, roles, and permissions affect CiviCRM integration and access.
extensions: []
related: []
review_priority: low
review_notes:
- The opening refers to four CMS that integrate with CiviCRM without naming or dating them.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: integration/backdrop/index.md
destination_path: sysadmin/integration/backdrop/index.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/integration/backdrop/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Integrating with Backdrop

Of all the four CMS that integrate with CiviCRM, Backdrop is most comparable to the deep integration that can be achieved with Drupal. This is primarily due to the fact that Backdrop is a port of Drupal 7 and repurposing work done for Drupal is relatively easy.

When thinking about website integration with Backdrop, it is important to understand **Backdrop modules**. A module provides a particular function: for example, the *calendar* module allows you to display calendars on your website. The Backdrop distribution of CiviCRM comes with a number of Backdrop modules that let you integrate CiviCRM with Backdrop in different ways.

## Backdrop roles and permissions

When you create a new Backdrop site **User** and CiviCRM is installed, a corresponding CiviCRM **Contact** is also created. Users and contacts have separate identification or index numbers.

*See also the permissions and access control chapter in initial set up for a general discussion of access control.*

Your Backdrop website allows you to create **Roles**. The website administrator gives roles to site users and grants each role **permission** to perform tasks—such as viewing, editing, deleting, and administering contacts—or to access information such as CiviCRM Contacts, CiviMail, CiviEvents, Backdrop Users, and specific content types.

Backdrop permission settings determine which tasks a **Role** can perform and which information it can access. They determine how much access a type of user has to configure modules or to view, create, edit, or change content, users, or CiviCRM Contact information.

For more information, read [Users: Roles and Permissions](https://backdropcms.org/user-guide/users-roles-and-permissions) at BackdropCMS.org.

Backdrop roles are global and will override relevant access controls (see chapter Initial Setup> Permissions and Access Control) setup in CiviCRM. For example, you can setup Access Control in CiviCRM to restrict access to contacts, but if the Backdrop permission 'Access All Contacts' is set, anyone with that role will be able to see all contacts regardless.

## Backdrop modules for role-based content access

Several Backdrop Modules determine which types of website content Backdrop **Roles** can access. Access can be based on Backdrop taxonomies; specific nodes; settings on views, pages, or panels; or certain contexts or rules. Common modules that control content access or include options based on Backdrop **Roles** are:

- Views (included in Backdrop by default)
- [Content View Access](https://backdropcms.org/project/content_view_access)
- [Simple Access Grants](https://backdropcms.org/project/simple_access_grants)

<!-- Source: integration/backdrop/index.md -->
