---
title: Using Notion for bulk document creation
videoId: W_j9W6XedqM
---

From: [[theaccountantguy]] <br/> 

[[Generating PDF documents in bulk using Notion and PDF Output | PDF Output]] offers a method for [[Using Notion for bulk document creation | generating bulk PDF documents]] using Notion templates and databases <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This process involves a Notion template with placeholder elements and a corresponding Notion database containing the data to replace those elements <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Key Components: Notion Template and Database

The core of this bulk generation system relies on two Notion components:

*   **Notion Template**
    *   This is a predefined document structure, such as a payment receipt template <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
    *   It contains specific elements enclosed in curly braces (e.g., `{receipt_number}`, `{receipt_date}`) that act as placeholders for dynamic data <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
    *   These placeholders are intended to be replaced with information from a database <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   **Notion Database**
    *   This database holds the structured information that will populate the template <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
    *   Each column in the database corresponds to a placeholder element in the template, using the exact same naming convention (including spaces and capitalization) <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
    *   For each row of information in the database, a separate PDF document will be generated <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. For example, three rows would generate three distinct PDFs <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

## The Process: Step-by-Step Guide

### Accessing PDFoutput.com and Duplicating Notion Resources

1.  **Navigate to PDF Output:** Go to PDFoutput.com, the tool used for [[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | bulk PDF document generation]] <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
2.  **Log In:** Log into your account <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
3.  **Find Templates:** Access the "Template" section within PDF Output <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Here, you can search for and select the desired template, such as "Payment Receipts" <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
4.  **Duplicate Template and Database:**
    *   For each template, there are links to both the Notion database and the Notion template <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
    *   Click the template link and duplicate it to your local Notion workspace <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
    *   Similarly, click the database link and duplicate it to your local Notion workspace <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. Ensure both are added to your intended Notion workspace (e.g., "accountant guy workspace") <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

### [[Connecting Notion database with API for bulk document generation | Connecting Notion to PDF Output]]

1.  **Initiate Connection:** On the PDF Output dashboard, click "Click here to add database" or "Add template" <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
2.  **Grant Access:** You will be prompted to give PDF Output access to your Notion pages <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. Select your Notion workspace and then choose both the duplicated template and database from your Notion workspace <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
3.  **Allow Access:** Click "Allow access" to complete the authentication <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
4.  **Name Connection:** Provide a connection name (e.g., "payment receipts") <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### Mapping Data and [[Bulk PDF document generation using Notion | Generating Documents]]

1.  **Automatic Mapping:** PDF Output will load the database properties and attempt to automatically map them to the template elements <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. This automatic mapping works best if the column names in your Notion database exactly match the placeholder names (inside curly braces) in your Notion template <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
2.  **Manual Mapping (if needed):** If there are mismatches, some fields may appear unmapped <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. You can manually select the corresponding database property for each unmapped template element using the dropdown menu <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
    *   *Note:* Filter and sorting options are available for properties <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
3.  **Create PDF:** Once all elements are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. The system will read each row from the database and generate a separate PDF document for each one <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
4.  **Preview and Download:** After generation, you can preview a sample document to ensure correctness <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. Then, click "Download all documents" to receive a zip file containing all the generated PDFs <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

## PDF Output Features

Beyond the core bulk generation process, PDF Output provides additional features:

*   **Connections:** This section displays a list of previously created connections (database and template pairings), allowing you to quickly reload them for future document generation without re-adding them manually <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
*   **Templates:** Offers a library of predefined templates for various use cases, such as payment receipts or [[creating_invoices_in_bulk_using_notion | invoices]] <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **Upgrade Options:** The free plan includes a "Made with PDF Output" watermark <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. Paid plans remove the watermark and offer higher generation limits <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
*   **Settings:**
    *   **Page Format:** Define the output PDF's page format (default is A4) <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
    *   **Add Templates/Databases:** Allows adding more Notion templates and databases to your PDF Output account <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Feedback:** A dedicated window for users to provide feedback or ask questions <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   **Help:** Provides guidance on using custom templates and databases for PDF generation, beyond the predefined options <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

For any questions or assistance, contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.