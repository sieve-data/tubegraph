---
title: Generating invoices from a Notion database
videoId: WfYK1BJd490
---

From: [[theaccountantguy]] <br/> 

This article details how to [[generating_pdf_invoices_in_bulk_using_a_notion_database | generate professional invoices directly from a Notion database]] using the PDF Output tool <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This process leverages [[using_notion_database_and_templates_for_pdf_generation | Notion databases and templates]] to automate PDF creation.

## Key Components

To [[setting_up_notion_for_invoice_management | set up Notion for invoice management]] and generation, two main components are required:

### 1. Notion Invoice Template

A Notion template is used as the base for the invoice layout <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   It includes sections like "from" and "to" <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
*   Placeholder text, such as `client name`, `client company`, `client address`, `city`, `state`, and `zip`, are enclosed within curly braces `{}` <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   Any element within curly braces will be replaced by data from the Notion database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This allows for [[customizing_invoice_templates_in_notion | customizing invoice templates in Notion]] with dynamic data.

### 2. Notion Invoice Database

The Notion database holds all the specific information required for each invoice <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   Columns in the database correspond to the placeholders in the template, e.g., `client name`, `amount column`, `bank name`, `client address`, `client company` <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   Each row in the database represents a unique invoice, and its information will populate the template to generate a PDF <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This is crucial for [[using_databases_in_notion_for_invoice_tracking | using databases in Notion for invoice tracking]].

## Using PDF Output for Invoice Generation

The PDF Output tool facilitates the connection between your Notion template and database to generate invoices.

### Initial Setup
1.  **Login:** Access the PDF Output interface <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
2.  **API Key Configuration:** Navigate to the "Help" section (by clicking 'H') to complete steps for enabling API keys. This is necessary to use the setup <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. Instructions for this are provided within the "Help" section <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### Connecting Notion to PDF Output
1.  **Define Connection Name:** Provide a name for your connection, for example, "Invoice Generation" <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Select Database:** Choose the specific Notion database you want to use. In this example, it's named "professional invoice database" <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
3.  **Select Template:** Choose the Notion template to be used for the invoice, such as "professional invoice template" <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Mapping Database Properties to Template Elements
*   After clicking "Next," the PDF Output tool loads and automatically maps database elements (columns) to the corresponding template placeholders <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   For successful automatic mapping, the element names in the template's placeholders (e.g., `{Client Address}`) must precisely match the column names in the Notion database (e.g., "Client Address") <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   If a mismatch occurs, the element will appear in gray <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. You can manually click on it and search for the correct value to map it <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Generating and Downloading Invoices
1.  **Export:** Click the "Export" button <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
2.  **PDF Status:** Observe the "PDF Status" column in your Notion database. It will automatically tick as each PDF file is generated <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. This enables [[creating_invoices_in_bulk_using_notion | creating invoices in bulk using Notion]].
3.  **Preview Sample:** Once generated, you can click "Preview Sample" to view an example of the output <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. The generated PDFs are clean and accurately populated with data from the database <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. For instance, `Acme Incorporation` and its address will be correctly replaced <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
4.  **Download All:** To download all generated PDF invoices, click "Download All" <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. The files will be downloaded to your system <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### Customization
*   All elements in the invoice template are customizable to fit your specific needs <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   The critical rule for [[creating_a_professional_invoice_template_in_notion | creating a professional invoice template in Notion]] is that all placeholder text elements must be enclosed within curly braces `{}` <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   Ensure that the names used in these placeholders match the column names in your [[creating_a_database_in_notion | Notion database]] exactly <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

For further assistance, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.