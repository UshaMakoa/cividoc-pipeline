---
title: Configure AdminTools for CiviCRM in Joomla
category: how-to
topic: system-administration
subtopic: extension-configuration
component: CiviCRM Joomla! integration
audiences:
- technical
- administrator
level: intermediate
journey_stage: plan-and-configure
summary: Review Joomla extension interactions and add the AdminTools exceptions described for CiviCRM.
extensions:
- AdminTools
related: []
review_priority: medium
review_notes:
- The source writes “directory” inside the code-formatted path `/media/civicrm/ directory`; the wording is retained because
  the intended path is unclear.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: integration/joomla/index-part2.md
destination_path: sysadmin/integration/joomla/index-part2.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/integration/joomla/index-part2/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# Configure AdminTools for CiviCRM in Joomla

The availability of additional modules to extend and modify CiviCRM behavior is fairly limited. However, Joomla integrators have full access to the CiviCRM API's and hook system, and there are a number of 3rd party tools designed to solve specific problems and make customizations easier.

For more information, developers can refer to the [3rd party module listing](https://wiki.civicrm.org/confluence/display/CRMDOC/Joomla!+Extensions+for+CiviCRM+%283rd+party%29) and the [Developer Guide](https://docs.civicrm.org/dev/en/latest).

## Configuration and conflicts with common extensions

For the most part, CiviCRM is self-contained inside Joomla and does not interact with other extensions except those intended to integrate with it, such as the 3rd party extensions noted earlier, or occasionally system plugins that affect the entire site. Some extensions may require configuration adjustments for CiviCRM to work properly. The following is a common Joomla extension to review.

### AdminTools

[AdminTools](https://extensions.joomla.org/extension/admin-tools/) is a site security extension that includes a web application firewall and .htaccess builder, among other things. The .htaccess builder, available in the Pro version, provides user interface options for building an .htaccess file to harden your site security.

Some standard hardening options need adjustments to work with CiviCRM. In particular, the .htaccess file includes directives that prevent direct access to all files and folders except the root `index.php`, `administrator/index.php`, and certain folders where allowable file types are permitted, primarily image files. In a standard Joomla+CiviCRM installation, files stored in the `/media/civicrm/ directory` may require direct access. To permit access, add exclusions to the .htaccess builder.

Open the AdminTools .htaccess Maker, scroll to the Exceptions section, and add these exceptions to the indicated fields:

- Allow direct access, except .php files, to these directories
    - `media/civicrm/persist/contribute/dyn/`
- Allow direct access, including .php files, to these directories
    - `administrator/components/com_civicrm/civicrm/extern/`
    - `administrator/components/com_civicrm/civicrm/bin/`
    - `administrator/components/com_civicrm/civicrm/packages/kcfinder/`

!!! note
    The above represents the standard directory paths where you will need to add exceptions. Depending on your configuration and use of the system, you may need to adjust the paths or add additional paths.

<!-- Source: integration/joomla/index-part2.md -->
