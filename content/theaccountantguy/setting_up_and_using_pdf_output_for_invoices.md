---
title: Setting up and using PDF Output for invoices
videoId: WfYK1BJd490
---

From: [[theaccountantguy]] <br/> 

[[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] is a tool designed to [[generating_professional_invoice_pdfs | generate professional invoices]] directly from a [[generating_pdf_invoices_from_notion | Notion database]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It automates the process of populating a template with data from your Notion database to create PDF documents <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Preparing Notion for PDF Output

To use [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]], you need both an invoice template and a database set up in Notion <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

### Invoice Template Configuration

The invoice template in Notion should include placeholder text for dynamic data <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
*   **Placeholders**: Every element in the template that will be replaced by database information must be enclosed in curly braces, e.g., `{client name}`, `{client company}`, `{client address}`, `{city}`, `{state}`, and `{zip}` <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. These curly-braced elements are designed to be replaced by data from your Notion database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Customization**: All elements in the template are customizable according to your specific requirements <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

### Database Structure

Your Notion database should contain columns that correspond to the placeholder names in your template <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Column Names**: The column names in the database should match the placeholder names in the template (e.g., `client name`, `amount column`, `bank name`, `client address`, `client company`) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Data Population**: For each row of information in your database, [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] will populate the template and [[generating_pdf_invoices_using_pdfoutput | generate a PDF]] <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Connecting Notion to PDF Output

### Initial Setup and API Keys

Before using [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]], you need to complete [[steps_to_set_up_and_export_pdfs_using_pdf_output | certain steps]] to enable the API keys <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   Log in to [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
*   Go to the help section by clicking on "H" <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   Follow the instructions provided to set up the API connection <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### Creating a New Connection

1.  **Define Connection Name**: After enabling API keys, type a name for your connection, such as "invoice generation" <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Select Database**: From the drop-down menu, select your Notion database (e.g., "professional invoice database") <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
3.  **Select Template**: Similarly, select your Notion template (e.g., "professional invoice template") <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
4.  **Proceed**: Click "Next" <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Mapping Database Fields to Template Placeholders

[[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] automatically loads all elements and values from your database and template, then attempts to map them <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Automatic Mapping**: The tool automatically maps database properties (listed on the left) to the corresponding template elements <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. For example, `client address` from the database will be connected to `client address` in the template <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   **Manual Correction**: If an element is not matching or appears in gray, click on it and search for the correct value to manually map it <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Naming Convention**: Ensure that the element names in the curly brace placeholders in your template exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

## Generating and Exporting Invoices

### Export Process

1.  **Initiate Export**: Once mapping is complete, click "Export" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
2.  **Status Tracking**: In your Notion database, a "PDF status" column will automatically tick as each PDF file is generated <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

### Previewing and Downloading PDFs

*   **Preview Sample**: You can click "Preview sample" to view a generated PDF <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This allows you to verify that all elements from the database are correctly populated in the template <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Download All**: Click "Download all" to download all generated PDF files <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. The downloaded files will be clean and ready for use <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   [[bulk_pdf_invoice_generation | Bulk PDF generation]] is supported, allowing you to create multiple invoices from a single database export <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

## Customization and Tips

*   Remember to enclose all placeholder text elements in curly braces in your template <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   Use the exact same names for these placeholders as your column names in the Notion database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   Refer to the "H" (Help) section within [[using_pdf_output_tool_for_efficient_document_creation | PDF Output]] for detailed setup instructions <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

## Support

For any questions, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.