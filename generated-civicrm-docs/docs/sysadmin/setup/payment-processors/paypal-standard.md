---
title: PayPal Standard configuration
category: how-to
topic: system-administration
subtopic: paypal-website-payments-standard
component: CiviContribute
audiences:
- administrator
- operations-user
- technical
- event-manager
level: intermediate
journey_stage: plan-and-configure
summary: Configure PayPal Website Payments Standard for contributions and event registration, and troubleshoot payment notifications.
extensions: []
related:
- recurring.md#ipnnotifyurl
review_priority: medium
review_notes:
- The PayPal interface instructions and references to June 2019 and CiviCRM versions 4.5 and 4.6 may be out of date; verify
  them before relying on these instructions.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/payment-processors/paypal-standard.md
destination_path: sysadmin/setup/payment-processors/paypal-standard.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/payment-processors/paypal-standard/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# PayPal Standard configuration

## Overview

**What is the basic business idea of paypal?**

Every user has his account with paypal where he has some money he can use to pay online, using various means like e-mail, web etc. Once a user has a paypal account he cannot do transactions with paypal without logging into his account.

Beware: If your account has some unresolved conflicts it will not let you do things you want but will just show the account overview where you could select the next actions.

Note for registered non-profits: If you start a non-profit account with Paypal you must provide acceptable documentation to Paypal of your legal status as a non-profit, or Paypal will disable your account.

**What is the principle of using a sandbox at paypal?**

They have tried to use exactly the same software as the live system with the same screens and behaviour. To enter the sandbox you first log in to your paypal developer account, then select a test user (the role depends on your needs) and enter the sandbox. From then on you are like a user in the live situation.

## PayPal Website Payments Standard

### Enable CiviContribute

* Log into CiviCRM as an administrator.
* Select **Administer CiviCRM &gt; Global Settings &gt; Enable Components**
* Ensure that CiviContribute is enabled.

### Add a payment processor

* Select **Administer CiviCRM &gt; Global Settings &gt; Payment Processors**
* Click **New Payment Processor**
* Select **PayPal - Website Payments Standard** for Processor Type.
* Enter into **Merchant Account Email Address** the email which is used for your Paypal account for **live transactions**.
* Enter the **Merchant Account Email Address** linked to your PayPal Sandbox merchant account (e.g. _paypal_1207343391_biz@example.com_ ) in the **Processor Details for TEST Payments** section, if you are using a testing sandbox. If not, enter the same email address as the step above.
* If you'd like to process live payments on the site, you can generally accept the default values for **Site and Button URLs**.

Note: If you are still developing the site, and would like to test the work-flow on the site (and accept no live payments), copy the "Test Payments" values to the "Live Payments" section.

Note: If you see an API URL field for Paypal_Standard, you can ignore it.

### Assign this processor to your contribution or event registration page(s)

You must assign your new Payment Processor to your Contribution Page or Event Registration before you can test-drive them.

* For Contribution Pages - go to **Manage Contribution Pages &gt; Configure &gt; Title and Settings** and select your Website Standard processor, then click **Save**.
* For Event Registration - go to **Manage Events &gt; Configure &gt; Event Fees** and select your Website Standard processor, then click **Save**.

### Enabling recurring contributions

If you are using PayPal Website Payments Standard - you can give users the option to make a recurring contribution on any of your Contribution Pages.

* **Administer CiviCRM &gt; Manage Contribution Pages**
* Click **Configure** for the page where you want to enable recurring contributions
* Click **Contribution Amounts**
* Check the **Enable recurring payments** box.

### Configure Paypal to talk to CiviCRM

CiviCRM can receive feedback from Paypal after the contribution is made. This requires making some changes within your Paypal account Profile at [https://www.paypal.com](https://www.paypal.com)

#### Instant Payment Notification

* To configure Instant Payments Notification (IPN) for your PayPal account click Profile (the gear ⚙️ icon) then under Selling Tools click to update "Instant payment notifications"
* Click "Choose IPN Settings"
* Select "Receive IPN messages (Enabled)"
* Your specific IPN will vary with you domain address, your CMS, and which payment processor ID CiviCRM has for this PayPal processor. Use the approach at [IPN Notify URL](recurring.md#ipnnotifyurl) to determine the right address, then put in as the Notification URL. (CiviContribute will also pass the exact IPN 'listener' URL to PayPal automatically during each transaction, but there are reports in June 2019 this was insufficient.)
* Click Save

!!! tip
    If you are still using the deprecated https://example.com/civicrm/extern/ipn.php you should switch to the standard CiviCRM URL as detailed at [IPN Notify URL](recurring.md#ipnnotifyurl)

#### Then set the auto return so the contributor goes back to your site

* Click: Profile &gt; Selling Tools &gt; Website Preferences &gt; Update
* Set Auto Return to On
* Enter your CiviCRM site home page as the **Return URL**. This is a placeholder. CiviContribute will pass the exact return URL to PayPal automatically during each transaction.
* Set "Payment Data Transfer" to "Off"
* Click Save

### Creating a testing sandbox account at Paypal Developer Central

[https://developer.paypal.com](https://developer.paypal.com/)

If you don't have an Developer Central account, follow PayPal instructions to register a developer account and create a sandbox (test) merchant account.

#### Launch your merchant sandbox

Login as your Developer Central account (e.g. _paypaldev@example.com_ ) and create two new "sandbox" accounts. "Create Account:" -> "Preconfigured"

* Create a "seller" - this is your website. E.g. _paypal_1207343391_biz@example.com_
* Create a "buyer" - this is your test donor/customer. E.g. _paypal_1208220862_per@example.com_

Configure CiviCRM with the "seller". Use the "buyer" to test the site. If you "reset" the seller account, be sure to repeat these steps.

#### Profile &gt;&gt; Instant Payment Notification Preferences

From your Developer central account (e.g. _paypaldev@example.com_ ) at [https://developer.paypal.com](https://developer.paypal.com/)

* Test accounts -> Select the "seller" account (e.g. _paypal_1207343391_biz@example.com_ ) -> Click "Enter Sandbox Test Site" -> Login
* You should now be at [https://www.sandbox.paypal.com/...](https://www.sandbox.paypal.com/...)

### Trouble-shooting

#### Contributions remain in PENDING status

In order for contributions to be marked as COMPLETED, PayPal's Instant Payment Notification (IPN) must post back to CiviCRM an acknowledgement that the contribution was completed. In order for this to happen, your CiviCRM site must be accessible on the public internet (i.e. not running on localhost or behind a firewall). Interactions with PayPal IPN are logged to a file called **CiviCRM.log** or CiviCRM.&lt;33char string&gt;.log located in your configured **Temporary Files Directory** (typicaly `<drupal_root>/sites/default/files/civicrm/ConfigAndLog` or `<wp_root>/wp-content/uploads/civicrm/ConfigAndLog`). Check this file for errors if your contribution statuses are not being set to COMPLETED.

One issue when using the Paypal test account is that you sometimes need to confirm your payments in PayPal- possibly only when dealing with multiple currencies. If you see a message in the CiviCRM.log file:

> [info] returning since contribution status is pending.

If this is the case:

* Log into into your test PayPal account:
* On the overview page you will see that the payment will be in an Unclaimed status - click Accept in the Order status/Actions column.
* The IPN will be resent and you should get a message similar to:

    > [info] Contribution record updated successfully
    > [info] Success: Database updated and mail sent

#### Resending IPNS

From civicrm 4.5 a copy of any IPNs received will be in the civicrm_system_log table. If the IPN was not received at all (e.g server outage) you can resend them while logged into your paypal account

1. Go to 'Profile' and then under 'Selling Preferences' you should see 'Instant Notification Preferences'
1. On the Instant Notification page you get to you should see a link to 'IPN History Page'
1. Search for the missed IPNS (up to 28 days ago), select them all & click resend
1. TIPS - you don't have to worry about oversending - if you select some that were already received no harm done (despite the scary message). Also, at the bottom of the page you can change to select more than 25 at once to reduce your effort

#### Unexpected errors from PayPal

Occasionally there are technical / availability problems with the PayPal Sandbox servers. You can [check Sandbox status here](https://www.paypaldeveloper.com/blog?blog.id=sb).

#### Turning on taxes in PayPal causes payments to remain pending

If you change the PayPal setting so that PayPal calculates and adds taxes, then the total amount charged by PayPal will no longer match that in CiviCRM. When PayPal calls back to CiviCRM saying it has received payment for $Total including taxes this doesn't match CiviCRM's $Total that excludes taxes. If you check your CiviCRM log file you'll find an error similar to

```
Nov 04 10:12:57 [info] Amount values don't match between database and IPN request
```

The solution is to turn off the PayPal Sales Tax option.

Sales tax support is added to core in v. 4.6, and there is a Canadian Sales Tax extension available. Feel free to contact Joe (dot) Murray (at) JMAConsulting (dot) biz for advice on how to create an extension for your jurisdiction if need be.

<!-- Source: setup/payment-processors/paypal-standard.md -->
