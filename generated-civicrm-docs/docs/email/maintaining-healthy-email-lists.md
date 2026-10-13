---
title: Maintaining healthy email lists
category: explanation
topic: mailings
subtopic: bounces-and-email-preferences
component: CiviMail
audiences:
- communications-manager
- operations-user
level: basic
journey_stage: manage-and-automate
summary: Understand email bounces and the differences between held addresses, unsubscribes, opt-outs, and the Do not email
  option.
extensions: []
related: []
review_priority: low
review_notes:
- The page says a bounced email never reached its recipient but also lists an automatic away reply as a reason for a bounce.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: email/maintaining-healthy-email-lists.md
destination_path: email/maintaining-healthy-email-lists.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/email/maintaining-healthy-email-lists/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Maintaining healthy email lists

After setting up and configuring Email lists, you need to manage them and consider compliance. Healthy lists have low rates of bounced emails and unsubscribes.

A high bounce rate may raise concerns about being blacklisted or receiving a complaint from your SMTP provider. High bounce and unsubscribe rates typically point to a deeper organization issue.

## Understanding email bounces

Each time you send a bulk email from CiviMail, some emails may bounce. Some bounces are temporary; others are permanent.

### Why do emails bounce?

A bounced email did not reach its recipient. Reasons include:

- The email address was input incorrectly.
- The email address is out of commission.
- The inbox is full and temporarily cannot accept more messages.
- The recipient has an automatic away reply because they are on vacation and out of the office.

CiviCRM handles bounce types differently. Temporary bounces do not affect a contact record, and CiviCRM will attempt to send future mailings to the address. Permanent bounces may put a contact email on **Hold**. No future emails will be sent to an address on **Hold** unless someone fixes it and removes the hold.

The [System Administrator Guide's Inbound email chapter](https://docs.civicrm.org/sysadmin/en/latest/setup/civimail/inbound/#why-is-a-contacts-e-mail-address-put-on-hold) has a detailed table of bounce types and the number of bounces allowed before an address is put on hold.

### On-hold emails and unsubscribes

An email address on hold is different from an unsubscribe. Someone unsubscribes by clicking “unsubscribe from this mailing” in an email. The link is created by either of these [tokens](../common-workflows/tokens-and-mail-merge.md): `{action.unsubscribe}` or `{action.unsubscribeUrl}`.

Recipients who unsubscribe from a single mailing list are removed from the group used as that mailing list.

### Opting out and unsubscribing

Recipients can opt out of all bulk emails by clicking a link you provide in every mass email. You can still send individual or small volume emails to someone who has opted out using **Send Email** from the contact's record or after a search. Scheduled reminders will also still be sent to contacts who have opted out. Be careful about the emails you send to someone who has opted out if you do not want to be accused of sending spam.

The opt-out link is created by either of these [tokens](../common-workflows/tokens-and-mail-merge.md): `{action.optOut}` or `{action.optOutUrl}`. You can include these tokens in the body of your mailing or in a footer message.

### The Do not email privacy option

If a contact has **Do not email** selected, you cannot send them individual or small volume emails using **Send Email** from their record or after a search. They will not receive bulk emails sent through CiviMail. They will still receive scheduled reminders unless you specifically exclude them from those reminders.

If **Do not email** was set manually after the person contacted you in person, it is probably a good idea to exclude them from scheduled reminders. The *Schedule Reminders* chapter outlines how to do that.

### Making sure a contact receives no emails

Someone could change CiviCRM settings incorrectly or manually misuse an email address. The only way to fully guarantee that a contact receives no emails is to remove all email addresses from their record. In that case, the contact would not be able to log in to your website.

<!-- Source: email/maintaining-healthy-email-lists.md -->
