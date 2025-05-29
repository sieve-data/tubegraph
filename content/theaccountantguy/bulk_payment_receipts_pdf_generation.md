---
title: Bulk Payment Receipts PDF Generation
videoId: W_j9W6XedqM
---

From: [[theaccountantguy]] <br/> 

This article discusses how to generate [[generating_payment_receipt_pdfs_with_notion | payment receipt PDF documents]] in bulk using a Notion template and a Notion database with the help of PDF Output <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Template and Database Overview

The process relies on a Notion template and a Notion database working together <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

### Payment Receipt Template
The payment receipt template contains elements enclosed in curly braces, such as `{company website}` <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. These elements are placeholders that will be replaced with data from the database <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### Notion Database
The Notion database contains rows of information, where each row corresponds to a separate PDF document to be generated <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Columns in the database, like `receipt number`, `receipt date`, and `receipt time`, directly correspond to the placeholder elements in the template <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. It is crucial for the database column names to exactly match the template placeholders, including capitalization and spaces, to ensure automatic mapping <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

## Step-by-Step Generation Process

To [[generating_pdf_documents_in_bulk | generate PDF documents in bulk]], the PDF Output platform is used <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

1.  **Access PDF Output**: Navigate to PDF Output.com <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
2.  **Log In**: Log in to your PDF Output account <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
3.  **Duplicate Template and Database**:
    *   From the "Templates" section on PDF Output, search for "payment receipts" <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
    *   Locate the "Payment Receipts" template and its corresponding database <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
    *   Click on the "Template link" and "Database link" to open them <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   Duplicate both the template and the database to your local Notion workspace <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Ensure you select the correct Notion workspace <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
4.  **Connect Notion to PDF Output**:
    *   On the PDF Output dashboard, click "Click here to add database" or "Add template" <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   Grant PDF Output permission to access your Notion pages by selecting your workspace (e.g., "accountant guy") and the duplicated template and database <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   Click "Allow access" to authenticate the connection <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
    *   Once connected, the "Payment Receipts Database" and "Payment Receipt Template" will be displayed <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
5.  **Name the Connection**: Provide a connection name, such as "Payment Receipts," and click "Next" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
6.  **Map Properties**:
    *   PDF Output will automatically populate database properties and attempt to map them to the template elements <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
    *   If there are mismatches, you can manually select the correct database property for each template element <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
    *   Filters and sorting options are available to manage properties <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
7.  **Create PDFs**: Once all properties are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. PDF Output will then [[generating_pdf_documents_in_bulk | generate the PDF documents in bulk]] based on each row in your database <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

## Output and Review

After generation, you can:
*   **Preview a Sample**: Review a sample document to check its appearance and data accuracy <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. The sample will show a clean output with all fields mapped correctly, like receipt number, date, time, customer name (e.g., Alice Brown, John Doe, Jam Smith), and email <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   **Download All Documents**: Download all generated PDFs as a single archive <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. Each document will reflect the data from its corresponding row in the Notion database <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

## Additional PDF Output Features

PDF Output offers several features to streamline your document generation:

*   **Connections**: View a list of previously created connections (database and template pairings) <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. Selecting a saved connection automatically loads the database and template, avoiding manual re-entry <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   **Templates**: Explore various pre-built templates for different use cases beyond payment receipts, such as [[generating_and_managing_pdf_invoices | invoices]], [[generating_sales_receipts_in_pdf_format | sales receipts]], or [[generating_purchase_order_pdfs | purchase orders]] <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **Upgrade**: Understand the differences between free and paid plans <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. The free plan includes a "made with PDF Output" watermark, which is removed in paid subscriptions <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. Paid plans also offer higher limits for document generation <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Settings**: Define page formats (e.g., A4) <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>, and add more templates and databases to your workspace <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Feedback**: Submit questions or feedback directly to the platform developers <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   **Custom Templates**: For users who prefer not to use predefined templates, there is a help section explaining how to generate custom PDF documents <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

For any questions or issues, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.