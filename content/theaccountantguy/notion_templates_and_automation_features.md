---
title: Notion templates and automation features
videoId: h47T7sRTmg0
---

From: [[theaccountantguy]] <br/> 

Notion provides robust features for organizing information and automating workflows, particularly useful for managing personal relationships and events. This article explores how to leverage [[creating_and_using_notion_templates | Notion templates]] and its automation capabilities to create a comprehensive relationship tracker and event summary dashboard <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Getting Started with Notion

When setting up a Notion page, users can customize its appearance and behavior:
*   **Page Width**: Options include "small text format" to reduce text size and "full width" to expand the page view, which is often preferred for better presentation <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **New Page Creation**: A blank page can be created from scratch to build a dashboard <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Naming and Visuals**: Pages can be named (e.g., "Relationship Tracker"), include dividers for clean presentation, and feature custom icons and cover images for visual appeal <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

## Building the Database Structure

The core of a Notion dashboard is its interconnected databases <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. This relationship tracker uses two primary databases:

### Person Database
This database stores information about individuals and their relationships <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Name**: Records the name of the person (e.g., Susan, Harry, Sarah) <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **Relation**: A "select" property (formerly "tags") indicating the relationship type (e.g., sister, friend, colleague) <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Images**: An "image" property can be added to include photos for each person, enhancing the visual appeal of gallery views <a class="yt-timestamp" data-t="00:33:14">[00:33:14]</a>.

### Event Database
This database holds details about various events users need to track <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   **Event Name**: The name of the event (e.g., Susan's birthday, Harry's marriage, Sarah's graduation) <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   **Date**: A "date" property to schedule when the event is supposed to happen, with an option to include time <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
*   **Attendance**: A "checkbox" property to signify whether the event has been attended <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
*   **Event Type**: An optional "select" property to categorize events (e.g., birthday, marriage, graduation) <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
*   **Priority**: A "select" property to set the importance of an event (e.g., low, medium, high) <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>.

### Linking Databases with Relations
A crucial Notion feature is the "relation" property, which creates a link between two databases <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. In this setup, the Event Database is linked to the Person Database, allowing users to associate specific events with individuals <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. When an event is added, selecting a person from the linked Person Database automatically updates that person's entry with the associated event <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

## Summarizing and Automating Information

Notion's advanced properties enable powerful data summarization and automation.

### Rollup Property
The "rollup" property retrieves information from a linked database <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
*   **Counting Events**: Used in the Person Database to count the total number of events associated with each person from the Event Database, using the "count values" calculation <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.
*   **Counting Attended Events**: Configured to count only the checked "attendance" properties in the Event Database, showing how many events for a person have been attended <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>.

### Formula Property
Formulas allow for dynamic calculations and styled text presentations.
*   **Dynamic Event Count Display**: A formula uses the "number of events (rollup)" property to display "Number of Events: X Event(s)", applying conditional logic to show "Event" for one event and "Events" for multiple events <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>. It also styles the text with bolding and color <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.
*   **Attendance Percentage**: Calculates the percentage of attended events by dividing "events attended (rollup)" by "number of events (rollup)" <a class="yt-timestamp" data-t="00:27:54">[00:27:54]</a>. This can be displayed as a progress bar or ring for visual representation <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a>.

## Dashboard Views and User Interaction

The power of Notion lies in its diverse views and interactive elements, enhancing [[overview_of_notion_tools | Notion's tools]] for data visualization.

### Linked Database Views
Databases can be linked and displayed in various formats on the main dashboard:
*   **Gallery View**: Displays people with their images and relationships, offering a compact "card size" option <a class="yt-timestamp" data-t="00:30:28">[00:30:28]</a>.
*   **Calendar View**: Visualizes events on a monthly or weekly calendar, displaying event type, associated person, attendance status, and priority <a class="yt-timestamp" data-t="00:40:42">[00:40:42]</a>.
*   **Board View (Kanban)**: Summarizes events, grouped by relationship or other properties, showing rollup and formula properties like event counts and attendance percentages <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a>. Columns can be colored and empty groups hidden for a cleaner look <a class="yt-timestamp" data-t="00:45:16">[00:45:16]</a>.

### Automation Buttons
Notion's "button" feature allows for direct automation of tasks <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a>.
*   **Add Event Button**: A button can be configured to automatically add a new page (event) to the Event Database, pre-filling properties like "event name" and "date" (e.g., today's date) <a class="yt-timestamp" data-t="00:48:33">[00:48:33]</a>. This streamlines the process of adding new entries.

### In-Page Editing and Dynamic Linking
*   **Adding New People**: Users can add new people directly from the linked events database. Typing a new name in the "person" relation property will create a new entry in the Person Database, demonstrating Notion's dynamic linking capabilities <a class="yt-timestamp" data-t="00:52:12">[00:52:12]</a>.
*   **Side Peak View**: When interacting with database entries, the "side peak" view allows properties to open on the right side of the window, keeping the main dashboard visible <a class="yt-timestamp" data-t="00:32:09">[00:32:09]</a>.

### Page Sections for Related Information
Within a person's page, related event information can be displayed using the "show as page section" option for relation properties <a class="yt-timestamp" data-t="00:56:12">[00:56:12]</a>. This docks the entire property underneath other properties, offering a quick glance at all associated events, their dates, priorities, and attendance status for that specific person <a class="yt-timestamp" data-t="00:56:16">[00:56:16]</a>.

## Template Availability
This specific relationship tracker template is available for download on Gumroad <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.