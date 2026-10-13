---
title: Moving an existing installation to a new URL, location or CMS
category: how-to
topic: system-administration
subtopic: servers-urls-and-cms
component: CiviCRM
audiences:
- technical
- administrator
- operations-user
- fundraising-manager
level: advanced
journey_stage: plan-and-configure
summary: Move a CiviCRM installation to a new URL, location, or CMS and update its files, database, and location-dependent
  settings.
extensions: []
related: []
review_priority: low
review_notes:
- The source contains apparent typos in the menu paths for Resource URLs and clearing the cache; these paths are retained
  as written.
- The path-variable example and the templates_c link have unmatched closing brackets in the source; they are retained as written.
- The substitution instructions name placeholders differently from those in the database commands; both are retained as written.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: misc/switch-servers.md
destination_path: sysadmin/misc/switch-servers.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/misc/switch-servers/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Moving an existing installation to a new URL, location or CMS

Some settings in the CiviCRM database relate to a physical location, such as a server file path or a public URL. These settings can use:

* Path variables (e.g., `[civicrm.files]/upload/`]. This is the most modern solution. It's recommended to convert paths to use path variables whenever possible.
* Relative paths (with respect to the webroot, eg `sites/default/files/civicrm` or `media/civicrm`). These can generally stay as-is unless you're moving to a new CMS (e.g. Drupal to WordPress).
* Absolute paths (e.g. `/path/to/my/site/wp-content/uploads`). These must almost always be changed to match a new server.

**If you regularly copy a production database to a test server, you can [use a settings override](../customize/settings.md) to avoid having to "fix" the directory and URL-based settings each time you copy the database over.**

For instructions on moving your CMS data, please consult the relevant CMS documentation.

Some sites may have been advised to create a file `/path/to/civicrm/settings_location.php`, which hardcodes the path to the site configuration directory. This is used to work around issues with deducing the site configuration path. If your site has such a file, it may require updating along with the hardcoded paths in `civicrm.settings.php`.

## Moving an existing site to a new URL/location

You will always be moving your database and assets (images, PDFs, etc.). When moving to a new CMS, or merging a separate CiviCRM into an existing site, you should install a fresh copy of CiviCRM, then copy your database and assets (images, PDFs, etc.). When moving a site to a new server (to create a test site, to move hosting companies, etc.), you should copy the database, assets, and the entire filesystem.

If you're moving the entire filesystem, you must make significant changes to `civicrm.settings.php`:

1. All URLs in civicrm.settings.php should be updated to the new version (search and replace your old URL with the new URL).
2. All database connection strings in `civicrm.settings.php` should reflect new database usernames/passwords/database names.
3. All paths in `civicrm.settings.php` should be updated to reflect the new site paths (examine the entire file for file paths and confirm the correct new values).

## Moving files

### Partial copy

If you're not copying the entire filesystem, make sure to copy:

* All the contents of directories listed in **Administer menu > System Settings > Directories**. Extensions, upload folders. Also custom templates and custom PHP if applicable.

### Full copy

After copying all files, delete the following files:

* The `templates_c` folder ([location is CMS-specific](https://civicrm.stackexchange.com/a/15932/12)].
* Some users report needing to delete `Config.IDS.ini` if it exists.

## Moving databases

If you have a single database for both CMS and CiviCRM data, you should export them together. If you're moving CMSes, you will need to [export only the CiviCRM tables](https://stackoverflow.com/a/5269543/2832108).

Many CMS tools have plugins specifically for exporting databases - e.g. [Backup and Migrate](http://drupal.org/project/backup_migrate) for Drupal. If you don't have experience with moving databases, it's recommended to use a dedicated export tool (e.g. `mysqldump` or `PhpMyAdmin`).

### mysqldump

_Substitute mysql_username, cms_db_name and dump_file_name_of_your_choice with appropriate values._

On the old server:

```shell
mysqldump --skip-definer -u <mysql username> -p <civicrm database name> > civicrm_backup.sql
```

#### Trigger and view definers

By default, MySQL dumps include the MySQL username for triggers (which all CiviCRM installs use) and views (which CiviCase and multilingual installs use). Importing those to a site with a different MySQL username will result in an error.

Almost all supported versions of MySQL/MariaDB support the `--skip-definer` option above. If yours does not, and if the MySQL username is different on the new server, you should find and replace in your .sql file to change all references of the old MySQL username to the new username. Alternatively, you can [export without triggers](https://civicrm.stackexchange.com/a/48381/12) (if you don't have views). If your MySQL username is a word that might exist elsewhere in the database, you can [use a regular expression](https://civicrm.stackexchange.com/a/2561/12) to find and replace only the definer lines.

### Loading your database on the new server

If you are using a CMS-specific plugin, you can use the documentation from that plugin. You can also use PhpMyAdmin if available.

From the command line:

_Substitute mysql_username, cms_db_name and dump_file_name_of_your_choice with appropriate values._

On the new server:

```shell
mysql -u <mysql username> -p <civicrm database name> < civicrm_backup.sql
# If you have `cv` installed:
cv sql < civicrm_backup.sql
```

!!! note
    Exporting and import databases can be performed with phpMyAdmin, but for exporting or importing a large database phpMyAdmin tends to time out
    and using command line is more reliable. The steps to export and import the database in phpMyAdmin are as follows:
    1. In the PHPMyAdmin interface, select your existing civiCRM database and then select the export feature.
    2. Under Export Method, select 'Quick' with format 'SQL.'
    3. Click the submit button to export your database which should then download somewhere onto your computer.
    4. Import the data by navigating to the new website's PHPMyAdmin system and doing a simple,
    no frills import, using the data you just downloaded. The import should be into a new database created for CiviCRM
    (or an existing database which has been emptied by deleting all tables), with suitable permissions for the database user
    configured in the new sites civicrm.settings.php.

## Post-import steps

* If your Resource URLs (**Administer > System Settings > Reource URLs**) and/or Directories (**Administer > System Settings > Directories**) do not use path variables, you must update these to match the new URLs and file paths.
* If the new site is a live site, ensure that cron is configured. Do not use cron on test/development sites.
* If you previously set up a log rotation for your [ConfigAndLog logs](https://civicrm.stackexchange.com/a/15932/12), you should do this again.
* Clear your CiviCRM cache (from **Adminster menu > System Settings**).

### Additional steps if your URL has changed

When moving your server, it's quite likely that you've changed your URL. If so, please make sure to update the URL in the following locations:

1. If you use a payment processor with recurring payments, and that processor notifies your server via IPN (e.g. PayPal, Authorize.Net), you must update the IPN in your payment processor's settings page. Please note that for PayPal, you can only change IPNs for new recurring payment profiles. To handle your old IPNs, you willneed to set up a [307 redirect](http://civicrm.stackexchange.com/questions/473/how-to-change-paypal-ipn-url-when-migrating-civicrm-onto-a-new-domain) from the old URL.
1. URLs linking to contribution pages etc. in mailing templates, scheduled reminders etc. need to be changed.
1. Images in mailing templates and scheduled reminders must get a new absolute URL (or a redirect).
1. Third-party integrations, e.g. ReCAPTCHA, are tied to specific URLs and must be updated.
1. If you use Mosaico, you will need to change the paths in your Mosaico templates. There is an API command but it doesn't handle all scenarios. It's recommended to run the following MySQL commands:

```sql
UPDATE civicrm_mosaico_template SET metadata = REPLACE(metadata, 'https://oldsite.org', 'https://newsite.org');
UPDATE civicrm_mosaico_template SET html = REPLACE(html, 'https://oldsite.org', 'https://newsite.org');
-- The following lines are changing the paths to your extensions and image upload directories.
-- The examples below show converting Drupal paths to standalone - please check the correct file paths for your CMS(es).
UPDATE civicrm_mosaico_template SET metadata = REPLACE(metadata, 'sites/default/files/civicrm/ext', 'ext');
UPDATE civicrm_mosaico_template SET html = REPLACE(html, 'sites/default/files/civicrm/ext', 'ext');
UPDATE civicrm_mosaico_template SET metadata = REPLACE(metadata, 'sites/default/files/civicrm/persist', 'public/persist');
UPDATE civicrm_mosaico_template SET html = REPLACE(html, 'sites/default/files/civicrm/persist', 'public/persist');
UPDATE civicrm_mosaico_template SET metadata = REPLACE(metadata, 'sites%2Fdefault%2Ffiles%2Fcivicrm%2Fpersist', 'public%2Fpersist');
UPDATE civicrm_mosaico_template SET html = REPLACE(html, 'sites%2Fdefault%2Ffiles%2Fcivicrm%2Fpersist', 'public%2Fpersist');
```

## Trouble-shooting

### Only the front page of your site can be displayed - Drupal

If you are using Drupal, you may find that your site looks to be working until you click on a link or go to any other url than the front page. This can be caused by the default setting for the Apache mod-rewrite module. If you can load url's like, "http://example.org/index.php?q=/civicrm/admin/setting", but not "http://example.org/civicrm/admin/setting, then this is likely the cause.

Use the following article, or many others on the web to enable mod_rewrite. -- [http://drupal.org/node/134439](http://drupal.org/node/134439)

### Only the front page of your site can be displayed - Joomla

You may see the error: `Failed opening required 'CRM/Core/Config.php'`. Solved this by manually editting [DOCROOT]/administrator/components/com_civicrm/civicrm.settings.php and [DOCROOT]/components/com_civicrm/civicrm.settings.php to replace incorrect values for $civicrm_root, CIVICRM_TEMPLATE_COMPILEDIR, and CIVICRM_UF_BASEURL.

### Table 'db_name.civicrm_option_value_en_us' doesn't exist

The error occurs on multi-lingual migrations when the source server is not case sensitive but the destination server is. To correct this error, edit the database dump in a text editor and globally find and replace your language codes to the proper case. The second pair of letters should be upper case, as in en_US.

### Database Error Code: FUNCTION ... does not exist

This seems to be caused by the database backup and restore not copying the functions and triggers properly.

The solution is to run `http://example.org/civicrm/menu/rebuild?reset=1&triggerRebuild=1` which fixes the trigger and function definitions in the database.

On Joomla sites run `http://example.org/administrator/?option=com_civicrm&task=civicrm/menu/rebuild&reset=1&triggerRebuild=1`

<!-- Source: misc/switch-servers.md -->
