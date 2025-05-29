---
title: Customizing invoice templates in Notion
videoId: WfYK1BJd490
---

From: [[theaccountantguy]] <br/> 

[[setting_up_notion_for_invoice_management | Setting up Notion for Invoice Management]] involves [[creating_a_professional_invoice_template_in_notion | creating a professional invoice template in Notion]] and connecting it to a Notion database to automatically generate invoices. This process utilizes a tool called "PDF output" to generate professional invoices directly from a Notion database <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Template Structure
A professional invoice template in Notion typically includes sections like "from" and "to" <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Key details within the "to" section, such as client name, client company, client address, city, state, and zip, are designated as placeholder text enclosed in curly braces <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Any element within the template enclosed in curly braces is designed to be replaced by dynamic data from a database <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Database Integration
The Notion database contains the specific information that populates these placeholders. Columns in the database correspond to the placeholder names in the template, holding details like client name, amount, bank name, client address, and client company <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. For every row of information in the database, the system will populate the template and generate a corresponding PDF <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Using PDF Output for Generation
To facilitate this, the "PDF output" tool is used <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. After logging into PDF output, users must first complete certain steps, including enabling API keys, which are detailed in the "H" (help) section of the interface <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Connection Setup
1.  **Define Connection Name**: Assign a name to the connection, such as "invoice generation" <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
2.  **Select Database**: Choose the Notion database (e.g., "professional invoice database") <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
3.  **Select Template**: Specify the Notion template (e.g., "professional invoice template") <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
4.  **Click Next**: This action initiates the loading and automatic mapping of database elements to template placeholders <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

### Data Mapping
The tool automatically maps database properties (listed on the left) to the corresponding template elements (on the right) <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. For example, "client address" from the database is connected to "client address" in the template <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

### Customization and Matching Rules
When [[customizing_notion_templates | customizing Notion templates]] for invoices, it's crucial that the element names in the template's placeholders exactly match the column names in the Notion database <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. If a mismatch occurs, the element will appear in gray, and you can manually click on it to search for and select the correct database column <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

All elements in the template are customizable according to specific requirements <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. The primary rule for [[customizing_invoice_details_in_notion | customizing invoice details in Notion]] and [[customizing_and_duplicating_templates_in_notion | customizing and duplicating templates in Notion]] is that all placeholder text must be enclosed in curly braces, and the names inside these braces must match the corresponding column names in the Notion database <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

### Export and Output
After mapping, clicking "export" begins the PDF generation process <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. In the Notion database, a "PDF status" column will be unticked initially and will automatically tick as each PDF file is generated <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Once all PDFs are generated, they can be previewed or downloaded collectively by clicking "download all" <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This enables [[creating_invoices_in_bulk_using_notion | creating invoices in bulk using Notion]]. The generated PDFs are clean and accurately reflect the data from the database within the chosen template <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

For further assistance, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.