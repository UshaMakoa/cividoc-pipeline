---
title: Message token
category: how-to
topic: forms
subtopic: message-token
component: Form Builder
audiences:
- communications-manager
level: intermediate
journey_stage: manage-and-automate
summary: Create a token that lets CiviMail authors link to a form and populate it with the recipient’s contact data.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: the-user-interface/message-token.md
destination_path: the-user-interface/message-token.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/the-user-interface/message-token/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Message token

Create a token for the form in the “Expose” field. This token allows CiviMail authors to link to the form.

![Message Token](../img/the-user-interface/form-builder/fb-msg-token-01.png)

You need to set **Autofill** to **Current User** in the **Individual** tab. But you do not need to **&quot;accept Id from URL”**. If you do not need it, it is more secure not to **&quot;accept Id from URL&quot;**.

![Autofill Current User](../img/the-user-interface/form-builder/fb-msg-token-02.png)

In a message template, you can select the **Afform Token** with the name of your form. Two tokens are created: URL and Hyperlink.

![Afform Token](../img/the-user-interface/form-builder/fb-msg-token-03.png)

When the recipient clicks the link, they access the form with the contact’s data populated.

<!-- Source: the-user-interface/message-token.md -->
