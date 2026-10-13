---
title: iATS Payments configuration
category: how-to
topic: system-administration
subtopic: iats-payments
component: iATS Payments
audiences:
- technical
- administrator
level: intermediate
journey_stage: plan-and-configure
summary: Set up an iATS account and configure payment processors for the payment types you receive.
extensions:
- iATS Services Payment Processor
related: []
review_priority: low
review_notes: []
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/payment-processors/iats.md
destination_path: sysadmin/setup/payment-processors/iats.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/payment-processors/iats/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# iATS Payments configuration

1. Read the [extension's README](https://github.com/iATSPayments/com.iatspayments.civicrm/blob/master/README.md) for notes about setting up your iATS account setting permissions, server requirements, and other configuration details.

2. Sign up for an account with [iATS Payments](http://home.iatspayments.com/). If you're working with a CiviCRM developer, they may have an agency-specific signup page you should use so that iATS knows who you're working with. Tell iATS that you're using CiviCRM so they can set up your account appropriately. Also tell them whether you want ACH/EFT and/or Swipe support, and make sure you set up the account for the right region (the North America or UK server).

3. Once your account is approved—which may take a few days to a few weeks—install the [iATS Services Payment Processor extension](https://civicrm.org/extensions/iats-payments) in the usual way.

4. Create a payment processor for each type of payment you'll be receiving (credit card, ACH/EFT, or swipe). The credentials are usually the same for each one.

Questions? Use the [github issue queue](https://github.com/iATSPayments/com.iatspayments.civicrm/issues).

<!-- Source: setup/payment-processors/iats.md -->
