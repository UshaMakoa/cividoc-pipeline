---
title: Configuring CiviCRM to use the default Drupal editor
category: how-to
topic: system-administration
subtopic: drupal-default-editor
component: CiviCRM Drupal integration
audiences:
- technical
- administrator
- communications-manager
level: intermediate
journey_stage: plan-and-configure
summary: Configure CiviCRM to use Drupal input formats and WYSIWYG profiles for rich-text editing.
extensions: []
related: []
review_priority: low
review_notes:
- The page refers to CiviCRM 3.4.2/4.0.2 and Drupal 7, and describes one approach as currently the only way to manage files;
  verify whether these statements still apply.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: integration/drupal/wysiwyg.md
destination_path: sysadmin/integration/drupal/wysiwyg.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/integration/drupal/wysiwyg/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Configuring CiviCRM to use the default Drupal editor

CiviCRM starting with versions 3.4.2/4.0.2 include a feature that allows administrators of sites running Drupal and the [WYSIWYG API](http://drupal.org/project/wysiwyg) module to use Drupal input formats (text formats in Drupal 7), including their associated WYSIWYG profiles, as the rich-text editor in CiviCRM. The editor can then look and act the same when users edit rich text in CiviCRM as it does in native Drupal forms.

## Required or useful modules

These modules are required or helpful when using the Default Editor option:

* [WYSIWYG API](http://drupal.org/project/wysiwyg)
* [IMCE](http://drupal.org/project/imce)
* [IMCE WYSIWYG bridge](http://drupal.org/project/imce_wysiwyg)
* [Pathologic](http://drupal.org/project/pathologic)

## Installation and configuration

1. Go to Administer > Customize Data & Screens > Display Preferences (screen and form configuration).
1. For WYSIWYG Editor, choose "Drupal Default Editor".
1. Optionally, change the default input format selected for forms with a rich-text control.

CiviCRM will then use Drupal's method of rendering and processing rich-text editor controls. WYSIWYG API must be installed for this to work; the option does not appear if it is not installed. Input formats configured to use a WYSIWYG profile will use that profile when selected. You can also enable or disable the rich-text editor and change input formats as you would in a native Drupal context.

## _Input_ formats are really _output_ formats

Drupal and CiviCRM process and store text differently, even when CiviCRM uses the "Drupal Default Editor" option. Drupal does not generally process input before saving it to the database. It saves raw input and applies input formats—whose input filters modify text—when the text is **output**. Some advanced input filters depend on special tags in the raw input that are translated into HTML only on output.

CiviCRM does not know which input format was used for a field. It has no single point where it can process WYSIWYG-related fields just before output, nor a practical way to store the input format used for a field. As a result, the Drupal Default Editor for CiviCRM applies input formats **before** saving input to the database. The output is as expected, but you **can't go back** to the raw input.

If you edit a record with a WYSIWYG form after changing its input format, CiviCRM will not know which format you previously selected: the default editor will be selected. Advanced filters and WYSIWYG buttons that depend on manipulating template information in the raw HTML will not work because only the processed output is stored.

This is especially noticeable if you use an input format such as the default Filtered HTML without a WYSIWYG profile assigned to a field. In native Drupal, you edit it as plain text, optionally add HTML, and line breaks and links are converted to HTML when displayed. When you return to the field in CiviCRM after navigating away:

1. The default input format chosen in the CiviCRM preferences screen will be selected, regardless of which input format you previously selected.
1. Even if Filtered HTML is selected, the non-WYSIWYG text area will display HTML. The input format has already been applied to the raw code: newlines have been converted to paragraphs, links have been created, and so on.

## IMCE as a file browser

If your WYSIWYG profiles are configured to use IMCE as a file browser, they will work when you edit rich-text fields in CiviCRM. You need [IMCE](http://drupal.org/project/IMCE) and [IMCE WYSIWYG bridge](http://drupal.org/project/imce_wysiwyg) installed. See the README file in IMCE WYSIWYG bridge for installation instructions.

!!! tip

    Using Drupal Default Editor along with an IMCE WYSIWYG profile is currently the only way to allow users to browse, upload and otherwise manage files on your server for use with mailings, event descriptions, etc.

## Absolute paths

When using this option for CiviMail, take special care to ensure absolute URLs are output. The [pathologic](http://drupal.org/project/pathologic) module is recommended for this task. Consider creating an input format specifically for CiviMail because it has special considerations. Apply pathologic as an input filter for that format; see the pathologic documentation for details.

One additional step ensures that Pathologic treats all resources as local and converts them to absolute URLs:

1. Go to the input formats screen (admin/settings/filters/list).
1. Click "configure" on the format, then click the "configure" tab.
1. In the Pathologic filter settings, enter your site's base path in the "Also considered local" textbox. If your site is in the root, enter "/" (no quotes). If it is in a subdirectory, such as `http://www.example.com/drupal`, enter "/drupal".

<!-- Source: integration/drupal/wysiwyg.md -->
