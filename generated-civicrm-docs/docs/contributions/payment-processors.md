---
title: Payment processors
category: explanation
topic: contributions
subtopic: selecting-a-processor
component: Contributions
audiences:
- fundraising-manager
- operations-user
- administrator
- technical
level: intermediate
journey_stage: plan-and-configure
summary: Compare payment processor characteristics and support before choosing one for CiviCRM.
extensions: []
related: []
review_priority: medium
review_notes:
- The sentence beginning “Many processors that allow you to manage Recurring Contributions” is incomplete; its intended meaning
  is unclear.
- The statements about SSL certificate costs and setup may need review.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: contributions/payment-processors.md
destination_path: contributions/payment-processors.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/contributions/payment-processors/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Payment processors

CiviCRM connects to a variety of different Payment Processors. Out-of-the-box, it comes with support for approximately 15 Payment Processors. Many other community contributed processors are available to download from the CiviCRM [Extensions Directory](https://civicrm.org/extensions).

Additional Payment Processors may also be available from third-party sites.

Community contributed processors are not supported by CiviCRM but there is no reason why they should not be just as reliable as the out-of-the-box Processors. If you do use a community contributed Processor, be sure that you have access to adequate technical support for that Processor, either in house, from the author of the Payment Processor, or from a trusted third party.

Browse a [comparison of the available Payment Processors](https://docs.civicrm.org/sysadmin/en/latest/setup/payment-processors/#comparison) in the System Administrator Guide.

## Selecting a payment processor

Payment providers differ in cost, suitability for your use case, and availability. If possible, talk to similar nearby organisations that use CiviCRM about their experiences with Payment Processors. You can also configure more than one Payment Processor and give constituents the option to choose the one they prefer.

### Onsite vs offsite processors

With an onsite Payment Processor, the user enters credit card details directly on your site. With an offsite processor, the user goes to another site to make the payment and then returns to yours. You can typically brand the payment site to a limited extent—for example, with your organisation name, logo and colours—but the workflow is less seamless, and a percentage of people tend not to complete the payment.

As well as providing a more seamless experience for end users, onsite Payment Processors allow site admins to process card payments (Contributions, Membership Fees, Event Payments, etc.) from CiviCRM admin pages.

The disadvantage of processing payments directly on your site is that you will need to have an SSL certificate to ensure the security of the users card details as they are transmitted over the internet. SSL certificates cost money (typically an annual fee) and they are not straight forward to set up. Your hosting provider or system administrator can help you here. You may also want to read the *Security* section in the *Initial set up* chapter of this book.

CiviCRM never stores credit card details on your server. It only transmits them to the payment processor.

### Regional availability

For many countries there are no Payment Processors written that support their currencies. If you do not have Payment Processor support for the Payment Processor you want to use, consider writing your own processor or asking a third party to do so.

### Merchant account vs built-in

Most organizations that accept credit card payments will have their own merchant account through a bank, however these usually have monthly charges which may not suit smaller organizations (though they generally have lower percentage payments). You can expect to pay a fee for the merchant account and to the Payment Processor, though these may be bundled together. Some, like World Pay and Paypal, do not require separate merchant accounts.

### Support for recurring contributions

Support for Recurring Contributions and auto-renewing memberships is an important feature for many organizations. However not all of the Payment Processors available for CiviCRM support this feature. Many processors that allow you to manage Recurring Contributions from within CiviCRM but PayPal and Authorize.net require you to log into their own portals to manage Recurring Contributions. Some, like Moneris, have "incomplete" support.

If you have configured a Payment processor that includes Recurring Payments as a feature, you can enable Recurring Contributions in your Contribution Page settings. For more details on page-specific configuration, refer to the [Online Contributions](contribution-pages.md#setting-up-a-contribution-page-full-details) chapter.

### Cost

Determining which Payment Processor is least expensive depends on the number and average size of the transaction you process. So the question is not which processor is the cheapest, but which is the cheapest for you. Commission percentages, per-transaction charges, and fixed monthly charges vary along with set-up costs. In general, if you process many transactions, an account with a monthly fee but low commission might be a good option. On the other hand, if you expect infrequent transactions, it is best to avoid monthly fees and accept paying a higher commission.

### Usability

If you do not collect the credit card information yourself on your own site, you need to consider whether the payment workflow is intuitive and easy to use. Paypal Standard is often confusing to end users because they are not sure whether or not they need to create a PayPal account. Such a barrier can result in decreased contributions.

## Support

CiviCRM supports the processors that are incorporated into the core codebase, to the extent that they ensure they do not break in upgrade - support and enhancements of community contributed processors are generally expected to come from the community.

## Writing a new payment processor

If you cannot find a suitable Payment Processor, or want to use a specific payment provider that is not currently supported by CiviCRM, you can write a new Payment Processor integration, or pay someone else to do so.

<!-- Source: contributions/payment-processors.md -->
