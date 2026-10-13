---
title: Recurring contributions and webhooks
category: how-to
topic: system-administration
subtopic: webhook-configuration
component: Payment processors
audiences:
- administrator
- fundraising-manager
- technical
level: intermediate
journey_stage: plan-and-configure
summary: Find the IPN notify URL to use when configuring a payment processor webhook.
extensions: []
related:
- https://docs.civicrm.org/sysadmin/en/latest/integration/wordpress/clean-urls/
review_priority: low
review_notes:
- The instructions refer specifically to Stripe while otherwise describing payment processors generally.
- The WordPress URL examples distinguish CiviCRM 5.26+ from 5.25 and earlier.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/payment-processors/recurring.md
destination_path: sysadmin/setup/payment-processors/recurring.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/payment-processors/recurring/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Recurring contributions and webhooks

## Overview

Most payment processors that support recurring contributions use a "webhook" to notify CiviCRM of each new payment, whether successful or failed.

If webhooks are not set up correctly, you may see one or more of these symptoms in CiviCRM:

- Payments not marked as "Completed".
- New payments not recorded in CiviCRM.

If you are not using recurring contributions, the webhook is not normally required.

## IPN notify URL {:#ipnnotifyurl}

!!! tip
    Follow the instructions for the specific payment processor. When you reach the part where you need to configure the IPN notify URL / Webhook, use the information below to work out what that URL should be.

To find the "URL to be called" value, check what ID is assigned to the Stripe payment processor in CiviCRM:

1. Go back to CiviCRM and click `Administer -> System Settings -> Payment Processor`.
2. Check the id column next to the relevant payment processor, e.g. 3. Do not use the Test ID: that is the id of the Test Processor, unless you are interacting with a sandbox site on your payment processor.

The call back address for a processor with an ID of 3 will be:

    civicrm/payment/ipn/3

Use the appropriate full address below for your site, replacing `NN` with your actual ID number:

- For Drupal and Backdrop: `https://example.com/civicrm/payment/ipn/NN`
- For Joomla: `https://example.com/?option=com_civicrm&task=civicrm/payment/ipn/NN`
- For WordPress with CiviCRM 5.26+: `https://example.com/BASEPAGE/?civiwp=CiviCRM&q=civicrm/payment/ipn/NN`
- For WordPress with CiviCRM 5.25 and earlier: `https://example.com/BASEPAGE/?page=CiviCRM&q=civicrm/payment/ipn/NN`
- For WordPress with [CleanerURLs enabled](https://docs.civicrm.org/sysadmin/en/latest/integration/wordpress/clean-urls/): `https://example.com/BASEPAGE/payment/ipn/NN`

For WordPress, replace `BASEPAGE` with the base page set at `https://example.org/wp-admin/admin.php?page=CiviCRM&q=civicrm/admin/setting/uf&reset=1`.

Typically, you only need to configure the end point to send live transactions, and you want it to send all events.

<!-- Source: setup/payment-processors/recurring.md -->
