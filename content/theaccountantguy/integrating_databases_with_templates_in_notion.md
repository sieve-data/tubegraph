---
title: Integrating databases with templates in Notion
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

This article explains how to integrate Notion databases with templates to generate PDF documents in bulk using a tool called PDF Output. This process leverages placeholder fields in a template that are dynamically filled with data from a Notion database.

## Template and Database Structure

To facilitate bulk document generation, both the Notion template and database follow a specific structure:

### Template Design
A template, such as a purchase order, includes specific fields enclosed in curly braces, like `{purchase order number}`, `{date field}`, `{supplier name}`, and `{buyer name}` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. These curly-braced items serve as placeholders that will be automatically replaced with corresponding data from a database when the PDF document is generated <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

### Database Design
The Notion database must contain columns (properties) with names that exactly match the placeholder names used in the template (e.g., "Purchase Order Number", "Date Field", "Supplier Name", "Buyer Name") <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Each row in this database represents a unique record, and a PDF document will be generated for each row using the specified template <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Bulk PDF Generation with PDF Output

The PDF Output platform enables users to [[connecting_a_database_in_notion | connect Notion databases]] and templates to generate multiple PDF documents simultaneously.

### Steps to Generate PDFs:

1.  **Log in to PDF Output** <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. The interface will prompt you to [[connecting_a_database_in_notion | connect a Notion database]] and a Notion template <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
2.  **Access Predefined Templates**: Navigate to the "template" section in the sidebar navigation <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. You can search for specific templates, such as "purchase order" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
3.  **Duplicate Templates to Notion**: Click on the provided database and template links <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Use the "Start with this template" option to duplicate them into your personal Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. When prompted for duplication, select your desired workspace and click "Add to Private" <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
4.  **[[connecting_a_database_in_notion | Connect Notion Assets to PDF Output]]**:
    *   Return to the PDF Output interface and click on "click here to add database" or "click here to add template" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    *   Grant permissions by selecting your Notion workspace and then choosing the specific duplicated database and template <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>, <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Click "Allow Access" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Once authorized, the connected database and template will appear <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. If they don't appear immediately, click the refresh button <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
5.  **Map Template Fields to Database Properties**:
    *   Provide a name for this connection (e.g., "Purchase Order") <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
    *   The platform will then load the database elements (properties) and template elements (curly-braced placeholders) <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   If the naming conventions are identical between the template placeholders and database properties, the mapping will occur automatically <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>, <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Otherwise, manual mapping is required, where you select the corresponding database property for each template field <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
6.  **Create and Download PDFs**:
    *   Click "Create PDF" <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. The system will process all records in the database to generate individual PDF documents <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    *   After processing, you can "Preview Sample" to view one of the generated files <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>, <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
    *   Click "Download All" to download all the generated PDF documents in a single go <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Customization and Reusability

### [[customizing_templates_and_databases_in_notion | Customizing Templates]]
The duplicated template is fully customizable <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Any edits or modifications can be made, but ensure that any data intended to be populated from the database remains within curly braces and adheres to the exact naming convention used in the database properties <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>, <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Managing Connections
Once a database and template pair is connected, it is saved as a "connection" <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This means you don't need to re-select the database and template every time you want to generate documents <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. Saved connections can be accessed from the "Connections" section <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

### Page Format
The default page format for PDF output is A4 <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

### Handling Relational Properties
If your database uses any relational properties, ensure you grant access to the linked databases during the connection process in PDF Output <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This ensures all relevant elements are correctly reflected in the generated PDF <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.