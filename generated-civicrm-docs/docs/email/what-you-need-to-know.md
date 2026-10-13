---
title: What you need to know
category: explanation
topic: mailings
subtopic: planning-and-choosing-email-methods
component: CiviCRM email
audiences:
- communications-manager
- operations-user
- administrator
- event-manager
level: basic
journey_stage: overview
summary: Understand CiviCRM's email options and the questions to consider before sending email.
extensions: []
related: []
review_priority: medium
review_notes:
- The Send Email limit is described as a maximum of 50 addresses, but later guidance says to use CiviMail for 50 or more contacts.
  The threshold needs clarification; both statements have been left unchanged.
- The privacy example contains unclear quotation and emphasis markup.
- The email design guidance says "response web design"; the intended wording is unclear.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: email/what-you-need-to-know.md
destination_path: email/what-you-need-to-know.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/email/what-you-need-to-know/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# What you need to know

This page outlines key concepts and questions for planning your use of CiviCRM's email capabilities. Read it before you start sending emails to contacts. Detailed information on carrying out the activities mentioned here is in the **Everyday Tasks** section.

## Key concepts

Email plays a central role in CiviCRM. Broadly speaking, email is sent from CiviCRM in three situations:

- To individuals and small groups via the Send Email action.
- To a large group as a mass mailing via CiviMail.
- To individuals who trigger an email through a workflow in another component, such as an event registration confirmation email.

An advantage of sending email through CiviCRM, rather than through an email client or a bulk email tool other than CiviMail, is that every email sent via the Send Email action or CiviMail is treated as an activity and stored in each recipient's activity history. For example, you can see that John Doe made a donation three days after receiving your April newsletter, or that your volunteer coordinator emailed Jane Smith to ask her to staff the information table at an upcoming event.

### Send Email versus CiviMail

CiviCRM offers two options for sending email to contacts:

- **Send Email** sends an email as an activity for a contact. It is suitable for individuals and small groups.
- **CiviMail** sends a mailing to a group. It is suited to mass mailings or scheduled emails to small groups.

To send mass emails, first [set up CiviMail](set-up.md). The Send Email action is available even when the CiviMail component is disabled.

The options have important differences:

- Emails sent via the Send Email action are limited to a maximum of 50 email addresses. There is no reporting other than an activity record for each recipient.
- CiviMail emails have bounce processing and reporting.
- CiviMail allows recipients to manage their own subscriptions.
- CiviMail can be configured to automatically track replies.

CiviMail requires more work to configure and involves more steps, but enabling and configuring it provides additional mass email capabilities. Which method to use for a particular email might not be immediately apparent. Over time, you can establish and share practices among your users.

#### When to use the Send Email action

As long as you are contacting fewer than 50 recipients and do not need to track whether they opened the email or clicked any links, the Send Email action is quicker and easier than sending a mass mailing in CiviMail.

The Send Email activity offers the functionality of sending through an email client: you can attach files, CC and BCC contacts, and use message templates.

CiviCRM records only the messages you send. Recipients' replies come to your email address and are not recorded in the database. For this reason, do not rely on the Send Email action for extended email exchanges. To record an email exchange, you could create an activity called Email Exchange and copy and paste the conversation into its body, as you would for a record of a telephone call.

You can also record emails sent through your email client using the autofiling outbound email option described below.

#### When to use CiviMail

If you want to send mail to 50 or more contacts at once, you must use CiviMail.

Use CiviMail when you want statistics about the success of a mailing, including bounce statistics and click-throughs. For more information, see the *Reports and analysis* chapter.

CiviMail also enables people to sign up for your mailing lists on your website and automatically tracks their unsubscription or opt-out requests. It can file emails that recipients send as replies to a mailing and send an autoresponse to those replies.

### Choosing recipients

Send Email lets you choose recipients from a contact record or from search results.

CiviMail lets you choose recipients from search results or from Groups marked as Mailing Lists, which must be created before you set up the mailing. There is a complication with search results: all mail sent from CiviMail must have an unsubscribe link. If recipients are in a Group, an unsubscribe request removes them from that Group's mailing list. If they are not in a Group, they must be added to one when they unsubscribe so CiviCRM can record the request.

### Personalisation with tokens

Emails sent with both Send Email and CiviMail can include personalised text, such as a person's name. This uses [tokens](../common-workflows/tokens-and-mail-merge.md): placeholders that CiviCRM replaces with an appropriate value when sending each message. Some tokens available in CiviMail are not available in the Send Email activity.

### From email addresses

Both mass and regular email can be sent from your personal address, a general email address associated with your organisation, or another person's address. For example, an assistant can send official email messages under the name of his manager.

### Headers and footers

In mass mailings only, you can include customised headers and footers. Configure them under **Administer &gt; CiviMail &gt; Headers, Footers, and Automated Messages**.

### Templates

Templates for entire emails or parts of emails, such as headers and footers, let you reuse content. You can create email templates beforehand or when you send an email, and edit them at any time.

### Reporting

CiviMail can track mass mailings, helping you understand recipients' interests and gauge the effectiveness of your communications. You can track how many recipients opened an email and which links were popular.

#### Mailing list sign-up and unsubscribing

CiviCRM lets you publish a sign-up page or form, called a profile, where people can join your mailing list on your website. It requires that you allow recipients to unsubscribe from any mailing list *and* opt out of ever getting email from you. CiviCRM automatically tracks these requests. For more information, see the *Set-Up* chapter.

### Autofiling external emails in CiviCRM

CiviCRM lets you automatically record email sent through your email client in contact records. Set up a special email address and include it in the BCC field of an email you send. The database reads the email and converts it into an activity, filed in the record of the contact whose email address matches. If that email address does not exist in your database, a new contact record is created. See the *Email System Configuration* chapter of the *Intial set up* section for details.

## Other considerations

### Key questions

When planning your use of CiviCRM's email capabilities, consider:

- Are there types of emails you send repeatedly and want to create templates for?
- Is there content you want in the header or footer of every mailing?
- Do you want a web page where people can sign up for your emails?
- Which emails are important to store in recipients' contact records?

When planning a specific email, consider:

- How many people are you sending it to?
- Do you want to know who opens it and clicks its links?
- Have you created a list—a Group or Smart Group—to send it to?
- Do you want recipients to be able to view the mailing in a browser window if they have trouble viewing it from their email browser?
- Who should be the sender: a generic organisation address or an address personalised with someone's name?

### Interaction with other tools

Many CiviCRM components interact with email functionality and CiviMail, for example, to send confirmation, thank-you, and receipt emails. The sections of this book about each component include information about customising these emails. Read them alongside this section to understand email in the broader context of CiviCRM.

### Privacy issues

Consider privacy issues when planning email. Different countries have different laws relating to email privacy, including opt out/unsubscribe options. CiviMail's tracking tools may also raise issues; for instance, you may wish to avoid tracking who has clicked on the &quot;how to deal with drug issues*&quot;* link in a specific mailing.

### Spam and email deliverability

When you send mass emails, there is a risk they will be marked as spam. This affects delivery of both the current email and future emails sent from your server. Managing these issues is complex and outside the scope of this book. If your organisation does not have a system administrator, consultant, or email hosting service knowledgeable about them, you may want to seek expert advice.

### Email and template design/layout

The success of an email depends partly on its design and layout, as well as its content. A well-designed email is clean, organised, and adapts to the ways people read email, including on smart phones, tablets, laptops, desktops, browsers, and applications. Consider these design practices:

- Create well-designed base templates and encourage or enforce their use. These might range from a single-column table layout with a header image and text footer to a series of progressively more structured layouts. A consistent look and feel matters for organisation and communication branding.
- Responsive email design can be very challenging &amp;mdash; in ways much more challenging than response web design &amp;mdash; because email is read in many environments and applications. Email applications also lack a universally accepted set of standards for rendering designs, making consistent layouts across devices difficult. Consider acquiring a responsive base template rather than building one from scratch. Free email templates are available that have been well tested on commonly used devices and applications.
- Keep layouts relatively simple. More complex structures are more likely to have problems on different devices. If you develop complex layouts, test them thoroughly or use an email testing service.
- Use tables for layouts. Unlike on websites, where div tags are more appropriate for layout, tables are more universally and consistently rendered in email clients.
- Use inline CSS. Many commonly used email clients do not support externally referenced CSS styles or styles defined in style blocks. To ensure styles are recognised, insert them inline with the element tags.
- Research rendering differences. Tags or CSS styles may render differently between email applications, so you may need to find out why a style is ignored in a particular context.
- Consider design and content together. Focusing on one while neglecting the other may compromise your message.

<!-- Source: email/what-you-need-to-know.md -->
