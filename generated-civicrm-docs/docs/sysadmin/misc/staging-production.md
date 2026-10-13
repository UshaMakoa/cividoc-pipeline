---
title: Moving a CiviCRM instance from production to staging
category: how-to
topic: system-administration
subtopic: moving-to-non-production
component: CiviCRM
audiences:
- technical
- administrator
- communications-manager
- fundraising-manager
level: intermediate
journey_stage: plan-and-configure
summary: Set the environment when copying a production CiviCRM instance to a non-production site and understand the resulting
  changes.
extensions: []
related: []
review_priority: medium
review_notes:
- The description of support added in CiviCRM 4.7.25+ is version-specific.
- The phrase “when the in a non-production Environment” is unclear in the source and has been left unchanged.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: misc/staging-production.md
destination_path: sysadmin/misc/staging-production.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/misc/staging-production/
civicrm_version:
- 4.7.2
- 4.7.25
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Moving a CiviCRM instance from production to staging

Many websites have production and staging/development/test instances. When copying a CiviCRM instance from production to non-production, a number of changes should be made to prevent undesirable effects from having two or more copies of the site running.

For example, each instance will attempt to send emails for scheduled reminders and scheduled and in-process bulk mailings from CiviMail. Other possibilities include posting recurring transactions to certain payment processors for recurring contributions, sending text messages, and custom synchronizations with external systems.

The following explains support added in CiviCRM 4.7.25+ to better support disabling production activities when moving a CiviCRM instance from production to non-production.

## Changing your environment

By default, 'Environment' is Production. Other option values can be defined, with 'Staging' and 'Development' defined by default.

To change a site instance from production to non-production mode—for example, when migrating a site from production to a staging, test, or development instance—navigate to the debugging page via **Administer > System Settings > Debugging and Error Handling**.

You can also set the Environment in `civicrm.settings.php`. Newer installs of CiviCRM have `global $civicrm_setting` at the top of the file and `$civicrm_setting['domain']['environment'] = 'Production';` commented out. If you have upgraded from an older version of CiviCRM, you can add these manually to `civicrm.settings.php`.

## Effects of changing your environment

- If you have set your Environment to Development or Staging via the UI, outbound email will be set to “Disable Outbound Email”. Logging of mails will not be done until the user explicitly sets the value in `civicrm.settings.php` and changes the outbound setting to `mail()`. **NOTE:** This does NOT happen if you have set your Environment via `civicrm.settings.php`.
- If one wishes to run a specific scheduled job when the in a non-production Environment, add `runInNonProductionEnvironment=TRUE` to that job's parameters.
- Additional changes may be added by extensions that are Environment-aware—for instance, disabling recurring payments.

<!-- Source: misc/staging-production.md -->
