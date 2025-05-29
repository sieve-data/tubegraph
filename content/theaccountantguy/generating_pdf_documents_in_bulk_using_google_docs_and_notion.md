---
title: Generating PDF documents in bulk using Google Docs and Notion
videoId: oprL9NBoj8o
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to help users [[generating_pdf_documents_in_bulk_with_notion | generate PDF documents in bulk]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It achieves this by using a Google Document as a template and a Notion database to hold the variable elements that will replace placeholders in the Google Document <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Core Functionality

The process involves three main steps <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>:
1.  Adding a Google Document template.
2.  Adding a Notion database.
3.  Clicking "Export PDF" to [[pdf_document_creation_with_notion_and_pdf_output | generate the documents]] <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Step-by-Step Guide

### 1. Accessing PDF Output

*   Navigate to PDFoutput.com <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   Log in to access the interface <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

### 2. Adding and Preparing a Google Document Template

You can add a Google Document in two ways <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>:
*   **Create a blank document**: This option allows you to start from scratch <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. After creation, you should rename the document (e.g., "Invitation Template") <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Choose an existing document**: Select any document already present in your Google Drive <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

Once the document is added, you will prepare it as a template <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>:
*   Add your content to the document <a class="yt="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   Identify fields that need to be replaced with dynamic data (e.g., `salutation` and `customer name`) <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### 3. Connecting and Preparing a Notion Database

*   Click on "Add Notion database" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   Connect with your Notion credentials and select the specific pages from your Notion account that you want to integrate <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **Create a new Notion database**: If you don't have one, create a new page in Notion, choose a table, and rename it (e.g., "Invitation List") <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Add properties (columns)**: Add columns in your Notion database that correspond to the dynamic fields in your Google Document template (e.g., `Salutation` and `Customer Name`) <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   **Populate the database**: Enter the data for each row in your Notion database <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **Refresh properties**: If new columns are added to Notion, click "refresh properties" in PDF Output to fetch the newly added columns <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

### 4. Linking Notion Properties to Google Doc Placeholders

*   In PDF Output, click on a Notion property (e.g., `Salutation`). This action copies the property's placeholder value <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   Go to your Google Document template within the PDF Output interface and paste the copied placeholder into the desired location <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   Repeat this for all dynamic fields (e.g., `Customer Name`) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   The tool will then replace these placeholders with the actual values from each row of your Notion database when [[generating_pdf_documents_from_notion_database_rows | generating PDF documents]] <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### 5. Exporting PDFs

*   Once the template and database are connected and properties mapped, click "Export PDF" <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   Complete any required Google authentication <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   The tool will read each row from the Notion database and [[generating_pdf_documents_using_notion | generate a separate PDF document]] for each <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. The generated PDFs will be automatically downloaded <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

## Additional Features and Tips

*   **Connected Databases**: If your primary Notion database is connected to other databases, ensure you choose all relevant connected databases when approving the database list <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Pre-built Templates**: PDF Output provides various pre-built templates (e.g., an [[generating_pdf_invoices_from_notion | invoice template]]) that you can use <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. You can make a copy of these templates to your Google Workspace or copy their content to a blank document <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   **Search and Sorting**: The interface includes options to search for particular properties and sort values for easier management <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

For any questions, you can reach out to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.