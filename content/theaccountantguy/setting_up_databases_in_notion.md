---
title: Setting up databases in Notion
videoId: h47T7sRTmg0
---

From: [[theaccountantguy]] <br/> 

This article outlines how to [[creating_and_connecting_databases_in_notion | create and connect databases in Notion]] to build a relationship tracker dashboard. The tracker helps manage events associated with people in your life, such as family, friends, or colleagues, ensuring you never miss an occasion <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The dashboard provides an overview of connected individuals, their relationship categories, and upcoming events like marriages or birthdays <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. It also includes an event summary to track attended events and overall attendance <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Initial Notion Page Setup

Before [[creating a database in Notion | creating a database in Notion]], it is helpful to configure basic page settings:
*   **Full Width View**: Select the "Full Width" option from the three dots menu on the right side of the page to expand the page view <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This provides more space for the dashboard.
*   **New Page Creation**: [[setting_up_a_database_in_notion | Set up a new page]] by clicking "New page" to create a blank canvas for your dashboard <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Title and Divider**: Give the page a title (e.g., "Relationship Tracker") and add a divider (`/divider`) for visual separation <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **Icon and Cover Image**: Add an icon and a cover image to personalize the page. These can be chosen from Notion's library or uploaded <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## Creating Databases

The relationship tracker is built upon multiple interconnected databases <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. It is recommended to create a dedicated sub-page for all databases to keep the main dashboard clean <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

### Database Sub-Page
1.  Create a new sub-page within the main "Relationship Tracker" page <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
2.  Name it (e.g., "DB - Person Database_New") and customize with an icon <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

### Person Database
This database stores information about the people connected in your life <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
1.  In the database sub-page, type `/database` and select "Inline database" <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
2.  Rename the database (e.g., "Person Database") <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
3.  **Add People**: Enter names of individuals (e.g., "Susan," "Harry," "Sarah") <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
4.  **Add Icons**: Click "Open" on each person's entry and select an icon <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
5.  **Relation Property**: Rename the default "Tags" property to "Relation" to define the relationship (e.g., "Sister," "Friend," "Colleague") <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

### Events Detail Database
This database will hold all event information and be [[linking_databases_in_notion | linked to the Person Database]] <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
1.  Below the Person Database, type `/database` and select "Inline database" <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
2.  Rename it (e.g., "DB - Events Database_New") and assign an icon <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
3.  **Event Name Property**: Rename the default "Name" property to "Event Name" <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
4.  **Date Property**: Add a new property of type "Date" to schedule events <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
5.  **Attendance Checkbox**: Add a "Checkbox" property named "Attendance" to mark if an event has been attended <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
6.  **Event Type Property**: Add a "Select" property named "Event Type" to categorize events (e.g., "Birthday," "Marriage," "Graduation") <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.
7.  **Relation Property (Linking Databases)**:
    *   Add a new property of type "Relation" <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
    *   Select the "Person Database" to link to it <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
    *   Choose to "Show on other database" and name the property (e.g., "Event Detail") <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. This creates a two-way link <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
    *   In the Events Detail Database, rename the newly linked property to "Person" for clarity <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
    *   Now, for each event, select the relevant person from the "Person" property dropdown <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.

## Database Linking and Rollups for Event Summary

To create an event summary, you'll use "Rollup" and "Formula" properties in the Person Database, deriving information from the linked Events Detail Database <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.

### Number of Events (Rollup)
1.  In the Person Database, add a new "Rollup" property <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
2.  Configure it:
    *   **Relation**: Select the "Event Detail" relation (from the linked Events Database) <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
    *   **Property**: Select "Event Name" <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
    *   **Calculate**: Choose "Count values" to count the total events for each person <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.
3.  Rename this property to "Number of Events (Rollup)" <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.

### Number of Events (Formula)
This property displays the count with custom text and styling <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.
1.  Add a new "Formula" property and name it "Number of Events" <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.
2.  Use the following formula structure to display "Number of Events: [Count] event(s)":
    ```notion
    if(prop("Number of Events (Rollup)") <= 1, style("Number of Events: " + format(prop("Number of Events (Rollup)")), "b", "blue") + " event", style("Number of Events: " + format(prop("Number of Events (Rollup)")), "b", "blue") + " events")
    ```
    This formula checks if the event count is singular or plural and applies bold blue styling <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.
3.  Hide the original "Number of Events (Rollup)" property <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>.

### Events Attended (Rollup)
1.  Duplicate the "Number of Events (Rollup)" property <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>.
2.  Rename it "Events Attended (Rollup)" <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.
3.  Configure it:
    *   **Relation**: "Event Detail" <a class="yt-timestamp" data-t="00:25:14">[00:25:14]</a>.
    *   **Property**: "Attendance" (the checkbox property) <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.
    *   **Calculate**: Choose "Count checked" to count only attended events <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>.

### Events Attended (Formula)
This property displays the count of attended events with custom styling <a class="yt-timestamp" data-t="00:25:56">[00:25:56]</a>.
1.  Duplicate the "Number of Events" formula property.
2.  Rename it "Events Attended" <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>.
3.  Modify the formula to use the "Events Attended (Rollup)" property and change the color to green:
    ```notion
    if(prop("Events Attended (Rollup)") <= 1, style("Events Attended: " + format(prop("Events Attended (Rollup)")), "b", "green") + " event", style("Events Attended: " + format(prop("Events Attended (Rollup)")), "b", "green") + " events")
    ```
4.  Hide the original "Events Attended (Rollup)" property <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>.

### Attendance Percentage (Formula)
This property calculates and visualizes the attendance percentage <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.
1.  Add a new "Formula" property named "Attendance Percentage" <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.
2.  Enter the formula:
    ```notion
    round(prop("Events Attended (Rollup)") / prop("Number of Events (Rollup)") * 100) / 100
    ```
    This formula divides attended events by total events and rounds the result <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>.
3.  Change the "Number format" for this property to "Percentage" <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.
4.  Change the "Show as" option to "Bar" (or "Ring") and choose a color (e.g., blue) for a visual progress bar <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a>.

## Displaying Databases on the Main Dashboard

Return to the main "Relationship Tracker" page to link and display the created databases.

### Person Database - Gallery View
1.  Type `/linked` and select "Create linked view of database" <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>.
2.  Select the "Person Database" you created <a class="yt-timestamp" data-t="00:30:17">[00:30:17]</a>.
3.  Change the layout to "Gallery" view from the three dots menu <a class="yt-timestamp" data-t="00:30:28">[00:30:28]</a>.
4.  In "Layout," set "Card size" to "Small" <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>.
5.  In "Properties," show "Relation," "Number of Events," "Events Attended," and "Attendance Percentage" <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>.
6.  **Add Image Property**:
    *   Go to the original "Person Database" (the sub-page).
    *   Add a new "Files & media" property and rename it "Image" <a class="yt-timestamp" data-t="00:33:11">[00:33:11]</a>.
    *   Upload images for each person <a class="yt-timestamp" data-t="00:33:28">[00:33:28]</a>.
7.  Back on the main dashboard's Gallery view:
    *   Click the three dots, go to "Layout," and set "Card preview" to "Image" to display the uploaded images <a class="yt-timestamp" data-t="00:35:12">[00:35:12]</a>.

### Events Detail Database - Calendar View
1.  Below the Person Database, add another "Linked view of database" <a class="yt-timestamp" data-t="00:40:20">[00:40:20]</a>.
2.  Select the "Events Database" <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>.
3.  Change the layout to "Calendar" view <a class="yt-timestamp" data-t="00:40:47">[00:40:47]</a>.
4.  In "Properties," show "Event Type," "Person," "Attendance," and "Priority" <a class="yt-timestamp" data-t="00:41:03">[00:41:03]</a>. You can also reorder these properties <a class="yt-timestamp" data-t="00:42:30">[00:42:30]</a>.
5.  Optionally, change the calendar view from "Monthly" to "Weekly" in "Layout" <a class="yt-timestamp" data-t="00:43:05">[00:43:05]</a>.

### Events Summary - Board View
1.  Add another "Linked view of database" and select the "Person Database" again <a class="yt-timestamp" data-t="00:46:19">[00:46:19]</a>.
2.  Change the layout to "Board" view <a class="yt-timestamp" data-t="00:44:48">[00:44:48]</a>.
3.  In "Layout," set "Card size" to "Medium" <a class="yt-timestamp" data-t="00:45:07">[00:45:07]</a>.
4.  In "Group," ensure it is grouped by "Relation" <a class="yt-timestamp" data-t="00:45:24">[00:45:24]</a>.
5.  Select "Hide empty groups" <a class="yt-timestamp" data-t="00:45:34">[00:45:34]</a>.
6.  In "Properties," enable "Number of Events," "Events Attended," and "Attendance Percentage" <a class="yt-timestamp" data-t="00:46:05">[00:46:05]</a>.
7.  Rename the linked database to "Events Summary" <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>.

## Adding New Entries and Advanced Management

### Add Event Button
1.  Below the calendar, add a two-column layout (`/two columns`) <a class="yt-timestamp" data-t="00:47:52">[00:47:52]</a>.
2.  In the left column, add a "Button" block (`/button`) and name it "Add Event" <a class="yt-timestamp" data-t="00:48:12">[00:48:12]</a>.
3.  Configure the button's action:
    *   **Action**: "Add page to" <a class="yt-timestamp" data-t="00:48:33">[00:48:33]</a>.
    *   **Database**: Select "Events Database" <a class="yt-timestamp" data-t="00:48:42">[00:48:42]</a>.
    *   **Properties**: Set "Name" to "Enter Event Name" and "Date" to "Today" <a class="yt-timestamp" data-t="00:48:49">[00:48:49]</a>.
4.  In the right column, add another "Linked view of database" and select the "Events Database" again <a class="yt-timestamp" data-t="00:49:20">[00:49:20]</a>.
5.  **Group by Date**: For this linked view, go to "Group" and select "Date." Choose "Month" for "Date by" <a class="yt-timestamp" data-t="00:50:49">[00:50:49]</a>.
6.  **Sort by Date**: In "Sort," choose "Date" and "Oldest first" <a class="yt-timestamp" data-t="00:50:18">[00:50:18]</a>.
7.  Select "Hide empty groups" <a class="yt-timestamp" data-t="00:51:14">[00:51:14]</a>.
8.  To hide vertical lines, go to "Layout" and uncheck "Show vertical lines" <a class="yt-timestamp" data-t="00:53:13">[00:53:13]</a>.

### Adding New Persons Directly
You can add new people directly from the "Person" property in the Events Detail Database. When typing a new name that isn't in the Person Database, Notion will prompt you to "Add new page to..." the Person Database, automatically creating a new entry <a class="yt-timestamp" data-t="00:52:12">[00:52:12]</a>.

### "Show as Page Section" Feature
When viewing a person's entry in the Person Database (e.g., by clicking their card in the Gallery view), relation properties (like "Event Detail") can be displayed as a "Page section" <a class="yt-timestamp" data-t="00:56:09">[00:56:09]</a>. This means the linked events will appear as a mini-database directly within the person's page, providing a quick overview of all associated events, their dates, priorities, and attendance status <a class="yt-timestamp" data-t="00:56:14">[00:56:14]</a>.

---
For further questions or assistance, contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:55:05">[00:55:05]</a>.