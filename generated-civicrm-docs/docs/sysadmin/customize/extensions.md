---
title: Extensions
category: explanation
topic: extensions
subtopic: sources-and-states
component: CiviCRM extensions
audiences:
- technical
- administrator
level: basic
journey_stage: overview
summary: Learn where CiviCRM extensions come from and what their states mean.
extensions: []
related: []
review_priority: low
review_notes: []
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: customize/extensions.md
destination_path: sysadmin/customize/extensions.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/customize/extensions/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Extensions

CiviCRM extensions allow you to install additional features and functionality for your site. Because they may update your database and affect how your CiviCRM site functions, best practice is to install any new extension on a test copy of your site first and verify that it functions as expected.

!!! tip "See Comparison of Add-On Formats"
    There are many ways to extend CiviCRM with benefits and drawbacks for each. This page covers "native" CiviCRM extensions - which are NOT restricted to use with a specific CMS. CiviCRM can also be "extended and customized" using CMS-specific extensions - e.g Drupal modules, Joomla components, and WordPress plugins. Refer to the [Packaging Formats](https://docs.civicrm.org/dev/en/latest/extensions/packaging/) page and to each CMS's documentation for more information.

!!! note "More information about CiviCRM extensions"
    To find out about **developing** CiviCRM extensions, see [Developer Guide: Writing Extensions](https://docs.civicrm.org/dev/en/latest/extensions/).

## Where do extensions come from?

Extensions come from various sources:

- **CiviCRM Core**: The official release of CiviCRM includes several "core extensions". These are always available.
- **[CiviCRM Extension Directory](https://civicrm.org/extensions)**: Members of the CiviCRM community may list extensions on the public directory. After a [general peer review](https://docs.civicrm.org/dev/en/latest/extensions/lifecycle/), these become available for in-app download.
- **Other Sources**: Administrators may manually add extensions from other sources. This may include:
    - New (*un-reviewed or un-released*) items from the [Extension Directory](https://civicrm.org/extensions).
    - Extensions from <https://lab.civicrm.org/extensions>
    - Extensions from `github.com`, `gitlab.com`, `codeberg.org`, or similar third-party system
    - Private extensions developed internally by the user-organization.

## Extension states: Enabled/Disabled/Uninstalled

The **Administer » System Settings » Extensions** page provides a list of extensions and their statuses.

Extensions need to be installed (the code files are on the server in the right place) and **Enabled** to be usable. Enabling an extension will create any data that the extension needs (e.g. new entity types, custom fields etc.).

Having been enabled you may **disable** and then **uninstall** an extension. Disabling means its functionality is not available, but typically any data it created is still there (even if it's unreachable). Typically, when you uninstall an extension, it will remove any data it created, however uninstalling does not delete the code files. Only after uninstalling an extension can you safely remove its code.

<!-- Source: customize/extensions.md -->
