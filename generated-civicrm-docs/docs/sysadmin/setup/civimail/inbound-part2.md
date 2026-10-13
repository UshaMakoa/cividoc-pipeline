---
title: Autofile email activities via EmailProcessor
category: how-to
topic: system-administration
subtopic: email-to-activity-processing
component: CiviMail
audiences:
- communications-manager
- operations-user
- administrator
- technical
level: intermediate
journey_stage: manage-and-automate
summary: Configure an email account to file incoming messages as contact activities.
extensions: []
related:
- ../jobs.md
review_priority: high
review_notes:
- The Firefox and Google Chrome automatic-bcc instructions depend on userscripts.org links and browser interfaces that appear
  obsolete; their current usability needs verification.
- The note's wording "You an configure" is unclear, and its advice refers to CiviCRM 5.67; both are retained for review.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/civimail/inbound-part2.md
destination_path: sysadmin/setup/civimail/inbound-part2.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/civimail/inbound-part2/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# Autofile email activities via EmailProcessor

The email processor is a function and scheduled job that attempts to parse emails in an email account (e.g. a POP3/IMAP inbox). It records a copy as an activity in the contact records corresponding to the To:, Cc:, Bcc:, and From: fields. If no matching contact record is found, a new contact is created and the email is filed under that record.

## Set up email-to-activity processing

1. If it is not already enabled, enable CiviMail under Administer &gt;&gt; Configure &gt;&gt; Global Settings &gt;&gt; Enable CiviCRM Components. You do not need to fully configure or use CiviMail functionality, but it must be enabled to activate the email autofiling tool. If you are using Drupal, set permissions to give you access to CiviMail.
2. Under Administer CiviCRM &gt;&gt; CiviMail &gt;&gt; Mail Accounts, configure one or more email accounts. In the "Used For" field, select Email-to-Activity Processing.
3. Test it by executing the job under Administer &gt;&gt; System Settings &gt;&gt; Scheduled Jobs &gt;&gt; select "Process Incoming Emails" (API: **fetch_activities** ) and "Execute now."
4. The first time you run the script, you should see folders created in your email account to designate processed and ignored emails. After testing, visit the contact record you emailed to and confirm the presence of the email activity.
5. Optionally, set it up to run regularly via [scheduled jobs](../jobs.md).

!!! note "Important note on bounce processing and processing incoming emails"
    Because the bounce handling and EmailProcessor routines both process emails and then file them under "processed" and "ignored" emails, they cannot be used on the same email account. You need two separate accounts: one for bounce processing and one for email-to-activity processing.

    You an configure your `fetch_bounces` scheduled job with `is_create_activities` to create activities for the bounces / any replies. But, this is not advised prior to CiviCRM 5.67. Note that the activities will be of the type 'Inbound Email' unless you create an activity type 'Bounce', in which case the latter will be used for bounces. Also note that there is information in these activities that can be seen via SearchKit but not via the View Activity page.

## Choose which emails to file

### Use an account dedicated to autofiling

In the typical implementation, you create a single email account used solely for autofiling as activities. As you interact with constituents using your email client, you may cc or bcc this account to have an email processed for the contact.

You may instead process your normal incoming email accounts, but doing so may unnecessarily clutter your system: many inbound emails are not important enough to attach to a contact record this way.

### Use an IMAP folder

Another possible implementation, if your mail server supports IMAP, is:

1. Create a mail folder to indicate which emails the processor should process. Let's call it `civicrm`.
2. When administering your mail accounts in the steps above, enter the path to that folder in the "Source" field. It will typically be `INBOX.civicrm`, not just `civicrm`.
3. To autofile an email in your inbox, move it into this folder. If your mail client supports it, make a copy rather than simply moving it; you will likely want the email to remain in your Inbox or primary folder structure.
4. The processor creates subfolders `INBOX.civicrm.CiviMail.processed` and `INBOX.civicrm.CiviMail.ignored` and moves the email into one of them when done. Those folders might not be visible at first, making it seem as though your emails are lost. You can subscribe to the folders in your webmail or email client to make them visible again.

### Send a copy from Thunderbird

If you use Thunderbird as your email program, a Bounce plugin allows you to send a copy of an email to another address—in this case, the single email address set up for autofiling—with its original headers intact. Unlike forwarding, which loses the original From, To, and Cc information, this allows the email processor to file it correctly.

### Use an intermediary for a mail account

If you have trouble configuring a mail account to work with your server, another possibility is an intermediary. For example, you could write a script using a program such as getmail to pull from the account into a local unix maildir, then configure the CiviMail account to use the maildir protocol.

### Set up automatic bcc for Gmail or Email via Google Apps

If you’re using Gmail or Email via Google Apps, there is no built-in automatic cc or bcc function, but you can set up an automatic bcc with a Greasemonkey script on Firefox or a Tampermonkey script on Google Chrome.

#### Using Firefox

1. Install the Greasemonkey add-on for Firefox: [https://addons.mozilla.org/en-US/firefox/addon/greasemonkey/](https://addons.mozilla.org/en-US/firefox/addon/greasemonkey/).
2. Install the "automatic bcc" Greasmonkey script: [http://userscripts.org/scripts/show/2255](http://userscripts.org/scripts/show/2255).
3. Restart Firefox.
4. Login to your Gmail account using the Firefox browser and hit "Compose" to create a new email. When the compose window opens, you should see a dialog box from the "automatic bcc" Greasemonkey script prompting you to add a destination bcc email address. You may enter more than one email address separated by commas.

As long as you use the Firefox browser and the Greasemonkey add-on is enabled, your emails will be automatically bcc’d to the email address(es) you specified in the dialog box. To test the script, expand the bcc section of your email compose screen. The bcc field should contain the automatic bcc addresses you entered in the dialog.

#### Using Google Chrome

1. Install the Tampermonkey add-on for Chrome: [https://chrome.google.com/webstore/detail/dhdgffkkebhmkfjojejmpbldmpobfkfo](https://chrome.google.com/webstore/detail/dhdgffkkebhmkfjojejmpbldmpobfkfo).
2. Install this “automatic bcc” script: [http://userscripts.org/scripts/show/2255](http://userscripts.org/scripts/show/2255).
3. Restart Google Chrome.
4. Login to your Gmail account using the Google Chrome browser and hit "Compose" to create a new email. When the Compose window opens, click on “add bcc”. A dialog box from the Tampermonkey script will prompt you to add a destination bcc email address. You may enter more than one email address separated by commas.

As long as you use the Google Chrome browser and the Tampermonkey add-on is enabled, your emails will be automatically bcc’d to the email address(es) you specified in the dialog box. To test the script, expand the bcc section of your email compose screen. The bcc field should contain the automatic bcc addresses you entered in the dialog.

<!-- Source: setup/civimail/inbound-part2.md -->
