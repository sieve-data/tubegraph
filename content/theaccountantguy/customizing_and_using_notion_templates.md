---
title: Customizing and Using Notion Templates
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

This article explains how to generate professional PDF documents, such as invoices, in bulk using Notion templates and databases, with the help of PDFoutput.com. The process involves leveraging Notion's flexible structure for data management and template design, then using a dedicated tool to automate PDF creation.

## Understanding the Notion Template and Database <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>

A core concept in this process is the "Professional Invoice Template" within Notion <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This template defines the layout and content of the PDF document. Key elements of the template are enclosed in curly braces, such as `{client name}`, `{client company}`, and `{client address}` <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. These elements act as placeholders that will be dynamically replaced with corresponding data from a Notion database <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

A Notion database is set up with properties that mirror the names of the placeholders in the template (e.g., "client name," "client company," "client address") <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This ensures a seamless mapping process when generating PDFs. For every element in the database, there is a corresponding element in the template placed inside curly braces <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## Generating PDFs in Bulk with PDFoutput.com

The software used to automate the PDF generation from Notion templates and databases is PDFoutput.com <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Step 1: Logging In and Initial Setup <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>

1.  Navigate to PDFoutput.com and log in <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
2.  Upon logging in, you'll see a "connection details" screen where you need to connect your Notion database and template <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

### Step 2: Duplicating Templates and Databases to Your Notion Workspace <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>

Before connecting, you need to copy the desired template and database to your own Notion workspace.
1.  On PDFoutput.com, click on "Templates" to view a list of pre-added templates <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
2.  Search for the specific template, such as "invoice" to find the "Professional Invoices" template <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
3.  Each template listed will have a "database link" and a "template link" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Click on both to open them in new tabs <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
4.  In the opened Notion pages for the template and the database, click the "Duplicate" option, usually found in the top right corner <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
5.  Select your Notion workspace (e.g., "the accountant guy workspace") to duplicate the template and database into <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This ensures they are available in your personal Notion environment <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### Step 3: Connecting Your Notion Database and Template <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>

1.  Back on PDFoutput.com, click "Add database" or "Add template" <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
2.  Select the Notion workspace where you duplicated the files <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
3.  Choose both the duplicated database (e.g., "professional invoice database") and template (e.g., "professional invoice template") <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
4.  Click "Allow access" <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. PDFoutput.com will then load these into its portal <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
5.  Optionally, define a connection name (e.g., "invoice template") <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
6.  Click "Next" <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

### Step 4: Mapping Database Properties to Template Elements <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>

PDFoutput.com will automatically display database properties on the left and attempt to map them to corresponding template elements <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

*   **Automatic Mapping**: If the names of the database properties (e.g., "Invoice Number," "Date") exactly match the names inside the curly braces in the template (e.g., `{invoice number}`, `{date}`), the mapping will occur automatically <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Manual Mapping**: If names differ, an element might appear with a gray icon <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Click on it and search for the correct database property to map it manually <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

### Step 5: Generating and Downloading PDFs <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>

1.  Once all elements are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
2.  The software will generate a PDF document for each row in your Notion database <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
3.  After successful export, you can:
    *   "Preview sample" to view one of the generated PDFs (e.g., an invoice for John Doe) <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
    *   "Download all" to download all generated PDF documents <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The downloaded files will be individual PDFs for each entry, such as for John Doe, Jane Smith, and AC Incorporation <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

## [[Customizing templates and databases in Notion | Customization]] and Best Practices

### Template Customization <a class="yt-timestamp" data-t="07:28:44">[07:28:44]</a>
The Notion template is entirely [[customizing_templates_in_notion | customizable]] to fit your specific needs <a class="yt-timestamp" data-t="07:30:30">[07:30:30]</a>.
*   **Placeholder Naming**: Ensure that any data you want to pull from the database into the template is enclosed in curly braces (e.g., `{My Custom Field}`) <a class="yt-timestamp" data-t="07:35:05">[07:35:05]</a>.
*   **Consistent Naming**: For automatic mapping during PDF generation, the name inside the curly braces in the template *must exactly match* the property name in your Notion database <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>. If names don't match, you'll need to manually map them during the connection process <a class="yt-timestamp" data-t="07:46:58">[07:46:58]</a>.

### Managing Connections and Settings

*   **Connections**: The "Connections" sidebar option shows all previously used connections. You can reuse a connection to quickly generate PDFs without redefining the template and database every time <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>.
*   **Templates**: The "Templates" section in PDFoutput.com lists various pre-made templates for different requirements <a class="yt-timestamp" data-t="08:46:00">[08:46:00]</a>.
*   **Upgrade**: The "Upgrade" section allows you to upgrade your subscription. The free plan includes a "Made with PDF output" watermark, which is removed on paid tiers <a class="yt-timestamp" data-t="09:00:59">[09:00:59]</a>.
*   **Settings**: In "Settings," you can define the page format (default is A4 size) and add more databases and templates <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>.
*   **Relational Properties**: If your Notion database uses relational properties (meaning it's connected to another database), ensure you also allow access to those linked databases when setting up your connection in PDFoutput.com <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.

### Custom Templates and Support

For using custom templates and databases not found in PDFoutput.com's pre-added list, consult the "Help" section <a class="yt-timestamp" data-t="10:10:00">[10:10:00]</a>. For any feedback or queries, use the "Feedback" option or contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="09:59:00">[09:59:00]</a>.