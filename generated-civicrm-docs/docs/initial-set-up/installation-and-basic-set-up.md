---
title: Installation and basic set-up
category: explanation
topic: installation
subtopic: planning-and-maintenance
component: CiviCRM
audiences:
- technical
- administrator
- operations-user
level: intermediate
journey_stage: plan-and-configure
summary: Understand the prerequisites, hosting choices, security considerations, and upgrade planning for a CiviCRM installation.
extensions: []
related: []
review_priority: low
review_notes:
- The prerequisites list names a package "MAMPP" and associates it with the Macintosh; verify the package name before changing
  it.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: initial-set-up/installation-and-basic-set-up.md
destination_path: initial-set-up/installation-and-basic-set-up.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/initial-set-up/installation-and-basic-set-up/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Installation and basic set-up

This information is for technicians and may be difficult to understand if you have little or no experience setting up web applications. In that case, you may wish to seek help or point your organisation's technical staff to this material.

## Prerequisites

CiviCRM must be installed on a computer with a web server (such as Apache or nginx), PHP and MySQL. Some prefer to try CiviCRM on their local computer before installing it on a dedicated web server. If you don't have these prerequisites, you can download packages from the Internet such as WAMP, XAMPP, MAMPP and LAMP. The first two packages are for Windows and the second two are for the Macintosh and Linux, respectively.

Consider where you host your CiviCRM instance. Discuss hosting with your System Administrator and review the [Hosting information](https://docs.civicrm.org/sysadmin/en/latest/planning/hosting/) in the System Admin guide.

Before installation, decide which CMS (Content Management System: used for building and managing websites) you wish to integrate with. The open-source options are Drupal, WordPress and Joomla!, or you can use Standalone CiviCRM.

You can find full installation instructions in the [System Administrator Guide](https://docs.civicrm.org/sysadmin/en/latest/requirements/).

## Internet vs. local installs

Most organisations access CiviCRM over the internet. Some organizations that only want internal staff to have access, and are security conscious, choose to install CiviCRM on an internal network where it is accessible only internally. The downside of an installation that is not publicly available is that contacts cannot 'self serve' to update their data.

## Securing your system

Once CiviCRM is installed, it is important to secure your system. The [System Administrator Guide](https://docs.civicrm.org/sysadmin/en/latest/setup/security/) describes techniques for securing your server and website.

## Upgrades

New versions of CiviCRM are released every month. Although [extensions](../introduction/extensions.md) are typically how you add major new features, you need to upgrade the CiviCRM core software periodically to keep your site secure and take advantage of smaller new features and improvements. Some upgrades contain security fixes that are crucial to apply in a timely manner.

Plan for the people and time needed to upgrade your site. Read release notes thoroughly to understand how an upgrade may change it. Test upgrades on a copy of your live site to make sure the process runs smoothly. Back up your site and database before upgrading your live site, even if you tested the process on a test site.

Because upgrades are important and technical, many organisations employ a CiviCRM expert service provider to carry them out.

<!-- Source: initial-set-up/installation-and-basic-set-up.md -->
