---
title: Integrating with Drupal
category: explanation
topic: system-administration
subtopic: modules-and-access-control
component: CiviCRM Drupal integration
audiences:
- technical
- administrator
- operations-user
level: basic
journey_stage: overview
summary: Understand how Drupal modules, roles, and permissions relate to CiviCRM integration.
extensions: []
related: []
review_priority: low
review_notes:
- The comparison with “the three CMS” does not identify the other CMS or give a timeframe.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: integration/drupal/index.md
destination_path: sysadmin/integration/drupal/index.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/integration/drupal/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Integrating with Drupal

Of all the three CMS that integrate with CiviCRM, Drupal has received the most attention and offers the most integration options. This is in part because the Drupal community is largely a developer community.

When thinking about website integration with Drupal, it is important to understand **Drupal modules**. A module provides a particular function: for example, the *calendar* module lets you display calendars on your website. The Drupal distribution of CiviCRM comes with modules that integrate CiviCRM with Drupal in different ways.

## Drupal roles and permissions

When you create a new Drupal site **User** and CiviCRM is installed, a corresponding CiviCRM **Contact** is also created. Users and contacts have separate identification or index numbers.

*See also the permissions and access control chapter in initial set up for a general discussion of access control.*

Your Drupal website lets you create **Roles**. A website administrator assigns roles to site users and grants each role **permission** to perform tasks—such as viewing, editing, deleting, and administering contacts—or to access information such as CiviCRM Contacts, CiviMail, CiviEvents, Drupal Users, and specific content types.

For more information on Drupal Roles, see the Drupal.org documentation:

- [User: Access and management settings](http://drupal.org/documentation/modules/user)
- [Managing Access Control with Permissions and Drupal Roles](http://drupal.org/node/22275)

Drupal permission settings determine which tasks a **Role** can perform and which information it can access. Permissions determine how much access a type of user has to configure modules or to view, create, edit, or change content, users, or CiviCRM Contact information.

For more information on Drupal Permission settings, see the Drupal.org documentation:

- [User: Access and management settings](http://drupal.org/documentation/modules/user)
- [Assigning permissions and users to roles](http://drupal.org/node/22278)
- [Adjusting permissions after adding modules](http://drupal.org/node/22279)
- [Permissions reference](http://drupal.org/node/132202)
- [Views module permissions](http://drupal.org/node/1089746)

Drupal roles are global and override relevant access controls set up in CiviCRM (see chapter Initial Setup> Permissions and Access Control). For example, you can set up Access Control in CiviCRM to restrict access to contacts, but if the Drupal permission 'Access All Contacts' is set, anyone with that role can see all contacts regardless.

## Drupal taxonomies, content access, and other role-based user access modules

Several Drupal modules determine which types of website content Drupal **Roles** can access. Access can be based on Drupal taxonomies, specific nodes, settings on specific views, pages or panels, or contexts or rules. Common modules for controlling content access, or offering options based on Drupal **Roles**, include:

- [Views](http://drupal.org/project/views)
- [Panels](http://drupal.org/project/panels)
- [Chaos Tools Suite and Page Manager](http://drupal.org/project/ctools)
- [Context](http://drupal.org/project/context)
- [Content Access](http://drupal.org/project/content_access)
- [Taxonomy Access Control](http://drupal.org/project/taxonomy_access)

<!-- Source: integration/drupal/index.md -->
