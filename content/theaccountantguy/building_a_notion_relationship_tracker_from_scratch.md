---
title: Building a Notion relationship tracker from scratch
videoId: h47T7sRTmg0
---

From: [[theaccountantguy]] <br/> 

This article outlines how to create a comprehensive relationship tracker in [[setting_up_a_database_in_notion_for_financial_tracking | Notion]] to manage events and interactions with family, friends, and colleagues <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The tracker helps schedule events in advance, ensuring you never miss important occasions <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. It includes details such as people connected to your life, their relationship categories, associated events (like marriages or birthdays), and an event summary showing attendance rates <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Getting Started

A template for this tracker is available for download on Gumroad by searching "relationship" <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

### Page Settings
Before building, adjust page settings in [[setting_up_a_database_in_notion_for_financial_tracking | Notion]]:
*   Click the three dots on the right side of the page <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   Enable "Full width" for an expanded page view <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   "Small text" can be toggled if desired, reducing text size <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Creating the Main Page
1.  Click "New page" to create a blank page <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
2.  Name the page "Relationship Tracker" <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
3.  Add a divider by typing `/divider` <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
4.  Add an icon (e.g., a user icon) by clicking "Add icon" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
5.  Add a cover image by clicking "Add cover" and choosing a solid background for a clean look <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

## Core Database Setup

The tracker is built from various linked databases <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### Database Sub-Page
To keep the main page clean, create a sub-page for all databases:
1.  On the main "Relationship Tracker" page, hit `Enter` and type `/database` <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
2.  Select "New sub page" to create a nested page <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
3.  Name this sub-page "Database" <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
4.  Add a divider and set the page to "Full width" <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
5.  Assign an icon (e.g., stacked discs) to this database page <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### Person Database
This database stores information about the people in your life <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
1.  Inside the "Database" sub-page, type `/database` and select "Inline database" <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
2.  Rename the database `db_person_database_new` <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
3.  Hide the database title if desired <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
4.  Rename the default "Name" column to "Person Database" <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
5.  Add hypothetical names (e.g., Susan, Harry, Sarah) <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
6.  Add icons for each person by opening their page and clicking "Add icon" <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
7.  Rename the "Tags" property to "Relation" <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
8.  Assign relations (e.g., Sister, Friend, Colleague) <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

### Events Database
This database stores details of events <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
1.  Below the Person Database, type `/database` and select "Inline database" <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
2.  Rename the database `db_events_database_new` <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
3.  Rename the default "Name" property to "Event Name" <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
4.  Add hypothetical events (e.g., Susan's birthday, Harry's marriage, Sarah's graduation) <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
5.  Add a "Date" property (`+` > `Date`) and set dates for events <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. You can also include time <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
6.  Add an "Attendance" property (`+` > `Checkbox`) to mark if an event was attended <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
7.  Add an "Event Type" property (`+` > `Select`) and create options like "Birthday Event", "Marriage Event", "Graduation Event" <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.
8.  **Establish Relation**:
    *   Add a new property (`+` > `Relation`) <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
    *   Select `db_person_database_new` to link the databases <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
    *   Enable "Show on `db_person_database_new`" and name it "Event Detail" <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
    *   Click "Add relation" <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. This creates a link, allowing you to associate events with specific people <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
    *   Rename the new column in the Events Database to "Person" for clarity <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
    *   Assign each event to the relevant person <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.

## Event Summary & Rollup Properties

To summarize event data, add rollup and formula properties to the **Person Database**:

### Number of Events
1.  In the Person Database, add a new property (`+` > `Rollup`) <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
2.  Configure the rollup:
    *   "Relation": `Event Details` (the relation property created earlier) <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
    *   "Property": `Event Name` <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
    *   "Calculate": `Count values` <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.
3.  Rename this property `Number of Events (Rollup)` <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>. This will show the total number of events associated with each person <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>.
4.  Add another property (`+` > `Formula`) named `Number of Events` <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>. Use the following formula for styled text and singular/plural logic:
    ```notion
    if(prop("Number of Events (Rollup)") <= 1, style("Number of Events: " + format(prop("Number of Events (Rollup)")) + " Event", "bold", "blue"), style("Number of Events: " + format(prop("Number of Events (Rollup)")) + " Events", "bold", "blue"))
    ```
    This displays the count of events for each person, using "Event" for one and "Events" for more than one, in bold blue text <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.

### Events Attended
1.  Duplicate the `Number of Events (Rollup)` property <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>.
2.  Rename it `Events Attended (Rollup)` <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.
3.  Configure the rollup:
    *   "Relation": `Event Details` <a class="yt-timestamp" data-t="00:25:14">[00:25:14]</a>.
    *   "Property": `Attendance` <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.
    *   "Calculate": `Count checked` <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>. This counts only the events marked as attended <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>.
4.  Duplicate the `Number of Events` formula property <a class="yt-timestamp" data-t="00:25:56">[00:25:56]</a>.
5.  Rename it `Events Attended` <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>.
6.  Modify the formula to reference `Events Attended (Rollup)` and change the color to green:
    ```notion
    if(prop("Events Attended (Rollup)") <= 1, style("Events Attended: " + format(prop("Events Attended (Rollup)")) + " Event", "bold", "green"), style("Events Attended: " + format(prop("Events Attended (Rollup)")) + " Events", "bold", "green"))
    ```

### Attendance Percentage
1.  Add a new property (`+` > `Formula`) named `Attendance Percentage` <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.
2.  Use the following formula:
    ```notion
    round(prop("Events Attended (Rollup)") / prop("Number of Events (Rollup)") * 100) / 100
    ```
    This calculates the percentage of attended events <a class="yt-timestamp" data-t="00:27:54">[00:27:54]</a>.
3.  Change the "Number format" to "Percentage" <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.
4.  Edit the property's "Show as" option to "Bar" and choose a color (e.g., blue) for a visual representation <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a>.
5.  Hide the `Number of Events (Rollup)` and `Events Attended (Rollup)` properties, as their values are used in the formula properties <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>.

## Main Dashboard Assembly

Return to the "Relationship Tracker" main page to link the databases and create the dashboard <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>.

### Person Database (Gallery View)
1.  Type `/linked` and select "Linked view of database" <a class="yt-timestamp" data-t="00:29:52">[00:29:52]</a>.
2.  Choose `db_person_database_new` <a class="yt-timestamp" data-t="00:30:17">[00:30:17]</a>.
3.  Click the three dots (`...`) next to the database name, then "Layout" and select "Gallery" view <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>.
4.  In "Layout" settings, set "Card size" to "Small" <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>.
5.  In "Properties" settings, ensure "Name" and "Relation" are visible <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>.
6.  Add an "Image" property (`+` > `Media` > `Image`) to the original Person Database to upload profile pictures <a class="yt-timestamp" data-t="00:32:58">[00:32:58]</a>.
7.  In the linked Gallery view's "Layout" settings, change "Card preview" to "Image" to display the uploaded images <a class="yt-timestamp" data-t="00:35:12">[00:35:12]</a>. You can reposition images within the card <a class="yt-timestamp" data-t="00:36:09">[00:36:09]</a>.
8.  Set "Open pages as" to "Side peak" in the layout options for a convenient side-panel view when opening a person's page <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>.

### Events Database (Calendar View)
1.  Below the Person Database, add another linked view by typing `/linked` and selecting `db_events_database_new` <a class="yt-timestamp" data-t="00:40:20">[00:40:20]</a>.
2.  Change the layout to "Calendar" view (`...` > `Layout` > `Calendar`) <a class="yt-timestamp" data-t="00:40:45">[00:40:45]</a>.
3.  In "Properties", enable "Event Type", "Person", and "Attendance" to be visible on the calendar entries <a class="yt-timestamp" data-t="00:41:03">[00:41:03]</a>.
4.  Add a "Priority" property (`+` > `Select`) to the original Events Database with options like "Low", "Medium", "High" <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>. Make this visible in the calendar properties <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>.
5.  You can reorder how properties appear on the calendar entries <a class="yt-timestamp" data-t="00:42:31">[00:42:31]</a>.
6.  The calendar can be viewed by "Month" (default) or "Week" via `...` > `Calendar` > `Show calendar as` <a class="yt-timestamp" data-t="00:43:03">[00:43:03]</a>.

### Event Summary (Board View)
1.  Add another linked view of `db_person_database_new` <a class="yt-timestamp" data-t="00:44:19">[00:44:19]</a>.
2.  Change the layout to "Board" view (`...` > `Layout` > `Board`) <a class="yt-timestamp" data-t="00:44:48">[00:44:48]</a>.
3.  Set "Card size" to "Medium" <a class="yt-timestamp" data-t="00:45:07">[00:45:07]</a>.
4.  The board view is grouped by "Relation" by default <a class="yt-timestamp" data-t="00:45:24">[00:45:24]</a>.
5.  Hide empty groups (`...` > `Group` > `Hide empty groups`) <a class="yt-timestamp" data-t="00:45:34">[00:45:34]</a>.
6.  In "Properties", enable "Number of Events", "Events Attended", and "Attendance Percentage" to be visible on the cards <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>.
7.  Rename this view to "Events Summary" <a class="yt-timestamp" data-t="00:47:03">[00:47:03]</a>.

### Event Details Section with Quick Add Button
1.  Add a divider by typing `/divider` (or two hyphens `--`) <a class="yt-timestamp" data-t="00:47:33">[00:47:33]</a>.
2.  Create two columns by typing `/two columns` <a class="yt-timestamp" data-t="00:47:52">[00:47:52]</a>.
3.  **Left Column - Add Event Button**:
    *   In the left column, type `/button` to add a new button <a class="yt-timestamp" data-t="00:48:12">[00:48:12]</a>.
    *   Name it "Add Event" and choose a `+` icon <a class="yt-timestamp" data-t="00:48:21">[00:48:21]</a>.
    *   Add a step: "Add page to" and select `db_events_database_new` <a class="yt-timestamp" data-t="00:48:33">[00:48:33]</a>.
    *   Set the "Event Name" property to "Enter event name" <a class="yt-timestamp" data-t="00:48:49">[00:48:49]</a>.
    *   Edit other properties (e.g., set "Date" to "Today") <a class="yt-timestamp" data-t="00:49:01">[00:49:01]</a>.
4.  **Right Column - Events Detail List**:
    *   In the right column, add a linked view of `db_events_database_new` <a class="yt-timestamp" data-t="00:49:20">[00:49:20]</a>.
    *   Change the view to a "Table" layout if it's not already <a class="yt-timestamp" data-t="00:49:42">[00:49:42]</a>.
    *   Group the table by "Date" (`...` > `Group` > `Date`) <a class="yt-timestamp" data-t="00:49:55">[00:49:55]</a>.
    *   Hide empty groups <a class="yt-timestamp" data-t="00:50:14">[00:50:14]</a>.
    *   Set "Sort by" to "Oldest first" <a class="yt-timestamp" data-t="00:50:28">[00:50:28]</a>.
    *   Set "Date by" to "Month" for a monthly organization of events <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>.
    *   To remove vertical lines in the table, click `...` > `Layout` > toggle off "Show vertical lines" <a class="yt-timestamp" data-t="00:53:13">[00:53:13]</a>.

## Advanced Features

### Adding New People Directly
When adding an event in the "Event Details" section, if you type a person's name into the "Person" property that doesn't exist yet, [[setting_up_a_database_in_notion_for_financial_tracking | Notion]] will prompt you to create a new page in the linked Person Database <a class="yt-timestamp" data-t="00:52:02">[00:52:02]</a>. This dynamically adds new people as you schedule events for them <a class="yt-timestamp" data-t="00:52:42">[00:52:42]</a>.

### Showing Related Properties as Page Sections
When viewing an individual's page from the "Person Database" (e.g., in the side peak view):
1.  Click the six dots next to the "Event Details" relation property <a class="yt-timestamp" data-t="00:56:09">[00:56:09]</a>.
2.  Select "Show as" and then "Page section" <a class="yt-timestamp" data-t="00:56:12">[00:56:12]</a>.
3.  This will embed the linked events directly into the person's page, allowing you to see all associated events, dates, priorities, and attendance status at a glance <a class="yt-timestamp" data-t="00:56:14">[00:56:14]</a>.

This tracker provides a flexible and visual way to manage your social engagements and ensure you stay connected with important people in your life <a class="yt-timestamp" data-t="00:57:25">[00:57:25]</a>.