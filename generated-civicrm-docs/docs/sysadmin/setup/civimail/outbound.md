---
title: Outbound email
category: how-to
topic: system-administration
subtopic: smtp-and-oauth
component: Outbound email
audiences:
- communications-manager
- technical
- administrator
level: intermediate
journey_stage: plan-and-configure
summary: Configure SMTP settings and the source-described OAuth setup for outbound email.
extensions:
- OAuth client (Core extension) extension
- OAuth Outgoing Mail Extension
related: []
review_priority: high
review_notes:
- The source contains an unresolved TODO about the ssl:// host-name requirement.
- The Google Mail Business Apps port example reports that port 25 worked after port 465 did not, but leaves the reason unresolved;
  this could mislead readers configuring SMTP.
- The CiviMail Mailer Settings heading was attached to the end of the final SMTP note in the source.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/civimail/outbound.md
destination_path: sysadmin/setup/civimail/outbound.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/civimail/outbound/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Outbound email

## SMTP

Outbound Email (SMTP) - SMTP server, port and authentication settings for outbound email.

SMTP Server - Enter the name of the SMTP server (machine) in the form: smtp.example.com

!!! note

    If you specify an SSL port in the next field, you must prepend an "ssl://" to the host name. TODO: This ought to get added to the CiviCRM book.

SMTP Port - The standard STMP port is 25. Only change this value if your SMTP server is running on a non-standard port and you know which port.

Authentication - Click Yes or No to indicate if your SMTP server requires authentication (user name + password).

SMTP Username - If your SMTP server requires authentication, enter your Username here AND the Password associated with that user in the next field.

!!! tip

    For most environments, the Username will be the **local-part** of a valid email account on your domain. This is the part that precedes the at-sign (@). EXAMPLE: if a valid email account on your domain is **admin@example.com** , enter **admin** as the Username.

SMTP Password - The password associated with the Username entered in the previous field.

!!! Joomla

    For Joomla! installs, you will need to update both the Admin and Front-end copies of civicrm.settings.php.

Click Save to save your action or Cancel to cancel it.

If successful you will see the message "Your changes have been saved."

!!! note

    We followed the port requirement directions on Google Mail Business Apps Page to use 465 BUT hours later we decided to try 25 and it worked. So for some odd reason we had to use a non-secure port.

    Note: Could this be because the ssl:// was left out of the host name field (see above)?

## Google or Microsoft Office 365

If you are using Microsoft Office 365 or Google you also need the OAuth client (Core extension) extension and the [OAuth Outgoing Mail Extension](https://civicrm.org/extensions/oauth-outgoing-mail)

You then need to setup an [OAuth provider](../oauth.md#register) and under **Administer** > **CiviMail** > **Site From Mail Address** you can add a From Mail Address with the configured OAuth provider.

<!-- Source: setup/civimail/outbound.md -->
