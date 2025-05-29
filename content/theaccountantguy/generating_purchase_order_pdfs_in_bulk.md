---
title: Generating purchase order PDFs in bulk
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 
The [[using_pdfoutput_tool_for_bulk_pdf_generation | PDFoutput tool]] allows users to [[generating_and_exporting_pdf_documents_for_purchase_orders | generate purchase order PDF documents]] in bulk using a Notion page and a Notion database <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

### Template Structure
The purchase order template includes fields such as the purchase order number, date, supplier, and buyer name <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. These fields, placed inside curly braces (e.g., `{{purchase order number}}`, `{{date field}}`), act as placeholders <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. They will be dynamically replaced with data from a Notion database during PDF generation <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

### Notion Database
The Notion database is structured to correspond with the template's fields <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. It contains properties like `purchase order number`, `date field`, `supplier name`, and `buyer name` <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. Each row in the database represents a unique purchase order, and a separate PDF document will be generated for each row <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Steps to [[generating_purchase_order_pdfs_using_notion | Generate Purchase Order PDFs]]

#### 1. Log In to PDFoutput.com
Access the platform by logging in at PDFoutput.com <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. The initial interface prompts users to connect a Notion database and template <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

#### 2. Access and Duplicate Templates
*   Navigate to the "template section" via the sidebar navigation <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   Search for "purchase order" to find the relevant template <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   Click on both the "database link" and the "template link" provided <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   Select "Start with this template" to duplicate both the database and the template into your Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Choose your workspace and click "Add to private" <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

#### 3. Connect Notion Database and Template
*   Return to PDFoutput and click "click here to add database" or "click here to add template" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   Select your Notion workspace, choose the duplicated database and template from the list of pages <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   Click "Allow access" to establish the connection <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   Once authenticated, the database and template will appear on the PDFoutput screen <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. If they don't appear, click "refresh" <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

#### 4. Define Output Name and Map Elements
*   Provide a name for the PDF output, e.g., "purchase order" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   Click "next" <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   The tool will load database properties (left side) and template elements (right side) <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Automatic Mapping**: If the naming convention in the database exactly matches the placeholders in curly braces in the template, elements will map automatically <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Manual Mapping**: If elements are not automatically mapped (appear in gray), click on the element and manually choose the corresponding field from the template <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

#### 5. Create and Download PDFs
*   Click "Create PDF" <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. The tool will process and generate a PDF for each row in the database <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   Once processing is complete, click "Preview sample" to review one of the generated documents <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   Click "Download all" to download all the generated PDF files <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### Customizing the Template
The provided template is customizable; users can edit, modify, or make any changes once it's duplicated <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Ensure that any data to be pulled from the database remains inside curly braces and follows the exact same naming convention in both the template and the database <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

### Post-Generation Options and Features

#### Connections
The "Connections" option on the right sidebar shows recently created connections, such as "purchase order" <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Clicking on a connection automatically loads the associated database and template, eliminating the need to re-enter them for future exports <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

#### Upgrade
Users on the free plan will see a "Made with PDFoutput" watermark on exported documents <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. Upgrading to a paid subscription removes the watermark and any limits on PDF generation <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

#### Settings
*   **Page Format**: The default page format is A4 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Add More Templates/Databases**: Users can click here to add additional databases and templates beyond the initial setup <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

#### Feedback and Help
*   **Feedback**: A feedback option is available for reporting difficulties or issues <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Help**: The help section includes a video demonstrating how to use custom templates from scratch, which is useful if users don't want to use predefined templates <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

### Important Considerations

*   **Relation Properties**: If using Notion relation properties in the database, ensure access is granted to those related databases during the connection process to ensure all elements are correctly reflected in the PDF output <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

For further questions, contact notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.