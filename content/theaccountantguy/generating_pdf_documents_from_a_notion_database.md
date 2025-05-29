---
title: Generating PDF documents from a Notion database
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

This article details the process of [[generating_pdf_documents_with_notion | generating PDF documents]] in bulk from a Notion database using a Notion page as a template. The demonstration utilizes a professional invoice template in Notion to create multiple invoices based on records from a Notion database <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Core Components

The process relies on three main components:
1.  **Notion Page (Template)**: A Notion page is set up as a template for the PDF document <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Placeholders within this template are defined using curly brackets (e.g., `{client name}`) <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
2.  **Notion Database**: A Notion database holds the specific information for each document to be generated <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. The columns in this database correspond to the placeholders in the Notion template <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
3.  **External Tool (pdf4put.com)**: This online service facilitates the bulk [[creating_pdf_documents_from_notion_database | creation of PDF documents]] by connecting the Notion template and database <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Step-by-Step Process for PDF Generation

### 1. Prepare Your Notion Template Page
The Notion page serving as your template must contain all the necessary information for the PDF <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Crucially, any dynamic information that will be pulled from your database should be enclosed in curly brackets, such as `{client name}` or `{invoice number}` <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>, <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

### 2. Prepare Your Notion Database
Ensure your Notion database contains records with the specific data needed for each PDF <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The column names in your database must exactly match the names used within the curly brackets in your Notion template page (e.g., a column named "Client Name" for the `{client name}` placeholder) <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### 3. Using pdf4put.com

#### A. Sign In
Navigate to pdf4put.com and sign in with your preferred account <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

#### B. Provide Notion Page URL
1.  Go to your Notion template page.
2.  Click "Share" -> "Publish" -> "Publish" again to make the page public <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This ensures it's accessible for use <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
3.  Copy the public link to the Notion page <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
4.  Paste this link into the "Notion Page URL" field on pdf4put.com <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
5.  Click "Load Page" to display a preview of your template on the right side <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

#### C. Create and Connect Notion API Key
An API key is essential to connect your Notion database with pdf4put.com <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
1.  On pdf4put.com, click the "Click here to add notion API key" link <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
2.  This will open Notion's integration page. Click "New integration" <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
3.  Give your integration a name (e.g., "New Key") and select your Notion account, then click "Save" <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
4.  Copy the generated API key by clicking "Show" and then "Copy" <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
5.  Paste the API key into the "Notion API Key" field on pdf4put.com <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

#### D. Connect Database to API Key
This step is critical for the [[notion_database_integration_with_pdf_generation | Notion database integration with PDF generation]].
1.  Go back to your Notion database.
2.  Click the three dots in the top right corner of the database view <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
3.  Click "Connections" <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
4.  Search for the API key you just created (e.g., "New Key") <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
5.  Select your API key and click "Confirm" to connect the database <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

#### E. Provide Notion Database URL
1.  From your Notion database, copy the URL from the browser's address bar <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
2.  Paste this URL into the "Notion Database URL" field on pdf4put.com <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

#### F. Load Database and Generate PDFs
1.  Click "Load Database" <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
2.  Select the column you want to use for naming the generated PDF files (e.g., "invoice number") <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
3.  You can choose to generate PDFs for "All Rows" or select "Custom Rows" by specifying a range or specific row numbers <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
4.  Click "Generate PDF" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
5.  The system will begin populating and presenting each PDF for saving <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The placeholders from the Notion template will be replaced with data from each database record <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
6.  You can adjust layout settings such as paper size (e.g., A4, Letter), orientation (Portrait or Landscape), and which pages to print <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
7.  Save each generated PDF file to your desired location <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The files will be named according to the column you selected for file naming <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

## Important Considerations

*   **Page Sharing**: Always ensure your Notion template page is shared publicly and accessible before pasting its URL <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>, <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Database Connection**: Verify that your Notion database is correctly connected to the Notion API key you created <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>, <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **Relational Properties**: If your Notion database uses any relation properties that link to other databases, those relational databases must also be connected to the *same* API key <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>, <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. This ensures all linked data can be fetched seamlessly <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

This comprehensive approach allows for efficient [[pdf_document_generation_from_notion | PDF document generation from Notion]] by [[using_notion_as_a_template_and_database_for_pdfs | using Notion as a template and database for PDFs]] and leveraging an external tool for the [[process_of_exporting_pdfs_from_notion | process of exporting PDFs from Notion]].