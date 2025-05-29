---
title: PDF Output tool for document generation
videoId: W_j9W6XedqM
---

From: [[theaccountantguy]] <br/> 

The [[introduction_to_pdf_output_tool | PDF Output tool]] (available at [[using_pdf_output_com_for_pdf_generation | PDFoutput.com]]) facilitates the bulk generation of PDF documents by utilizing Notion templates and databases <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process involves mapping data from a Notion database to placeholders within a Notion template to create multiple customized PDF files <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## Core Components
[[automating_pdf_document_generation | Automating PDF document generation]] with [[introduction_to_pdf_output_tool | PDF Output tool]] relies on two primary Notion components:

1.  **Notion Template:** This document contains elements enclosed in curly braces (e.g., `{receipt number}`, `{company website}`) which act as placeholders for dynamic data <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
2.  **Notion Database:** This database holds the specific information that will replace the placeholders in the template <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Each column in the database should correspond to an element in the template, ideally using the exact same naming convention, including capitalization and spaces <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. Each row in the database typically represents one PDF document to be generated <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Process for Bulk PDF Generation

The following steps outline how to [[using_pdf_output_tool_for_bulk_pdf_generation | use the PDF Output tool for bulk PDF generation]]:

### 1. Access and Log In to PDFOutput.com
Navigate to [[using_pdf_output_com_for_pdf_generation | PDFoutput.com]] and log into your account <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### 2. Duplicate Template and Database to Notion Workspace
From the "Templates" section within [[introduction_to_pdf_output_tool | PDF Output tool]], locate the desired template (e.g., "Payment Receipts") and its corresponding database <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   Click on the "template link" and "database link" to open them in new windows <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   Duplicate both the Notion template and the Notion database to your local Notion workspace <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Select your Notion workspace (e.g., "accountant guy workspace") when prompted <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

### 3. Connect Notion Database and Template to PDFOutput
On the [[introduction_to_pdf_output_tool | PDF Output tool]] interface, click "Click here to add database" or "Add template" <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   Grant permission to access your Notion pages <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   Select your Notion workspace and then choose the duplicated template and database from the list <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   Click "Allow access" to connect them <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   Provide a connection name (e.g., "payment receipts") and click "Next" <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### 4. Map Database Properties to Template Elements
The [[introduction_to_pdf_output_tool | PDF Output tool]] will automatically populate database properties and attempt to map them to template elements <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **Automatic Mapping:** If the column names in your Notion database exactly match the placeholder names in curly braces within your Notion template, the mapping will occur automatically <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   **Manual Mapping:** If there are mismatches, you may need to manually select the corresponding database property for each template element <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. The tool provides filter, search, and sorting options for properties <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

### 5. Generate and Download PDFs
Once all elements are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   The tool will process each row in your database, generating a separate PDF document <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   You can preview a sample document to ensure the output is correct <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   Click "Download all documents" to receive a zip file containing all generated PDFs <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

### Example: Payment Receipt Generation
For payment receipts, the database would contain fields like receipt number, receipt date, receipt time, customer name, customer email, etc. <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. The template would have placeholders for these fields. The tool replaces these placeholders with the data from each row, [[using_pdf_output_tool_for_invoice_generation | generating a payment receipt for each entry]] <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

## Features and Settings

### Connections
The "Connections" section stores previously created database and template configurations, allowing quick regeneration of documents without manually adding components again <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

### Templates
A library of different templates is available, including payment receipts and invoices, with more templates planned for future additions <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### Upgrade Option
The free plan includes a "made with [[introduction_to_pdf_output_tool | PDF Output tool]]" watermark on generated PDFs <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. Upgrading to a paid plan removes the watermark and offers higher generation limits <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.

### Settings
*   **Page Format:** Define the page format for PDFs (default is A4) <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   **Add Templates/Databases:** Add more templates and databases for subsequent use <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

### Feedback and Help
Users can provide feedback through a dedicated window <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. A help section explains how to [[using_pdf_output_for_document_generation | use a custom PDF document]] template and database, allowing for document generation without predefined templates <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

> [!TIP] Naming Convention <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>
> Ensure that elements inside curly braces in your template use the exact same naming convention (including spaces and capitalization) as the corresponding column names in your Notion database to enable automatic mapping and avoid manual configuration <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

> [!INFO] Refresh <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>
> If the database or template does not load initially, click the refresh button <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.