---
title: Troubleshoot PayPal payments pending because of taxes
category: how-to
topic: system-administration
subtopic: paypal-tax-troubleshooting
component: CiviContribute
audiences:
- operations-user
level: intermediate
journey_stage: reference-and-troubleshooting
summary: Identify the PayPal tax setting associated with payments that remain pending.
extensions:
- Canadian Sales Tax
related: []
review_priority: medium
review_notes:
- The statement that sales tax support was added to core in v. 4.6 is version-specific.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/payment-processors/paypal-pro-part3.md
destination_path: sysadmin/setup/payment-processors/paypal-pro-part3.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/payment-processors/paypal-pro-part3/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# Troubleshoot PayPal payments pending because of taxes

If you change the PayPal setting so that PayPal calculates and adds taxes, then the total amount charged by PayPal will no longer match that in CiviCRM. When PayPal calls back to CiviCRM saying it has received payment for $Total including taxes this doesn't match CiviCRM's $Total that excludes taxes. If you check your CiviCRM log file (generally under files/civicrm/ConfigAndLog/) you'll find an error similar to

```
Nov 04 10:12:57 [info] Amount values don't match between database and IPN request
```

The solution is to turn off the PayPal Sales Tax option.

Sales tax support is added to core in v. 4.6, and there is a Canadian Sales Tax extension available. Feel free to contact Joe (dot) Murray (at) JMAConsulting (dot) biz for advice on how to create an extension for your jurisdiction if need be.

<!-- Source: setup/payment-processors/paypal-pro-part3.md -->
