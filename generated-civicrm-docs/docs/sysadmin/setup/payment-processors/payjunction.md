---
title: PayJunction configuration
category: how-to
topic: system-administration
subtopic: payjunction
component: PayJunction payment processor
audiences:
- administrator
- fundraising-manager
level: advanced
journey_stage: plan-and-configure
summary: Set up and test a PayJunction payment processor, configure a live account, and review recurring contribution support.
extensions: []
related: []
review_priority: medium
review_notes:
- The recurring contribution instructions refer to CiviCRM1.9 and future versions of CiviCRM. Their current applicability
  needs review before readers rely on the database change.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/payment-processors/payjunction.md
destination_path: sysadmin/setup/payment-processors/payjunction.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/payment-processors/payjunction/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# PayJunction configuration

## Set up a test account

PayJunction has a sandbox account that is open to the public to use. To use it, follow these steps:

1. Set up your CiviCRM payment processor by going to Administer CiviCRM &gt;&gt; Global Settings &gt;&gt; Payment Processors &gt;&gt; New Payment Processor.
2. Select "PayJunction" as the payment processor type.
3. Enter the following details under Test Payment:
    * User Name = pj-ql-01
    * Password = pj-ql-01p
    * Site URL = [https://www.payjunctionlabs.com/quick_link](https://www.payjunctionlabs.com/quick_link)
    * Recurring Payments URL = leave blank, not used

## Run a test charge

1. Set up contribution page in CiviContribute (see [documentation](https://wiki.civicrm.org/confluence/display/CRMDOC/CiviContribute+Admin)).
2. Select your PayJunction payment processor as that contribution page's processor.
3. Run your contribution page in Test mode.
4. For the financial information, enter the following:
    * Card Type: Visa
    * Card Number: 4444333322221111
    * Code: 999
    * Expiration Date: Any date in the future
5. Make sure your charge is not huge - suggest something like $10.77, so it is easy to identify among the thousands of other test charges in PayJunction.

!!! warning "Repetitive charges"
    PayJunction will not allow you to charge the same amount to the same card within a 10 minute period, so keep this in mind when testing

### View your test charges

After submitting a charge via CiviContribution or other Civi module, you can view your charges by following these steps:

1. Go to [PayJunction Demo site](http://www.payjunctionlabs.com).
2. Click on "Merchant Login".
3. Login to the test account with Username: payjunctiondemo, Password: demo123.
4. In the top menu, go to "Batches/History", then click on "View Current Batch".
5. Recurring transactions can be found by going to "Recurring", then "Recurring Overview".

## Set up a live account

Follow the same steps above, but you'll need to get an account at [PayJunction](http://www.payjunction.com).

1. Set up a live merchant account at [http://www.payjunction.com/trinity/merchant-account/free_trial.action](http://www.payjunction.com/trinity/merchant-account/free_trial.action).
2. When you activate your PayJunction account, you will also be given your QuickLink Login and Password. Enter your QuickLink Login and Password under the Live Payment Details for your PayJunction Payment Processor.
3. If you did not print your QuickLink Login and Password, simply click on the following link for instructions to find your QuickLink Login and Password [http://www.payjunction.com/trinity/support/view.action?knowledgeBase.knbKnowledgeBaseId=589](http://www.payjunction.com/trinity/support/view.action?knowledgeBase.knbKnowledgeBaseId=589).

## Recurring contributions

The PayJunction payment processor will handle recurring contributions, but currently it will only create a single initial contribution in the CiviCRM database. PayJunction will keep processing recurring payments based on the schedule requested by the donor, but there is no call-back procedure to CiviCRM to let it know that follow on contributions or charges have been processed. [Phase2 Technology](http://www.phase2technology.com), contact Michael Morris at mmorris at phase2technology dot com) has developed a Drupal module that performs automatic processing of subsequent recurring contributions in the CiviCRM database, but the process is prone to getting out of synch if the actual charge from PayJunction fails, e.g., due to expired card, etc. So, the module assists in managing your recurring contributions, but there is still some manual effort involved.

!!! warning "Future handling of recurring contributions"
    Future versions of CiviCRM may have a better solution for handling recurring contributions from payment processors that don't have a charge call back feature, like PayJunction.

Because of the situation described, the version of the PayJunction processor that shipped with CiviCRM1.9 is not enabled for recurring contributions right out of the box. This was done in order to reduce confusion and to not lead users on that the PayJunction payment processor is a fully fledged, front to back, recurring contribution solution. However, if you are willing to accept the limitations described above, the processor is able to submit recurring contributions to PayJunction. To activate that functionality, a small change needs to be made to the CiviCRM database.

!!! warning "Enabling the PayJunction processor to handle recurring contributions"

    Run the following query on your CiviCRM database:

    _update civicrm_payment_processor set is_recur=1 where name='PayJunction';_

    Once this is done, a checkbox will appear on your Contribution Amount set up page that allows you to enable Recurring contributions for that Contribution page.

<!-- Source: setup/payment-processors/payjunction.md -->
