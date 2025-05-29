---
title: Designing a dashboard with linked databases and calendar view in Notion
videoId: h47T7sRTmg0
---

From: [[theaccountantguy]] <br/> 

This guide details the creation of a Notion dashboard designed to track events associated with people in your life, such as family members, friends, or colleagues. The dashboard allows for scheduling events in advance, ensuring no occasion is missed <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. It incorporates information about people, their relationships, specific events like marriages or birthdays, and provides a summarized view of events <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

The template for this dashboard is available for download on Gumroad by searching for "relationship" <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## Initial Setup in Notion

Before building the dashboard, it's beneficial to configure Notion's page settings for optimal viewing:
*   Click the three dots on the right side of the page <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   Enable **Full Width** to utilize the entire page <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   You can also toggle **Small Text** to adjust font size <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Creating the Main Dashboard Page
1.  Add a new page in Notion <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
2.  Name it "Relationship Tracker" <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
3.  Add a divider by typing `/divider` or `---` <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
4.  Add an icon (e.g., a user icon) <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
5.  Add a cover image (e.g., a solid background color) <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

## Building the Underlying Databases

The dashboard is built upon multiple [[setting_up_a_database_in_Notion | Notion databases]] that hold and link information <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. It's recommended to create a dedicated sub-page for these databases to keep the main dashboard clean <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
1.  Inside the "Relationship Tracker" page, add a new sub-page by typing `/page` and selecting `Page` <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
2.  Name this sub-page "Database" and give it an icon (e.g., stacked discs) <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
3.  Set this page to "Full Width" <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### 1. Person Database
This database will store information about the people in your life <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
1.  Inside the "Database" sub-page, [[setting_up_a_database_in_Notion | create a new inline database]] by typing `/database inline` <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
2.  Rename the database to `DB_Person Database_New` (or similar) <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a> and set its display name to "Person Database" <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
3.  Add hypothetical names like Susan, Harry, Sarah, and Peter <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
4.  [[customizing_databases_in_Notion | Add an icon to each person]] by opening their page and clicking "Add Icon" <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
5.  Rename the default "Tags" property to **Relation** <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
6.  Populate the `Relation` property (e.g., Sister, Friend, Colleague) <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
7.  Add a new property named **Image** with the type `Files & media` <a class="yt-timestamp" data-t="00:33:11">[00:33:11]</a>. Upload an image for each person <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>. You can also add a cover image to each person's page <a class="yt-timestamp" data-t="00:33:57">[00:33:57]</a>.

### 2. Events Details Database
This database will store information about specific events <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
1.  Below the Person Database, [[setting_up_a_database_in_Notion | create another inline database]] <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
2.  Rename it to `DB_Events Database_New` <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a> and set its display name to "Events Details" <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
3.  Rename the default "Name" property to **Event Name** <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
4.  Add the following properties:
    *   **Date**: Type `Date` <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
    *   **Attendance**: Type `Checkbox` <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.
    *   **Event Type**: Type `Select` (e.g., Birthday, Marriage, Graduation) <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.
    *   **Priority**: Type `Select` (e.g., Low, Medium, High) <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>.

### Linking Databases (Relation Property)
To connect events to people, you'll use a `Relation` property <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
1.  In the **Events Details** database, add a new property <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
2.  Select type `Relation` <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
3.  Choose `DB_Person Database_New` as the database to relate to <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
4.  Enable "Show on `DB_Person Database_New`" and name the property "Event Details" <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. This creates a reciprocal link <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
5.  Rename the property in the Events Details database to **Person** <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
6.  Now, for each event in the `Events Details` database, link it to the relevant person from the `Person Database` using the `Person` property <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.

## Creating Event Summary (Rollup and Formulas)

This section, built within the **Person Database**, will summarize event information for each person <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.

### 1. Number of Events (Rollup Property)
1.  In the `Person Database`, add a new property <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
2.  Select type `Rollup` <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
3.  Configure the rollup:
    *   **Relation**: Choose the `Event Details` property (linking to the Events database) <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
    *   **Property**: Select `Event Name` <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
    *   **Calculate**: Choose `Count values` <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.
4.  Rename this property to **Number of Events (Rollup)** <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.

### 2. Events Attended (Rollup Property)
1.  Duplicate the "Number of Events (Rollup)" property <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>.
2.  Rename the duplicate to **Events Attended (Rollup)** <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.
3.  Configure this rollup:
    *   **Relation**: `Event Details` <a class="yt-timestamp" data-t="00:25:14">[00:25:14]</a>.
    *   **Property**: Select `Attendance` <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.
    *   **Calculate**: Choose `Count checked` <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>. This will count only the events marked as attended.

### 3. Number of Events (Formula Property with Styling)
This property will display the total number of events with custom formatting <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.
1.  Add a new property of type `Formula` <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.
2.  Name it "Number of Events" <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.
3.  [[creating_a_database_in_Notion_for_calculations | Enter the following formula]]:
    ```notion
    if(prop("Number of Events (Rollup)") <= 1, style(format(prop("Number of Events (Rollup)")), "b", "blue") + " event", style(format(prop("Number of Events (Rollup)")), "b", "blue") + " events")
    ```
    *   This formula checks if the `Number of Events (Rollup)` is 1 or less.
    *   If true, it displays the number in bold blue followed by "event".
    *   If false, it displays the number in bold blue followed by "events" (plural) <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>.

### 4. Events Attended (Formula Property with Styling)
This property will display the number of attended events with custom formatting.
1.  Duplicate the "Number of Events" formula property <a class="yt-timestamp" data-t="00:25:56">[00:25:56]</a>.
2.  Rename it to "Events Attended" <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>.
3.  Modify the formula to use the "Events Attended (Rollup)" property and change the color to green:
    ```notion
    if(prop("Events Attended (Rollup)") <= 1, style(format(prop("Events Attended (Rollup)")), "b", "green") + " event attended", style(format(prop("Events Attended (Rollup)")), "b", "green") + " events attended")
    ```

### 5. Attendance Percentage (Formula Property with Progress Bar)
This property calculates and visualizes the attendance percentage <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.
1.  Add a new property of type `Formula` <a class="yt-timestamp" data-t="00:27:43">[00:27:43]</a>.
2.  Name it "Attendance Percentage" <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.
3.  [[creating_a_database_in_Notion_for_calculations | Enter the formula]]:
    ```notion
    round(prop("Events Attended (Rollup)") / prop("Number of Events (Rollup)"))
    ```
4.  Change the `Number Format` to `Percentage` <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.
5.  Set `Show as` to `Bar` and choose a color (e.g., blue) <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a>.

## Linking Databases to the Main Dashboard

Now, return to the main "Relationship Tracker" page to display these databases <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.

### 1. People View (Gallery)
1.  On the main "Relationship Tracker" page, type `/linked database` <a class="yt-timestamp" data-t="00:29:52">[00:29:52]</a>.
2.  Select `DB_Person Database_New` <a class="yt-timestamp" data-t="00:30:17">[00:30:17]</a>.
3.  Click the three dots next to the database name, go to `Layout`, and select `Gallery` <a class="yt-timestamp" data-t="00:30:28">[00:30:28]</a>.
4.  In `Layout` settings, set `Card size` to `Small` <a class="yt-timestamp" data-t="00:30:48">[00:30:48]</a>.
5.  Set `Card preview` to `Image` (or `Page Cover`) to display the person's image on the card <a class="yt-timestamp" data-t="00:35:34">[00:35:34]</a>.
6.  Under `Properties`, enable `Relation` to show the relationship type <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>.
7.  To simplify editing a person's details, click the three dots on the gallery view, go to `Layout`, and under `Open pages as`, select `Side peak` <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>. This opens the page details on the right side of your screen <a class="yt-timestamp" data-t="00:32:17">[00:32:17]</a>.

### 2. Events Calendar View
1.  On the main dashboard, click the `+ Add a view` button next to the "Person Database" view <a class="yt-timestamp" data-t="00:40:22">[00:40:22]</a>.
2.  Select `DB_Events Database_New` <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>.
3.  Click the three dots, go to `Layout`, and select `Calendar` <a class="yt-timestamp" data-t="00:40:53">[00:40:53]</a>.
4.  In `Layout` settings, ensure `Show calendar as` is set to `Month` <a class="yt-timestamp" data-t="00:43:07">[00:43:07]</a>.
5.  Under `Properties`, enable `Event Type`, `Person`, and `Attendance` <a class="yt-timestamp" data-t="00:41:09">[00:41:09]</a>. You can also show `Priority` <a class="yt-timestamp" data-t="00:42:04">[00:42:04]</a>.

### 3. Event Summary (Board View)
This view provides a summarized overview of events grouped by relationship <a class="yt-timestamp" data-t="00:44:09">[00:44:09]</a>.
1.  Add another linked database view of `DB_Person Database_New` <a class="yt-timestamp" data-t="00:44:19">[00:44:19]</a>.
2.  Change its layout to `Board` <a class="yt-timestamp" data-t="00:44:48">[00:44:48]</a>.
3.  Name this view "Events Summary" <a class="yt-timestamp" data-t="00:47:03">[00:47:03]</a>.
4.  In `Layout` settings, set `Card size` to `Medium` <a class="yt-timestamp" data-t="00:45:09">[00:45:09]</a>.
5.  Under `Group`, ensure `Group by` is set to `Relation` <a class="yt-timestamp" data-t="00:45:24">[00:45:24]</a>.
6.  Enable `Hide empty groups` to remove columns without people <a class="yt-timestamp" data-t="00:45:34">[00:45:34]</a>.
7.  Under `Properties`, enable `Number of Events`, `Events Attended`, and `Attendance Percentage` <a class="yt-timestamp" data-t="00:46:05">[00:46:05]</a>.

## Adding Event Details Section (Two Columns)
To enhance usability, create a section for adding new events.
1.  Add a divider (`---`) on the main dashboard <a class="yt-timestamp" data-t="00:47:33">[00:47:33]</a>.
2.  Type `/2 columns` to create two side-by-side columns <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a>.

### Left Column: Add Event Button
1.  In the left column, add a new `Button` block by typing `/button` <a class="yt-timestamp" data-t="00:48:03">[00:48:03]</a>.
2.  Name the button "Add Event" and choose an icon (e.g., a plus sign) <a class="yt-timestamp" data-t="00:48:21">[00:48:21]</a>.
3.  Configure the button's action:
    *   Click `Add a step`.
    *   Select `Add page to` <a class="yt-timestamp" data-t="00:48:33">[00:48:33]</a>.
    *   Choose `DB_Events Database_New` <a class="yt-timestamp" data-t="00:48:42">[00:48:42]</a>.
    *   Set the `Event Name` property to "Enter event name" <a class="yt-timestamp" data-t="00:48:50">[00:48:50]</a>.
    *   Optionally, set the `Date` property to `Today` <a class="yt-timestamp" data-t="00:49:01">[00:49:01]</a>.

### Right Column: Events Details (Grouped by Month)
1.  In the right column, add a linked database view of `DB_Events Database_New` <a class="yt-timestamp" data-t="00:49:22">[00:49:22]</a>.
2.  Click the three dots, go to `Group`, and set `Group by` to `Date` <a class="yt-timestamp" data-t="00:49:57">[00:49:57]</a>.
3.  Enable `Hide empty groups` <a class="yt-timestamp" data-t="00:51:15">[00:51:15]</a>.
4.  Set `Sort` to `Oldest first` to display upcoming events chronologically <a class="yt-timestamp" data-t="00:50:42">[00:50:42]</a>.
5.  Set `Date by` to `Month` to group events by month <a class="yt-timestamp" data-t="00:51:04">[00:51:04]</a>.
6.  For a cleaner look, you can hide vertical lines in the table layout by going to `Layout` and disabling `Show vertical lines` <a class="yt-timestamp" data-t="00:53:15">[00:53:15]</a>.

### Adding New People Directly
You can add new people to the Person Database directly from the Events Details database. When linking an event to a person, if the person doesn't exist, you can type their name in the `Person` relation property and Notion will prompt you to create a new page for them in the Person Database <a class="yt-timestamp" data-t="00:52:12">[00:52:12]</a>.

### Enhanced Relation Property View
For related properties (like the `Event Details` property in the Person Database), you can change how they are displayed on the page of an individual record.
1.  Open any person's page (e.g., Susan's).
2.  Hover over the `Event Details` property, click the six dots next to it <a class="yt-timestamp" data-t="00:56:09">[00:56:09]</a>.
3.  Select `Show as` and then `Page section` <a class="yt-timestamp" data-t="00:56:12">[00:56:12]</a>.
4.  This will display the linked events (from the Events Details database) directly on the person's page, as a dedicated section, showing their details, dates, and attendance status <a class="yt-timestamp" data-t="00:56:16">[00:56:16]</a>. This provides a quick glance at all events associated with that person <a class="yt-timestamp" data-t="00:57:25">[00:57:25]</a>.