---
title: Bug reporting
category: how-to
topic: reporting
subtopic: investigating-and-reporting-bugs
component: CiviCRM
audiences:
- operations-user
- administrator
- technical
level: basic
journey_stage: reference-and-troubleshooting
summary: Check possible causes of a problem, try to reproduce it, and provide the details needed for a useful bug report.
extensions: []
related: []
review_priority: low
review_notes:
- The page links to Stack Exchange but later tells readers to write to a forum without identifying whether it means Stack
  Exchange.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: the-civicrm-community/bug-reporting.md
destination_path: the-civicrm-community/bug-reporting.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/the-civicrm-community/bug-reporting/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Bug reporting

As with all software, there may be times when CiviCRM doesn't work the way you expect it to.

A good first step is to search the question-and-answer site [Stack Exchange](https://civicrm.stackexchange.com/) for similar problems and follow advice given there. If your problem hasn't been addressed, posting a question about it is probably the right thing to do.

When posting, be detailed and specific about the software you are using: the version of CiviCRM, your CMS platform and its version, and your browser and its version. Explain what you are trying to do and how you are trying to do it. For example, sharing the URL you are using—with any confidential details removed—may help someone realise that you are configuring the wrong page. Unclear posts are less likely to get good replies.

## Using older versions of CiviCRM

If you are using an older version and your problem is a bug that has been fixed in the latest release, be prepared for the answer “it is time to upgrade to the latest version.” Although the CiviCRM community tries to be as helpful as possible and recognises that upgrading puts a burden on your organisation, it is difficult to support multiple versions simultaneously.

## What causes problems with CiviCRM?

Check the following possible sources of problems before reporting something on a forum. Isolating the problem can save you and others trouble. CiviCRM forums try to be friendly and don't criticise you for misjudging a problem, but checking first will help you get assistance and resolve problems faster.

- **Misunderstanding the software:** The documentation may not be perfect, but check it carefully when you hit a barrier. Frustration can make it hard to concentrate, so read slowly and thoroughly. Different parts of CiviCRM depend on each other; check related modules as well as the one where you think the problem lies.
- **Your server set up:** Servers can be configured in many ways, and their settings can change how CiviCRM operates. Depending on the issue, your server configuration may be the cause.
- **Older or unsupported versions of CiviCRM, PHP, and MySQL:** These may cause unpredictable errors. It is good practice to use the latest stable version of software.
- **Customisations to your installation's CiviCRM source code:** Changes to the source code may have unintended consequences. Community forums may be able to help, but you will need to be patient, share source code, and try suggestions. You may also want to ask your in-house development staff or outside consultant / service provider whether CiviCRM has been customised in a way that might relate to the problem.
- **Other newly installed and enabled modules or components:** Review additional modules and components that are not usually included in the install package. Check that you have their latest stable versions and that they work with your version of CiviCRM.
- **Bugs in the version of CiviCRM you are using:** After eliminating the previous possibilities, you can report the problem as a bug. The community appreciates bug reports because they help improve CiviCRM for everyone.

## Recreating your problem on the demo site

Try to recreate the bug on one of the [demo sites](http://demo.civicrm.org), selecting the demo site that matches your CiviCRM version. This helps determine whether the problem comes from the source code or from changes on your site. If the code on the demo site produces the bug, the CiviCRM source code is very likely the cause, and your demonstration will help others find and fix it.

No demo site can cover every possibility. Issues involving email output or payment processing cannot be recreated on the demo sites. A problem may still be a CiviCRM bug even if you cannot reproduce it there, though it is probably triggered by your server setup or other customisations.

Write to the forum and explain the problem. If you reproduced the bug on the demo site, describe exactly what you did and copy the demo site's URLs to document your steps. If you did not, provide as much information about your server setup as you feasibly can. Configuration files from the web server, CMS, and CiviCRM are valuable, but do not include sensitive information such as your database log-in.

If the forum suggests you have discovered a CiviCRM bug, you can report it to the [CiviCRM issue tracker](https://lab.civicrm.org/groups/dev/-/issues).

## Writing good bug reports

Give background and context. The way your organisation uses CiviCRM is likely to be specific to it, so more background can make your report more useful.

Clearly state:

- What you did
- What you expected to happen
- What actually happened
- Version of CiviCRM (must be included)
- Which CMS platform and CMS version (must be included)
- Which browser and browser version (must be included)
- Version of PHP and MySQL
- Screen shots of the errors or issue
- History of the bug
- The recreatibility of the bug—for example, whether it always happens, is reported by others but cannot be recreated consistently, or happens in one browser but not another

## Fixing bugs

The time it takes to fix a bug depends on its severity and complexity. A fix could be available the same day, or it could take much longer.

The easiest way to get bug fixes is to download and install the latest revision of CiviCRM. It is also possible to download bug fixes between releases and apply them to your existing software, a process called patching. If you have technical abilities, refer to the CiviCRM Developer's Guide for instructions on applying a patch. Otherwise, seek technical assistance to provide tests and a patch for the issue.

<!-- Source: the-civicrm-community/bug-reporting.md -->
