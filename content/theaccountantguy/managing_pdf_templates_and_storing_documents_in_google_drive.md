---
title: Managing PDF templates and storing documents in Google Drive
videoId: 6PR3AESuBoA
---

From: [[theaccountantguy]] <br/> 

[[automating_pdf_generation_with_userdefined_templates | PDFoutput.com]] is a tool designed to [[automating_pdf_generation_with_userdefined_templates | generate PDF documents]] in bulk by [[using_google_docs_as_a_template_for_pdf_creation | utilizing Google document as a template]] with the assistance of a [[using_google_documents_and_notion_for_pdf_generation | Notion database]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This platform allows users to automate the creation and storage of personalized [[creating_pdf_documents_for_business_needs | PDF documents]] directly into their Google Drive.

## Getting Started with PDFoutput.com

To begin, navigate to [[automating_pdf_generation_with_userdefined_templates | PDFoutput.com]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Click on "create PDF" and sign in using a Google account <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. It is necessary to enable the checkbox granting access to specific files for PDFoutput.com to function <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. After enabling access, click "continue" to be redirected to the homepage <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Utilizing Google Documents as Templates

While [[automating_pdf_generation_with_userdefined_templates | PDFoutput.com]] offers certain pre-populated [[automating_pdf_generation_with_userdefined_templates | PDF templates]] <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, users can also use their own raw [[using_google_docs_as_a_template_for_pdf_creation | Google documents]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

1.  **Select Google Document**: Click the link next to the Google document option to view all documents listed on your Google Drive <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
2.  **Choose Document**: Select the desired Google document to serve as the template, for example, an "invitation letter PDF output invitation letter" <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This document will be loaded for your use <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. The template should include placeholders (e.g., first name, last name) that will be dynamically replaced with data from a [[using_google_documents_and_notion_for_pdf_generation | Notion database]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Connecting to a Notion Database

[[creating_and_using_notion_templates_for_pdfs | Notion]] databases provide the dynamic data needed to populate [[automating_pdf_generation_with_userdefined_templates | Google Docs templates]] <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

1.  **Select Notion**: From the dropdown menu in [[automating_pdf_generation_with_userdefined_templates | PDFoutput.com]], select "Notion" <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
2.  **Retrieve Database URL**: Click the provided link to open your [[creating_and_using_notion_templates_for_pdfs | Notion workspace]] <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
    *   Create a new page, for example, "PDF output database" <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
    *   Create an inline database by typing `/database` <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   Rename columns as needed (e.g., "first name," "last name") <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
    *   Populate the database with data (e.g., "Priya Sharma," "Miller Stark," "John roads") <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
    *   Ensure you are in the database view <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
    *   Click "share" and then "copy link" to obtain the database URL <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Paste this URL into the designated field in [[automating_pdf_generation_with_userdefined_templates | PDFoutput.com]] <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
3.  **Generate API Key**: Click "add API key" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    *   Create a new key, naming it (e.g., "notion PDF output connection") <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
    *   Select the particular account and click "save" <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
    *   Go back to the API key created, click "show," copy the key value, and paste it into [[automating_pdf_generation_with_userdefined_templates | PDFoutput.com]] <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
4.  **Connect Database to API Key**: In Notion, click the three dots on the database page, then "connections," and search for "PDF output connection" to connect the database to the API key <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## Configuring PDF Generation and Storage

Once the [[using_google_docs_as_a_template_for_pdf_creation | Google Doc template]] and [[using_google_documents_and_notion_for_pdf_generation | Notion database]] are linked, configure the output settings.

1.  **Load Properties**: Click "load properties" in [[automating_pdf_generation_with_userdefined_templates | PDFoutput.com]] to fetch all properties from the Notion database <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
2.  **Define Output File Name**: Select a Notion property (e.g., "first name") from the dropdown to name the generated PDF files <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
3.  **Choose Output Folder**:
    *   **Google Drive**: Select "Google drive" to save the files to your Google Drive <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
        *   Create a new folder in Google Drive (e.g., "invitation documents") <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
        *   In [[automating_pdf_generation_with_userdefined_templates | PDFoutput.com]], click "add folder" and select the newly created Google Drive folder <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
    *   **Downloads Folder**: Alternatively, choose the "downloads folder" option to save files directly to your desktop <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
4.  **Map Properties to Template**: Replace placeholders in the [[using_google_docs_as_a_template_for_pdf_creation | Google Doc template]] (e.g., "first name," "last name") with the corresponding properties fetched from the [[using_google_documents_and_notion_for_pdf_generation | Notion database]] <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Simply copy the property name from the fetched list and paste it into the template <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

## Generating and [[exporting_and_managing_pdf_documents_for_business | Exporting and Managing PDF Documents]]

With all settings configured, the [[automating_pdf_generation_with_userdefined_templates | PDF generation]] process can begin.

1.  **Export PDF**: Click "export PDF" to start generating documents <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The "PDF generated count" will increase as documents are created <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
2.  **Verify Documents**: Once generation is complete, click "view in Google drive" to open the folder containing the newly created PDFs <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. The documents will show the placeholders replaced with the correct data from the [[using_google_documents_and_notion_for_pdf_generation | Notion database]] <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

### Additional Features

[[automating_pdf_generation_with_userdefined_templates | PDFoutput.com]] also includes:
*   **Predefined Templates**: A selection of ready-to-use [[automating_pdf_generation_with_userdefined_templates | templates]] <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **History**: An option to view all previously generated documents <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Upgrade Options**: Ability to upgrade to a specific plan <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

For any questions or queries, users can contact support via the "contact section" <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.