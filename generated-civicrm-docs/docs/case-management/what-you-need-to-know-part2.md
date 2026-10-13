---
title: Relationship type status warnings
category: reference
topic: cases
subtopic: relationship-type-status-warnings
component: CiviCase
audiences:
- operations-user
level: intermediate
journey_stage: reference-and-troubleshooting
summary: Identify situations that can cause CiviCase status warnings related to Relationship Types.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: case-management/what-you-need-to-know-part2.md
destination_path: case-management/what-you-need-to-know-part2.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/case-management/what-you-need-to-know-part2/
civicrm_version:
- latest
last_modified: '2026-10-06'
---

# Relationship type status warnings

CiviCase may, in unusual situations, cause some status warnings related to Relationship Types. Some general principles applicable to all of these warnings are:

- If you haven't created any relationships yet between contacts you can delete the relationship type and recreate it.
- If you have created relationships between contacts, but not many, you may consider deleting those relationships, then deleting the relationship type, recreating the type, and then recreating the relationships between the contacts.

## Relationship type internal name duplicates

This situation can come up if you get confused about A/B directions when setting up relationship types, which is quite easy if you're new to it. For example:

1. Create a type called "Candy maker is" (A to B) / "Candy maker for" (B to A).
1. Thinking that you need to create another type to have both directions appear properly, create another type called "Candy maker for" (A to B) / "Candy maker is" (B to A).
1. Realize that you don't need that, so rename the second to something else you were planning to add, such as "Gum maker is"/"Gum maker for".
1. This will cause problems when assigning roles of type Gum maker.

## Relationship type display label duplicates

Somehow you have two different relationship types with the same display label. The simplest solution is to change the label for one of them or delete the duplicate. If they really are the same relationship it's a bad idea to have two anyway.

## Relationship type cross-duplication

This situation can come up if you change your mind several times when setting up relationship types and you make those changes in a specific order. For example:

1. Create a type called "Candy maker".
1. Create a type called "Gum maker".
1. Create a type called "Sweets maker".
1. Later, decide you don't need Gum so delete Gum.
1. Later still, decide you don't need both Candy and Sweets but you wanted Gum, so you rename Sweets to Gum.
1. Then you decide you like the word Sweets better than Candy so you rename Candy to Sweets.
1. At this point the system will get confused about what means what.

## Relationship type ambiguity

This situation can come up if you do something like create a new Relationship Type that is bidirectional, like "Spouse of", and then change your mind and edit it so that direction matters. The system will still function but you may find some relationships of that type appear backwards.

The reverse is also possible, where you initially created it as unidirectional and then later edited it so that it's bidirectional.

## Missing roles

One way this situation can come up is if you are using external XML files and you have made a typo in the file so that the relationship type doesn't match any existing type. Another way is if you deleted a relationship type referenced in the file but have not updated the file, so it still references it.

<!-- Source: case-management/what-you-need-to-know-part2.md -->
