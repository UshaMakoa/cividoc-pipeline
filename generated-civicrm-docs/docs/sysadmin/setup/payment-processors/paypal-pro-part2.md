---
title: Configure PayPal Pro recurring contributions
category: how-to
topic: system-administration
subtopic: paypal-pro-recurring-contributions
component: CiviContribute
audiences:
- fundraising-manager
- operations-user
- administrator
level: intermediate
journey_stage: manage-and-automate
summary: Understand PayPal Pro recurring contributions and configure their IPN updates.
extensions: []
related:
- recurring.md#ipnnotifyurl
review_priority: low
review_notes: []
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/payment-processors/paypal-pro-part2.md
destination_path: sysadmin/setup/payment-processors/paypal-pro-part2.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/payment-processors/paypal-pro-part2/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# Configure PayPal Pro recurring contributions

CiviCRM supports Paypal Pro recurring contributions.

The differences between Paypal Standard Subscriptions and Paypal Pro Recurring Contributions are as follows:

* Standard Subscriptions require the contributor/donor to have a Paypal account while Pro Recurring does **not** require the donor to have a Paypal account. A credit card is sufficient to use Paypal Pro recurrings.
* Standard Subscriptions are included for free in your Standard account services. Pro Recurring feature costs an additional monthly charge on top of Pro.

To take advantage of recurring and one-time contributions on the same CiviCRM Contribution page, you must have the Pro Recurring add on. You cannot process Pro one-time donations and Standard Subscriptions from the same Contribution page.

Once you have added the Recurring feature to your existing Paypal Pro account, configure your IPN settings in Paypal so CiviCRM can receive updates on the recurring contributions:

* Log in to your Paypal account
* Click Settings (Gear icon)
* Click Account Settings > Website Payments > Instant Payment Notifications
* Follow the instructions here: [IPN Notify URL](recurring.md#ipnnotifyurl) to work out the correct URL to use
* Enter the URL and save

!!! note
    You can re-send an IPN message from this area by using the IPN search. This is good if you have had it set to the wrong URL & want to resend them once you've fixed it

!!! tip
    If you are still using the deprecated `https://example.com/civicrm/extern/ipn.php` you should switch to the standard CiviCRM URL details can be found here: [IPN Notify URL](recurring.md#ipnnotifyurl)

## Expected behavior

When CiviCRM processes a recurring contribution via Paypal (Standard or Pro) a single Contribution is created in CiviCRM which is marked visibly as "recurring". However within the Paypal account history, two separate transactions will be visible.

* The 'initial' payment is transacted immediately, in the amount specified
* A separate, 'repeating' (in the case of Pro) or 'subscription' (in the case of Standard) is also created, which will transact again at the specified interval, duration and amount

With Paypal Standard, a payor wishing to stop their recurring payment may do so within their own Paypal account by stopping their subscription. In contrast, with Paypal Pro, the payment is made via credit card and thus the repeating payment must be stopped from within the merchant's Paypal account, **not** the payor's Paypal account.

## Recurring processing failure

Credit card numbers and expiration dates change over time. Because neither CiviCRM nor Paypal are capable of reaching into a payor's wallet to update this information, you should expect that a percentage of recurring payments will fail. When this happens, CiviCRM records a contribution of status "Failed" associated with the Contact record, although CiviCRM does **not** send a "Failed" email notification to the payor directly. Paypal will, however, send an email to the payor notifying them of a failed recurring payment and the repeating payment or subscription will be canceled. The payor can then attempt to re-establish their payment.

<!-- Source: setup/payment-processors/paypal-pro-part2.md -->
