---
title: Mapping database elements to templates for PDF generation
videoId: WfYK1BJd490
---

From: [[theaccountantguy]] <br/> 

This article explains how to use PDFOutput to [[generating_pdfs_from_database_entries | generate professional invoices]] or other documents directly from a [[working_with_databases_and_data_replacement_in_pdf_templates | Notion database]] by [[mapping_notion_database_elements_to_pdf_templates | mapping database elements to PDF templates]] <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. The process involves defining a template with placeholders and then connecting it to a database that holds the corresponding data.

## Template Preparation

The first step in [[creating_and_using_templates_for_pdf_generation | creating and using templates for PDF generation]] is to design your template.
For invoices, this includes sections like "from" and "to" <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

### Placeholder Elements

Key elements in your template that will be replaced by database information must be defined as placeholder text <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. These placeholders are encased in curly braces, for example:
*   `{client name}` <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>
*   `{client company}` <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   `{client address}` <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
*   `{city}` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>
*   `{state}` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>
*   `{zip}` <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>

The entire template will be utilized to [[using_templates_to_automate_pdf_creation | generate the PDF documents]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Database Structure

Your Notion database should contain columns that correspond to the placeholder names in your template <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Examples of database columns include:
*   Client name <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>
*   Amount <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>
*   Bank name <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>
*   Client address <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>
*   Client company <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>

For every row of information in the database, a separate PDF will be generated, with the data populating the respective fields in the template <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Using PDFOutput for Generation

### Initial Setup

1.  Log in to PDFOutput <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
2.  Navigate to the help section (by clicking 'H') to complete the necessary steps for enabling API keys. This is crucial for the setup to function <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Defining the Connection

1.  Provide a name for your connection, such as "Invoice Generation" <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  Select your Notion database name from the dropdown (e.g., "professional invoice database") <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
3.  Similarly, select your Notion template name (e.g., "professional invoice template") <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
4.  Click "Next" <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Automatic Mapping

PDFOutput will load all database elements and template values and automatically map them <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. The database properties are listed on the left, connected to their corresponding template elements <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

> [!NOTE] Matching Names
> For a successful automatic mapping, ensure that the element names in your template's placeholders exactly match the column names in your database <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. If an element isn't matching, it will appear in gray. You can manually select the correct value if available <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### Exporting and Generating PDFs

1.  After mapping, click "Export" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
2.  A "PDF status" column in your Notion database will automatically update (tick) as each PDF file is generated <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
3.  Once the process is complete, you can click "Preview Sample" to view an output <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
4.  Click "Download All" to download all generated PDF files <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

The generated PDFs will cleanly display all elements as per your database <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. For example, an invoice will show the correct company name and address, pulled directly from the corresponding database entry <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

This process allows for [[using_notion_templates_and_databases_for_pdf_generation | seamless PDF generation from Notion templates and databases]] <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. All template elements are customizable according to your requirements, as long as placeholders are correctly defined in curly braces and match database column names <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.