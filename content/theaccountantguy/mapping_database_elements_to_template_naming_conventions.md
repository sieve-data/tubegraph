---
title: Mapping database elements to template naming conventions
videoId: W_j9W6XedqM
---

From: [[theaccountantguy]] <br/> 

Generating PDF documents in bulk from a Notion database and template relies heavily on a precise naming convention between the two components. This process enables efficient [[automatic_mapping_of_notion_database_properties_to_pdf_template_elements | automatic mapping of Notion database properties to PDF template elements]], streamlining the creation of numerous documents like payment receipts <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Template and Database Structure

A template, such as a payment receipt, includes specific elements or placeholders enclosed within curly braces <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. These placeholders represent the dynamic information that will be pulled from a database <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. For example, a template might have `{receipt number}`, `{receipt date}`, `{receipt time}`, `{customer name}`, and `{company website}` <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

The corresponding Notion database must contain columns for each of these elements <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. The key to successful [[mapping_database_elements_to_template_placeholders | mapping database elements to template placeholders]] is to use the exact same naming convention for the database columns as for the placeholders in the template <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This includes matching spacing and capitalization <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. For instance, if the template uses `{Company Website}`, the database column should also be named `Company Website` <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

## Automatic Mapping

When the naming conventions are followed precisely, the system (e.g., PDF output.com) can automatically map the database properties to the template elements <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. This means that for every column in the database, the system will automatically identify and link it to the corresponding placeholder in the template <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. This eliminates the need for manual configuration and ensures that data from each row in the database populates a unique PDF document correctly <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

<p class="yt-timestamp" data-t="00:09:02">[00:09:02]</p>
> "Make sure you put all the elements inside these curly braces and use the same exact naming Convention of the database so as to avoid any manual mapping in the second step."

## Handling Mismatches

If there is a mismatch in the naming convention between a database column and a template placeholder (e.g., a typo or different capitalization), the system will indicate that the element is unmapped <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. In such cases, you will need to manually select the correct corresponding element from a dropdown list to complete the [[mapping_notion_database_to_templates | mapping Notion database to templates]] <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

By adhering to a consistent and exact naming convention, users can ensure seamless [[integrating_databases_with_templates | integrating databases with templates]] and efficient bulk PDF generation using Notion <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.