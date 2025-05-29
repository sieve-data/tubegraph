---
title: Mapping and managing data fields between Notion database and PDF templates
videoId: 432wMcdqv1w
---

From: [[theaccountantguy]] <br/> 

[[Generating PDF documents from Notion database | PDF Output]] is a tool designed to [[Creating PDF documents from a Notion database | generate PDF documents directly from a Notion database]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This process involves [[Connecting Notion databases and templates for PDF creation | connecting a Notion database]] and selecting a Notion template to create the PDF document <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Requirements for Data Mapping

To successfully map data fields and [[Generating PDF documents from Notion database | generate PDFs]], two primary components are needed:

### Notion Template
A template is essential for PDF generation <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This template, such as an invoice template, contains placeholder text elements enclosed in curly brackets <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Examples include `client name`, `client company`, `client address`, `invoice number`, and `due date` <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. These placeholders will be replaced with actual data from a Notion database <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### Notion Database
The Notion database, like an invoice database, should contain columns with information such as `client name`, `client company`, and `client address` <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Each row in the database represents unique information that will be used to populate the template <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

The information from the database rows will replace the placeholder text in the template, one by one, to create the PDF documents <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Connecting Notion for Data Mapping

Before mapping, the Notion API key must be set up, typically using a private integration key <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This involves creating a new integration in Notion, selecting a workspace, and copying the secret key <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This key is then pasted into [[Setting up Notion databases for PDF generation | PDF Output]]'s settings <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>, <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

Crucially, both the Notion template and the database must be shared with the created integration <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>, <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. This is done by clicking the three dots on the top right of the Notion page, selecting "Connect," and choosing the integration name <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>, <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

Additionally, a "PDF status" property (checkbox type) should be added to the Notion database. If this checkbox is unchecked for a particular row, [[synchronizing_notion_data_with_pdf_output | PDF Output]] will generate a PDF for that row; if checked, it will not <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## The Data Mapping Process

Once the connection is established and the template and database are selected within [[Generating PDF documents from Notion database | PDF Output]] <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>, the tool proceeds to read information from both sources <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

### Automatic Mapping
[[Customizing Notion Templates for PDF Documents | PDF Output]] lists all Notion database properties on the left side of its interface <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. It then automatically maps each of these properties to the corresponding placeholder elements in the Notion template <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. For example, a "client name" property from the database will automatically map to the "client name" placeholder in the template if the naming convention matches <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

*   **Recommendation**: To ensure seamless automatic mapping, it is recommended that the naming conventions used for placeholder text in the template (e.g., `client name` in curly brackets) exactly match the column names in the Notion database <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Manual Mapping and Tools
If certain elements are not automatically mapped (appearing in gray instead of green) <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>, users can manually map them:
1.  Click on the unmapped element <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
2.  A list of fetched PDF elements from the Notion template will appear <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
3.  Search for and select the correct element to establish the mapping <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

The interface also provides:
*   **Search Option**: To quickly find a particular property <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Sorting Option**: To organize elements <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Filter Option**: To view unmapped, mapped, or all properties <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

## Generating PDF Documents

Once all data fields are correctly mapped, clicking "export" initiates the PDF generation process <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. [[synchronizing_notion_data_with_pdf_output | PDF Output]] processes the documents, ticking the "PDF status" checkboxes in the Notion database for the generated rows <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. The tool then fetches columns from the database and replaces the placeholder elements in the template, [[Creating and using Notion templates for PDFs | generating the PDF output]] <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

Generated PDFs can be previewed directly on the web interface or downloaded <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. These downloaded files will reflect the data from each respective database row, populated into the template <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>, <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. A watermark will appear on PDFs if using the free plan, which is removed on paid plans <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

Connections can be saved, allowing users to quickly load previously defined settings for [[Using Templates in Notion for PDF Generation | subsequent PDF generation]] without re-specifying details <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

## Conclusion

[[Generating PDF documents from Notion database | PDF Output]] simplifies the process of [[using_notion_templates_for_pdf_generation | generating template-based PDF documents]] from Notion databases <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. By adhering to consistent naming conventions for placeholder text in templates (using curly braces) and corresponding column names in Notion databases, users can ensure efficient and accurate data mapping and PDF creation <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.