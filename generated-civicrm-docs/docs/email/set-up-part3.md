---
title: Configure automated messages, headers, and footers
category: how-to
topic: mailings
subtopic: mailing-messages-and-templates
component: CiviMail
audiences:
- communications-manager
level: intermediate
journey_stage: plan-and-configure
summary: Edit automated messages, create mailing headers and footers, and test templates.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: email/set-up-part3.md
destination_path: email/set-up-part3.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/email/set-up-part3/
civicrm_version:
- latest
last_modified: '2026-10-06'
---

# Configure automated messages, headers, and footers

## Automated messages and mailing list management

CiviCRM sends emails automatically when your participants take certain actions:

- When someone signs up for a mailing list, they get a confirmation email with a link that they must click.
- When they confirm, they get a welcome email.
- When they unsubscribe, opt-out of all emails from your domain, or resubscribe to a list they have previously unsubscribed from, they get a confirmation email that does not require any action.
- When they reply to a message you have sent through CiviMail, you can set up an autoresponse to their reply.

In CiviCRM, these are called Automated Messages, and you can edit them and add new ones at **Mailings > Headers, Footers, and Automated Messages**.

For more information on email list management see [Maintaining healthy email lists](maintaining-healthy-email-lists.md) which explores how CiviCRM handles unsubscribes, bounces and email holds.

## Create headers and footers

Headers and footers can be used only in mass mailings using CiviMail. They are not available unless CiviMail is enabled.

The header is the area at the top of the email; it should include elements that you want to be displayed before the main content body, such as the logo of your organization and the title of the newsletter.

The footer is always the last thing in the email. The footer is an ideal place for the compulsory [unsubscribe tokens](../common-workflows/tokens-and-mail-merge.md#opt-out).

You can manage the content of headers and footers in **Mailings > Headers, Footers, and Automated Messages**. You can create different headers and footers for different purposes; for example, you might want to create a set of headers with different images and titles that can be used for different campaigns or programs. It is recommended to style them similarly, to present a coherent visual identity across all your messages.

After headers and footers are configured, staff who prepare a new mailing will be able to select them from available headers and footers. This helps staff create more standardized mailings with elements that help your readers identify the contents of the mailing or find information.

Like the Message Templates, headers and footers have both a text and an HTML version. Unlike Message Templates, however, the header and footer creation pages do not offer a WYSIWYG editor. You will need to write header and footer HTML directly or use another HTML editor to produce the HTML code.

## Test templates

Once your templates are ready, we strongly recommend that you test them in various email clients, such as Mozilla Thunderbird, MS Outlook, Mac Mail and web-based e-mail such as Gmail, Yahoo and Hotmail. An easy way to do this is to create a group that includes a test contact for each of those destinations and use it each time you create a new mailing.

Because email clients can display the HTML very differently from each other, we recommend that you keep the HTML as simple as possible and use only inline CSS or tables for formatting. Include as much of the layout as possible in the templates so that each new mailing will not require too much reviewing, since the template will have already been tested.

<!-- Source: email/set-up-part3.md -->
