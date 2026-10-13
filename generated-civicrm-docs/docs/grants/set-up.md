---
title: Set up CiviGrant
category: how-to
topic: grants
subtopic: set-up
component: CiviGrant
audiences:
- operations-user
- administrator
level: basic
journey_stage: plan-and-configure
summary: Enable CiviGrant and configure grant types, statuses, and custom data.
extensions:
- CiviGrant
related: []
review_priority: low
review_notes:
- The phrase "At the moment" makes the limitation on custom data for grant types time-dependent; verify that it remains accurate.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: grants/set-up.md
destination_path: grants/set-up.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/grants/set-up/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Set up CiviGrant

First, enable the CiviGrant extension in **Administer &gt; System Settings &gt; Extensions**.

## Grant types

Set up grant types on the **Administer &gt; CiviGrant &gt; Grant types** screen. There isn't much to configure here apart from a title and description of the grant.

At the moment, you cannot add custom data to grant *types*, but you can add it to grants (see below).

## Grant statuses

The option list for **Grant status** is on the **Administer &gt; System Settings &gt; Option Groups** screen. Select **Options** on the right of the Grant status line to view existing options or create new statuses to match your grant giving workflow.

## Custom data for grants

To add custom data to grants:

1. Go to **Administer &gt; Customize Data and Screens &gt; Custom Fields**.
2. Click on **Add Set of Custom Fields**.
3. Set **Used For** to **Grant**.

Consider adding custom data fields to upload the original application form. These could be converted to a PDF before uploading to make it read-only and reasonably future compatible.

See [Creating Custom Fields](../organising-your-data/creating-custom-fields.md) for more information about setting up custom data.

<!-- Source: grants/set-up.md -->
