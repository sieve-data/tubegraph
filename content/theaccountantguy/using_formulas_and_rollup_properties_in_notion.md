---
title: Using formulas and rollup properties in Notion
videoId: h47T7sRTmg0
---

From: [[theaccountantguy]] <br/> 

Notion is a versatile workspace tool that allows users to create custom dashboards, such as a relationship tracker, to keep tabs on events and interactions with people in their lives, including family, friends, and colleagues <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. A key to building dynamic and informative dashboards in Notion is the effective use of databases, [[using_rollup_properties_in_notion | rollup properties]], and formulas <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

## Setting Up Your Notion Page and Databases

Before diving into formulas and rollups, it's beneficial to optimize your Notion page's view. Users can change the text size to a small text format <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a> or switch to a "full width" view for a broader presentation <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

To begin building a relationship tracker, you typically start by creating a new, blank page <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. This main page can be named "Relationship Tracker" <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a> and customized with an icon and a cover image <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

The core of a Notion dashboard lies in its interconnected databases <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. For a relationship tracker, you might create a "database" sub-page to house multiple databases <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
Essential databases include:
*   **Person Database**: Stores information about people, such as their name and relationship type (e.g., sister, friend, colleague) <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. Each person can have an icon assigned <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   **Events Database**: Holds details for all events, including the event name, date, event type (e.g., birthday, marriage, graduation), and a checkbox for attendance <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

The connection between these databases is established using a "Relation" property <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. This property links records in one database to records in another, allowing for complex data relationships <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. For instance, an event in the Events Database can be linked to a person in the Person Database <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.

## [[using_rollup_properties_in_notion | Using Rollup Properties]]

A [[using_rollup_properties_in_notion | rollup property]] is crucial for summarizing information from one database onto another, once they are linked by a relation <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.

### Counting Total Events
To count the total number of events associated with each person:
1.  In the Person Database, add a new property and select `Rollup` <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
2.  Configure the rollup:
    *   **Relation**: Select the "Event Details" relation (linking to the Events Database) <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
    *   **Property**: Choose "Event Name" from the Events Database <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
    *   **Calculate**: Select "Count values" <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.
This rollup property, named "Number of events" (e.g., "Number of events (rollup)"), will display the total number of events for each person <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.

### Counting Attended Events
To count events that have been attended:
1.  Duplicate the "Number of events (rollup)" property <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>.
2.  Rename it to "Events Attended (rollup)" <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.
3.  Configure the rollup:
    *   **Relation**: Keep "Event Details" <a class="yt-timestamp" data-t="00:25:14">[00:25:14]</a>.
    *   **Property**: Select "Attendance" (the checkbox property) <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.
    *   **Calculate**: Select "Count checked" to count only the events where the attendance checkbox is ticked <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.

## [[creating_and_saving_formulas_in_notion | Using Formulas in Notion]]

Formulas allow for dynamic calculation and display of data based on other properties.

### Styling Text and Conditional Display
A common use case is to display the rollup results with custom text and styling.
1.  Add a new property to the Person Database and select `Formula` as its type <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.
2.  To style text, use the `style()` function <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. For example, to make the number of events bold and blue, the formula would involve:
    ```notion
    if(prop("Number of events (rollup)") <= 1,
        style(format(prop("Number of events (rollup)")) + " Event", "b", "blue"),
        style(format(prop("Number of events (rollup)")) + " Events", "b", "blue")
    )
    ```
    This formula also demonstrates an `if` condition <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a> to display "Event" for a single event and "Events" for multiple events, ensuring grammatical correctness <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>.

### [[calculating_percentages_in_notion | Calculating Percentages]]
To calculate the attendance percentage for each person:
1.  Add another `Formula` property, named "Attendance Percentage" <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.
2.  The basic formula for percentage is: `(Events Attended / Number of Events) * 100` <a class="yt-timestamp" data-t="00:27:54">[00:27:54]</a>.
    *   `prop("Events Attended (rollup)") / prop("Number of events (rollup)") * 100` <a class="yt-timestamp" data-t="00:27:58">[00:27:58]</a>
3.  To format the output as a percentage with a progress bar:
    *   Click `Edit property` on the formula <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>.
    *   Change the number format to `Percentage` <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.
    *   Select `Bar` (or `Ring`) for the show as option and choose a color (e.g., blue) <a class="yt-timestamp" data-t="00:28:59">[00:28:59]</a>.
The `round()` function can be used to ensure the percentage is displayed correctly <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>. While not explicitly mentioned as [[using_excelstyle_formulas_in_notion | Excel-style formulas]], Notion's formula syntax shares similarities with spreadsheet functions <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.

## Displaying Data in the Main Dashboard

Once databases and properties are set up, they can be displayed on the main "Relationship Tracker" page using "Linked Database" views <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>.

### Person Summary (Gallery View)
1.  Add a `Linked view of database` and select the "Person Database" <a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a>.
2.  Change the layout to `Gallery` view <a class="yt-timestamp" data-t="00:30:28">[00:30:28]</a>.
3.  Adjust card size to "Small" <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>.
4.  In properties, ensure the "Relation" is visible <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>.
5.  To display images, add an `Image` property to the Person Database <a class="yt-timestamp" data-t="00:33:11">[00:33:11]</a>. In the gallery layout, set `Card preview` to `Image` (or `Page Cover`) <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>.

### Events Calendar (Calendar View)
1.  Add another `Linked view of database`, selecting the "Events Database" <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>.
2.  Change the layout to `Calendar` view <a class="yt-timestamp" data-t="00:40:53">[00:40:53]</a>.
3.  Enable properties to display on the calendar, such as event type, person, attendance, and priority <a class="yt-timestamp" data-t="00:41:03">[00:41:03]</a>.
4.  The calendar can be viewed in monthly or weekly format <a class="yt-timestamp" data-t="00:43:05">[00:43:05]</a>.

### Event Summary (Board View)
1.  Add a final `Linked view of database` using the "Person Database" again <a class="yt-timestamp" data-t="00:44:19">[00:44:19]</a>.
2.  Change the layout to `Board` view <a class="yt-timestamp" data-t="00:44:48">[00:44:48]</a>.
3.  Group the board by `Relation` <a class="yt-timestamp" data-t="00:45:24">[00:45:24]</a>.
4.  Enable the formula properties "Number of events", "Events Attended", and "Attendance Percentage" to show the summary <a class="yt-timestamp" data-t="00:46:05">[00:46:05]</a>.

## Streamlining Data Entry

### Add Event Button
A button can be added to quickly create new event entries <a class="yt-timestamp" data-t="00:48:12">[00:48:12]</a>.
1.  Insert a `Button` block <a class="yt-timestamp" data-t="00:48:03">[00:48:03]</a>.
2.  Configure it to `Add page to` the "Events Database" <a class="yt-timestamp" data-t="00:48:33">[00:48:33]</a>.
3.  Set default properties like `Event Name` as "Enter Event Name" and `Date` to `Today` <a class="yt-timestamp" data-t="00:48:49">[00:48:49]</a>.

### Adding New People Directly
New people can be added to the Person Database directly from the Event Details when linking an event to a person. If a person's name typed into the "Person" relation property doesn't exist, Notion offers to create a new page for that person in the linked database <a class="yt-timestamp" data-t="00:52:15">[00:52:15]</a>.

## Advanced Property Display

Relation properties (and some rollup properties) can be displayed as a "Page Section" within a Notion page <a class="yt-timestamp" data-t="00:56:09">[00:56:09]</a>. This means when you open a person's page, all associated events can be directly viewed and interacted with as a nested section within that person's page <a class="yt-timestamp" data-t="00:56:14">[00:56:14]</a>. This provides a quick glance at all relevant information tied to a specific individual <a class="yt-timestamp" data-t="00:57:19">[00:57:19]</a>.