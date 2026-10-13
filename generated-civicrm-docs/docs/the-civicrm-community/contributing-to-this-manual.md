---
title: Contributing to the CiviCRM user guide
category: how-to
topic: general
subtopic: user-guide-edits
component: CiviCRM user guide
audiences:
- newcomer
level: intermediate
journey_stage: manage-and-automate
summary: Learn how to propose a single edit or multiple edits to the CiviCRM user guide.
extensions: []
related: []
review_priority: low
review_notes:
- The file-system path given for editing “What is CiviCRM?” does not match the linked page path; the example needs verification.
- The multiple-changes instructions refer to GitLab, but the image captions refer to GitHub.
- The multiple-changes instructions say to click merge request in two consecutive steps; both steps are retained pending review.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: the-civicrm-community/contributing-to-this-manual.md
destination_path: the-civicrm-community/contributing-to-this-manual.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/the-civicrm-community/contributing-to-this-manual/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Contributing to the CiviCRM user guide

This page is a starting point for contributing to the CiviCRM user guide. More advanced documentation for contributing is in the [CiviCRM developer guide](https://docs.civicrm.org/dev/en/latest/documentation/).

## Style guide {:#style_guide}

When proposing changes, follow the [Documentation style guide](https://docs.civicrm.org/dev/en/master/best-practices/documentation-style-guide/).

## Contributing single changes {:#single_changes}

1. [Sign up for an civicrm.org-account](https://civicrm.org/user/register) (if you don't already have one) and [login at lab.civicrm.org](https://lab.civicrm.org/users/sign_in).
2. Find the page in the manual that you want to edit. For example, [Menu, Dashboard and Dashlets](../the-user-interface/menu-dashboard-and-dashlets.md).
3. Click the pencil icon next to the page title.

   ![Image of the pencil icon](../img/contributing_to_this_manual.png)

4. You will be taken to a GitLab editing screen at lab.civicrm.org. Make your changes, describe your changes in a descriptive commit message and *commit changes*.

This will create a merge request for your changes, which will be published as soon as they are reviewed by someone on our documentation team.

## Contributing multiple changes {:#multiple_changes}

1. [Sign up for an civicrm.org-account](https://civicrm.org/user/register) (if you don't already have one) and [login at lab.civicrm.org](https://lab.civicrm.org/users/sign_in).
2. Create a *Fork* with the fork button on the top right of the page.

   ![Fork icon from github.com](../img/fork.png)

3. In your [git client](https://git-scm.com/download/gui/linux) clone the CiviCRM user guide repository to your computer.
4. Locate the Markdown file (`.md`) in your file system that you want to edit by matching it to the file that that you want to change. For example, if you want to edit ["What is CiviCRM?"](../introduction/what-is-civicrm.md) you would find `<your_file_system>/docs/getting-prepared/is-civicrm-for-you.md`.
5. Make one or more related changes and commit them in your git client.
6. Push your changes from your git client to your fork.
7. In [GitLab](https://lab.civicrm.org) click *merge request* to create the new merge request.

   ![New PR in Github Interface](../img/new_pr.png)

8. Click **merge request**.
9. Leave a descriptive message and then click **Create merge request**.

Your PR will be reviewed by someone on the documentation team and published once they are approved.

## Additional resources {:#additional_resources}

Additional resources on how CiviCRM does documentation and Markdown can be found in the [developer docs](https://docs.civicrm.org/dev/en/latest/documentation/#resources).

## Versioning (which version should I edit?) {:#versioning}

All edits based on the current version of CiviCRM should be committed against the master branch. The [Developer guide](https://docs.civicrm.org/dev/en/latest/documentation/#versions) has more detailed information.

<!-- Source: the-civicrm-community/contributing-to-this-manual.md -->
