---
title: Creating databases for people and events in Notion
videoId: h47T7sRTmg0
---

From: [[theaccountantguy]] <br/> 

This article details how to build a "relationship tracker" dashboard in Notion to manage events associated with people in your life, such as family, friends, and colleagues <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The dashboard helps keep track of events like marriages, birthdays, parties, or any functions you are supposed to attend, allowing you to schedule them in advance to avoid missing occasions <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

The dashboard allows you to:
*   Add information about connected people <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   Assign a category for their relationship <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
*   Input specific events like marriages or birthdays <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   View the entire schedule in a monthly format <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   See an event summary showing outlined and attended events <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

This template is available for download on Gumroad by searching for "relationship" <a class="yt-timestamp" data-t="01:27:54">[01:27:54]</a>.

## Getting Started

Before [[setting_up_a_database_in_notion | building the Notion template]], it's helpful to configure your page view <a class="yt-timestamp" data-t="01:51:30">[01:51:30]</a>:
*   Click the three dots on the right side of the Notion page <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.
*   You can select "Small text" to reduce the text size <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>.
*   Choose "Full width" to utilize the entire page view for better presentation <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>.

### Creating the Main Page
1.  Create a new page by clicking "New page" <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.
2.  Name the page "Relationship Tracker" <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>.
3.  Add a divider by typing `/` and then `divider` <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>.
4.  Add an icon (e.g., by searching for "user") <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.
5.  Add a cover image (e.g., a solid background) for visual appeal <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.

## Building Core Databases

The dashboard is a collection of different databases that hold information, providing a summarized view <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>. You will build and link these databases <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.

### Database Sub-Page
It's recommended to create a dedicated sub-page to store all your databases for organization <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>.
1.  On your "Relationship Tracker" page, hit `+` and then type `database` <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.
2.  This creates a new sub-page (a nested page) <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>.
3.  Name this sub-page "DB_Person_database_new" (or similar) <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.
4.  Set its view to full width and add an icon (e.g., stacked disks) <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>.

### Person Database
This database holds information for all connected people <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>.
1.  Inside the database sub-page, rename the default "Untitled" database to "Person Database" <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.
2.  Enter hypothetical names (e.g., "Suzan", "Harry", "Sara") <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>.
3.  Add icons for each person by clicking "Open" next to their name and then "Add icon" <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>.
4.  Rename the "Tags" property to "Relation" to signify how people are related to you <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.
5.  Assign relations (e.g., "Sister", "Friend", "Colleague") <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.
6.  Add an "Image" property (Media type) to each person's entry for visual representation <a class="yt-timestamp" data-t="33:00:00">[33:00:00]</a>. You can upload an image and reposition it <a class="yt-timestamp" data-t="33:30:00">[33:30:00]</a>.

### Events Detail Database
This database stores all event information <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>.
1.  In the database sub-page, hit `/` and type `database`. Select "Inline database" <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>.
2.  Rename this database to "DB_Events_database_new" <a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a>, and its display name to "Events Details" <a class="yt-timestamp" data-t="09:42:00">[09:42:00]</a>.
3.  Rename the default "Name" property to "Event Name" <a class="yt-timestamp" data-t="09:52:00">[09:52:00]</a>.
4.  Add event names (e.g., "Susan's birthday", "Harry's marriage", "Sara's graduation") <a class="yt-timestamp" data-t="10:16:00">[10:16:00]</a>.
5.  Add a "Date" property <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>. You can include time if needed <a class="yt-timestamp" data-t="11:22:00">[11:22:00]</a>.
6.  Add an "Attendance" property (Checkbox type) to mark if an event was attended <a class="yt-timestamp" data-t="11:56:00">[11:56:00]</a>.
7.  Add an "Event Type" property (Select type) to categorize events (e.g., "Birthday", "Marriage", "Graduation") <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>.
8.  Add a "Priority" property (Select type) with options like "Low", "Medium", "High" <a class="yt-timestamp" data-t="41:44:00">[41:44:00]</a>.

## Linking Databases (Relation Property)

To associate events with people, you use a "Relation" property <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>.
1.  In the "Events Detail" database, add a new property and select "Relation" <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>.
2.  Link this relation to the "DB_Person_database_new" <a class="yt-timestamp" data-t="13:34:00">[13:34:00]</a>.
3.  It will ask if you want to show this property on the other database. You can enable this and name it (e.g., "Event Detail") <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>.
4.  Rename the new column in the "Events Detail" database to "Person" <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>.
5.  For each event, select the associated person from the "Person" column <a class="yt-timestamp" data-t="14:43:00">[14:43:00]</a>. This will automatically show the event in the person's entry in the "Person Database" <a class="yt-timestamp" data-t="14:49:00">[14:49:00]</a>.

## Summarizing Information (Rollup and Formula Properties)

### Number of Events (Rollup)
To count events per person:
1.  In the "Person Database", add a new property and select "Rollup" <a class="yt-timestamp" data-t="16:46:00">[16:46:00]</a>.
2.  Select the "Event Details" relation <a class="yt-timestamp" data-t="17:45:00">[17:45:00]</a>.
3.  For "Property", select "Event Name" <a class="yt-timestamp" data-t="18:08:00">[18:08:00]</a>.
4.  For "Calculate", select "Count values" <a class="yt-timestamp" data-t="18:12:00">[18:12:00]</a>. This will count how many events are linked to each person <a class="yt-timestamp" data-t="18:23:00">[18:23:00]</a>.
5.  Rename this property to "Number of Events (Rollup)" <a class="yt-timestamp" data-t="19:18:00">[19:18:00]</a>.

### Events Attended (Rollup)
To count attended events per person:
1.  Duplicate the "Number of Events (Rollup)" property <a class="yt-timestamp" data-t="24:54:00">[24:54:00]</a>.
2.  Rename it to "Events Attended (Rollup)" <a class="yt-timestamp" data-t="25:05:00">[25:05:00]</a>.
3.  Edit the rollup: for "Property", select "Attendance" (the checkbox property) <a class="yt-timestamp" data-t="25:16:00">[25:16:00]</a>.
4.  For "Calculate", select "Count checked" <a class="yt-timestamp" data-t="25:29:00">[25:29:00]</a>. This counts only the events marked as attended <a class="yt-timestamp" data-t="25:31:00">[25:31:00]</a>.

### Formatted Event Counts (Formula)
To display event counts with custom text and styling:
1.  Add a new property and select "Formula" <a class="yt-timestamp" data-t="19:37:00">[19:37:00]</a>.
2.  **Number of Events:** Use a formula like `style("Number of events: " + prop("Number of Events (Rollup)") + (prop("Number of Events (Rollup)") <= 1 ? " event" : " events"), "b", "blue")` <a class="yt-timestamp" data-t="21:11:00">[21:11:00]</a>. This displays the count in bold blue text and correctly uses "event" or "events" based on the count <a class="yt-timestamp" data-t="23:05:00">[23:05:00]</a>.
3.  **Events Attended:** Duplicate the previous formula property.
    *   Change the text to "Events attended:" <a class="yt-timestamp" data-t="26:20:00">[26:20:00]</a>.
    *   Change the color (e.g., to "green") <a class="yt-timestamp" data-t="26:28:00">[26:28:00]</a>.
    *   Change the property referenced to "Events Attended (Rollup)" <a class="yt-timestamp" data-t="26:30:00">[26:30:00]</a>.

### Attendance Percentage (Formula)
To show the percentage of attended events:
1.  Add a new property and select "Formula" <a class="yt-timestamp" data-t="27:37:00">[27:37:00]</a>.
2.  Use the formula `round(prop("Events Attended (Rollup)") / prop("Number of Events (Rollup)") * 100) / 100` <a class="yt-timestamp" data-t="28:22:00">[28:22:00]</a>.
3.  Change the number format to "Percentage" <a class="yt-timestamp" data-t="28:11:00">[28:11:00]</a>.
4.  For visual illustration, change "Show as" to "Bar" (or "Ring") and select a color (e.g., "blue") <a class="yt-timestamp" data-t="28:56:00">[28:56:00]</a>.

## Dashboard Assembly

Now, link these databases to your main "Relationship Tracker" dashboard <a class="yt-timestamp" data-t="29:26:00">[29:26:00]</a>.

### Person Database View
1.  On the main "Relationship Tracker" page, type `/` and `linked` to add a "Linked view of database" <a class="yt-timestamp" data-t="29:50:00">[29:50:00]</a>.
2.  Select your "DB_Person_database_new" <a class="yt-timestamp" data-t="30:17:00">[30:17:00]</a>.
3.  Change the layout to "Gallery" view <a class="yt-timestamp" data-t="30:28:00">[30:28:00]</a>.
4.  Adjust card size to "Small" <a class="yt-timestamp" data-t="30:44:00">[30:44:00]</a>.
5.  In properties, show "Relation" so the relation appears on each card <a class="yt-timestamp" data-t="31:07:00">[31:07:00]</a>.
6.  Set "Card preview" to "Image" so the person's image is displayed on the card <a class="yt-timestamp" data-t="35:45:00">[35:45:00]</a>.

### Events Calendar View
1.  Add another linked database view below the person database <a class="yt-timestamp" data-t="40:20:00">[40:20:00]</a>.
2.  Select your "DB_Events_database_new" <a class="yt-timestamp" data-t="40:29:00">[40:29:00]</a>.
3.  Change the layout to "Calendar" view <a class="yt-timestamp" data-t="40:45:00">[40:45:00]</a>.
4.  In properties, show "Event Type", "Person", and "Attendance" <a class="yt-timestamp" data-t="41:09:00">[41:09:00]</a>. You can also show "Priority" <a class="yt-timestamp" data-t="42:02:00">[42:02:00]</a>.
5.  You can change the calendar view to "Monthly" or "Weekly" <a class="yt-timestamp" data-t="43:05:00">[43:05:00]</a>.

### Events Summary View
1.  Add a third linked database view <a class="yt-timestamp" data-t="44:15:00">[44:15:00]</a>.
2.  Select your "DB_Person_database_new" again <a class="yt-timestamp" data-t="44:19:00">[44:19:00]</a>.
3.  Change the layout to "Board" view <a class="yt-timestamp" data-t="44:48:00">[44:48:00]</a>.
4.  Set "Group by" to "Relation" <a class="yt-timestamp" data-t="45:24:00">[45:24:00]</a>.
5.  Enable "Hide empty groups" <a class="yt-timestamp" data-t="45:34:00">[45:34:00]</a>.
6.  In properties, ensure "Number of events", "Events attended", and "Attendance Percentage" formulas are visible <a class="yt-timestamp" data-t="46:03:00">[46:03:00]</a>.
7.  Rename this section to "Events Summary" <a class="yt-timestamp" data-t="46:58:00">[46:58:00]</a>.

### Event Details (Columnar Layout)
To arrange the event adding button and a detailed event list side-by-side:
1.  Add a divider (`/divider`) <a class="yt-timestamp" data-t="47:33:00">[47:33:00]</a>.
2.  Type `/` and `two columns` to create two vertical columns <a class="yt-timestamp" data-t="47:52:00">[47:52:00]</a>.
3.  **Left Column: Add Event Button**
    *   Add a "Button" block (`/button`) <a class="yt-timestamp" data-t="48:03:00">[48:03:00]</a>.
    *   Name it "Add Event" <a class="yt-timestamp" data-t="48:21:00">[48:21:00]</a> and set its icon <a class="yt-timestamp" data-t="48:24:00">[48:24:00]</a>.
    *   Configure the button to "Add page to" your "DB_Events_database_new" <a class="yt-timestamp" data-t="48:33:00">[48:33:00]</a>.
    *   Set default properties, like "Event Name" to "Enter event name" and "Date" to "Today" <a class="yt-timestamp" data-t="48:49:00">[48:49:00]</a>.
4.  **Right Column: Event Details Table**
    *   Add a linked database view of your "DB_Events_database_new" <a class="yt-timestamp" data-t="49:20:00">[49:20:00]</a>.
    *   Drag this linked database into the right column <a class="yt-timestamp" data-t="49:30:00">[49:30:00]</a>.
    *   Group this view by "Date" <a class="yt-timestamp" data-t="49:55:00">[49:55:00]</a>.
    *   Hide empty groups <a class="yt-timestamp" data-t="50:14:00">[50:14:00]</a>.
    *   Sort by "Oldest first" <a class="yt-timestamp" data-t="50:18:00">[50:18:00]</a>.
    *   Set "Date by" to "Month" for a monthly organization of events <a class="yt-timestamp" data-t="50:50:00">[50:50:00]</a>.
    *   Hide vertical lines in the table layout for a cleaner look <a class="yt-timestamp" data-t="53:13:00">[53:13:00]</a>.

## Adding Data and Advanced Options

### Adding New People/Events
*   You can add a new person by clicking the "Add Event" button (in the Event Details column) and entering a new name in the "Person" property. Notion will automatically create a new entry for this person in the "Person Database" <a class="yt-timestamp" data-t="52:12:00">[52:12:00]</a>.
*   Alternatively, you can use templates or buttons for adding entries, but manually adding via relation properties is efficient <a class="yt-timestamp" data-t="36:38:00">[36:38:00]</a>.

### Page Section for Relations
You can change how relation properties are displayed within a person's page:
1.  Open a person's page from the "Person Database" <a class="yt-timestamp" data-t="55:47:00">[55:47:00]</a>.
2.  Click the six dots next to the "Event Details" relation property <a class="yt-timestamp" data-t="56:09:00">[56:09:00]</a>.
3.  Select "Show as" and then "Page section" <a class="yt-timestamp" data-t="56:12:00">[56:12:00]</a>. This will embed a view of all related events directly within the person's page, allowing you to see dates, priorities, and attendance without leaving the page <a class="yt-timestamp" data-t="56:14:00">[56:14:00]</a>.