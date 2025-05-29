---
title: Connecting Notion to PDF Output via API Key
videoId: Uh1g7uXtr_4
---

From: [[theaccountantguy]] <br/> 

[[integrating_notion_with_pdf_output_for_document_creation | Integrating Notion with PDF Output]] allows for the bulk generation of PDF documents from Notion databases. This process primarily relies on connecting your Notion database to the [[using_pdf_output_tool_with_notion | PDF Output tool]] through an API key <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

## Why an API Key is Needed
The API key serves as a confidential and private credential for your specific use case <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. It is essential for the [[using_api_keys_for_connecting_notion_to_pdf_generation_tools | PDF Output tool]] to securely access and interact with your Notion database <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

## Steps to Connect Notion to PDF Output

### 1. Set Up a New Integration in Notion
*   From the [[using_api_keys_for_connecting_notion_to_pdf_generation_tools | PDF Output interface]], click the link to add an API key, which will direct you to Notion's API key settings <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>, <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   Click on "new integration" <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   Add a new name for your integration and choose your workspace <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   Click "save" <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### 2. Copy the Internal Integration Secret
*   Once the integration is created, click on its name <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   Click "show" next to "internal integration secret" <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>, <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
*   This is the key required for the connection <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. Copy it <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

### 3. Paste the API Key into PDF Output
*   Navigate back to the [[using_pdf_output_tool_with_notion | PDF Output tool]] dashboard <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   Paste the copied API key into the designated field <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>, <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### 4. Connect the Notion Database to the API Key
*   The Notion database must be explicitly connected to the newly created API key <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>, <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   In your Notion database, click the three dots menu <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   Select "Connections" <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   Search for and select the name of the API key you created (e.g., "new key") <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>, <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   Click "Confirm" <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

### 5. Publish the Notion Database
*   For [[integrating_notion_databases_with_pdfoutput | PDFOutput]] to access the database, it must be published <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>, <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
*   In Notion, click "Share" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   Click "Publish" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   Click "Publish" again to confirm <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   This step is crucial for [[generating_pdf_documents_from_notion_using_pdfoutput | PDF Output]] to fetch the pages within the database <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>, <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

Once these steps are completed, you can use the [[exporting_notion_data_to_pdf | PDF Output tool]] to load the database and begin [[generating_pdf_documents_from_notion_using_pdfoutput | generating PDF documents]] <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.