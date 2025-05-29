---
title: Building a relationship tracker using Notion
videoId: h47T7sRTmg0
---

From: [[theaccountantguy]] <br/> 

This article outlines how to create a comprehensive relationship tracker using Notion, designed to help you keep tabs on important events and connections with people in your life <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It ensures you never miss significant occasions like marriages, parties, or functions <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The tracker allows you to manage information about people, their relationship categories, and upcoming events, all viewable in a monthly calendar format with an event summary <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

> [!info] Template Availability
> A pre-built version of this [[notion_relationship_tracker | Notion relationship tracker]] is available for download on the creator's Gumroad page <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Search "relationship" on the page to find it <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. The link is provided in the video's description <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

## Notion Basics

Before beginning, adjust your Notion page settings for optimal viewing:
*   **Small text format:** Optionally reduce text size by selecting the "small text" option from the three-dot menu <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **Full width:** For a broader presentation, enable "full width" from the three-dot menu <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. The creator prefers this setting for the entire presentation <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Setting Up the Tracker Page

1.  **Create a New Page:** Start by creating a new blank page in Notion <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
2.  **Name the Page:** Title the page "Relationship Tracker" <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
3.  **Add a Divider:** Insert a visual break using `/divider` <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
4.  **Add an Icon:** Choose an icon (e.g., a "user" icon) to visually represent the tracker <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
5.  **Add a Cover Image:** Select a cover image, preferably a solid background, for a clean aesthetic <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

## Building the Databases

The tracker relies on interconnected databases. The primary databases are the "Person Database" and "Events Database" <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### Database Sub-Page

It's recommended to create a dedicated sub-page for all your databases to keep the main tracker clean <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
1.  **Create a New Page:** Inside your "Relationship Tracker" page, add a new page (e.g., named "Database") <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
2.  **Configure Sub-Page:** Set this new page to "full width" and assign an icon (e.g., stacked discs) <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### 1. Person Database

This database stores information about the people in your life <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
1.  **Create an Inline Database:** Inside the "Database" sub-page, create an inline database by typing `/database inline` <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
2.  **Rename Database:** Rename the database to `db_person_database_new` (or similar) <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
3.  **Add People:** Populate the database with names (e.g., Susan, Harry, Sarah) <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
4.  **Add Icons:** Assign icons to each person by opening their page and clicking "Add icon" <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
5.  **Define Relations:** Rename the default "Tags" property to "Relation" to categorize relationships (e.g., "Sister", "Friend", "Colleague") <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### 2. Events Database

This database tracks all the events associated with the people in your life <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
1.  **Create an Inline Database:** Below the Person Database, create another inline database <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
2.  **Rename Database:** Name it `db_events_database_new` <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
3.  **Rename Title Property:** Change the default "Name" property to "Event Name" <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
4.  **Add Events:** List hypothetical events (e.g., Susan's Birthday, Harry's Marriage, Sarah's Graduation) <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
5.  **Add "Date" Property:** Add a "Date" property to schedule events. You can include time if needed <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
6.  **Add "Attendance" Checkbox:** Add a "Checkbox" property named "Attendance" to mark if an event was attended <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
7.  **Add "Event Type" Select Property:** Add a "Select" property named "Event Type" to categorize events (e.g., "Birthday", "Marriage", "Graduation") <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

### Linking Databases with "Relation" Property

The "Relation" property is crucial for connecting your Person and Events databases <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
1.  **Add "Relation" Property to Events Database:** In the Events Database, add a new "Relation" property <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
2.  **Select Target Database:** Choose the `db_person_database_new` to link to <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
3.  **Show on Other Database (Optional):** You can opt to show this relation property on the Person Database, naming it "Event Detail" <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
4.  **Assign People to Events:** In the Events Database, link each event to the relevant person from the Person Database <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. This automatically updates the "Event Detail" property in the Person Database <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

## Summarizing Event Information (Rollup & Formula)

To get a summary of events for each person, use "Rollup" and "Formula" properties in the Person Database.

### 1. Number of Events

This property counts the total events for each person <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.
1.  **Add "Rollup" Property:** In the Person Database, add a new "Rollup" property <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
2.  **Configure Rollup:**
    *   **Relation:** Select "Event Details" (the relation property linking to the Events Database) <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
    *   **Property:** Select "Event Name" <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
    *   **Calculate:** Choose "Count values" <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.
3.  **Rename:** Name this property "Number of Events (Rollup)" <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.

### 2. Events Attended

This property counts how many events a person has attended <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.
1.  **Duplicate "Number of Events (Rollup)":** Duplicate the previous rollup property <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>.
2.  **Configure Rollup:**
    *   **Relation:** Keep "Event Details" <a class="yt-timestamp" data-t="00:25:11">[00:25:11]</a>.
    *   **Property:** Select "Attendance" <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.
    *   **Calculate:** Choose "Count checked" to count only attended events <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.
3.  **Rename:** Name this property "Events Attended (Rollup)" <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.

### 3. Number of Events (Formula)

This formula property displays the total event count with conditional text formatting (e.g., "1 event" vs. "2 events") <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.
1.  **Add "Formula" Property:** Add a new "Formula" property <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>.
2.  **Enter Formula:** Use the following formula:
    ```notion
    if(prop("Number of Events (Rollup)") <= 1, style("Number of Events: " + format(prop("Number of Events (Rollup)")) + " Event", "b", "blue"), style("Number of Events: " + format(prop("Number of Events (Rollup)")) + " Events", "b", "blue"))
    ```
    This formula checks if the "Number of Events (Rollup)" is less than or equal to 1. If true, it displays "Event"; otherwise, it displays "Events" <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. It also styles the text to be bold and blue <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.

### 4. Events Attended (Formula)

Similar to the above, this formula property displays the count of attended events with conditional text and green styling <a class="yt-timestamp" data-t="00:26:15">[00:26:15]</a>.
1.  **Duplicate "Number of Events (Formula)":** Duplicate the previous formula property <a class="yt-timestamp" data-t="00:25:56">[00:25:56]</a>.
2.  **Enter Formula:** Modify the formula to use the "Events Attended (Rollup)" property and green color:
    ```notion
    if(prop("Events Attended (Rollup)") <= 1, style("Events Attended: " + format(prop("Events Attended (Rollup)")) + " Event", "b", "green"), style("Events Attended: " + format(prop("Events Attended (Rollup)")) + " Events", "b", "green"))
    ```

### 5. Attendance Percentage

This formula calculates the percentage of attended events and displays it as a progress bar <a class="yt-timestamp" data-t="00:27:30">[00:27:30]</a>.
1.  **Add "Formula" Property:** Add a new "Formula" property named "Attendance Percentage" <a class="yt-timestamp" data-t="00:27:41">[00:27:41]</a>.
2.  **Enter Formula:**
    ```notion
    round(prop("Events Attended (Rollup)") / prop("Number of Events (Rollup)") * 100) / 100
    ```
    This calculates the percentage and rounds it <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>.
3.  **Format as Percentage:** Change the "Number Format" to "Percentage" <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.
4.  **Display as Bar:** In the "Edit Property" settings, select "Show as > Bar" and choose a color (e.g., blue) <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a>.

## Building the Main Dashboard View

Now, link the created databases to the main "Relationship Tracker" page for a summarized view.

### 1. Event Summary (Board View)

This section provides an overview of events grouped by relationship <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.
1.  **Link Database:** On the main tracker page, type `/linked database` and select your `db_person_database_new` <a class="yt-timestamp" data-t="00:30:17">[00:30:17]</a>.
2.  **Change Layout:** Click the three dots on the linked database, go to "Layout," and select "Board" view <a class="yt-timestamp" data-t="00:44:48">[00:44:48]</a>.
3.  **Configure Board Layout:**
    *   **Card Size:** Set "Card size" to "Small" or "Medium" for a clean look <a class="yt-timestamp" data-t="00:45:07">[00:45:07]</a>.
    *   **Group By:** Ensure "Group by" is set to "Relation" <a class="yt-timestamp" data-t="00:45:24">[00:45:24]</a>.
    *   **Hide Empty Groups:** Enable "Hide empty columns" to clean up the view <a class="yt-timestamp" data-t="00:45:44">[00:45:44]</a>.
4.  **Display Properties:** In "Properties," enable `Number of Events (Formula)`, `Events Attended (Formula)`, and `Attendance Percentage` <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>.
5.  **Rename:** Rename this linked database block to "Events Summary" <a class="yt-timestamp" data-t="00:47:03">[00:47:03]</a>.

### 2. Events Details (Calendar View)

This section provides a calendar view of all events <a class="yt-timestamp" data-t="00:40:13">[00:40:13]</a>.
1.  **Link Database:** Add another linked database, this time selecting your `db_events_database_new` <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>.
2.  **Change Layout:** Change the layout to "Calendar" view <a class="yt-timestamp" data-t="00:40:53">[00:40:53]</a>.
3.  **Configure Calendar Properties:** In "Properties," enable `Event Type`, `Person`, and `Attendance` <a class="yt-timestamp" data-t="00:41:03">[00:41:03]</a>. You can also add `Priority` as a "Select" property here to categorize event importance <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>.
4.  **Calendar View Options:**
    *   **Show Calendar As:** Toggle between "Monthly" or "Weekly" view <a class="yt-timestamp" data-t="00:43:14">[00:43:14]</a>.
    *   **Navigation:** Use the navigation arrows to move between weeks/months or click "Today" to return to the current date <a class="yt-timestamp" data-t="00:43:47">[00:43:47]</a>.

### 3. Adding an Image Property to People

To display images in the person cards:
1.  **Open a Person's Page:** Click on any person in the "Event Summary" section to open their page <a class="yt-timestamp" data-t="00:31:47">[00:31:47]</a>.
2.  **Set Page Opening to Side Peak:** In the three-dot menu for the linked database, go to "Open pages as" and select "Side peak" for a cleaner view <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>.
3.  **Add "Image" Property:** Inside a person's page, add a new "Media" property and select "Image" <a class="yt-timestamp" data-t="00:33:11">[00:33:11]</a>.
4.  **Upload Images:** Upload an image for each person <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>. You can also set it as the cover image <a class="yt-timestamp" data-t="00:33:57">[00:33:57]</a>.
5.  **Display Images in Gallery:** Back on the main dashboard, for the "Event Summary" (Person Database) linked view:
    *   Click the three dots > "Layout" > "Card preview."
    *   Select "Image" or "Page cover" to display the uploaded image <a class="yt-timestamp" data-t="00:35:51">[00:35:51]</a>.
    *   Optionally "Fit image" to contain it within the card <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>.

## Enhancing Data Entry

### Add Event Button

Create a quick button to add new events.
1.  **Add a Button:** In the main tracker page, create a new column (e.g., using `/two columns`) and add a "Button" block by typing `/button` <a class="yt-timestamp" data-t="00:48:03">[00:48:03]</a>.
2.  **Configure Button:**
    *   **Name:** "Add Event" <a class="yt-timestamp" data-t="00:48:21">[00:48:21]</a>.
    *   **Icon:** A plus sign <a class="yt-timestamp" data-t="00:48:24">[00:48:24]</a>.
    *   **Action:** Add a step > "Add page to."
    *   **Database:** Select `db_events_database_new` <a class="yt-timestamp" data-t="00:48:42">[00:48:42]</a>.
    *   **Properties:** Set "Event Name" to "Enter event name" and "Date" to "Today" <a class="yt-timestamp" data-t="00:48:49">[00:48:49]</a>.

### Organizing Event Details by Date

In the "Events Details" linked database (calendar view):
1.  **Group By Date:** Click the three dots > "Group" > "Date" <a class="yt-timestamp" data-t="00:49:55">[00:49:55]</a>.
2.  **Hide Empty Groups:** Enable "Hide empty groups" <a class="yt-timestamp" data-t="00:50:14">[00:50:14]</a>.
3.  **Sort Dates:** In "Sort," select "Oldest first" for chronological order <a class="yt-timestamp" data-t="00:50:42">[00:50:42]</a>.
4.  **Date By:** Select "Month" to group events by month <a class="yt-timestamp" data-t="00:51:13">[00:51:13]</a>.

### Adding New People Directly from Events

You can add new people to your `db_person_database_new` directly from the `db_events_database_new` <a class="yt-timestamp" data-t="00:52:02">[00:52:02]</a>. When adding an event, if a person isn't listed, type their name in the "Person" property field and select "Add new" <a class="yt-timestamp" data-t="00:52:15">[00:52:15]</a>. This will automatically create a new entry for them in the Person Database <a class="yt-timestamp" data-t="00:52:26">[00:52:26]</a>.

## Enhanced Property Views

Within a person's individual page (accessed by clicking on their card), you can modify how related properties are displayed <a class="yt-timestamp" data-t="00:55:49">[00:55:49]</a>:
1.  **Show as Page Section:** For a relation property (like "Event Details"), click the six dots next to it, select "Show as," and then "Page section" <a class="yt-timestamp" data-t="00:56:12">[00:56:12]</a>. This docks the related database view directly within the person's page, allowing you to see all associated events and their details (date, priority, attendance) at a glance <a class="yt-timestamp" data-t="00:56:14">[00:56:14]</a>.

This comprehensive [[using_notion_for_relationship_management | Notion relationship management]] system provides a dynamic and visually appealing way to [[tracking_relationship_commitments_in_notion | track relationship commitments]] and ensure you stay connected with important individuals in your life.