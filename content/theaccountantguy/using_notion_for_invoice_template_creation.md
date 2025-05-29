---
title: Using Notion for invoice template creation
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

Notion can be used as a platform for [[creating_professional_invoices_using_notion | creating professional invoices]] by setting up a template and linking it to a database to [[generating_professional_invoices_from_notion_database | generate multiple PDF documents]]. This process leverages a Notion page as an [[creating_and_using_invoice_templates_in_notion | invoice template]] and a Notion database to store the dynamic invoice data <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Setting Up Your Notion Invoice Template

A professional invoice template in Notion includes all necessary information for an invoice document <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Key information fields that will be dynamically populated from a database are placed within curly brackets, such as `{client name}`, `{client company}`, `{client address}`, etc. <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. These placeholders correspond to column names in your Notion database <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

## [[Generating PDF invoices from Notion data]] Using PDFoutput.com

To [[generating_pdf_invoices_from_notion_data | generate PDF documents]] from your Notion invoice template and database, a third-party tool like PDFoutput.com can be used <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This platform enables the bulk creation of PDF documents <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

### Steps to Generate Invoices:

1.  **Sign In**: Access PDFoutput.com and sign in with your chosen account <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
2.  **Provide Notion Page URL**:
    *   Navigate to your Notion invoice template page <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
    *   Click "Share" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
    *   Click "Publish" twice to make the page public <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. This allows the page to be accessed by PDFoutput <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
    *   Copy the page link (either via "Copy link" or from the browser URL bar) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
    *   Paste the copied URL into PDFoutput.com <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
    *   Click "Load page" to display your template <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
3.  **Create and Connect Notion API Key**:
    *   PDFoutput requires an API key to connect to your Notion database <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
    *   Click the "click here to add notion API key" link on PDFoutput <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
    *   In the Notion integrations page, click "New integration" <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   Provide a name for the integration (e.g., "new key"), choose your Notion account, and click "Save" <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
    *   Copy the newly generated API key <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   Paste the API key back into PDFoutput.com <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
4.  **Connect Notion Database**:
    *   Go to your Notion invoice database <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    *   Click the three dots in the top right corner of the database view <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Select "Connections" <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
    *   Search for and select the API key you just created (e.g., "new key") to connect the database to it <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. Confirm the connection <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
    *   Copy the database URL from your browser's address bar <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
    *   Paste the database URL into PDFoutput.com <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
5.  **Load Database and Select Naming Column**:
    *   Click "Load database" on PDFoutput <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
    *   Choose a column from your database (e.g., "invoice number") to name the generated PDF files <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
    *   Optionally, specify custom rows or a range of rows to generate documents for; otherwise, select "all rows" <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
6.  **Generate PDFs**:
    *   Click "Generate PDF" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
    *   The tool will process each record, populating the template with data from the database <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
    *   You can adjust layout settings such as paper size (e.g., A4), orientation (portrait/landscape), and pages to print <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
    *   Save each generated PDF document to your desired location <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The files will be saved with the names specified by your chosen column (e.g., "invoice number") <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

The generated PDF invoices will accurately reflect the data from your Notion database, with placeholders replaced by corresponding values <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

## Important Considerations for [[Using Notion for PDF Template Creation]]

*   **Template Placeholders**: Ensure all dynamic fields in your Notion template are enclosed in curly brackets `{}` and match the exact names of your database columns <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Notion Page Sharing**: The Notion invoice template page must be shared publicly and made accessible for the tool to fetch its content <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Database API Connection**: The Notion database containing invoice data must be connected to the specific API key you created for PDFoutput <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Relational Properties**: If your database includes relational properties (linking to other databases), those related databases must also be connected to the *same* API key for data to be fetched seamlessly <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

By following these steps and considerations, you can efficiently [[using_a_notion_database_and_templates_to_create_pdf_invoices | create and generate professional PDF invoices using Notion]] and a third-party service like PDFoutput.com, streamlining your [[invoicing_and_workflow_management_in_notion | invoicing and workflow management in Notion]] <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

For further assistance, you can reach out via notionformyuse@gmail.com or through the contact window on the PDFoutput website <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.