---
title: Using PDF4put for bulk invoice generation
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

PDF4put is a tool that enables users to generate PDF documents in bulk from a Notion invoice template and database <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. It allows for the creation of professional invoice documents containing necessary information, dynamically populated from a Notion database <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a> - <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Preparing Your Notion Template and Database

To use PDF4put effectively for [[generating_pdf_invoices_using_pdf_output_service | generating PDF invoices]], ensure your Notion setup meets the following requirements:

*   **Invoice Template**: Create a professional invoice template in a Notion page <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.
*   **Dynamic Fields**: Place any information you wish to replace from your database inside curly brackets `{}` within the template <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a> - <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. These fields must correspond to column names in your database <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a> - <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Database**: Ensure your Notion database contains the specific information required for each invoice record, matching the fields defined in your template <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a> - <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>, <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a> - <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

### Sharing Your Notion Page

The Notion page containing your invoice template must be made public for PDF4put to access it:
1.  Open your Notion invoice template page <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
2.  Click on "Share" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
3.  Click "Publish" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>, then again "Publish" to make the page public <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a> - <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
4.  Copy the page URL, either from the "Share" menu or the browser's address bar <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a> - <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Setting up PDF4put

1.  **Access PDF4put**: Navigate to pdf4put.com <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
2.  **Sign In**: Click "Sign In" and choose your preferred account <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a> - <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
3.  **Paste Notion Page URL**: Paste the copied Notion page URL into the designated field on PDF4put <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a> - <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Click "Load Page" to preview the document <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a> - <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

    > [!NOTE] Viewing Options
    > You can toggle between "Document" view to see the rendered page or "Source" view to see the input fields <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a> - <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

4.  **Generate Notion API Key**:
    *   Click on the "Click here to add Notion API key" link <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a> - <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
    *   In the Notion window that opens, click "New Integration" <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a> - <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
    *   Provide a name (e.g., "new key") and choose your account, then click "Save" <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a> - <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
    *   Go to "Integrations," click on your new key, click "Show," and copy the API key <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a> - <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
    *   Paste the copied API key into the PDF4put application <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a> - <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

5.  **Connect Notion Database with API Key**:
    *   Go back to your Notion database <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a> - <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
    *   Click on the three dots in the top right corner of the database <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a> - <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
    *   Click "Connections" <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a> - <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
    *   Search for and select the API key you just created (e.g., "new key") <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a> - <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
    *   Click "Confirm" <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

6.  **Paste Database URL**: Copy the URL of your Notion database from the browser's address bar <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a> - <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. Paste it into the PDF4put application <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a> - <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
7.  **Load Database**: Click "Load Database" in PDF4put <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

## Generating Bulk PDFs

1.  **File Naming**: Select a column from your database to use for naming the generated PDF files (e.g., "invoice number") <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a> - <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
2.  **Row Selection**: Choose which rows from the database to use for PDF generation <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>:
    *   **All Rows**: Generates a PDF for every record in the database <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a> - <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
    *   **Custom Rows**: Specify a range (e.g., 4th through 7th row) <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a> - <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
    *   **Specific Row**: Generate for a single, specific row <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a> - <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
3.  **Generate PDF**: Click "Generate PDF" <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a> - <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. PDF4put will begin populating and generating each invoice, prompting you to save them sequentially <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a> - <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### Layout Settings
You can adjust various layout settings for the generated PDFs, such as:
*   Paper size <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a> - <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>
*   Orientation (portrait or landscape mode) <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a> - <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>
*   Pages to print (e.g., all pages) <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a> - <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>

## Key Considerations

*   **Public Page**: Ensure your Notion page is always shared publicly and accessible <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a> - <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
*   **Database Connection**: The Notion database must be connected to the specific API key you are using <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a> - <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **Relational Properties**: If your database uses any relational properties that link to other Notion databases, those linked databases must also be connected to the *same* API key for seamless document generation <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a> - <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

## Support

For any queries or issues, you can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a> - <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>, or use the contact window available on the PDF4put website <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a> - <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.