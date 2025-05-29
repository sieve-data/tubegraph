---
title: Customizing PDF templates in Notion
videoId: hfHjnNxqo4o
---

From: [[theaccountantguy]] <br/> 

PDF Output allows users to [[using_notion_for_generating_pdf_documents | generate PDF documents]] in bulk directly from a Notion page and database, utilizing customizable templates <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Template Structure
PDF templates use curly braces `{}` to denote fields that will be replaced by data from a Notion database <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. For example, `{purchase order number}`, `{date field}`, `{supplier name}`, and `{buyer name}` are all placeholders <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. These items inside curly braces are automatically replaced with corresponding data from your Notion database when generating PDFs <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## How to Customize and Use Templates
To begin, log in to PDF Output.com <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. You will be prompted to connect to a Notion database and a Notion template <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

### Duplicating Predefined Templates
1.  Navigate to the "Template" section in the sidebar navigation <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
2.  Search for a predefined template, such as "purchase order" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
3.  Click on the provided database and template links associated with the desired template <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
4.  Select "Start with this template" to duplicate both the database and the template into your Notion workspace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
5.  Choose your Notion workspace and click "Add to private" to complete the duplication <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Editing a Duplicated Template
Once a template is duplicated into your Notion workspace, you can freely edit, modify, or make any desired changes to it <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
> [!IMPORTANT] Naming Convention
> Ensure that any dynamic content you wish to populate from your database remains enclosed in curly braces <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. The naming convention for these placeholders inside the template **must exactly match** the naming of the properties in your Notion database <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>, <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>, <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. This enables automatic mapping of database elements to template elements <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### Manual Mapping
If the naming conventions between the template placeholders and database properties do not match exactly, manual mapping will be required <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. Mismatched elements will appear in gray, and you will need to manually select the corresponding database property for each template element <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

## Connecting to PDF Output
After [[creating_and_using_templates_in_notion | creating and using templates in Notion]], connect them to PDF Output:
1.  In PDF Output, click "Click here to add database" or "Click here to add template" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  Grant permission by selecting your workspace and choosing the duplicated database and template <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
3.  Click "Allow access" to authorize the connection <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
4.  Once connected, you can name your connection (e.g., "purchase order") and proceed to generate PDFs <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

### Handling Relation Properties
If your Notion database utilizes "relation properties," ensure that you also grant access to the related database when connecting to PDF Output <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This ensures all related elements are correctly reflected in the PDF output <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

## Advanced Customization
For users who prefer not to [[using_predefined_templates_in_notion_for_pdf_generation | use predefined templates in Notion for PDF generation]], a video guide is available in the "Help" section of PDF Output that demonstrates how to create a custom template from scratch <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. This allows for complete control over your PDF template design and data structure <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.