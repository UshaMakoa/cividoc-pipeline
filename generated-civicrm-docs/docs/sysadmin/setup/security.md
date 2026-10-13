---
title: Security
category: explanation
topic: system-administration
subtopic: security-considerations
component: CiviCRM
audiences:
- technical
- administrator
- operations-user
level: basic
journey_stage: overview
summary: Understand the security considerations involved in hosting CiviCRM and handling sensitive data.
extensions: []
related:
- backups.md
- ../misc/behind-a-firewall.md
- https://docs.civicrm.org/dev/en/latest/security/inputs/#phpids
review_priority: medium
review_notes:
- The opening description of a VPN and encrypted protocols is unclear and has been left unchanged.
- The PCI compliance section has an incomplete Markdown link; its link text and target have been left unchanged.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/security.md
destination_path: sysadmin/setup/security.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/security/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Security

CiviCRM is a web based solution, and as such, requires a web server to
run. When web servers store sensitive data and are publicly available
over the Internet - as CiviCRM is designed to be - security is an
important aspect to consider. The recommended approach to securing CRM
data is to use a VPN (Virtual Private Network) to encapsulate data
transferred over public networks in encrypted packets. One of the
simplest methods of implementing this is through forcing the use of
encrypted tunnels when accessing the server through various data
protocols (e.g. SSH, SSL and FTPS, explored below); this effectively
wraps and the data in a protective shell, which can only be opened by
the user's web browser, and the server.

## Encrypted data transfer

There are a number of different protocols (methods) for transferring
data from one point to another.

- **FTPS**: for uploading files to the server outside of the CiviCRM
  interface (admins only), you may wish to use a FTPS (Secure File
  Transfer Protocol) client. If possible, set up FTPS accounts with
  usernames and passwords.
- **SSH**: the SSH (Secure Shell) is a method which can be used to
  authenticate a user - by password or a key - and tunnel them into
  the server to execute command-line instructions.
- **SSL**: this affects your everyday users accessing CiviCRM through
  a web browser. SSL (Secure Sockets Layer) encrypts the data
  submitted on a page by a user and sends it to the server - the only
  entity holding the 'key' to decrypt the data, and vice versa. SSL
  may be required for PCI compliance, or simply to prevent the
  interception of sensitive information during transit. By default,
  CiviCRM is *not* secured for browser access, please read the section
  'Setting up SSL' for configuration instructions.

Note: ensure passwords used by one person across several protocols are
different, as each carry with it varying levels of control.

## PCI compliance

American Express, Discover Financial Services, JCB International,
MasterCard Worldwide, and Visa Inc. work together to form standards for
online payment processing (see
[https://www.pcisecuritystandards.org/about_us/](https://www.pcisecuritystandards.org/about_us/).

Websites that accept payments, for example using CiviContribute and
CiviEvent, should comply with their standards. If the plug-in you are
using routes the user to external pages for payment processing
(e.g. PayPal Standard redirects users to PayPal pages to make the
transaction before returning to your website) the risks are fairly low.
However you should still be compliant, which involves completing a Self Assessment Questionnaire (SAQ),
usually SAQ A, covering some technical points which go beyond using SSL
to secure your site, and just as importantly, covering good security practices in the way
your organization is run.

If credit card information *is* being processed or
stored on your server, standards are higher, involving technical testing of your site, and ongoing monitoring
of the way you manage both human and technical security risks,
and you may need to engage a qualified assessor to help you meet a sufficient standard.
The PCI Security Standards Council publishes [a table](https://www.pcisecuritystandards.org/pci_security/completing_self_assessment)
for guidance about which level of compliance you require.
Consider the payment processing method you intend to use carefully before
implementing it, and seek security consultation if you
decide to store credit card information on your server (this is not
recommended for smaller organizations because compliance is expensive).

For further information, see:
[https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/).

## Unauthorised data access

Aside from the potential need to meet PCI compliance, you should use SSL
if you wish to ensure:

- your data cannot be read by unauthorised users (e.g. through
  intercepting un-encrypted data during transit between the user and
  server).
- a user's session is not hi-jacked through acquiring the cookie used
  to authenticate their access. If this occurs, an unauthorised
  individual could assume their identity and proceed to use the system
  through their account.

## Backups and their security

Hackers are as likely to steal data from backups as from production sites.
The security of backups is covered on the [backups page of this guide](backups.md).

## Data storage jurisdiction

CiviCRM can be run on a web server managed by your organisation, or by
an external hosting provider. When working with issues related to human
rights, or if your organisation is gathering sensitive information about
a country's government or its officials, it may be important to know
where your data is stored. Consider gathering detailed information about
where the servers are physically located, and the country whose
jurisdiction the data will fall under in case a governmental agency
requests information.

## Other security concerns

Data may be accessed by unauthorised individuals through a
variety of methods, many of which do not directly relate to the CRM's
security. Amongst others, the following are areas that should be
examined:

- Physical access to the server: the building holding the servers
  should be adequately protected against break-in.
- Passwords: an organisational policy should be implemented where
  passwords are of a sufficient complexity and length (e.g. minimum 8
  characters, including letters and numbers), and must not be shared
  or divulged over insecure communications like email.

!!! note
    CiviCRM implements PHPIDS, which checks the content of fields users are trying to save, and either prevents them being saved,
    or logs them, if they are suspected of being malicious. There is a little more detail in
    [the section on PHPIDS in the Developer Guide](https://docs.civicrm.org/dev/en/latest/security/inputs/#phpids).

## Putting CiviCRM behind a firewall

Some sites put their CiviCRM behind a firewall instance. This is
especially applicable to sites with mostly backend users. This is
covered on the [behind-a-firewall page of this guide](../misc/behind-a-firewall.md).

<!-- Source: setup/security.md -->
