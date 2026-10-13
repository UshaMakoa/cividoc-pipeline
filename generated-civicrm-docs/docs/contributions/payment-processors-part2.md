---
title: Set up a payment processor
category: how-to
topic: contributions
subtopic: configuration-and-testing
component: Contributions
audiences:
- fundraising-manager
- operations-user
- administrator
- membership-manager
level: intermediate
journey_stage: plan-and-configure
summary: Configure a payment processor and find the card details given for testing.
extensions: []
related: []
review_priority: medium
review_notes:
- The setup instructions begin with an unfinished condition, “If no Payment Processors have been configured for your site,”
  so it is unclear whether the steps also apply when a processor is already configured.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: contributions/payment-processors-part2.md
destination_path: contributions/payment-processors-part2.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/contributions/payment-processors-part2/
civicrm_version:
- latest
last_modified: '2026-10-06'
---

# Set up a payment processor

You can configure one or more Payment Processors for your CiviCRM installation.

You will then need to assign an active Payment Processor to each Online Contribution Page and each paid Event. If no Payment Processors have been configured for your site,

1. Go to **Administer > System Settings > Payment Process** and click on **New Payment Processor**.
2. Choose the Payment Processor Type from the dropdown list.
3. Assign a descriptive name to this processor configuration and an optional description. The name will show up when you want to select a Payment Processor for a Contribution Page or Event. A description can be useful if you are configuring multiple merchant accounts for different chapters or sub-organizations within your site with the same Payment Processor type.
4. Select a Financial Account. You probably want to have a separate Financial Account for each Payment Processor, but your bookkeeper or accountant will be able to advise you best on this. The Financial Account you select records where the money gets deposited, not the sort of revenue you anticipate it receiving. The Contribution, Membership and Event money you receive will also get recorded into different revenue Financial Accounts as well, based on the configuration of contribution pages and events. For a partial explanation of how this works, see *Double Entry Accounting* in Wikipedia.
5. Make the Processor active so that it is available for use with paid Events and Online Contribution Pages. If the Processor allows you to collect credit card information on your website, your staff will also be able to use it to submit credit card Contributions and payment for Memberships and Events.
6. If you have multiple Payment Processors, the one you set as the default will be selected when you create a Contribution or Event Page or process a credit card payment in the admin area, although you will be able to override that selection manually.
7. Fill in the appropriate live payment and test payment details for your Payment Processor. Note that the fields in these sections vary according to the Payment Processor type selected.

You will need to do some further set up on the actual payment gateway but that is beyond the scope of this book and should be documented by your gateway.

Once done, the Processor will be available in your paid Events and Contribution pages.

## Test payments and dummy payment processors

For the purposed of testing, you can configure dummy Payment Processors.

If you do use a dummy Payment Processor, or are using any payment pages in test mode, the following card details should work:

- Card type: Visa
- Card number 4111 1111 1111 1111
- CVV: any three digits
- Expiry: any date in the future

<!-- Source: contributions/payment-processors-part2.md -->
