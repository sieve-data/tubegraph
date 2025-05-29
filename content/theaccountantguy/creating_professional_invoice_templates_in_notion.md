---
title: Creating professional invoice templates in Notion
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

This article details how to create a professional invoice template within Notion and use it to generate PDF documents in bulk <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This process leverages a Notion database to store invoice-related information and a third-party tool, pdf4put.com, for the PDF generation <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Template Structure in Notion

A professional invoice template is created as a Notion page <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Key information within this template that needs to be dynamic (e.g., client name, address, invoice number) is placed inside curly brackets `{}` <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. These curly-bracketed fields will later be replaced with data from a Notion database <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Database Integration

An essential part of this system is a Notion database that holds various invoice-related information <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Each record in this database contains the data for a single invoice, corresponding to the fields within the Notion template <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. For example, if the template has `{client name}`, the database will have a column named "client name" <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

## Generating PDF Invoices

The bulk PDF generation is performed using the `pdf4put.com` service <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### Step-by-Step Process

1.  **Sign In**: Navigate to `pdf4put.com` and sign in using your preferred account <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
2.  **Publish Notion Page**: The Notion invoice template page must be made public.
    *   In Notion, click "Share" on your invoice template page <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
    *   Click "Publish" and then "Publish" again to make the page publicly accessible <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
    *   Copy the public link of the page <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
3.  **Provide Notion Page URL**: Paste the copied Notion page URL into `pdf4put.com` and click "Load page" <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. The template document should appear on the right side of the interface <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
4.  **Create Notion API Key**:
    *   On `pdf4put.com`, click the link to add a Notion API key <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This will open a Notion integration window.
    *   Click "New integration," provide a name (e.g., "new key"), and choose your account <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   Save the integration and copy the generated API key <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
    *   Paste the API key into `pdf4put.com` <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
5.  **Connect Database to API Key**:
    *   Go back to your Notion invoice database <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    *   Click the three dots `(...)` in the top right corner of the database view <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Select "Connections" and search for the API key you just created (e.g., "new key") <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
    *   Select the API key and click "Confirm" to connect the database <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
6.  **Provide Database URL**: Copy the URL of your Notion invoice database <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Paste this URL into `pdf4put.com` <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
7.  **Load Database and Select Naming Column**: Click "Load database" on `pdf4put.com` <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. You will be prompted to choose a column from your database to name the generated PDF files (e.g., "invoice number") <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
8.  **Generate PDFs**:
    *   You can choose to generate PDFs for "all rows," a "custom range" (e.g., rows 4-7), or "custom rows" (specific rows) <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   Click "Generate PDF" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
    *   The system will start populating the invoices, replacing the curly-bracketed fields with data from your database <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
    *   For each invoice, you can adjust layout settings like paper size (e.g., A4, Letter), orientation (portrait or landscape), and pages to print <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
    *   Click "Save" for each generated PDF, choosing the destination folder on your computer <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

The generated PDF documents will accurately reflect the data from your Notion database, with dynamic fields correctly populated <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## Important Considerations

*   **Notion Page Sharing**: Ensure your Notion template page is shared publicly and accessible before attempting to generate PDFs <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Database Connection**: The Notion database containing your invoice data *must* be connected to the API key you created <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Relational Properties**: If your database utilizes any relational properties (linking to other Notion databases), those linked databases must also be connected to the *same* API key for the process to work seamlessly <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. This ensures all necessary data can be fetched <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

This method provides an efficient way to generate professional PDF invoices from a Notion-based system, leveraging [[creating_and_using_templates_in_notion | Notion templates]] and database capabilities for bulk document creation. This aligns with [[using_templates_in_notion_for_business | using templates in Notion for business]] and [[setting_up_a_small_business_bookkeeping_template_in_notion | setting up a small business bookkeeping template in Notion]].

For any queries or assistance, you can reach out via email at `notionformyuse@gmail.com` or use the contact window on `pdf4put.com` <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.