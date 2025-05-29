---
title: Using Templates in Notion for PDF Generation
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This article outlines the process of [[creating_and_using_templates_for_pdf_generation_in_notion | generating PDF documents]] for purchase orders using a Notion database and a Notion template, leveraging the PDF output.com platform <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Getting Started with PDFoutput.com

To begin, you need to log in to PDF output.com <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The interface will display options for connection name, Notion database, and Notion template <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Accessing Predefined Templates

1.  From the sidebar on the right, click on "Templates" <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
2.  This section lists predefined templates for generating PDF documents, such as invoices, payment receipts, and purchase orders <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
3.  You can quickly search for a specific template using the search icon <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Sorting and filtering options are also available <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
4.  Click the "Download" link next to your desired template (e.g., Purchase Order) to add it to PDF output <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This action opens a new page for the selected template <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Understanding the Notion Template and Database

The template page you opened contains both a database and a template that will be connected to PDF output <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### The Template

*   The template (e.g., a purchase order template) includes elements like purchase order number, date, supplier, buyer, and item descriptions <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   Certain elements are enclosed in curly braces (e.g., `{purchase order number}`, `{date}`, `{supplier name}`, `{buyer name}`) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. These are placeholder texts that will be replaced by data from your Notion database <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### The Database

*   The accompanying database contains predefined fields such as supplier name, buyer name, date, and purchase order number <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   Each row in the database represents a set of information that will be used to generate a separate PDF document <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. The column values from the database will replace the corresponding placeholder texts in the template <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

## Duplicating the Template to Your Notion Workspace

1.  On the PDF generator page, locate the "Duplicate" option at the top <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. If the template is already published, you might see "Start with this template" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
2.  Clicking "Duplicate" will prompt you to select your Notion workspace where you want to add the page <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
3.  After selecting your workspace (e.g., "accountant guy") and clicking "Add to private," the purchase order PDF generator page will be added to your Notion workspace <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Connecting Notion to PDF output

1.  Return to PDF output.com and go to the "Settings" section <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
2.  Here, you can optionally select your desired page format for the PDF <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
3.  Click on "Click here to add templates" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
4.  A new window will appear, listing your connected Notion workspaces <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Select the workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
5.  Click "Select Pages" and choose the specific page (e.g., "Purchase Order PDF Generator") that contains your database and template <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
6.  Click "Allow access" to connect this page with PDF output <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
7.  Once authentication is successful, you will be redirected back to the PDF output page <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## Mapping Database Properties to Template Elements

After connecting, PDF output will load the database and template elements <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

*   Select the "Purchase Order database" from the dropdown <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   Then, select the specific "template page" from the other dropdown <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   Give your connection a name (e.g., "purchase order") and click "Next" <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

PDF output will automatically match most elements between your Notion database properties and the template elements <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

*   **Manual Matching:** If some elements remain unmatched (e.g., "Total Amount" due to a space mismatch in naming), you will need to map them manually <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   **Filter Unmapped Properties:** Use the "filter unmapped properties" option to quickly identify and address any missing connections <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
*   **Overview:** Notion properties (from the database) are shown on the left, and template elements are on the right <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. You can also search and sort elements <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

## Exporting and Generating PDFs

1.  Click on "Export" <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
2.  A "PDF status" column will be automatically added to your Notion database <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. When a PDF document is generated for a row, this column will be ticked <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
    *   To regenerate a PDF for a specific row, ensure this checkbox is unticked <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
3.  Once the export is successful, you can click "Preview sample" to view a sample of the generated PDF <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
4.  Finally, click "Download all documents" to save the generated PDFs to your output folder <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. Each row from your Notion database will have a corresponding PDF document <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

## Customization and Best Practices

*   Both the template and the database are fully [[customizing_notion_templates | customizable]] <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. You can add, delete, or modify values as needed <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   Ensure that all values intended for replacement in the template are enclosed within curly braces <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   It is crucial that the name of the database column exactly matches the name of the placeholder text within the curly braces in the template (e.g., no extra commas or spaces) to ensure proper linking <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## PDF Output Features

*   **Connections:** After generating a PDF, PDF output creates and stores a connection, allowing you to quickly regenerate documents without re-filling database and page information <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Upgrade:** Free plans will generate PDFs with watermarks. [[customizing_notion_templates | Paid plans]] remove these watermarks <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Settings:** Define your desired page format and manage connected templates <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Feedback:** Provides an option to report issues with connections or other functionalities <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   **Help:** Offers a complete demonstration video for setup and troubleshooting <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

For any further assistance or specific PDF document use cases, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.