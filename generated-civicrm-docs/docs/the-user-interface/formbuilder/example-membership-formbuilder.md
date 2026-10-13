---
title: Create a membership signup form with online payment
category: how-to
topic: contributions
subtopic: online-payment-form
component: FormBuilder
audiences:
- fundraising-manager
- operations-user
- administrator
- membership-manager
level: intermediate
journey_stage: plan-and-configure
summary: Create a public membership signup form with online payment using FormBuilder.
extensions:
- Stripe
related:
- ../../membership/defining-memberships.md#membership-types
- https://docs.civicrm.org/stripe/en/latest/
- https://docs.civicrm.org/user/en/latest/contributions/contribution-forms/#available-checkout-options
review_priority: low
review_notes:
- The final step says the public link lets people register for an event, although the page describes a membership signup form.
  The source wording is retained.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: the-user-interface/formbuilder/example-membership-formbuilder.md
destination_path: the-user-interface/formbuilder/example-membership-formbuilder.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/the-user-interface/formbuilder/example-membership-formbuilder/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Create a membership signup form with online payment

Use FormBuilder to create a public membership signup form with online payment. This lets you create flexible membership booking forms that do not follow the strict layout of the core Contribution Pages.

!!! note
    This example assumes the Stripe Payment Processor is installed on your CiviCRM system. See the [Stripe Extension](https://docs.civicrm.org/stripe/en/latest/) documentation. Other payment processors are available as [FormBuilder Checkout Options](https://docs.civicrm.org/user/en/latest/contributions/contribution-forms/#available-checkout-options).

## 1. Create the membership type

1. Navigate to **Administer > Membership > Membership Types**.
2. Ensure you have a suitable membership Type. For more information, see [Membership Types](../../membership/defining-memberships.md#membership-types).

## 2. Create the form

1. Navigate to **Administer > Customize Data and Screens > FormBuilder**.
2. On the Submission Forms tab, select **New Submission Form**.

## 3. Configure the form settings

Use the configuration pane on the left side to configure these settings:

- **Title**: Join As A New Member.
- **Permission**: Change to **Allow all users (including anonymous)**.
- **Page Route**: Give the form a public URL, such as civicrm/christmasfundraiser.
- **Frontend or Backend**: Choose **Frontend** so members of the public can access the form.
- **Post-Submit (Optional)**: To redirect people to a specific page after they submit the form, add the full web link (e.g., https://example.com) to the Post-Submit text box. Alternatively, add a **confirmation message** to display when they submit the form. Make sure you **save** the message if you add one.

## 4. Add the form fields

1. At the top of the Form, click the **+ symbol** and choose **Membership**. This creates a new tab called Membership 1.
2. On the **Membership 1** tab, under **Values** in the configuration pane on the left side:
    - Click the down symbol and choose Individual 1.
    - Click the **Add Value** select list and choose **Membership Type**. This lets you set a default value for the Membership Type. **Choose** the correct Membership Type for the form.
    - Click the **Add Value** select list and choose **Status**. Click on Status and choose **Pending**.
    - Click the **Add Value** select list and choose **Contribution Amount: Membership Amount**. Choose the Membership Amount required for the form.
3. At the top of the form, click the **+ symbol** and choose **Contribution**. This creates a new tab called Contribution 1, where you can add contribution fields.
4. On the **Contribution 1** tab, under **Values** in the configuration pane on the left side:
    - For **Contact** under the **Values** subheading, remove ‘Select Current User’ and change to Individual 1.
    - Click the **Add Value** select list and choose **Checkout Option**. This adds Checkout Option as a Value. Choose **Stripe Embedded Checkout**.
5. In the **Add** column, select **Checkout Details** and drag it onto the Contribution 1 section on the form Layout. Click the settings wheel by both **Contribution Amount** and **Contribution Source**, and choose **Remove field**.
6. Return to the **Individual 1** tab on the left panel. In the **Add** column, select **Contact Email(s)** and drag it onto the Individual 1 section on the form Layout. Configure the Email block:
    - Toggle **Multiple** so it changes to **Single**.
    - Select **is Primary**.
    - Select a **Location type**.
7. On the Individual 1 tab, scroll down to **Duplicate Matching**. Choose the appropriate Duplicate Matching rule; the default is ‘Email (reserved)’.
8. In the right pane, click the settings wheel symbol on each field in the form Layout and tick **Required**.

!!! tip
    You can also rename each Fieldset or Field, change background colors, and adjust other layout options by clicking the settings wheel symbols. On the Individual 1 tab, you can choose any other individual fields, such as address or phone number, and drag them onto the Individual 1 section on the form Layout.

## 5. Save and access the form

1. Click **Save** at the top right of the form screen.
2. Once saved, a **View Page** link appears next to the Save button. This is the link you will share with members of the public so they can register for the event.

The form can now be tested and adjusted as needed.

<!-- Source: the-user-interface/formbuilder/example-membership-formbuilder.md -->
