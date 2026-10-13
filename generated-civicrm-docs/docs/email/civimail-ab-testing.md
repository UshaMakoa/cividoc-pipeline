---
title: CiviMail A/B testing
category: how-to
topic: mailings
subtopic: a-b-tests
component: CiviMail
audiences:
- communications-manager
level: basic
journey_stage: everyday-tasks
summary: Create a CiviMail A/B test, review its results, and select a final mailing.
extensions: []
related: []
review_priority: low
review_notes: []
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: email/civimail-ab-testing.md
destination_path: email/civimail-ab-testing.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/email/civimail-ab-testing/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# CiviMail A/B testing

CiviMail A/B Testing lets you send two test e-mails to two random samples of your recipients. After the test mailings are complete, you can use the available metrics to choose which mailing to send to the remaining recipients.

Before conducting a new A/B Test, put your recipients in a Mailing List. To learn more about configuring a Mailing List, see the chapters on *Groups and Tags*.

## Create a new A/B test

1. Navigate to **Mailings > New A/B Test**.
2. On the Setup screen, define the campaign that corresponds with the mailing and select the type of test. You can test:
   - Different **Subject** lines
   - Different **From** lines
   - Entirely different emails

   ![screenshot](../img/ab_testing.png)

3. On the Target screen, define your recipients and the distribution percentage. Drag the blue percentage bar to change the percentage of test mailings and, in turn, the percentage of final mailings sent to the remaining participants. The test mailings and final mailing sum to 100%.

   ![screenshot](../img/ab_testing_targeting.png)

4. On the Compose screen, enter the fields for your chosen test type. The screen changes depending on the type of A/B Test:
   - For different **From** lines, enter From (A) and From(B).

     ![screenshot](../img/ab_testing_compose_screen1.png)

   - For different **Subject** lines, enter Subject(A) and Subject(B).

     ![screenshot](../img/ab_testing_by_subject1.png)

   - For entirely different emails, add a **From** and **Subject** for each mailing.

     ![screenshot](../img/ab_testing_by_email1.png)

5. Choose an email template that you have previously composed. Once you have selected the template and specified the From and Subject field, send a test email before scheduling or sending your final mailing.

## Review results and select a final mailing

Once the test mailings are complete, navigate to **Mailings > Manage A/B Tests** and select **Results**. On the A/B Test Results screen, monitor the results and select which mailing should be submitted as the Final mailing.

![screenshot](../img/ab_testing_results_page1.png)

![screenshot](../img/ab_testing_metrics.png)

<!-- Source: email/civimail-ab-testing.md -->
