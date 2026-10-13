---
title: Backup data
category: how-to
topic: system-administration
subtopic: database-files-and-security
component: CiviCRM
audiences:
- administrator
- technical
- operations-user
level: intermediate
journey_stage: plan-and-configure
summary: Identify what to back up, how often to do it, and how to protect the backups.
extensions: []
related:
- ../misc/switch-servers.md
review_priority: low
review_notes:
- The CIVICRM_DSN example uses `user_passord` as a placeholder; this may be a typo and needs verification.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/backups.md
destination_path: sysadmin/setup/backups.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/backups/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Backup data

Perform regular backups and keep a current copy somewhere other than the machine running CiviCRM. Backups protect against hard drive failure and less common data disasters.

## Database backup

Your CiviCRM data is primarily stored in the MySQL database configured for your site. Before putting a CiviCRM site into production, ensure that you have an automated procedure for regular backups. Choose the frequency based on how often your data changes and how many days’ worth of data you can afford to lose.

!!! tip
    The database server and database name are identified in the CIVICRM_DSN setting in civicrm.settings.php:

    ```
    define( &#39;CIVICRM_DSN&#39;, &#39;mysql://db_user:user_passord@db_server/db_name?new_link=true&#39; );
    ```

If you use a hosting provider, ask whether regular backups are part of your service and what disaster contingency plans are in place, such as redundancy and offsite or multiple-location backup storage.

If you set up backups yourself, tools such as **mysqldump** or **phpMyAdmin** can be used. Searching for *“mysql backup”* will give you options and links to procedures.

## File-system backup

To restore a complete copy of your site, you may also need regular backups of directories on your server’s file system. These directories are configured under **Administer CiviCRM** » **System Settings** » **Directories**.

- If you use **custom fields to attach files to your contacts**, such as photos, other images, resumes, or other documents, back up the **Custom Files Directory** regularly.
- If you have configured **Premiums with images**, back up the **Images Directory**.
- If you have created **custom template(s)** to replace standard CiviCRM screen(s), back up the **Custom Templates Directory**.
- If you have modified core files in the CiviCRM codebase, keep a backup of those files too.

One way to test whether your backup is sufficient is to [re-create your CiviCRM database on another machine](../misc/switch-servers.md).

## Security of backups

Regular backups help you recover after a fire or other disaster, disk failure, or a hack. They also need protection: a backup can be easier to steal than data from the production site. Someone who steals a database backup is in almost the same position as someone who steals a copy of the live database.

A stolen code backup is usually less serious than a stolen database backup. However, cache files or settings files in a code backup may be useful to a hacker; settings files include database passwords. Code can also contain hard-coded credentials for third-party services.

Store backups in secure locations. Generally, it is best practice not to include settings files or cache files in a backup, and not to hard-code credentials when writing code. If a backup contains sensitive or private data, consider encrypting the entire backup or at least its sensitive part—probably the database dump—so that someone who steals it cannot read it unless they crack the encryption password.

<!-- Source: setup/backups.md -->
