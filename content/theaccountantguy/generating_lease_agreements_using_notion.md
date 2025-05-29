---
title: Generating lease agreements using Notion
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

This guide demonstrates how to generate PDF lease agreement documents from a [[finance_templates_in_notion | Notion database]] and Notion page using the PDF output tool <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Overview of the Process

The process involves using a lease agreement template in Notion with placeholder text elements (e.g., `{{landlord name}}`) and a Notion database containing the actual data (e.g., landlord names, tenant names, street addresses) <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. The PDF output tool will replace these placeholder texts in the template with the corresponding values from each row of your database to generate individual PDF documents <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Setting Up PDF Output

1.  **Log In and Initial Setup**:
    *   Log into the PDF output platform <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
    *   Navigate to the help section to find instructions on setting up the PDF output, including [[setting_up_loan_details_in_notion | setting up API keys]] required before generating documents <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

2.  **Specify Connection Details**:
    *   Enter a connection name, such as "lease agreement" <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
    *   From the dropdown menu, select your lease database that is connected via the API key <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
    *   Select your lease template from the template set <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
    *   Click "Next" <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Mapping Database Properties to Template Placeholders

After clicking "Next", the system loads the database and template elements <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>:

*   The PDF output tool automatically maps Notion properties from your database (e.g., "landlord name," "tenant name," "street address") to the corresponding placeholder elements in your template if their names match <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   On the left side, you'll see all your Notion properties <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   If a property is not automatically mapped, it will appear with a gray element. Clicking on it will show available properties, and unmapped ones will be listed in red <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Manually select the correct mapping if needed <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

> [!TIP] Naming Convention
> Ensure that the naming convention of your database properties and template placeholders matches exactly to facilitate automatic mapping <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## Generating and Downloading PDFs

1.  **Export**:
    *   Click "Export" <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
    *   As the information is processed, a "PDF status" column will appear in your Notion database <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. This column's purpose is to indicate which rows need PDF generation; unticked rows will be processed, and once generated, they will be ticked <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

2.  **Preview and Download**:
    *   Once processing is complete, you can click on the "Preview sample" option to view a single generated PDF (e.g., with landlord Tom Green and tenant Sarah Blue) <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   Click "Download all" to download all the generated PDF files in one go <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. The downloaded files will be exact replicas of your agreement template with data dynamically pulled from your database <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
    *   If you forget to download, you can click "Download" again <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

> [!INFO] Customization
> You can [[creating_professional_invoice_templates_in_notion | customize the template]] and utilize the database as per your specific use case <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

For any questions or assistance, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.