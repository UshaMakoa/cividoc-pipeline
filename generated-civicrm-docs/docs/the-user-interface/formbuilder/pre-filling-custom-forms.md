---
title: Pre-filling forms and using secret links
category: how-to
topic: searchkit
subtopic: url-defaults-and-secret-links
component: FormBuilder
audiences:
- administrator
- operations-user
level: intermediate
journey_stage: manage-and-automate
summary: Set default form values through URL parameters and send contacts secret links to pre-filled forms.
extensions: []
related:
- ../../searching/relative-date-formats.md
review_priority: low
review_notes:
- The instruction to format date values without special symbols conflicts with the examples containing hyphens and a period.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: the-user-interface/formbuilder/pre-filling-custom-forms.md
destination_path: the-user-interface/formbuilder/pre-filling-custom-forms.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/the-user-interface/formbuilder/pre-filling-custom-forms/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Pre-filling forms and using secret links

To make your forms quicker to fill out and encourage higher response rates, your organisation can create personalized, pre-filled form links. By utilizing URL parameters or specialized security settings, you can pass known default information safely to your users or let them fill out personal records securely without requiring a standard user account login.

## Set defaults using URL parameters

You can automatically fill out specific text or choice selections on a submission form when a user lands on the page by attaching parameters directly to your form's web link.

1. Identify the field key names you have used in your FormBuilder setup.
2. Build your sharing link by taking your form's published page route and adding a question mark, followed by the field key and the desired default text. For example: `https://yourorganisation.org/civicrm/volunteer-signup?status=interested`
3. To specify precise dates in a URL default parameter, format the value without spaces or special symbols using one of the following variations:
   * `receive_date=2026-06-30`
   * `receive_date=20260630`
   * `receive_date=20260630105600` (to specify exact hour, minute, and second values)
   * Relative dates: `receive_date=this.month`

   (See [the list](../../searching/relative-date-formats.md))

## Configure forms for secret access links

If you want to send form links to contacts via email that dynamically identify who they are—similar to standard CiviCRM checksum behavior—you must adjust your form permissions to support secure anonymous access.

1. Navigate to **Administer** > **Customize Data and Screens** > **FormBuilder** and open your form.
2. In the left-side **Form Settings** pane, click the **Permission** selection box.
3. Select **Generic: Anyone with secret link**. This configuration explicitly signals to CiviCRM that the incoming web traffic will only be authorized if it arrives with a unique security token attached to the link.
4. Under the **Placement** section, find the **Expose To** setting and select **Message Tokens**. This makes your form visible as an interactive mail-merge selection when designing broadcast communications.

## Generate and distribute the secret link

Once the form permissions are ready, you can insert individual secret links dynamically into bulk mailings or workflow templates.

1. Go to your mailings manager or template builder to write a message to your supporters.
2. Open the **Tokens** list in your message composer editor.
3. Locate your newly created form in the token list. Because you exposed the form to "Message Tokens" in FormBuilder, it will appear as a selectable merge choice.
4. Insert the token into your email text or as the destination address for a "Update Your Info" button.
5. When CiviCRM sends out the final email delivery, it automatically replaces that token with a uniquely generated, encrypted link for each recipient. When clicked, the link matches the recipient to their database profile and safely pre-populates their existing records without exposing your system to general public tampering.

<!-- Source: the-user-interface/formbuilder/pre-filling-custom-forms.md -->
