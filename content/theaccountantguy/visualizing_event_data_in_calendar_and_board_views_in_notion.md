---
title: Visualizing event data in calendar and board views in Notion
videoId: h47T7sRTmg0
---

From: [[theaccountantguy]] <br/> 

The Notion relationship tracker is a dashboard designed to help users keep track of events associated with people in their lives, such as family members, friends, or colleagues <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This tool allows users to schedule events in advance, ensuring important occasions like marriages, birthdays, or parties are not missed <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Dashboard Setup

To begin building the dashboard from scratch, start by creating a new page in Notion <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
Essential initial settings include:
*   **Full Width**: Enable the "full width" option for an expansive view by clicking the three dots on the right side of the page <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **Name**: Assign a name like "Relationship Tracker" <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **Divider**: Add a divider (`/divider`) for a clean presentation <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
*   **Icon and Cover**: Add an icon (e.g., a "user" icon) and a cover image to personalize the page <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

All underlying data for the dashboard is stored in separate databases linked together <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. It is recommended to create a dedicated sub-page named "Database" (`/database`) to house all these databases for organization <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

## Database Structures

### Person Database

This database stores information about individuals connected to the user <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Name**: The primary column for the person's name <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **Relation**: A multi-select property to define the relationship (e.g., sister, friend, colleague) <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Image**: An image property to add a visual representation of the person <a class="yt-timestamp" data-t="00:33:11">[00:33:11]</a>.

### Events Database

This database tracks all events associated with individuals <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   **Event Name**: The name of the event (e.g., "Susan's birthday") <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
*   **Date**: A date property to specify when the event is scheduled <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. This can also include time <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
*   **Attendance**: A checkbox property to mark if an event has been attended <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.
*   **Event Type**: A multi-select property for categorization (e.g., "birthday," "marriage," "graduation") <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.
*   **Priority**: A select property to set the urgency (e.g., "low," "medium," "high") <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>.

### Linking Databases

The `Person` and `Events` databases are connected using a `Relation` property <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. This link allows events to be associated with specific people and vice-versa <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

### Event Summary Calculations

Within the `Person` database, rollup and formula properties are used to summarize event data:
*   **Number of Events (Rollup)**: A rollup property that counts the total number of events associated with each person from the `Events` database <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>.
    *   `Relation`: Event details <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>
    *   `Property`: Event name <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>
    *   `Calculate`: Count values <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>
*   **Events Attended (Rollup)**: Another rollup property that counts only the events where the "Attendance" checkbox is ticked <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>.
    *   `Relation`: Event details <a class="yt-timestamp" data-t="00:25:14">[00:25:14]</a>
    *   `Property`: Attendance <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>
    *   `Calculate`: Count checked <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>
*   **Number of Events (Formula)**: A formula property that displays the "Number of Events" (rollup) with styled text (e.g., bold, blue, and dynamic "event" or "events" based on count) <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>.
*   **Events Attended (Formula)**: Similar to the above, this formula property displays the "Events Attended" (rollup) with styled text (e.g., bold, green, and dynamic "event" or "events") <a class="yt-timestamp" data-t="00:26:05">[00:26:05]</a>.
*   **Attendance Percentage (Formula)**: Calculates the percentage of attended events and displays it as a progress bar <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.
    *   Formula: `round((prop("Events Attended (Rollup)") / prop("Number of Events (Rollup)")) * 100) / 100` <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>
    *   Format: Number format set to "Percentage" and "Show as" set to "Bar" <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a>.

## Visualizing Data on the Main Dashboard

Once databases are set up, they are linked to the main dashboard to provide summarized views.

### People Overview (Gallery View)

The `Person` database is displayed as a linked database on the main dashboard in a gallery view <a class="yt-timestamp" data-t="00:30:29">[00:30:29]</a>.
*   **Card Size**: Can be set to "small" for a compact display <a class="yt-timestamp" data-t="00:30:48">[00:30:48]</a>.
*   **Properties Displayed**: Show the person's name and "Relation" property <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>.
*   **Card Preview**: Set the "Card Preview" to "Image" to display the person's added image on the card <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>.
*   **Side Peak**: When opening a person's card, configure it to open as a "side peak" for easier viewing and editing <a class="yt-timestamp" data-t="00:32:09">[00:32:09]</a>.

### Event Details (Calendar View)

The `Events` database is displayed as a linked database in a calendar format <a class="yt-timestamp" data-t="00:40:45">[00:40:45]</a>.
*   **Properties Displayed**: Configure which event properties are visible on the calendar entries, such as Event Type, Person, Attendance, and Priority <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a>.
*   **Monthly/Weekly View**: Switch between a monthly or weekly calendar view using the "Show calendar as" option in the layout settings <a class="yt-timestamp" data-t="00:43:05">[00:43:05]</a>.

### Event Summary (Board View)

The `Person` database is linked again to create an event summary in a board view <a class="yt-timestamp" data-t="00:44:48">[00:44:48]</a>.
*   **Grouping**: Group the board by the "Relation" property to categorize people by their relationship type <a class="yt-timestamp" data-t="00:45:24">[00:45:24]</a>.
*   **Hide Empty Groups**: Hide columns where no people are present for a cleaner view <a class="yt-timestamp" data-t="00:45:44">[00:45:44]</a>.
*   **Properties Displayed**: Display the "Number of Events," "Events Attended," and "Attendance Percentage" formulas for each person <a class="yt-timestamp" data-t="00:46:05">[00:46:05]</a>.

## Adding New Data

*   **Add Event Button**: A button can be configured to automatically add a new page (event) to the `Events` database with predefined properties, such as setting the date to "today" <a class="yt-timestamp" data-t="00:48:21">[00:48:21]</a>.
*   **Adding New Persons from Linked Databases**: When adding an event in the `Events` database, if a person's name is typed that doesn't exist in the `Person` database, Notion allows creating a new person property directly from that input <a class="yt-timestamp" data-t="00:52:15">[00:52:15]</a>. This new person will automatically appear in the `Person` database <a class="yt-timestamp" data-t="00:52:26">[00:52:26]</a>.

## Advanced Display Options

*   **Hide Vertical Lines**: In table views, vertical lines can be hidden for a cleaner aesthetic <a class="yt-timestamp" data-t="00:53:13">[00:53:13]</a>.
*   **Show as Page Section**: For `Relation` properties within a person's page, you can choose "Show as page section" <a class="yt-timestamp" data-t="00:56:12">[00:56:12]</a>. This embeds the related database view (e.g., all events associated with that person) directly within the person's page, allowing for a quick glance at their specific events and attendance status <a class="yt-timestamp" data-t="00:56:14">[00:56:14]</a>.

This comprehensive approach allows for detailed tracking and [[Using Notion to analyze financial data | analysis]] of events and relationships within Notion. While this article focuses on event tracking, similar database and visualization techniques can be applied to other areas, including [[Monthly and yearly financial overviews in Notion | monthly and yearly financial overviews]], [[Updating and viewing expenses overview in Notion | updating and viewing expenses]], [[Using Notion for budgeting | budgeting]], [[Creating a budget planner using Notion | budget planning]], [[Finance templates in Notion | finance templates]], [[Project tracking and prioritization in Notion | project tracking]], or [[Creating a training dashboard in Notion | training dashboards]].