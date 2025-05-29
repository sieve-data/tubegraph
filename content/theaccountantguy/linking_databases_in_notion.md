---
title: Linking databases in Notion
videoId: h47T7sRTmg0
---

From: [[theaccountantguy]] <br/> 

When building a dashboard in Notion, everything often constitutes a collection of different databases holding information, which is then summarized into a single view <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. The core process involves [[creating_a_database_in_notion | building different databases]] and then linking them up to achieve the desired presentation <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

## Relationship Tracker Dashboard Overview

This article demonstrates [[connecting_notion_databases_and_templates | connecting Notion databases]] by building a "Relationship Tracker" dashboard <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This tracker helps keep tabs on events (like marriages, birthdays, or parties) associated with people in your life, such as family, friends, or colleagues <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. It allows you to schedule events in advance to avoid missing them <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

The dashboard will include:
*   Information about connected people and their relationship categories <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   Details of events like marriages or birthdays <a class="yt="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   A monthly view of events <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   An event summary showing outlined and attended events per person <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Initial Notion Setup

Before [[setting_up_databases_in_notion | setting up databases]], configure your Notion page:
1.  Click the three dots on the right side of the page <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
2.  Enable "Full width" for a broader page view <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
3.  Create a new blank page to build the dashboard from scratch <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
4.  Name the new page (e.g., "Relationship Tracker") and add an icon and cover image <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

## Creating Core Databases

All primary databases for this dashboard will be stored within a dedicated "Database" sub-page <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

### Database Sub-Page
1.  On your main "Relationship Tracker" page, hit `/` and type `page` to create a new sub-page <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
2.  Name this sub-page "Database" (e.g., `db_Database_new`) and add an icon <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
3.  Set this page to "Full width" <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### Person Database
This database will store information about the people in your life <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
1.  Inside the "Database" sub-page, hit `/` and type `database` <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. Select "Inline database" <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
2.  Rename the database "Person Database" (e.g., `db_Person_Database_new`) <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Hide the database title <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
3.  Add entries for people (e.g., Susan, Harry, Sarah) <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
4.  Add icons for each person by opening their page and clicking "Add icon" <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
5.  Rename the "Tags" property to "Relation" <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. This "Select" property will define relationships (e.g., Sister, Friend, Colleague) <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### Events Database
This database will store details about specific events <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
1.  Still within the "Database" sub-page, create another "Inline database" <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
2.  Rename it "Events Database" (e.g., `db_Events_Database_new`) <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
3.  Rename the default "Name" property to "Event Name" <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
4.  Add hypothetical events (e.g., Susan's Birthday, Harry's Marriage, Sarah's Graduation) <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
5.  Add a "Date" property to schedule events <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
6.  Add a "Checkbox" property named "Attendance" to mark if an event was attended <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
7.  Add a "Select" property named "Event Type" for categories like "Birthday," "Marriage," or "Graduation" <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

## Linking Databases with "Relation" Property

The "Relation" property establishes a link between two databases <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
1.  In the "Events Database," add a new property <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
2.  Select "Relation" as the property type <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
3.  Choose the `db_Person_Database_new` to relate to <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
4.  Opt to "Show on" the `db_Person_Database_new` and name it "Event Detail" <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
5.  Rename the new column in the "Events Database" to "Person" for clarity <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
6.  For each event, select the associated person from the linked "Person Database" <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. This action will automatically add the event to the linked person's entry in the "Person Database" <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

## Summarizing Data with "Rollup" Property and Formulas

The "Rollup" property allows you to derive information from a linked database <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. This is crucial for [[creating_a_database_in_notion_for_calculations | creating a database in Notion for calculations]] and summaries.

### Number of Events (Rollup)
1.  In the "Person Database," add a new property <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
2.  Select "Rollup" as the property type <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
3.  Configure the rollup:
    *   **Relation:** Choose "Event Details" (the relation property linking to the events database) <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
    *   **Property:** Select "Event Name" from the related database <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
    *   **Calculate:** Choose "Count values" to count all linked events <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.
4.  Rename this property "Number of Events (Rollup)" <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.

### Events Attended (Rollup)
1.  Duplicate the "Number of Events (Rollup)" property <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>.
2.  Rename it "Events Attended (Rollup)" <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.
3.  Configure this rollup:
    *   **Relation:** "Event Details" <a class="yt-timestamp" data-t="00:25:14">[00:25:14]</a>.
    *   **Property:** "Attendance" (the checkbox property) <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.
    *   **Calculate:** Choose "Count checked" to count only the events marked as attended <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.

### Styling with Formulas (Number of Events, Events Attended)
To display the counts with custom text and styling:
1.  Add a new "Formula" property <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.
2.  Use the `style()` function to apply formatting (e.g., bold, color) <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.
3.  Implement an `if` condition to display "event" (singular) or "events" (plural) based on the rollup count <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.

    ```notion-formula
    if(prop("Number of Events (Rollup)") <= 1,
        style("Number of Events: " + format(prop("Number of Events (Rollup)")), "blue", "bold") + " event",
        style("Number of Events: " + format(prop("Number of Events (Rollup)")), "blue", "bold") + " events"
    )
    ```
    *   Repeat a similar formula for "Events Attended," changing the property referenced and color to green <a class="yt-timestamp" data-t="00:26:07">[00:26:07]</a>.
4.  Hide the raw "Rollup" properties as they are now used by the formulas <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>.

### Attendance Percentage (Formula)
1.  Add a new "Formula" property named "Attendance Percentage" <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.
2.  Use a formula to calculate the percentage:
    `round(prop("Events Attended (Rollup)") / prop("Number of Events (Rollup)") * 100) / 100` <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>.
3.  Change the number format to "Percentage" <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.
4.  In the "Edit Property" settings, select "Bar" or "Ring" to visualize the percentage <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a>.

## Displaying Linked Databases on the Main Dashboard

Now, return to your main "Relationship Tracker" page to link and display the created databases <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>. This is a key step in [[creating_and_connecting_databases_in_notion | creating and connecting databases in Notion]].

### People Overview (Gallery View)
1.  Hit `/` and type `linked` <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>. Select "Linked view of database" <a class="yt-timestamp" data-t="00:29:56">[00:29:56]</a>.
2.  Choose your `db_Person_Database_new` <a class="yt-timestamp" data-t="00:30:17">[00:30:17]</a>.
3.  Change the layout to "Gallery" view <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>.
4.  In "Layout" settings:
    *   Set "Card size" to "Small" or "Medium" <a class="yt-timestamp" data-t="00:30:42">[00:30:42]</a>.
    *   Set "Card preview" to "Image" (after adding an "Image" property to the Person Database and uploading images for each person) <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>.
5.  In "Properties" settings, choose which properties to show on the cards (e.g., "Name", "Relation") <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>.

### Events Calendar (Calendar View)
1.  Below the Person Database, add another "Linked view of database" <a class="yt-timestamp" data-t="00:40:22">[00:40:22]</a>.
2.  Select your `db_Events_Database_new` <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>.
3.  Change the layout to "Calendar" view <a class="yt-timestamp" data-t="00:40:47">[00:40:47]</a>.
4.  In "Properties" settings, select which event details to display (e.g., "Event Type", "Person", "Attendance", "Priority") <a class="yt-timestamp" data-t="00:41:03">[00:41:03]</a>.
5.  You can change the calendar view from "Month" to "Week" <a class="yt-timestamp" data-t="00:43:05">[00:43:05]</a>.

### Event Summary (Board View)
This section provides a summary of events per relationship category.
1.  Add another "Linked view of database" and select your `db_Person_Database_new` <a class="yt-timestamp" data-t="00:44:19">[00:44:19]</a>.
2.  Change the layout to "Board" view <a class="yt-timestamp" data-t="00:44:48">[00:44:48]</a>.
3.  In "Layout" settings:
    *   Set "Card size" to "Medium" <a class="yt-timestamp" data-t="00:45:07">[00:45:07]</a>.
    *   Ensure "Group by" is set to "Relation" <a class="yt-timestamp" data-t="00:45:24">[00:45:24]</a>.
    *   Toggle "Hide empty groups" to keep the view clean <a class="yt-timestamp" data-t="00:45:34">[00:45:34]</a>.
4.  In "Properties" settings, enable the rollup/formula properties created earlier: "Number of Events," "Events Attended," and "Attendance Percentage" <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>.

## Adding New Entries

### Using Buttons
Buttons can quickly add new entries to a specific database with predefined properties <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>.
1.  Hit `/` and type `button` <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a>.
2.  Name the button (e.g., "Add Event") <a class="yt-timestamp" data-t="00:48:21">[00:48:21]</a>.
3.  Add a step: "Add page to" <a class="yt-timestamp" data-t="00:38:33">[00:38:33]</a>.
4.  Select the target database (e.g., `db_Events_Database_new`) <a class="yt-timestamp" data-t="00:48:42">[00:48:42]</a>.
5.  Set default property values (e.g., "Event Name" to "Enter event name", "Date" to "Today") <a class="yt-timestamp" data-t="00:48:49">[00:48:49]</a>.

### Direct Input via Relation Property
You can also add new related items directly from a relation property.
1.  In the "Events Database" (table or grouped view), click on the "Person" property for an event <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>.
2.  Type a new name (e.g., "Peter") <a class="yt-timestamp" data-t="00:52:12">[00:52:12]</a>. Notion will offer to "Create new page in Person Database" <a class="yt-timestamp" data-t="00:52:16">[00:52:16]</a>.
3.  Selecting this option will automatically add the new person to the "Person Database" <a class="yt-timestamp" data-t="00:52:26">[00:52:26]</a>.

## Enhancing Data Visibility

### Page Sections for Relation Properties
For relation properties within a database entry, you can change their display to a "page section" to see all related items directly within the page view <a class="yt-timestamp" data-t="00:56:09">[00:56:09]</a>.
1.  Open any person's page from the "Person Database" <a class="yt-timestamp" data-t="00:55:47">[00:55:47]</a>.
2.  Click the six dots next to the "Event Details" relation property <a class="yt-timestamp" data-t="00:56:09">[00:56:09]</a>.
3.  Select "Show as" and then "Page section" <a class="yt-timestamp" data-t="00:56:12">[00:56:12]</a>.
4.  This docks the entire relation property as a section within the page, allowing you to see all associated events directly there <a class="yt-timestamp" data-t="00:56:14">[00:56:14]</a>.

This comprehensive approach allows for robust data management and visualization within Notion, enabling you to track and manage complex relationships and events effectively.