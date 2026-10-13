---
title: Creating contribution forms using FormBuilder
category: how-to
topic: contributions
subtopic: formbuilder
component: FormBuilder Contributions
audiences:
- fundraising-manager
- operations-user
- administrator
- technical
level: intermediate
journey_stage: plan-and-configure
summary: Set up a contribution form with FormBuilder and configure its checkout and confirmation options.
extensions:
- FormBuilder
- Stripe
- Paypal
- HelloAsso
- Authnet
related: []
review_priority: medium
review_notes:
- The page describes this functionality as new and gives version-specific availability and payment processor support as of
  the time of writing.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: contributions/contribution-forms.md
destination_path: contributions/contribution-forms.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/contributions/contribution-forms/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Creating contribution forms using FormBuilder

!!! tip "New functionality"
    Creating Contribution Forms using FormBuilder is a new alternative to [Contribution Pages](contribution-pages.md). You can help contribute to development by raising issues or new feature requests on the [CiviCRM Issue Tracker](https://lab.civicrm.org/dev/core/-/issues).

FormBuilder can create forms for making Contributions to your organisation, from a simple donation form to a complex checkout experience that includes Donations, Paid Memberships and/or Event Registrations.

## Getting started

- FormBuilder Contributions is available in CiviCRM 6.14. You must upgrade to at least this version to get started.
- Install a Payment Processor extension that supports FormBuilder Contributions. At time of writing, the main integrations with support are [Paypal Complete Payments](https://civicrm.org/extensions/paypal) and [Stripe](https://civicrm.org/extensions/stripe-payment-processor), though more should be coming in the following months. See [Available Checkout Options](#available-checkout-options) below for details.
- Configure a Payment Processor connection for your chosen Payment Processor. The steps may vary between processors: you may have to log in to a connection page or copy an API key from your account with the Payment Processor.
- To edit forms through the UI, enable the FormBuilder extension if you haven't already.
- Enable FormBuilder Contributions functionality for your site at **Administer > CiviContribute > CiviContribute Component Settings**.
- Familiarity with [using FormBuilder](../the-user-interface/formbuilder/what-is-formbuilder.md) will help, particularly if you want to make a complex form with multiple entities, such as Memberships or Event Registrations.

## Starter donation page

After you enable FormBuilder Contributions, a simple donation form should be available at `https://my.example.site/civicrm/donate`.

By default, the form uses the **Pay Later** Checkout Option. You will probably want to either:

- Set it to use your preferred Checkout Option, such as Stripe Embedded Checkout; or
- Add Checkout Option as a field on the form so users can choose an option.

You can add fields to the Individual entity or other fields on the Contribution, such as Contribution Source. You can also rearrange the inputs and/or add Rich Content elements to prettify your form.

You should now be ready to test using the form.

## Using test mode

To use Test Mode for Contributions created through the form, add the special parameter `testMode=1` to the form URL, for example `https://my.example.site/civicrm/donate?testMode=1`.

This uses the Test connection configured for your selected Checkout Option / Payment Processor.

## Making a recurring contribution

To allow users to set up a Recurring Contribution, use the *Recur Period* field on the Contribution entity. You can set a fixed value on the left hand side or add it as a field input to let users pick an option.

## Adding a thank you page / message

Configure a thank you page / message using the Confirmation Type setting on the Form Settings tab.

You can show a confirmation message or redirect to another URL for a thank you page. You can include tokens from the form submission to personalise these messages / redirect url—for example, a message like `Thank you {Individual1.0.first_name}!` or a URL like `https://my.example.site/thank-you?contribution_id={Contribution1.0.id}`.

## Minimum requirements for a new form

To take payments through a form:

- Include a Contribution entity on the form.
- Include the Checkout Option field on the Contribution, either with a fixed value on the left hand side or as a user input on the right hand side.
- Include the Checkout Details field on the Contribution. This should always be a user input on the right hand side.
- Set `Allowed Actions` for the Contribution to either `Create` to create a new Contribution or `Update` to make payments for a previously created contribution, but not both.
- Include at least one Price Field, either as a fixed value on the left hand side or as a form input on the right hand side. The Price Field can be on the Contribution or a linked Membership or Participant entity. The starter form uses the simplest Contribution Amount field.

When creating a form, it may help to start by cloning the `civicrm/donate` form, which should already have all the minimum requirements set.

## Available Checkout Options

| Option | Extension | Status | Notes |
| --- | --- | --- | --- |
| Stripe Embedded Checkout | [Stripe](https://civicrm.org/extensions/stripe-payment-processor) | Working | Requires version 6.16+ |
| Stripe Hosted Checkout | [Stripe](https://civicrm.org/extensions/stripe-payment-processor) | Working | Requires version 6.16+ |
| Paypal Complete Payments | [Paypal](https://civicrm.org/extensions/paypal) | Working | New extension |
| HelloAsso | [HelloAsso](https://lab.civicrm.org/extensions/helloasso-payment-processor) | Working | Requires version 2.1.1+ |
| Authnet AcceptJS | [Authnet](https://lab.civicrm.org/extensions/authnet) | Working in sandbox | https://lab.civicrm.org/extensions/authnet/-/merge_requests/45 |
| Authnet Credit Card | [Authnet](https://lab.civicrm.org/extensions/authnet) | Working in sandbox | Renders form fields from Quickform metadata https://lab.civicrm.org/extensions/authnet/-/merge_requests/45 |

<!-- Source: contributions/contribution-forms.md -->
