---
title: Version-specific upgrade tasks
category: reference
topic: system-administration
subtopic: version-specific-tasks
component: CiviCRM
audiences:
- operations-user
- technical
- communications-manager
- administrator
level: intermediate
journey_stage: reference-and-troubleshooting
summary: Find additional tasks and changes to check when an upgrade crosses specific CiviCRM versions.
extensions: []
related:
- ../setup/secret-keys.md
- ../customize/paths.md
- ../setup/jobs.md
review_priority: high
review_notes:
- The Drupal version recommendation in the CiviCRM 5.51 section may be obsolete and could mislead readers planning an upgrade;
  it has been left unchanged.
- The preferred token `{contact.id'}` in the CiviCRM 5.43 table appears malformed; it has been left unchanged.
- The CiviCRM 5.67 section says that 2005 was 22 years earlier, which does not match the supplied page's 2026 modification
  date; the statement has been left unchanged.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: upgrade/version-specific.md
destination_path: sysadmin/upgrade/version-specific.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/upgrade/version-specific/
civicrm_version:
- 4.7.3
- 4.7.31
- 5.27.0
- 5.29.0
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# Version-specific upgrade tasks

In general, the steps to upgrade CiviCRM are identical no matter which versions you're upgrading *from* and *to*. This page lists exceptions: check each CiviCRM version your upgrade crosses for special steps.

For example, if you are upgrading from CiviCRM 4.1 to CiviCRM 4.3, check both “CiviCRM 4.2” and “CiviCRM 4.3”.

## CiviCRM 5.67

### Message template concerns.

We have been updating the message templates over time to make the code easier to adapt to updates to PHP and Smarty. We have switched to using tokens rather than variables where possible and, where it isn't, have been rationalising the way we compile the variables and often the variables themselves.

Prior to 5.67, we were still assigning the old variables as well as the new ones. In 5.67, we are no longer assigning a number of variables used in older versions of the Offline Event Receipt template. If you have customised this template, you will need to update your local version to avoid breakage.

From CiviCRM 5.67 onwards, we are starting to remove the text versions of Workflow Messages. When these were first introduced in 2005, it was common to have email clients that did not display HTML, but this is exceptionally rare 22 years later. As we automatically generate a text version when sending, the effort of maintaining these in core and on a site-by-site basis seems like a poor use of time, and we are starting to empty out the text versions as we upgrade the html versions.

### Large database concerns

This upgrade has some queries that might be slow on a large database.

If you have a large database and want to run these sql statements before your main upgrade, the statements are:

```
ALTER TABLE civicrm_mailing_event_queue MODIFY job_id int unsigned null comment 'Mailing Job',
ADD COLUMN mailing_id int(10) unsigned DEFAULT NULL COMMENT 'Related mailing. Used for reporting on mailing success, if present.',
ADD CONSTRAINT FOREIGN KEY (`mailing_id`)
REFERENCES `civicrm_mailing` (`id`) ON DELETE SET NULL,
ADD COLUMN is_test tinyint(4) NOT NULL DEFAULT 0,
DROP FOREIGN KEY FK_civicrm_mailing_event_queue_job_id;

ALTER TABLE `civicrm_mailing_event_queue`
ADD CONSTRAINT `FK_civicrm_mailing_event_queue_job_id`
FOREIGN KEY (`job_id`)
REFERENCES `civicrm_mailing_job`(`id`) ON DELETE SET NULL;

UPDATE  civicrm_mailing_event_queue q
INNER JOIN civicrm_mailing_job job ON job.id = q.job_id
SET q.mailing_id = job.mailing_id, q.is_test=job.is_test
WHERE q.mailing_id IS NULL;

```

## CiviCRM 5.59

## Error handling change in CiviMail, scheduled reminders, automated emails

When you write some sorts of messages, you may have the option, depending on your configuration, to add conditions using Smarty. For example, `{if $firstName === 'Tim'}Dear guru{/if}` would add “Dear guru” only if the variable `$firstName` was assigned and was equal to Tim.

If, however, you put in the smarty `{if $firstName === 'Tim'}Dear guru`, then the smarty would be invalid due to the lack of the closing `{/if}`. Prior to 5.59, this would result in a hard fail in Wordpress and a soft fail in Drupal. The soft fail would mean the message would go out although the contents would be unpredictable. The hard fail means the job will stop.

In 5.59, broken smarty code in all CMS will result in a hard fail. It is unusual for sites to have broken smarty in their messages, but we recommend you keep an eye on any automated emails after the upgrade in case you have some broken smarty that was not picked up earlier.

## CiviCRM 5.53

### PHP variable `auto_detect_line_endings` deprecated

The civicrm.settings.php file contains a line to set the `auto_detect_line_endings` variable. It is deprecated and the line should be removed from the file.

## CiviCRM 5.51

### Drupal version support

This is the last version to support Drupal 8.x. Drupal 7.x is still supported. Drupal 9.3+ is the current recommended version.

## CiviCRM 5.43

### Token format

Some minor changes have been made to some tokens in 5.43. If these affect you negatively, please [log an issue in GitLab]( https://lab.civicrm.org/groups/dev/-/boards) and we will assist you to find a work around.

From 5.43 onwards, tokens should be consistently rendered from all screens using a consistent syntax, except, if flexmailer is not enabled, from civimail. We recommend all sites enable flexmailer and ensure the version matches the CiviCRM version (if it doesn't match, you may have an old copy in your extensions directory to remove).

In general, the token name will match the db name and will output the db value. To get the label, add `:label`, e.g. `{contribution.payment_instrument_id:label}`. If you need the db name, you can use 'name' instead of 'label'.

#### Date tokens

Additional date formatting options are available in 5.43, documented in the [user guide](https://docs.civicrm.org/user/en/latest/common-workflows/tokens-and-mail-merge/).

#### Money tokens

The formatting of tokens for money fields has been standardised to use a php library that supports internationalisation. For example, a French recipient should see 5 990,99 € while a German would expect 1.234,56 €. Our current money formatting cannot handle that, so we have accepted the opinion of the brick money library as to what is 'standard'. The library also uses non breaking spaces, which is not the case with our legacy function.

This involved a small difference in that $ 1.00 is not $1.00 when rendered in the US locale. We still respect the configuration your site has for the thousand separator and decimal separator unless you opt out. To opt out, set `define('IGNORE_SEPARATOR_CONFIG', TRUE);` in your civicrm.settings.php. (The intention was that your site-configured thousand separator and decimal separator would be ignored if the locale differed from the site locale—as of writing, that is not working as the mechanism to change locale makes that comparison always true.)

This localisation only works in locale-aware workflows. Currently, this is specifically scheduled reminders, which will pick up the contact's preferred language.

1. The output of tokens `{case.created_date}`, `{case.modified_date}`, `{contribution.cancel_date}`, and `{contribution.thankyou_date}` is now formatted the same as other date fields, so you can expect 'September 8th, 2021 7:01 AM' instead of '2021-09-08 07:01:09'.
1. The output of token `{case.is_deleted}` is now a boolean (True/False) output. For Yes/No output, use `{case.is_deleted:label}`.
1. If you have custom tokens involving cases, the hook syntax has changed slightly (per [this issue](https://lab.civicrm.org/dev/core/-/issues/2554)).
1. If you have enabled `CIVICRM_MAIL_SMARTY`, you may no longer have the `$contact` smarty variable available in pdf and email tasks. The same values are available via contact tokens.
1. The following tokens have been replaced. An upgrade script will have replaced them in scheduled reminders, but if you try to use them in pdf and letters, you will need to fix them manually when you go to do a mail merge (the token you can manually select is correct).

|Old|New|
|----|----|
|`{membership.status}`|`{membership.status_id:label}`|
|`{membership.type}`|`{membership.membership_type_id:label}`|
|`{contribution.campaign}`|`{contribution.campaign_id:label}`|
|`{contribution.contribution_id}`|`{contribution.id}`|
|`{contribution.contribution_source}`|`{contribution.source}`|
|`{contribution.payment_instrument}`|`{contribution.payment_instrument_id:label}`|
|`{contribution.contribution_page_id}`|`{contribution.contribution_page_id:label}`|
|`{contribution.contribution_status}`|`{contribution.contribution_status_id:label}`|
|`{contribution.type}`|`{contribution.financial_type_id:label}`|
|`{contribution.contribution_cancel_date}`|`{contribution.cancel_date}`|
|`{event.event_id}`|`{event.id}`|
|`{event.balance}`|`{participant.balance}` (may be unreliable before and after)|
|`{event.event_id}`|`{event.id}`|
|`{event.event_type_id}`|`{event.event_type_id:label}`|
|`{event.fee_amount}`    |`{participant.fee_amount}`|
|`{contact.preferred_communication_method}`    |`{contact.preferred_communication_method:label}`|

These tokens still work but are deprecated in favour of preferred alternatives (which are standardised).

|Old|New|
|----|----|
|`{contact.individual_prefix}`|`{contact.prefix_id:label}`|
|`{contact.individual_suffix}`|`{contact.suffix_id:label}`|
|`{contact.contact_type}`|`{contact.contact_type:label}`|
|`{contact.gender}`|`{contact.gender_id:label}`|
|`{contact.communication_style}`|`{contact.communication_style_id:label}`|
|`{contact.preferred_communication_method}`|`{contact.preferred_communication_method:label}`|
|`{contact.email_greeting}`|`{contact.email_greeting_display}`|
|`{contact.postal_greeting}`|`{contact.postal_greeting_display}`|
|`{contact.addressee}`|`{contact.addressee_display}`|
|`{contact.contact_id}`|`{contact.id'}`|
|`{contact.contact_source}`|`{contact.source}`|
|`{contact.contact_is_deleted}`|`{contact.is_deleted}`|
|`{contact.current_employer_id}`|`{contact.employer_id}`|
|`{activity.activity_id}`|`{activity.id}`|
|`{activity.activity_type}`|`{activity.activity_type_id:label}`|
|`{activity.status}`|`{activity.status_id:label}`|
|`{activity.campaign}`|`{activity.campaign_id:label}`|

- The `{participant.note}`, `{participant.default_role_id}`, `{participant.template_title}` and `{participant.currency}` (broken) tokens are no longer available in event badges.
- The `{participant.register_date}` token in event badges now gives a more verbose format. This will be offset when we add support for more flexible date formatting.
- The `{contact.gender_id}` hidden token now renders a number, not (eg.) 'Female'. The `{contact.gender}` still works as before.
- The `{contact.preferred_communication_method}` token now renders a number. `{contact.preferred_communication_method:label}` renders the value (eg. 'Phone').
- The `{contact.signature_html}` token now renders as html, not encoded html in 'html mode' or just the text in 'text mode'.

## CiviCRM 5.37

### Token format

CiviCRM 5.37 reconciled a split in how some tokens were formatted.

| Data Type | Standard Formatting | Raw Formatting |
| -- | -- | -- |
| Date | `01/20/2020 12:00:00 am` (*localized*) | `2020-01-20 00:00:00` (*MySQL*) |
| Dropdown / Radio / Checkbox (Option Value) | `Purple` (*label*) | `P` (*value*) |
| Contact reference fields | `Mr Orson Welles` (*name*) | `7` (*ID*) |
| Link | `<a href='https://civicrm.org'>https://civicrm.org</a>` (*hyperlink*) | `https://civicrm.org` (*url*) |

In most contexts, CiviCRM tokens output standard formatting, but a handful of outliers outputted raw formatting. Outliers were Scheduled Reminders, Mosaico Templates, and PDF letters. These will now output standard formatting ([PR #19806](https://github.com/civicrm/civicrm-core/pull/19806)).

This change should improve readability in many cases. However, if you used the tokens to generate hyperlinks or evaluate Smarty conditionals, then you may need to switch back to raw format. If you would like enable raw formatting, then install [rawtoken](https://lab.civicrm.org/extensions/rawtoken/).

## CiviCRM 5.36

### Signing key

CiviCRM 5.36 introduces a mechanism for signing security tokens. This mechanism is not immediately required for any core user-interfaces. However, it may be required by extensions or future releases. It requires that you define [a secret key](../setup/secret-keys.md) called `CIVICRM_SIGN_KEYS`. A typical value in `civicrm.settings.php` looks like this:

```php
<?php
if (!defined('CIVICRM_SIGN_KEYS')) {
define('CIVICRM_SIGN_KEYS', 'jwt-hs256::r4Nd0Mv4LU3');
}
```

Note the use of `define()` and `jwt-hs256::`. For full information, see:

1. [Locating `civicrm.settings.php`](../setup/secret-keys.md#edit-settings)
1. [Generating a new 256-bit secret](../setup/secret-keys.md#generate-secrets)
3. [Specification of `CIVICRM_SIGN_KEYS`](../setup/secret-keys.md#civicrm_sign_keys)

## CiviCRM 5.34

### SMTP Passwords

The way CiviCRM stores SMTP passwords (and other credentials) changes in 5.34. It provides improved encryption support, but it also requires you to define [a secret key](../setup/secret-keys.md) called `CIVICRM_CRED_KEYS`. A typical value in `civicrm.settings.php` looks like this:

```php
<?php
if (!defined('CIVICRM_CRED_KEYS')) {
define('CIVICRM_CRED_KEYS', '::r4Nd0Mv4LU3');
}
```

Note the use of `define()` and `::`. For full information, see:

1. [Locating `civicrm.settings.php`](../setup/secret-keys.md#edit-settings)
1. [Generating a new 256-bit secret](../setup/secret-keys.md#generate-secrets)
3. [Specification of `CIVICRM_CRED_KEYS`](../setup/secret-keys.md#civicrm_cred_keys)

## CiviCRM 5.29

### WordPress and `[civicrm.files]`

The CiviCRM "files" folder (a.k.a. `[civicrm.files]`) stores runtime data, such as uploaded images, log files, and certain caches. The folder is created automatically during installation. However, the default location of this folder has evolved, and some systems require a manual update.

??? note "How has the folder changed?"

    The *de facto* typical location changed:

    | Installer version | Typical location |
    | -- | -- |
    | CiviCRM <=4.6 | `{WEB_ROOT}/wp-content/plugins/files/civicrm/` |
    | CiviCRM >=4.7 | `{WEB_ROOT}/wp-content/uploads/civicrm/` |

    Additionally, the technical rule for calculating the location changed subtly:

    | Version | Technical rule to determine default location |
    | -- | -- |
    | CiviCRM <=5.28 | Start from `CIVICRM_TEMPLATE_COMPILEDIR` and go to the parent folder |
    | CiviCRM >=5.29 | Start from `wp_get_upload_dir()` and go to child folder, `civicrm/` |

    For many deployments, the change in the technical rule will still give the same outcome. However, if a site originated on <=4.6, then the `wp_get_upload_dir()` rule may cause breakage.

    __Special aside__: Early revisions of 5.27 (5.27.0-5.27.3) included an update to use `wp_get_upload_dir()`; however, this did not provide adequate documentation/support for the migration. It was rolled back in 5.27.4 and deferred to 5.29.

??? note "Why has the location evolved?"

    The original location did not match the WordPress convention for runtime data-storage. For some environments and configurations, this created compatibility or installation problems. With the changes in 4.7 and 5.29, CiviCRM is better aligned with the convention - leading to better long-term compatibility.

??? note "How do I know what the real location is?"

    Use a shell or file-manager to examine the filesystem and determine where there is actual data. In particular, look at both:

    * `wp-content/plugins/files/civicrm`
    * `wp-content/uploads/civicrm`

    If only one folder exists, then that's it.

    It is possible that both folders exist. This may happen if (a) an older site was upgraded to 5.27.0/5.29.0 without preparation, or (b) a site previously did a partial migration.

    The existence of two folders may indicate a split in the real data - or there may simply be extraneous placeholders. You need to examine to the subfolders to find any important content. Note:

    * Important content can often live in the subfolders `custom/`, `ext/`, `persist/contribute/`, and `upload/`.
    * Empty folders or any placeholder files (`.htaccess`, `index.html`) are disposable.
    * `templates_c` or `dyn` are auto-generated and disposable.

    If using a command-line, the commands `find`, `find -type f`, and `du` can help to skim or measure content.

After determining where the data currently lives, we can suggest a course of action:

| Current data location | Recommended action |
| -- | -- |
| Only `wp-content/uploads/civicrm` has real data | No change needed |
| Only `wp-content/plugins/files/civicrm` has real data | See "How To: Configure the folder explicitly" |
| Both folders have real data | See "How To: Merge or migrate the folder" |
| Neither folder has real data | It doesn't matter what you do |

??? tip "How To: Configure the folder explicitly"

    The aim of this approach is to preserve the original location of `[civicrm.files]`. If there are any external references to the original location (such as hyperlinks or backup tools), they will continue to work. We can achieve this by [explicitly setting the location in `civicrm.settings.php`](../customize/paths.md).

    Steps:

    1. Determine the correct, local path of the current folder (ex: `/var/www/wp-content/plugins/files/civicrm`)
    2. Determine the correct, public URL of the current folder (ex: `https://example.com/wp-content/plugins/files/civicrm`)
    3. Find and edit the file `civicrm.settings.php`. Add the correct path and URL:

       ```php
       global $civicrm_paths;
       $civicrm_paths['civicrm.files']['path'] = '/var/www/wp-content/plugins/files/civicrm';
       $civicrm_paths['civicrm.files']['url'] = 'https://example.com/wp-content/plugins/files/civicrm';
       ```

??? tip "How To: Merge or migrate the folder"

    The aim of this approach is to re-arrange your filesystem to match the new defaults. This makes the configuration "thinner" or "more portable", and it can resolve a split, but it may require more expertise and attention. Be sure to read the full instructions first.

    First, make sure you have a current backup of the files and the database. (If there's a problem, you may want to rollback.)

    Second, migrate the folder `wp-content/plugins/files/civicrm` to `wp-content/uploads/civicrm`. This may be as simple as renaming the folder. However, if the target folder already exists, then you'll need to move files on a per-sub-folder basis. Alternatively, in a Unix shell, you can use the `rsync` command, e.g.

    ```bash
    ## Dry run - Preview the files to sync/merge
    rsync --dry-run -uva wp-content/plugins/files/civicrm/./ wp-content/uploads/civicrm/./

    ## Actual run
    rsync -uva wp-content/plugins/files/civicrm/./ wp-content/uploads/civicrm/./

    ## Remove the old folder
    mv wp-content/plugins/files/civicrm /tmp/removed-files
    ```

    Third, with the files in place, you should update any CiviCRM settings which reference these paths:

    1. Find and edit the file `civicrm.settings.php`. Search for any references to `plugins/files/civicrm`
       and change them to `uploads/civicrm`.
    2. In CiviCRM, navigate to `Administer => System Settings => Directories`. If there are any explicit
       references to the old folder, change them.
    3. In CiviCRM, navigate to `Administer => System Settings => Resource URLs`. If there are any explicit
       references to the old folder, change them.

    Finally, we come to the most open-ended step. There may still be external references to the old URLs or the old paths, and they should be transitioned. For example, references may be found in:

    * Email templates which use images that were previously uploaded
    * Contact records with photo attachments
    * External links to assets in downloaded extensions
    * Backup tools and logging tools which collect information from the old folder

    How to address external references? Alas, the prognosis and details will depend on the specific deployment. However, here a few ideas to consider:

    * Create a sym-link or hard-link from the old folder to the new folder (if your hosting environment supports sym-links or hard-links).
    * Configure the HTTP server to redirect old URLs to new URLs.
    * Perform aggressive search/replace operations (in the filesystem and the database).

## CiviCRM 5.26

### WordPress 5.5 compatibility

WordPress 5.5 introduces a breaking change for CiviCRM. This issue was fixed in CiviCRM 5.26. Please ensure that you upgrade to CiviCRM 5.26 or later *before* you upgrade to WordPress 5.5 or later.

After upgrading to CiviCRM 5.26 you may need to update the URLs you use for payment processors etc.

Read this blog post for more details of the change: [CiviCRM 5.26 and WordPress Important Notice](https://civicrm.org/blog/kcristiano/civicrm-526-and-wordpress-important-notice)

## CiviCRM 5.0

### Flush CiviCRM cache

After upgrading from CiviCRM 4.7.31, the cache must be flushed to resolve a mailing bug in the generated javascript. The upgrade web interface will take care of this automatically, but if you are running the database migration on the command-line, run `cv flush` to cleanup caches.

## CiviCRM 4.3

### Settings changes

**Background:** Settings are usually stored in the civicrm_setting table, where they're easily maintained. But there are occasions when developers might find it useful to override them. For instance, the development environment might mirror the production environment, except for a handful of settings. Adding a few lines to the civicrm.settings.php file can be much easier and less error-prone than changing production settings for development.

The settings in the `civicrm_setting` table are keyed on `domain`, `group`, and `name`. Here's an example using the CiviCRM 4.1 mechanism:

```
define('URL Preferences.customCSSURL', 'http://example.com/css');...
```

The `domain` is determined by the civicrm.settings.php file, the _group_ is 'URL Preferences', the _name_ is 'customCSSURL', and the `value` is `http://example.com/css`. If you're uncertain of the valid values these can take, inspect the `civicrm_setting` table.

**The change:** In CiviCRM 4.3 and later, the format has changed to:

```
global $civicrm_setting;
```

```
$civicrm_setting['URL Preferences']['customCSSURL'] = 'http://example.com/css';...
```

### Password must be supplied to cron

If you are running scheduled jobs using `CLI.php`, you will need to reconfigure cron to include a password. Scheduled jobs will no longer run if the password is not provided..

## CiviCRM 4.2

All CiviCRM-related cron jobs will stop working as soon as any site is upgraded from 4.1.x and below. If you are upgrading from a version prior to 4.2, cron jobs will need to be reconfigured using the new [Scheduled Jobs](../setup/jobs.md) method.

<!-- Source: upgrade/version-specific.md -->
