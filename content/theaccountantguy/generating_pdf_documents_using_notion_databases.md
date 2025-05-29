---
title: Generating PDF documents using Notion databases
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

This article details the process of [[generating_pdf_documents_in_bulk_with_notion | generating PDF documents in bulk]] using a Notion database and a template, leveraging the pdf4notion.com platform. The method is demonstrated with an invoice template, but can be applied to other document types.

## Overview
The process involves creating a professional template within a Notion page, setting up a Notion database with relevant information, and then connecting these to pdf4notion.com to automatically populate and [[pdf_document_creation_with_notion_and_pdf_output | create PDF documents]] for each record in the database <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Steps for PDF Generation

### 1. Prepare Your Notion Template
*   **Create a Template Page:** Design a professional template (e.g., an invoice) on a Notion page <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.
*   **Define Placeholders:** Identify information that will be dynamically replaced from your database. Place these elements inside curly brackets `{}` in your Notion template (e.g., `{client name}`, `{invoice number}`) <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Share the Page:** Ensure your Notion template page is public. To do this, click "Share," then "Publish," and confirm "Publish" to make the page accessible <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. Copy the public link for later use <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### 2. Set Up Your Notion Database
*   **Create a Database:** Set up a Notion database containing the data you want to use for your documents <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   **Match Properties:** Ensure that the property names in your database exactly match the placeholders you defined in curly brackets in your Notion template (e.g., a "Client Name" column for the `{client name}` placeholder) <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   **Connect to API Key:** Before proceeding, connect your Notion database to the API key you will generate. Click the three dots on the top right of your database, select "Connections," and search for your API key (e.g., "new key") to confirm the connection <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a> <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
    *   If your database uses any relational properties, ensure that the *relational databases* are also connected with the *same API key* <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

### 3. Using pdf4notion.com
*   **Access the Platform:** Go to pdf4notion.com <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   **Sign In:** Sign in using your preferred account <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Provide Notion Page URL:** Paste the public Notion page URL of your template into the designated field <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. Click "Load page" to preview the document <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### 4. Generate Notion API Key
*   **Add API Key:** Click the link to add a Notion API key <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Create New Integration:** In the Notion window that opens, click "New integration," provide a name (e.g., "new key"), choose your account, and save <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Copy API Key:** Go to "Integrations," click on your newly created key, select "Show," and copy the full API key <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   **Paste API Key:** Paste the copied API key into the "API key" field on pdf4notion.com <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### 5. Provide Database URL
*   **Copy Database URL:** Go back to your Notion database and copy its URL from the browser's address bar <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   **Paste Database URL:** Paste this URL into the "Database URL" field on pdf4notion.com <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Load Database:** Click "Load database" <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### 6. Configure Generation Settings
*   **File Naming:** Choose a column from your database (e.g., "invoice number") to use as the name for the generated PDF files <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Row Selection:**
    *   You can choose to [[generating_pdf_documents_from_notion_database_rows | generate documents]] for "all rows" <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
    *   Alternatively, you can specify a "custom range" (e.g., rows 4-7) or select specific rows <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Layout Settings:** Adjust paper size, orientation (portrait/landscape), and specify which pages to print if your template has multiple pages <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

### 7. Generate and Save PDFs
*   **Generate PDF:** Click "Generate PDF" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   The system will process each record, populating the template with data from your database properties <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   **Save Files:** As each PDF is generated, you will be prompted to save it to your desired location, named according to your selected database column <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### Verification
Once generated, you can open the PDF documents to verify that the information has been correctly pulled from your Notion database into the template <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. For instance, an invoice for "Alice Johnson" with "May 1" date and "May 15" due date will precisely match the corresponding database record <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

### Important Reminders
*   Your Notion page containing the template *must* be shared and publicly accessible <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   Your Notion database *must* be connected to the API key you created <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   If your database uses relational properties, ensure that *all related databases* are also connected with the *same API key* for seamless data fetching <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

This comprehensive approach allows for efficient [[generating_pdf_invoices_from_notion | generation of PDF invoices]] or any other documents directly from your Notion databases, making it a powerful tool for [[setting_up_and_managing_notion_databases_for_pdf_generation | managing and generating documents]] in bulk.