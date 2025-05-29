---
title: Creating and using templates for PDF generation
videoId: oprL9NBoj8o
---

From: [[theaccountantguy]] <br/> 

[[using_templates_to_automate_pdf_creation | PDF Output]] is a tool designed for [[using_templates_to_automate_pdf_creation | generating PDF documents in bulk]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. It leverages a Google Document as a [[customizing_templates_for_pdf_document_generation | template]] and a Notion database to supply the data for replacement <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Getting Started
To begin, navigate to PDFoutput.com and log in <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The interface will prompt you to add a Google Document (serving as your [[customizing_templates_for_pdf_document_generation | template]]) and a Notion database <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. After these are connected and configured, you can click "export PDF" to generate documents <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## [[creating_and_utilizing_pdf_templates | Creating and Utilizing PDF Templates]] with Google Docs

There are two primary methods for adding a Google Document as a [[customizing_templates_for_pdf_document_generation | template]]:
1.  **Create a blank document from scratch** <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
2.  **Choose an existing document** from your Google Drive <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Creating a New Template
To create a blank document:
1.  Click the "create document" button <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
2.  Select the Google account you wish to connect <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
3.  Once the blank document is created (e.g., "PDF output new document"), rename it to suit your needs, such as "invitation template" <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
4.  Populate this document with your desired content. This can include text, formatting, and placeholders for dynamic data <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
5.  Identify the fields in your [[customizing_templates_for_pdf_document_generation | template]] that will be replaced by data from your database. For instance, if [[using_templates_in_pdf_output_for_generating_receipts | generating receipts]], you might have "customer name" or "salutation" as fields <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### Linking an Existing Template
If you already have a Google Document prepared as a [[customizing_templates_for_pdf_document_generation | template]]:
1.  Click "add Google Document" <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
2.  Select your Google account <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
3.  You can browse your Google Drive for the document or use the search bar to find it by name (e.g., typing "invitation" to find "invitation template") <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
4.  Double-click the desired document to add it <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

### Using Pre-Existing Templates Provided by PDF Output
PDF Output also provides a library of pre-existing [[customizable_pdf_templates | templates]]:
*   Click on the templates section to view available options <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
*   Once you click on a [[customizable_pdf_templates | template]] (e.g., an invoice [[customizable_pdf_templates | template]]), it will appear on your screen <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   To use it, you can either:
    *   Go to "File" > "Make a copy" to save it to your Google Workspace <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
    *   Select all content (Ctrl+A or Cmd+A), copy it (Ctrl+C or Cmd+C), create a new blank document within PDF Output, and paste the content there (Ctrl+V or Cmd+V) <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

## [[managing_templates_and_databases_in_pdfoutput | Managing Templates and Databases]]

### Connecting a Notion Database
1.  Click "add notion database" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Authenticate with your Notion credentials <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
3.  Select the specific Notion database pages you want to use. If you haven't created one, you'll need to do so in Notion first (e.g., create a new page, select "table," and rename it "invitation list") <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
4.  Once created in Notion, the database (e.g., "invitation list") should appear in PDF Output. Select it and click "allow access" <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
5.  This connects your Notion database to [[using_templates_to_automate_pdf_creation | PDF Output]], displaying its properties (columns) <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### [[mapping_database_elements_to_templates_for_pdf_generation | Mapping Database Elements to Templates]]
After connecting your Google Document [[customizing_templates_for_pdf_document_generation | template]] and Notion database:
1.  Ensure your Notion database contains the columns that correspond to the dynamic fields in your Google Document. For example, if your template has "customer name" and "salutation," your Notion database should have matching columns <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
2.  If you add new columns to your Notion database, click "refresh properties" in PDF Output to fetch them <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
3.  In PDF Output, click on the database property (e.g., "salutation") to copy its placeholder <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
4.  Go to your Google Document [[customizing_templates_for_pdf_document_generation | template]] and paste this placeholder where you want the data to appear (e.g., replace "Mr" with the "salutation" placeholder) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
5.  Repeat this process for all dynamic fields (e.g., "customer name") <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
    > [!NOTE]
    > The changes you make in PDF Output (e.g., pasting placeholders) are reflected live in the linked Google Document <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### [[managing_connections_and_templates_in_pdf_output | Managing Connections and Templates]]
*   **Searching Properties:** Use the search properties feature to find any particular database property <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Sorting:** The sorting window allows you to sort all values for your use case <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Refreshing Properties:** This is crucial for updating the list of properties available from your database after adding new columns <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## [[using_templates_to_automate_pdf_creation | Generating PDFs]]

1.  Once your [[customizing_templates_for_pdf_document_generation | template]] is ready and your database is connected with mapped fields, click "export PDF" <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
2.  You may need to complete Google authentication <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
3.  [[using_templates_to_automate_pdf_creation | PDF Output]] will read each row in your database and generate a separate PDF document for each one, automatically downloading them <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
    *   For example, if you have three customer entries in your database, three customized PDF invitation documents will be generated, each personalized with the correct salutation and customer name <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

> [!TIP]
> If your Notion database is connected to other secondary databases, ensure you choose all relevant databases during the connection process to allow for comprehensive data retrieval <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

For further assistance, you can reach out to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.