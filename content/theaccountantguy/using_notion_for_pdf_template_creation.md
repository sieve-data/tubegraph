---
title: Using Notion for PDF Template Creation
videoId: YbcxEBwvmKU
---

From: [[theaccountantguy]] <br/> 

[[generating_pdf_documents_from_notion | PDF output]] is a tool designed to [[generating_pdf_documents_from_notion | generate PDF documents]] in bulk by utilizing a Notion page as a template and a Notion database to supply the elements for replacement within that template <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. To [[setting_up_a_notion_database_and_template_for_pdf_generation | create a template and a database from scratch]] for PDF generation, you will need to define both a Notion database and a Notion template <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Creating a Notion Template

To begin creating a Notion template for PDF output:
1.  Navigate to your Notion workspace <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
2.  Click on the "create a new page" icon <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This will open a blank page <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
3.  Name your template, for example, "Invitation Letter Template" <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
4.  Set the page to "full width mode" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
5.  Define the content of your template <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### Defining Placeholder Elements

When creating your template, specific sections intended to be replaced with data from a database should be defined inside curly braces <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. These "placeholder text elements" will be automatically mapped to corresponding elements in your database if the naming convention is exact <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

*   **Example:** If you want to replace a title and customer name, you would include `{title}` and `{customer name}` within your template <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

> [!TIP] Consistent Naming
> Ensure the naming convention for your placeholder text elements within curly braces matches the exact column names in your Notion database <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. If the names differ, you will need to manually map them during the PDF generation process <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

## Using Predefined Templates

[[creating_and_using_notion_templates | PDF output]] also offers predefined templates <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. To use one of these templates, you must duplicate it (along with its associated database) to your Notion workspace <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
1.  Click on "start with this template" <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
2.  Select your Notion workspace <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
3.  Click "add to private" <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>, which will add the template to your Notion database <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

## Integrating with PDF Output

Once your Notion template and database are set up:
1.  Log into PDF output <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
2.  In the "Notion Database" section, select your database <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
3.  In the "Notion Template" section, select your template <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
4.  Authorize PDF output to access these pages in your Notion workspace <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
5.  Define a connection name <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
6.  Map the database properties (like `customer name` and `title`) to the corresponding template elements (the placeholder text inside curly braces) <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. If the naming is exact, this mapping happens automatically <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
7.  Click "Create PDF" to generate the documents <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. The tool will then replace the placeholder elements in the template with the data from each row of your database <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

This process allows for [[using_a_notion_database_and_templates_to_create_pdf_invoices | creating and generating multiple PDF documents]] from a single Notion template and database <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

> [!NOTE] Plan Limitations
> The free plan for PDF output includes a "made with PDF output" watermark and certain limitations. To remove the watermark and access full features, an upgrade subscription is available <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.