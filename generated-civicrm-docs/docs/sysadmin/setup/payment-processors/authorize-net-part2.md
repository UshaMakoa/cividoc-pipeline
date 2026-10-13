---
title: eProcessing Network configuration via Authorize.net Emulation
category: how-to
topic: system-administration
subtopic: eprocessing-network
component: CiviCRM payment processors
audiences:
- technical
- administrator
- event-manager
- fundraising-manager
level: intermediate
journey_stage: plan-and-configure
summary: Configure eProcessing Network through Authorize.net Emulation and test payments.
extensions: []
related: []
review_priority: medium
review_notes:
- The PHP 4.3.0+ requirements and interface paths appear outdated; they have been left unchanged.
- The source calls the required key RestrctKey and describes an AIM submission to Authorize.Net while discussing eProcessing
  Network emulation; these details need verification.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/payment-processors/authorize-net-part2.md
destination_path: sysadmin/setup/payment-processors/authorize-net-part2.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/payment-processors/authorize-net-part2/
civicrm_version:
- 4.3.0
last_modified: '2026-07-02'
---

# eProcessing Network Configuration (via Authorize.net Emulation)

!!! note

    To interface with **eProcessing Network** via Authorize.net Emulation, you can select Authorize.net AIM (Advanced Integration Method) as the Payment Processor for your CiviCRM online contributions, membership sign-up and event registration. This page describes the configuration requirements and steps.

## PHP Configuration Requirements

The following PHP extensions must be enabled in order for CiviCRM to interface with the eProcessing Network's payment services:

* PHP Perl Compatible Regular Expressions extension for PHP 4.3.0+ and higher
* PHP cURL extension for PHP 4.3.0+ and higher with SSL support

Use phpInfo() to check for these extensions. You should see the following lines:

```
PCRE (Perl Compatible Regular Expressions) Support =&gt; enabled
CURL support =&gt; enabled
```

The MHash extension is also recommended, although not required.

## Advanced Integration Method vs Simple Integration Method

For eProcessing.com (Authorize.Net Emulation) **Advanced Integration Method (AIM)**, card information is submitted to the server. The server then takes all submitted information, and submits it to Authorize.Net as an HTTP Post form. A reply is then received, which consists of a single CSV line. This reply is parsed to determine success or failure, and if failure, the reason for failure.

**At this time, CiviCRM only supports the Advanced Integration Method.**

## Configure API Access

**NOTE:** The following assumes that you already have an eProcessing Network merchant account. If you don't, you can go to [http://www.eprocessingnetwork.com/](http://www.eprocessingnetwork.com/) to sign up.

If you do not already have an **RestrctKey** , generate this now from the eProcessing Network account page.

After this is done, create the eProcessing Network Payment Processor configuration in CiviCRM::

* Log into CiviCRM as an administrator
* Select **Administer CiviCRM** » **Global Settings** » **Payment Processors**
* For **Payment Processor Type** , choose **Authorize.Net - AIM**
* Enter the **Account ID** in the **API Login** field, enter the **RestrctKey** in both the **Payment Key** and **MD5 Hash** fields.
* Enter [https://www.eProcessingNetwork.Com/cgi-bin/an/order.pl](https://www.eProcessingNetwork.Com/cgi-bin/an/order.pl) in the **Site URL** field.

Remember that credit card information is being transmitted to the server. **Unless the site is specifically being used for testing, and no live transactions will take place, it is highly recommended that Force Secure URLs be set**

## Testing

The following card numbers can be used for testing:

* American Express: 370000000000002
* Discover: 6011000000000012
* MasterCard: 5424000000000015
* Visa: 4007000000000027 (NOTE: This test card number doesn't validate on CiviCRM's contribution page)

These numbers will always succeed in test mode as long as the expiration date is in the future. You can enter any value for the Security Code (CSC) when testing.

## Additional Documentation

For more information on the eProcessing Network's Integration and Devloper utilities, see: [http://www.eprocessingnetwork.com/Utilities.html](http://www.eprocessingnetwork.com/Utilities.html)

For more information on the Authorize.Net Advanced Integration Method, see the AIM guide: [http://www.authorize.net/support/AIM_guide.pdf](http://www.authorize.net/support/AIM_guide.pdf)

<!-- Source: setup/payment-processors/authorize-net-part2.md -->
