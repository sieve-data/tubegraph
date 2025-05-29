---
title: Visualizing Data with Notion Layouts and Views
videoId: h47T7sRTmg0
---

From: [[theaccountantguy]] <br/> 

Notion provides robust features for [[tracking_relationships_using_Notion|tracking relationships]] and events, and for visualizing data through various layouts and views. The platform allows users to build comprehensive dashboards from scratch, incorporating different data sets and presentations to keep track of information effectively <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Setting Up Your Notion Page for Visualization

Before building a dashboard, fundamental page settings can optimize the visual experience:
*   **Small Text**: Reduces text size <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **Full Width**: Expands the page view to occupy the entire screen, which is often preferred for a cleaner presentation <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

New pages can be created as blank canvases for building dashboards <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Adding a name, an icon, and a cover image helps to brand and distinguish the page <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

## Building Core Databases

Data visualization in Notion typically begins with creating and linking multiple databases <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### Person Database
This database stores information about individuals, such as family members, friends, or colleagues, including their names and relationship types <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. Properties can include:
*   **Name**: The individual's name <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Relation**: A multi-select property to categorize relationships (e.g., sister, friend, colleague) <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **Image**: A media property to add a profile image for each person <a class="yt-timestamp" data-t="00:33:16">[00:33:16]</a>.

### Events Detail Database
This database tracks all events associated with individuals. Properties can include:
*   **Event Name**: The name of the event <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   **Date**: The scheduled date and optional time of the event <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   **Attendance**: A checkbox property to mark if an event was attended <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>, <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
*   **Event Type**: A select property to categorize events (e.g., birthday, marriage, graduation) <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
*   **Priority**: A select property to assign a priority level (e.g., low, medium, high) <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>.
*   **Person (Relation Property)**: A relation property linking events to individuals in the "Person Database" <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. This establishes a two-way link where event details are visible in the person's entry and vice-versa <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

## Calculating Custom Data Summaries

Notion's [[calculating_custom_data_summaries_in_Notion|rollup]] and [[using_formulas_in_Notion|formula]] properties are crucial for [[analyzing_financial_data_with_notion_templates|analyzing financial data]] and summarizing data within and across databases.

### Rollup Property
A rollup property pulls information from a related database <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. For example, in the "Person Database":
*   **Number of Events (Rollup)**: Counts the total number of events associated with each person from the "Events Detail Database" <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.
*   **Events Attended (Rollup)**: Counts only the events marked as "attended" for each person <a class="yt-timestamp" data-t="00:25:21">[00:25:21]</a>.

### Formula Property
[[using_formulas_in_Notion|Formulas in Notion]] allow for advanced calculations and custom data formatting.
*   **Styling Text**: The `style()` function can be used to apply bolding, colors (e.g., blue, green), and even background colors to text within a formula <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>, <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.
*   **Conditional Formatting**: An `if` condition can display singular "event" or plural "events" based on the count <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
*   **Attendance Percentage**: Calculates the percentage of attended events by dividing "Events Attended" by "Number of Events" and can be displayed as a bar or ring <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>, <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>. The number format can be set to "percentage" <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.

## Presenting Data with Linked Databases and Views

The final step is to link the created databases to the main dashboard and choose appropriate views for visualization <a class="yt-timestamp" data-t="00:29:26">[00:29:26]</a>.

### Gallery View (for Persons)
A linked view of the "Person Database" can be displayed as a gallery <a class="yt-timestamp" data-t="00:30:28">[00:30:28]</a>.
*   **Card Size**: Can be adjusted (e.g., small, medium) <a class="yt-timestamp" data-t="00:30:46">[00:30:46]</a>.
*   **Properties Display**: Choose which properties are visible on each card (e.g., person name, relation) <a class="yt-timestamp" data-t="00:31:02">[00:31:02]</a>.
*   **Card Preview**: Set to display the "image" property as the card's visual <a class="yt-timestamp" data-t="00:35:12">[00:35:12]</a>. Images can be repositioned within the card <a class="yt-timestamp" data-t="00:34:08">[00:34:08]</a>.

### Calendar View (for Events)
A linked view of the "Events Detail Database" can be presented as a calendar <a class="yt-timestamp" data-t="00:40:45">[00:40:45]</a>.
*   **Layout Options**: Displays events in a monthly or weekly format <a class="yt-timestamp" data-t="00:43:05">[00:43:05]</a>.
*   **Visible Properties**: Select properties to show on each calendar entry (e.g., event type, person, attendance, priority) <a class="yt-timestamp" data-t="00:41:03">[00:41:03]</a>.
*   **Navigation**: Quick navigation buttons allow moving between weeks or months <a class="yt-timestamp" data-t="00:43:32">[00:43:32]</a>.

### Board (Kanban) View (for Event Summary)
A linked view of the "Person Database" can be transformed into a board, providing a summary of events grouped by relationships <a class="yt-timestamp" data-t="00:44:48">[00:44:48]</a>. This helps in the [[presentation_of_expense_data_in_Notion|presentation of expense data in Notion]] or event data.
*   **Grouping**: Group cards by a specific property, such as "Relation," to organize people under categories like "Friend," "Colleague," etc. <a class="yt-timestamp" data-t="00:45:24">[00:45:24]</a>.
*   **Card Size**: Adjust to medium or small for a cleaner look <a class="yt-timestamp" data-t="00:45:07">[00:45:07]</a>.
*   **Column Colors**: Option to color columns based on the grouping property <a class="yt-timestamp" data-t="00:45:16">[00:45:16]</a>.
*   **Hide Empty Groups**: Conceal columns that have no entries <a class="yt-timestamp" data-t="00:45:42">[00:45:42]</a>.
*   **Visible Properties**: Display rollup and formula properties (e.g., "Number of Events," "Events Attended," "Attendance Percentage") for quick insights <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>. [[customizing_sales_dashboards_in_Notion|Customizing sales dashboards in Notion]] would follow a similar approach.

## Advanced Data Entry and Visualization Features

### Adding New Entries
*   **Page Templates**: Define a predefined set of properties to automatically apply when creating a new page in a database <a class="yt-timestamp" data-t="00:36:44">[00:36:44]</a>. This is useful for [[creating_content_on_notion_pages|creating content on Notion pages]] in a consistent manner.
*   **Buttons**: Create a button that, when clicked, performs an action like adding a new page (e.g., a new person or event) to a specified database with pre-set properties <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a>.
*   **Inline Addition**: Directly add new entries to a linked database view, even creating new related entries in another database (e.g., adding a new person directly from the event entry) <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>.

### Page Sections
Relation properties can be displayed as "page sections" within an individual page <a class="yt-timestamp" data-t="00:56:09">[00:56:09]</a>. This docks the related database directly into the page, allowing users to see and interact with all associated information (e.g., all events for a specific person) without navigating away <a class="yt-timestamp" data-t="00:56:14">[00:56:14]</a>. This feature is particularly useful for [[integrating_databases_with_templates_in_Notion|integrating databases with templates in Notion]] and for the [[presentation_of_income_tracking_data_in_Notion|presentation of income tracking data in Notion]].