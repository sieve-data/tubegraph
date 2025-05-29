---
title: Customizing purchase order templates in Notion
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This article explains how to generate Purchase Order (PO) PDF documents using a Notion database and a Notion template via PDF output.com <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The templates and databases used in this process are fully customizable to meet specific requirements <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

## Getting Started with PDF Output

To begin, log in to PDF output.com <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The interface displays options to connect a Notion database and a Notion template <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Accessing Predefined Templates

On the right sidebar of PDF output.com, click on "Templates" to load a list of predefined templates available for PDF generation <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Available templates include invoices, payment receipts, and purchase orders <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Users can search for a specific template using the search icon <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

To use a template, click the "Download" link next to the desired template <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This opens a new page, such as the "purchase order PDF generator" page, which includes both a database and a template <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Understanding the Notion Template and Database

The purchase order template contains elements like purchase order number, date, supplier, buyer, and item description <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Key elements that will be replaced with data from the database are enclosed in curly braces, for example, `{Purchase Order Number}`, `{Date}`, `{Supplier Name}`, and `{Buyer Name}` <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

The associated Notion database contains the predefined fields that correspond to these template placeholders, such as supplier name, buyer name, date, and purchase order number <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. PDF documents will be generated for each row of information in the database, replacing the placeholder text in the template with the respective column values <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Duplicating the Template to Notion

To use the template, it must be duplicated to your Notion workspace <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. Look for a "Duplicate" option at the top of the PDF generator page, or "Start with this template" if it's already published <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. After clicking "Duplicate," select your Notion workspace to add the purchase order page <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Connecting Notion to PDF Output

After duplicating the template to your workspace, return to PDF output.com and navigate to the "Settings" section <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

1.  **Configure Page Format:** Select your desired page format for the PDF <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
2.  **Add Templates:** Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
3.  **Select Workspace:** Choose the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
4.  **Select Pages:** Choose the "purchase order PDF generator" page (or the specific template page) from the list <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
5.  **Allow Access:** Click "Allow access" to connect the Notion page with PDF output <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

## Customization and Mapping Properties

Once authenticated, PDF output.com will load the database and template elements <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

### Customizing the Template and Database

The template and database elements are fully [[customizing_notion_templates | customizable]] <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. You can add, delete, or modify any values in the template <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

**Crucial Customization Rule:** Ensure that all values intended to be replaced by database information are placed inside curly braces (e.g., `{Field Name}`) <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. Critically, the name within the curly braces in the template **must exactly match** the corresponding column name in your Notion database <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. Avoid extra commas or spaces, as these mismatches will prevent proper linking <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This ensures successful [[customizing_notion_templates | customization]] and data mapping.

### Mapping Database Properties to Template Elements

PDF output.com will automatically match many elements <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Notion properties from the database are displayed on the left, and template elements are on the right <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

If any elements are unmatched, such as "Total Amount" in the template not matching "Total Amount " (with a space) in the database, they will be highlighted <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. You can use the "Filter unmapped properties" option to quickly identify these <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Manually select the correct matching property from the template side for any unmatched Notion database properties <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Generating Purchase Order PDFs

Once all properties are correctly mapped, click "Export" <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. During export, PDF output.com will automatically add a "PDF Status" column to your Notion database <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. A ticked checkbox in this column indicates that the PDF document for that row has been generated <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. If you need to regenerate a PDF for a specific entry, ensure its checkbox in the "PDF Status" column is unticked <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

After successful export, you can preview a sample PDF <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>, or download all generated documents <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. The generated PDFs will accurately reflect the data from your Notion database within your [[customizing_and_exporting_purchase_order_templates | customized]] template <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

## Additional Features

*   **Connections:** PDF output.com saves generated connections, allowing you to quickly regenerate documents without re-entering database and page information <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Upgrade:** Free plans include a watermark on generated templates, which can be removed by upgrading to a paid subscription <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Settings:** Define PDF page format settings <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Feedback/Help:** Options are available for sending feedback or accessing a setup demonstration video for troubleshooting <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

By following these steps, users can effectively [[customizing_the_notion_template_for_specific_needs | customize]] and [[generating_purchase_order_pdfs_using_notion | generate purchase order PDFs]] using Notion and PDF output.com.