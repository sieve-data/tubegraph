---
title: Exporting and downloading PDF documents
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool that allows users to generate PDF documents in bulk using a Notion page and a Notion database <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process involves using a predefined template where specific fields enclosed in curly braces are replaced with data from a Notion database <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Template and Database Setup

The process begins with a template, such as a purchase order template, containing placeholders for details like purchase order number, date, supplier, and buyer name, all enclosed in curly braces <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. These placeholders correspond to fields in a Notion database, which holds the actual values for each document to be generated <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. Each row in the database will correspond to a unique PDF document <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

For example, a purchase order template might have `{{purchase order number}}` which is then populated from a "Purchase Order Number" column in the Notion database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Duplicating Templates to Notion

To get started, users need to:
1.  Log in to PDF output.com <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
2.  Navigate to the "Template" section in the sidebar <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
3.  Search for a desired template, e.g., "purchase order" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
4.  Click on the provided database link and template link <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
5.  Use the "Start with this template" option to duplicate both the database and the template into your Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This ensures the template and database are added under your Notion pages <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## Connecting to PDF Output

After duplicating the templates, connect them to PDF Output:
1.  Click on "click here to add database" or "click here to add template" on the PDF Output screen <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  Select your Notion workspace and choose the duplicated database and template from the list of available pages <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
3.  Click "Allow access" to authorize the connection <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
4.  Once authorized, both the database and template will appear in PDF Output <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. A refresh button is available if they don't immediately show up <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. Users can select from multiple added databases and templates using dropdowns <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
5.  Name the connection, e.g., "Purchase Order," and click "Next" <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## Mapping Data Elements

The next step involves mapping database properties to template elements:
*   PDF Output automatically loads template elements (those in curly braces) and database properties <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   **Automatic Mapping**: If the naming convention in the template (e.g., `{{purchase order number}}`) exactly matches the Notion database property name ("Purchase Order Number"), mapping occurs automatically <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
*   **Manual Mapping**: If names don't match, elements will appear in gray. Users must manually click on the gray element and select the corresponding database property from a dropdown <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

## Generating and [[exporting_and_downloading_generated_pdf_documents | Downloading PDF Documents]]

Once mapping is complete:
1.  Click on "Create PDF" <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
2.  The tool will process all documents based on the rows in the Notion database <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
3.  After successful export, users can "Preview sample" to view one of the generated files <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
4.  To get all documents, click "Download all." This will download all generated PDF files <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. If downloading is missed, "Download PDF again" is an option <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

## Customization and Advanced Features

### Template Customization
The duplicated template can be customized, modified, or edited by the user. The crucial point is to ensure that any data intended to be replaced from the database remains inside curly braces and follows the exact same naming convention as the database properties <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Saved Connections
The "Connections" section on the right sidebar stores previously created connections. Clicking on a saved connection will automatically load the associated database and template in the first step of the generation process, eliminating the need to re-select them for future exports <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

### Upgrade Options
Free plan users will find a "Made with PDF Output Watermark" on exported documents <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. Upgrading to a paid subscription removes this watermark and any limits on PDF document generation <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

### Settings
The "Settings" section allows users to:
*   Set the default page format (e.g., A4) <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   Add more databases and templates beyond the initial setup <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

### Feedback and Help
*   **Feedback**: A feedback option is available to report difficulties or issues <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Help**: The help section includes a video demonstrating how to use a custom template from scratch, if users prefer not to use the predefined templates <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

### Relation Properties in Notion
If the Notion database uses "relation properties," it's essential to grant access to those related databases when initially selecting the database and template <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This ensures all related elements are correctly reflected in the generated PDF output <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

For further questions, contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.