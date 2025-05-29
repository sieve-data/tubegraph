---
title: Customizing invoice elements using placeholders
videoId: WfYK1BJd490
---

From: [[theaccountantguy]] <br/> 

To generate professional invoices directly from a Notion database, a key technique involves [[using_notion_templates_for_invoice_pdfs | using Notion templates]] with customizable placeholders <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This method allows for the dynamic population of invoice details from a database into a structured template.

## Understanding Placeholders

In a Notion invoice template, specific elements are designated as placeholders <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. These placeholders are defined by enclosing a descriptive name within curly braces, such as `{client name}` or `{client address}` <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

Key characteristics of placeholders:
*   **Definition**: Any element in the template placed inside curly braces (e.g., `{client name}`, `{client company}`, `{client address}`, `{city}`, `{state}`, `{zip}`) functions as a placeholder <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   **Purpose**: These placeholder texts are designed to be replaced by corresponding data from a database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Customizability**: All template elements are customizable to fit specific requirements <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

## Mapping Database Elements to Templates

The process involves connecting a Notion database, which contains the actual invoice information, to the template containing the placeholders <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. For every row of information in the database (e.g., client name, amount, bank name, client address, client company), the corresponding data will populate the template and generate a PDF <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

[[mapping_database_elements_to_invoice_templates | Mapping database elements to invoice templates]] is often automated by tools like "PDF Output" <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This tool loads all database properties and template elements, then automatically attempts to map them <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### Ensuring Correct Mapping

For successful automatic mapping, it is crucial that the names of the elements in the placeholders within the template exactly match the column names in the Notion database <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

If a mismatch occurs, the unmapped element will be highlighted (e.g., in gray color) <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. In such cases, users can manually select the correct corresponding value from the database to ensure proper mapping <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.