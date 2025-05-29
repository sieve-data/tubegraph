---
title: Creating and Linking Notion Databases
videoId: h47T7sRTmg0
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[creating_and_managing_databases_in_notion | create and manage databases]] in Notion, specifically focusing on how to link them to build a comprehensive relationship tracker dashboard <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This system helps keep track of events associated with people in your life, such as family, friends, and colleagues <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Dashboard Overview
The relationship tracker dashboard allows users to:
*   Add information about connected people <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   Categorize relationships (e.g., family, friend, colleague) <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
*   Input events like marriages, birthdays, or other occasions <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   View events in a monthly format <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   Access an event summary showing outlined and attended events per person <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

The template for this tracker is available for download on Gumroad by searching for "relationship" <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## Initial Notion Setup
To begin, start with a new page <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Page Settings**: Click the three dots on the right side of the page <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
    *   **Small Text**: Select this option to reduce the text size <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
    *   **Full Width**: Enable this for the page content to span the entire screen <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. This is recommended for a better presentation <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Naming the Page**: Name the main page, for example, "Relationship Tracker" <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **Divider**: Add a divider by typing `/divider` or `--` to create a clean line <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
*   **Icon and Cover Image**:
    *   Click "Add Icon" and search for an appropriate icon (e.g., "user") <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
    *   Click "Add Cover" to add a background image to the page <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

## [[Creating databases in Notion | Creating Databases in Notion]]

The dashboard is built from a collection of different databases that hold information and are linked together <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### Database Sub-Page
It's recommended to create a dedicated sub-page to store all your databases for organization <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
1.  On your main page, type `/database` and select `Database - Page` <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. This creates a nested page <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
2.  Name this new sub-page, for example, "Database" <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
3.  Set its view to full width and add an icon (e.g., stacked discs) <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### Person Database
This database will store information about the people connected in your life <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
1.  Inside the "Database" sub-page, create a new inline database <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
2.  Name it "DB_Person Database_New" (or similar to differentiate) <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
3.  Rename the default "Name" property to "Person Database" <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
4.  Add hypothetical names (e.g., Susan, Harry, Sarah) <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
5.  **Properties**:
    *   **Relation (Select)**: Rename the default "Tags" property to "Relation" <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. Use this to tag the relationship (e.g., "sister", "friend", "colleague") <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
    *   **Image (Files & Media)**: Add a new property, select "Files & Media", and rename it "Image" <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>. This allows adding images for each person <a class="yt-timestamp" data-t="00:33:14">[00:33:14]</a>.

### Events Database
This database will hold all the event details <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
1.  In the "Database" sub-page, create another inline database by typing `/database` and selecting `Database - Inline` <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
2.  Rename it "DB_Events Database_New" <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
3.  Rename the default "Name" property to "Event Name" <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
4.  Add hypothetical events (e.g., Susan's Birthday, Harry's Marriage, Sarah's Graduation) <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
5.  **Properties**:
    *   **Date (Date)**: Add a "Date" property to schedule events on specific dates <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. You can also include time if needed <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
    *   **Attendance (Checkbox)**: Add a "Checkbox" property named "Attendance" to mark if an event has been attended <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
    *   **Event Type (Select)**: Add a "Select" property named "Event Type" to categorize events (e.g., "Birthday", "Marriage", "Graduation") <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. This is optional <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
    *   **Priority (Select)**: Add a "Select" property named "Priority" with options like "Low", "Medium", "High" <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>.

## [[Connecting a database in Notion | Connecting Databases (Relations)]]
The "Relation" property establishes a link between two databases <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
1.  In the `Events Database`, add a new property and select "Relation" <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
2.  When prompted, select the `Person Database` to link to <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
3.  Choose whether to show this property on the other database; you can name it "Event Detail" <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
4.  Once linked, you can select the relevant person for each event from a dropdown list <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>. This automatically updates the linked `Person Database` page with the associated events <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

## Creating Event Summaries using Rollup and Formula Properties
These properties allow you to derive and display summarized information from linked databases.

### Number of Events (Rollup)
1.  Go to the `Person Database` <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.
2.  Add a new property and select "Rollup" <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
3.  **Configure Rollup**:
    *   **Relation**: Select "Event details" (the relation to the `Events Database`) <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
    *   **Property**: Select "Event Name" <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.
    *   **Calculate**: Select "Count values" to count the total number of events associated with each person <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.
4.  Rename the property to "Number of Events (Rollup)" <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.

### Events Attended (Rollup)
1.  Duplicate the "Number of Events (Rollup)" property <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>.
2.  Rename it to "Events Attended (Rollup)" <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.
3.  **Configure Rollup**:
    *   **Relation**: Keep "Event details" <a class="yt-timestamp" data-t="00:25:14">[00:25:14]</a>.
    *   **Property**: Select "Attendance" (the checkbox property from the `Events Database`) <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.
    *   **Calculate**: Select "Count checked" to count only the events where the attendance checkbox is ticked <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.

### Number of Events (Formula)
This formula property displays the count of events with text and styling <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.
1.  Duplicate one of the Rollup properties and change its type to "Formula" <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>.
2.  Name it "Number of Events" <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.
3.  Enter the following formula, which includes an `if` condition to handle singular and plural "event(s)", bolding, and color <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>:
    ```notion
    if(prop("Number of Events (Rollup)") <= 1, style("Number of Events: " + format(prop("Number of Events (Rollup)")) + " event", "b", "blue"), style("Number of Events: " + format(prop("Number of Events (Rollup)")) + " events", "b", "blue"))
    ```

### Events Attended (Formula)
Similar to the above, but for attended events.
1.  Duplicate the "Number of Events (Formula)" property <a class="yt-timestamp" data-t="00:25:56">[00:25:56]</a>.
2.  Name it "Events Attended" <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>.
3.  Modify the formula to use the `Events Attended (Rollup)` property and a different color (e.g., green):
    ```notion
    if(prop("Events Attended (Rollup)") <= 1, style("Events Attended: " + format(prop("Events Attended (Rollup)")) + " event", "b", "green"), style("Events Attended: " + format(prop("Events Attended (Rollup)")) + " events", "b", "green"))
    ```

### Attendance Percentage (Formula)
This formula calculates the percentage of attended events and displays it as a progress bar <a class="yt-timestamp" data-t="00:27:31">[00:27:31]</a>.
1.  Add a new property and select "Formula" <a class="yt-timestamp" data-t="00:27:43">[00:27:43]</a>.
2.  Name it "Attendance Percentage" <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.
3.  Enter the formula:
    ```notion
    round(prop("Events Attended (Rollup)") / prop("Number of Events (Rollup)") * 100) / 100
    ```
4.  Change the "Number format" to "Percentage" <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.
5.  In "Edit Property" options, select "Bar" for "Show as" and choose a color (e.g., blue) to visualize the percentage <a class="yt-timestamp" data-t="00:28:58">[00:28:58]</a>.

## Displaying Databases on the Main Dashboard

Return to your main "Relationship Tracker" page to link the created databases and present them in various views.

### Linked Person Database (Gallery View)
1.  Type `/linked` and select `Linked view of an existing database` <a class="yt-timestamp" data-t="00:29:52">[00:29:52]</a>.
2.  Select the `DB_Person Database_New` <a class="yt-timestamp" data-t="00:30:17">[00:30:17]</a>.
3.  **Configure View**:
    *   Click the three dots `...` next to the database title.
    *   Go to **Layout** and select "Gallery" view <a class="yt-timestamp" data-t="00:30:28">[00:30:28]</a>.
    *   Set "Card size" to "Small" or "Medium" <a class="yt-timestamp" data-t="00:30:48">[00:30:48]</a>.
    *   Under **Properties**, enable "Name" and "Relation" to display on the cards <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>.
    *   Under **Layout** -> **Card preview**, select "Image" (or "Page Cover") to display the person's image on the card <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>.
    *   You can reposition images by clicking on the image within a card <a class="yt-timestamp" data-t="00:34:08">[00:34:08]</a>.

### Linked Events Database (Calendar View)
1.  Add another linked database view on the main page <a class="yt-timestamp" data-t="00:40:22">[00:40:22]</a>.
2.  Select the `DB_Events Database_New` <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>.
3.  **Configure View**:
    *   Change the **Layout** to "Calendar" <a class="yt-timestamp" data-t="00:40:53">[00:40:53]</a>.
    *   Under **Properties**, enable "Event Type", "Person", "Attendance", and "Priority" to show event details on the calendar <a class="yt-timestamp" data-t="00:41:03">[00:41:03]</a>.
    *   You can arrange the order of properties <a class="yt-timestamp" data-t="00:42:31">[00:42:31]</a>.
    *   To change the calendar display, go to **Layout** -> **Show calendar as** and select "Month" or "Week" <a class="yt-timestamp" data-t="00:43:18">[00:43:18]</a>.

### Events Summary (Board View)
This view provides a summarized overview of events per relationship category.
1.  Add another linked database view on the main page <a class="yt-timestamp" data-t="00:44:19">[00:44:19]</a>.
2.  Select the `DB_Person Database_New` <a class="yt-timestamp" data-t="00:44:27">[00:44:27]</a>.
3.  **Configure View**:
    *   Change the **Layout** to "Board" <a class="yt-timestamp" data-t="00:44:48">[00:44:48]</a>.
    *   Set "Card size" to "Medium" <a class="yt-timestamp" data-t="00:45:07">[00:45:07]</a>.
    *   Under **Group**, select "Relation" to group people by their relationship type <a class="yt-timestamp" data-t="00:45:24">[00:45:24]</a>.
    *   Enable "Hide empty groups" to conceal relationship categories with no people assigned <a class="yt-timestamp" data-t="00:45:34">[00:45:34]</a>.
    *   Under **Properties**, enable "Number of Events", "Events Attended", and "Attendance Percentage" to display on the board cards <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>.
    *   Rename the linked view to "Events Summary" <a class="yt-timestamp" data-t="00:47:03">[00:47:03]</a>.

## Adding Content and Customization
### Page Layout (Columns)
To arrange linked databases side-by-side, use columns <a class="yt-timestamp" data-t="00:47:45">[00:47:45]</a>.
1.  Type `/columns` and select the desired number of columns (e.g., `2 columns`) <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a>.
2.  Drag and drop the linked databases into these columns. For example, place the "Events Summary" on the left and the "Events Details" (Calendar View) on the right <a class="yt-timestamp" data-t="00:49:30">[00:49:30]</a>.

### Adding Entries with Buttons
You can [[setting_up_a_database_in_notion | set up a database in Notion]] to add entries via a button <a class="yt-timestamp" data-t="00:37:58">[00:37:58]</a>.
1.  Type `/button` to create a new button <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a>.
2.  Name the button (e.g., "Add Event") and add an icon (e.g., a plus sign) <a class="yt-timestamp" data-t="00:48:21">[00:48:21]</a>.
3.  **Configure Button**:
    *   Click "Add a step" and select "Add page to" <a class="yt-timestamp" data-t="00:38:31">[00:38:31]</a>.
    *   Select the `DB_Events Database_New` <a class="yt-timestamp" data-t="00:48:42">[00:48:42]</a>.
    *   Set properties for the new page, such as the `Event Name` default text (e.g., "Enter event name") and the `Date` property to "Today" <a class="yt-timestamp" data-t="00:48:49">[00:48:49]</a>.
4.  Place this button above the "Events Details" calendar view <a class="yt-timestamp" data-t="00:49:12">[00:49:12]</a>.

### Filtering and Sorting Events
For the "Events Details" calendar view displayed as a table:
*   **Grouping**: Click the three dots `...` -> **Group** -> "Date" to group events by their date <a class="yt-timestamp" data-t="00:49:50">[00:49:50]</a>.
    *   Enable "Hide empty groups" <a class="yt-timestamp" data-t="00:50:14">[00:50:14]</a>.
    *   **Sort by**: Select "Oldest first" for chronological order <a class="yt-timestamp" data-t="00:50:42">[00:50:42]</a>.
    *   **Date by**: Choose "Month" to group events by month <a class="yt-timestamp" data-t="00:51:02">[00:51:02]</a>.

### Adding New People Directly
When adding a new event, if a person isn't in your `Person Database`, you can add them directly through the "Person" relation property in the `Events Database` <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>. Typing a new name and selecting "Add new property" will automatically create a new entry in the linked `Person Database` <a class="yt-timestamp" data-t="00:52:16">[00:52:16]</a>.

### Styling Table Layouts
To remove vertical lines in a table view, click the three dots `...` -> **Layout** -> **Table** and uncheck "Show vertical lines" <a class="yt-timestamp" data-t="00:53:13">[00:53:13]</a>.

## Viewing Related Information (Page Section)
Within a database item's page, you can display related database entries in a "Page section" <a class="yt-timestamp" data-t="00:56:09">[00:56:09]</a>.
1.  Open any person's page from the `Person Database` (e.g., by clicking on their card in the Gallery view).
2.  For a "Relation" property (e.g., "Event Details"), click the six dots `⋮⋮` next to its name <a class="yt-timestamp" data-t="00:56:09">[00:56:09]</a>.
3.  Select "Show as" -> "Page section" <a class="yt-timestamp" data-t="00:56:12">[00:56:12]</a>. This will dock the related events database underneath the person's properties, showing all associated events directly on their page <a class="yt-timestamp" data-t="00:56:16">[00:56:16]</a>. This allows for a quick glance at all information related to that person <a class="yt-timestamp" data-t="00:57:25">[00:57:25]</a>.