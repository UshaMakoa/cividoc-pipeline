---
title: CiviCRM themes
category: explanation
topic: system-administration
subtopic: civicrm-and-cms-themes
component: CiviCRM theming
audiences:
- technical
- operations-user
level: intermediate
journey_stage: plan-and-configure
summary: Understand how CiviCRM themes interact with CMS themes and how to select a CiviCRM theme.
extensions: []
related: []
review_priority: low
review_notes:
- The reference to v5.16 may need review for currency.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: customize/theme.md
destination_path: sysadmin/customize/theme.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/customize/theme/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# CiviCRM themes

CiviCRM includes base styles that give its user interface a standard look and feel. Your chosen CMS theme can also affect that appearance. Since v5.16, CiviCRM has supported installing a CiviCRM theme to load custom CSS, images, or other assets.

The theming system extends the existing ability to override or hide the default `civicrm.css` file. It provides separate options to disable the stock CiviCRM CSS on the front-end or back-end, giving system administrators more control over the appearance of CiviCRM for their users.

!!! note "CMS theming system interactions"
    CMS integrations have their own theming systems, which may interact or clash with a CiviCRM theme. When creating either kind of theme, consider how the chosen themes might interact. You can also use no CiviCRM theme and handle all style customization through the CMS theme.

## CMS integration

The CiviCRM theming subsystem lets you decide which CiviCRM theme to use. The available options depend on your CMS:

- For Drupal and Backdrop, you can choose a theme for front-end CiviCRM pages, such as Contribution Pages, and a theme for back-end pages, such as Advanced Search and Contact Summary.
- For WordPress and Joomla, you can choose a theme based on whether a page is a front-end or back-end page.

### How CiviCRM identifies front-end and back-end pages

For Drupal and Backdrop, the test is the presence of the `is_public` key on the menu route for the requested URL. For WordPress and Joomla, the test is whether the `is_frontend` configuration parameter is true.

## Installing a CiviCRM theme

To install a CiviCRM theme, download an extension that implements [`hook_civicrm_themes`](https://docs.civicrm.org/dev/en/latest/hooks/hook_civicrm_themes/). The [Shoreditch](https://civicrm.org/extensions/shoreditch) extension is one example.

After downloading and enabling the extension, go to **Administer -&gt; Customize Data and Screens -&gt; Display Preferences** and set the theme you want to use.

<!-- Source: customize/theme.md -->
