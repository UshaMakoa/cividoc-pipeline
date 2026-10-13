---
title: Auto-file email conversations in CiviCRM
category: how-to
topic: mailings
subtopic: auto-filing
component: CiviCRM email-to-activity
audiences:
- communications-manager
- administrator
- operations-user
level: intermediate
journey_stage: manage-and-automate
summary: Use a designated email address to file conversations as activities and set permissions for editing inbound email
  activities.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: email/set-up-part4.md
destination_path: email/set-up-part4.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/email/set-up-part4/
civicrm_version:
- latest
last_modified: '2026-10-06'
---

# Auto-file email conversations in CiviCRM

It is possible to have emails sent to and from your regular email client automatically filed in CiviCRM. This is done by including a designated email address in the To, Cc, or Bcc field (Bcc is recommended, as it is invisible to the recipient.) Emails that include this designated email get filed as an activity for the contact(s) that match the other email addresses in the From, To, and Cc fields. If any of these email addresses are not already in the system, a new contact record will be created. (Technically, this can work for inbound emails as well; however, it does depend on the person sending the mail to you including the auto-filing address in the To, Cc, or Bcc field.)

For this, your administrator should have configured IMAP or other mail accounts and set them up in CiviMail (see **Email System Configuration**, especially **Adding an incoming email account for handling bounces or auto filing to CiviMail**, in **Initial Set-Up** for more details).

## Allow users to edit inbound e-mails

Activities created by CiviCRM as a result of email-to-activity processing are not editable by users, as there is a restriction enforced on the Inbound Email activity type. To allow users to be able to edit these activities, an administrator can enable the **CiviCRM: edit inbound email basic information** or the **CiviCRM: edit inbound email basic information and content** permissions for the roles that require it.

**CiviCRM: edit inbound email basic information** will allow users to edit every field of the activity, except the original message, stored in the activity's details.

**CiviCRM: edit inbound email basic information and content** will allow users to edit every field of the activity, including the original message's content.

<!-- Source: email/set-up-part4.md -->
