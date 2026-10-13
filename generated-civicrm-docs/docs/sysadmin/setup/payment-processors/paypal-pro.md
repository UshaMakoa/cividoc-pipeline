---
title: Configure PayPal Website Payments Pro and Express
category: how-to
topic: system-administration
subtopic: paypal-pro-and-express
component: CiviContribute
audiences:
- technical
- operations-user
- administrator
- fundraising-manager
level: advanced
journey_stage: plan-and-configure
summary: Configure and test PayPal Website Payments Pro and Express for CiviContribute.
extensions: []
related: []
review_priority: medium
review_notes:
- The PHP requirements are dated February 2021, and the PayPal interface instructions include an undated May 20 update and
  a May 2012 alternative.
- The live-account note contains malformed image markup, !PayPal_Web_Pro_Apply.gif!*, which cannot be reliably presented as
  an image without a valid target.
- Several interface instructions and the Drupal warning refer to older screens or paths; their current applicability is unclear.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/payment-processors/paypal-pro.md
destination_path: sysadmin/setup/payment-processors/paypal-pro.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/payment-processors/paypal-pro/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Configure PayPal Website Payments Pro and Express

!!! note "Scope and Audience"
    This document covers the steps needed to configure and run CiviContribute using the PayPal Website Payments Pro plugin. This plugin supports PayPal Pro Express Checkout, and (if desired) Direct Checkout. Consult the PayPal's site for an overview of features and pricing for [Website Payments Pro](https://www.paypal.com/webapps/mpp/merchant).
     The installation of the PayPal plugin is recommended for developers and technical users only at this stage. _It is important that you thoroughly test your site using PayPal Sandbox Server and Sandbox accounts prior to configuring and enabling live transactions. You will also need to acquire and install an SSL certificate if you planning on offering Direct Checkout_.

## Overview of PayPal Pro

PayPal Pro allows you to process payments without users leaving your site.

## Overview of PayPal Express

PayPal Express is an option available to Paypal Pro account users that works like Paypal Standard. It shows up as an orange button "Check out with PayPal" that appears above the billing address. Pressing it takes the end user to the Paypal website where they pay and hopefully return to the site.

PayPal Express has limitations. Like any offsite payment processor it can only process one transaction at a time. Therefore it is incompatible with the setting "Separate Membership Payment" which can be enabled on the membership tab of a contribution page settings. This setting is used in the case that the contribution page is collecting both membership and donation money. It allows each transaction to be processed separately. In the case of PayPal Express it tries to only process the donation amount because that is the last one on the list. Therefore if the donation amount is not selected or is set to "No thanks" an error will occur:

Payment Processor Error message 10400: Transaction refused because of an invalid argument. See additional error messages for details. Order total is missing.

This is a [known issue](http://issues.civicrm.org/jira/browse/CRM-8221).

!!! danger "Availability May Be Limited for Organizations Outside of the United States"

    If your organization is headquartered outside of the United States, we recommend that you confirm availability of Website Payments Pro for your country (and/or banking relationship) with PayPal prior to beginning configuration of this plugin.

## Configuration

### PHP configuration requirements

The following are the PHP requirements for integrating CiviCRM with PayPal's payment services (as of February 2021 https://www.paypal.com/ca/smarthelp/article/what-version-of-php-is-required-to-use-the-paypal-sdk-for-php-ts1057):

* PHP 5.3 and above
* PHP cURL extension with support for OpenSSL
* PHP OpenSSL extension
* Composer

Use phpInfo() to check for these extensions. You should see the following lines:

```
CURL support => enabled
OpenSSL support => enabled
```

### Create a Developer Central account

* Go to [https://developer.paypal.com/](https://developer.paypal.com/) and click "Sign Up".
* Fill out the sign-up form (be sure to make a record of the email address and password used - and use a valid email address so you can respond to the activation email sent by PayPal).
* Check for activation email and click on link to go to Developer Central login page

### Create a Business (Merchant) account on the PayPal Sandbox

* Login to PayPal Developer Central
* Click on the Sandbox tab
* Click **Create a test account** link near the bottom of the page
    * Signup for a PayPal Account form opens in a new window
* Select Business Account, select country and click continue
* Complete both pages of the Business Account Signup form. You can enter 'fake' information as this is only a test sandbox account.
* Make a record of this Sandbox Business Account login (email and password). You will need it to login to the Sandbox in the future.

!!! danger "Use caution in the domain you choose for your sandbox account"
    Please make sure that you actually select a domain that matches the one on your test server if you plan to use the recommended Signature Authentication method. While most of the data you input here can be fake, the business website address you enter should match your test server domain as PayPal will encrypt your key using this domain.

* Now you need to **Confirm Email Address** for this account
    * The confirmation email for this account is NOT actually sent to an email address. This and all other communications for this 'sandbox account' show under the **Email** tab in Developer Central.
    * Click the Email tab in Developer Central and locate the confirmation email
    * Paste the confirmation link from this 'email' into your browser URL and enter your Sandbox Business Account password when prompted
    * You should see **Email Confirmed**. Click continue.
    * Your **Business Account Overview** page is displayed.
* Now you need to **Get (this account) Verified by adding a bank account**
    * Click **Get Verified** link on left column of Overview page and follow prompts
    * You will be adding a 'fake' Bank Account' (you can enter a fake Bank Name - and use the Routing and Account Numbers as per below)

**US Accounts**

The Sandbox automatically generates bank account and sort code numbers when you add a bank account to an US Account.

**UK, Australian, Canadian and German Accounts**

To add test Canadian, German, or UK bank account information, use the following test numbers.

* UK
    * Bank account number: Any 8-digit number- try to be unique - see Error message for why
    * Sort code: 609204 or 700709
* Australia
    * Bank account number: Any one-digit to 12-digit number
    * Account number: any random number
    * BSB Number: 242-200
* Canada
    * Institution number: 311
    * Transit number: 00001
    * Sort code: Any 8-digit number
* Germany
    * Bank account number: Any 10-digit number
    * Routing number: 37020500

**Error Messages**

If receive an an error message when attempting to verify the account, contact MTS requesting that they verify the account for you, providing the email address of the Sandbox account.

Contact MTS including your Sandbox Email Address by clicking on [https://www.paypal.com/mts](https://www.paypal.com/mts). I have an unconfirmed theory that if the account already exists in the system you get the error message which would explain why numbers like 12345678 seem to have failed for me

* Confirm your bank account by continuing and following instructions on the next screen.
    * Click continue on the Congratulations screen. (Ignore the statements about confirming deposits to this dummy account - this only happens for a live account.)
    * Click Confirm button on the next page (Confirm your bank account). Then follow Sandbox prompt and click Submit.
    * You should see **Your Bank Account in the United States Has Been Confirmed**

*Return to Overview tab in the Sandbox. Your account status should now be *Verified*

## Enable Website Payments Pro for your Sandbox account

* In Sandbox, click the **Merchant Tools** tab
* Under all-in-one payments, click **Sign Up** under **Website Payments Pro**
* Next to Submit Application, press **Go**
* Enter 111223333 when prompted for Account Owner Social Security Number
* Ignore the duplicate Social Security Number warning message at the to of the next page and continue with the application.
* You should see **Application Approved**
* Return to **Overview** tab and **Accept Billing Agreement** link in Getting Started panel (upper left corner of My Account Overview page).
* Click Agree to confirm billing agreement

!!! check "Sandbox Use of Website Pro is Free"
    There is actually no charge for using any of the services in the PayPal Sandbox. However, you will need to go through the same steps if you choose to create a live Website Pro Account. EXCEPT there will be a waiting period while PayPal actually reviews and approves your application.

!!! check "Applying for Website Payments Pro for a Live Account"
    When going through these steps for a live account, you should see a **Getting Started** panel in the upper left corner of your **My Account - Overview tab**. Once you verify your bank account information, you should be able to click on **Apply for Website Payments Pro** to begin the process. After submitting the requested info online - you will need to wait for an approval email reply from PayPal - in our experience this took approximately 3 days.
    !PayPal_Web_Pro_Apply.gif!*You will get an error message from the PayPal Payments server if you attempt to do a direct (Website Payments Pro style) transaction before your account is approved.*

## Configure API access

API Credentials are used to authenticate the connection between the PayPal payment gateway and the server where CiviContribute is installed. Two types of credentials are available - **API Signature** and **API Certificate**. The API Signature credential is recommended because it is easier to configure.

### Generate API Signature credential

* Login to your Sandbox Account.
* Click the **Profile** sub-tab from My Account.
* Click **My selling tools**.
* Click **API access** (under **Selling online** ).
* Under **Option 2 - PayPal API** , click on **2. Set up PayPal API credentials and permissions**
* Select **Request API Signature** option, click on **Agree and Submit**
* A page with your credential information is displayed. Record the values for:
    * API Username
    * API Password
    * API Signature

UPDATE May 20 - PayPal interface has changed in some cases. You may need to visit this url [https://www.paypal.com/businessprofile/mytools/apiaccess](https://www.paypal.com/businessprofile/mytools/apiaccess), (Profile, My selling tools, API Access), then click on View API Signature - under NVP/SOAP API Integration.

!!! information "Changing from API Certificate to API Signature"
    If you previously used an API Certificate with PayPal Pro, you will not be able to generate an API Signature until you delete the API Certificate. The interface for doing so from Canada in May, 2012 is:

* Login
* Click the Profile sub-tab from My Account
* Click Request API Credentials
* Under Option 1: PayPal API, click Set up PayPal API credentials and permissions
* Under **Option 2** - Request API credentials to create your own API username and password, click View API Certificate
* Click Remove, then Remove again
* Then under **Option 2** - Request API credentials to create your own API username and password, click Request API credentials
* Leave the default Request API Signature as your choice for the kind of API credential. Click Agree and Submit.

### Configure CiviContribute using API Signature

* Log into CiviCRM as an administrator.
* Select **Administer CiviCRM**.
* Select **Global Settings**.
* Select **Enable Components** and ensure that CiviContribute is enabled.
* Select **Administer CiviCRM &gt;&gt; Global Settings &gt;&gt; Payment Processors**
* Click **» New Payment Processor**
* Select **PayPal - Website Payments Pro** for Processor Type.
* Complete the fields in the **Processor Details for TEST Payments** section with the values from your **PayPal Sandbox account's View API Signature** screen:
    * Your API **Username**
    * The API **Password**
    * The API **Signature**
    * You can generally accept the default values for **Site URL, API URL and Button URL**.

| | Live Payments | Test Payments |
| --- | --- | --- |
| **Site URL** | [https://www.paypal.com/](https://www.paypal.com/) | [https://www.sandbox.paypal.com/](https://www.sandbox.paypal.com/) |
| **API URL** | [https://api-3t.paypal.com/](https://api-3t.paypal.com/) | [https://api-3t.sandbox.paypal.com/](https://api-3t.sandbox.paypal.com/) |
| **Button URL** | [https://www.paypal.com/en_US/i/btn/btn_xpressCheckout.gif](https://www.paypal.com/en_US/i/btn/btn_xpressCheckout.gif) | [https://www.paypal.com/en_US/i/btn/btn_xpressCheckout.gif](https://www.paypal.com/en_US/i/btn/btn_xpressCheckout.gif) |

!!! danger "During Initial Testing - Use Test (Sandbox) Account/API Info for Both TEST and LIVE Settings"

    CiviCRM allows you to store settings for connecting to both the Test and Live Payment Processor servers. When first setting up your site to accept online contributions, you should configure both TEST and LIVE server settings **with test values**. This will ensure that no LIVE transactions are submitted unintentionally. Once you have tested your site thoroughly, you can update the LIVE settings with the correct values for your live merchant account. The TEST settings will be used when you access an Online Contribution Page in **Test-drive Mode**.

    If you are having problems submitting transactions to the PayPal Sandbox - check PayPal's [Sandbox Status Page](http://www.paypaldeveloper.com/blog?blog.id=%20sb) to see if there is an system problem on their end.

!!! note "Credentials for LIVE Payments"
    Remember that when you are ready to configure CiviContribute for LIVE payments, you must generate new API credentials by logging in to your live merchant account (at [http://www.paypal.com](http://www.paypal.com). Then, enter these values in the Processor Details for LIVE Payments section of the Payment Processor configuration form. We recommend doing an initial LIVE contribution yourself and then checking for activity by logging back in to your PayPal account.

!!! tip "Changing Your API Access Method"
    If you have setup your API Access using the **API Certificate** method, and want to change to **API Signature** - you first need to Remove the existing credential. Click **View or Remove Credentials** from the API Setup page (My Account &gt;&gt; Profile &gt;&gt; API Access). Then click the Remove button. After confirmation, you are redirected to the API Setup page where you can click **Request API Credentials** to get a new credential.

## Configure Drupal error reporting

The PayPal SDK currently triggers a PHP warning during transaction processing. This warning does not affect processing - but you need to make sure that Drupal is configured to NOT display warnings on the screen.

* Navigate to Drupal **administer &gt;&gt; settings** or ( **administer &gt;&gt; site configuration &gt;&gt; error reporting** )
* In the Error Handling section, the Error Reporting drop-down should be set to **Write errors to log**. Update and save this setting if needed.

_NOTE: This is the recommended setting for production sites._

If the following warning is displayed after clicking **Make Contribution** - your Error Reporting setting is incorrect:

```
warning: Services_PayPal::getType(Services/PayPal/Type/Struct.php)
[CRM:function.getType]: failed to open stream: No such file or directory
in <drupal-root>/modules/civicrm/packages/Services/PayPal.php on line 50.
```

## Assign this processor to your Contribution or Event Registration page(s)

You must assign your new Payment Processor to your Contribution Page or Event Registration before you can test-drive them.

* For Contribution Pages - go to **Manage Contribution Pages » Configure » Contribution Amounts** and select your PayPal Website Pro processor, then click **Save**.
* For Event Registration - go to **Manage Events » Configure » Event Fees** and select your PayPal Website Pro processor, then click **Save**.

## Test-drive a CiviContribute online contribution page

* Login and navigate to Administer CiviCRM &gt;&gt; Configure Online Contribution Pages.
* Click on the referenced 'Test-drive' link for your page and make a contribution. In this mode, contributions records are saved with a **Test** flag. These are not shown under contact view - but you can view them by searching for **Test Contributions** under **CiviContribute » Find Contributions**.

!!! tip "Test Credit Cards"
    Use the PayPal Sandbox **Add a Credit Card** function to generate credit card numbers which are valid for testing.

## Apply for and configure your LIVE account

Once you are comfortable with your site's operation in testing mode, you will need to apply for a live PayPal Business Account [here](https://www.paypal.com/us/cgi-bin/webscr?cmd=_registration-run) - or upgrade an existing PayPal account to a Business Account. Approval may take several days.

The basic steps for obtaining and configuring your live Profile and settings are the same as for the Sandbox process described above - except that you will request the API Signature from your live merchant account login - and populate the Live settings in the Processor configuration screen.

Once you have your LIVE account configured, it is important that you submit a few live contributions prior to exposing your live online contribution page(s) to the public.

<!-- Source: setup/payment-processors/paypal-pro.md -->
