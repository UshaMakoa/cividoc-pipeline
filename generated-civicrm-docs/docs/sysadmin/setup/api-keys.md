---
title: API keys
category: how-to
topic: system-administration
subtopic: assigning-keys
component: CiviCRM API
audiences:
- technical
level: intermediate
journey_stage: plan-and-configure
summary: Choose a contact and assign a unique API key using an extension, an API explorer, the CLI, or MySQL.
extensions:
- API Key Extension
related: []
review_priority: low
review_notes:
- The CLI and MySQL code blocks contain HTML entities in place of quotation marks. They are preserved as supplied, but the
  commands may not run if copied.
guide: sysadmin
source_repository: https://lab.civicrm.org/documentation/docs/sysadmin.git
source_path: setup/api-keys.md
destination_path: sysadmin/setup/api-keys.md
legacy_urls:
- https://docs.civicrm.org/sysadmin/en/latest/setup/api-keys/
civicrm_version:
- latest
source_commit: 67f502eac2321850796b712f4699fca5e05a1201
last_modified: '2026-07-02'
---

# API keys

## Overview

If a third-party application needs to read or write data in CiviCRM, you may need to generate an *API key*.

Each API key is attached to a specific **contact record** or **user account**, which determines the [permissions](https://docs.civicrm.org/dev/en/latest/security/permissions/). When configuring a new application, determine the contact ID and double-check their roles or permissions.

Each API key must be **unique** and **difficult to guess**. To generate a good API key, use a random sequence of 20+ alphanumeric characters.

## Assigning keys

Once you have identified a suitable **contact record**, you can assign a key through any of the following tools:

### &quot;API Key&quot; Extension

The optional [API Key Extension](https://civicrm.org/extensions/api-key) provides a simplified web interface for managing keys.

![API Key Extension](https://civicrm.org/sites/civicrm.org/files/API_key.png)

### APIv3 and APIv4 Explorer

The &quot;APIv3 Explorer&quot; and &quot;APIv4 Explorer&quot; provide a built-in way to manipulate CiviCRM data through the administrator interface.

See [&quot;Stack Exchange: How do I set up an API key for a user?&quot;](http://civicrm.stackexchange.com/questions/9945/how-do-i-set-up-an-api-key-for-a-user)

### CLI

If you have shell access and [cv](https://github.com/civicrm/cv), you can generate and assign API keys:

1. Generate a random key:

    ```bash
    head -c32 /dev/urandom | base64 | tr -d &#39;+/=&#39;
    ```
    ```bash
    T0PS3CR3T6ateeUXgTOJ9e3PpXvDZF9Al55WAmBsNQI
    ```

2. Assign this new value to the contact. In this example, we update contact `#100`:

    ```bash
    cv api contact.create id=100 api_key=&quot;T0PS3CR3T6ateeUXgTOJ9e3PpXvDZF9Al55WAmBsNQI&quot;
    ```

### MySQL

If you have direct access to the MySQL database, you can generate and assign API keys:

1. Generate a random key:

    ```sql
    SELECT @api_key := REPLACE(REPLACE(REPLACE(
      TO_BASE64(RANDOM_BYTES(32)), &quot;+&quot;, &quot;&quot;), &quot;/&quot;, &quot;&quot;), &quot;=&quot;, &quot;&quot;) AS api_key;
    ```
    ```sql
    +---------------------------------------------+
    | api_key                                     |
    +---------------------------------------------+
    | T0PS3CR3T6ateeUXgTOJ9e3PpXvDZF9Al55WAmBsNQI |
    +---------------------------------------------+
    ```

2. Assign this new value to the contact. In this example, we update contact `#100`:

    ```sql
    UPDATE civicrm_contact SET api_key = @api_key WHERE id = 100;
    ```

<!-- Source: setup/api-keys.md -->
