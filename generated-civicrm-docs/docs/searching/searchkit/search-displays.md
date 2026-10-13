---
title: Search displays
category: reference
topic: search
subtopic: display-types-and-configuration
component: SearchKit
audiences:
- administrator
- operations-user
- technical
level: intermediate
journey_stage: plan-and-configure
summary: Learn how to add a SearchKit display, choose a display type, and configure how results appear.
extensions:
- ChartKit
- SearchKit Calendar
- SearchKit Maps
- SearchKit Tokens
- SearchKit Column Display
related: []
review_priority: low
review_notes:
- The source labels the site-wide autocomplete option "Make Default Autocomplte"; verify the label before changing it.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: searching/searchkit/search-displays.md
destination_path: searching/searchkit/search-displays.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/searching/searchkit/search-displays/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Search displays

Search Displays present search results in different formats on your site. They make SearchKit results accessible across your CiviCRM implementation.

## Adding a display

A search can have zero, one, or multiple displays, so you can present the same data in multiple ways. To add a display, click the "Add..." button on the left side when editing your saved search.

!!! note "Default Display"
    Every search can be displayed as a table without creating a display - that's what you see when clicking the "Search" button.
    This "Search results table" can be viewed as a standalone page or even embedded in a form in-lieu of creating a display.
    However, you'll typically want to create your own display instead of using the default so you can set some configuration options.

## Display types

When adding a search display, first choose the *type* from the dropdown list:

- **Table**: Displays results in rows and columns, with an optional pager and selectable actions. The styling of rows and columns is highly configurable.
- **List**: Displays results on one or more lines. Each field can be styled differently or given a custom css class.
- **Grid**: Useful for image gallery thumbnails and other content to show side-by side.
- **Tree**: Represents hierarchical data in a nested tree structure.
- **Data Entry**: Unlike the above displays which output data, this creates a spreadsheet-like input form for batch data entry.
- **Autocomplete**: Autocomplete fields give results from the search as the user types. An autocomplete display allows customization of how each result appears in the dropdown. Once created, the display can be selected for use in FormBuilder, or select "Make Default Autocomplte" to affect forms site-wide.
- **DB Entity**: Creates a database table or view which can be accessed with SearchKit, the API, or SQL-based tools.

### Additional extensions

More search displays are provided by extensions in the [Extensions Directory](https://civicrm.org/extensions?search=searchkit):

- **ChartKit**: Enable this extension (already bundled with CiviCRM core) for data visualisation in the form of plots, charts, and graphs.
- **SearchKit Calendar**: [Download this extension](https://civicrm.org/extensions/searchkit-calendar) for a time-based display of events, activities, etc.
- **SearchKit Maps**: [Download this extension](https://civicrm.org/extensions/searchkit-maps) to show the location of contacts, events, etc. on a map.
- **SearchKit Tokens**: [Download this extension](https://civicrm.org/extensions/searchkit-tokens) to create your own tokens with SearchKit, for use in mailings.
- **SearchKit Column Display**: [Download this extension](https://civicrm.org/extensions/searchkit-column-display) for a display that stacks fields into columns.
- **And more**: Check the [Extensions Directory](https://civicrm.org/extensions?search=searchkit) for the latest additions.

## Configuration options

Each Search Display can be customized with various settings:

- Field selection and ordering
- Column headers and labels
- Sorting preferences
- Link configurations
- Inline editing capabilities
- Access permissions
- Display-specific styling
- Pagination settings
- Formatting and rewriting results

## Rewriting results in Search Displays

Search Displays let you rewrite fields to customize how data is presented to users.

### Basic field combining

Combine multiple fields using square brackets to reference field names:

```
[first_name] [last_name]
[street_address], [city] [postal_code]
```

This creates concatenated values like:

- "Jane Smith"
- "123 Main St, Springfield 12345"

### Smarty rewrites

For more complex formatting, use Smarty template syntax with curly brackets:

- **Conditional Display:**
``` smarty
{if $nick_name}[nick_name]{else}[first_name]{/if} [last_name]
```
- **Math Operations:**
``` smarty
{$total_amount - $fee_amount}
```
- **Value Transformation:**
``` smarty
{if $age_years >= 18}Adult{else}Minor{/if}
```

### Tips

1. Field names in square brackets (e.g. `[display_name]`) are replaced with their values automatically
2. Use `{$field_name}` to access raw field values in Smarty code, so you can get, for example, 125 instead of $125.00.
3. Smarty modifiers like `|date_format` and `|crmMoney` help with common formatting needs
4. You can combine both square bracket and Smarty syntax in the same rewrite

!!! tip
    Rewritten fields are display-only and won't affect the underlying data storage.

<!-- Source: searching/searchkit/search-displays.md -->
