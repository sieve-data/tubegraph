---
title: Using PDF output tool with Notion
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

The PDF Output tool facilitates [[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | generating PDF documents in bulk]] directly from a Notion database <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This process allows for the creation of individual PDF documents for each row of data in a Notion database, eliminating the need for manual data entry and export <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Notion Setup for PDF Generation

Before using PDF Output, the Notion database needs to be prepared:

### 1. Database Structure
An application form database is used as an example, tracking candidate profiles, education, and other application requirements <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Each row in this database represents a distinct application.

### 2. Creating a Notion Template
A specific template page is created that matches the columns in the Notion database <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Placeholders:** Data fields from the database, such as `Full Name`, `Date of Birth`, `Gender`, and `Phone Number`, are placed inside curly brackets (e.g., `{Full Name}`) within the template <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. These curly-bracketed fields correspond exactly to the column names in the Notion database <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### 3. Populating Database Rows with the Template
The template needs to be present within each row of the Notion database to enable PDF generation <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>:

#### Manually Populating Rows
1.  Open each database row <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
2.  Scroll to the bottom to find an empty section <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
3.  Copy all content from the prepared template page <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
4.  Paste the template content into the empty section of the database row <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
5.  Repeat this for all desired rows <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

#### Automating Template Population (Recommended)
To avoid manual copying for new rows <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>:
1.  Click the dropdown next to the "New" button in the Notion database <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  Select "New template" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
3.  Name the template (e.g., "Applicant Name") <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
4.  Paste the template content into this new template page <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
5.  Click outside to save the template <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
6.  Click the three dots next to the template name in the dropdown <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
7.  Select "Set as default" for "For all views" in the specific database <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
Now, any new row added to the database will automatically include the template content <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## [[integrating_notion_with_pdf_output_tool | Integrating Notion with PDF Output]]

The [[integrating_notion_with_pdf_output_tool | PDF Output tool]] requires specific setup to connect with your Notion database:

### 1. Signing into PDF Output
Access the PDF Output tool and sign in to your dashboard <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### 2. Copying Notion Database URL
Copy the URL of the Notion database from the top of the browser <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a> and paste it into the designated field in PDF Output <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

### 3. Connecting via Notion API Key
The Notion database must be connected to PDF Output using an API key <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>:
1.  In Notion, navigate to API key settings (usually by clicking a link provided by PDF Output, e.g., "Click here to add API key") <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
2.  Click "New integration" <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
3.  Add a new name and choose your workspace <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
4.  Once created, click on the integration and find the "Internal Integration Secret" <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
5.  Copy this secret key <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
6.  Paste the copied API key into the corresponding field in PDF Output <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

### 4. Connecting Database to API Key
The specific database page in Notion needs to be shared with the newly created API key:
1.  In Notion, click the three dots (`...`) at the top right of your database page <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
2.  Go to "Connections" <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
3.  Search for and select the name of the API key you just created (e.g., "new key") <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
4.  Click "Confirm" <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

### 5. Publishing the Notion Database
The database must be published to be accessible by PDF Output:
1.  Click "Share" on your Notion database page <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
2.  Click "Publish" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
This makes the database live and allows PDF Output to fetch its pages <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

## [[generating_pdf_documents_from_notion_database | Generating PDF Documents]]

Once the Notion setup and integration with PDF Output are complete, you can proceed with PDF generation:

### 1. Loading the Database in PDF Output
In PDF Output, click "Load Database" <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

### 2. Configuring PDF Naming and Row Selection
1.  **PDF Naming:** Select a Notion column (e.g., "Full Name") to use as the reference for naming the generated PDF files <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
2.  **Row Selection:** Choose to generate PDFs for "All rows," a "range of rows," or "custom rows" <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

### 3. Initiating PDF Generation
Click "Generate PDF" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. A preview window will appear, showing the populated PDF document for each selected row <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. The placeholder elements from the template are automatically replaced with data from the corresponding database row <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

### 4. Customization and Saving
On the right side of the preview, settings like paper size and layout can be adjusted <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. Click "Save" to download each generated PDF file <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. The files will be named according to the chosen column (e.g., "Carol Davis.pdf") <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

## Alternative Generation Method: Using a Standalone Template Page

Instead of embedding the template within each Notion database row, you can also link a standalone template page in PDF Output:
1.  Copy the URL of the main Notion template page <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
2.  In PDF Output, paste this URL into the "Notion Page" field <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
3.  Click "Load Page" to load the template document on the right side <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
4.  Then, proceed to "Load Database" and follow the same steps for generating PDFs, selecting a column for naming and choosing rows <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. This method still works even if the database rows don't contain the template content directly <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

## General Use Cases and Support

This process is applicable for [[creating_pdf_documents_from_a_notion_database | creating PDF documents from a Notion database]] for various purposes, such as [[integrating_notion_with_pdf_output_for_invoices | generating invoices]] from an invoice database <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

### Flexible Content
While using placeholder text with curly brackets (e.g., `{Full Name}`) is demonstrated for dynamic content replacement, it's not strictly mandatory <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. PDF Output can also read entire page content and generate documents from notes, lectures, or any other documentation within Notion pages <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

### Resources
*   **Templates:** PDF Output offers a template section with predefined templates that can be directly copied along with their databases to get started <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>. Each template includes a "how-to-use" video <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
*   **Contact:** For support or queries, a contact section is available on the PDF Output homepage <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.