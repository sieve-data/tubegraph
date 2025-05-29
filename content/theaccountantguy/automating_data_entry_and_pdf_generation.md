---
title: Automating data entry and PDF generation
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

This article outlines a process for [[automating_pdf_generation_with_userdefined_templates | automating PDF generation with user-defined templates]] and data entry using a Notion database and the PDF Output tool. This method allows for the [[bulk_pdf_document_generation | bulk PDF document generation]] of unique documents from database rows without manual input for each file <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## The Challenge

Manually creating PDF documents for each row of data in a database, such as application forms, can be time-consuming, requiring individual data entry and export <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a> <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. The described solution addresses this by automating the process for documents like application forms, tracking requirements from candidate profiles to education details <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Solution Components

### Notion Database

A Notion database serves as the data source. For instance, an "Application Form Database" tracks various candidate details <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a> <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

### Application Form Template

A template is created to match the database structure. This template includes placeholder fields (e.g., `full name`, `date of birth`, `gender`, `phone number`) enclosed in curly brackets `{}`. These placeholders directly correspond to column names in the database <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a> <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

### PDF Output Tool

PDF Output is an online tool used to generate documents in bulk from a Notion database <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a> <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

## Preparing the Notion Database

To prepare the database for PDF generation:

1.  **Add the Template to Database Rows:**
    *   For each row in the database, open the entry and scroll to the bottom <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
    *   Copy the content of the pre-designed application form template <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
    *   Paste the template into the empty section of each row <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. This ensures that the template is present within each database entry <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
2.  **[[pdfoutput_software_setup_for_document_generation | Setting Up a Default Template]] (Automation for New Entries):**
    *   To avoid manually copying the template for new rows, create a default template within the Notion database <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a> <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
    *   Click the dropdown next to "New" and select "New template" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a> <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
    *   Name the template (e.g., "Applicant Name") and paste the template content into it <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a> <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
    *   Click the three dots next to the template name, select "Set as default," and choose "For all views and application form database" <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a> <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Now, any new data added to the database will automatically include the template <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a> <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## [[pdfoutput_software_setup_for_document_generation | Setting Up PDF Output Software]]

To connect the Notion database with PDF Output:

1.  **Copy Database URL:** Copy the URL of your Notion database from the browser's address bar <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a> <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
2.  **Generate and Connect API Key:**
    *   In PDF Output, the database must be connected via an API key <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
    *   Click the "click here to add API key" link, which directs to Notion's API key settings <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   Create a new integration, name it, choose your workspace, and save <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a> <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
    *   Copy the "Internal Integration Secret" key <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a> <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
    *   Paste this key into the designated field in PDF Output <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
3.  **Connect Database to API Key:**
    *   In your Notion database, click the three dots, then "Connections" <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a> <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
    *   Search for and select the API key (e.g., "new key") you just created, then confirm <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a> <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
4.  **Publish the Notion Database:**
    *   For PDF Output to access the database, it must be published <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
    *   Click "Share," then "Publish," and confirm "Publish" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a> <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

## [[bulk_pdf_document_generation | Generating PDF Documents]]

Once the setup is complete:

1.  **Load Database:** In PDF Output, paste the database URL and click "Load database" <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a> <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
2.  **Select Naming Column:** Choose a column (e.g., "Full Name") from the dropdown to be used as the reference for naming the generated PDF files <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a> <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
3.  **Choose Rows for Generation:** Select whether to generate PDFs for "all rows," a "range of rows," or "custom rows" <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a> <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
4.  **Generate PDFs:** Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   The tool will display each generated PDF, automatically populating the template placeholders with corresponding data from each database row <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a> <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
    *   Users can adjust settings like paper size and layout on the right side <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a> <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
    *   Save each generated PDF file (e.g., to desktop) <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### Checking the Output

The generated PDF files will be named according to the selected naming column (e.g., "Carol Davis.pdf," "Bob Williams.pdf") <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. The content will be clean and professional, with all placeholder data correctly replaced <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a> <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

## Flexibility and Other Use Cases

This method is applicable for [[generating_pdf_documents_for_business_purposes | generating PDF documents for business purposes]] or personal use, including:
*   [[Using PDF Output software for invoice creation | Creating invoices]] from an invoices database <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   [[generating_sales_receipts_pdf_documents_using_online_tools | Generating sales receipts PDF documents using online tools]].
*   [[generating_pdf_documents_for_purchase_orders | Generating PDF documents for purchase orders]].

It's not mandatory for placeholder text elements to strictly match the content inside the page; the tool will still read the entire page content and generate the documents <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a> <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. Users can include any notes, lectures, or handy information on the pages for generation <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

### Alternative Method: Using a Template Page URL

Instead of embedding the template within each database row, you can use a standalone template page:

1.  **Copy Template Page URL:** Copy the URL of the standalone template page <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
2.  **Paste into PDF Output:** Paste this URL into the "notion page" field in PDF Output <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a> <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
3.  **Load Page and Database:** Click "Load page" to display the template content <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. Then, click "Load database" and proceed with selecting the naming column and generating PDFs as usual <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

This provides two flexible ways to ensure the template is available for the PDF generation process <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.

## Additional Resources

The PDF Output homepage offers a "Contact" section for support and queries <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a> <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. Additionally, a "Template" section provides predefined templates that can be directly copied along with their corresponding databases to get started quickly <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a> <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. Each template often includes a "how-to-use" video <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.