---
title: Integrating Notion with PDF Output for Invoices
videoId: r6IYxPK0iz8
---

From: [[theaccountantguy]] <br/> 

This guide explains how to [[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | generate professional invoice PDF documents in bulk]] using a [[using_notion_templates_for_pdf_generation | Notion template]] and a [[generating_pdf_documents_from_notion_database | Notion database]] with the help of [[using_pdf_output_tool_with_notion | PDF Output]].

## Prerequisites: Notion Template and Database

To begin, you will need a professional invoice template and a corresponding database in [[integrating_notion_with_pdf_output_tool | Notion]] <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

### Template Structure
The template should define all the elements typically found in an invoice <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Any element placed inside curly braces (e.g., `{client name}`) will be replaced by data from the [[generating_pdf_documents_from_notion_database | Notion database]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Examples include `{client name}`, `{client company}`, and `{client address}` <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

### Database Structure
The [[generating_pdf_documents_from_notion_database | Notion database]] must contain corresponding information for each element defined in the template <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. For every element in the database, there should be a corresponding element in the template, placed inside curly braces <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. [[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | PDF Output]] will use these elements to [[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | generate multiple PDF documents]] for each row in your database <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Step-by-Step Guide to [[generating_pdf_documents_in_bulk_using_notion_and_pdf_output | Generating PDF Documents]]

### 1. Access [[using_pdf_output_tool_with_notion | PDF Output]]
Navigate to PDFoutput.com and log in <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. Upon logging in, you will see a connection details screen where you need to define the connection for your [[creating_pdf_documents_from_a_notion_database | PDF generation process]] <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This involves connecting a [[generating_pdf_documents_from_notion_database | Notion database]] and a [[using_notion_templates_for_pdf_generation | Notion template]] <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

### 2. Duplicate Template and Database
Before connecting, you need to copy the desired template and database from [[using_pdf_output_tool_with_notion | PDF Output]]'s pre-added templates to your local [[integrating_notion_with_pdf_output_tool | Notion]] workspace <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   Click on "Templates" on the [[using_pdf_output_tool_with_notion | PDF Output]] site to see a list of available templates <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   Search for "invoice" or your desired template <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   Click on both the database link and the template link associated with your chosen template <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   Once opened in a new tab, click the "Duplicate" option in the top right corner for both the template and the database <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   Select your [[integrating_notion_with_pdf_output_tool | Notion]] workspace and click "Add to Private" to duplicate them <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### 3. Connect [[integrating_notion_with_pdf_output_tool | Notion]] to [[using_pdf_output_tool_with_notion | PDF Output]]
Once the template and database are duplicated in your [[integrating_notion_with_pdf_output_tool | Notion]] workspace, connect them to [[using_pdf_output_tool_with_notion | PDF Output]]:
*   In [[using_pdf_output_tool_with_notion | PDF Output]], click on "Add Database" (or "Add Template") <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   Select your [[integrating_notion_with_pdf_output_tool | Notion]] workspace <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   Select both the duplicated template and database, then click "Allow Access" <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   [[using_pdf_output_tool_with_notion | PDF Output]] will automatically load the selected database and template from your local [[integrating_notion_with_pdf_output_tool | Notion]] workspace <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   Define a connection name (e.g., "Invoice Template") and click "Next" <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### 4. Map Database Properties to Template Elements
[[synchronizing_notion_data_with_pdf_output | PDF Output]] will load the database and template, automatically mapping properties where names match <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   All database properties will be reflected on the left, and if named identically, they will automatically map to corresponding template elements <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   If template and database names differ, mapping will not be automatic <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. In this case, click the gray icon next to the unmapped element and search for the correct property to map it manually <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

### 5. [[generating_pdf_documents_from_notion_database | Generate PDF]]
Once all elements are correctly mapped, click "Create PDF" <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   [[using_pdf_output_tool_with_notion | PDF Output]] will begin [[generating_pdf_documents_from_notion_database | generating a PDF]] for every row in your database <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   Upon successful export, you can preview a sample PDF or download all generated documents <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.

> "As you can see, the PDF has been generated and it is saying the export was successful." <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>

## Key Considerations and Tips

*   **Customizable Templates:** The template is fully customizable to your requirements <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. Ensure that any data you want to pull from the database is placed inside curly braces in the template and uses the exact same name as the database property for automatic mapping <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Connections:** [[using_pdf_output_tool_with_notion | PDF Output]] saves your connections <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. You can access previously created connections via the sidebar under "Connections" to quickly regenerate PDFs without re-defining the template and database <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   **Relational Properties:** If your [[generating_pdf_documents_from_notion_database | Notion database]] uses relational properties connected to other databases, ensure you also allow access to those linked databases during the connection setup <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Subscription Plans:** The free plan includes a "Made with [[using_pdf_output_tool_with_notion | PDF Output]]" watermark <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Upgrading to a paid plan removes the watermark and offers higher document generation tiers <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **Page Format:** In the settings, you can define the specific page format (e.g., A4 size) for your PDF documents <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   **Adding More Databases/Templates:** After initial setup, you can add more databases and templates through the "Settings" option <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Custom Templates/Databases:** If you prefer to use your own custom [[using_notion_templates_for_pdf_generation | Notion template]] and [[generating_pdf_documents_from_notion_database | database]] rather than the pre-provided ones, detailed instructions are available under the "Help" section <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

## Support
For any feedback or queries, you can use the feedback option within the [[using_pdf_output_tool_with_notion | PDF Output]] portal <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>, or reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.