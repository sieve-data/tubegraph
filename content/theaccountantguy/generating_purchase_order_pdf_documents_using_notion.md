---
title: Generating purchase order PDF documents using Notion
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This article outlines how to [[generating_purchase_order_pdfs_using_notion | generate purchase order PDF documents]] using a [[using_notion_for_managing_purchase_orders | Notion database]] and template in conjunction with the PDFOutput service <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Getting Started with PDFOutput

The first step is to log in to PDFOutput.com <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. Upon logging in, you will see an interface that allows for connecting a database and a template <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

### Accessing Templates

PDFOutput provides a list of predefined templates to facilitate [[generating_pdf_documents_from_notion | PDF document generation]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. These include templates for [[generating_pdf_invoices_from_notion_data | invoices]], [[generating_payment_receipts_in_pdf_using_notion | payment receipts]], and purchase orders <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. You can quickly search for a specific template using the search icon <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Setting Up Your Purchase Order Template

1.  **Download the Template**: Select and click the download link next to the desired purchase order template <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This opens a dedicated "Purchase Order PDF Generator" page, which includes both a database and a template <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

2.  **Understand the Template Structure**: The template defines elements like purchase order number, date, supplier, buyer, and item description <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. Key elements intended for dynamic replacement are enclosed within curly braces (e.g., `{purchase order number}`, `{date}`, `{supplier name}`) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

3.  **Database Integration**: The associated Notion database contains predefined fields (columns) such as `supplier name`, `buyer name`, `date`, and `purchase order number` <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. These column values are used to replace the placeholder text in the template <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Multiple rows in the database allow for [[generating_bulk_pdf_documents_using_google_docs_and_notion | generating bulk PDF documents]] <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

4.  **Duplicate to Notion Workspace**: On the "Purchase Order PDF Generator" page, click the "Duplicate" option (or "Start with this template" if published) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Select your Notion workspace to add the page <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Connecting and Generating PDFs

1.  **Connect in PDFOutput Settings**: After duplicating the template to your Notion workspace, return to PDFOutput.com. Go to the "Settings" section <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
    *   Select your desired page format for the PDF <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   Click "click here to add templates" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
    *   Select your Notion workspace <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a> and then choose the duplicated "Purchase Order PDF Generator" page <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
    *   Click "Allow access" to connect the page with PDFOutput <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

2.  **Select Database and Template**: Once authenticated, the database and template elements will load <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
    *   From the Notion database dropdown, select the `Purchase Order` database <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
    *   From the Notion template dropdown, select the template page (e.g., `Template`) <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   Give your connection a name (e.g., "Purchase Order") <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a> and click "Next" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

3.  **Map Properties**: PDFOutput will attempt to automatically match database properties with template placeholders <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
    *   Notion properties (from the database) are shown on the left, and template elements are on the right <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   Ensure exact naming: The name of the database column must precisely match the placeholder text within the curly braces in the template <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. Even extra spaces or commas can cause mismatches <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
    *   For unmapped properties, use the filter option to identify them <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>, then manually select the corresponding template element <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
    *   You can sort or search properties for easier mapping <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

4.  **Export and Download**:
    *   Click "Export" <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
    *   A `PDF Status` column will automatically be added to your Notion database, ticking once a PDF has been generated for that row <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. Untick this box to regenerate a PDF for a specific row <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
    *   Once the export is successful, you can preview a sample PDF <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a> or download all generated documents <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
    *   The generated PDFs will reflect the data from each row of your Notion database, accurately filling in the template placeholders <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

## Customization and Features

*   **Customization**: Both the Notion template and database are fully customizable <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. You can add, delete, or modify values, ensuring that all values to be replaced are within curly braces in the template and match the database column names <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. This process allows for [[using_notion_for_pdf_template_creation | PDF template creation using Notion]].
*   **Connections**: PDFOutput saves your configurations as "connections," allowing you to regenerate documents without re-entering database and page information <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Upgrade**: Free plans include a watermark on generated PDFs. Upgrading to a paid plan removes this watermark <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Feedback and Help**: You can submit feedback if you encounter issues or find additional help resources within the platform <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

This method streamlines the process of [[generating_pdf_documents_from_purchase_orders_in_notion | generating PDF documents from purchase orders in Notion]] and [[generating_pdf_documents with_notion_and_pdfoutput | generating PDF documents with Notion and PDFOutput]].

For further assistance, you can contact `notionformyuse@gmail.com` <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.