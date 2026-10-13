---
title: Views integration
category: how-to
topic: system-administration
subtopic: civicrm-data-in-backdrop-views
component: Backdrop Views
audiences:
- technical
- administrator
- operations-user
- membership-manager
level: intermediate
journey_stage: plan-and-configure
summary: Configure Backdrop Views to display CiviCRM data on a website.
extensions: []
related: []
review_priority: low
review_notes:
- The described CMS Database Integration output begins with `$databases['default']['default']['prefix']= array(`, but the
  example begins with `$database_prefix = array(`.
- The notes about repeating configuration after adding custom fields or custom data sets appear to give different requirements.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: integration/backdrop/views.md
destination_path: sysadmin/integration/backdrop/views.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/integration/backdrop/views/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Views integration

## Backdrop Views

Views is a Backdrop module for displaying website content, such as a list of the latest news on a home page. CiviCRM integrates with Backdrop Views so that CiviCRM data can be shown on your website.

For example, to create a public page called ‘Partner Organizations’, you could:

1. Select criteria for the Contact data to display:
    - Organization contacts only
    - Contacts tagged ‘Partner’ in CiviCRM
    - Contacts with a membership of status ‘New’ or ‘Current’
2. Choose the data to show:
    - Organization name
    - State/Province
    - Website
    - Phone number
3. Show the data in either table or paragraph format.
4. Allow the public to filter the results by State/Province.

### Configuration

These instructions assume CiviCRM and Backdrop are in separate databases on the same physical host. If CiviCRM and Backdrop are in the same database, the 12 steps below are not required.

1. Before making any changes, it is _strongly_ advised that you make backups of your mysql databases and settings.php file.
2. If you have different database users for your CiviCRM and Backdrop databases, grant `SELECT` access for the Backdrop user to all the CiviCRM tables.
3. Make sure you are logged into your Backdrop site as the administrator.
4. In the CiviCRM admin menu, visit **Administer > System Settings > CMS Database Integration** (`http://example.org/civicrm/admin/setting/uf?reset=1`).
5. You should see a page with output that begins with `$databases['default']['default']['prefix']= array(`. It should look like the following snippet, where `example_civicrm` is replaced with the name of the database that contains CiviCRM. (**Note:** backticks are no longer included.)

   ```
   $database_prefix = array(
     'default' => '',
     'civicrm_acl'                              => 'example_civicrm.',
     'civicrm_acl_cache'                        => 'example_civicrm.',
     //...
   ```

6. Copy this setting output, including the trailing `);`.
7. Open `/settings.php` for editing from the root directory of the site, typically `public_html` on most servers.

    !!! note
        This assumes you have a single site installation. The location of the settings file might be different depending on whether or not you have multiple sites.

8. Go to the bottom of the file and paste in the settings output you copied. If the settings.php file already includes an earlier version of the output, remove the earlier version before pasting the new output.
9. Backdrop uses a simplified database string as follows: `$database = 'mysql://user:pass@localhost/database_name';`. To allow multiple databases, convert it to this format in the `settings.php` file as shown below. [More on this](https://civicrm.stackexchange.com/questions/21085/how-do-i-get-views-working-with-civicrm-and-backdrop).

```php
  $databases['default']['default'] = array(
    'driver' => 'mysql',
    'database' => 'database_name',
    'username' => 'user',
    'password' => 'pass',
    'host' => 'localhost',
  );
```

10. You may need to indicate the default prefix. If you see an error like the one below:

    !!! error ""
        PDOException: SQLSTATE[42S02]: Base table or view not found: 1146 Table 'kckruppc_every.semaphore' doesn't exist: SELECT ...

    Include an additional line, `'default' => '<backdroptableprefix>'`, in your `settings.php` just after `$database_prefix = array(`. You can find more information on this error in [this forum post](http://forum.civicrm.org/index.php?topic=20910.0).

11. Save the file settings.php. You might want to clear your site cache at this point.
12. You should now be able to create Backdrop Views based on CiviCRM data.

!!! note
    If you add a new set of custom fields to CiviCRM, you will need to re-do these steps again so any new fields in the field set can be accessed by Backdrop Views.

!!! note
    If you are using Custom Data sets in CiviCRM, anytime you add a new data **set** (not just a field) you must repeat this process.

### Creating views using CiviCRM data

Views are located in the **Structure** section of the Backdrop administrative menu. When you create a View, give it a name and select what kind of data you wish to show.

If your view is focused on Contacts, which most are, select Show: CiviCRM Contacts. To display details about other CiviCRM data, such as events, relationships, contributions or activities, there are additional options that might provide more data fields for those types.

![Screenshot demonstrating the "Add new view" page](../../img/Views-CiviCRM-Partner-1.png)

After the View is created, edit the fields, filters, display and other configurations to show the data as you prefer. Views takes some experimentation and/or training to get it right. If you become stuck, ask questions on [Stack Exchange](https://civicrm.stackexchange.com/) or [Mattermost](https://chat.civicrm.org), or [hire a consultant](https://civicrm.org/partners-contributors).

### Other things Views and CiviCRM can do

- Lists of upcoming events
- Building reports on contributions, activities or event registrants
- Honor roll listing of recent donors
- Staff, board of directors or committee lists
- A list of current members
- ...and more!

<!-- Source: integration/backdrop/views.md -->
