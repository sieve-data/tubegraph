---
title: Using Notion database as an invoice source
videoId: WfYK1BJd490
---

From: [[theaccountantguy]] <br/> 

This article explains how to [[generating_pdf_invoices_from_notion | generate professional invoices]] directly from a [[setting_up_a_database_in_notion | Notion database]] using a tool called PDF Output <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Notion Setup for Invoices

### Invoice Template
A Notion invoice template serves as the basis for the PDF invoices <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This template includes sections like "from" and "to," with client details such as client name, company, address, city, state, and zip <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

Key characteristics of the template:
*   Every element intended to be replaced with data from the database is set as a placeholder text enclosed in curly braces (e.g., `{client name}`) <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. These placeholders will be populated from the database <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

### Invoice Database
The Notion database contains the specific information for each invoice. It includes columns such as client name, amount, bank name, client address, and client company <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Each row of information in the database will populate the template to generate a unique PDF invoice <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Connecting Notion to PDF Output

To [[generating_pdf_invoices_from_notion | generate PDF invoices from Notion]], the PDF Output tool is used <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### Initial Setup
1.  Log in to PDF Output <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
2.  Go to the "Help" section (by clicking 'H') to complete steps for enabling API keys, which are necessary for the setup <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Defining the Connection
1.  **Define a connection name:** For example, "invoice generation" <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  **Select the Notion Database:** Choose the specific Notion database (e.g., "professional invoice database") <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
3.  **Select the Notion Template:** Choose the corresponding Notion template (e.g., "professional invoice template") <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
4.  Click "Next" to load and map the database elements to the template <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Mapping Database Elements to Template Placeholders

PDF Output automatically maps database properties to template elements <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   Database properties (columns) are listed on the left <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   Each database property is connected to a template element (e.g., "client address" in the database maps to `{client address}` in the template) <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   All elements like `item one`, `terms`, and `amount three` are automatically mapped if their names match <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

> [!tip] Naming Convention
> Ensure that the element names in the template placeholders (inside curly braces) exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Fixing Mismatched Elements
If an element is not automatically mapped, it will appear in gray <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. You can click on it and search for the correct corresponding value from the database to manually map it <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## Generating and Downloading Invoices

1.  After mapping, click "Export" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
2.  In your Notion database, a "PDF status" column will show as ticked as each PDF file is generated <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
3.  Once completed, you can click "Preview sample" to review an example of the generated output <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. The output will be clean and accurate, reflecting the data from the database <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
4.  Click "Download all" to download all the generated PDF invoices <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

## Customization

All elements in the invoice template are customizable to your specific requirements <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   Remember to place all placeholder text elements inside curly braces <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   Use the exact same names for these placeholders in your Notion database columns <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

For detailed setup instructions, refer to the "Help" section within PDF Output after logging in <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.