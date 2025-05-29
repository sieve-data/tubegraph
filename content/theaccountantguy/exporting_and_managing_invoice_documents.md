---
title: Exporting and managing invoice documents
videoId: n1_fpSFcf3k
---

From: [[theaccountantguy]] <br/> 

This article details how to [[exporting and managing PDF documents for business | export and manage PDF invoice documents]] by utilizing a Notion page and template with PDF Output software. The process involves connecting a Notion database to a pre-designed template to generate customizable invoices in PDF format.

## Overview of the Process

The system allows users to generate PDF documents from a Notion page and template <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This demonstration specifically uses an invoice template <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Getting Started with PDF Output

1.  **Access PDF Output:** Log in to PDF output.com, the website where documents are created <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
2.  **Select a Template:**
    *   Navigate to the "Templates" section <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
    *   Choose from a list of pre-created templates <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. For invoices, click the download link next to the invoice template <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
    *   A search, sorting, or filter option is available to find specific templates <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
3.  **Duplicate Template to Notion:**
    *   After selecting a template, click "Start with this template" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
    *   Duplicate the template onto your Notion workspace <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Select your desired workspace and click "add to private" <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

## Configuring Template and Database

### Template Structure

The template contains placeholder text elements, such as client name, address, invoice number, date, and terms, enclosed in curly braces <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. These placeholders will be replaced with data from a connected database <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### Database Structure

The Notion database contains columns corresponding to the template's placeholder elements, like invoice number, date, client name, and client company <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Each row in the database represents a specific invoice's data <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

> [!NOTE] Naming Convention
> Ensure that the naming convention for data elements in the database columns exactly matches the placeholder text within the curly braces in the template <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. This ensures correct mapping and output generation <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### Connecting to PDF Output Settings

1.  **Add Template:** Go to the "Settings" section in PDF Output and click "Add Template" <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
2.  **Select Workspace:** Select the Notion workspace where the template was duplicated <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
3.  **Grant Access:** Click "Select pages" and choose the "invoice generator template," then click "Allow access" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This authenticates and adds the template to PDF Output <a class="yt=" data-t="00:03:36">[00:03:36]</a>.
4.  **Sync Data:** Allow a few seconds for the database and template elements to sync <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
5.  **Map Properties:** The system will automatically map Notion properties (database columns) to the corresponding template elements <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Unmapped properties can be manually searched for and mapped <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

## [[managing_invoice_pdf_generation_settings | Generating and Exporting Invoices]]

1.  **Initiate Export:** Click "Export" to start the document processing <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
2.  **PDF Status:** In the Notion database, a "PDF Status" column will automatically get checked as documents are generated <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
3.  **Preview and Download:**
    *   After a successful export, you can "Preview sample" to see a generated invoice <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
    *   To [[bulk_export_of_pdf_documents | bulk export of PDF documents]], click "[[bulk_exporting_and_downloading_generated_pdf_files | Download all]]" to download all generated PDF invoices <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
4.  **Re-generation Note:** Ensure that the "PDF Status" row in the Notion database is unticked if you wish to re-generate a document from scratch, as ticked rows will be ignored <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

## Customization and Additional Features

*   **Template Customization:** The invoice template is fully customizable; you can add, delete, or modify elements as needed <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Database Customization:** The Notion database can also be customized to suit your specific invoice details <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   **Watermark:** On a free plan, PDFs will include a "PDF output" watermark; upgrading to a paid plan removes this <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
*   **Saved Connections:** The "Connections" section automatically saves your mapped database and template settings, allowing you to load them quickly without re-mapping <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Help Section:** A comprehensive guide on setting up the system for the first time is available under the "Help" section <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

This process facilitates [[adding_and_managing_invoice_details_in_a_database | adding and managing invoice details in a database]] and efficiently [[exporting_completed_pdf_invoices | exporting completed PDF invoices]] using [[using_pdf_output_software_for_invoice_creation | PDF Output software for invoice creation]].