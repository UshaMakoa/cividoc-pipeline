---
title: Invoicing
category: how-to
topic: contributions
subtopic: contributions
component: CiviContribute
audiences:
- fundraising-manager
- operations-user
- administrator
- communications-manager
level: basic
journey_stage: everyday-tasks
summary: Invoicing works for all Financial Types and Completed and Pending Contribution Statuses and has to be enabled. To
  enable Invoicing go to Administer > CiviContribute > CiviContribute Component Settings and check the Enable Tax and Invoicing
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: contributions/invoicing.md
destination_path: contributions/invoicing.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/contributions/invoicing/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Invoicing

Invoicing works for all Financial Types and Completed and Pending
Contribution Statuses and has to be enabled. To enable Invoicing go
to **Administer > CiviContribute > CiviContribute Component Settings** and
check the **Enable Tax and Invoicing** box.

In this screen you can set certain settings for Invoices as well:

-   add a Prefix for Invoices and Credit Notes
-   the interval of days, weeks, or years until Due Date
-   customized Notes or Standard Terms you want to appear on your
    Invoice

![screenshot](../img/civicontribute_comp_settings.png)

## Creating an Invoice

Once Invoicing has been enabled, you can easily Email or Print Invoices
for Complete or Pending Contributions from a contact's **Contribution**
Tab.

1.  Go to Contact's Contribution tab
2.  View the record you want to create an Invoice for

![List of contributions for a specific contact.](../img/contribution_summary.png)

Once you are viewing the record you have the option to **Print Invoice** or **Email Invoice**. Printing an Invoice will download a pdf and Emailing an Invoice will provide an additional Options screen.

![The print Invoice and email Invoice buttons are at the bottom of the contrbution screen.](../img/contributiion_view_Screen.png)

Emailing Invoices:
1.  Once you have chosen the Email Invoice option you have options before sending:

-   From Email Address

-   Type an additional message

![E-mail message.](../img/email_invoice.png)

!!! note
    When you send an Invoice by email it is not possible to add CC / BCC.
    If you do want to have the possibility to CC / BCC (although with explicit fields, not implicit), there is an extension for that: [invoicehelper](https://lab.civicrm.org/extensions/invoicehelper).

Here is an example of a printed Invoice. Invoices can be customized.

![Invoice example.](../img/invoice.png)

## Invoice Customization

The out of the box template code populates the Company Name, Address,
and Website Information listed on the top right of Invoices come
directly from the Organization Address and Contact Info. To make any
edits to this information, you can access it at **Administer Console >
Configuration Checklist > Organization Address and Contact Info**.

The look of the Invoice and Invoice image can be edited and customized
in **Administer > Communications > Message Templates > System Workflow Messages > Contributions-Invoice.**

To change the image on the Invoice you will need to modify the code see below, replacing the image source (img src).

```html
<td><img src = "{$resourceBase}/i/civi99.png" height = "34px" width
= "99px"></td>
```
For more advanced configuration with accounting software packages like
QuickBooks, you should involve your organization's bookkeeper or
accountant in setting up your Financial Types and Financial Accounts.
See *Accounting Integration* and the Wiki Page for more information.

<!-- Source: contributions/invoicing.md -->
