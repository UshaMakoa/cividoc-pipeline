---
title: Switching Smarty
category: how-to
topic: system-administration
subtopic: version-selection-and-configuration
component: Smarty
audiences:
- technical
- administrator
level: intermediate
journey_stage: plan-and-configure
summary: Choose and configure a supported Smarty version for a CiviCRM installation.
extensions: []
related: []
review_priority: medium
review_notes:
- The guidance says administrators can choose a version and that earlier versions will be removed in the future, but the warning
  and version matrix say CiviCRM 6.12+ supports only Smarty v5.
- The guidance says Smarty v5 became primary in CiviCRM 5.78+, while the milestones and version matrix show it as primary
  from CiviCRM 5.74.
- The Smarty v2 sub-path entry says its end date is TBD, while the milestones and version matrix give CiviCRM 6.11 as the
  last version supporting v2.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: misc/switch-smarty.md
destination_path: sysadmin/misc/switch-smarty.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/misc/switch-smarty/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Switching Smarty

## Background

In CiviCRM, the <em>Smarty</em> templating engine is central building-block. It is used for both:

* __Web Pages__: Many of the screens in CiviCRM are generated from Smarty templates.
* __Email Communication__: Email blasts and automated alerts may be customized and fine-tuned using Smarty templates.

Smarty templates come from many places, including CiviCRM (_core_), third-party extensions, and local CiviCRM customizations (_users_).

During 2023-2025 (v5.66 - v6.11), the project transitioned from Smarty v2 to v5. In the transitional period, CiviCRM (core)
was compatibile with multiple versions of Smarty. Site-administrators could choose which version to enable.

!!! warning "Beginning in 2026, the transition period is ended. Newer releases (CiviCRM v6.12+) only support Smarty v5."

## Choose a version

As an administrator, you can choose the version of Smarty. This decision should be influenced by a few factors:

* __CiviCRM Version__:

    In CiviCRM v5.78+, _primary_ support is provided for Smarty v5. This is the default for _new installations_ and _quality assurance_.
    There is _secondary_ support for Smarty v2 and v4. (These work, but they aren't tested as much.)

    Details vary by version. For full details, see the [version matrix](#version-matrix).

* __Extensions__:

    If you use third-party extensions, then you should consider their compatibility.

    In general, extensions released before 2023 require Smarty v2. Extensions released during the
    transitional period (2023-2025) will often support newer versions of Smarty. But this is
    not guaranteed and ultimately depends on the specific extension/version/developer.

    <!-- FIXME: Here, it might be a good idea to link to some appendix/appendices to help assess your specific extensions.
    Maybe that's a table with some important extension names/versions/dates. Maybe that's some technial cues. -->

* __Email Templates__:

    If you have customized the "System Message Templates", then you need to assess the customizations yourself. Try changing the Smarty version (to
    taste) and re-testing the customization.

    <!-- FIXME: Here, it might be good to link to some appendix/appendices to help assess your templates. Maybe there are examples of
    old-syntax/new-syntax/bridge-syntax. Maybe there's a linter/extension/script to scan your msg tpls. -->

Eventually, you will need to choose Smarty v5 -- earlier versions will be removed in the future. However, during the transition period, you can
consider a few subjective questions like:

* How many extensions or custom templates do you have? With more customizations, you may need a more careful or phased process.
* Do you have a _staging system_ (or _development system_)? Can you update and test that first?
* Do you prefer to upgrade incrementally? You might find it easier to make one large jump (Smarty v2=>v5) or multiple, smaller jumps (Smarty v2=>v4=>v5).

<!-- NOTE: IMHO, this level of care ^^^ is mostly driven by the fact that we don't have good tools/processes/advice on the fundamentals.
If we improve the tooling/advice on the fundamentals, then maybe we drop the subjective ballyhoo. -->

## Configure the version

To configure the Smarty version, you must update `civicrm.settings.php`. The exact text will depend on your environment. Here are two examples:

!!! example "Use Smarty v5 on a TAR/ZIP-based system (Backdrop, Joomla, Standalone, WordPress)"

    ```php
    if (!defined('CIVICRM_SMARTY_AUTOLOAD_PATH')) {
     define('CIVICRM_SMARTY_AUTOLOAD_PATH',
       $civicrm_root . '/packages/smarty5/Smarty.php'
     );
    }
    ```

!!! example "Use Smarty v2 on a Composer-based system (Drupal 9/10/11)"

    ```php
    if (!defined('CIVICRM_SMARTY_AUTOLOAD_PATH')) {
     define('CIVICRM_SMARTY_AUTOLOAD_PATH',
       dirname($civicrm_root) . '/civicrm-packages/Smarty/Smarty.class.php'
     );
    }
    ```

Let's examine how these parts may vary:

* The base path needs to match your file-layout. This depends on the CMS and deployment method. Typical scenarios:

    | Scenario | Base Path |
    | -- | -- |
    | TAR/ZIP deployment<br/> <small>(_Backdrop, Drupal 7, Joomla, Standalone, WordPress_)</small> | `$civicrm_root . '/packages/'` |
    | Composer deployment<br/> <small>(_Drupal 9/10/11_)</small> | `dirname($civicrm_root) . '/civicrm-packages/'` |
    | If in doubt, use an absolute path | `'/var/www/example.com/modules/civicrm/packages/'` |

* The sub-path indicates the Smarty version. Possible values include:

    | Version | Sub-Path | Comment |
    | -- | -- | -- |
    | Smarty v5 | `smarty5/Smarty.php` | _Available in CiviCRM 5.71+_ |
    | Smarty v4 | `smarty4/vendor/autoload.php` | _Available in CiviCRM 5.71+_ |
    | Smarty v3 | `smarty3/vendor/autoload.php` | _Available in CiviCRM 5.67 - 5.77_ |
    | Smarty v2 | `Smarty/Smarty.class.php` | _Available in all versions. (End date TBD.)_ |

* The constant `CIVICRM_SMARTY_AUTOLOAD_PATH` is for CiviCRM v5.71+. On earlier versions (5.67-5.70),
  the analogous constant was `CIVICRM_SMARTY3_AUTOLOAD_PATH`.

## Appendix: Milestones {:#milestones}

* __CiviCRM 5.67__: Introduce Smarty __v3__ (_opt-in_).
* __CiviCRM 5.70__: Use Smarty __v3__ on _new_ installations. QA bias toward __v3__.
* __CiviCRM 5.71__: Introduce Smarty __v4__ and __v5__ (_opt-in_).
* __CiviCRM 5.72__: Use Smarty v4 on _new_ installations. QA bias toward __v4__.
* __CiviCRM 5.74__: Use Smarty v5 on _new_ installations. QA bias toward __v5__.
* __CiviCRM 5.78__: Drop support for Smarty __v3__.
* __CiviCRM 6.5__: Use Smarty __v5__ by default (unless your settings _explicitly_ say otherwise).
* __CiviCRM 6.11__: Last version with __v2__ and __v4__.
* __CiviCRM 6.12__: Smarty __v5__ only.

## Appendix: Version Matrix {:#version-matrix}

For each version of CiviCRM, you can ask a few questions:

1. What is the _primary_ Smarty version used for ___new installations___ and ___quality-assurance___?
2. What is the _fallback_ Smarty version used for ___older, unconfigured___ installations?
3. What are _all_ the available versions of Smarty?

<style type="text/css">
.waffle .th-1{background-color:#ffffff;color:#000000;text-decoration:underline;}
.waffle .th-2{background-color:#ffffff;color:#000000;}
.waffle .is-civicrm{background-color:#ffffff;text-align:left;color:#000000;}
.waffle .default-v2{background-color:#c9daf8;color:#000000;}
.waffle .default-v3{background-color:#a4c2f4;color:#000000;}
.waffle .default-v4{background-color:#6d9eeb;color:#000000;}
.waffle .default-v5{background-color:#1155cc;color:#ffffff;}
.waffle .is-yes{background-color:#b6d7a8;color:#000000;}
.waffle .is-no{background-color:#f4cccc;color:#000000;}
.waffle .bold {font-weight:bold;}
.waffle th, .waffle td {text-align:center; vertical-align:bottom;word-wrap:break-word; padding: 1em;}
.waffle tbody th:nth-child(3), .waffle tbody td:nth-child(3) { border-right: 1px dotted #444; }
</style>

<table class="waffle" cellspacing="0" cellpadding="0">
<thead>
<tr>
<th class="th-1 bold">CiviCRM</th>
<th class="th-1 bold" colspan="1">Primary</th>
<th class="th-1 bold" colspan="1">Fallback</th>
<th class="th-1 bold" colspan="4">Available</th>
</tr>
</thead>
<tbody>
<tr>
<td class="is-civicrm">CiviCRM &lt;=5.66</td>
<td class="default-v2">v2</td><td class="default-v2">v2</td>
<td class="is-yes bold">v2</td><td class="is-no"><!-- No --></td><td class="is-no"><!-- No --></td><td class="is-no"><!-- No --></td>
</tr>
<tr>
<td class="is-civicrm">CiviCRM 5.67 - 5.69</td>
<td class="default-v2">v2</td><td class="default-v2">v2</td>
<td class="is-yes bold">v2</td><td class="is-yes">v3</td><td class="is-no"><!-- No --></td><td class="is-no"><!-- No --></td>
</tr>
<tr>
<td class="is-civicrm">CiviCRM 5.70</td>
<td class="default-v3">v3</td><td class="default-v2">v2</td>
<td class="is-yes">v2</td><td class="is-yes bold">v3</td><td class="is-no"><!-- No --></td><td class="is-no"><!-- No --></td>
</tr>
<tr>
<td class="is-civicrm">CiviCRM 5.71</td>
<td class="default-v3">v3</td><td class="default-v2">v2</td>
<td class="is-yes">v2</td><td class="is-yes bold">v3</td><td class="is-yes">v4</td><td class="is-yes">v5</td>
</tr>
<tr>
<td class="is-civicrm">CiviCRM 5.72 - 5.73</td>
<td class="default-v4">v4</td><td class="default-v2">v2</td>
<td class="is-yes">v2</td><td class="is-yes">v3</td><td class="is-yes bold">v4</td><td class="is-yes">v5</td>
</tr>
<tr>
<td class="is-civicrm">CiviCRM 5.74 - 5.77</td>
<td class="default-v5">v5</td><td class="default-v2">v2</td>
<td class="is-yes">v2</td><td class="is-yes">v3</td><td class="is-yes">v4</td><td class="is-yes bold">v5</td>
</tr>
<tr>
<td class="is-civicrm">CiviCRM 5.78 - 5.82</td>
<td class="default-v5">v5</td><td class="default-v2">v2</td>
<td class="is-yes">v2</td><td class="is-no"><!-- No --></td><td class="is-yes">v4</td><td class="is-yes bold">v5</td>
</tr>
<tr>
<td class="is-civicrm">CiviCRM 6.0 - 6.4</td>
<td class="default-v5">v5</td><td class="default-v2">v2</td>
<td class="is-yes">v2</td><td class="is-no"><!-- No --></td><td class="is-yes">v4</td><td class="is-yes bold">v5</td>
</tr>
<tr>
<td class="is-civicrm">CiviCRM 6.5 - 6.11</td>
<td class="default-v5">v5</td><td class="default-v5">v5</td>
<td class="is-yes">v2</td><td class="is-no"><!-- No --></td><td class="is-yes">v4</td><td class="is-yes bold">v5</td>
</tr>
<tr>
<td class="is-civicrm">CiviCRM &gt;= 6.12</td>
<td class="default-v5">v5</td><td class="default-v5">v5</td>
<td class="is-no"></td><td class="is-no"><!-- No --></td><td class="is-no"></td><td class="is-yes bold">v5</td>
</tr>
</tbody>
</table>

## See also

* __[dev/core#4146: Upgrade Smarty to Smarty3+](https://lab.civicrm.org/dev/core/-/issues/4146)__: Geneal discussion.
  As a discussion, some of its details are transitory. However, it is fairly broad.
* __[PR #27547: More Smarty 3 prep](https://github.com/civicrm/civicrm-core/pull/27547)__: Example demonstrating
  common syntax issues in updating templates from Smarty v2 to v3+.

<!-- Source: misc/switch-smarty.md -->
