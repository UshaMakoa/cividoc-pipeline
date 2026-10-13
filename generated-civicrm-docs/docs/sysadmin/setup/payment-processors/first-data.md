---
title: First Data, Linkpoint, Global Gateway
category: how-to
topic: system-administration
subtopic: first-data
component: CiviCRM payment processors
audiences:
- technical
level: intermediate
journey_stage: plan-and-configure
summary: Configure First Data as a CiviCRM payment processor using a `.pem` certificate, an open port, a store number, and
  a server URL.
extensions: []
related: []
review_priority: medium
review_notes:
- The introduction says 'rever', which is unclear; verify what it means before changing the instruction.
- The certificate-path examples contain backticks around `.pem` inside the fenced code block; verify the intended filenames
  before changing them.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/payment-processors/first-data.md
destination_path: sysadmin/setup/payment-processors/first-data.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/payment-processors/first-data/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# First Data, Linkpoint, Global Gateway

This is a quick guide to implementing First Data, Aka. Linkpoint or Global Gateway as your payment processor in CiviCRM, unlike Authorize.net and Paypal, using First Data is slightly more complicated.

You will need to place a `.pem` certificate in your file system and correctly point your CiviCRM to it, you will have to open port 1129 on your rever and/or firewall, enter your store number, and finally make sure that the url to the payment processor is correct.

## `.pem` placement and implementation

First Data requires the placement of a `.pem` Certificate within your server file structure.

While the `.pem` Certificate may resemble an SSL Certificate, it has nothing to do with your standard SSL implementation. The `.pem` only serves as a handshake authentication between your server and the payment processor.

You should place it in a folder where your standard php user has read access, but preferably somewhere outside your web directory (not visible to the outside word). The filename is usually a ten digit integer with a `.pem` extension, and should be in ASCII format to be Linux readable.

!!! warning "certificate path"

    Once the `.pem` certificate is placed in the directory, make sure you insert the full certificate path into your CiviCRM payment processor configuration, starting from server root all the way out to the file location and including the file name.

    ```
    Bad:
    /linkpoint
    /linkpoint/1234567890`.pem`
    /home/site/public_html/linkpoint

    Good:
    /home/site/public_html/linkpoint/1234567890`.pem`
    ```

## Ports

First Data requires TCP port 1129 to be opened bidirectionally.

If you are not running a firewall you do not need to take this step!

On a Linux server you will likely have to modify your IP Tables, if you have root access to your server you can do this by using some of the quickguides.

CentOS/ RedHat

[http://wiki.centos.org/HowTos/Network/IPTables](http://wiki.centos.org/HowTos/Network/IPTables)

Ubuntu

[https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)

If you don't have root access to your server you will need host modify the IP Tables for you.

## Store number

When configuring the payment processor, you will be asked for your "store name" - you should enter the store number for your account (by default, it's the same as the `.pem` filename generated for you).

## Server URL

by default the First Data payment processor will reside at [https://secure.linkpt.net](https://secure.linkpt.net), make sure you have nothing after the .net (example of bad: [https://secure.linkpt.net/](https://secure.linkpt.net/))

<!-- Source: setup/payment-processors/first-data.md -->
