---
title: Generating purchase order PDFs using Notion
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

This article outlines how to [[generating_purchase_order_pdf_documents_using_notion | generate purchase order PDF documents]] in bulk using a Notion page and a Notion database with PDFOutput.com <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Template and Database Setup

### Purchase Order Template
The purchase order template includes fields such as purchase order number, date, supplier, and buyer name <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Key items intended for replacement by database data are placed inside curly braces (e.g., `{purchase order number}`, `{date field}`) <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. These curly-braced items will be automatically replaced with corresponding values from the Notion database <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

### Notion Database
The Notion database is structured to mirror the fields defined in the template, using the exact same naming conventions <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Each row in the database represents a distinct purchase order, and values are placed for every field <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. PDFOutput will then [[bulk_pdf_generation_from_notion_databases | generate a PDF document for each of these rows]] <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Step-by-Step Process for PDF Generation

### 1. Log In to PDFOutput.com
Access the PDFOutput.com website and log in to your account <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. The interface will prompt you to connect a Notion database and a Notion template <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### 2. Access and Duplicate Templates
Navigate to the "template" section on the right-side sidebar navigation <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. Here, you'll find a list of predefined templates <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
1.  Search for the "purchase order" template using the search field <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
2.  Click on both the database link and the template link provided <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
3.  Click "Start with this template" to duplicate both the database and the template into your Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   Select your preferred Notion workspace and click "Add to private" when prompted for duplication <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### 3. Connect Notion to PDFOutput
Once the templates are duplicated in Notion, return to PDFOutput.com <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
1.  Click on either "click here to add database" or "click here to add template" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  Select your Notion workspace <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
3.  Choose the duplicated database and template from the list <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
4.  Click "Allow access" to authorize the connection <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   If the database and template don't appear immediately, click the refresh button <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### 4. Map Elements and Generate PDFs
1.  Define a name for your PDF generation setup (e.g., "Purchase Order") and click "Next" <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
2.  PDFOutput will load database elements and template elements (those within curly braces) <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
    *   **Automatic Mapping:** If the naming conventions in your Notion database exactly match the curly-braced fields in your template, the elements will map automatically <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   **Manual Mapping:** If names don't match, you'll see gray placeholders. Click on these and manually select the corresponding database element <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
3.  Click "Create PDF" <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. PDFOutput will then process and [[generating_pdf_documents_with_notion_and_pdfoutput | generate the PDF documents]] for each row in your database <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### 5. Preview and Download
Once the export is successful <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>:
1.  Click "Preview sample" to view one of the generated PDFs <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
2.  Click "Download all" to download all the generated PDF files <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. You can also click "Download PDF again" if you miss the initial download <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

## Customizing Templates and Best Practices

### Template Customization
The entire template is customizable; you can edit, modify, or make any changes once it's duplicated to your Notion workspace <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Ensure that any data you want to be replaced from the database is enclosed in curly braces <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

### Naming Conventions
It is crucial to use the exact same naming convention for fields in both the Notion template (within curly braces) and the Notion database <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This ensures automatic mapping within PDFOutput, saving time and preventing errors <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### Handling Relation Properties
If your Notion database uses any relation properties, make sure to grant access to those related databases when connecting Notion to PDFOutput <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This ensures all elements are correctly reflected in the generated PDF <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

## PDFOutput Features and Support

### Connections
The "Connections" option allows you to quickly re-load previously set up database and template pairings <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This avoids the need to repeatedly select the database and template for subsequent exports <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

### Upgrade Options
Under the free plan, generated documents will include a "Made with PDF Output" watermark <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. You can upgrade to a paid subscription to remove the watermark and remove limits on PDF generation <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### Settings
The "Settings" section allows you to adjust the page format (default is A4) <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. You can also add additional databases and templates from here after your initial setup <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

### Feedback and Help
*   **Feedback:** Use the "Feedback" option to report any issues or provide suggestions <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Help:** The "Help" section contains a video demonstrating how to use a custom template from scratch, if you prefer not to use the predefined options <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

For further questions or assistance, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.