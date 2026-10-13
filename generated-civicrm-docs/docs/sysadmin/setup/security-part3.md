---
title: Filesystem permissions and file access
category: how-to
topic: system-administration
subtopic: filesystem-and-file-access
component: CiviCRM
audiences:
- administrator
- technical
- operations-user
level: intermediate
journey_stage: reference-and-troubleshooting
summary: Assess filesystem permissions and investigate warnings about publicly accessible CiviCRM files.
extensions: []
related:
- https://civicrm.stackexchange.com/questions/168/are-there-recommended-directory-ownership-and-permission-settings-for-civicrm-fi#answer-11640
- https://github.com/civicrm/civicrm-core/blob/master/CRM/Utils/Check/Security.php#L168
- https://civicrm.org/advisory/civi-sa-2014-001-risk-information-disclosure
- http://forum.civicrm.org/index.php?topic=31570.new;topicseen#new
review_priority: medium
review_notes:
- The uploads check is dated to CiviCRM 4.4.4, and the log-file section says further direction is pending; both passages have
  been left unchanged.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/security-part3.md
destination_path: sysadmin/setup/security-part3.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/security-part3/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# Filesystem permissions and file access

!!! tip
    There is a [detailed post on Stack Exchange about CiviCRM file permissions](https://civicrm.stackexchange.com/questions/168/are-there-recommended-directory-ownership-and-permission-settings-for-civicrm-fi#answer-11640). In particular it points out that allowing the code to be writable by the web server
    greatly increases the risk of a hack. However, if the directories in the file system containing PHP code are not writable by the
    web server, then installation of extensions via the browser UI may fail (as will updates of the CMS
    via the browser, such as WordPress offers). Besides, on shared hosting it may not
    be possible to make the codebase unwritable. In short, if the hosting allows you to make your codebase unwritable, and
    losing the possibility of updating or installation of extensions via the browser is acceptable,
    then doing so offers a considerable improvement in security.

## Directories should not be browsable

In its default configuration, CiviCRM places some uploaded and server-generated data in the CMS's data folder (such as Drupal's "sites/default/files" or Joomla's "media"). This folder is web-accessible, but many of the documents processed by CiviCRM should not be web-accessible. If CiviCRM's data folders are not suitably protected from web access, then sensitive information may be disclosed.

If these directories are accessible and browseable, then data from your site may be indexed by search engines. This makes it significantly easier for an attacker to identify your site.

## Uploads should not be accessible

If you see this warning, CiviCRM is alerting you that it was able to retrieve a file from the CiviCRM uploads directory over HTTP. If this is the case then there is a risk of personal data being exposed via your CiviCRM install.

Files in this directory need to be accessible to CiviCRM via local file reference, but may contain personal data and therefore should not be accessible over the public internet.

The correct response on seeing this warning is to attempt to confirm whether the warning is valid by accessing files directly yourself. If this is possible, then server configuration adjustment is required to prevent direct access of those files.

To do this -

1. Identify the full URL path to your CiviCRM uploads directory.
   _For example: the CiviCRM Drupal Demo site is configured to use /var/www/drupal.demo.civicrm.org/public/sites/drupal.demo.civicrm.org/files/civicrm/upload/ as the upload path, and /var/www/drupal.demo.civicrm.org/public/ is the webroot, so the full URL to the uploads directory is http://drupal.demo.civicrm.org/sites/drupal.demo.civicrm.org/files/civicrm/upload/_
2. Identify the name of a file in that upload directory.
   _To continue the example, I'd look in that directory on the server, see that "SomeUpload_1122334455667788.csv" exists, and add that to the URL, resulting in http://drupal.demo.civicrm.org/sites/drupal.demo.civicrm.org/files/civicrm/upload/SomeUpload_1122334455667788.csv_
3. Attempt to directly visit this URL. If I am able to view the contents of the file, then additional server configuration is required.

Refer to your server administrator or hosting organisation for support in configuring your webserver, as webserver configuration details differ between servers and hosting environments.

`CRM_Utils_Check_Security::checkUploadsAreNotAccessible()` is defined in [CRM/Utils/Check/Security.php](https://github.com/civicrm/civicrm-core/blob/master/CRM/Utils/Check/Security.php#L168) - see this file for implementation details.

See also `CRM_Utils_Check_Security::checkDirectoriesAreNotBrowseable()`

This check was introduced in CiviCRM 4.4.4. For details, see [https://civicrm.org/advisory/civi-sa-2014-001-risk-information-disclosure](https://civicrm.org/advisory/civi-sa-2014-001-risk-information-disclosure)

If you believe you are seeing false positives on this check, please see [http://forum.civicrm.org/index.php?topic=31570](http://forum.civicrm.org/index.php?topic=31570.new;topicseen#new)

## The Log file should not be accessible

The CiviCRM log file contains a significant amount of debug data on some sites. If directly accessible, sensitive data may be revealed to outsiders. This file should be protected.

Until some direction can be given, more info can be found at this link:

[https://civicrm.org/advisory/civi-sa-2014-001-risk-information-disclosure](https://civicrm.org/advisory/civi-sa-2014-001-risk-information-disclosure)

<!-- Source: setup/security-part3.md -->
