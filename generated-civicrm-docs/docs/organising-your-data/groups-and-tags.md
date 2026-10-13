---
title: Groups and tags
category: explanation
topic: groups-and-tags
subtopic: groups-and-tags
component: Groups and tags
audiences:
- administrator
- operations-user
- communications-manager
level: basic
journey_stage: overview
summary: Understand how groups and tags categorise records and choose between them.
extensions: []
related: []
review_priority: medium
review_notes:
- The Smart Group example uses the year 2010; confirm whether this dated example should be refreshed.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: organising-your-data/groups-and-tags.md
destination_path: organising-your-data/groups-and-tags.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/organising-your-data/groups-and-tags/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Groups and tags

Groups and tags are two key methods of organising data in CiviCRM. Both can help you segment and search your database, but they serve different purposes.

A common approach is to use tags as descriptive categories for contacts, activities, and cases, and groups for collections of people that need to be treated as a cohesive unit—for example, to receive a mailing. Under this approach, *volunteer*, *ally organisation*, *vegetarian*, and *musician* would be tags, while *Volunteer Committee*, *Allied Organisations Coalition*, *Vegetarian Newsletter*, and *This Awesome Band With A Bad Name* would be groups. This is a guideline rather than a rule.

## Groups

Groups are collections of contacts that have something in common. They play a role in CiviMail and Profiles and can be used to set up advanced access rights on Drupal. Well-defined groups help segment a CiviCRM contact database.

There are two kinds of groups:

- **Groups**, also called regular groups, have contacts that you manually add and remove. For example, you can assign your organisation's board members to a Board of Directors group, then email that group without searching for and selecting each member individually.
- **Smart Groups** are configured to include contacts that share characteristics or activities. As contacts are added or edited, CiviCRM checks whether they meet the configured criteria and adds them if they do. For example, a Smart Group for “2010 Contributors from California” could include contacts who contributed in 2010 and have an address in California. New contacts who meet both criteria are automatically added. Another Smart Group could contain donors who have not yet been sent a thank-you letter: as you send letters, their recipients automatically leave the group.

## Tags

**Tags** categorise contacts, activities, and cases. You can create as many as needed, but avoiding duplicate or unnecessary tags makes them easier to use. A standard process for creating and using tags can help.

## Groups versus tags {#groups-vs-tags}

Which method to use depends on how you intend to segment contacts. Having both lets you make refined searches using AND and OR. For example, if journalists, volunteers, and members are groups, while development, art, and history are tags for interests, you can find journalists interested in art or development, volunteers or members interested in history, or other combinations.

Groups also have features that tags do not:

- Groups are integrated with other CiviCRM functions, notably CiviMail.
- Contacts can be added to Smart Groups automatically based on their characteristics.
- Groups can be associated with Drupal Organic Groups.

Tags can be applied to contacts, activities, and cases; groups consist only of contacts.

### Benefits of tags

- Tags are easy to set up and use.
- You can search by tag in Basic or Advanced Search.
- You can combine tags with other properties, such as residence state/province, to create Smart Groups.

### Limitations of tags

- You cannot create tags for only a specific contact type—for example, tags that are *only* for Individual contacts.
- When you export tags, all tags assigned to a record are exported as a list in one cell, such as “Teacher, Volunteer”.
- Tags allow multiple selections, so they may not suit mutually exclusive characteristics such as “Democrat”, “Republican”, and “Green Party”.
- You cannot selectively hide or permission tags on built-in or Profile create and edit forms; all tags appear on edit forms.

### Benefits of groups

- Groups offer a flexible way to segment contacts for a range of purposes.
- Groups support recurring tasks such as sending an enewsletter or printing mailing labels.
- Groups let you restrict access to “special” sets of contacts.
- Groups support administrative and end-user “subscribe” and “unsubscribe” actions, and the system keeps a history of those actions.
- Visibility settings let you choose which groups appear to end-users on Profile forms; some groups can be “private”.
- You can create Smart Groups that combine members of Group A + Group B.

### Limitations of groups

- All existing groups appear under Manage Groups and in search forms. If your organisation has many groups, these lists may become overloaded.
- Groups used for short-term projects should be “purged” when no longer needed.
- When you export contact records, all groups a contact belongs to are exported as a single comma-separated list, such as “Administrators,Newsletter Subscribers”.

<!-- Source: organising-your-data/groups-and-tags.md -->
