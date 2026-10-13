---
title: Create a public membership list
category: tutorial
topic: memberships
subtopic: filterable-logo-grid
component: SearchKit and FormBuilder
audiences:
- membership-manager
- administrator
- operations-user
level: intermediate
journey_stage: plan-and-configure
summary: Create a public, filterable membership logo grid using SearchKit and FormBuilder.
extensions: []
related: []
review_priority: low
review_notes:
- The token instruction says to remove `/civirm`, but the example begins `civicrm/` and the explanation refers to `/civicrm`;
  confirm which prefix is intended.
- The example host `your.civicrm.tdl` may be a typo; confirm its intended value.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: searching/searchkit/example-membership-listing.md
destination_path: searching/searchkit/example-membership-listing.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/searching/searchkit/example-membership-listing/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Create a public membership list

An organization with several levels of membership may want filterable, searchable lists on its website populated by live data from CiviCRM. This tutorial uses SearchKit and FormBuilder to create a logo grid with tooltips and links to external websites, such as members' websites. Visitors can filter the grid by membership type.

![Grid showing filterable Memberships](../../img/search-kit/membership-listing-goal.png)

## Step 1: Create a new search and define the data

Go to **Administer &gt; Search &gt; SearchKit** and click **New Search**. Then:

1. Give the search a title name (e.g. "Our Members") in the box labeled "Untitled Search".
2. Select Memberships from the **Search for** list.
3. Add a **With** for Membership Contact so that data can be pulled from the member's contact record (e.g. the display name to show in a tooltip).
4. Add a second **With** for Contact Websites to access the link to the member's homepage.

![Search Screen](../../img/search-kit/membership-listing-creating-search.png)

Tap **Search** to check the results. The criteria above returned six memberships. When you add Membership Contact and Contact Websites, SearchKit automatically adds some columns with data from these sources:

![Search results](../../img/search-kit/membership-listing-search-results.png)

## Step 2: Add columns to output additional data

The displayed columns determine which data the search returns. To add a column for the logo URL:

1. Tap the **+Add** button at the top right of the results table.
2. Choose the column to display (e.g. Membership Contact: Image URL).
3. Refresh the results display by clicking **Search**.

This selection uses the standard contact image. Using custom fields, such as a different image, requires adding another data source first.

The results will now look like this:

![Search results with one more column](../../img/search-kit/membership-listing-search-results-url.png)

!!! Tip
    Don't forget to **Save** your work.

## Step 3: Add and configure a grid display

To format the search results, click the **+Add** button underneath the search's title field to add a display. Select a Grid display to organize the output into tiles.

![Adding Grid as Display](../../img/search-kit/membership-listing-add-grid.png)

Give the display configuration a title (e.g. "Our Members"). By default, SearchKit adds all the search's fields (columns) to the new display. You can customize these fields, including by dragging and dropping them into a new order.

![Adding Grid as Display](../../img/search-kit/membership-listing-grid-items.png)

Click **Preview** to see the results in a 3x3 pattern grid below the button at the bottom of the page. At this stage, the display does not yet show the intended logos. To configure it:

1. **Remove** all items that are not needed by clicking the remove symbol (indicated by the red arrow in the screenshot above) in each item's section. Leave only Membership Contact: Image URL for this example.
2. Check the **Image** checkbox to display the logo as an image.
3. Optionally, set size attributes to make the logo sizes match (e.g. adjust the height to 200px).
4. Check the **Link** checkbox, select **'Other...'** from the dropdown menu, and select Membership Contact - Contact Websites: Website from the **token dropdown**.
5. **Attention:** remove `/civirm` from the front of the token:
   `civicrm/[Membership_Contact_contact_id_01_Contact_Website_contact_id_01.url]`
   so that it becomes:
   `[Membership_Contact_contact_id_01_Contact_Website_contact_id_01.url]`
   as the `/civicrm` portion would inhibit the url from reaching the member's external website.
6. Check the **Tooltip** checkbox and make sure the label that pops up to the right is a token for the Display Name.

Click **Refresh** to see the logos displayed as intended:

![changing Grid items and preview](../../img/search-kit/membership-listing-change-grid-items.png)

!!! Note
    This configuration will only show members who have logos associated with their record. To include those without logos, check the **Alternative image** box.

## Step 4: Add and configure a form

To show the results on a public website, create a Form. Return to the SearchKit dashboard and click **Forms &gt; + Create Form for Our Members Grid**:

![adding Form from SearchKit dashboard](../../img/search-kit/membership-listing-add-form.png)

Then:

1. Give the Form a name and a description.
2. Enter the URL for the page on which you want the results displayed (e.g. 'civicrm/members').

![configuring new Afform Form](../../img/search-kit/membership-listing-form-created.png)

After clicking **Save**, the link **View Page** will appear. This link shows the fully formatted results grid.

To filter which membership types are shown, switch from the **Form Settings** tab to the **Our Members Grid** tab and drag the item Membership Type into the **Form Layout** tab.

![adding a filter](../../img/search-kit/membership-listing-form-adding-filter.png)

Then:

1. Change the preset of the filter so that it shows the desired membership types.
2. Change the layout details, such as the title of a container element.

![configuring a filter](../../img/search-kit/membership-listing-form-configuring-filter.png)

So long as you are logged into your CiviCRM account, the specified URL (e.g. your.civicrm.tdl/civicrm/members/) will display the configured Form.

## Step 5: Set permissions

To make the form accessible to anonymous users, return to the search's display configuration and unlock the **Enforce Permissions** button by clicking it. Once clicked, the button will read **Bypass Permissions**, as shown below.

![switching permissions for search display](../../img/search-kit/membership-listing-grid-permissions.png)

**Save** before going back to the Form configuration.

To make the page containing the results grid viewable on a public website:

1. Remove all restrictions by selecting 'Generic: Allow all users (including anonymous)' from the dropdown list.
2. Check the **Accessible on front-end of website** box.

![switching permissions for search display](../../img/search-kit/membership-listing-form-permissions.png)

Users, whether logged in or not, will now be able to view and filter the form.

<!-- Source: searching/searchkit/example-membership-listing.md -->
