---
title: Synchronize CiviCRM memberships with Drupal roles
category: how-to
topic: system-administration
subtopic: membership-to-role-synchronization
component: CiviMember Roles Sync
audiences:
- technical
- administrator
- operations-user
- membership-manager
level: intermediate
journey_stage: manage-and-automate
summary: Configure membership-to-role association rules and choose when CiviMember Roles Sync runs.
extensions: []
related: []
review_priority: medium
review_notes:
- The instructions give Drupal 6 and Drupal 7 menu paths, which may leave readers on other versions unable to follow the task.
- The example lists “Bakery” as a membership type but later calls it “Current Bakery Membership Type”; the intended type is
  unclear.
- The source uses both “Association Rule” and “Association Role” for the newly configured association.
- The source calls the organization both “Retail Baker's Association of America” and “Retail Bakers Association of America.”
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: integration/drupal/index-part4.md
destination_path: sysadmin/integration/drupal/index-part4.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/integration/drupal/index-part4/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# Synchronize CiviCRM memberships with Drupal roles

A common need is to synchronize CiviCRM members with Drupal roles so that, among other things, website content is accessible only to current members as defined by the rules and types set up in CiviCRM.

The CiviMember Roles Sync module is now part of the core Drupal CiviCRM package. It lets administrators of Drupal Websites:

- Automatically grant a Drupal Role to a user based on their membership type and whether they are currently in good standing.
- Allow a user to access member-only content or perform member-only tasks.
- Restrict a non-member or expired member from accessing member-only content or performing member-only tasks until they register or renew their membership.

## Scenario: member-only content

The Retail Baker's Association of America (RBA) connects bakery suppliers and owners across the country to foster a community that encourages the exchange of business and industry information, networking, mentoring, and business opportunities, and to establish industry standards through certification, research, and school programs.

Visitors to its website have three different user experiences:

- Non-Members purchase resources and materials from RBA’s online boutique. A non-Member must register for a user account to make a transaction so they can track their purchase history and RBA can petition them for membership in the future.
- Current members in good standing can access member-only resources, including discussion boards, programs, marketing materials, and digital versions of RBA publications.
- Members with expired memberships or former members need to log in to renew, but should not have access to member-only resources until their membership is reactivated.

Rather than having staff grant the Drupal Role "Active Member" each time a user renews and remove it when a user cancels or lets their membership expire, RBA uses CiviMember Role Sync. It grants the "Active Member" role to new or current members and to users whose membership has entered the grace period. When a user registers or renews, they are automatically granted access to RBA’s Member-Only web content.

## What you need to know

Before working with CiviMember Role Sync, assess how different users interact with your website. Consider whether the use case depends on your membership structure, on the organization of committees or teams, on contacts meeting specific criteria, or whether your workflow warrants using CiviMember Role Sync at all.

### CiviCRM membership types

You should fully understand CiviCRM Membership Types and CiviCRM Membership Statuses before working with the CiviMember Role Sync module. You can learn more about the CiviMember component in the **MEMBERSHIP** chapter.

## Configuring CiviMember roles sync

Before using CiviMember Roles Sync module, prepare the following:

- Create and configure your organization’s Membership Types and Membership Statuses in the CiviMember component.
- Create the roles needed for each use case in Drupal.
- Agree with your staff on which content each Membership Type should grant permissions to.
- Agree with your staff on which tasks each Membership Type should grant permission to.
- If you use additional modules to fine-tune access, install and configure all the modules you need.

When determining which Membership Types and Drupal Roles to create, remember that multiple Membership Types may grant the same Drupal Role, and each Membership Type can grant multiple Drupal roles.

*For example: The Retail Bakers Association of America has five different membership types: Corporate Sponsor, Bakery, Individual, Student, and Retired Bakery. Having any one of the five Membership Types grants a user the "Active Member" Drupal Role, which gives access to member-only content. Users with the Corporate Sponsor Membership Type should also have access to additional exclusive content. RBA calls the Drupal role for this content "Corporate Member"; a user with the Corporate Sponsor Membership Type is granted the "Corporate Member" role in addition to the "Active Member" role.*

### Enabling CiviMember Roles Sync Module

1. Navigate to your list of installed Drupal modules:
   - Drupal 6: Go to **Administer > Site Building > Modules**
   - Drupal 7: Go to **Modules** from the Administration Menu at the top of your screen.
2. Find the Module **CiviMember Roles Sync** and check the box to the left of the module’s name.
3. Click **Save Configuration**.

### Syncing CiviCRM membership types to Drupal roles

1. Navigate to the CiviMember Role Sync configuration screen:
   - Drupal 6: Go to *Administer > Site Configuration > CiviMember Roles Sync*
   - Drupal 7: Go to *Configuration > CiviMember Roles Sync*
2. Click **Add Association Rule.**
3. Under **Select a CiviMember Membership Type**, select the Membership Type that you want a user to have in order to be granted a specific Drupal Role.

   *Example: RBA wants any user with a Current Bakery Membership Type to be granted the "Active Member" role, so the RBA staff creates a new Association Rule and selects Bakery under Select a CiviMember Membership Type and selects "Active Member" under Select a Drupal Role.*

4. Under **Select a Drupal Role**, select the Drupal Role that should be granted.
5. Under **Current Status**, select the Membership Status that a user should have to be granted the selected Drupal Role.

   *Example: RBA wants to grant any user who has a Membership Status of either New, Current, or Grace access to the member-only website content, so the RBA staff checks the boxes next to those three Membership Statuses.*

6. Under **Expired Status**, select the Membership Status that will revoke the Drupal Role from the user.

   *Example: RBA wants to make sure that any user whose membership expires or who cancels their membership has their access to the member-only website content revoked, so the RBA staff checks the boxes next to Expired and Canceled.*

7. Click **Add Association Rule** when you have finished configuring the new association rule.
8. The page will reload, and you should see the message "Your Association Rule has been added."
9. Repeat the steps above to add all necessary association rules for your organization.
10. Click the **Manually Synchronize** tab.
11. Click **Synchronize CiviMember Membership Types to Drupal Roles Now**. This puts your new CiviMember Role Sync Association Role immediately into effect.

### Editing existing association rules

You can edit or delete existing association rules.

1. Navigate to the CiviMember Role Sync configuration screen:
   - Drupal 6: Go to *Administer > Site Configuration > CiviMember Roles Sync*
   - Drupal 7: Go to *Configuration > CiviMember Roles Sync*
2. You should see a list of all existing CiviMember Role Sync Association Rules. If not, click the **List Association Rule(s)** tab.
3. To edit an existing Association Rule:
   - Find the Association Rule you want to change and click **edit** for that Association rule.
   - Make your changes and click **Edit association rule**.
4. To delete an Association Rule:
   - Find the Association Rule you want to remove and click **delete** for that Association Rule.
   - Your association rule will be deleted. You will not need to confirm deletion.

### Configure when synchronization should happen

You can select different options for when synchronization occurs on the CiviMember Role Sync Configure screen:

- Drupal 6: Go to **Administer > Site Configuration > CiviMember Roles Sync > Configure**
- Drupal 7: Go to **Configuration > CiviMember Roles Sync > Configure**

#### Automatic synchronization methods

- **Synchronize whenever someone logs in or logs out:** Synchronization occurs only after a user logs in or out. Be careful with this method: if you have long user sessions, a user could continue to have access to actions or content until they log out. This is the default setting.
- **Synchronize when a Drupal Cron occurs:** A cron triggers synchronization. [Learn more about Drupal Cron.](http://drupal.org/cron)
- **Synchronize when membership is updated:** Synchronization occurs when a user registers for or renews their membership, or when organization staff update a user’s membership information from the back office.
- **Disable Automatic Synchronization:** An organization staff member must trigger synchronization manually. Go to **CiviMember Roles Sync settings**, click the Manually Synchronize tab, and click Synchronize CiviMember Membership Types to Drupal Roles Now.

Click **Save Configuration** after making any changes.

!!! tip
    Test this module by creating a test user with a test CiviCRM membership and an association rule for that type. Log in as that user to check that you have been granted the appropriate role. Then take away the membership in the user’s CiviCRM record, log back in as the test user, and check that you no longer have that role.

<!-- Source: integration/drupal/index-part4.md -->
