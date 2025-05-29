---
title: Generating lease agreement PDFs using Notion and PDFOutput
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

This guide outlines how to generate lease agreement PDF documents using a [[Using Notion as a template and database for PDFs | Notion database]] and template, leveraging the [[Using PDFOutput tool for Notion | PDF Output]] tool <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Preparing Your Notion Template and Database

Before generating PDFs, you need to set up your Notion template and database:

1.  **Lease Agreement Template**: Create a Notion page that serves as your lease agreement template <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
    *   This template should include all necessary details such as landlord name, tenant name, and street address <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
    *   Crucially, use placeholder text elements enclosed in curly braces (e.g., `{landlord name}`, `{tenant name}`, `{street address}`) for information that will be dynamically replaced <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

2.  **Lease Agreement Database**: Create a Notion database that contains the specific values for each lease agreement <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
    *   This database should have properties (columns) like "Landlord Name", "Tenant Name", and "Street Address" <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
    *   The values from each row in this database will be imported into the template to replace the placeholder text elements <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
    *   **Best Practice**: Ensure the naming conventions for your database properties (columns) exactly match the placeholder names in your template to facilitate automatic mapping <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>, <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## Setting Up PDFOutput

1.  **Log In**: Access the [[Using PDFOutput tool for Notion | PDF Output]] platform <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
2.  **Initial Setup**: Navigate to the "Help" section within [[Using PDFOutput tool for Notion | PDF Output]] <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. Follow the tutorial there to set up [[Using PDFOutput tool for Notion | PDF Output]], including configuring API keys, before generating any documents <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
3.  **Connection Details**:
    *   Specify a connection name, for example, "Lease Agreement" <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
    *   From the dropdown menu, select your Notion database that is connected via the API key (e.g., "Lease") <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
    *   Select your Notion template page (e.g., "Lease Template") <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
4.  **Proceed**: Click "Next" to load the database and template elements <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Mapping Notion Properties to PDF Elements

After clicking "Next", [[Using PDFOutput tool for Notion | PDF Output]] will load and attempt to automatically map your Notion database properties to the template's placeholder elements based on matching names <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

*   On the left side, you'll see all your Notion database properties (e.g., "Landlord Name", "Tenant Name", "Street Address") <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   On the right side, you'll see the corresponding PDF template elements that have been mapped <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   If a property isn't automatically mapped, it will appear in gray <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Unmapped properties are listed in red <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. You can manually map them by clicking on the element <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## [[PDF document generation from Notion | Generating the PDF Documents]]

1.  **Export**: Once mapping is complete, click "Export" <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
2.  **PDF Status Column**: [[Using PDFOutput tool for Notion | PDF Output]] will add a "PDF status" property (column) to your Notion database <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
    *   This column indicates which rows need PDF generation <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
    *   Any row that is *unticked* in this column will have its PDF generated <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
    *   As [[Using PDFOutput tool for Notion | PDF Output]] processes a row and generates its PDF, it will automatically tick the corresponding checkbox in the "PDF status" column <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

## Viewing and Downloading PDFs

1.  **Preview Sample**: After the generation process, a "Preview Sample" option will become available <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Clicking this allows you to see an example of a generated PDF, ensuring the placeholders have been correctly replaced with database values (e.g., landlord Tom Green, tenant Sarah Blue) <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
2.  **Download All**: To get all generated PDF files, click "Download All" <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. This will download all documents, often in a single ZIP file <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. You can open individual files to verify their content <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
3.  **Re-download**: If you forget to download the files, you can click "Download" again <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

This process allows for automated and efficient [[Creating PDF Documents from Notion Database | creation of PDF documents from a Notion database]], customized for each entry <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. For further assistance, you can reach out via email <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.