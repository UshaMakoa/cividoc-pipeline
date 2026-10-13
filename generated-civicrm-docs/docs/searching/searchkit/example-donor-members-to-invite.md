---
title: Create an invitation list for donor members
category: how-to
topic: searchkit
subtopic: donor-member-invitation-list
component: SearchKit
audiences:
- operations-user
- event-manager
- fundraising-manager
- membership-manager
level: intermediate
journey_stage: everyday-tasks
summary: Build a SearchKit invitation list of current members who are major donors and have no event participant record.
extensions: []
related: []
review_priority: low
review_notes:
- The Having condition names "(Sum) Contact Contibution", which appears to contain a typo. The field name is retained as written
  pending verification.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: searching/searchkit/example-donor-members-to-invite.md
destination_path: searching/searchkit/example-donor-members-to-invite.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/searching/searchkit/example-donor-members-to-invite/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Create an invitation list for donor members

This example builds an invitation list for members who are major donors and have not previously attended an event.

## Step 1: Select current members

On the SearchKit page, click **New Search** and choose a base entity in **Search for**. The base entity cannot be changed once the search has been saved.

![First entity](../../img/search-kit/members-to-invite-empty.png)

You could start with Contacts and link Memberships, or start with Memberships and link Contacts. Because the goal is a list of contacts, select **Contacts** from **Search for**. Change **With (optional)** to **With (required)**, then select **Memberships** from **+Entity**.

To include only active members, go to **Where** and change Status to **is one of** New and Current.

![Contacts and Memberships and Where](../../img/search-kit/members-to-invite-entities.png)

Enter a name for the search and click **Save**. You can click **Search** to preview the results.

## Step 2: Find members with no event participant record

To find members who have never attended an event, look for contacts without a participant record. Change a second **With (optional)** field to **Without** and select Contact Participants.

![Participants](../../img/search-kit/members-to-invite-participants.png)

## Step 3: Add donors and sum their contributions

Change a third **With (optional)** to **With (required)** and select Contact Contributions. Under **Where**, add a clause that sets Financial Type **=** Donation.

![Contributions](../../img/search-kit/members-to-invite-contributions.png)

A contact may have multiple donations. To list each contact only once, select Contact ID from **Group By**.

![Group By](../../img/search-kit/members-to-invite-group-by.png)

Using Group By enables a Field Transformation, such as combine, count, or sum. To sum each contact's contributions, click **+Add** and select **Total Amount** to add it to the search results. Under **Field Transformation** above the results, select **Sum** from the drop-down menu next to the Total Amount field.

![Sum](../../img/search-kit/members-to-invite-sum.png)

## Step 4: Filter for major donors

To include donors who have contributed at least a specified amount, add a condition on the sum of the total amount. Because the condition uses a field transformation, use **Having** instead of **Where**. Set (Sum) Contact Contibution to greater than or equal to the specified amount.

![Having](../../img/search-kit/members-to-invite-having.png)

## Step 5: Add email and phone number

Add the contact's primary email and phone number as entities for the invitation list.

![Phone and Email](../../img/search-kit/members-to-invite-phone-email.png)

!!! Note:
    * Not every contact may have an email or phone number in the database, so **With (optional)** is recommended.
    * A contact may have specified that they do not want to be phoned or emailed. This is shown on their Contact Summary and needs to be taken into account.

The configured search results will likely look something like this:

![Result](../../img/search-kit/members-to-invite-result.png)

## Step 6: Export as a CSV file

Click **Actions** above the search results to see available actions, including downloading the data as a spreadsheet (CSV file).

![Export as CSV](../../img/search-kit/members-to-invite-download.png)

<!-- Source: searching/searchkit/example-donor-members-to-invite.md -->
