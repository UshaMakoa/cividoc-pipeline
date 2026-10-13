---
title: Card Access Services CASConnect configuration
category: how-to
topic: system-administration
subtopic: casconnect-configuration
component: CASConnect
audiences:
- technical
- administrator
- operations-user
level: intermediate
journey_stage: plan-and-configure
summary: Download, install, and configure the CASConnect payment processor extension.
extensions:
- CASConnect
related: []
review_priority: medium
review_notes:
- The directory, extension-management, and extern-directory instructions name specific older CiviCRM, Joomla, and Drupal versions;
  their applicability to other versions is unclear.
- The alternative-URL instructions require contacting 'us' for account and notify-script changes, but do not identify the
  contact.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/payment-processors/card-access.md
destination_path: sysadmin/setup/payment-processors/card-access.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/payment-processors/card-access/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Card Access Services CASConnect configuration

## Download

CASConnect is available from the download section at [http://developer.cardaccess.com.au/en/civicrm-integration/#download](http://developer.cardaccess.com.au/en/civicrm-integration/#download).

## Installation and configuration

### Ensure your CiviCRM extensions directory is configured

More details can be found on the CiviCRM website, but typically this involves logging in as administrator and editing the directory setting:

- CiviCRM 3.4.8 and 4.0.8: "Administer->Configure->Global Settings->Directories->CiviCRM Extensions Directory"
- CiviCRM 4.1: "Administer->System Settings->Directories->CiviCRM Extensions Directory"

If you have already configured other extensions, this step is not necessary.

### Install the extension

This requires three separate steps.

#### Unpack the extension

Unzip `au.com.cardaccess.payment.casconnect.zip` into the extensions directory configured above.

#### Copy the IPN files to their final location

Copy the following files into CiviCRM's "extern" directory:

- `cASConnectNotify.php`
- `CASConnectIPN.php`
- `CASConnectUtil.php`

The "extern" directory varies according to the CRM hosting CiviCRM, for instance:

- Joomla 1.7.4: `[JOOMLA_DIRECTORY]/administrator/components/com_civicrm/civicrm/extern`
- Drupal 7.12: `[DRUPAL_DIRECTORY]/sites/all/modules/civicrm/extern`

The procedure above is recommended because it will work without further modifications.

But if you absolutely cannot modify the extern directory (e.g. your hosting provider won't allow it) and need to use another URL then this can be done but it will require some manual fiddling - please contact us for more details, we will need to make a configuration change to your account on our end and the notify script

#### Activate the CASConnect Payment Processor

1. Log into your website as an administrator and navigate to the "CiviCRM Extensions" setting:
   - CiviCRM 3.4.8 and 4.0.8: "Administer->Customize->Manage CiviCRM Extensions"
   - CiviCRM 4.1: "Administer->Customise Data And Screens->Manage CiviCRM Extensions"
2. You should now see CASConnect become available for installation. Click "Install" and then "Install" again.

### Configure the extension

Configure the following items before starting to process transactions. These will be randomly generated when an account is setup on our end:

- Merchant ID
- Transaction Password
- Callback Password

In some cases you might also be provided an aggregator ID. If this is not provided, the aggregator ID field can be left blank.

It is recommended that the other fields be left as is (especially the Site and Button URLs).

<!-- Source: setup/payment-processors/card-access.md -->
