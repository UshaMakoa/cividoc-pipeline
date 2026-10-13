---
title: The Bootstrap base theme
category: explanation
topic: system-administration
subtopic: cms-theme-approaches
component: CiviCRM integration
audiences:
- technical
- membership-manager
level: intermediate
journey_stage: extensions-and-integrations
summary: Explains approaches to using the Bootstrap framework with CiviCRM and the Drupal Bootstrap base theme.
extensions: []
related: []
review_priority: medium
review_notes:
- The statements that there has been no WordPress or Joomla activity to date, and that CiviCRM.org is now built using a Bootstrap
  subtheme, may be dated.
- The reference to a PTP subtheme being "available here" has no link, although a clone command is provided.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: integration/drupal/bootstrap-css.md
destination_path: sysadmin/integration/drupal/bootstrap-css.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/integration/drupal/bootstrap-css/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# The Bootstrap base theme

!!! note

    The purposes of this page are:

    * to disambiguate the use and discussion of the "bootstrap framework" with relation to CiviCRM
    * provide a starting point for common practices amongst developers using the Drupal bootstrap base theme
    * to inspire and move forward the vision of using the bootstrap framework as a standard/default UI for CiviCRM

The [Bootstrap Framework](http://getbootstrap.com/) calls itself the most popular HTML, CSS, and JS framework for developing responsive, mobile first projects on the web.

CiviCRM has a vision of adopting the 'Bootstrap Framework' as the standard for the UI in the future.

There are many different approaches to incorporating bootstrap into CiviCRM that are in progress.

## Modifying CiviCRM core

These changes will work regardless of which CMS (Drupal, WordPress, Joomla) you are using.

For a 2014 Google Summer of Code (GSoC) project, a student documented how to use the Drupal Bootstrap base theme for a Drupal/CiviCRM site. See the [CiviCRM blog post](https://civicrm.org/blog/teja/bootstrap-ui-one-small-step-for-civicrm) about that project, a CiviCRM wiki entry, [Bootstrap UI for CiviCRM](https://wiki.civicrm.org/confluence/display/CRMDOC/Bootstrap+UI+for+CiviCRM) and the [GitHub repo](https://github.com/amilineni/civicrm-core/).

## Drupal

The Drupal approaches only work if you are using Drupal as your CMS.

Within Drupal, there are different approaches as well. Most of them are based on the Drupal base theme called "[bootstrap](https://www.drupal.org/project/bootstrap)" that incorporates a lot of the bootstrap framework into Drupal and provides a reasonable model of how to use other bits as well.

### Public-facing pages only

One approach is to only focus on a custom Drupal theme to be applied to public facing pages. This approach makes no effort to use the bootstrap theme to display the administrative screens of CiviCRM. Instead, it focuses on ensuring that your contribution, membership, event, petition, etc. pages are properly displayed in the mobile-friendly bootstrap way.

This approach makes sense if:

* Your CiviCRM installation is separate from your main web site and you want to ensure that the public pages are consistent with your main web site, or
* You run both CiviCRM and your main web site from the same Drupal installation and you want to ensure all non-CiviCRM pages are mobile friendly, but you want to keep CiviCRM admin pages using a theme that works well in a desktop browser.

You can use [themekey](https://www.drupal.org/project/themekey) (and [themekey_civicrm](https://www.drupal.org/project/themekey_civicrm)) or civicrm_theme (in core) to choose different themes for different parts of CiviCRM.

[CiviCRM.org is now built using a subtheme of the Drupal Bootstrap base theme.](https://github.com/civicrm/civicrm-website-org/tree/master/drupal/sites/all/themes/civicrm_bootstrap) It appears to focus on public facing pages and is designed for a full scale web site.

In addition, PTP has developed a base subtheme, available here that is specifically focused on ensuring public facing pages work well and is designed to be sub-themed to match a variety of different layouts: git clone git://git.progressivetech.org/powerbase/civiresponsive.git

## WordPress

No activity to date.

## Joomla

No activity to date.

<!-- Source: integration/drupal/bootstrap-css.md -->
