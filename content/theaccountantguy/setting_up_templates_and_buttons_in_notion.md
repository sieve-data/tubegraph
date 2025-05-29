---
title: Setting up templates and buttons in Notion
videoId: h47T7sRTmg0
---

From: [[theaccountantguy]] <br/> 

Notion provides robust features for creating and managing databases, including the use of templates and buttons for efficient data entry and display <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This guide outlines how to leverage these features for tasks like tracking events associated with people in your life <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Notion Page Setup Basics

Before building any template, it's beneficial to configure basic Notion page settings:
*   **Small Text/Full Width**: Access the three dots menu on the right side of the Notion page <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>. You can choose to enable "Small Text" to reduce text size <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a> or "Full Width" to expand the page view across the entire screen <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>. Full width is often preferred for a better presentation <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.
*   **New Page Creation**: Create a new blank page by clicking the "New page" option <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.
*   **Naming and Styling**:
    *   Give your page a name, e.g., "Relationship Tracker" <a class="yt-timestamp" data-t="03:05:05">[03:05:05]</a>.
    *   Add a divider using `/divider` or typing `---` to create a clean line <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>.
    *   Add an icon to your page for visual identification, such as a "user" icon <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.
    *   Add a cover image to the page for aesthetic appeal <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.

## Database Creation

The core of a Notion tracker involves building and linking multiple databases <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>.

### Database Sub-Page
It's recommended to create a dedicated sub-page for all your databases to keep the main dashboard clean <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>.
*   Type `/database` and select "Database - inline" <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>. This creates a nested page under the main page <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>.
*   Rename this sub-page, e.g., "DB_person_database_new" <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.

### Person Database
This database stores information about individuals <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>.
*   Rename the default "Untitled" database to "Person Database" <a class="yt-timestamp" data-t="06:56:00">[06:56:00]</a>.
*   **Properties**:
    *   **Name**: Default text property for the person's name (e.g., Susan, Harry, Sarah) <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>.
    *   **Relation**: A multi-select property to categorize relationships (e.g., "Sister", "Friend", "Colleague") <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>.
    *   **Image**: A media property to add an image for each person <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>. These can be displayed as card previews in a gallery view <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>.

### Events Database
This database tracks events associated with the people in the Person Database <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>.
*   Create a new inline database and rename it, e.g., "D_events_database_new" <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>.
*   Rename the initial property to "Event Name" <a class="yt-timestamp" data-t="09:52:00">[09:52:00]</a>.
*   **Properties**:
    *   **Date**: A date property to schedule the event <a class="yt-timestamp" data-t="10:45:00">[10:45:00]</a>. You can include time if needed <a class="yt-timestamp" data-t="11:22:00">[11:22:00]</a>.
    *   **Attendance**: A checkbox property to mark if an event has been attended <a class="yt-timestamp" data-t="11:56:00">[11:56:00]</a>.
    *   **Event Type**: A select property for categories like "Birthday," "Marriage," or "Graduation" <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>.
    *   **Priority**: A select property to assign a priority (e.g., Low, Medium, High) <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>.
    *   **Person (Relation)**: A relation property linking this database to the "Person Database" <a class="yt-timestamp" data-t="13:00:00">[13:00:00]</a>. This allows you to associate events with specific individuals <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>. When relating, you can choose to "Show on other database" to see related events on the person's page <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>.

## Event Summary with Rollup and Formula Properties

To create an event summary dashboard, you'll use rollup and formula properties within the "Person Database" <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>.

### Number of Events (Rollup)
*   Add a new property and select "Rollup" <a class="yt-timestamp" data-t="16:46:00">[16:46:00]</a>.
*   Configure the rollup:
    *   **Relation**: Select the "Event Details" relation (linking to the Events database) <a class="yt-timestamp" data-t="17:45:00">[17:45:00]</a>.
    *   **Property**: Choose "Event Name" <a class="yt-timestamp" data-t="18:08:00">[18:08:00]</a>.
    *   **Calculate**: Select "Count values" <a class="yt-timestamp" data-t="18:20:00">[18:20:00]</a>. This counts the total number of events associated with each person <a class="yt-timestamp" data-t="18:24:00">[18:24:00]</a>.
*   Rename this property to "Number of Events (Rollup)" <a class="yt-timestamp" data-t="19:15:00">[19:15:00]</a>.

### Events Attended (Rollup)
*   Duplicate the "Number of Events (Rollup)" property <a class="yt-timestamp" data-t="24:51:00">[24:51:00]</a>.
*   Rename it to "Events Attended (Rollup)" <a class="yt-timestamp" data-t="25:05:00">[25:05:00]</a>.
*   Configure the rollup:
    *   **Relation**: "Event Details" <a class="yt-timestamp" data-t="25:11:00">[25:11:00]</a>.
    *   **Property**: "Attendance" <a class="yt-timestamp" data-t="25:16:00">[25:16:00]</a>.
    *   **Calculate**: Select "Count checked" <a class="yt-timestamp" data-t="25:31:00">[25:31:00]</a>. This counts only the events where the "Attendance" checkbox is ticked <a class="yt-timestamp" data-t="25:29:00">[25:29:00]</a>.

### Number of Events (Formula)
This formula property displays the count of events with text and proper singular/plural formatting <a class="yt-timestamp" data-t="21:11:00">[21:11:00]</a>.
*   Add a new property and select "Formula" <a class="yt-timestamp" data-t="19:37:00">[19:37:37]</a>.
*   **Formula**:
    ```notion
    if(prop("Number of Events (Rollup)") <= 1, style(prop("Number of Events (Rollup)"), "b", "blue") + " Event", style(prop("Number of Events (Rollup)"), "b", "blue") + " Events")
    ```
    This formula checks if the rollup value is 1 or less. If true, it appends "Event" to the bolded, blue number; otherwise, it appends "Events" <a class="yt-timestamp" data-t="23:14:00">[23:14:00]</a>.

### Events Attended (Formula)
Similar to the above, but for attended events <a class="yt-timestamp" data-t="26:00:00">[26:00:00]</a>.
*   Duplicate the "Number of Events (Formula)" property <a class="yt-timestamp" data-t="25:56:00">[25:56:00]</a>.
*   Rename to "Events Attended" <a class="yt-timestamp" data-t="26:02:00">[26:02:00]</a>.
*   **Formula**: Adjust the formula to use the "Events Attended (Rollup)" property and change the color (e.g., to green) <a class="yt-timestamp" data-t="26:20:00">[26:20:00]</a>.
    ```notion
    if(prop("Events Attended (Rollup)") <= 1, style(prop("Events Attended (Rollup)"), "b", "green") + " Event", style(prop("Events Attended (Rollup)"), "b", "green") + " Events")
    ```

### Attendance Percentage (Formula)
Calculates the attendance rate <a class="yt-timestamp" data-t="27:21:00">[27:21:00]</a>.
*   Add a new "Formula" property, rename to "Attendance Percentage" <a class="yt-timestamp" data-t="27:37:00">[27:37:00]</a>.
*   **Formula**:
    ```notion
    round(prop("Events Attended (Rollup)") / prop("Number of Events (Rollup)") * 100) / 100
    ```
*   Change the number format to "Percentage" <a class="yt-timestamp" data-t="28:11:00">[28:11:00]</a> and display as a "Bar" with a chosen color (e.g., blue) <a class="yt-timestamp" data-t="28:56:00">[28:56:00]</a>.

## Linking Databases and Dashboard Views

Now, link the databases to your main dashboard page <a class="yt-timestamp" data-t="29:26:00">[29:26:00]</a>.

### Person Database (Gallery View)
*   On the main page, type `/linked` and select "Linked view of database" <a class="yt-timestamp" data-t="29:50:00">[29:50:00]</a>.
*   Choose your "Person Database" <a class="yt-timestamp" data-t="30:05:00">[30:05:00]</a>.
*   Change the layout to "Gallery" view <a class="yt-timestamp" data-t="30:26:00">[30:26:00]</a>.
*   Set "Card size" to "Small" <a class="yt-timestamp" data-t="30:42:00">[30:42:00]</a>.
*   In "Properties," select which properties to show on the cards, e.g., "Name" and "Relation" <a class="yt-timestamp" data-t="31:00:00">[31:00:00]</a>.
*   Set "Card preview" to "Image" to display the person's image on the card <a class="yt-timestamp" data-t="35:12:00">[35:12:00]</a>.

### Events Details (Calendar View)
*   Add another linked database view, selecting your "Events Database" <a class="yt-timestamp" data-t="40:22:00">[40:22:22]</a>.
*   Change the layout to "Calendar" view <a class="yt-timestamp" data-t="40:42:00">[40:42:00]</a>.
*   In "Properties," enable visibility for "Event Type," "Person," "Attendance," and "Priority" <a class="yt-timestamp" data-t="41:00:00">[41:00:00]</a>.
*   Calendar can be displayed as "Monthly" or "Weekly" via the calendar settings <a class="yt-timestamp" data-t="43:05:00">[43:05:00]</a>.

### Events Summary (Board View)
*   Add another linked database view of the "Person Database" <a class="yt-timestamp" data-t="44:19:00">[44:19:00]</a>.
*   Change the layout to "Board" view <a class="yt-timestamp" data-t="44:44:00">[44:44:00]</a>.
*   Set "Group by" to "Relation" <a class="yt-timestamp" data-t="45:24:00">[45:24:00]</a>.
*   Hide empty groups if desired <a class="yt-timestamp" data-t="45:34:00">[45:34:00]</a>.
*   Display the formula properties: "Number of Events," "Events Attended," and "Attendance Percentage" <a class="yt-timestamp" data-t="46:03:00">[46:03:00]</a>.

## Adding Content with Templates and Buttons

### Using Templates (Database-specific)
While the transcript touches on database templates <a class="yt-timestamp" data-t="36:42:00">[36:42:00]</a>, it ultimately recommends using buttons for adding new entries in this specific context <a class="yt-timestamp" data-t="37:50:00">[37:50:00]</a>.

### Using Buttons
Buttons provide a quick way to add new entries with pre-defined properties <a class="yt-timestamp" data-t="37:58:00">[37:58:00]</a>.
*   Type `/button` to add a button <a class="yt-timestamp" data-t="38:03:00">[38:03:00]</a>.
*   Name the button (e.g., "Add Event") and add an icon <a class="yt-timestamp" data-t="48:21:00">[48:21:00]</a>.
*   **Configure the button's action**:
    *   Click "Add a step" and select "Add page to" <a class="yt-timestamp" data-t="48:31:00">[48:31:00]</a>.
    *   Choose the "Events Database" <a class="yt-timestamp" data-t="48:42:00">[48:42:00]</a>.
    *   Set the default "Event Name" property, e.g., "Enter event name" <a class="yt-timestamp" data-t="48:49:00">[48:49:00]</a>.
    *   You can also set other default properties, such as "Date" to "Today" <a class="yt-timestamp" data-t="49:01:00">[49:01:00]</a>.
*   Place this button on your dashboard, e.g., in a two-column layout next to the events details <a class="yt-timestamp" data-t="47:45:00">[47:45:00]</a>.

### Two-Column Layout
To organize content side-by-side:
*   Type `/two columns` to create two distinct content areas <a class="yt-timestamp" data-t="47:52:00">[47:52:00]</a>. You can also create three or four columns <a class="yt-timestamp" data-t="47:58:00">[47:58:00]</a>.
*   Drag your "Add Event" button into one column and your "Events Details" (linked database) into the other <a class="yt-timestamp" data-t="49:17:00">[49:17:00]</a>.
*   For the "Events Details" database in this view, consider grouping by "Date" and displaying it by "Month" or "Year" to see events chronologically <a class="yt-timestamp" data-t="49:50:00">[49:50:00]</a>. You can also sort by "Oldest first" or "Newest first" <a class="yt-timestamp" data-t="50:18:00">[50:18:00]</a>.

## Dynamic Features

*   **Adding New Persons on the Fly**: When adding a new event and selecting a person for it, if the person doesn't exist in the "Person Database," Notion allows you to create a new entry for them directly from the event entry <a class="yt-timestamp" data-t="52:02:00">[52:02:02]</a>.
*   **Page Sections for Relations**: For relation properties within a database entry (e.g., a person's page), you can change how the related information is displayed. By clicking the six dots next to the property and selecting "Show as" -> "Page section," all related events will appear as a sub-section on the person's page <a class="yt-timestamp" data-t="56:09:00">[56:09:00]</a>. This provides a quick overview of all associated events directly on the person's profile <a class="yt-timestamp" data-t="56:38:00">[56:38:00]</a>.

This comprehensive setup allows for effective tracking and management of personal events and relationships within Notion. For further assistance, contact Notion for My Use at gmail.com <a class="yt-timestamp" data-t="55:05:00">[55:05:00]</a>.