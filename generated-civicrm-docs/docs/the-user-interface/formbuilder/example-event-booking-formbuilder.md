---
title: 'Example: use FormBuilder to create an event booking form with online payment'
category: how-to
topic: contributions
subtopic: online-payment-forms
component: FormBuilder
audiences:
- fundraising-manager
- operations-user
- administrator
- event-manager
level: intermediate
journey_stage: plan-and-configure
summary: Create a public event booking form with online payment using FormBuilder.
extensions: []
related: []
review_priority: medium
review_notes:
- The instructions say to add Participant in both Step 2 and Step 4. It is unclear whether the second action is necessary
  or would add another Participant; both instructions are retained.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: the-user-interface/formbuilder/example-event-booking-formbuilder.md
destination_path: the-user-interface/formbuilder/example-event-booking-formbuilder.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/the-user-interface/formbuilder/example-event-booking-formbuilder/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Example: use FormBuilder to create an event booking form with online payment

This example shows how to use FormBuilder to create a public form that lets people book onto a CiviCRM event with an online payment. It allows you to create flexible event booking forms that do not follow the strict layout of the core Event booking forms.

!!! note
    This example assumes the Stripe Payment Processor is installed on your CiviCRM system. See the [Stripe Extension](https://docs.civicrm.org/stripe/en/latest/) documentation. Other payment processors are available as [FormBuilder Checkout Options](https://docs.civicrm.org/user/en/latest/contributions/contribution-forms/#available-checkout-options).

## Step 1: Create the event

1. Navigate to **Administer &gt; Events &gt; New Event**.
2. Create a New Event with a **Title** ‘Christmas Fundraiser’, Start **date** and time, Event **type**, and a default role of attendee. On the **Fees** tab, add the required Fee options with labels and amounts. Then **Save** the event.

## Step 2: Create the form

1. Navigate to **Administer &gt; Customize Data and Screens &gt; FormBuilder**.
2. On the **Submission Forms** tab, click **New Submission Form** link.
3. The form will automatically include the Individual and some fields (first name and last name). At the top of the Form, click the **+ symbol** and choose **Participant** to enable the individual to register for an event.

## Step 3: Configure form settings

Use the configuration pane on the left side to configure these settings:

* **Title**: Register For Our Christmas Fundraiser.
* **Permission**: Change to **Allow all users (including anonymous)**.
* **Page Route**: Give the form a public URL, such as civicrm/christmasfundraiser.
* **Frontend or Backend**: Choose the **Frontend** option so the form can be accessed by members of the public.
* **Post-Submit (Optional)**: To redirect people to a specific page after the form has been submitted, add the full web link (e.g., https://example.com) to the Post-Submit text box. Alternatively, add a **confirmation message** to display when they submit the form. Make sure you **save** the message if you add a confirmation message.

## Step 4: Add the form fields

1. At the top of the Form, click the **+ symbol** and choose **Participant**.
2. Then, at the top of the form, click the **+ symbol** and choose **Contribution**. This creates a new tab called Contribution 1, which allows you to add contribution fields.
3. Click the **Participant 1** tab. In the configuration pane on the left side, under **Values**, set the following values:
    * For the **Contact** field, remove ‘Select Current User’ and change to **Individual 1**.
    * For **Event**, choose the event you created in Step 1.
    * For **Status**, choose **Pending (incomplete transaction)**.
4. In the **Add** column, select **Contribution Amount:Christmas Fundraiser** and drag it onto the **Participant 1** section on the form Layout. This adds the Fee options for the event to the form.
5. Click the **Contribution 1** tab. In the configuration pane on the left side, under **Values**, set the following values:
    * For the **Contact** field, remove ‘Select Current User’ and change to **Individual 1**.
    * Click the **Add Value** select list and choose **Checkout Option**. This adds Checkout Option as a Value. Choose the **Stripe Embedded Checkout option** from the drop-down.
6. In the **Add** column, select **Checkout Details** and drag it onto the **Contribution 1** section on the form Layout.
7. On the Contribution 1 section on the right panel, click the **settings wheel** by both fields **Contribution Amount** and **Contribution Source** and choose **Remove field** for both.
8. Click back on the **Individual 1** tab on the left panel. In the **Add** column, select **Contact Email(s)** and drag it onto the Individual 1 section on the form Layout. Configure the Email block as follows:
    * Toggle the word **Multiple** so it changes to **Single**.
    * Select **is Primary**.
    * Select a **Location type**.
9. While still on the Individual 1 tab, scroll down to **Duplicate Matching**. Choose the appropriate Duplicate Matching rule; the default is ‘Email (reserved)’.
10. In the right pane, click the settings wheel symbol on each field in the form Layout and tick the **Required** option.

!!! tip
    You can also rename each Fieldset or Field, change background colors, and adjust other layout options by clicking the settings wheel symbols. On the Individual 1 tab, you can choose any other individual fields, such as address or phone number, and drag them onto the Individual 1 section on the form Layout.

## Step 5: Save and access the form

1. Click the **Save** button at the top right of the form screen.
2. Once saved, a **View Page** link will appear next to the Save button. This is the link you will share with members of the public so they can register for the event.

The form can now be tested and adjusted as needed.

<!-- Source: the-user-interface/formbuilder/example-event-booking-formbuilder.md -->
