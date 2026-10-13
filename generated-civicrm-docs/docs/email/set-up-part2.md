---
title: Allow people to sign up for mailing lists online
category: how-to
topic: mailings
subtopic: online-subscriptions
component: CiviMail
audiences:
- communications-manager
- administrator
- technical
level: intermediate
journey_stage: plan-and-configure
summary: Make a mailing list available online and offer a subscribe link or profile for sign-up.
extensions: []
related: []
review_priority: medium
review_notes:
- The WordPress URL guidance refers to installations before version 5.13.
- The Drupal Webform guidance points to a wiki page whose currency has not been established.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: email/set-up-part2.md
destination_path: email/set-up-part2.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/email/set-up-part2/
civicrm_version:
- latest
last_modified: '2026-10-06'
---

# Allow people to sign up for mailing lists online

CiviCRM makes it possible for people to sign themselves up for your mailing lists online.

To allow this, you must designate the group as a mailing list. If you didn't do this when you created the Group, go to **Contacts** > **Manage Groups**. Click **Settings** on the group that holds your mailing list recipients and check the Mailing List next to Group Type. You must also change the Visibility to Public Pages.

For this to work for users who don't have a log-in to your CiviCRM, you must ensure that anonymous users in Drupal have the following permission checked: "Access CiviMail subscribe/unsubscribe pages."

## Use the subscribe link

One way to allow users to subscribe to an email list online is by directing them to:

- Drupal: <i>example.org</i>/civicrm/mailing/subscribe
- Backdrop: <i>example.org</i>/civicrm/mailing/subscribe
- WordPress with [clean URLs](https://docs.civicrm.org/sysadmin/en/latest/install/wordpress/#enabling-cleaner-urls-for-wordpress): <i>example.org</i>/civicrm/mailing/subscribe?reset=1
- WordPress without clean URLs (the default for CiviCRM instances installed before version 5.13): <i>example.org</i>/civicrm?page=CiviCRM&q=civicrm/mailing/subscribe&reset=1
- Joomla: <i>example.org</i>/administrator/index2.php?option=com_civicrm&task=civicrm/mailing/subscribe&reset=1

You and anyone who accesses this link can subscribe to the available mailing list groups.

## Use a profile

Alternatively, you can use [profiles](../organising-your-data/profiles.md) to collect more information from people who sign up to your mailing list.

For example, you could create a new Profile called Newsletter Sign-up. Add to this profile the fields that you'd like website visitors who want to join your mailing list to fill out. Each of the fields in the profile must have its Visibility set to Public Pages.

For each field you include, you can choose whether it is required or optional for people filling out the public form. The one exception is that the profile must include an email field that is required. This is so that an email can be sent to the person to confirm that they wanted to sign up for the mailing list. Until they confirm, they will have a status of "Pending" in the mailing list group.

There are two ways to display the profile publicly:

1. Share a link directly. Return to the listing of profiles (at **Administer > Custom Data and Screens > Profiles**) and click **More** to the far right of your profile. Click **Use Profile-Create Mode**. Your browser will open up the public page; you can publish this link to allow users to sign up for your mailing lists.
2. Embed this set of fields as a form in your website. Return to the listing of profiles (at **Administer > Custom Data and Screens > Profiles**) and click **More** to the far right of your profile. Select **HTML Form Snippet**. This will open a window in your browser that has a box with HTML code in it. Copy and paste the contents of the box into a page on your website. Website visitors will be able to sign up to your mailing lists on this page.

Alternatively, for WordPress you can display the form publicly by using a shortcode. On any WordPress Page, click the **CiviCRM** button above the editor. For **Page Type** select **Profile**. On the next drop-down that appears, select the name of the profile that you have created. Select **Edit** on the radio button option just below the drop-downs, so that you give users access to edit data in your database (i.e. to add their email address and name to your database). Click **Insert Form** and the shortcode will be added to the editor.

## Use a Webform (Drupal)

Many Drupal site administrators prefer to use a webform instead of a profile to create their newsletter sign-up, because it provides additional features such as advanced spam control and flexible theming. For more information see:

[http://wiki.civicrm.org/confluence/display/CRMDOC/Webform+CiviCRM+Integration](http://wiki.civicrm.org/confluence/display/CRMDOC/Webform+CiviCRM+Integration)

## Add people to your mailing list group by using a profile

To get a user automatically added to your mail list group(s) when they fill out your Newsletter Sign-up form (CiviCRM profile), you have two options:

**Option A:** On the profile, you can add a field for the mailing lists groups that you want users to be able to sign up for. Go to the profile's fields and click **Add Field**. For Field Name, select Contacts. When the possible selections load in the second field, select Group(s). In Field Label, you can leave "Group(s)" or you may want to change it to something more intuitive to your website visitors such as "Newsletter Sign-up." Visibility for this field must be set to Public Pages. When the profile displays publicly, this field will show check boxes for all Mailing List Groups that have their Visibility set to Public Pages. This way users can add themselves to all of your Mailing List Groups that they want to by putting a tick on the appropriate checkboxes.

**Option B:** Go to the profile settings. In the Advanced Settings section, select your desired Mailing List Group for **Add new contacts to a Group?**. Now when users fill out your form, they will be automatically added to this group.

## Mailing list confirmation workflow

For this to work, first make sure that you have put a tick on the desired **Enable Double Opt-in** options in **Administer > Administration Console > CiviMail Component Settings**.

After people subscribe to mailing list groups &mdash; via the subscribe link or a profile &mdash; CiviCRM will automatically send them an email asking them to confirm their subscription. Until they click the confirmation link in the email, their contact information will appear in CiviCRM with their group subscription set to Pending. When they confirm, CiviCRM will automatically change their group subscription status to Added and they will be sent a welcome message.

!!! note
    When users subscribe to multiple groups at once, a confirmation email is
    sent for each group separately.

<!-- Source: email/set-up-part2.md -->
