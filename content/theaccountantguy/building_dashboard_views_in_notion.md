---
title: Building dashboard views in Notion
videoId: h47T7sRTmg0
---

From: [[theaccountantguy]] <br/> 

This article details how to construct a comprehensive dashboard in Notion for tracking relationships and associated events, using various database features, rollups, formulas, and linked views <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The dashboard helps users schedule and manage events related to family, friends, and colleagues, ensuring no important occasions are missed <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Getting Started: Page Setup

Before building the dashboard, it's essential to set up the Notion page:
*   **Full Width View** By default, Notion pages restrict the view. To expand the workspace, click the three dots on the right side of the page and select "Full Width" <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>. This provides more space for presentation <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.
*   **New Page Creation** Start by creating a new blank page within Notion <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.
*   **Title and Divider** Name the page (e.g., "Relationship Tracker") and add a divider using `/divider` for a clean presentation <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.
*   **Icons and Covers** Add an icon (e.g., "user" icon) and a cover image to personalize the page <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>. The cover appears in the background of the page header <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.

## Database Fundamentals

The entire dashboard is built upon a collection of linked databases that hold and summarize information <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>.

### Creating a Database Sub-page
It's recommended to create a dedicated sub-page for all databases to keep the main dashboard clean <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>.
1.  Type `/page` and create a new sub-page <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.
2.  Name it (e.g., "Database") and set it to full width <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>.
3.  Add an icon (e.g., stacked discs) for visual identification <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.

### Person Database
This database stores information about people connected in your life <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>.
1.  Inside the "Database" sub-page, type `/database` and select "Database - Inline" <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a>.
2.  Rename the database (e.g., "Person Database") <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.
3.  Add entries (e.g., Susan, Harry, Sarah) <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>.
4.  **Properties:**
    *   `Name` (default property) <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>.
    *   `Relation` (Select property): Defines how people are related (e.g., Sister, Friend, Colleague) <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.
    *   `Image` (Files & Media property): For adding profile pictures <a class="yt-timestamp" data-t="33:11:00">[33:11:00]</a>.

### Events Database
This database stores details about events associated with people <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>.
1.  Inside the "Database" sub-page, type `/database` and select "Database - Inline" <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>.
2.  Rename the database (e.g., "Events Database") <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>.
3.  **Properties:**
    *   `Event Name` (default property) <a class="yt-timestamp" data-t="09:52:00">[09:52:00]</a>.
    *   `Date` (Date property): For scheduling event dates and times <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.
    *   `Attendance` (Checkbox property): To mark if an event was attended <a class="yt-timestamp" data-t="12:15:00">[12:15:00]</a>.
    *   `Event Type` (Select property): Categorize events (e.g., Birthday, Marriage, Graduation) <a class="yt-timestamp" data-t="12:44:00">[12:44:00]</a>.
    *   `Priority` (Select property): Assign priority levels (e.g., Low, Medium, High) <a class="yt-timestamp" data-t="41:31:00">[41:31:00]</a>.
    *   `Person` (Relation property): Crucially, this links the "Events Database" to the "Person Database" <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>. Selecting a person in an event automatically links it to their profile in the "Person Database" <a class="yt-timestamp" data-t="14:47:00">[14:47:00]</a>.

## Summarizing Data with Rollups and Formulas

To create an event summary, new properties are added to the "Person Database" using rollups and formulas.

1.  **Number of Events (Rollup Property):**
    *   Add a new property to the "Person Database" and select "Rollup" <a class="yt-timestamp" data-t="16:51:00">[16:51:00]</a>.
    *   Configure it:
        *   `Relation`: Link to the "Events Database" via the `Event Details` property <a class="yt-timestamp" data-t="17:46:00">[17:46:00]</a>.
        *   `Property`: Select `Event Name` <a class="yt-timestamp" data-t="18:10:00">[18:10:00]</a>.
        *   `Calculate`: Choose `Count Values` <a class="yt-timestamp" data-t="18:23:00">[18:23:00]</a>. This counts the total number of events associated with each person <a class="yt-timestamp" data-t="19:08:00">[19:08:00]</a>.

2.  **Number of Events (Formula Property):**
    *   Add a new `Formula` property <a class="yt-timestamp" data-t="19:43:00">[19:43:00]</a>.
    *   The formula uses the `style()` function to format the text and dynamically changes "event" to "events" based on the count using an `if` condition <a class="yt-timestamp" data-t="23:14:00">[23:14:00]</a>.
    *   Example formula logic: `if(prop("Number of Events (Rollup)") <= 1, style("Number of events: " + prop("Number of Events (Rollup)"), "blue"), style("Number of events: " + prop("Number of Events (Rollup)"), "blue") + "s")` (simplified representation) <a class="yt-timestamp" data-t="23:16:00">[23:16:00]</a>. This displays the number of events with a blue, bolded text <a class="yt-timestamp" data-t="22:20:00">[22:20:00]</a>.

3.  **Events Attended (Rollup Property):**
    *   Duplicate the "Number of Events (Rollup)" property <a class="yt-timestamp" data-t="25:56:00">[25:56:00]</a>.
    *   Configure it to count `Checked` properties from the `Attendance` property in the "Events Database" <a class="yt-timestamp" data-t="25:31:00">[25:31:00]</a>. This counts how many events a person has attended <a class="yt-timestamp" data-t="25:31:00">[25:31:00]</a>.

4.  **Events Attended (Formula Property):**
    *   Duplicate the "Number of Events (Formula)" property <a class="yt-timestamp" data-t="25:56:00">[25:56:00]</a>.
    *   Modify the formula to display the count of "Events Attended" in green <a class="yt-timestamp" data-t="26:17:00">[26:17:00]</a>.

5.  **Attendance Percentage (Formula Property):**
    *   Add a new `Formula` property called "Attendance Percentage" <a class="yt-timestamp" data-t="27:37:00">[27:37:00]</a>.
    *   Formula: `round((prop("Events Attended (Rollup)") / prop("Number of Events (Rollup)")) * 100) / 100` <a class="yt-timestamp" data-t="28:22:00">[28:22:00]</a>.
    *   Change the number format to "Percentage" <a class="yt-timestamp" data-t="28:11:00">[28:11:00]</a>.
    *   Edit the property to display as a visual "Bar" or "Ring" instead of just a number <a class="yt-timestamp" data-t="28:56:00">[28:56:00]</a>.

## Creating Dashboard Views

Once databases are set up, they are linked to the main dashboard page to create different views.

### Person Database View (Gallery View)
1.  On the main dashboard page, type `/linked` and select "Linked view of database" <a class="yt-timestamp" data-t="29:52:00">[29:52:00]</a>.
2.  Select the "Person Database" <a class="yt-timestamp" data-t="30:17:00">[30:17:00]</a>.
3.  Change the layout to "Gallery" view <a class="yt-timestamp" data-t="30:28:00">[30:28:00]</a>.
4.  Adjust card size to "Small" under Layout properties <a class="yt-timestamp" data-t="30:46:00">[30:46:00]</a>.
5.  Under Properties, ensure `Name` and `Relation` are visible <a class="yt-timestamp" data-t="31:07:00">[31:07:00]</a>.
6.  Set "Card preview" to `Image` in Layout properties to display profile pictures <a class="yt-timestamp" data-t="35:12:00">[35:12:00]</a>.

### Event Details View (Calendar View)
1.  Add another "Linked view of database" on the main dashboard <a class="yt-timestamp" data-t="40:22:00">[40:22:00]</a>.
2.  Select the "Events Database" <a class="yt-timestamp" data-t="40:29:00">[40:29:00]</a>.
3.  Change the layout to "Calendar" view <a class="yt-timestamp" data-t="40:53:00">[40:53:00]</a>.
4.  Under Properties, make `Event Type`, `Person`, `Attendance`, and `Priority` visible <a class="yt-timestamp" data-t="41:13:00">[41:13:00]</a>.
5.  Calendar can be displayed in "Monthly" or "Weekly" format under "Show calendar as" in the layout options <a class="yt-timestamp" data-t="43:05:00">[43:05:00]</a>.

### Events Summary View (Board View / Kanban)
This view provides an [[creating_visual_presentations_of_data_in_notion | overview of event attendance]] grouped by relationships.
1.  Add another "Linked view of database" and select the "Person Database" <a class="yt-timestamp" data-t="44:19:00">[44:19:00]</a>.
2.  Change the layout to "Board" view (also known as Kanban board) <a class="yt-timestamp" data-t="44:48:00">[44:48:00]</a>.
3.  Set the card size to "Medium" or "Small" <a class="yt-timestamp" data-t="45:07:00">[45:07:00]</a>.
4.  Ensure "Group by" is set to `Relation` <a class="yt-timestamp" data-t="45:24:00">[45:24:00]</a>.
5.  Hide empty groups if desired <a class="yt-timestamp" data-t="45:34:00">[45:34:00]</a>.
6.  Under Properties, enable `Number of Events`, `Events Attended`, and `Attendance Percentage` to visualize the summary <a class="yt-timestamp" data-t="46:01:00">[46:01:00]</a>.

## Adding New Entries and Advanced Customization

### Adding Events with a Button
To streamline adding new events:
1.  Create a "Two Columns" block using `/two columns` to arrange content <a class="yt-timestamp" data-t="47:52:00">[47:52:00]</a>.
2.  In the left column, add a "Button" using `/button` <a class="yt-timestamp" data-t="48:03:00">[48:03:00]</a>.
3.  Configure the button:
    *   Set name: "Add Event" <a class="yt-timestamp" data-t="48:21:00">[48:21:00]</a>.
    *   Add a step: "Add page to" <a class="yt-timestamp" data-t="48:33:00">[48:33:00]</a>.
    *   Select "Events Database" <a class="yt-timestamp" data-t="48:42:00">[48:42:00]</a>.
    *   Set `Event Name` property to "Enter event name" <a class="yt-timestamp" data-t="48:49:00">[48:49:00]</a>.
    *   Set `Date` property to "Today" <a class="yt-timestamp" data-t="49:01:00">[49:01:00]</a>. Clicking this button will instantly add a new event with the current date <a class="yt-timestamp" data-t="49:50:00">[49:50:00]</a>.

### Events Detail Section (Table View)
In the right column of the two-column block:
1.  Add another "Linked view of database" and select the "Events Database" <a class="yt-timestamp" data-t="49:20:00">[49:20:00]</a>.
2.  Keep the default "Table" layout.
3.  Group the information by `Date` <a class="yt-timestamp" data-t="49:55:00">[49:55:00]</a>.
4.  Sort by `Oldest first` <a class="yt-timestamp" data-t="50:32:00">[50:32:00]</a>.
5.  "Date by" can be set to `Month` to organize events monthly <a class="yt-timestamp" data-t="51:04:00">[51:04:00]</a>.
6.  Hide "empty groups" to keep the view clean <a class="yt-timestamp" data-t="51:14:00">[51:14:00]</a>.
7.  To remove vertical lines in the table for a cleaner look, click the three dots, select "Layout of table," and uncheck "Show vertical lines" <a class="yt-timestamp" data-t="53:13:00">[53:13:00]</a>.

### Adding New People On The Fly
When adding a new event and selecting a person, you can type a new name if it doesn't exist in the "Person Database." Notion will offer to "Add new person" directly from that prompt, automatically creating an entry in the "Person Database" <a class="yt-timestamp" data-t="52:12:00">[52:12:00]</a>.

### Showing Relation Properties as Page Sections
For a detailed view within a person's page:
1.  Open a person's page from the "Person Database" (e.g., Susan's page).
2.  Click the six dots next to the `Event Details` (relation) property <a class="yt-timestamp" data-t="56:09:00">[56:09:00]</a>.
3.  Select "Show as" and then "Page section" <a class="yt-timestamp" data-t="56:12:00">[56:12:00]</a>. This docks the related events directly underneath the person's properties, allowing you to see all events associated with that person, including their dates, priorities, and attendance status <a class="yt-timestamp" data-t="56:14:00">[56:14:00]</a>.

This robust setup allows for comprehensive tracking and visualization of relationship-based events within Notion.