---
title: Custom templates and PHP files
category: how-to
topic: system-administration
subtopic: custom-templates
component: CiviCRM
audiences:
- operations-user
- technical
level: intermediate
journey_stage: plan-and-configure
summary: Store custom templates outside the main CiviCRM fileset and review how custom PHP files affect upgrades.
extensions: []
related: []
review_priority: medium
review_notes:
- The custom PHP files section does not identify which directory “this directory” refers to.
- The advice about extra template files cites versions 3.4.3 / 4.0.3; its current applicability needs review.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/directories-part2.md
destination_path: sysadmin/setup/directories-part2.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/directories-part2/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# Custom templates and PHP files

## Custom templates

1. Create a folder, for example, drupal/sites/all/civicrm_templates. Add its full system path to the custom templates section on the directories page.
2. To modify a template, copy its path and file into your custom templates directory. For example, copy civicrm/templates/CRM/History/Selector/Activity.tpl to drupal/sites/all/civicrm_templates/CRM/History/Selector/Activity.tpl. You can then modify the custom template.

CiviCRM searches your custom template directory and uses a template it finds there instead of the stock template. Your custom templates will not be overwritten when you upgrade CiviCRM.

!!! tip "Add Custom JavaScript Functions to Templates"

    As of version 3.4.3 / 4.0.3 CiviCRM will also check your Custom Templates Directories for files to append to a given template. These "extra" files should be named using the root template file name + 'extra.tpl'. For example, if you want to append some jQuery logic (or crmAPI calls, or ....) to the CiviEvent Dashboard - add them to this file in your custom templates directory tree: _CRM/Event/Page/Dashboard.extra.tpl_.

    Note that you will need to start your "extra" custom file with the Smarty {literal} tag and then use {/literal} if you need to use any Smarty code or variables.

!!! note "Case configuration files"

    If you are using the CiviCase component, your [Case configuration files](https://wiki.civicrm.org/confluence/display/CRMDOC/CiviCase+Configuration) should also be stored under your custom templates path so they are not affected by upgrades. These should be placed in _<custom templates path>/CRM/Case/xml/configuration_.

## Custom PHP files

These are similar to custom templates in theory to php files that sit in this directory will over-ride the php files in the main CiviCRM fileset. They will not be overwritten when an upgrade takes place (which keeps your changes but can cause problems if the file has been upgraded and you don't port the changes across to your customised file).

<!-- Source: setup/directories-part2.md -->
