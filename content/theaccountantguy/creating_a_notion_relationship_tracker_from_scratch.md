---
title: Creating a Notion relationship tracker from scratch
videoId: h47T7sRTmg0
---

From: [[theaccountantguy]] <br/> 

This guide outlines how to build a comprehensive relationship tracker using Notion, designed to help manage and track events associated with people in one's life, such as family, friends, and colleagues <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The tracker allows users to schedule events in advance to avoid missing occasions <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

The dashboard, built from scratch, includes:
*   Information about connected people <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   Categorization of relationships <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
*   Event details (e.g., marriages, birthdays, occasions) <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   A monthly view of events <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   An event summary showing outlined and attended events <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

> [!NOTE]
> This template is available for download on Gumroad by searching for "relationship" <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The link is provided in the video description <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

## Setting Up the Notion Page

Before building the dashboard, it's helpful to configure the Notion page settings:
*   **Small Text**: Reduces text size <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **Full Width**: Expands the page view across the entire screen, which is preferred for presentation <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

To begin:
1.  Create a new blank page <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
2.  Name the page "Relationship Tracker" <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
3.  Add a divider by typing `/divider` (or `---`) for a clean line <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
4.  Add an icon (e.g., "user" icon) <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
5.  Add a cover image for background <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

## Building the Databases

The [[notion_relationship_tracker | Notion relationship tracker]] is built upon a collection of linked databases <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### Database Sub-Page

It's recommended to create a separate sub-page to house all the raw databases for organization <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
1.  On the main "Relationship Tracker" page, add a new sub-page by typing `/page` or clicking `+` <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
2.  Name this new sub-page "Database" <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
3.  Set the sub-page to full width and add an icon (e.g., stacked disks) <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### Person Database

This database stores information about the people connected in your life <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
1.  Inside the "Database" sub-page, create a new inline database by typing `/database inline` <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
2.  Rename it `DB_Person Database_New` (or simply "Person Database") <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
3.  Add entries for individuals (e.g., Susan, Harry, Sarah) <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
4.  Assign icons to each person <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
5.  Rename the "Tags" property to "Relation" to define relationship types (e.g., "Sister", "Friend", "Colleague") <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
6.  Add an "Image" property (Media type) to upload pictures for each person <a class="yt-timestamp" data-t="00:33:11">[00:33:11]</a>.

### Event Details Database

This database tracks all events <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
1.  Inside the "Database" sub-page, create another inline database <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
2.  Rename it `DB_Events Database_New` (or "Events Details") <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
3.  Rename the "Name" property to "Event Name" <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
4.  Add hypothetical events (e.g., "Susan's birthday", "Harry's marriage", "Sarah's graduation") <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
5.  Add a "Date" property to schedule events <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. Dates can include time, but it's optional <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
6.  Add an "Attendance" property (Checkbox type) to mark if an event was attended <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
7.  Add an "Event Type" property (Select type) for categories like "Birthday", "Marriage", "Graduation" <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
8.  Add a "Priority" property (Select type) with options like "Low", "Medium", "High" <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>.

#### Linking Databases (Relation Property)

To connect events to people:
1.  In the "Event Details" database, add a new property and select "Relation" <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
2.  Choose to relate to the "Person Database" (`DB_Person Database_New`) <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
3.  Choose to show this property on the other database and name it "Event Detail" (this creates a reciprocal link) <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
4.  Rename the relation property in "Event Details" to "Person" for clarity <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
5.  Associate each event with the corresponding person from the "Person Database" <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. When a person is selected in the event, the event automatically appears in their entry in the "Person Database" <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

## Event Summary Calculations (Rollup and Formulas)

Add these properties to the "Person Database" to summarize event data:

### Number of Events (Rollup Property)
This property counts how many events are associated with each person <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.
1.  Add a new property to the "Person Database" and select "Rollup" <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
2.  Configure the rollup:
    *   **Relation**: `Event Details` (the link to the events database) <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
    *   **Property**: `Event Name` <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.
    *   **Calculate**: `Count values` <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.
3.  Rename the property to "Number of Events (Rollup)" <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.

### Events Attended (Rollup Property)
This property counts how many associated events have been marked as "attended" <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.
1.  Duplicate the "Number of Events (Rollup)" property <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>.
2.  Rename the duplicated property to "Events Attended (Rollup)" <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.
3.  Configure the rollup:
    *   **Relation**: `Event Details` <a class="yt-timestamp" data-t="00:25:14">[00:25:14]</a>.
    *   **Property**: `Attendance` (the checkbox) <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.
    *   **Calculate**: `Count checked` <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.

### Number of Events (Formula Property with Styling)
This property displays the total number of events with custom styling and singular/plural text <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.
1.  Add a new "Formula" property to the "Person Database" and name it "Number of Events" <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.
2.  Enter the following formula:
    ```notion
    if(prop("Number of Events (Rollup)") <= 1, style(format(prop("Number of Events (Rollup)")), "b", "blue") + " event", style(format(prop("Number of Events (Rollup)")), "b", "blue") + " events")
    ```
    This formula checks if the count is 1 or less. If so, it displays "event"; otherwise, it displays "events". The number is bolded and colored blue <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.

### Events Attended (Formula Property with Styling)
Similar to the above, but for attended events <a class="yt-timestamp" data-t="00:25:55">[00:25:55]</a>.
1.  Duplicate the "Number of Events (Formula)" property.
2.  Rename it "Events Attended" <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>.
3.  Modify the formula to reference `Events Attended (Rollup)` and change the color to green <a class="yt-timestamp" data-t="00:26:20">[00:26:20]</a>.
    ```notion
    if(prop("Events Attended (Rollup)") <= 1, style(format(prop("Events Attended (Rollup)")), "b", "green") + " event", style(format(prop("Events Attended (Rollup)")), "b", "green") + " events")
    ```

### Attendance Percentage (Formula Property with Progress Bar)
This calculates the attendance percentage and displays it as a visual bar <a class="yt-timestamp" data-t="00:27:24">[00:27:24]</a>.
1.  Add a new "Formula" property to the "Person Database" and name it "Attendance Percentage" <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.
2.  Enter the formula:
    ```notion
    round(prop("Events Attended (Rollup)") / prop("Number of Events (Rollup)") * 100) / 100
    ```
    This calculates the raw percentage <a class="yt-timestamp" data-t="00:27:54">[00:27:54]</a>.
3.  Change the "Number Format" for this property to "Percentage" <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.
4.  To display as a progress bar or ring:
    *   Click "Edit property" <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>.
    *   Select "Show as": "Bar" (or "Ring") <a class="yt-timestamp" data-t="00:28:59">[00:28:59]</a>.
    *   Choose a color (e.g., blue) <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>.
5.  Hide the raw "Number of Events (Rollup)" and "Events Attended (Rollup)" properties as they are no longer needed for display <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.

## Main Dashboard Layout

Return to the main "Relationship Tracker" page to bring everything together <a class="yt-timestamp" data-t="00:29:35">[00:29:35]</a>.

### People Summary (Gallery View)
1.  Add a linked database view by typing `/linked` <a class="yt-timestamp" data-t="00:29:52">[00:29:52]</a>.
2.  Select the "Person Database" (`DB_Person Database_New`) <a class="yt-timestamp" data-t="00:30:17">[00:30:17]</a>.
3.  Change the layout to "Gallery" view <a class="yt-timestamp" data-t="00:30:28">[00:30:28]</a>.
4.  In Layout settings:
    *   Set "Card size" to "Small" <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>.
    *   Set "Card preview" to "Image" so uploaded pictures appear <a class="yt-timestamp" data-t="00:35:34">[00:35:34]</a>.
5.  In Properties settings, ensure "Relation" is visible <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>.
6.  To open pages in a side peak (instead of center peak):
    *   Click the three dots next to the database title <a class="yt-timestamp" data-t="00:31:59">[00:31:59]</a>.
    *   Go to "Layout" -> "Open pages as" -> "Side peak" <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>.

### Events Calendar (Calendar View)
1.  Add another linked database view below the gallery view <a class="yt-timestamp" data-t="00:40:20">[00:40:20]</a>.
2.  Select the "Events Database" (`DB_Events Database_New`) <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>.
3.  Change the layout to "Calendar" <a class="yt-timestamp" data-t="00:40:53">[00:40:53]</a>.
4.  In Properties, enable visibility for "Event Type", "Person", "Attendance", and "Priority" <a class="yt-timestamp" data-t="00:41:12">[00:41:12]</a>.
5.  Set "Show calendar as" to "Month" for a monthly overview <a class="yt-timestamp" data-t="00:43:05">[00:43:05]</a>. (Can also be set to "Week") <a class="yt-timestamp" data-t="00:43:12">[00:43:12]</a>.

### Events Summary (Board View)
1.  Add another linked database view <a class="yt-timestamp" data-t="00:44:15">[00:44:15]</a>.
2.  Select the "Person Database" <a class="yt-timestamp" data-t="00:44:19">[00:44:19]</a>.
3.  Change the layout to "Board" <a class="yt-timestamp" data-t="00:44:48">[00:44:48]</a>.
4.  In Layout settings:
    *   Set "Card size" to "Medium" <a class="yt-timestamp" data-t="00:45:07">[00:45:07]</a>.
5.  In Grouping settings:
    *   Group by "Relation" to organize people by relationship type <a class="yt-timestamp" data-t="00:45:24">[00:45:24]</a>.
    *   Enable "Hide empty groups" <a class="yt-timestamp" data-t="00:45:34">[00:45:34]</a>.
6.  In Properties, enable visibility for "Number of Events", "Events Attended", and "Attendance Percentage" <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>.
7.  Rename the linked database view to "Events Summary" <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>.

## Adding Events and People

### Adding Events with a Button
1.  Add a two-column layout by typing `/two columns` <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a>.
2.  In the left column, add a "Button" by typing `/button` <a class="yt-timestamp" data-t="00:48:03">[00:48:03]</a>.
3.  Name the button "Add Event" and add a "+" icon <a class="yt-timestamp" data-t="00:48:21">[00:48:21]</a>.
4.  Set the button's action:
    *   `Add a step` -> `Add page to` <a class="yt-timestamp" data-t="00:48:31">[00:48:31]</a>.
    *   Select the "Events Database" <a class="yt-timestamp" data-t="00:48:42">[00:48:42]</a>.
    *   Set default properties for the new page, e.g., "Event Name" to "Enter event name", and "Date" to `today` <a class="yt-timestamp" data-t="00:48:49">[00:48:49]</a>.
5.  In the right column, add another linked database view of the "Events Database" <a class="yt-timestamp" data-t="00:49:20">[00:49:20]</a>.
6.  For this view, set "Group by" to "Date" <a class="yt-timestamp" data-t="00:49:55">[00:49:55]</a>.
7.  Enable "Hide empty groups" and sort by "Oldest first" <a class="yt-timestamp" data-t="00:50:14">[00:50:14]</a>.
8.  Set "Date by" to "Month" to group events by month <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>.

### Adding New People via Event Database
New people can be added directly through the "Person" relation property in the "Events Details" database <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>.
1.  When adding a new event, click on the "Person" property.
2.  Type a new name (e.g., "Peter") <a class="yt-timestamp" data-t="00:52:12">[00:52:12]</a>.
3.  Notion will prompt to create a new page for that person in the "Person Database" <a class="yt-timestamp" data-t="00:52:16">[00:52:16]</a>. This new person will then appear in the "People Summary" and "Events Summary" <a class="yt-timestamp" data-t="00:52:26">[00:52:26]</a>.

## Advanced Features

### Property Visibility
*   Properties can be hidden within a page to keep the view clean <a class="yt-timestamp" data-t="00:32:31">[00:32:31]</a>. Click on the six dots next to the property name and choose "Always hide".

### Show as Page Section
*   When viewing an individual person's page, related information can be displayed as a dedicated section.
*   For the "Event Detail" property (the relation to the events database), click the six dots next to it <a class="yt-timestamp" data-t="00:56:09">[00:56:09]</a>.
*   Select "Show as" -> "Page section" <a class="yt-timestamp" data-t="00:56:12">[00:56:12]</a>. This embeds the related events as a sub-section within the person's page, providing a quick glance of all events associated with them <a class="yt-timestamp" data-t="00:56:33">[00:56:33]</a>.