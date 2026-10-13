---
title: What you need to know
category: explanation
topic: campaigns
subtopic: planning-a-survey
component: CiviCampaign
audiences:
- communications-manager
- administrator
- membership-manager
level: basic
journey_stage: plan-and-configure
summary: Understand the concepts and decisions involved in planning a CiviCampaign survey.
extensions: []
related:
- ../organising-your-data/creating-custom-fields.md
- ../organising-your-data/profiles.md
review_priority: high
review_notes:
- The Drupal permissions link points to Drupal 7 documentation and may mislead readers using other versions.
- The membership satisfaction service example and the wording of the question about a standard set of responses are unclear;
  they have been left unchanged.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: survey/what-you-need-to-know.md
destination_path: survey/what-you-need-to-know.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/survey/what-you-need-to-know/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# What you need to know

The following concepts and questions will help you get the most out of the survey tool in CiviCampaign.

Surveys are part of the functionality of the CiviCampaign component, so you must have this enabled in order to use surveys; however, you can create surveys that are not connected to a specific campaign. For example, an organisation may wish to conduct a membership satisfaction service to assess the performance of their own service, without having it associated with a campaign.

## Key concepts

### Custom fields and profiles

CiviCampaign surveys use profiles to capture survey participants' responses. Once you've decided on your questions and the types of responses, you need to create custom fields for the questions and responses with option values if you're collecting multiple choice responses. You can then either create a new profile from the main profile screen or create a new profile when you are creating a survey. A profile is used to display the survey questions.

To learn more about how to create custom field sets, see [Creating Custom Fields](../organising-your-data/creating-custom-fields.md). To learn how to create a custom profile, see [Profiles](../organising-your-data/profiles.md).

### Reserving and releasing respondents

Before you can capture responses to your survey, you need to create a group made up of the contacts you are seeking responses from. This could be an existing group within your contacts, or you may need to create a group specifically for the survey. Survey describes this process as reserving respondents. When the contact has completed the survey and their data recorded, they are released from this group.

You can learn more about creating groups in the chapter *Groups and Tags* in the section *Organising Your Data*.

Surveys are designed to capture responses from existing contacts; if you are seeking responses from the wider public, use the Petition tool; see the Petitions section for information on this.

### Drupal permissions

If you are using Drupal, you need to set permissions to allow specific roles to Reserve Campaign Contacts and Release Campaign Contacts when conducting the surveys. To learn more about setting Drupal permissions, go to the Drupal documentation at [http://drupal.org/getting-started/7/admin/user/permissions](http://drupal.org/getting-started/7/admin/user/permissions).

## Key questions

- Is the survey part of a campaign? When creating a survey, you don't have to connect it to a specific campaign; a general survey may be used for any programme in your organisation. But if you are using surveys as a particular strategy within a campaign, connecting the survey to the campaign will enable you to analyse the survey along with other strategies and activities related to this campaign.
- Think about the specific questions and types of responses you want to gather. Do you want to standard set of responses to make it easier to analyse results to specific questions, e.g. Yes, No, Undecided, Declined? Or is an open-ended question more appropriate, to allow the individual to provide you with a narrative?
- How many questions do you need to ask? If it is more than one, you will need to create custom fields; if it is more than three, consider using Petition instead of Survey.
- Who will conduct the survey, and how will the data be entered into CiviCRM?
- What group of your constituents do you want to survey?

<!-- Source: survey/what-you-need-to-know.md -->
