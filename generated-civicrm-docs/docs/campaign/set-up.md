---
title: Set up CiviCampaign
category: how-to
topic: campaigns
subtopic: configuration
component: CiviCampaign
audiences:
- communications-manager
- administrator
- operations-user
level: basic
journey_stage: plan-and-configure
summary: Enable CiviCampaign and configure campaign types, statuses, and the Engagement Index.
extensions: []
related: []
review_priority: medium
review_notes:
- The campaign type instructions refer to the order in which a new event type appears; it is unclear whether this means campaign
  type.
- The Engagement Index instructions do not explain how to enter or save an index number.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: campaign/set-up.md
destination_path: campaign/set-up.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/campaign/set-up/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Set up CiviCampaign

Set up CiviCampaign to track related activities, such as contributions, surveys, and mailings, that are part of a campaign or project.

## Enable CiviCampaign

1. Go to **Administer &gt; System Settings &gt; Components**.
2. Select **CiviCampaign** and click **Enable** then **Save**.

Once enabled, CiviCampaign appears as a new **Campaigns** menu item along the top of your CiviCRM screen.

## Add a new campaign type

CiviCampaign provides three default campaign types:

- Direct Mail
- Referral Program
- Constituent Engagement

You can add campaign types appropriate for your work and disable those that aren't.

1. Go to **Administer &gt; CiviCampaign &gt; Campaign Types**. This displays the existing campaign types:

   ![column headers are: label, value (unique number), description, order, reserved, enabled (yes or no)](../img/campaign_configuration_typeoptions_1.png)

2. Click **Add Campaign Type** and give the new type a label and, optionally, a description.
3. Optionally, change the default weight. This affects the order in which this new event type appears in drop-down menus; smallest numbers appear highest.
4. Click **Save**.

The campaign type will be available to assign the next time you add a campaign.

## Campaign status

Assign a status to a campaign to track internally which stage it is in. The default statuses are Planned, In Progress, Completed, and Cancelled.

1. Go to **Administer &gt; CiviCampaign &gt; Campaign Status**.
2. Click **Add Campaign Status** and give it a name and, optionally, a description.
3. Changing the weight is not necessary, but it affects the order in which the new status appears in drop-down menus.
4. Click **Save**. The new status will be available to assign to campaigns.

![overview of campaign statuses. Column headers are: label, value, description, order, reserved (yes or no), enabled (yes or no)](../img/campaign_configuration_statuses.png)

## Engagement index

CiviCampaign lets you track an individual's level of interest or engagement in a particular activity. The Engagement Index can be recorded for general activities or actions, such as Send an Email, Meeting, Phone Call, and Interview, as well as additional custom activities or actions you create. To find out more about recording an activity for an individual, see Contacts in the Organising Your Data section.

To configure the Engagement Index:

1. Go to **Administer &gt; CiviCampaign &gt; Engagement Index**.
2. Configure the engagement index as a number, e.g. 1 is a high level of engagement, and 5 is low level of engagement.

This information can supplement your outreach employees' or organizers' assessment of member engagement or interest in your organization.

![overview of engagement index options. Columns headers are: label, value, description, order, reserved (yes or no), enabled (yes or no). Each option can be edited, disabled, or deleted.](../img/campaign_configuration_engageoptions.png)

<!-- Source: campaign/set-up.md -->
