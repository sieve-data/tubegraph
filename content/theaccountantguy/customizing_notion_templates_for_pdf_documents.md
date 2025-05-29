---
title: Customizing Notion Templates for PDF Documents
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This article details how to [[creating_and_using_notion_templates_for_pdfs | create and use Notion templates]] with a Notion database to [[using_notion_templates_for_pdf_generation | generate PDF documents]] like purchase orders using PDF output.com.

## Getting Started with PDF Output.com

To begin generating PDF documents from Notion, you need to log in to PDF output.com <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The interface will display options for connection name, Notion database, and Notion template <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

On the right sidebar, click on "Templates" to access a list of predefined templates <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. These include invoices, payment receipts, and purchase orders <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. You can search for a specific template using the search icon <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. To add a desired template to PDF output, click the "Download" link next to it <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This opens a new page, for example, the purchase order PDF generator page, which contains both a database and a template <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Understanding Notion Templates and Databases

A Notion template, such as a purchase order, defines the structure and layout of the document <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Key elements like the purchase order number, date, supplier, buyer, and item description are defined within it <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

For [[personalizing_templates_with_notion_data | personalizing templates with Notion data]], specific elements within the template are designated as placeholders <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. These placeholders are enclosed in curly braces, e.g., `{{purchase order number}}`, `{{date}}`, `{{supplier name}}`, `{{buyer name}}` <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

A Notion database is used to supply the data for these placeholders <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. The database contains columns like "Supplier Name," "Buyer Name," "Date," and "Purchase Order Number" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Each row in the database represents a unique record for which a PDF document will be generated <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The values from these database columns will replace the corresponding placeholder text in the template <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

Essentially, you need a [[creating_and_using_templates_for_pdf_generation_in_notion | Notion template]] and a Notion database whose column names match the template's placeholder names <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

## Customizing Notion Templates for PDF Generation

All elements within the Notion template and database are [[customizing_notion_templates | customizable]] to fit your specific requirements <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. You can add, delete, or modify any values <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### Customization Rules:
*   **Placeholder Format:** Ensure that all values intended for replacement are placed inside curly braces (e.g., `{{PlaceholderName}}`) <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **Exact Matching:** The name of the database column must exactly match the placeholder text within the curly braces <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. Avoid adding extra commas or spaces, as this is how the linking between the database and template is established <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Mismatches can be manually corrected in a later step <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

## Connecting Notion to PDF Output

1.  **Duplicate the Template:** On the PDF generator page (e.g., Purchase Order PDF Generator), click "Duplicate" or "Start with this template" <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
2.  **Select Notion Workspace:** Choose your Notion workspace where you want to add the page <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. This duplicates the template and database into your Notion account <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
3.  **Go to PDF Output Settings:** Return to PDF output.com and navigate to the "Settings" section <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
4.  **Select Page Format:** You can select your desired page format for the PDF document <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
5.  **Add Templates:** Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
6.  **Connect Workspace and Pages:** Select your Notion workspace from the dropdown <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>, then click "Select Pages" <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Choose the specific page (e.g., "Purchase Order PDF Generator") that was duplicated to your workspace <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
7.  **Allow Access:** Click "Allow access" to connect the Notion page with PDF output <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. After successful authentication, you will be redirected back to PDF output <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## Mapping Database Fields to Template Placeholders

Once connected, refresh PDF output to load all database and template elements <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

1.  **Select Database and Template:** From the dropdowns, select the "Purchase Order Database" and the "Template page" (e.g., "Purchase Order PDF Generator Template") <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. Give your connection a name <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a> and click "Next" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
2.  **Automatic Matching:** PDF output will automatically match most database properties (on the left) with their corresponding template elements (on the right) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
3.  **Manual Mapping of Unmatched Properties:** If some elements remain unmatched (e.g., due to a slight naming discrepancy like "Total Amount" vs. "TotalAmount"), you can filter for "unmapped properties" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. Click on the unmatched Notion property and search for the corresponding template element to link them <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
4.  **Verify Mapping:** Ensure all elements are correctly displayed and mapped <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. Sorting and searching options are available to help manage the mapping <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

## Generating and Downloading PDFs

1.  **Export:** Click "Export" to begin the PDF generation process <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
2.  **PDF Status Column:** During export, a "PDF status" column will automatically be added to your Notion database <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. When a PDF document has been generated for a specific row, its checkbox in this column will be ticked <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. If you need to regenerate a page, ensure this checkbox is unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
3.  **Preview and Download:** Once export is successful, you can click "Preview Sample" to view a generated PDF <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. This allows you to verify that all database values have correctly replaced the template placeholders <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. Finally, click "Download all documents" to save the generated PDFs to your system <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

## Additional Features of PDF Output

*   **Connections:** The "Connections" tab stores your previous PDF generation setups, allowing you to quickly regenerate documents without re-entering database and page information <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Upgrade:** Free plan generated PDFs will have a watermark <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Upgrading to a paid plan removes the watermark <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Feedback:** If you encounter issues, the "Feedback" option allows you to send detailed reports <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Help:** The "Help" section provides a complete demonstration video for setup and troubleshooting <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

For further assistance or specific PDF document solutions, you can reach out via email <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.