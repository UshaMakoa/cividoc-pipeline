---
title: Handle bounced mail
category: how-to
topic: system-administration
subtopic: bounce-handling
component: CiviMail
audiences:
- communications-manager
- operations-user
- administrator
- technical
level: intermediate
journey_stage: manage-and-automate
summary: Set up bounce handling and find or remove on-hold email addresses.
extensions: []
related: []
review_priority: low
review_notes:
- The Google Suite instructions quote a filter label as "Never end it to Spam"; this may make the filter difficult to configure
  and needs verification.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/civimail/inbound.md
destination_path: sysadmin/setup/civimail/inbound.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/civimail/inbound/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Handle bounced mail

## How bounce handling works

When an e-mail message "bounces", that means the recipient e-mail address is temporarily or permanently undeliverable, or the receiving e-mail server has refused the message.

When a mail server cannot deliver an e-mail, it returns the message to an address specified in the mail headers. CiviCRM adds a return address to every mailing message. The address contains a unique id for that message, such as 'id.1234@domain.org'.

CiviCRM also supports VERP, variable envelope return path. As an option, VERP-handling can add a local part to the return address, giving an address such as 'bounce+id.234@domain.org'. Either way, every message has a unique return address so that it can be identified.

You need a real, working mail account for returned messages. A name such as 'bounce@domain.org' or 'returned@domain.org' would be appropriate. If the mail service for this account features VERP-handling, you should use it. In that case, name the account 'bounce@domain.org'; VERP handling will deliver messages addressed to 'bounce+<anything>@domain.org' to that account.

If VERP-handling is unavailable, your only option is a catch-all address. This sends messages to unknown addresses in the domain, such as 'id.1234@domain.org', to one designated mailbox. A catch-all is necessary because each message has a unique return address. It also receives spam sent to random addresses in the domain.

The bounce discovery job regularly logs into the mail account and processes messages that have arrived. It can trace a returned message to a particular message sent to a specific contact and record that message as bounced. You can then report bounce statistics for a mailing and identify problematic contacts.

To get this working, you need to:

- Get a bounce email account and enable VERP or catch-all for it.
- Configure a mail account for bounce handling in CiviCRM Mail Accounts.
- Configure mailings to use VERP or not.

## Find "On Hold" contacts

Use either search:

- From **Search > Advanced Search**, choose **Email On Hold** from the Basic Criteria section at the top.
- Use **Search > Search Builder**. Then choose **Contacts, On Hold, Primary, =, Yes**.

## Causes of e-mail address bounces

When the recipient's email server responds with a "bounce" email, it could be for a variety of reasons. The CiviCRM mail processing script attempts to determine the cause by parsing the bounce email returned by the receipient's email server. Based on the nature of the bounce and the number of times a bounce has occurred when attempting to send to that email, a Contact's email may be placed **on hold.**

The following list from the database shows the different types of bounces and how many times each must occur before CiviCRM deems **on hold** appropriate.

| id | name | description | `hold_threshold` |
| -- | -- | -- | -- |
| 1 | AOL | AOL Terms of Service complaint | 1 |
| 2 | Away | Recipient is on vacation | 30 |
| 3 | DNS | Unable to resolve recipient domain | 3 |
| 4 | Host | Unable to deliver to destination mail server | 3 |
| 5 | Inactive | User account is no longer active | 1 |
| 6 | Invalid | Email address is not valid | 1 |
| 7 | Loop | Mail routing error | 3 |
| 8 | Quota | User inbox is full | 3 |
| 9 | Relay | Unable to reach destination mail server | 3 |
| 10 | Spam | Message caught by a content filter | 1 |
| 11 | Syntax | Error in SMTP transaction | 3 |

## Remove hold

You can remove **on hold** in any of these ways:

- After running a Search, choose from Actions: **Email - unhold addresses**.
- To remove **on hold** from a single contact, manually edit that contact.
- To search for Contacts with **on hold** status and/or remove hold status in a batch, execute SQL queries. Hold status is recorded in the `civicrm_email` table in the `on_hold` column. The most basic batch query is:

```sql
UPDATE civicrm_email SET on_hold = 0;
```

!!! warning "Warnings"
    * Backup your database before running any direct queries.
    * This query will remove all "ON HOLD" status from email addresses, whether the email should be on hold or NOT!

A more nuanced query might be:

```sql
UPDATE civicrm_email ce
LEFT JOIN civicrm_group_contact gc ON ( gc.contact_id = ce.contact_id AND gc.status = 'Added' )
INNER JOIN civicrm_group gr ON ( gr.id = gc.group_id )
SET ce.on_hold = 0
WHERE gr.name = 'give your contact group name';
```

## Use a Google Suite account for the return address

1. To prevent bounce emails from being classified as spam, [create a filter](https://support.google.com/mail/answer/6579?hl=en) in the settings of your bounce gmail account. An easy way to avoid messages being sent to spam is to set the **Doesn't Have** value to a word that would never be in an email (you can hit random keys on your keyboard), and tick the box labeled "Never end it to Spam".
2. Google requires you use OAuth to access an email account via a third-party application. [Detailed instructions for setup](https://civicrm.stackexchange.com/a/38846/12) are available on Stack Exchange.

<!-- Source: setup/civimail/inbound.md -->
