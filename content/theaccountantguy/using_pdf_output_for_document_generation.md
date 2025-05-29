---
title: Using PDF Output for document generation
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

[[PDF Output tool for document generation | PDF Output tool for document generation]] helps users to [[automating_pdf_document_generation | automate PDF document generation]] in bulk using Notion templates and databases <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process is particularly useful for tasks like [[using_pdf_output_for_invoice_generation | invoice generation]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Core Components for Document Generation

The system relies on two main Notion components: a Notion template and a Notion database <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

### Notion Template
The template defines the structure and layout of the document <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Elements within curly braces `{{ }}` serve as placeholders that will be replaced with data from the Notion database <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Examples of placeholders include `client name`, `client company`, and `client address` <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Templates are entirely customizable <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### Notion Database
The database holds the actual data for each document <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. It must contain properties with names that exactly match the placeholders in the template (e.g., `client name`, `client company`, `client address`) <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This precise naming allows for automatic mapping between the template and the database <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

## [[Setting up PDFOutput for document generation | Setting up PDFOutput for document generation]]

To begin, navigate to PDF output.com <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a> and log in <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

### Preparing Notion Assets
Before connecting, you need to duplicate the required template and database from PDF Output's pre-added list to your local Notion workspace <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
1.  Go to the "Templates" section on PDF output.com <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
2.  Search for the desired template (e.g., "invoice") <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
3.  Click on both the "database link" and "template link" associated with your chosen template <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
4.  In the new tabs that open, click the "Duplicate" option located in the top right corner of Notion for both the template and the database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
5.  Select your Notion workspace to duplicate the assets to <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Connecting to PDF Output Portal
Once the template and database are duplicated to your Notion workspace, connect them to PDF Output:
1.  On the PDF Output connection details screen, click "Add database" or "Add template" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
2.  Select your Notion workspace <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
3.  Choose the specific template and database you just duplicated <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
4.  Click "Allow access" <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. The database and template will automatically load in the PDF Output portal <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
5.  Define a connection name (e.g., "Invoice Template") <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
6.  Click "Next" <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

### Data Mapping
PDF Output will automatically map database properties to template elements if their names are identical <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. If names differ, manual mapping is required:
1.  Click on the gray icon next to the unmapped template element <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
2.  Search for and select the corresponding database property <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

## [[Utilizing PDF output for document generation | Generating Documents]]

Once all elements are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. The system will then [[using_pdf_output_com_for_pdf_generation | generate PDF documents]] for every row in your Notion database using the specified template <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

After generation, you can:
*   **Preview a sample PDF**: View one of the generated documents <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
*   **Download all documents**: Get a zip file containing all generated PDFs <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.

## Advanced Features and Settings

PDF Output offers several features beyond basic document generation:

*   **Connections**: The "Connections" sidebar displays all previously created connections, allowing you to quickly reuse them for new PDF generations without re-defining templates and databases <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Templates**: Access a library of pre-added templates for various use cases <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
*   **Upgrade Options**:
    *   Free plans include a "Made with PDF Output" watermark on generated PDFs <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
    *   Paid subscriptions remove the watermark and offer higher tiers for document generation <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **Settings**: Customize page format (e.g., A4 size) <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a> and add more databases and templates <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   **Feedback**: A dedicated option to send messages or queries <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
*   **Custom Templates/Databases**: Information on how to connect your own custom Notion templates and databases is available in the help section <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Relational Properties**: If your Notion database uses relational properties linked to other databases, ensure these linked databases are also added during the connection setup <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

For any questions or support, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.