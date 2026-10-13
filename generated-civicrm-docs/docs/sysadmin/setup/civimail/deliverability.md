---
title: Tactics for staying off email blacklists
category: how-to
topic: system-administration
subtopic: civimail-sending-reputation
component: CiviMail
audiences:
- communications-manager
- operations-user
- administrator
- technical
level: intermediate
journey_stage: plan-and-configure
summary: Check mail server settings and use provider guidance to improve CiviMail email deliverability.
extensions: []
related: []
review_priority: medium
review_notes:
- The [rDNS] reference has no link definition in the source.
- The Yahoo forum guidance is described as covering an earlier version of the form.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/civimail/deliverability.md
destination_path: sysadmin/setup/civimail/deliverability.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/civimail/deliverability/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Tactics for staying off email blacklists

When sending email from CiviMail, a significant percentage of messages may bounce as suspected spam or be delivered but marked as suspected spam by the recipient's email program. Paid bulk email services usually achieve better deliverability because they have expertise in handling this problem.

Blacklist services and spam filters rarely disclose the rules they use to identify spam. However, bounce reports often include email headers that indicate why a message bounced. For example, bounces from Google Mail addresses often mention a missing or invalid SPF record. Others sometimes name a blacklist on which your domain or IP address appears.

## Basic steps

- Make sure all your mail servers accept [bounce messages](https://en.wikipedia.org/wiki/Bounce_message).
- Set up an [SPF](http://www.openspf.org/) record in DNS for the server that sends outgoing messages. Optimally, also deploy [DKIM](http://www.dkim.org/) and [DMARC](https://dmarc.org/).
- Make sure your mail server has a reverse DNS [rDNS] entry. For most shared hosting and many private servers, only the server or hosting company can set up an rDNS entry. In that case, raise a ticket requesting one.
- Make sure your email server complies with the [RFC rules](https://en.wikipedia.org/wiki/Anti-spam_techniques#Strict_enforcement_of_RFC_standards) regarding service configuration.
- Use an online tool, such as [http://espcoalition.org/senderid/](http://espcoalition.org/senderid/), to test your email settings.

!!! note
    If your domain name already has an SPF record, make sure it includes the IP address of your CiviCRM mail server. This server might be different from the host used for the web server or from your mail servers. If the SPF record does not include the IP address, add it.

!!! note
    A search will provide links to several email blacklist checkers. Their results can show lists of suspected spammers that have blacklisted your domain or IP address. In many cases, a blacklisting is short-lived and requires no action provided the points above are fixed. Some blacklists provide a form you can use to ask to be removed.

## Additional tools

Some leading email providers offer additional tools or guidance on improving deliverability.

### Yahoo

Bulk senders can improve their reputation with Yahoo by completing the form linked from [the Yahoo FAQ on deliverability](https://help.yahoo.com/kb/postmaster/yahoo-mail-deliverability-faqs-sln24439.html). Guidance on completing an earlier iteration of Yahoo's form, which may still be useful, is available at [https://forum.civicrm.org/index.php%3Ftopic=1484.0#msg6479](https://forum.civicrm.org/index.php%3Ftopic=1484.0#msg6479).

### GMail

Google provides guidance on email deliverability to Google Mail addresses, including [https://support.google.com/mail/answer/81126](https://support.google.com/mail/answer/81126).

### Outlook Live

MS Outlook Live mail (formerly also called Hotmail) has a Junk Mail Reporting Program (JMRP). When a user clicks the "Spam" button in a Hotmail account or moves an item to their junk folder, a report is forwarded to you. You can then exclude that recipient from your lists. This may help your emails maintain a good reputation with Microsoft's spam filter.

To subscribe to JMRP, visit [https://sendersupport.olc.protection.outlook.com/snds/JMRP.aspx](https://sendersupport.olc.protection.outlook.com/snds/JMRP.aspx) (requires a Microsoft login) and complete the form.

Be aware that this is not an opt-out. If you want to opt-out contacts who mark your emails as "Spam" or "Junk", you could use a shell script and the API (with drush civicrm-api or via REST) to opt-out contacts who have marked your email as spam.

See also [https://sendersupport.olc.protection.outlook.com/pm/services.aspx](https://sendersupport.olc.protection.outlook.com/pm/services.aspx).

<!-- Source: setup/civimail/deliverability.md -->
