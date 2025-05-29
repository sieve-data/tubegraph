---
title: Generating lease agreements using Notion
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

This guide details how to generate PDF lease agreement documents using a Notion database and a Notion page as a template, leveraging a PDF output tool <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Components for Lease Agreement Generation

### Lease Agreement Template in Notion
A Notion page serves as the lease agreement template <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This template includes all necessary details for a lease agreement, such as landlord name, tenant name, and street address <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Key information within this template is placed as placeholder text elements, enclosed in curly braces (e.g., `{{landlord name}}`, `{{tenant name}}`, `{{street address}}`) <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

### Notion Database for Lease Details
A Notion database holds the specific data for each lease agreement <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This database contains properties such as `landlord name`, `tenant name`, and `street address`, which will be used to replace the placeholder text in the template <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Each row in the database corresponds to an individual lease agreement <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Steps to Generate Lease Agreements

### 1. Log In and Set Up the PDF Output Tool
The first step is to log into the PDF output tool <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. It is crucial to visit the tool's help section to follow the setup tutorial, which includes instructions for setting up API keys necessary for integration with Notion <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### 2. Configure the Connection
Once logged in and set up, specify a connection name (e.g., "lease agreement") <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. Then, select the appropriate Notion database (e.g., "lease") from the dropdown menu, which lists all databases connected via the API key <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Similarly, select the Notion template page (e.g., "lease template") <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### 3. Map Database Properties to Template Placeholders
After selecting the database and template, click "next" <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. The tool will then load and automatically map the Notion database properties (displayed on the left side) to the corresponding PDF template elements (placeholders) if their names match <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>, <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

*   **Automatic Mapping**: Properties like "landlord name" from the database are automatically mapped to the "landlord name" placeholder in the template <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   **Manual Mapping**: If a property is not automatically mapped, it will appear in gray <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Clicking on it will show all available properties, with unmapped ones listed in red <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. These can then be manually mapped.

### 4. Export and Generate PDFs
After mapping is complete, click "export" <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. As the tool processes the information, a new "PDF status" column will appear in your Notion database <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

*   **PDF Status Column**: This column indicates which rows have had PDFs generated. Rows that are unticked will be processed <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. As PDFs are generated, a tick mark will automatically appear in this column for the corresponding rows <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### 5. Review and Download
Once generation is complete, you can:
*   **Preview Sample**: Click "preview sample" to view one of the generated PDF files (e.g., a lease agreement for "Tom Green" and "Sarah Blue") <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>, <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Download All**: Click "download all" to download all generated lease agreement PDFs in one go <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. These downloaded files will be exact replicas of the agreement template, populated with data from your database <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

## Important Considerations
*   **Customization**: The template can be customized to suit your specific use case <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Naming Conventions**: Ensure that the naming convention of properties in your Notion database exactly matches the placeholder names in your Notion template to facilitate automatic mapping and avoid difficulties <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## Support
For any questions or assistance, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.