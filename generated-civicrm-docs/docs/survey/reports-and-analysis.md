---
title: Survey reports and analysis
category: how-to
topic: campaigns
subtopic: reports-and-analysis
component: CiviSurvey
audiences:
- communications-manager
- operations-user
level: basic
journey_stage: reports-and-review
summary: Use the Survey Report (Detail) to analyse survey results.
extensions: []
related: []
review_priority: medium
review_notes:
- Step 2 presents selecting a report template or clicking a survey name on the survey dashboard after step 1; the relationship
  between these routes is unclear.
- The final paragraph refers to criteria indicated in the survey responses area, but this page does not identify where those
  criteria are set.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: survey/reports-and-analysis.md
destination_path: survey/reports-and-analysis.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/survey/reports-and-analysis/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Survey reports and analysis

You can use the Survey Report (Detail) to analyse the results of your surveys.

## Review survey results in a report

1. Go to **Administer &gt; CiviReport &gt; Create New Report from Template.**
2. Under **Campaign Report Templates** select **Survey Report (Detail)** or click on a survey name on the survey dashboard.
3. On the **Columns** tab, check the boxes for **Survey Responses** and anything else you want to view in the report, such as Street Number and Street Name.
4. On the **Filters** tab, by Survey select the name of your survey, and in **Respondent Status** select **Interviewed**.

    ![image](../img/survey_set_filters.png)

5. There will be another drop-down area that will be named after your custom data set of questions. You can select responses to questions to limit your report, for example to show all the "yes" responses to one of your questions.
6. Click **Preview Report**.
7. In the **Survey Report (Detail) - Template** screen, you can view the results. You can also export the report information to a CSV file if you want more detailed reporting.

![image](../img/survey_report_detail.png)

If you would like to see a formatted report with the cover sheet of questions and responses and the street names in ascending order (as you indicated in the survey responses area criteria) then click **Print Preview**.

![image](../img/survey_report_cover.png)

![image](../img/survey_report_p2.png)

<!-- Source: survey/reports-and-analysis.md -->
