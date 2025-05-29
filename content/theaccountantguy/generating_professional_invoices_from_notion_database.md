---
title: Generating professional invoices from Notion database
videoId: WfYK1BJd490
---

From: [[theaccountantguy]] <br/> 

This article outlines how to [[creating_professional_invoices_using_notion | generate professional invoices]] directly from a [[using_databases_to_manage_invoice_details_in_notion | Notion database]] using a tool called PDF output <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This process leverages a Notion template and a Notion database to automate the creation of PDF documents <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Notion Setup for Invoicing

To begin, you need to configure your Notion workspace with an invoice template and a database.

### Invoice Template Design
A Notion page serves as the invoice template <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This template includes standard invoice sections like "from" and "to" <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Key details that will be populated dynamically from your database are represented as placeholder text enclosed in curly braces (`{}`) <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

For example, placeholders might include:
*   `{client name}` <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>
*   `{client company}` <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   `{client address}` <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   `{city}` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>
*   `{state}` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>
*   `{zip}` <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>
*   `{item one}` <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>
*   `{amount column}` <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>
*   `{terms and conditions}` <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>

> Customization Tip: All elements within the template are customizable according to your needs. Just ensure placeholder text is within curly braces <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

### Invoice Database Structure
A Notion database holds the invoice details <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Each column in this database corresponds to a placeholder in your template <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. For every row of information in the database, a separate PDF invoice will be generated <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

Example database columns include:
*   Client Name <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
*   Amount Column <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>
*   Bank Name <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>
*   Client Address <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>
*   Client Company <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>

> Important: The names of the placeholder elements in your template **must exactly match** the column names in your Notion database <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

## [[generating_pdf_invoices_from_notion_data | Generating PDF Invoices]] with PDF Output

PDF output is the tool used to bridge your Notion data and template to produce [[generating_pdf_documents_from_notion | PDF documents]] <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Initial Setup and Connection
1.  **Log in to PDF output:** Upon logging in, you'll see the main interface <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
2.  **Enable API Keys:** Navigate to the "Help" section (usually by clicking 'H') <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Follow the instructions to complete the necessary steps for enabling API keys <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
3.  **Define Connection Name:** Provide a name for your connection, such as "invoice generation" <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
4.  **Select Notion Database:** Choose the specific Notion database that holds your invoice data (e.g., "professional invoice database") <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
5.  **Select Notion Template:** Select the Notion template page you created for your invoices (e.g., "professional invoice template") <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
6.  **Proceed to Mapping:** Click "Next" <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Automatic and Manual Mapping
PDF output will automatically attempt to map your database columns to the template placeholders <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The left side of the interface will display your Notion database properties, while the right side shows the corresponding template elements <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

*   For instance, "client address" from the database will be connected to the `{client address}` placeholder in the template <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   If any elements are not automatically matched (indicated by a gray color), you can click on them to manually search and select the correct database column <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### Exporting and Reviewing Invoices
1.  **Start Export:** Click "Export" <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
2.  **Monitor Status:** In your Notion database, a "PDF Status" column will be unticked initially <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. As PDF files are generated for each row, this column will automatically become ticked <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
3.  **Preview Sample:** Once generation is complete, you can click "Preview Sample" to view a generated invoice <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This allows you to verify that all data, such as "Acme Incorporation" and address details, has been correctly populated <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
4.  **Download All:** To get all generated PDF invoices, click "Download All" <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. The files will be downloaded to your device <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

This streamlined process allows for efficient [[invoicing_and_workflow_management_in_notion | invoicing and workflow management]] by leveraging [[using_notion_templates_for_invoice_pdfs | Notion templates for invoice PDFs]] and database integration <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

For any questions or further assistance, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.