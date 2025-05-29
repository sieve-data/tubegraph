---
title: Setting up and using Notion API key
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

A Notion API key is essential for connecting a Notion database with external tools, such as PDF output services like PDFoutput.com. It acts as a bridge, allowing the external service to access and utilize data from your Notion database to generate documents <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

## Creating a Notion API Key (Internal Integration)

To integrate your Notion database with an external tool, you first need to [[creating_internal_integration_secret_for_notion | create an internal integration secret]], which serves as your API key <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>:

1.  Navigate to the integration creation interface (e.g., via a link provided by the external tool, or directly in Notion) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
2.  Click on "New Integration" <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
3.  Assign a descriptive name to your new integration (e.g., "New Key") <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
4.  Select your Notion account to associate with the integration <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
5.  Click "Save" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
6.  Once created, navigate to the "Integrations" section to view your new key <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
7.  Click on the key and select "Show" to reveal the full API key <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
8.  Copy the API key to your clipboard <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## Connecting a Notion Database to the API Key

After creating your API key, you must [[connecting_notion_with_pdf_output_via_api | connect your Notion database]] to this specific integration to grant it access <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>:

1.  Go to the [[creating_database_in_notion | Notion database]] you wish to use <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
2.  Click on the three dots located at the top right of the database <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
3.  Select "Connections" <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
4.  Search for the name of the API key (e.g., "new key") that you created earlier <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
5.  Select the integration and click "Confirm" <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
6.  This action links your database to the API key, making it accessible for the integrated tool <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

## Using the API Key with PDF Output Tools

Once you have your Notion page URL, the API key, and the database URL, you can configure the PDF output tool:

1.  Paste the copied API key into the designated field on the PDF output tool's interface <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
2.  Ensure your Notion page, used as a template, is shared publicly and accessible <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>, <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
3.  Verify that your Notion database is successfully connected to the API key you've added <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
4.  Click "Load Database" to allow the tool to fetch data <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

## Important Considerations

*   **Public Page Sharing**: The Notion page serving as your template (e.g., invoice template) must be shared publicly for the external tool to access its structure and content <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   **Database Connection**: Always ensure the database you intend to use is connected to the specific API key you've created <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **[[connecting_relational_databases_with_notion_api | Relational Databases]]**: If your primary database utilizes [[connecting_relational_databases_with_notion_api | relational properties]] linked to other databases, those secondary databases must also be connected to the *same* API key for seamless data fetching and document generation <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.