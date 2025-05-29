---
title: Customizing and exporting generated PDF files
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

This tutorial demonstrates how to use "PDF output" to generate customized lease agreement documents in PDF format from a Notion database and page <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Preparing the Template and Database

### Lease Agreement Template
A lease agreement template is used, which includes details such as landlord name and tenant name <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This template incorporates placeholder text elements, indicated by curly braces (e.g., `{landlord_name}` and `{tenant_name}`), which will be replaced by data from the database <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

### Notion Database
A Notion database holds the specific values for each lease agreement, such as "landlord name," "tenant name," and "street address" <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. These values from individual rows in the database will be imported into the template to replace the placeholder text elements <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Using PDF Output for Generation

### Initial Setup
Before generating documents, users need to log in to the PDF output tool <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. It's crucial to follow the setup instructions in the "help section," which covers steps like setting up API keys <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Connecting Database and Template
Within the PDF output interface:
1.  Assign a "connection name" (e.g., "lease agreement") <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
2.  Select the Notion database from a dropdown list, which shows all databases connected via the API key <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
3.  Choose the corresponding lease template <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
4.  Click "next" to load the database and template elements <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Automatic Mapping
The tool automatically maps Notion properties from the database (e.g., "landlord name," "tenant name," "street address") to the corresponding PDF template elements if their names match <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. If elements are not automatically mapped, they appear in gray, and unmapped properties are listed in red <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Users can manually click to map them correctly <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## Exporting and Managing Generated PDFs

### Generating Documents
After mapping, clicking "export" processes the information <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. A "PDF status" column appears in the Notion database <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This column indicates which rows need PDF generation (unticked) and automatically ticks rows as their PDFs are generated <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

### Previewing and Downloading
Once processing is complete, a "preview sample" option becomes available to view a sample generated PDF <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. The preview demonstrates that the database information (e.g., "Tom Green" as landlord, "Sarah Blue" as tenant) has correctly replaced the placeholders in the template <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

Users can then click "[[exporting_and_downloading_pdf_documents | download all]]" to get all generated files in one go <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Individual PDF files can be opened to verify their content <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

## Key Considerations for Customization

To ensure smooth generation and mapping:
*   Customize the template to fit specific use cases <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   Ensure that the naming conventions in the database exactly match those in the template's placeholder elements <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. This precision prevents difficulties in automatic mapping <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

For any further questions, users can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.