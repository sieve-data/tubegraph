---
title: Customizing invoice templates with placeholders
videoId: WfYK1BJd490
---

From: [[theaccountantguy]] <br/> 

Professional invoices can be [[generating_professional_invoice_pdfs | generated professionally]] directly from a Notion database by utilizing a tool called PDF Output <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This process involves creating a template with specific placeholders that are then populated by data from a Notion database.

## Template Structure

An invoice template typically includes sections like "from" and "to" <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Within these sections, specific details such as client name, client company, client address, city, state, and zip are designated as placeholder text <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### Placeholder Syntax
Every element in the template intended for data replacement from a database must be enclosed in curly braces, e.g., `{client name}` <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Database Integration

The Notion database stores the information that will populate the template <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Database columns, such as "client name", "amount", "bank name", "client address", and "client company", correspond to the placeholders in the template <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. For each row of information in the database, a separate PDF will be generated <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Generating PDFs with PDF Output

To generate the PDFs, the PDF Output tool is used <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Initial Setup
1.  **Log In**: Access the PDF Output interface <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
2.  **API Key Setup**: Navigate to the help section (H) to complete the steps required for enabling API keys, which are necessary for the setup to function <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Connection and Mapping
1.  **Define Connection Name**: Provide a name for the connection, such as "invoice generation" <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Select Database**: Choose the specific Notion database, e.g., "professional invoice database" <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
3.  **Select Template**: Select the corresponding template, e.g., "professional invoice template" <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
4.  **Automatic Mapping**: After clicking "next," the tool loads all elements and values from both the database and the template, automatically [[mapping_database_elements_to_invoice_templates | mapping each database element to its corresponding template placeholder]] <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
    *   Database properties are listed on the left, connected to their respective template elements <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. For example, "client address" from the database will be linked to the "client address" placeholder in the template <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
    *   It is crucial that the element names in the placeholder match the column names in the database <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
5.  **Manual Correction**: If a mismatch occurs, the element will appear in gray <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. You can manually click on it and search for the correct database value to establish the mapping <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Export and Download
1.  **Export**: Click "export" to begin the PDF generation process <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
2.  **Status Tracking**: A "PDF status" column in the database will be ticked as each PDF file is generated <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
3.  **Preview and Download**: Once generated, a "preview sample" allows you to review the output <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>, and "download all" retrieves all generated PDF files <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

## Customization

All elements within these templates are [[customizing_templates_for_pdf_generation | customizable]] according to specific requirements <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. The key is to ensure that all placeholder text elements are correctly enclosed in curly braces and use the exact same names as the corresponding columns in the Notion database <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.