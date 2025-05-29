---
title: Connecting Notion database and templates
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This article explains how to generate PDF documents, such as purchase orders, by [[notion_template_and_database_integration | integrating a Notion database with a Notion template]] using PDFoutput.com <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Getting Started with PDFoutput.com

1.  **Log in to PDFoutput.com**: Begin by logging into PDFoutput.com <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
2.  **Navigate to Templates**: On the right sidebar, click on "Templates" <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This will load a list of predefined templates for generating PDF documents, including invoices, payment receipts, and purchase orders <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
3.  **Select and Download a Template**: You can search for a specific template using the search icon <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. For a purchase order template, type "purchase" in the search bar <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Once found, click the "Download" link next to your desired template <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This will open a new page, typically a "PDF generator page," which includes a database and a template <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

### Understanding the Notion Template and Database

Before connecting, it's helpful to understand the components:

*   **Template**: The template defines the structure of your PDF document (e.g., purchase order, date, supplier, buyer, item description) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Placeholders**: Elements within the template that will be replaced by data from the database are enclosed in curly braces, such as `{purchase order number}`, `{date}`, `{supplier name}`, and `{buyer name}` <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Database**: The database contains the actual data (e.g., supplier names, buyer names, dates, purchase order numbers) in predefined fields <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. Each row of information in the database will generate a separate PDF document <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. The column values from the database will replace the placeholder text in the template <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

> [!INFO] Customization
> Both the template and the database are customizable <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. You can add, delete, or modify values as needed <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. Ensure that all values intended for replacement in the template are placed inside curly braces <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a> and that the database column names exactly match the template placeholder names (excluding curly braces), with no extra commas or spaces <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Connecting to Notion

1.  **Duplicate to Notion Workspace**: On the PDF generator page, look for the "Duplicate" option (or "Start with this template" if already published) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Click it to duplicate the page, including its embedded database and template, to your Notion workspace <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. Select your desired Notion workspace from the options <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
2.  **Go to PDFoutput.com Settings**: Return to PDFoutput.com and click on "Settings" <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
3.  **Connect Templates**: In settings, you can select the desired page format for your PDF <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. Then, click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
4.  **Select Notion Workspace and Page**: A new window will appear, listing your connected Notion workspaces <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Select the workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. Then, click "Select Pages" <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a> and choose the duplicated Notion page (e.g., "Purchase Order PDF Generator") <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
5.  **Allow Access**: Click "Allow Access" to connect this Notion page with PDFoutput.com <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. Wait for the authentication to be successful and for PDFoutput.com to redirect back to its page <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## Mapping Database Fields to Template Placeholders

1.  **Select Database and Template**: Once redirected and refreshed, PDFoutput.com will populate the "Notion Database" and "Notion Template" dropdowns <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. Select your Notion database (e.g., "Purchase Order Database") <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a> and the specific template page (e.g., "Purchase Order PDF Template") <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. Provide a connection name (e.g., "Purchase Order") <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a> and click "Next" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
2.  **Match Properties**: PDFoutput.com will automatically match most of the database properties (on the left) to the template elements (on the right) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
3.  **Handle Unmatched Properties**: If any elements remain unmatched (e.g., "Total Amount" due to a space mismatch in the name) <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>, click on the unmatched field and search for the corresponding field from the template side <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. A quick way to identify unmatched properties is to click the "Filter" option and select "Filter unmapped properties" <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
4.  **Confirm Mapping**: Ensure all Notion database properties are correctly mapped to their corresponding template elements <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. You can use search and sort options for easier management <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

## Generating and Downloading PDFs

1.  **Export**: Click "Export" to start generating the PDF documents <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
2.  **PDF Status Column**: In your Notion database, a "PDF Status" column will be automatically added <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. When a PDF document is generated for a row, this checkbox will be ticked <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. If you need to regenerate a PDF for a specific row, ensure this checkbox is unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
3.  **Preview and Download**: Once the export is successful, you can click "Preview Sample" to view a sample of the generated file <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. Then, click "Download all documents" to download a ZIP file containing all generated PDFs <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. Each PDF will correspond to a row in your Notion database, with all placeholder values correctly replaced <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

## Additional PDFoutput.com Features

*   **Connections**: Once a PDF document is generated, a connection is created and stored <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. This allows you to directly click on the connection to regenerate documents without re-filling database and page information <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   **Upgrade**: Free plans generate templates with a watermark <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Paid plans generate templates without a watermark <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Settings**: Beyond [[connecting_a_database_to_a_template_in_notion | connecting templates]], the settings allow you to define your preferred page format <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Feedback**: If you encounter any issues, you can submit feedback through a dedicated option <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   **Help**: The help section provides a complete demonstration video for setup and troubleshooting <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

For further assistance or custom PDF document solutions, you can reach out via email <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.