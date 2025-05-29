---
title: Using Notion databases for event management
videoId: h47T7sRTmg0
---

From: [[theaccountantguy]] <br/> 

A Notion relationship tracker can be built to help users keep track of events associated with people in their lives, such as family members, friends, or colleagues <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This dashboard helps users schedule events in advance to avoid missing important occasions <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Key Information Tracked <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>

The tracker organizes several types of information:
*   **People:** Individuals connected in one's life.
*   **Relationship Categories:** Defines the relationship (e.g., family, friend, colleague).
*   **Events:** Specific occasions like marriages, birthdays, or functions.
*   **Event Summary:** A consolidated view of how many events are outlined for each person and how many have been attended <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **Monthly View:** Shows all events in a calendar format <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Building the Dashboard from Scratch

The entire dashboard is a collection of different databases holding information, which are then linked to provide a summarized view <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### Initial Page Setup

1.  **New Page Creation:** Start by [[creating_a_database_in_Notion | creating a new page]] in Notion <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
2.  **Page Title:** Name the page "Relationship Tracker" <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
3.  **Divider:** Add a divider for clean presentation by typing `/divider` <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
4.  **Icon and Cover:** Add an icon (e.g., a user icon) and a cover image for visual appeal <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
5.  **Page Width:** Set the page to "Full Width" for better presentation <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### Database Creation

The core of the tracker involves [[creating_and_using_databases_in_Notion | creating and using databases in Notion]] and [[setting_up_databases_and_relationships_in_Notion | setting up relationships]] between them. It is recommended to create a dedicated sub-page for all databases to keep them organized <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

#### 1. Person Database

This database stores information about the people connected in your life <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   **Creation:** Type `/database` and select "Inline" to create a new database <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   **Name:** Rename it "Person Database" <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
*   **Properties:**
    *   **Name:** Default "Name" property (e.g., Susan, Harry, Sarah) <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
    *   **Relation:** A "Select" property to categorize relationships (e.g., "Sister," "Friend," "Colleague") <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
    *   **Image:** A "Files & Media" property to upload images for each person <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>.

#### 2. Events Detail Database

This database holds all the specific event details <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   **Creation:** Type `/database` and select "Inline" <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **Name:** Rename it "Events Details" <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Properties:**
    *   **Event Name:** Default "Name" property for the event title (e.g., "Susan's Birthday") <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
    *   **Date:** A "Date" property to specify when the event occurs <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
    *   **Attendance:** A "Checkbox" property to mark if an event has been attended <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.
    *   **Event Type:** A "Select" property for the type of event (e.g., "Birthday," "Marriage," "Graduation") <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.
    *   **Priority:** A "Select" property to set the priority (e.g., "Low," "Medium," "High") <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>.
    *   **Person (Relation Property):** A "Relation" property to link to the "Person Database." This allows associating events with specific people <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. When creating this relation, ensure to "Show on other database" and name it "Event Detail" on the Person Database side <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.

### Event Summary Features

To create an event summary that shows how many events are outlined and how many are attended for each person:

1.  **Number of Events (Rollup Property):**
    *   Add a "Rollup" property to the Person Database <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
    *   Configure it to derive information from the "Events Detail" relation <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
    *   Select the "Event Name" property from the Events Detail database <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
    *   Under "Calculate," choose "Count values" to count the total events for each person <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.

2.  **Events Attended (Rollup Property):**
    *   Duplicate the "Number of Events" rollup property <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>.
    *   Configure it to derive from the "Events Detail" relation <a class="yt-timestamp" data-t="00:25:11">[00:25:11]</a>.
    *   Select the "Attendance" (checkbox) property from the Events Detail database <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.
    *   Under "Calculate," choose "Count checked" to count only the attended events <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.

3.  **Attendance Percentage (Formula Property):**
    *   Add a "Formula" property to the Person Database <a class="yt-timestamp" data-t="00:27:43">[00:27:43]</a>.
    *   The formula divides "Events Attended" by "Number of Events" <a class="yt-timestamp" data-t="00:27:54">[00:27:54]</a>.
    *   Format the number as a "Percentage" <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.
    *   For visual representation, change the "Show as" option to "Bar" <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a>.

## Linking Databases to the Main Dashboard

To display the information on the main dashboard:

1.  **Linked View of Person Database:**
    *   On the main "Relationship Tracker" page, type `/linked` and select "Linked view of database" <a class="yt-timestamp" data-t="00:29:52">[00:29:52]</a>.
    *   Choose the "Person Database" <a class="yt-timestamp" data-t="00:30:17">[00:30:17]</a>.
    *   Change the layout to "Gallery view" <a class="yt-timestamp" data-t="00:30:28">[00:30:28]</a>.
    *   Set the card size to "Small" <a class="yt-timestamp" data-t="00:30:48">[00:30:48]</a>.
    *   Under "Layout," set "Card preview" to "Image" to display the person's image <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>.
    *   Enable relevant properties to display on the cards, such as "Relation" <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>.
    *   Group the cards by "Relation" to organize by relationship type <a class="yt-timestamp" data-t="00:31:24">[00:31:24]</a>.
    *   Configure page opening as "Side Peak" for convenience <a class="yt-timestamp" data-t="00:32:09">[00:32:09]</a>.

2.  **Linked View of Events Detail Database (Calendar View):**
    *   Add another linked view of the database <a class="yt-timestamp" data-t="00:40:22">[00:40:22]</a>.
    *   Choose the "Events Details" database <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>.
    *   Change the layout to "Calendar view" <a class="yt-timestamp" data-t="00:40:53">[00:40:53]</a>.
    *   Enable properties to display on the calendar entries, such as "Event Type," "Person," "Attendance," and "Priority" <a class="yt-timestamp" data-t="00:41:03">[00:41:03]</a>.
    *   The calendar can be displayed in "Monthly" or "Weekly" format <a class="yt-timestamp" data-t="00:43:12">[00:43:12]</a>.

3.  **Event Summary (Board View):**
    *   Add another linked view of the database <a class="yt-timestamp" data-t="00:44:19">[00:44:19]</a>.
    *   Choose the "Person Database" <a class="yt-timestamp" data-t="00:44:19">[00:44:19]</a>.
    *   Change the layout to "Board view" <a class="yt-timestamp" data-t="00:44:48">[00:44:48]</a>.
    *   Set card size to "Medium" <a class="yt-timestamp" data-t="00:45:09">[00:45:09]</a>.
    *   Ensure grouping is set by "Relation" <a class="yt-timestamp" data-t="00:45:24">[00:45:24]</a>.
    *   Hide empty columns if no people are in a specific relation group <a class="yt-timestamp" data-t="00:45:34">[00:45:34]</a>.
    *   Enable the "Number of Events," "Events Attended," and "Attendance Percentage" properties to be visible on the cards <a class="yt-timestamp" data-t="00:46:05">[00:46:05]</a>.

## Adding New Entries and Customization

*   **Add Event Button:** Create a button (`/button`) that adds a new page to the "Events Details" database <a class="yt-timestamp" data-t="00:48:03">[00:48:03]</a>. Configure it to auto-fill the event name and set the date to "Today" <a class="yt-timestamp" data-t="00:48:49">[00:48:49]</a>.
*   **Add Person Directly:** From the "Events Details" database, when linking an event to a person, you can type a new name, and Notion will offer to "Add new page" to the Person database, instantly creating a new entry there <a class="yt-timestamp" data-t="00:52:12">[00:52:12]</a>.
*   **Database Layouts:** Different views (Table, Gallery, Board, Calendar) and their properties can be customized for optimal visibility and organization <a class="yt-timestamp" data-t="00:40:42">[00:40:42]</a>.
*   **Page Sections for Relations:** For a specific person's page, a relation property can be shown as a "Page section." This docks the related events (or other linked data) underneath the person's properties, providing a quick glance at all associated events for that individual <a class="yt-timestamp" data-t="00:56:09">[00:56:09]</a>.

This comprehensive setup allows for effective [[using_databases_in_Notion_for_expense_tracking | using databases in Notion for expense tracking]], [[using_databases_in_Notion_for_invoice_tracking | invoice tracking]], or other financial tracking, by applying similar principles of related databases and rollup/formula properties.