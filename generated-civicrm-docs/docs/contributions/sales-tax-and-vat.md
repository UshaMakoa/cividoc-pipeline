---
title: Sales tax and VAT
category: how-to
topic: contributions
subtopic: configuration
component: CiviContribute
audiences:
- fundraising-manager
- operations-user
- administrator
level: intermediate
journey_stage: plan-and-configure
summary: Enable Sales Tax or VAT, create a tax Financial Account, and assign it to a Financial Type.
extensions: []
related: []
review_priority: low
review_notes:
- The source spells the Financial Types menu path as "Adminster > CiviContribute > Financial Types"; the spelling is preserved
  because an incorrect menu path could hinder the task.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: contributions/sales-tax-and-vat.md
destination_path: contributions/sales-tax-and-vat.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/contributions/sales-tax-and-vat/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Sales tax and VAT

If your organization charges Sales Tax or VAT, enable this feature.

## Enable Sales Tax/VAT

Go to **Administer > CiviContribute > CiviContribute Component Settings** and check the **Enable Tax and Invoicing** box.

On this screen, you can also set:

- **Tax Term** — the text your organization wants to use for the relevant Sales Tax or VAT.
- **Tax Display Settings** — how your organization wants to display the Tax/VAT:
    - No breakdown, total only
    - Shows as inclusive price - $120 (includes $20 tax)
    - Shows as exclusive price - $100 + $20 tax

![CiviContribute Component settings with the tax term listbox at the bottom.](../img/enable_tax_fields.png)

## Add a Financial Account for Sales Tax/VAT

Once Sales Tax/VAT is enabled, create one or more Financial Accounts for Tax/VAT at **Administer > CiviContribute > Financial Account**. Scroll to the bottom of the page and click **Add Financial Account**.

To create the Sales Tax Account, set **Financial Account Type** to **Liability**. Select **Enabled** and **Is Tax**, and specify the **Tax Rate**. If you use **Quick Books**, the **Account Type Code** should be set to **SALESTAX**. **Accounting Code** should be based on the organization's specific Accounting Codes.

![screenshot](../img/salestaxaccount4.png)

## Assign the account to a Financial Type

After creating the Financial Account, go to **Adminster > CiviContribute > Financial Types**. Find the Financial Type this Sales Tax applies to and click **Accounts**, then **Assign Account**.

![List of financial accounts.](../img/assignaccount2.png)

For **Financial Account Relationship**, choose **Sales Tax Account is**. In the **Financial Account** field, select your **Sales Tax** account. Click **Save.**

![screenshot](../img/civicontribute-sales-tax-add-account.png)

The **Sales Tax Financial Account** will appear with the other **Financial Accounts** for that **Financial Type**.

![screenshot](../img/salestaxadded2.png)

For more advanced configuration with accounting software packages like QuickBooks, involve your organization's bookkeeper or accountant in setting up your **Financial Types** and **Financial Accounts**.

<!-- Source: contributions/sales-tax-and-vat.md -->
