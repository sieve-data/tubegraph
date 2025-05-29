---
title: Steps to set up and export PDFs using PDF Output
videoId: oprL9NBoj8o
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to [[using_pdfoutput_for_bulk_document_generation | generate PDF documents in bulk]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It leverages a Google Document as a template and a Notion database to hold the elements that will replace placeholders in the Google Document <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Getting Started with PDF Output

To begin, you need to log in to [[using_pdfoutputcom_for_bulk_pdf_generation | PDF output.com]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Upon logging in, you will see an interface that guides you through the process <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. The general flow involves adding a Google Document, adding a Notion database, and then clicking "Export PDF" to [[exporting_and_managing_generated_pdf_documents | generate the documents]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Adding a Google Document (Template)

The first step is to add your Google Document, which serves as the template <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. There are two methods for adding a Google Document:

1.  **Create a blank document from scratch** <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
2.  **Choose an existing document from Google Drive** <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

For a new document, select the "create document" button and choose the Google account you wish to connect <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. Once created, rename the document as needed (e.g., "Invitation Template") <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. You can then paste content into this template, identifying fields that need to be replaced, such as `customer name` or `salutation` <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## Adding a Notion Database (Data Source)

Next, you need to connect a Notion database that will hold the dynamic content for your documents <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

1.  Click on "add notion database" to connect your Notion credentials <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Select the specific Notion workspace and pages you want to grant access to <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
3.  If you haven't already, create a new database in Notion (e.g., "Invitation List") <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
4.  Once the database is created in Notion, return to PDF Output, select the database, and click "allow access" <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
5.  Add columns to your Notion database that correspond to the placeholders in your Google Document template (e.g., "salutation", "customer name") <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
6.  Populate these columns with the necessary data for each document you wish to generate <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
7.  If you add new columns in Notion, click "refresh properties" in PDF Output to fetch the new properties <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## Mapping Fields

With both the Google Document template and Notion database connected, you can now map the fields:

1.  In PDF Output, click on a property name (e.g., "salutation") from your Notion database to copy its value <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
2.  Go to your Google Document template and paste the copied property value into the corresponding placeholder <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
3.  Repeat this process for all dynamic fields (e.g., "customer name") <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

When you proceed to generate PDFs, PDF Output will replace these pasted values with the actual data from your Notion database rows <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

## [[exporting_and_managing_generated_pdf_documents | Exporting PDFs]]

Once your template and database are set up and linked, you can [[automating_document_exports_using_pdf_output | export your PDFs]]:

1.  Click the "export PDF" button <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
2.  Complete the Google authentication process if prompted <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
3.  PDF Output will then read each row from your Notion database and generate a separate PDF document for each one <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. The generated PDFs will be automatically downloaded <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

### Verification of Generated PDFs

You can open your downloads folder to view the generated PDFs <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. Each PDF will reflect the specific data from its corresponding row in the Notion database <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Additional Features and Tips

*   **Connected Databases:** If your Notion database has connections to other databases, ensure you choose all connected databases while approving the Notion database list <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Pre-made Templates:** PDF Output offers various pre-made templates, such as an [[generating_pdf_invoices_using_pdfoutput | invoice template]] <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. You can click on these to preview them <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   **Using Pre-made Templates:**
    *   **Make a Copy:** Click "File" > "Make a copy" to save a template to your Google Workspace <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
    *   **Copy Content:** Alternatively, select all content (`Ctrl+A`), copy it (`Ctrl+C`), create a blank Google Document, and paste the content there (`Ctrl+V`) <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
*   **Search and Sort:** The interface includes search properties to find specific data and a sorting window to organize values <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Refresh Properties:** Remember to use the "refresh properties" option if you make changes to your Notion database columns <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

For any questions, you can reach out via email to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.