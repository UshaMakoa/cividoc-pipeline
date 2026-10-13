---
title: Create a donation form with FormBuilder
category: how-to
topic: searchkit
subtopic: formbuilder-donation-form
component: FormBuilder
audiences:
- administrator
- fundraising-manager
- event-manager
- operations-user
level: intermediate
journey_stage: plan-and-configure
summary: Create a public donation form with FormBuilder and a Stripe checkout option.
extensions:
- Stripe
related:
- https://docs.civicrm.org/stripe/en/latest/
- https://docs.civicrm.org/user/en/latest/contributions/contribution-forms/#available-checkout-options
- ../../contributions/contribution-forms#starter-donation-page
review_priority: medium
review_notes:
- The instructions say to add a Participant and describe the saved form as a way to register for an event, although the page
  is about creating a donation form. These statements need review before they are changed.
- The section numbering jumps from Step 3 to Step 5.
- The confirmation-message instruction contains the unclear phrase “when. they submit the form.”
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: the-user-interface/formbuilder/example-donation-formbuilder.md
destination_path: the-user-interface/formbuilder/example-donation-formbuilder.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/the-user-interface/formbuilder/example-donation-formbuilder/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Create a donation form with FormBuilder

This example describes how to use FormBuilder to create a public Donation form. It allows you to create flexible online donation forms that do not follow the strict layout of the core Contribution forms.

!!! note
    This example assumes the Stripe Payment Processor is already installed. See the [Stripe Extension](https://docs.civicrm.org/stripe/en/latest/) documentation. Other payment processors are available as [FormBuilder Checkout Options](https://docs.civicrm.org/user/en/latest/contributions/contribution-forms/#available-checkout-options).

## Step 1: Create the form

1. Navigate to **Administer &gt; Customize Data and Screens &gt; FormBuilder**.
2. On the **Submission Forms** tab, click **New Submission Form** link.
3. The form will automatically include the Individual and some fields (first name and last name). At the top of the Form, click the **+ symbol** and choose **Participant** to enable the individual to register for an event.

## Step 2: Form settings

Use the configuration pane on the left side to configure the following settings for your form:

- **Title**: Make a Donation
- **Permission**: Change to **Allow all users (including anonymous)**.
- **Page Route**: give the form a public URL, such as civicrm/support-us

!!! note
    There is already a packaged form called **New Donation** with the URL civicrm/donate so you'll need to edit that form if you want your donation page to use that URL. There is more information about this on the [Contribution Forms](../../contributions/contribution-forms.md#starter-donation-page) page.

- **Frontend or Backend**: Choose the **Frontend** option so the form can be accessed by members of the public.
- **Post-Submit (Optional)**: If you wish to redirect people to a specific page after the form has been submitted, add the full web link (e.g., https://example.com) to the Post-Submit text box. Alternatively, add a **confirmation message** to be displayed when. they submit the form. Make sure you **save** the message if you add a confirmation message.

## Step 3: Add the form fields

1. At the top of the Form, click the **+ symbol** and choose **Contribution**. This creates a new tab called **Contribution 1**. In the configuration pane on the left side, under **Values**, set the following values:
    - For the **Contact** field, remove ‘Select Current User’ and change to **Individual 1**.
    - Then click the **Add Value** select list and choose **Checkout Option**. This will add Checkout Option as a Value. Choose the **Stripe Embedded Checkout option** from the drop-down.
2. In the **Add** column, select **Checkout Details** and drag it onto the **Contribution 1** section on the form Layout.
3. On the Contribution 1 section on the right panel, click the **settings wheel** for **Contribution Source** and choose **Remove field**.
4. Click back on the **Individual 1** tab on the left panel. In the **Add** column, select **Contact Email(s)** and drag it onto the Individual 1 section on the form Layout. Configure the Email block as follows:
    - Toggle the word **Multiple** so it changes to **Single**,
    - select **is Primary**,
    - select a **Location type**.
5. While still on the Individual 1 tab, scroll down to **Duplicate Matching**. Choose the appropriate Duplicate Matching rule, the default is ‘Email (reserved)’.
6. In the right pane, click the settings wheel symbol on each field in the form Layout and tick the **Required** option.

!!! tip
    You can also rename each Fieldset or Field, change background colors, and adjust other layout options by clicking the settings wheel symbols. On the Individual 1 tab, you can choose any other individual fields, such as address or phone number, and drag them onto the Individual 1 section on the form Layout.

## Step 5: Save and access the form

1. Click the **Save** button at the top right of the form screen.
2. Once saved, a **View Page** link will appear next to the Save button. This is the link you will share with members of the public so they can register for the event.

The form can now be tested and adjusted as needed.

<!-- Source: the-user-interface/formbuilder/example-donation-formbuilder.md -->
