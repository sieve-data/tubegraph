---
title: Connecting Notion database and templates to PDF output
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This guide explains how to generate PDF documents, such as purchase orders, using a Notion database and a Notion template in conjunction with the PDF output.com service <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Initial Setup with PDF Output

To begin, you need to log in to PDFoutput.com <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The interface will display options for `Connection Name`, `Notion Database`, and `Notion Template` <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

### Finding and Selecting Templates

1.  Click on "Templates" in the sidebar to view a list of predefined templates <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
2.  You can find templates for invoices, payment receipts, and purchase orders <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
3.  Use the search icon to quickly locate a specific template by typing in keywords <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
4.  Once you've identified the desired template, click the "Download" link next to it <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This will open a new page containing both the database and template for the chosen document, such as a purchase order PDF generator page <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Understanding the Notion Template and Database Structure

Before [[connecting_notion_templates_with_pdf_output | connecting Notion templates with PDF output]], it's important to understand their structure.

*   **Template**: A template, like a purchase order, defines the layout and fixed text <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Dynamic elements, such as `purchase order number`, `date`, `supplier name`, and `buyer name`, are enclosed within curly braces `{}` <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. These curly braces act as placeholders for data from your Notion database <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Database**: The Notion database contains the actual data that will replace the placeholders in the template <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. It should have columns that exactly match the names of the placeholders in the template (e.g., `supplier name`, `buyer name`, `date`, `purchase order number`) <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Each row in the database represents a distinct document to be generated <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

> [!NOTE]
> All elements in the template and database are customizable <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. When customizing, ensure that:
> *   All values to be replaced are within curly braces in the template <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
> *   The name of the database column exactly matches the placeholder name in the template, avoiding extra commas or spaces <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. Mismatches can be resolved in the mapping step <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

## Duplicating the Notion Template

To [[setting_up_notion_database_for_pdf_document_templates | set up your Notion database for PDF document templates]], you must first duplicate the provided PDF generator page to your Notion workspace:

1.  On the PDF generator page, locate and click the "Duplicate" option at the top <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. If the template is already published, you might see "Start with this template" instead <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
2.  Select your desired Notion workspace to duplicate the page into <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
3.  Click "Add to Private" (or your specific workspace name) <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This will add the `Purchase Order PDF Generator` page, including its database and template, to your Notion workspace <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## [[connecting_and_setting_up_pdf_output_with_notion | Connecting and Setting Up PDF Output with Notion]]

Once the template is duplicated in Notion, return to PDF Output to establish the connection:

1.  Go to the "Settings" section in PDF Output <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
2.  Select your desired page format for the PDF output (e.g., A4, Letter) <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
3.  Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
4.  A new window will open, prompting you to connect your Notion workspace <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Select the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
5.  Click "Select Pages" <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. This will display all templates within that workspace <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
6.  Choose the `Purchase Order PDF Generator` page that you duplicated <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
7.  Click "Allow Access" to connect this Notion page with PDF Output <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. The authentication process will redirect you back to PDF Output upon success <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## Mapping Database Fields to Template Placeholders

After authentication, PDF Output will load the database and template elements for mapping, which is crucial for [[using_notion_database_and_templates_for_pdf_generation | using Notion database and templates for PDF generation]].

1.  Once redirected, refresh the PDF Output page if necessary <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
2.  From the drop-down menus, select the `Purchase Order Database` for the Notion database and the specific `template page` (e.g., `Template`) from the Notion template options <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
3.  Give your connection a name, like "Purchase Order" <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
4.  Click "Next" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. PDF Output will automatically attempt to match the Notion database properties (on the left) with the template elements (on the right) <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
5.  **Troubleshooting Unmapped Properties**:
    *   If any elements remain unmapped, it's usually due to a mismatch in naming (e.g., a space in the database column name vs. no space in the template placeholder) <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
    *   Click the "Filter unmapped properties" option to quickly identify any unmatched items <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
    *   Manually select the corresponding database property for the unmapped template element from the drop-down list <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
    *   Confirm all elements are correctly matched <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

## Generating and Exporting PDFs

Once all properties are mapped, you are ready for [[using_notion_templates_and_databases_for_pdf_creation | using Notion templates and databases for PDF creation]].

1.  Click "Export" <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
2.  In your Notion database, a new `PDF Status` column will automatically be added <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. This column will be ticked once a PDF document for that row has been generated <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. If you need to regenerate a PDF for a specific row, ensure this checkbox is unticked <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
3.  Upon successful export, you can click "Preview Sample" to view a generated PDF, verifying that all data from the database has correctly replaced the placeholders in the template <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
4.  Click "Download All Documents" to receive a zip file containing all generated PDFs based on the rows in your Notion database <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. Each document will correspond to a row of data, e.g., "Purchase Order Number Two", "Purchase Order Number One", "Purchase Order Number Three" <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

## Additional Features

*   **Connections**: The "Connections" tab stores previously created connections, allowing you to quickly regenerate documents without re-filling database and page details <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Upgrade**: Free plans will generate PDFs with a watermark <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Upgrading to a paid plan removes the watermark <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Settings**: Beyond connecting templates, the "Settings" section allows you to define your default page format for PDFs <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Feedback**: If you encounter any issues, use the "Feedback" option to report them directly <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   **Help**: The "Help" section provides setup videos and troubleshooting assistance <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

For further assistance or specific PDF document solutions, you can reach out via email to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.