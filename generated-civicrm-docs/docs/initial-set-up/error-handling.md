---
title: Error handling
category: how-to
topic: troubleshooting
subtopic: fatal-errors
component: CiviCRM
audiences:
- operations-user
level: basic
journey_stage: plan-and-configure
summary: Configure custom fatal error handling and save the settings.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: initial-set-up/error-handling.md
destination_path: initial-set-up/error-handling.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/initial-set-up/error-handling/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Error handling

Administer » System Settings » Debugging and Error Handling

Debugging options are covered in the developer documentation.

## Fatal error settings

- **Fatal Error Template** - Enter the path and filename for a custom Smarty template if you want to define your own screen for displaying fatal errors.
- **Fatal Error Handler** - Enter the path and class for a custom PHP error-handling function if you want to override built-in CiviCRM error handling for your site.

Click **Save** to save your action or **Cancel** to cancel it.

If successful you will see the message "Your changes have been saved."

<!-- Source: initial-set-up/error-handling.md -->
