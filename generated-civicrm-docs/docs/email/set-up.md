---
title: Set up CiviMail for mass mailings
category: how-to
topic: mailings
subtopic: mass-mailing-setup
component: CiviMail
audiences:
- communications-manager
- administrator
- event-manager
- fundraising-manager
level: intermediate
journey_stage: plan-and-configure
summary: Configure organisation contact information, mailing groups, and scheduled jobs for mass mailings.
extensions: []
related: []
review_priority: high
review_notes:
- The Smart Group guidance describes an exception for Event Participants, but later says Smart Groups cannot be created from
  Advanced Search results displayed as anything other than Contacts. The source leaves this apparent contradiction unresolved.
- The scheduled-jobs guidance links to a wiki page whose currency has not been established.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: email/set-up.md
destination_path: email/set-up.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/email/set-up/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Set up CiviMail for mass mailings

This page describes how to set up information such as From email addresses and Mailing List Groups. It assumes that the basic functionality necessary for your server to send and process emails has already been configured. See *CiviMail Setup* in the [System Administrator Guide](https://docs.civicrm.org/sysadmin/en/latest) for details.

## Configure your organisation's contact information

To send mass emails, you must fill in your organisation's name, a short description, your email address, and your postal address. CiviMail requires that you include the sender's postal address along with unsubscribe/opt-out links in any mass mailing you send, in order to comply with privacy laws in many countries. This information is made available via tokens and must be included in any mail sent with CiviMail.

To configure this information, go to **Administer > Communications > Organization Address and Contact Info**.

## Mailing groups

CiviMail uses Groups to organise recipients of mass mailings. To create a group, go to **Contacts > New Group**. When you create and configure a Group for this purpose, make sure to check Mailing List under Group Type so that it is available as a Mailing List in CiviMail. You can then do a search and add contacts to the Group.

You can also create Smart Groups based on search results, which will update the Group with any contacts that fit the search criteria. For example, based on the results of Advanced Search you can create a Smart Group of contacts who have active memberships, or a Smart Group of contacts in a given city. As people become members or move to the city you've searched on, they will be automatically added to the Smart Group. This makes it possible to send mailings without having to first update the contacts in a group.

To create a **Smart Group**:

1. Go to **Advanced Search** or **Find Contact** and run a search query based on the criteria for your group.
2. On the search results page, click the radio button that selects all the records.
3. From the **Actions** drop-down menu, select **Group - create smart group**.
4. The next screen provides a review of the criteria chosen for the Smart Group. Give the Smart Group a name and (optionally) a description, and make the Smart Group a Mailing List.
5. Click **Save Smart Group**.

!!! info
    You can also create a Smart Group based on a Participant
    search. However, the Smart Group save page will not offer you the option
    to make this group a Mailing List. To make this Smart Group available to
    CiviMail, you must change its settings through **Contacts > Manage
    Groups**. This same thing happens if you use the Advanced Search and
    choose Event Participants under "Display results as."

You cannot create smart groups based on Membership, Contributions or Pledge searches, or based on results of an Advanced Search if the "Display results as" option is set to anything but Contacts.

## Scheduled jobs and cron jobs

After people have signed up on your mailing list(s), you will want to be able to send them mass mailings. You will also want to automatically handle any bounced email messages. These topics are dealt with in detail in the **Everyday tasks** and **Maintaining Healthy Email Lists** parts of this book, respectively. Here in this section we are going to look at some backend and server options that enable the sending of mass mailings and the bounce handling to happen.

Go to **Administer > System Settings > Scheduled Jobs** and you will see all scheduled jobs that CiviCRM uses to do certain tasks on a regular basis. One such task is the actual sending of mass mailings, which is handled by the **Send Scheduled Mailings** scheduled job. Another task is the processing of bounced emails, for which the **Fetch Bounces** scheduled job is responsible. You will need to enable these two scheduled jobs (and any others that you want to be run on a regular basis). Without these two, CiviMail will not be sending any mailings and will not be processing the bounces.

Now, CiviCRM's scheduled jobs cannot self-trigger themselves. Something on your server has to trigger them. The most common option for this is to set up a cron job on your server. This cron job can trigger one or more (or all) of the scheduled jobs. For more detailed explanations and examples of how to do this, see the [Managing Scheduled Jobs](http://wiki.civicrm.org/confluence/display/CRMDOC/Managing+Scheduled+Jobs) wiki page.

<!-- Source: email/set-up.md -->
