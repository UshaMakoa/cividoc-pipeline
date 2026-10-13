---
title: Configuring a new site
category: how-to
topic: system-administration
subtopic: new-site-configuration
component: CiviCRM
audiences:
- administrator
- fundraising-manager
- operations-user
- communications-manager
level: basic
journey_stage: plan-and-configure
summary: Review configuration tasks for the features and components your organization will use.
extensions: []
related: []
review_priority: low
review_notes:
- The Tags (Categories) link points to a Drupal demo site; readers may mistake it for their own site's configuration page.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/index-part2.md
destination_path: sysadmin/setup/index-part2.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/index-part2/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# Configuring a new site

After installing a new instance of CiviCRM, site administrators should review these configuration tasks and implement those related to the features and components their organization will use.

!!! tip
    You must be logged in as a user with **administer CiviCRM** permission to complete these tasks. All configuration settings are accessed from the **Administer CiviCRM** page.

## Site configuration

- **Configure** » **Global Settings** » **Localization** » - Language, currency, list of the countries.
- **Configure** » **Domain Information** - Organization name, email address for system-generated emails, organization address.

## Viewing and editing contacts

- **Configure** » **Global Settings** » **Site Preferences** - Configure screen and form elements for Viewing Contacts, Editing Contacts, Advanced Search, Contact Dashboard and WYSIWYG Editor.
- **Configure** » **Global Settings** » **Address Settings** - Format addresses in mailing labels, input forms and screen display.
- **Configure** » **Global Settings** » **Mapping and Geocoding** - to display maps
- **Configure** » **Global Settings** » **Miscellaneous** - Contact search behaviors
- **Configure** » **Customise Data and Screens** » **reCAPTCHA Settings** - reCAPTCHA configuration

## Sending emails (includes contribution receipts and event confirmations)

- **Configure** » **Global Settings** » **Outbound Email (SMTP/Sendmail)**
- **Option Lists** » **From Email Addresses** - Define general email address(es) that can be used as the FROM address when sending email to contacts from within CiviCRM (e.g. info@example.org)

## Online contributions / online membership signup / online event registration

- **Configure** » **Global Settings** » **Payment Processors**
- You will also need to change the access rights so anonymous users can contribute/sign up/register

## Organize your contacts

- **Configure** » [Option Lists » Tags (Categories)](http://drupal.demo.civicrm.org/civicrm/admin/tag?reset=1)
- **Manage groups**

Once you've completed these settings, you can move on to exploring and configuring custom fields, profiles, as well as the various optional components for fundraising and constituent engagement:

- CiviContribute and CiviPledge
- CiviEvent
- CiviMember
- CiviMail
- CiviCase
- CiviGrant

<!-- Source: setup/index-part2.md -->
