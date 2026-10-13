---
title: Setting up SSL
category: how-to
topic: system-administration
subtopic: encrypted-browser-access
component: CiviCRM
audiences:
- administrator
- technical
level: intermediate
journey_stage: plan-and-configure
summary: Set up an SSL certificate and choose how to redirect CiviCRM traffic to HTTPS.
extensions: []
related:
- https://letsencrypt.org/
review_priority: low
review_notes:
- The description of the CiviCRM HTTPS redirection option may reflect an older interface or feature; its behaviour and menu
  path have been left unchanged.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/security-part2.md
destination_path: sysadmin/setup/security-part2.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/security-part2/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# Setting up SSL

SSL encrypts the data transferred between a user's web browser and the server. It is *not* enabled upon installation as it requires an SSL certificate. Many browsers now display a warning that a page is insecure if content on it is not delivered via an SSL connection secured by a certificate from a trusted vendor.

Before choosing a hosting company or web server provider, check how they support SSL certificates. If running your own server, you can obtain free certificates from [LetsEncrypt](https://letsencrypt.org/). Control panel vendors may also provide proprietary systems for installing free certificates instead of, or as well as, LetsEncrypt. On shared hosting, free certificates from LetsEncrypt or the control panel vendor can normally be activated by clicking in the relevant part of the control panel, or by raising a support ticket, following documentation provided by the hosting company.

All SSL certificates expire, and must be reinstalled before expiry, otherwise browsers will display warnings about the certificate not being valid. Free certificates usually last for only three months, on the assumption that a short life is more secure if the certificate is compromised, and creates no inconvenience because free certificates are are usually installed and renewed automatically. Paid certificates can usually be purchased from your hosting company, as well as third-party vendors. On shared hosting they usually have to be installed by the hosting company, or in the control panel, following documentation the hosting company provides.

## Redirecting traffic from http to https

After installing the SSL certificate, traffic to your site should be redirected to use https instead of http. To use SSL for *all* CiviCRM pages, either edit the web server's configuration file (not usually possible on shared hosting), or your CMS's .htaccess file, to force SSL by redirecting all HTTP requests to HTTPS. Sometimes hosting control panels provide a facility for setting up such a redirect, which usually involves automatically writing a few lines of code to your .htaccess file. If using Drupal, bear in mind that every core update by default replaces your .htaccess file with a new copy, and all modifications including any https redirect will be lost and must be re-instated. Without this redirect, users will be able to access the site on both SSL and non-SSL connections (except in the rare case that the server is configured not to work at all on non-SSL connections).

Alternatively, after installing the certificate, enable 'HTTPS' redirection on your CiviCRM site so that just the login, online contribution, member, event and administrator pages use SSL encryption. CiviCRM has an option to check the certificate and enable SSL for these pages at **Administer** > **System Settings** > **Resource URLs**.

If you have a public-facing website, note that when switching traffic from (for example) http://example.org to https://example.org, some analytics programs, such as the Facebook share count, treat http://example.org and https://example.org as separate sites, and re-start the count of page visits or shares for the https version at zero. Workarounds for this issue are not specific to CiviCRM and are outside the scope of this documentation.

<!-- Source: setup/security-part2.md -->
