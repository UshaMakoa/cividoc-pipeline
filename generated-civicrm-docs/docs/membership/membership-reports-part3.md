---
title: Export membership records
category: how-to
topic: data-management
subtopic: exporting-records
component: Membership
audiences:
- membership-manager
- operations-user
level: basic
journey_stage: reports-and-review
summary: Export membership records using primary fields or a selection of fields.
extensions: []
related:
- finding-and-viewing-memberships.md#searching
review_priority: low
review_notes:
- The source says to select records you want to import during an export procedure; verify the intended wording.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: membership/membership-reports-part3.md
destination_path: membership/membership-reports-part3.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/membership/membership-reports-part3/
civicrm_version:
- latest
last_modified: '2026-10-06'
---

# Export membership records

You can export membership records for further analysis, document mail merges, or reports outside CiviCRM. You can export a default set of primary fields or choose fields specific to the membership record.

First, [search for the specific membership records](finding-and-viewing-memberships.md#searching) you would like to export.

1. Click on **Memberships &gt; Find Members** and enter your search criteria.
2. On the "Find Members" search results screen, select the records you want to import. In the **-actions-** drop down, select **Export Members**.
3. Select **Export PRIMARY fields** or **Select fields for export**, then click **Continue**.

![image](../img/memberships_export_memberships_screen.png)

- If you selected **Export PRIMARY fields**, a file called `CiviCRM_Member_Search.csv` will be created containing the membership records based on your search criteria.
- If you selected **Select fields for export**, include the fields you would like to export. Check **Save this field mapping** if you want to re-use this field mapping for a future export, then click **Export**. A file called `CiviCRM_Member_Search.csv` will be created containing the membership records based on your search criteria and the fields you selected to export.

![image](../img/memberships_select_fields_to_export.png)

<!-- Source: membership/membership-reports-part3.md -->
