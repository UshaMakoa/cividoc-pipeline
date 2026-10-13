---
title: Directories
category: how-to
topic: system-administration
subtopic: upload-directories
component: CiviCRM
audiences:
- operations-user
level: basic
journey_stage: plan-and-configure
summary: Set paths for CiviCRM upload directories and review the precautions for images and custom files.
extensions: []
related: []
review_priority: medium
review_notes:
- The Images Path warning cites kcfinder version 3.12 and CiviCRM version 4.5.3; its current applicability needs review.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/directories.md
destination_path: sysadmin/setup/directories.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/directories/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Directories

Click Directories to open the Upload Directories page. The first time you access CiviCRM, default values for these upload directories are supplied based on the CIVICRM_TEMPLATE_COMPILEDIR file specified in civicrm.settings.php. If you modify the defaults, make sure your web server has write access to the directories.

1. Indicate a path on your server or network for the items you wish to set up: temporary files, images, custom files and/or custom templates. For example, a temporary file path might look like this: /home/drupal/public_html/drupal/files/civicrm/upload/
2. Click Save to save your action or Cancel to cancel it.

If successful, you will see the message "Your settings changes have been saved."

!!! danger "Images Path"

    The **Images** directory should be specified without the use of symbolic links. Using symbolic links in this field has been observed to cause an "Unknown error" message when attempting to upload images or refresh image thumbnails in the email editor. This is due to a change in the kcfinder package version 3.12 introduced in CiviCRM version 4.5.3.

!!! danger "Custom Files Path"

    The current "default" setting for the **Custom Files** directory is below the default path for **Temporary Files**. This is potentially dangerous, as running the _directoryCleanup_ debug action could delete all custom files. If you are using custom files, you should modify the path so it is NOT below your Temporary Files directory.

<!-- Source: setup/directories.md -->
