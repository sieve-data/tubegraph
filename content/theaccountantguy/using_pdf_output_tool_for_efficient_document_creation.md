---
title: Using PDF Output tool for efficient document creation
videoId: oprL9NBoj8o
---

From: [[theaccountantguy]] <br/> 

[[features_and_functionalities_of_pdfoutput_tool | PDFOutput]] is a straightforward tool designed to [[bulk_pdf_document_creation | generate PDF documents in bulk]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. It leverages a Google Document as a template and a Notion database to hold the dynamic elements that replace placeholders in the Google Document <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## [[steps_to_set_up_and_export_pdfs_using_pdf_output | Steps to Set Up and Export PDFs]]

The general process for [[automating_document_exports_using_pdf_output | automating document exports]] using [[features_and_functionalities_of_pdfoutput_tool | PDFOutput]] involves three main steps:
1.  Adding a Google Document <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
2.  Adding a Notion database <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
3.  Clicking "Export PDF" to generate the documents <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

### Initial Setup and Login

To begin, users need to log in to [[using_pdfoutputcom_for_bulk_pdf_generation | PDFoutput.com]] <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. After logging in, an interface will appear on the screen <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

### Adding a Google Document Template

[[features_and_functionalities_of_pdfoutput_tool | PDFOutput]] allows two methods to add a Google Document as a template:
*   **Creating a blank document from scratch** <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Choosing an existing document from Google Drive** <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

When creating a blank document, users select the Google account to connect <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. The newly created document will be named "PDF output new document" by default and should be renamed as per requirements, for example, "Invitation Template" <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The template should contain placeholder fields, such as `{{salutation}}` and `{{customer_name}}`, to be replaced by data from the Notion database <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### Adding a Notion Database

The next step is to add a Notion database by clicking "add notion database" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This requires connecting to Notion credentials and selecting the specific pages or databases from the Notion account <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. If a database doesn't exist, one can be quickly created in Notion, for instance, a table named "invitation list" <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. Once created, the database will be visible in [[features_and_functionalities_of_pdfoutput_tool | PDFOutput]] and can be selected to allow access <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

The Notion database should include columns corresponding to the placeholders in the Google Document template, such as "customer name" and "salutation" <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. If new columns are added to the Notion database, clicking "refresh properties" in [[features_and_functionalities_of_pdfoutput_tool | PDFOutput]] will automatically fetch these new properties <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

### [[syncing_and_exporting_documents_using_pdf_output | Syncing and Exporting Documents]]

Once both the Google Document template and the Notion database are connected, the values from the Notion database properties can be copied and pasted into the corresponding placeholders in the Google Document <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. For example, clicking on "salutation" copies its value, which can then be pasted into the `{{salutation}}` placeholder in the Google Doc <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

After the template is set up with placeholders linked to Notion properties, click "Export PDF" <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. This will initiate Google authentication, which must be completed <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. Once authenticated, [[features_and_functionalities_of_pdfoutput_tool | PDFOutput]] will read each row of data in the Notion database and generate a separate PDF document for each, automatically downloading them <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

## [[features_and_functionalities_of_pdfoutput_tool | Features and Functionalities of PDFOutput]]

*   **Real-time Editing**: Changes made in [[features_and_functionalities_of_pdfoutput_tool | PDFOutput]] are reflected in the connected Google Document <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   **Handling Connected Databases**: If a Notion database is connected to other databases, ensure all connected databases are chosen during the initial Notion database selection to allow proper data flow <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   [[utilizing_predefined_pdf_templates_for_efficient_workflow | Utilizing predefined PDF Templates]]: [[features_and_functionalities_of_pdfoutput_tool | PDFOutput]] provides a variety of predefined templates, such as an invoice template <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. Users can make a copy of these templates to their Google Workspace or copy the content and paste it into a new blank document <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   **Search Properties**: A search bar allows users to find specific properties within their linked Notion databases <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Sorting**: The tool includes a sorting window to organize values <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Refresh Properties**: As noted earlier, this feature updates the available properties from the Notion database if new columns are added <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

For assistance, users can reach out to notionforuse@gmail.com <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.