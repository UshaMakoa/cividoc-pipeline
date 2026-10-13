---
title: Sync CiviCRM memberships to Backdrop roles
category: how-to
topic: system-administration
subtopic: membership-role-sync
component: CiviMember Roles Sync
audiences:
- technical
- administrator
- operations-user
- membership-manager
level: intermediate
journey_stage: manage-and-automate
summary: Configure membership-to-role associations and choose when Backdrop roles are synchronized.
extensions: []
related: []
review_priority: medium
review_notes:
- The source describes CiviMember Roles Sync as now part of the core Backdrop CiviCRM package without dating that statement.
- The Corporate Sponsor example contains the unclear wording “RBA decides calls”; it has been left unchanged.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: integration/backdrop/index-part3.md
destination_path: sysadmin/integration/backdrop/index-part3.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/integration/backdrop/index-part3/
civicrm_version:
- latest
last_modified: '2026-07-02'
---

# Sync CiviCRM memberships to Backdrop roles

A common need is to synchronize CiviCRM members to Backdrop roles so that, among other things, website content is accessible only to current members as defined by the rules and types set up in CiviCRM.

The CiviMember Roles Sync module is now part of the core Backdrop CiviCRM package. It allows administrators of Backdrop Websites to:

- Automatically grant a Backdrop Role based on a user's membership type and whether the user is currently in good standing.
- Allow a user to access member-only content or perform member-only tasks.
- Restrict a non-member or expired member from accessing member-only content or performing member-only tasks until they register or renew their membership.

## Scenario: member-only content

The Retail Baker's Association of America (RBA) connects bakery suppliers and owners across the country to foster a community that encourages the exchange of business and industry information, networking, mentoring, and business opportunities, and establishes industry standards through certification, research, and school programs.

Visitors to its website have three different experiences:

- Non-Members purchase resources and materials from RBA's online boutique. A non-Member must register for a user account to make a transaction so that they can track their purchase history and RBA can petition them for membership in the future.
- Current members in good standing can access member-only resources, including discussion boards, programs, marketing materials, and digital versions of RBA publications.
- Members with expired memberships or former members need to log into the RBA website to renew, but should not have access to member-only resources until their membership has been reactivated.

Rather than have staff grant the Backdrop Role &quot;Active Member&quot; each time a user renews and remove it when a user cancels or lets a membership expire, RBA uses CiviMember Role Sync. It grants &quot;Active Member&quot; to new or current members and to users whose membership has entered the grace period. When a user registers or renews, they are automatically granted access to RBA's Member-Only web content.

## What you need to know

Before working with CiviMember Role Sync, assess how different users interact with your website. Consider whether the use case depends on your membership structure; on committees, teams, and contacts meeting specific criteria; or whether your workflow does not warrant CiviMember Role Sync at all.

### CiviCRM Membership Types

You should understand CiviCRM Membership Types and CiviCRM Membership Statuses before working with the CiviMember Role Sync module. You can learn more about the CiviMember component in the **MEMBERSHIP** chapter.

## Configure CiviMember Roles Sync

Before using CiviMember Roles Sync module:

- Create and configure your organization's Membership Types and Membership Statuses in the CiviMember component.
- Create the Backdrop roles needed for each use case.
- Agree with your staff on what content each Membership Type should grant permissions to.
- Agree with your staff on what tasks each Membership Type should grant permission to.
- If you use additional modules to fine-tune access, install and configure all the modules you need.

Multiple Membership Types may grant the same Backdrop Role, and each Membership Type can grant multiple Backdrop roles.

*For example: The Retail Bakers Association of America has five different membership types: Corporate Sponsor, Bakery, Individual, Student, and Retired Bakery. Having any one of the five Membership Types will grant a user the &quot;Active Member&quot; Backdrop Role that gives access to the member-only content. In addition to this, users with the Corporate Sponsor Membership Type should have access to additional exclusive content. RBA decides calls the Backdrop role used to access this additional exclusive content &quot;Corporate Member&quot; and user with the Corporate Sponsor Membership Type will be granted the &quot;Corporate Member&quot; role in addition to the &quot;Active Member&quot; role.*

### Enable CiviMember Roles Sync Module

1. Navigate to your list of installed Backdrop modules: go to **Functionality** from the Administration Menu at the top of your screen (**/admin/modules**).
2. Find the Module **CiviMember Roles Sync** and check the box to the left of its name.
3. Click **Save Configuration**.

### Sync CiviCRM Membership Types to Backdrop Roles

1. Navigate to the CiviMember Role Sync configuration screen: **Configuration &gt; CiviCRM &gt; CiviMember Roles Sync**.
2. Click **Add Association Rule.**
3. Under **Select a CiviMember Membership Type**, select the Membership Type a user must have to receive a specific Backdrop Role.

    *Example: RBA wants any user with a Current Bakery Membership Type to be granted the &quot;Active Member&quot; role, so the RBA staff creates a new Association Rule and selects Bakery under Select a CiviMember Membership Type and selects &quot;Active Member&quot; under Select a Backdrop Role.*

4. Under **Select a Backdrop Role**, select the Backdrop Role to grant.
5. Under **Current Status**, select the Membership Status a user must have to receive the selected Backdrop Role.

    *Example: RBA wants to grant any user who has a Membership Status of either New, Current, or Grace access to the member-only website content, so the RBA staff checks the boxes next to those three Membership Statuses.*

6. Under **Expired Status**, select the Membership Status that will revoke the Backdrop Role from the user.

    *Example: RBA wants to make sure that any user whose membership expires or who cancels their membership has their access to the member-only website content revoked, so the RBA staff checks the boxes next to Expired and Canceled.*

7. Click **Add Association Rule** when you have finished configuring the new association rule.
8. The page will reload. You should see the message &quot;Your Association Rule has been added.&quot;
9. Repeat the steps above to add all necessary association rules for your organization.
10. Click the **Manually Synchronize** tab.
11. Click **Synchronize CiviMember Membership Types to Backdrop Roles Now**. This puts your new CiviMember Role Sync Association Role immediately into effect.

### Edit or delete existing association rules

1. Navigate to the CiviMember Role Sync configuration screen: **Configuration &gt; CiviCRM &gt; CiviMember Roles Sync**.
2. You should see a list of all existing CiviMember Role Sync Association Rules. If not, click the **List Association Rule(s)** tab.
3. To edit an Association Rule, find it and click **edit**. Make your changes, then click **Edit association rule**.
4. To delete an Association Rule, find it and click **delete**. Your association rule will be deleted; you will not need to confirm deletion.

### Configure when synchronization should happen

Navigate to the CiviMember Role Sync Configure screen at **Configuration &gt; CiviCRM &gt; CiviMember Roles Sync &gt; Configure** to select when synchronization occurs.

#### Automatic synchronization methods

- **Synchronize whenever someone logs in or logs out:** Synchronization happens only after a user logs in or out. Be careful with this method: if user sessions are long, a user could retain access to actions or content until they log out. This is the default setting.
- **Synchronize when a Backdrop Cron occurs:** A cron triggers synchronization.
- **Synchronize when membership is updated:** Synchronization happens when a user registers for or renews their membership, or when organization staff update a user's membership information from the back office.
- **Disable Automatic Synchronization:** An organization staff member must manually trigger synchronization. Go to **CiviMember Roles Sync settings**, click the Manually Synchronize tab, and click Synchronize CiviMember Membership Types to Backdrop Roles Now.

Click **Save Configuration** after making any changes.

!!! tip
    Test the module by creating a test user with a test CiviCRM membership and an association rule for that type. Log in as that user to check that they receive the appropriate role. Then remove the membership from the user's CiviCRM record, log back in as the test user, and check that they no longer have that role.

<!-- Source: integration/backdrop/index-part3.md -->
