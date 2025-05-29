---
title: Generating bulk PDF documents using Google Docs and Notion
videoId: oprL9NBoj8o
---

From: [[theaccountantguy]] <br/> 

PDFOutput is a tool designed to [[generating_pdf_documents_in_bulk_using_notion_and_pdfoutput | generate PDF documents in bulk]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It achieves this by using a Google Document as a template and a Notion database to supply the data for replacement elements within the document <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Core Components

The process relies on two main components:
*   **Google Document**: Serves as the template for the PDF documents <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.
*   **Notion Database**: Holds the dynamic elements that will replace placeholders in the Google Document <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Workflow

To [[generating_pdfs_from_notion_using_pdfoutput | generate PDFs from Notion using PDFOutput]], follow these steps:

### 1. Log in to PDFOutput
Access the tool by logging in at PDFOutput.com <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The interface will be visible upon successful login <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

### 2. Add a Google Document
You can add a Google Document in two ways <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>:
*   **Create a blank document**: Start a new document from scratch <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   **Choose an existing document**: Select a document already present in your Google Drive <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

Once created or selected, rename the document as needed <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This document will serve as your template, into which content can be pasted, for example, an invitation template <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Identify the fields within the template that need to be dynamically replaced, such as "customer name" or "salutation" <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### 3. Add a Notion Database
Click on "add notion database" to connect your Notion account <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   Select the specific Notion workspace <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   Choose the desired Notion database page, such as an "invitation list" <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a> <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   Allow access to connect the database to PDFOutput <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   If new columns (properties) are added to the Notion database, click "refresh properties" to ensure they are fetched by PDFOutput <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

### 4. Connect Notion Properties to Google Document Placeholders
Once the Notion database is connected, its properties (columns) will appear <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   Click on a property name from the Notion database (e.g., "salutation" or "customer name") to copy its value <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   Paste this copied value into the corresponding placeholder in your Google Document template <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. This establishes the dynamic link between the Notion data and the Google Doc template <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### 5. Export PDFs
With the template and database ready and connected, click "export PDF" <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. You may need to complete a Google authentication step <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. PDFOutput will then read each row of data from your Notion database and generate a separate PDF document for each one <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. The generated PDFs will be automatically downloaded <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

## Demonstration Example

In a demonstration, an "invitation template" Google Document was used with placeholders like `salutation` and `customer name` <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. A Notion database named "invitation list" was created with columns for "salutation" and "customer name" <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. Data for multiple customers (e.g., Mr. Bikash, Mr. Sanat, Mrs. Satabdi) was entered into the Notion database <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. By connecting these, three personalized invitation PDFs were generated <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

## Key Features and Tips

*   **Live Editing**: Changes made in PDFOutput are reflected in the connected Google Document <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   **Connected Databases**: If your Notion database has connections to other databases, ensure all relevant databases are chosen during the approval process to allow PDFOutput to fetch all necessary data <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Pre-made Templates**: PDFOutput offers various pre-made templates, such as an [[creating_invoices_in_bulk_using_notion | invoice template]] <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. You can make a copy of these templates in your Google Workspace or copy their content to a new blank document <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   **Search and Sort Properties**: The interface includes search capabilities to find specific properties and a sorting window to organize values <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Refresh Properties**: Always refresh properties after adding new columns to your Notion database <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

For questions or assistance, you can reach out to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.