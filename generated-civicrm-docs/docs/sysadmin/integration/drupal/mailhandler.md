---
title: Archive CiviMail emails with Drupal Mailhandler
category: how-to
topic: system-administration
subtopic: drupal-mailhandler
component: CiviMail
audiences:
- communications-manager
- technical
level: intermediate
journey_stage: manage-and-automate
summary: Archive emails sent through CiviMail as Drupal nodes.
extensions: []
related: []
review_priority: high
review_notes:
- The instruction to "check this box" does not identify a box, so readers may be unable to complete that step.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: integration/drupal/mailhandler.md
destination_path: sysadmin/integration/drupal/mailhandler.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/integration/drupal/mailhandler/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Archive CiviMail emails with Drupal Mailhandler

Follow these steps to archive emails that you send via CiviMail.

1. Install the [mailhandler module](http://drupal.org/project/mailhandler).
2. Set up an email on your server, for example `newsletter@example.com`.
3. Make a content type in Drupal called "Newsletter Archives".
    1. Follow the mailhandler module on how to do this so that emails are posted as nodes to this content type.
4. Setup mailhandler to check this box per its instructions.
5. Make a Group in CiviCRM, for example called "Newsletter2Archive".
6. Make _one_ member in this group with the email address you created for your server above.
7. When you send an email and choose this group from the recipient list, the email goes there, is taken in by the mailhandler, and is added to the Drupal node database.
8. Make a view of ALL nodes of this content type and display them at url newsletter_archives.

You now have an HTML archive of emails in Drupal from CiviMail.

<!-- Source: integration/drupal/mailhandler.md -->
