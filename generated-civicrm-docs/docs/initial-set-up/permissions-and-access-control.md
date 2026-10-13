---
title: Permissions and access control
category: explanation
topic: permissions
subtopic: choosing-an-access-control-method
component: CiviCRM
audiences:
- administrator
- operations-user
level: basic
journey_stage: overview
summary: Understand the difference between CMS permissions and CiviCRM ACLs before deciding how to control access.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: initial-set-up/permissions-and-access-control.md
destination_path: initial-set-up/permissions-and-access-control.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/initial-set-up/permissions-and-access-control/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Permissions and access control

Permissions and the related concept of access control lists (ACLs) are collections of rules that define access to areas of the system. You create roles for your site, give those roles permissions to do certain things, and assign the roles to people.

Permissions and ACLs allow you to grant access to:

- Different areas of CiviCRM, such as CiviContribute, CiviCase and CiviMail, according to the tasks a user is responsible for.
- Entities within the system, such as contacts and contributions, and ways to interact with them, such as viewing, editing and deleting.

Permissions define who can see and do what on your site. From a security perspective, it is important to understand them before checking a permissions box: badly configured permissions may inadvertently expose your contacts' data.

## The difference between CMS permissions and CiviCRM ACLs

Permissions and ACLs are defined in two places: the content management system (CMS) and CiviCRM itself. Many organisations can meet their needs with CMS permissions alone. Others need CiviCRM ACLs for more fine-grained access control.

CMS permissions grant or deny user roles access to entire sections of CiviCRM, such as CiviMail and CiviEvent. They also restrict whether users can view, edit, add and delete records such as contacts, events and contributions. This is an 'all or nothing' approach: for instance, you cannot differentiate between contacts in different groups.

Native CiviCRM ACLs offer finer-grained control. For example, you can limit access to view, edit, create, delete and search to:

- groups of contacts
- a profile (a collection of existing and/or custom fields; see "*Profiles*")
- a set of custom fields
- events (for example, a user may access one event but not others)

As a general rule, start with CMS permissions. If they cannot meet your needs, consider CiviCRM ACLs for more granular access rights.

These examples show when to use CiviCRM ACLs instead of access controls in Drupal, Joomla! or WordPress:

1. An organisation has a head office and three regional offices. The event director at the central office must be able to view all events, while coordinators at each regional office should only view and edit their own events. A CMS access control list can restrict viewing, editing, adding or deleting *all* events or *no* events, but cannot distinguish events by office. A CiviCRM ACL is needed.
2. A team in Paris manages volunteers using one set of custom fields, while a team in London collects donor information in another set. Each team should access only its own set. A CMS access control list could grant access to all custom information or none of it. In this case, disable any CMS rule controlling access to custom fields and use a CiviCRM ACL instead.

<!-- Source: initial-set-up/permissions-and-access-control.md -->
