---
title: Cancelling and expiring memberships
category: how-to
topic: memberships
subtopic: cancelling-expiring-and-deleting
component: CiviMember
audiences:
- membership-manager
- operations-user
level: basic
journey_stage: everyday-tasks
summary: Change a membership to Cancelled or Expired while retaining its history, or delete a membership entered in error.
extensions: []
related: []
review_priority: medium
review_notes:
- The path **Memberships &gt; Find Members &gt;** ends with a separator, so its final destination is unclear.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: membership/cancelling-and-expiring-memberships.md
destination_path: membership/cancelling-and-expiring-memberships.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/membership/cancelling-and-expiring-memberships/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Cancelling and expiring memberships

If a contact resigns or cancels their membership, change its status to Cancelled or another status that is not considered current rather than deleting it. This retains the contact's membership history and any contribution records attached to the membership.

If a contact's membership is in a grace period and you know they will not continue for another period, you can manually change its status to Expired rather than Cancelled, since they completed the membership period.

To cancel or manually expire a membership:

1. Search for the contact, click the **Membership** tab, then click **Edit** next to the membership record.
2. On the membership edit screen, check the **Status Override box** and select the appropriate **Membership Status**, such as Cancelled or Expired.

![image](../img/z_sprint14_Membership_Status_Override_8.png)

Manually expiring memberships may not be necessary. Depending on how the membership status rules are set up under **Administer &gt; CiviMember &gt; Membership Status Rules**, memberships automatically expire based on timeline criteria.

## Deleting memberships

Delete a membership only if it was entered in error. For example, if you made Jo Smith a member instead of Joe Smith, you would remove Jo Smith's incorrect membership and any linked contribution record.

Deleting a membership completely removes it and any linked contributions from the database. **This action cannot be undone**, so give permission to delete memberships only to trusted staff.

You can delete membership records in either of these ways:

- Search for the contact, click the **Membership** tab, click **More** next to the membership record, then click **Delete**.
- Click **Memberships &gt; Find Members &gt;**, enter your criteria, then select the membership records from the "Find Members" results screen and click **Delete**.

![image](../img/z_sprint14_Deleting_memberships.png)

<!-- Source: membership/cancelling-and-expiring-memberships.md -->
