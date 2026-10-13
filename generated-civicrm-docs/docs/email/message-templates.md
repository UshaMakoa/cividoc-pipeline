---
title: Message templates
category: how-to
topic: mailings
subtopic: user-driven-templates
component: CiviCRM
audiences:
- operations-user
- communications-manager
- membership-manager
- administrator
level: intermediate
journey_stage: everyday-tasks
summary: Create and manage reusable message templates for emails and mass mailings.
extensions: []
related:
- ../common-workflows/tokens-and-mail-merge.md
review_priority: low
review_notes:
- The source uses Administer > Communications > Message Templates here but Administer > Communication > Message Templates
  for system workflow messages; the menu label may be inconsistent.
- The source says a list of available tokens follows, but no list is present.
- The source lists Preview among existing-template actions but does not describe it in the EXISTING section.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: email/message-templates.md
destination_path: email/message-templates.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/email/message-templates/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Message templates

## Overview

Message templates let you reuse entire emails or parts of emails in mass mailings and when using the Send Email activity.

CiviCRM has two categories of Message Templates:

- **User-driven Messages** are created by staff to communicate with constituents and be reused. Examples include thank-you letters and meeting announcements.
- **System Workflow Messages** are pre-configured messages used by CiviCRM features. Examples include contribution receipts and event registration confirmations.

## Creating user-driven templates

The easiest way to create a message template is to check **Save as New Template** on the message creation screen. This option is available when using the Send Email activity and when sending a mass mailing.

You can also create templates from scratch or edit existing templates at **Mailings > Message Templates** or **Administer > Communications > Message Templates**.

1. Click **Add Message Template**.
2. Enter a Message Title and a Message Subject. You can use [tokens](../common-workflows/tokens-and-mail-merge.md) to personalize the subject line.
3. Scroll down to the HTML Format section and create your template. Online resources that are not specific to CiviCRM offer instructions for creating HTML email templates. One approach is to find and copy an email template from a website that offers samples.
4. To paste HTML from an external template, write HTML directly, or modify HTML created in the WYSIWYG editor, switch to the code view using the toolbar icon called "Source". Its appearance and label vary depending on whether you use Drupal, Joomla, or WordPress.

Message templates are available even when CiviMail is disabled.

### Full HTML documents

Some HTML content pasted into a User-Driven template—for example, content copied from an email design tool or an older CiviCRM sample template—is a full HTML document. It has its own `<!DOCTYPE>`, `<html>`, `<head>` and `<body>` tags, rather than just the content that goes inside the body of an email.

If you switch such a template to the rich text (WYSIWYG) editor, only the content inside `<body>` is kept. The `<!DOCTYPE>`, `<html>` and `<head>` wrapper, and anything in it, is discarded. CiviCRM warns you before this happens.

In most cases, this is harmless: when CiviMail sends a User-Driven message, it combines a separate Header, the message itself, and a separate Footer into one email. The message template therefore only needed the inner content.

It is **not** harmless if something in the document’s `<head>` is required for how the email displays. A common example is a `<style>` block used to make the layout responsive on different screen sizes, such as one using a `<meta name="viewport">` tag and media queries. Switching a template like this to the rich text editor will silently drop the styling that makes it responsive. If you are unsure, keep editing in Raw HTML mode or check with whoever built the template.

### Tips for creating templates

HTML allowed in emails is more restricted than HTML used for web pages. For instance, it needs tables for layout and inline CSS, and must not include background images. These tips can help a template display well in mail clients:

- **Table border:** The HTML `<table>` element has an optional border attribute. Its default value is 0, so it does not appear unless you set it. Setting it to 1—for example, `<table border="1">`—makes table edges visible and can help identify layout problems. HTML email templates usually have multiple tables, including nested tables. Make changes one at a time and switch to the HTML view to see the results. A table usually has more than one parameter, so leave spaces between parameters.
- **Table cellpadding and cellspacing:** These table parameters can improve readability. Try different settings in different tables.
- **Width:** Do not send an email wider than 600 pixels, to ensure maximum compatibility across email clients. Keep the outermost table and any tables inside it within 600 pixels. Keep the total width of each image within 600 pixels too. An image’s horizontal padding parameter can increase its width beyond its width parameter.
- **Images:** Images need to be online and accessible. Edit each image to an appropriate width and height, then save it with as small a file size as possible. Free online resources can help you resize images if you do not have image-editing software or do not know how to use it.
- **HTML editor:** CiviCRM comes with two WYSIWYG editors, CKEditor and TinyMCE, and Textarea, a plain text editor. If another editor is configured as part of your Drupal, Joomla, or WordPress installation, you can use it instead. Go to **Administer > Customize Data and Screens > Display Preferences** and select a different WYSIWYG Editor.

### Plain text and HTML formats

All messages can be sent in either plain text or HTML. Today, the vast majority of people use email clients that can read HTML messages.

It is good practice to send a plain text version as well as an HTML version so that all recipients can view the message. There are two ways to do this:

1. **Recommended:** Leave the text version fully blank. During sending, a text version will be generated from the HTML version.
2. Enter a text version in the text box on the message template screen. You will need to keep it up to date manually. This takes time, and if the text version is not maintained, people using plain text-only email clients may receive an incorrect or incomplete message. This may include visually impaired people whose email-reading software prefers the text version.

To create a plain text version manually from HTML:

1. Copy and paste the text from the HTML Format field into the Plain Text Format field. Do this from the WYSIWYG view, not the Source view: you need the text, not the code. The plain text field automatically strips formatting and other elements that do not work in plain text.
2. Copy the URLs of all links to the appropriate places in the Plain Text Format field.
3. If the HTML version contains tables, modify the text layout manually to make it readable.

## Configure message templates

To configure message templates, begin at the **Administer CiviCRM** page. In the **Communications** section, choose **Message Templates**.

You will see a list of existing templates. If none exist, you will see:

> There are no Message Templates entered. You can add one.

Click **add one** to create a template.

You can create NEW message templates or use the links to the right of each existing template to **Edit**, **Preview**, **Disable** or **Delete** it.

### NEW

To create a NEW message template, choose **>>New Message Template**. You will be taken to the New Message Template page.

Create a **Message Title**. This title organizes your messages and will not appear in the email.

!!! tip "Tokens"
    The next three fields can all use [tokens](../common-workflows/tokens-and-mail-merge.md) to personalize messages with names, dates, amounts of gifts and other details.

Here is a list of the tokens you can use

Create the **Message Subject** for your email. Use tokens if desired.

Create your **HTML Message**. Include tokens to personalize your messages.

Leave **Text Message** blank unless you have a strong reason not to.

Choose **Enabled?** to enable the message template for use.

Click **Save** to save the template or **Cancel** to cancel.

If successful, you will see:

> "The Message Template "Membership Renewal Initial Message" has been saved."

### EXISTING

For EXISTING templates, you can **Edit**, **Disable** or **Delete** each template using the links to its right.

### EDIT

Select **Edit** to open the Edit Template page, where you can change each option. You can also enable or disable the template by checking or unchecking **Enabled?** at the bottom of the page. Click **Save** to save the template.

If successful, you will see:

> The Message Template "Membership Renewal Initial Message" has been saved.

### DISABLE

Select **Disable** to temporarily disable an Existing Template. You will see:

> "Are you sure you want to disable this Message Template? "

Click **OK** to continue or **Cancel** to cancel. To re-enable the template, click **Enable**.

### DELETE

Select **Delete** to delete the template. You will see:

> Do you want to delete this message template?

Click **Delete** to continue or **Cancel** to cancel the deletion.

<!-- Source: email/message-templates.md -->
