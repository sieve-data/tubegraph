---
title: Setting up PDFOutput with API keys
videoId: lCyhl8mofjE
---

From: [[theaccountantguy]] <br/> 

[[Using PDFOutput for document generation | PDFOutput]] is a tool designed to generate PDF documents from a Notion database and Notion pages <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It can be used for tasks like generating lease agreements <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Preparing the Template and Database

To use [[Using PDFOutput for document generation | PDFOutput]], you'll need:
1.  **A template:** This template should contain placeholder text elements (e.g., `{{landlord name}}`, `{{tenant name}}`, `{{street address}}`) enclosed in curly braces <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
2.  **A Notion database:** This database will hold the values that will replace the placeholder text in your template <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. It's crucial that the naming convention of the database properties (e.g., "landlord name," "tenant name," "street address") exactly matches the placeholder names in your template <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## [[Steps to set up API keys for PDF generation | Setting up API Keys]] and Initial Configuration

To begin the setup process:
1.  **Log in to [[Using PDFOutput for document generation | PDFOutput]]** <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
2.  **Access the Help Section:** Navigate to the "Help" section within [[Using PDFOutput for document generation | PDFOutput]] <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
3.  **Follow API Key Setup Instructions:** This section provides all necessary instructions for [[Steps to set up API keys for PDF generation | setting up API keys]] to [[Connecting Notion to PDF Output via API Key | connect Notion to PDF generation tools]] <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. These steps are essential before you can generate any PDF documents <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## [[Setting up and configuring PDFOutput | Configuring PDFOutput]] for Document Generation

Once the API keys are set up, you can proceed with specific document generation:
1.  **Specify Connection Name:** Enter a name for your connection, such as "lease agreement" <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
2.  **Select Database:** Use the dropdown menu to select the desired Notion database. This menu displays all databases connected via your [[Using API keys for connecting Notion to PDF generation tools | API key]] <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
3.  **Select Template:** Choose the appropriate template from the template set <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
4.  **Click "Next"** <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Data Mapping and Export

After clicking "Next", [[Using PDFOutput for document generation | PDFOutput]] will load the database and template elements:
1.  **Automatic Mapping:** [[Using PDFOutput for document generation | PDFOutput]] automatically maps Notion database properties (on the left side) to corresponding PDF template elements (on the right side) if their names match <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. For instance, "landlord name" from the database will map to "landlord name" in the template <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
2.  **Manual Correction:** If an element is not automatically mapped, it will appear in gray <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. You can click on it to see all available properties and select the correct one if it's highlighted in red <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
3.  **Initiate Export:** Click "Export" to start the PDF generation process <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Post-Export Features

*   **PDF Status Column:** A "PDF status" column will appear in your Notion database. This column helps track which rows have had PDFs generated. Unticked rows indicate documents yet to be generated, and a tick mark appears once a PDF is created for that row <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Preview Sample:** After processing, you can click "Preview Sample" to view one of the generated PDF files <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This allows you to verify that information from the database (e.g., landlord name, tenant name, street address) has been correctly replaced in the template <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   **[[Exporting and managing PDFs in PDFOutput | Download All]]**: To download all generated PDF files, click "Download all." This will download them in a zip file <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. You can redownload files at any time <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

For any questions or assistance, you can reach out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.