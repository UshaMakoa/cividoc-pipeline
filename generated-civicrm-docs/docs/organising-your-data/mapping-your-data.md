---
title: Mapping your data
category: explanation
topic: general
subtopic: choosing-where-data-belongs
component: CiviCRM
audiences:
- fundraising-manager
- operations-user
- communications-manager
- membership-manager
level: basic
journey_stage: plan-and-configure
summary: Understand where existing constituent and organization data fits in CiviCRM before transferring it.
extensions: []
related: []
review_priority: low
review_notes:
- The Contributions section directs readers to information about configuring and using relationships; the wording is retained
  as written.
- The Activities section refers to an 'Activites' section; the spelling is retained as written.
guide: user-en
source_repository: https://lab.civicrm.org/documentation/docs/user-en.git
source_path: organising-your-data/mapping-your-data.md
destination_path: organising-your-data/mapping-your-data.md
legacy_urls:
- https://docs.civicrm.org/user/en/latest/organising-your-data/mapping-your-data/
civicrm_version:
- latest
source_commit: cd03beb215973d5e4ce662440c85b1ce765a0188
last_modified: '2026-10-06'
---

# Mapping your data

Your existing data may come from multiple sources: electronic records, paper records, and people's memories. **Mapping** means taking data labeled in one way and finding its place in CiviCRM's structure. Skipping this step may have unwanted consequences. For example, you may not be able to control or report on data as you expect.

People think about data differently depending on their experience with another CRM, or with no CRM at all. For example, Donation, Opportunity, and Contribution can all refer to money given to your organization. CiviCRM was designed to be flexible and adaptable, so you should have no problem finding a place for every piece of information relevant to your organization.

Resist the temptation to add custom fields right away. Rather than creating a field for manually entering membership expiration dates, learn about CiviCRM's membership module, which automates membership duration, expiration, and renewal reminders. Multiple fields that collect the same data can cause confusion. Make informed choices up front to avoid duplication.

The sections below introduce options CiviCRM provides out of the box. Instead of keeping data in “flat” spreadsheets, you can use **relationships** to connect it and build a more complete picture of the community that supports your organization.

## Basic information about your constituents

CiviCRM has default fields for constituent names, addresses, phone numbers, emails, notes, and other contact information. It was designed for non-profits, so mapping basic constituent information should be straightforward.

CiviCRM divides constituents into three categories, called Contact Types:

- **Individuals:** Any person your organisation wants to keep a record of.
- **Organizations:** Another non-profit, a company, a chapter of your organisation, or a committee. You will generally want to create at least one contact of the Organization type to represent your organization. This is particularly useful when configuring memberships.
- **Households:** A family or group of people who share a physical location.

Each contact type has fields suited to the data you may want to track. For example, gender applies to individuals, not organisations or households, so the gender field is available only for Individual contact types and subtypes.

See [Contacts](contacts.md) to learn more about built-in CiviCRM basic constituents fields and how to use them.

## Information specific to your organization (custom fields)

Many organizations collect data specific to their mission or structure. CiviCRM provides fields for basic data that non-profits commonly collect, but your organisation may also need to record information such as constituent allergies for individuals or service area for organizations.

When mapping data into CiviCRM, decide whether each piece of information pertains to an individual, organization, or household. For example, “service area” only makes sense for Organizations. To find out how to create custom fields, see [Creating Custom Fields](creating-custom-fields.md).

## Relationships between constituents

Relationships capture current and historical information about how two records connect.

You or your colleagues may know things about constituents that have never been written down. A flat spreadsheet may not have had space for them, or they may have remained mental notes. A Relationship can capture family members, places of employment, and connections to other constituents in your database.

CiviCRM has predefined relationship Types, including “employer--employee”, “parent--child”, and “employee--employer”. You can create more to describe relationships specific to your organization, such as “vicar--church”. When you create a new Relationship, you can define when it began and, if relevant, when it ends. You can still access a previous relationship after it ends—for example, to see where someone used to work.

The term Household and the relationship Types “household member of--head of the household” confuse many new CiviCRM users. Grouping individuals who share an address in one household can mean they receive only one letter. The “head of the household” designation helps an organization decide whom to address—for example, a parent rather than a child.

To read more about configuring and using relationships, please see the the *Relationships* section in *Organising Your Data*.

## Activities

Knowing how and when constituents engage with your organization can help you understand their involvement. Someone who gives monthly, volunteers frequently, and renews her membership yearly may respond well to opportunities that strengthen her relationship with your organization. CiviCRM lets you record interactions such as phone calls, emails, and meetings between staff and constituents, helping your organization retain a history of those relationships.

CiviCRM calls these exchanges Activities. They are closely linked to other CiviCRM modules. When you record contributions, event attendance, membership subscriptions, and emails, CiviCRM automatically creates a related activity in the Contact record. Decide whether your organization needs activity types beyond those provided, such as training, review, exam, or support.

To read more about configuring and using activities, please see the *Activites* section in *Organising Your Data*.

## Webinars, events, performances, and meetings (CiviEvents)

CiviCRM helps manage and track occasions that bring community members together at a place and time. Webinars, events, performances, and meetings have start and end dates and times, meeting places (including online), and reasons for bringing people together. They can be ticketed, RSVP only, or require no reservation. CiviCRM provides functionality to promote events and record registrations. If you have records of participation in past events, you can transfer them into CiviEvents.

The **Event Types** field distinguishes the kinds of events your organization hosts. This can help you evaluate participation in a series of similar events or whether someone prefers one kind of event over another.

To read more about configuring and using events , please see the *Events* chapter later in this book.

## Memberships

Many organizations offer programs in which community members sign up for benefits for a pre-defined period. Members may choose from dues levels with associated benefits; generally, higher dues bring more benefits. An organization can also give a membership at no price, perhaps as an award. For example, a long-time volunteer might receive a life-time membership. Common benefits include access to member directories, extra content, and discounts. Individuals, families or households, and organizations can all sign up for memberships.

The main difference between membership dues and a donation is that membership changes someone's relationship to an organization for a period of time. Organizations often expect memberships to be renewed from year to year, while a donation is a one-time gift. Organizations need to send an acknowledgement letter, but a donation—or Contribution in CiviCRM—does not promise the donor advertised benefits in return.

Analyze your membership structure before importing membership records into CiviCRM. Take time to eliminate unused membership levels or simplify promised benefits. The information you really need to transfer for each member is start date, duration, membership dues paid, and type of membership.

Generally, more than 10–15 membership types may be hard to manage. Some organizations have many types because they store other constituent information in membership records. Before extending those records, check whether CiviCRM already has membership-related fields for that information.

Information previously recorded as static data may now be calculated dynamically and displayed in reports or other fields. For example, CiviCRM can calculate how many years a constituent has been a member from the “Membership since” date.

To read more about configuring and managing memberships, please see the *Memberships* chapter later in this book.

## Contributions

Contribution in CiviCRM refers to money, goods, or services coming into your organization. Money remains money whether someone buys an event ticket, signs up for a membership, or makes another payment. CiviCRM lets you record incoming money as a Contribution with different Types to retain information about its source. You can also specify the date received, its status—including pending before money is deposited in your bank account—and how it was delivered, such as by check or cash.

If you plan to keep using an external donations system, you may leave transactions there. You may nevertheless want to transfer information about past event or webinar registrations to CiviCRM because it shows a constituent's history of involvement. Consider how far back to import contribution history. Large contributions should be preserved, but a 5-dollar donation from 10 years ago may no longer be relevant.

To read more about configuring and using relationships, please see the *Contributions* chapter later in this book.

## Campaigns

Organizations sometimes hold a fundraising gala, send an email appeal, and record contributions in support of one goal—for example, raising $50,000 for a kids camp. Campaigns are usually time limited. They connect a range of activities and provide a high-level view for comparing how people responded to your initiatives.

Campaigns may be useful if your organization's fundraising initiatives fit distinct themes, such as year end pledge drives or project specific fundraisers. An organization may send several appeals for one project or fundraiser, including a 'final notice' and one or more 'countdown' appeals.

## Grouping and tagging constituents

Development directors, volunteer coordinators, and program managers often carry information in their heads when deciding whom to invite to an event, exclude from an appeal, or consider for a volunteer opportunity.

Groups and tags can store that information and help build email and invitation lists. **Groups** identify two or more contacts with something in common; relationships capture information about only two contacts. Groups can also serve as mailing lists. A group of newsletter subscribers is one place to start.

Organizations may send different communications to subsets of their community. One Individual can be tagged member and volunteer to receive both member-specific and volunteer-specific communications. Groups can also store issue- or program-specific communication preferences. For example, when creating an email appeal mailing, you can exclude a group of Individuals who have asked not to receive fundraising appeals.

Avoid creating groups for information already stored in other CiviCRM fields. You do not need a group for individuals who have opted out of bulk mailings: that option is selected on their Contact record, and CiviCRM automatically excludes them from bulk mailings. Likewise, you do not need a group called “donors”: an advanced search can find any **Contact** record with an associated **Contribution**, including within specified date ranges. Most functions available to groups are also available through the search results screen.

To have new records that meet particular criteria added to a group automatically, create a **Smart Group** from an **advanced search**. For example, you might create a Smart Group of members who also donated more than $100 in the past year. If a member makes a new $100 donation after the group is created, their record will be added to the Smart Group.

**Tags** are more like keywords associated with a record. You can easily add or remove them, but there is no easy way to see their history of changes. Relationships are a better tool for viewing information history.

## Profiles

CiviCRM lets you assemble sets of fields for different purposes, helping reduce the time staff spend on administrative tasks. These sets are called [Profiles](profiles.md).

Profiles determine how data is edited or displayed to staff or other users, not how it is stored.

## Where next?

The sections above describe places where existing data may fit in CiviCRM, but cover only basic functionality. For more about how CiviCRM can work with your data, see later chapters in this book, which explain specific functionality from major extensions.

<!-- Source: organising-your-data/mapping-your-data.md -->
