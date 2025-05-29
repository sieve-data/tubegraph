---
title: Mapping Notion database elements to template placeholders
videoId: XPSQBVl9mKs
---

From: [[theaccountantguy]] <br/> 

[[PDF output | PDF output]] is a tool designed to [[using_notion_database_and_templates_for_pdf_generation | generate PDF documents in bulk]] by [[connecting_notion_database_and_templates_to_pdf_output | connecting a Notion database]] with a Notion template <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The core of this functionality relies on [[mapping_database_elements_to_template_placeholders | mapping specific elements]] from your Notion database to placeholders within your chosen Notion template <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## How Mapping Works

The process involves taking a Notion template, which contains placeholder text elements typically enclosed in curly braces, and replacing them with corresponding information from a Notion database <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

For each row in the Notion database, [[PDF output | PDF output]] fetches the information from the relevant columns and uses it to replace the placeholder text elements in the template <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This enables the bulk generation of customized PDF documents <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

For example, an invoice template might include placeholders such as `{{invoice number}}`, `{{date field}}`, `{{due date}}`, and `{{terms}}` <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. These placeholders are then replaced by the data from the corresponding columns in your Notion invoice database <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## The Mapping Interface

After selecting your Notion database and template within the [[PDF output | PDF output]] tool, the system proceeds to the second step of the process, which is the mapping of elements <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

In this interface:
*   **Notion Properties (Left Side)**: All the properties (column headers) present in your selected Notion database are displayed <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **Template Elements (Right Side)**: The placeholders identified in your Notion template are listed <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

[[PDF output | PDF output]] attempts to automatically map Notion properties to template elements <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. Successfully mapped elements appear in green <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### Manual Mapping

If there is a difference in the naming between a Notion property and a template element, the automatic mapping may not occur, and the unmapped element will appear in gray <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Users can click on these gray elements to manually map them <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

The interface also provides:
*   A search option to quickly find specific elements <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   A sorting option to organize the list of elements <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   A filtration option, allowing users to filter for unmapped properties to easily identify and address them <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

## Key Considerations for Successful Mapping

*   **Exact Name Match**: For automatic mapping to work effectively, ensure that the name specified for a placeholder in your Notion template (e.g., `{{Client Name}}`) exactly matches the name of the corresponding column in your Notion database <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   **Template Customization**: You can [[customizing_notion_templates | customize your Notion template]] by adding, deleting, or modifying elements <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. However, any elements added inside curly braces must have a corresponding column with information in your Notion database <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

By carefully [[synchronizing_database_elements_with_templates | synchronizing database elements with templates]] through proper mapping, [[PDF output | PDF output]] can accurately generate customized PDF documents from your Notion data <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.