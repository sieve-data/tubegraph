---
title: Exporting and managing multiple PDF documents
videoId: XPSQBVl9mKs
---

From: [[theaccountantguy]] <br/> 

PDF Output is a tool designed to [[generating_and_downloading_pdf_documents_in_bulk | generate PDF documents in bulk]] using a Notion database and a Notion template <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This process involves replacing placeholder elements within a template with corresponding data from a Notion database <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. For instance, an invoice template with fields like "invoice number," "date," and "due date" can be populated automatically from database rows <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Each row of information from the database will be fetched to replace placeholder text elements in the template, resulting in the creation of PDF documents <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## How to Generate and Export PDFs

To [[generating_and_downloading_pdf_documents_in_bulk | generate and download PDF documents in bulk]] using PDF Output, follow these steps:

### 1. Accessing PDF Output and Templates
*   Navigate to PDF Output's website <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   Once logged in, go to the "Templates" section <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   You can search, sort, or filter the available templates to find one that suits your needs <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### 2. Duplicating Templates to Notion
*   Select a template (e.g., an invoice template) and click the "Download link" next to it <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This opens the template in a new tab <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   To use a template, you must duplicate it to your own Notion workspace by clicking "Start with this template" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   Choose the desired Notion workspace and click "Add to private" to add the template and its associated database (e.g., a professional invoice database) to your Notion account <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### 3. Connecting Notion to PDF Output
*   Return to PDF Output and go to "Settings" <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   Click "click here to add templates" to redirect to your Notion workspace <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
*   Select the same Notion account where you duplicated the templates <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   Choose the specific page containing the template and database (e.g., "Invoice PDF Generator") and click "Allow access" <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. This will authenticate and redirect you back to PDF Output <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

### 4. Selecting Database and Template
*   On PDF Output, select the correct Notion database (e.g., "Professional Invoice Database") and the specific Notion template (e.g., "Invoice Template") that you duplicated <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   Give your export a name (up to 20 characters) and click "Next" <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

### 5. Mapping Notion Properties to Template Elements
*   The system will load all elements from your database and template <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   On the left, you'll see "Notion Properties" (columns from your database), and on the right, "Template Elements" (placeholders from your template) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   Ensure that the names of your Notion properties exactly match the names of the template elements for automatic mapping <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   If any elements are unmapped (indicated in gray), you can manually map them by clicking on the element and selecting the corresponding Notion property <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
*   You can use search, sort, and filter options to manage mappings <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. All mapped elements will appear in green <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### 6. Exporting and Managing PDF Status
*   Before [[exporting_and_downloading_pdf_documents | exporting and downloading PDF documents]], check your Notion database for a "PDF Status" column <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   For a row to be generated as a PDF, its "PDF Status" checkbox must be *unchecked* <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   The first time you integrate, this column is unchecked by default <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. After documents are generated, it will automatically be checked <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   Click "Export" to begin processing the documents <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. As each document is generated, a tick will appear in the "PDF Status" column for that row in your Notion database <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

### 7. Previewing and Downloading Generated PDFs
*   Once the export is successful, you have two options: "Preview Sample" or "Download All documents" <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   "Preview Sample" shows one generated PDF to verify correct data replacement <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   "Download All" will [[exporting_and_downloading_generated_pdf_documents | export and download all generated PDF documents]] from the database in a single go <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. Each row from the database will result in a separate PDF file, with corresponding data mapped correctly <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

## Managing Connections for Repeat Exports

After generating an export, the configuration is saved as a "Connection" <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   You can find these connections in the "Connections" window <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   To re-use the same database and template, simply select the saved connection <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. It will automatically load all previously configured elements <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   To regenerate specific rows, ensure their "PDF Status" checkboxes in Notion are *unchecked* before clicking "Next" and exporting again <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. This feature is crucial for [[exporting_and_tracking_generated_pdf_documents | exporting and tracking generated PDF documents]] by managing which files need to be re-exported.

## Customization and Additional Features

### Customizing Templates
*   Users can [[customizing_and_exporting_generated_pdf_files | customize and export generated PDF files]] by modifying the Notion template <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   You can add, delete, or modify any elements within the template, as long as the placeholder names (inside curly braces) exactly match the column names in your Notion database <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Subscription Plans
*   Paid plans remove watermarks from generated PDF outputs <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. New users on free plans will see a watermark <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   The "Upgrade Subscription" option is available to change plans <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

### Page Format
*   Under the "Settings" tab, you can choose from various page formats (e.g., A4, Letter) for your PDF documents <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

### Feedback and Support
*   A "Feedback" option is available for questions or issues, directly sending a message to support <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   The "Help" window provides access to demonstration videos for guidance <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.