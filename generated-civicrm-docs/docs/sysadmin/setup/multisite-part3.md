---
title: Multisite components and functional separation
category: reference
topic: system-administration
subtopic: components-and-entity-separation
component: CiviCRM multisite
audiences:
- administrator
- operations-user
- technical
- communications-manager
level: advanced
journey_stage: reference-and-troubleshooting
summary: Look up how multisite functionality is delivered and which entities are separated by domain.
extensions:
- multisite
related:
- https://lab.civicrm.org/extensions/multisite
review_priority: medium
review_notes:
- Several entries refer to CiviCRM 4.1, CiviCRM 4.7, the “latest version” of the extension, and upgrade issues; their applicability
  should be reviewed.
- The group-parent entry says parent ID is compulsory, then says parent ID OR organisational contact_id is required in the
  latest extension version; the distinction needs clarification.
- The scheduled jobs entry warns that mail will not go out unless jobs are configured for all domains, but does not give configuration
  directions.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/multisite-part3.md
destination_path: sysadmin/setup/multisite-part3.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/multisite-part3/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# Multisite components and functional separation

## Components of multisite functionality

| Functionality | Delivered by | Setting | Comments | Issues |
| --- | --- | --- | --- | --- |
| Various settings, urls can be domain specific, | CiviCRM Core - Settings table | This can be configured by domain or overridden at runtime in the civicrm.settings.php file - the latter is a good approach when only settings are dependent on the domain being accessed as it is simpler | Works well in general. | |
| payment processors are domain specific | CiviCRM Core | Based on domain_id in payment processor table | Domain_id set in civicrm.settings.php | |
| Domain contact details are domain specific | CiviCRM Core | Based on the contact_id in the civicrm_domain table | | |
| Navigation is domain specific | CiviCRM Core | Domain_id set in civicrm.settings.php | Works well except for WRT upgrades | A couple of upgrade issues are open on this |
| Reports are Domain specific | CiviCRM Core | Domain_id set in civicrm.settings.php | Works well in general | Upgrades are hit & miss on whether they update these correctly |
| Group Organization field is exposed | CiviCRM Core Multisite functionality | Domain_id set in civicrm.settings.php. `multisite_is_enabled` is set to 1. | Works fine, allows group to be set Group can be linked to multiple orgs in the schema but only single in the UI | |
| Contact is added to the group associated with the domain they are created on | CiviCRM Core Multisite functionality | Domain_id set in civicrm.settings.php. multisite domain group is specified. `multisite_is_enabled` is set to 1 | Works well | |
| Parent ID is compulsory for any group created This is implemented in 2 ways. People with the permission to ‘administer multiple organisations’ can choose the parents For others the parent will automatically be set to the domain group of the site it is created on | CiviCRM Core Multisite functionality - note that the parent ID OR the organisational contact_id is required in the latest version of the extension | Domain_id set in civicrm.settings.php multisite domain group is specified `multisite_is_enabled` is set to 1 | There are 3 possible scenarios for these nested groups 1. The child group is a non-smart group and only contains contacts also in the parent group. In this case the nesting will have no effect on the membership of the parent group 1. The child group is a non-smart group and contains contacts (intentionally or otherwise) not in the child group. The parent group is extended to include these contacts (not hard-added). Contacts added to this type of group extend the ACL visibility for those permitted to see this group 3. Child group is a smart group. Child group criteria extend the parent group. However this extended group is restricted by ACLs. Hence smart groups do not extend any ACLs that apply to the parent group (in core or in code) | This group nesting is problematic as it creates a large load in terms of creating the group_contact_cache entries of 2-3 levels of parent groups and resolving the smart group cache. Using the latest version of the extension & using group organisation for linkages will mitigate this. You can still use the hierarchical approach where you want to build up a hierarchical group for other purposes (e.g. mailing) Changes to groups frequently cause time outs & server load as the group cache is rebuilt for the parent group – inclusive of resolving every child smart group. |
| Contacts without ‘view all contacts’ permission but with ‘view all contacts in site’ are allowed to see all contacts in the domain group | CiviCRM multisite extension | Domain_id set in civicrm.settings.php, `multisite_is_enabled` is set to 1. multisite domain group is specified. `multisite_acl_is_enabled` is set to 1. | Permission is based on hard-adds to the domain group. WRT the 3 scenarios above 1) The addition of contacts to both parent and child groups is redundant 2) Hard adds to child groups extend the parent group and are useful where this is the intention (e.g. a child group that represents a sub-site. 3) Smart groups. Smart groups are cached in their entirety, both for the smart group and any parents it may have. This creates a lot of work. However, on their way out they are filtered according to the previous 2 items. | From a contact viewing permissioning point of view this suggests that only where #2 applies the group nesting is useful. As an aside the multisite extension currently works on an either or basis with other ACL hooks. Hence a contact can either view all contacts in domain OR have other code based ACLs applied. Some thought should go into desired behaviour when both are in use |
| Contacts without ‘view all contacts’ permission but with ‘view all contacts in site’ are allowed to see all groups within the site | CiviCRM multisite extension | Domain_id set in civicrm.settings.php. Multisite domain group is specified. `multisite_is_enabled` is set to 1. `multisite_acl_is_enabled` is set to 1 | This is currently tied with the group nesting & those groups that are children of the site group are visible. However, as seen above the nesting mechanism should only be used for child groups where it is desirable for hard-adds to that group that are not otherwise part of the domain be included in the parent group – ie. it should be used carefully & deliberately. Potential replacement mechanisms are group_organization & group_type. Either of these could be used to designate which domains a group should be visible on & either from a schema point of view support many to one, from a UI group_organization only supports one-to-one. Potentially people with ‘administer multiple organisations’ could create global smart groups & specify which sites they appear on. Those on sub-sites with administer civicrm could specify if the group is available on child sites. | |
| Shared User Table handling | Multisite extension | Extension enabled | UF_matches are updated where the user name name is the same on multiple domains. The multisite extension will manage this when enabled even when multisite & acls are turned off | |

## Functional separation in multisite

| Entity | Is separated | Notes |
| --- | --- | --- |
| Contacts | No | However, the multilevel 'multisite' extension adds ACLs that do provide segregation contact related entities- |
| Activities | No | The multisite concept only limits access to this data by ACLs - one implementation is the 'multisite' Multilevel Extension. |
| Address | No | The multisite concept only limits access to this data by ACLs - one implementation is the 'multisite' Multilevel module. |
| Phone | No | The multisite concept only limits access to this data by ACLs - one implementation is the 'multisite' Multilevel module. |
| Email | No | The multisite concept only limits access to this data by ACLs - one implementation is the 'multisite' Multilevel module. |
| Contribution | No | The multisite concept only limits access to this data by ACLs - one implementation is the 'multisite' Multilevel module. |
| Pledge | No | The multisite concept only limits access to this data by ACLs - one implementation is the 'multisite' Multilevel module. |
| Participants | No | The multisite concept only limits access to this data by ACLs - one implementation is the 'multisite' Multilevel module. |
| Case | No | The multisite concept only limits access to this data by ACLs - one implementation is the 'multisite' Multilevel module. |
| Relationship | No | The multisite concept only limits access to this data by ACLs - one implementation is the 'multisite' Multilevel module. |
| Personal Contribution Page | No | The multisite concept only limits access to this data by ACLs - one implementation is the 'multisite' Multilevel module. |
| Grant | Possibly | see notes with option value |
| Membership Type | Yes | **Options for Membership types** not owned by a given org appear on the membership tab of the contact summary screen. However the membership types in search are limited to the domain's organization. L2 site manager 'appears' have permission to change which site a membership type belongs to (although this fails per item above). |
| Membership | No | |
| Membership Status | No | It would be more generally useful for this to be by membership type than by domain per se |
| Payment Processor | Yes | |
| Contact type & subtype | No | |
| Campaign | No | Desirable |
| Contribution Type | No | (in multi-country models this might be desirable whereas national organisations are likely to think it a bad thing) |
| Contribution Page | No | Desirable |
| Contribution Premium | No | Desirable |
| Event | No | Desirable |
| Custom fields | No | It isn't but tabbed Custom Fields for contacts the display of them can be controlled through the multisite extension |
| Dashboard | Yes | |
| Dedupe rules | No | |
| Financial Account | No | |
| Group | Sort of | Group visibility is dictated by the multilevel module if installed. |
| Scheduled jobs | Yes | beware - your mails won't go out if you don't configure for all domains |
| Location Type | No | |
| Domain location | Yes | ie. street address etc for your organisation is per domain |
| Mailing | Yes | These are per domain. Before CRM-16981 (Civi 4.7), mailings go out with the correct permissions, but are visible to members of other domains. |
| Mail Settings | Yes | pop / smtp / from addresses are per site |
| Import & export mappings | No | Desirable |
| Menu & navigation | Yes | This is fairly problematic as, at least on the upgrade to 4.1, only the main site menu was upgraded |
| Message Templates | No | |
| Logos & headers | No | Desirable This isn't something currently storable in Civi & to add your logo / header to workflow templates you need to edit all the individual templates but to support multisite we need to look at storing logos & headers so a smarty token can signify them |
| Option groups & option values | Partially | The option value has a domain id. It doesn't seem to be heavily used - ie. I found mail approval, grant_types & from_email_address to be the only ones with domain ids. But this seems like it might be a good angle for events & others - eg. if the event_type_id is for that domain or has no domain then show on the page. |
| Price sets | Partially | The price sets themselves are but not the price fields & values - which makes the idea of having one price set which shows different fields on each site impossible. |
| Profiles | No | |
| Relationship Type | No | |
| Report Instances | Yes | |
| Smart groups | Partially | If multilevel permissioning is installed then permission to view groups in other parts of the hierarchy is restricted by ACLs |
| SMS Provider | Yes | |
| Settings | Yes | The CiviCRM settings table is domain specific |
| Status Preferences | Yes | CiviCRM 4.7+ |
| Survey | No | |
| Tag | No | |
| Users | Yes | Users are separately matched to civicrm contacts by domain |

<!-- Source: setup/multisite-part3.md -->
