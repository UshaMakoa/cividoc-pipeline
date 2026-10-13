---
title: Configuring PayPal API Certificate credentials
category: reference
topic: system-administration
subtopic: paypal-api-certificate-credentials
component: CiviContribute
audiences:
- administrator
- technical
- fundraising-manager
level: advanced
journey_stage: reference-and-troubleshooting
summary: Preserve the documented API Certificate procedure and its stated support limitation.
extensions: []
related: []
review_priority: high
review_notes:
- The source says this method is not supported in CiviCRM v1.8 and later but then gives instructions for using it; readers
  could be unable to complete the procedure.
- The procedure refers to configuration screens and settings whose applicability is unclear. Its instructions have been left
  unchanged.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/payment-processors/paypal-pro-part4.md
destination_path: sysadmin/setup/payment-processors/paypal-pro-part4.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/payment-processors/paypal-pro-part4/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# Configuring PayPal API Certificate credentials

## Generating and configuring PayPal API Certificate credentials

**Note that this method is not supported in CiviCRM v1.8 (and later)**

**API Certificates** are an alternate authentication method for interacting with PayPal's servers. Follow these procedures if you wish to use this method rather than the default API Signature credential.

## Generate and download API Certificate credential

* Login to your Sandbox or Live Account.
* Click the Profile sub-tab from My Account.
* Click the **API Access** link in the left column (under **Account Information** )
* Click **request an API certificate** under the **Direct Access** section.
* Fill in the **API Certificate Request** form
* Record the **API Username** and the **API Password** selected (you will need this to create your API Profile and configure CiviCRM later)
* Click Generate Certificate and then Download on the next page
    * A certificate file will be downloaded to your local machine (file name will be cert_key_pem.txt)

## Create your API Profile and configure CiviCRM with your PayPal configuration settings

!!! danger "During Initial Testing - Use Test (Sandbox) Account/API Info for All Settings"
    CiviCRM allows you to store settings for connecting to both the Test and Live Payment Processor servers. When first setting up your site to accept online contributions, you should configure both TEST and LIVE server settings **with test values**. This will ensure that no LIVE transactions are submitted unintentionally. Once you have tested your site thoroughly, you can update the LIVE settings with the correct values for your live merchant account. The TEST settings will be used when you access an Online Contribution Page in **Test-drive Mode**.

The final steps in getting ready to use CiviContribute with PayPal in **TEST MODE** are to create and store an **API Profile** on your server, and enter settings in the Payment Processor section of the CiviCRM configuration file. This is actually a pair of files which are used to authenticate your server to the PayPal transaction server.

* Create or locate a directory which can be used for your API Profile files. During this step, your webserver must have read/write access to the path - but for security it should preferably be a directory that is NOT below your web root. Note down the path to this directory - this will be your **TEST_CERT_PATH**.
* Navigate to **Administer CiviCRM » Global Settings » Enable Components** and make sure CiviContribute is enabled.
* Now go to the **Global Settings » Payment Processor**.
* Set your Payment Processor value as either **PayPal** (for Website Payments Pro) or **PayPal Express**.
* Set both your TEST and live **..._Certificate Path** settings to the directory noted above. **Include a trailing slash on both path settings.**

    !!! danger
        **Make sure the Test and Live Username fields are blank before saving this screen.** If these fields are not empty, you will get an error from PayPal when attempting to make a test or live contribution.

* Open your CiviCRM configuration file in a text editor (civicrm.settings.php)
* Set both your TEST and live **..._PASSWORD** settings to the **API Password** you used when requesting your sandbox certificate.

    ```php
    define( 'CIVICRM_CONTRIBUTE_PAYMENT_TEST_PASSWORD' , 'fo$y7#233u' );
    // ...
    define( 'CIVICRM_CONTRIBUTE_PAYMENT_PASSWORD' , 'fo$y7#233u' );
    ```

* Now log back to your site (with Administer CiviCRM permission) and go to **Administer CiviCRM**
* Click on the new item in the CiviContribute section of the control panel - **Create PayPal API Profile**. (If this item is not visible, check your CiviCRM configuration file to make sure the Payment Processor setting is PayPal or PayPal_Express, and the Enable Components setting lists CiviContribute.)
* Select **sandbox** as your API Environment, enter the API Username you used to request your sandbox digital certifcate, and browse to the certificate file you downloaded from PayPal earlier.
* After submitting the form, you should see a status message with your Profile **PAYMENT_KEY** value. You may also want to verify that the *.cert and *.ppd files have been created in your CERT_PATH.

    ```
    // example API Profile files
      82dd81ec5b571959b3d36b73bd30d9fa.cert
      82dd81ec5b571959b3d36b73bd30d9fa.ppd
    ```

* Go back to you CiviCRM configuration file, and enter your Profile **PAYMENT_KEY** value in both TEST and LIVE settings.

    ```php
    define( 'CIVICRM_CONTRIBUTE_PAYMENT_TEST_KEY' , '82dd81ec5b571959b3d36b73bd30d4o2' );
    // ...
    define( 'CIVICRM_CONTRIBUTE_PAYMENT_KEY' , '82dd81ec5b571959b3d36b73bd30d4o2' );
    ```

* Finally, it is recommended that you set the directory permissions to READ-ONLY for your API Profile directory (CERT_PATH).

<!-- Source: setup/payment-processors/paypal-pro-part4.md -->
