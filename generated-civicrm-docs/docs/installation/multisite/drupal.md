---
title: Drupal multisite
category: how-to
topic: installation
subtopic: drupal-site-setup
component: CiviCRM multisite
audiences:
- technical
- administrator
- operations-user
level: advanced
journey_stage: plan-and-configure
summary: Set up another CiviCRM domain for a Drupal site and configure its domain settings and access control.
extensions:
- Multisite Permissioning
- multisite
related: []
review_priority: high
review_notes:
- The Drupal module path `Site building -> Modules` (`/admin/build/modules`) looks potentially obsolete; verify it before
  updating the instructions.
guide: installation
source_repository: https://lab.civicrm.org/documentation/docs/installation.git
source_path: multisite/drupal.md
destination_path: installation/multisite/drupal.md
legacy_urls:
- https://docs.civicrm.org/installation/en/latest/multisite/drupal/
civicrm_version:
- latest
source_commit: 5a8b870477f63bea90551acb2f7516df67784b19
last_modified: '2026-08-20'
---

# Drupal multisite

## Install the first site

Install `site1.example.com` as you would any other normal CiviCRM installation.

The top-level site does not need to be multisite aware. If you want it to be, enable multisite by visiting `civicrm/admin/setting/preferences/multisite?reset=1`. If you do this, also grant the associated Drupal permission, "CiviCRM: administer Multiple Organizations", to your developers or website administrators.

Create a new contact to be the domain contact for the new domain. The contact and domain records can now be created with the `MultisiteDomain.create` api, which is part of the extension.

## Create new database records

You can create the database records in this section automatically by installing the [Multisite Permissioning](https://civicrm.org/extensions/multisite-permissioning) extension and using the `MultisiteDomain.create` api as described in the [extension's README file](https://lab.civicrm.org/extensions/multisite/-/blob/master/README.md).

### Create the "Default Organization" record

Each CiviCRM domain must have its own [Default Organization](https://docs.civicrm.org/sysadmin/en/latest/setup/#site-configuration). Create a new Organization record to represent the default organization of the new domain.

### Create the domain record

Insert a new domain record into the CiviCRM database. For example, if your new contact is 555:

```sql
INSERT INTO `civicrm_domain` (
  `name`,
  `description`,
  `version`,
  contact_id)
SELECT
  'site 2',
  'second test site',
  cd.version,
  555
FROM civicrm_domain cd
WHERE cd.id = 1;
```

### Build the navigation links for new domain

Modify the `civicrm_codebase/sql/civicrm_navigation.mysql` file to specify the new domain. For example, change:

```sql
SELECT @domainID := id
FROM civicrm_domain
WHERE `name` = 'Default Domain Name';
```

To:

```sql
SELECT @domainID := id
FROM civicrm_domain
WHERE `name` = 'site 2';
```

OR:

```sql
SET @domainID = 2;
```

Import this file into your CiviCRM database.

## Create the new site

Set up the CMS for the second site. In some cases, you will install a new instance of the CMS. You can also use the existing CMS if you are using the [Domain Access](https://www.drupal.org/project/domain) module for Drupal.

### Locate the settings file for the second site

Depending on how you would like to install CiviCRM for site 2, proceed to one of the following options.

### Manual CiviCRM installation for site2.example.com

- Copy the CiviCRM settings file from the previous site (site1) to the new site (site2).

    ```
    cp sites/site1.example.com/civicrm.settings.php sites/site2.example.com/
    ```

    `sites/site2.example.com/civicrm.settings.php` is your new settings file and needs to be modified.

- The sites can share a single instance of the CiviCRM code in `sites/all/modules/` directory if they are using the same CMS.
- Modify the `sites/site2.example.com/civicrm.settings.php` file to adjust settings such as `CIVICRM_TEMPLATE_COMPILEDIR` and `CIVICRM_UF_BASEURL` for the new site.
- Enable the CiviCRM module through Drupal, at Site building -> Modules ( `/admin/build/modules` ).

### Drupal with the Domain Access module

!!! note
    If you're using Drupal with Domain Access, consider installing the [Domain Access CiviCRM](https://civicrm.org/extensions/domain-access-civicrm) module if users might be creating new Drupal accounts via CiviCRM profiles.

Similar to WordPress, with the Domain Access module there is only one copy of the codebase and one copy of `civicrm.settings.php`.

The easiest approach is to assign the same domain_id's in Drupal and CiviCRM. Then replace this line:

```php
define( 'CIVICRM_DOMAIN_ID' , 1 );
```

With:

```php
if (!function_exists('domain_get_domain')) {
  // The Domain Access module is not enabled
  define('CIVICRM_DOMAIN_ID', 1);
}
else {
  // Get domain_id from the Drupal setup - Drupal and CiviCRM domain IDs MUST match!
  $domain = domain_get_domain();
  define('CIVICRM_DOMAIN_ID', $domain['domain_id']);
}
```

Otherwise, replace the above line with a conditional similar to:

```php
//define the per-domain settings here first in case we're running from CLI (e.g. bin/csv/import.php)
if(empty($_SERVER['SERVER_NAME'])) {
  define( 'CIVICRM_DOMAIN_ID', 1 );
  define( 'CIVICRM_UF_BASEURL' , 'http://example.local/' );
}
```

```php
switch ($_SERVER['SERVER_NAME']) {
  case 'example.local':
    define( 'CIVICRM_DOMAIN_ID', 1 );
    define( 'CIVICRM_UF_BASEURL' , 'http://example.local/' );
    break;
  case 'cdp.example.local':
    define( 'CIVICRM_DOMAIN_ID', 2 );
    define( 'CIVICRM_UF_BASEURL' , 'http://cdp.example.local/' );
    break;
  case 'svp.example.local':
    define( 'CIVICRM_DOMAIN_ID', 3 );
    define( 'CIVICRM_UF_BASEURL' , 'http://svp.example.local/' );
    break;
}
```

With either of the above, skip the following "Register a new domain" step.

### Auto + manual installation for site2.example.com

- Use the CiviCRM installer to install CiviCRM for `site2.example.com`. Specify a new CiviCRM database, which can be dropped later. `sites/site2.example.com/civicrm.settings.php` is your new settings file and needs to be modified.
- Adjust the `CIVICRM_DSN` setting to use the CiviCRM database used by site1. Drop the new CiviCRM database previously created.
- The sites can share a single instance of the CiviCRM code in `sites/all/modules/` directory.

### Register a new domain

Modify the located `civicrm.settings.php` file for site2. Change:

```php
define( 'CIVICRM_DOMAIN_ID' , 1 );
```

To reflect the id of the inserted domain record in step2. Assuming the id is 2 for the newly inserted record, the line would change to:

```php
define( 'CIVICRM_DOMAIN_ID' , 2 );
```

### Register a domain group

In a multi-org installation, you can configure a group for each multisite aware domain, not necessarily including the top-level domain. When you log in to the site and go to the "manage groups" screen, you will see a group with the name of the domain. The system requires you to register this master group, which holds sub-groups/contacts. Contacts using the site will be automatically added to the site. Set a different group for each site at `civicrm/admin/setting/preferences/multisite?reset=1`.

It is valid not to enable multisite on the top-level domain, which is unaware of the subdomains. This improves performance by not creating such a deep hierarchy of groups.

### Associate an organization with the master group

To represent a multi-org hierarchy, an organization could be connected to the master group in a one-to-one relationship. Add a record in the civicrm_group_organization table to represent this, or use the MultisiteDomain.create api to create your domain. This record only has value if the multisite extension is enabled.

### Configure access control

Here, we restrict users on Site N to contacts in Site N's Site Group.

A separate extension called **multisite** automatically implements CiviCRM access control for multisite installations, so that normal users on Site N are restricted to contacts in Site N's Site Group. Users with permission to view or edit all contacts bypass this access control.

<!-- Source: multisite/drupal.md -->
