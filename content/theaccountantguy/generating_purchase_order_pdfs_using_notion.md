---
title: Generating purchase order PDFs using Notion
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 

This article details how to [[generating_pdf_documents_for_purchase_orders | generate purchase order PDF documents]] using a Notion database and a Notion template with the help of PDFOutput.com <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Prerequisites

To begin, you need to log in to PDFOutput.com <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Step-by-Step Guide

### 1. Accessing Purchase Order Templates

*   Once logged into PDFOutput, navigate to the "Templates" section in the sidebar <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   Here, you'll find a list of predefined templates, including invoices, payment receipts, and purchase orders <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   You can use the search icon to quickly find the "purchase order" template <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   Click the "Download" link next to the desired template <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This opens a new page for the purchase order PDF generator, which contains both a database and a template <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

### 2. Understanding the Template and Database

*   **Template:** The template defines the structure of your purchase order, including fields like "Purchase Order Number," "Date," "Supplier Name," and "Buyer Name" <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Placeholder elements, such as `{purchase order number}` or `{supplier name}`, are enclosed in curly braces <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. These placeholders will be replaced with data from your Notion database <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Database:** The accompanying database contains the actual data for these fields (e.g., supplier name, buyer name, date, purchase order number) organized in columns <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. For example, if there are three rows of information, the system will [[generating_purchase_order_pdfs_in_bulk | generate PDF documents]] for each row <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### 3. Duplicating the Template to Notion

*   On the purchase order PDF generator page, click "Duplicate" (or "Start with this template" if it's already published) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   Select your Notion workspace where you want to add the purchase order page <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This will add the purchase order PDF generator page, including its database and template, to your Notion workspace <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### 4. Connecting Notion to PDFOutput

*   Return to PDFOutput and go to the "Settings" section <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   You can set the desired page format for your PDFs <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
*   Click "Click here to add templates" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   Select the Notion workspace where you duplicated the template <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   Choose the "Purchase Order PDF Generator" page that was added to your Notion workspace <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   Click "Allow access" to connect this page with PDFOutput <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. After successful authentication, you will be redirected back to the PDFOutput page <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### 5. Selecting Database and Template in PDFOutput

*   Once redirected, wait for the database and template elements to load <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   From the dropdown menus, select the "Purchase Order Database" and the specific "Template" page (not the main generator page) <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   Give your connection a name, like "Purchase Order" <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   Click "Next" <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### 6. Mapping Properties

*   PDFOutput will automatically try to match Notion database properties (on the left) with template elements (on the right) <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   If any property is unmatched (e.g., due to a mismatch in spacing like "total amount" vs. "totalamount"), you will need to manually map it <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. You can use the "Filter unmapped properties" option to easily find unmatched items <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   Ensure that the names in your Notion database columns exactly match the placeholder names in the template (excluding the curly braces) <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### 7. Exporting and Downloading PDFs

*   Click "Export" <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   PDFOutput will add a "PDF Status" column to your Notion database. When a PDF is generated for a row, this column will be ticked <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. If you need to regenerate a PDF, ensure this checkbox is unticked <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
*   Once the export is successful, you can "Preview sample" to see a generated PDF <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   Click "Download all documents" to get a zip file containing all generated PDFs <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. Each PDF will correspond to a row in your Notion database <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

## Customization

*   Both the template and the database elements are customizable <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   You can add, delete, or modify any values in the template or database <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   Ensure that any values you want to be dynamically replaced are placed inside curly braces in the template <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   The name of the database column must exactly match the placeholder name in the template for correct linking <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

## PDFOutput Features

*   **Connections:** After generating a PDF, PDFOutput stores a connection, allowing you to quickly regenerate documents without refilling database and page details <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Templates:** This section allows you to browse and select predefined templates <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
*   **Upgrade:** Free plans will generate PDFs with a watermark. Paid plans remove the watermark <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Settings:** Define page format for PDFs and manage connected templates <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Feedback:** Provides an option to send feedback or report issues directly to the developer <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Help:** Contains a complete demonstration setup video for troubleshooting <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

For further assistance or other PDF document solutions, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.