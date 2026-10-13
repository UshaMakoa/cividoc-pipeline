---
title: Mapping and geocoding
category: how-to
topic: general
subtopic: provider-configuration
component: Mapping and Geocoding
audiences:
- technical
- administrator
level: basic
journey_stage: plan-and-configure
summary: Configure mapping and geocoding providers and their keys.
extensions:
- https://civicrm.org/extensions/geocoder
related:
- scheduled-jobs.md#job_geocode
review_priority: low
review_notes:
- The phrase “you now require” is time-sensitive; confirm that the CARTO API key requirement remains accurate.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: initial-set-up/mapping.md
destination_path: initial-set-up/mapping.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/initial-set-up/mapping/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Mapping and geocoding

Visit **Administer > System Settings > Mapping and Geocoding** to configure mapping and geocoding providers.

**Mapping Provider**
Select the service used to build and display the maps shown in the CiviCRM UI.

**Mapping Provider Key**
Enter your API Key or Application ID for the selected mapping provider. For Google Maps, refer to developers.google.com for the latest information. For OpenStreetMaps, you now require an API key from CARTO.

!!! note "API Key for OpenStreetMaps usage"
    Maps under OpenStreetMaps rely on images from CARTO, which requires an API key. Without a valid API key, your maps may be repeatedly overlaid with an "API KEY REQUIRED" watermark.
    See [CARTO's documentation](https://carto.com/basemaps/apikey/) for information on API keys for CARTO.

**Geocoding Provider**
Select the service used to look up latitude and longitude for contact addresses so they can be shown on maps.

**Geo Provider Key**
Enter the API key as required by your GeoCoding provider.

Click **Save** to save your action or **Cancel** to cancel it. If successful, you will see the message "Your changes have been saved."

!!! note "Internal Server and/or Firewall Issues"
    If CiviCRM is installed on a server that does not have access to the public internet, or a firewall prevents CiviCRM from communicating with your chosen web services, you will see one or more fatal errors when attempting to add or edit contact records. To resolve this, either disable Mapping and Geocoding or resolve the connectivity issue.

After enabling the mapping provider, configure the [job.geocode](scheduled-jobs.md#job_geocode) scheduled job to geocode addresses without a latitude and longitude according to the configured options.

!!! note "Usage Limits"
    Some providers have usage limits on their Mapping and Geocoding APIs. If you go over the limits, you may receive an overlimit error when trying to save an address.

## Alternative geocoding providers

If you need an alternative Geocoding Provider, you may wish to evaluate this extension, which includes many improvements: https://civicrm.org/extensions/geocoder

<!-- Source: initial-set-up/mapping.md -->
