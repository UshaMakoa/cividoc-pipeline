---
title: Using your own font or CJK characters in PDF output
category: how-to
topic: installation
subtopic: unicode-fonts
component: CiviCRM PDF output
audiences:
- technical
- administrator
level: intermediate
journey_stage: plan-and-configure
summary: Add a web font or locally stored font for CJK characters in PDF output.
extensions: []
related: []
review_priority: medium
review_notes:
- The Unicode support statement names CiviCRM 6.0 and may need review as versions change.
guide: installation
source_repository: https://lab.civicrm.org/documentation/docs/installation.git
source_path: general/unicode_pdf.md
destination_path: installation/general/unicode_pdf.md
legacy_urls:
- https://docs.civicrm.org/installation/en/latest/general/unicode_pdf/
civicrm_version:
- latest
source_commit: 5a8b870477f63bea90551acb2f7516df67784b19
last_modified: '2026-08-20'
---

# Using your own font or CJK characters in PDF output

As of CiviCRM 6.0, most unicode characters will output correctly in PDFs. But if you need CJK characters, DejaVu does not contain those, so you will need to install another font file such as SimSun using the steps below.

If you are still seeing question marks (?) in place of unicode characters, even for non-CJK characters, check that you don't have a `<font>` tag or `style` attribute in the html specifically setting a font that doesn't support unicode.

## Option A: Using web fonts

1. In your html template add a `<link>` tag like the following, e.g. for the Noto Sans SC font: `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@100..900">`
1. Specify the font using CSS in the templates where you use the CJK characters. You can use the Source button in CKEditor to do this and type it directly into the HTML: e.g. `<p style="font-family: Noto Sans SC;">的</p>`

## Option B: Storing fonts locally

Option A will cache a version of the file after the first download, but it may not be available on the internet or may be a commercial font.

1. Create a folder in a location that won't get overwritten when you upgrade, e.g. sites/default/fonts for Drupal.
1. Copy the .ttf font file you want to use into that folder.
1. Run `php -r 'require_once "/path/to/civicrm/vendor/autoload.php"; $f = \FontLib\Font::load("/full/path/to/the/ttf/file"); $f->parse(); $f->saveAdobeFontMetrics("/full/path/to/output/ufm/file");'`
    * e.g. `php -r 'require_once "/var/www/sites/all/modules/civicrm/vendor/autoload.php"; $f = \FontLib\Font::load("/var/www/sites/default/fonts/simsun.ttf"); $f->parse(); $f->saveAdobeFontMetrics("/var/www/sites/default/fonts/simsun.ufm");'`
1. Create a file in that folder called `installed-fonts.json` that looks like this:
    ```json
    {
        "simsun": {
            "normal": "simsun"
        }
    }
    ```
1. Visit Administer - System Settings - Misc and in the field for DOMPDF Font Folder put the full path to the font folder you created in step 1.
1. Specify the font using CSS in the templates where you use the CJK characters. You can use the Source button in CKEditor to do this and type it directly into the HTML: e.g. `<p style="font-family: simsun;">的</p>`

Fonts you set up here are in addition to the ones distributed with dompdf/CiviCRM. You do not need to copy those core fonts over or add entries in this json file to use them.

<!-- Source: general/unicode_pdf.md -->
