---
title: Creating professional invoice templates
videoId: WfYK1BJd490
---

From: [[theaccountantguy]] <br/> 

Professional invoices can be generated directly from a Notion database using a pre-defined template <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This process involves creating a Notion template with specific placeholders that are then populated by data from a Notion database <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Template Structure

An invoice template typically includes sections such as "from" and "to" <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. The "to" section might contain fields for the client name, client company, client address, city, state, and zip code <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Using Placeholders

All elements in the template that are intended to be replaced by data from a database are designated as "placeholder text" <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. These placeholders must be enclosed within curly braces, e.g., `{client name}` <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

The names used for these placeholder elements in the template must exactly match the column names in the Notion database <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. This ensures that the system can automatically map the database properties to the corresponding template elements <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. For example, a `{client address}` placeholder in the template would be linked to a "client address" column in the database <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. If a mismatch occurs, the unmapped elements will appear in gray and can be manually corrected <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## Database Integration

The Notion database contains the actual information that will populate the template, such as client name, amount, bank name, client address, and client company <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Each row of information in the database will be used to populate a new instance of the template, resulting in a generated document <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## [[customizing_invoice_templates_in_notion | Customization and Generation]]

The elements within the invoice template are fully customizable to suit specific requirements <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. The primary rule to remember is that all placeholder text must be enclosed in curly braces, and their names must correspond to the column names in the linked database <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

Once the template and database are set up, a tool like [[using_pdf_output_for_invoice_generation | PDF output]] can be used to connect them <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. After connecting the database and template names, the tool automatically maps the fields and allows for [[generating_pdf_documents_from_invoices | PDF document generation]] <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The resulting PDF output is clean and reflects all the elements populated from the database <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.