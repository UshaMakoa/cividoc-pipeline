---
title: Multilevel permissioning in multisite
category: explanation
topic: system-administration
subtopic: contact-access
component: CiviCRM multisite
audiences:
- administrator
- operations-user
level: advanced
journey_stage: plan-and-configure
summary: Understand how domain groups and associated groups affect contact visibility, and how permissioned relationships
  provide an alternative.
extensions:
- multisite
- Permissioned Relationship
related:
- https://lab.civicrm.org/extensions/multisite
- https://civicrm.org/extensions/relationship-permissions-acls
review_priority: low
review_notes:
- The passage about Branch site 2 refers to “extra drupal permissioning,” but does not explain which permission it means.
- The page says access to contact details is not separated by charity; this limitation is important to verify before relying
  on the permissioning model.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/multisite-part2.md
destination_path: sysadmin/setup/multisite-part2.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/multisite-part2/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# Multilevel permissioning in multisite

## Multilevel permissioning behaviour

This permissioning is delivered by the [multisite extension](https://lab.civicrm.org/extensions/multisite). The extension also helps manage a shared user table (even if you turn permissioning off by setting domain group to 0).

Multilevel permissioning lends itself very well to a head office branch or chapter organisation as the functionality is hierarchical. The users of the Head Office site can see all the users from all the sub-sites. Users logged into Branch site 1 cannot see users from Branch site 2 unless they have 'view all contacts', 'edit all contacts' or 'administer multisite' permissions. Likewise users logged into branch 2 cannot see Branch 1 users unless they have the extra drupal permissioning. The Head Office users can see both.

The mechanism behind it is groups. Each domain has a domain group (with the likely exception of the top level domain). This group has 'associated groups'. The associated groups are either child groups or groups that share the same group organisation. The preferred method is to share a group organisation as there are less performance costs and there is less potential for confusion. A good use-case for a child group is when you want to add another level to your multisite set up. These level 3 sites will be members of their parent site in a hierarchical organisation.

You should avoid setting up smart groups as child groups. Permissions are only based on 'hard-add's to the group. When a person views a smart group that is an associated group they will see the interesection of that group & contacts that have been hard-added to the parent group or an associated group. However, the site will still incur the performance cost of calculating the whole smart group. In addition, if it is a child group the site will incur the performance cost of storing all the contacts of the child group against the parent group. If a user with 'view all contacts' permission views the site group they will see all the contacts of site group and all child groups INCLUDING smart groups - so what they see when they look at this site group will NOT reflect the contacts that are visible from that site. There may be situations where this makes sense - but in general it increases confusion.

It is possible for a group to be a child of more than one group in which case it will be considered to be in both those groups and can be seen from the site of both those groups.

If the multilevel permissioning module is enabled:

* Contacts with 'view all contacts', 'edit all contacts' will continue to see all contacts
* Other contacts with the 'civicrm view all contacts in domain' permission will be able to see all the contacts in the site group they are logged onto, and contacts hard-added to it's child groups and groups linked by group organisations (associated groups).
* If child groups are smart groups then ACL-restricted users will not see smart group members who are not hard-added to the parent or associated groups. It is not recommended to put smart groups as child groups per above
* The silo-ing of data is at the contact level. It is similar to what can be achieve using CiviCRM ACLS.
* If you have access to view a user then you can see all details including contributions, activities.
* If someone is in more than one site group they will be visible from both sites
* Contacts can only see the groups which are children of their site group unless they have 'administer multiple organizations' permission
* ACL permissions to give users access to view a group from another site do not over-ride the limitations of the multisite. If they have permission to view the treasurers group but it is not part of their site they cannot view members in it .

The multisite functionality is limited from the perspective of providing services to multiple organisations that are not closely linked. Take for a site providing fund raising services for multiple charities (ideally with a single sign-on for a giver). Each charity would want to see the contributions person A gave them and not the contributions that person gave to another charity. At this stage this isn't supported. A number of sensitive bits of data such as activities are not site specific.

## Permissioned relationships for multilevel ACLs

A lighter-weight solution is to use the [Permissioned Relationship extension](https://civicrm.org/extensions/relationship-permissions-acls). This can be used to limit a user to only those contacts that they have a Permissioned Relationship to, or that those contacts in turn have a Permissioned Relationship to, etc. In other words you can daisy-chain these relationships to create multi-level access controls.

Example: User A - has a Permissioned Relationship to Organisation A - and can therefore 'see' Org A, and if Org A has Permissioned Relationship over eg Org B and Org C, and if those Orgs have Permissioned Relationships over eg Persons B1 and B2, and Persons C1 and C2, then User A can access Orgs A, B and C, and Persons B1, B2, C1 and C2. And this can go further down multiple layers.

This deploys very well without the wiring involved in multisite and hence is more approachable for 'beginners' (and for advanced folk who need a lighter weight solution).

Beauty of this solution is that it can scale really easily. And for Drupal sites, together with Webforms and Views can let delegates of Orgs manage their contacts without actually ever needing to set foot on the CiviCRM side.

<!-- Source: setup/multisite-part2.md -->
