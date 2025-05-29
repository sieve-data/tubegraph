---
title: Setting up and sharing a Notion page for public use
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 
The process of making a Notion page public and accessible involves specific sharing settings, allowing external services to interact with its content. This is particularly useful when using a Notion page as a template for bulk document generation.

## Sharing a Notion Page for Public Use

To make a [[creating_content_on_notion_pages | Notion page]] publicly accessible, follow these steps:

1.  Navigate to the desired [[creating_content_on_notion_pages | Notion page]] you intend to use (e.g., an invoice template). <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>
2.  Click on the "Share" button, usually located in the top right corner of the page. <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
3.  Within the share menu, click on "Publish". <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>
4.  Confirm your action by clicking "Publish" again. This action makes the page public and available for various uses. <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>

Once the page is published, you can obtain its public URL by clicking "Share" again and selecting "Copy link" <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, or by copying the URL directly from your browser's address bar <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This URL can then be pasted into external applications, such as PDF output services like pdf4put.com, to load and utilize the [[creating_and_using_notion_templates | document template]]. <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>

> [!CAUTION]
> It is crucial to ensure the [[creating_content_on_notion_pages | Notion page]] is shared and publicly accessible before attempting to use its URL with any external service. <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a> <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>

## Importance of Page Sharing for External Tools

Making a [[creating_content_on_notion_pages | Notion page]] public allows external web services to access and process its content. For example, when [[using_notion_for_pdf_template_creation | generating PDF documents]] in bulk from a [[setting_up_a_notion_database_and_template_for_pdf_generation | Notion database]] using a [[creating_and_using_notion_templates | Notion page]] as a template, the external service needs to "read" the page's structure and placeholder fields (those enclosed in curly brackets) to substitute them with data from the database. <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a> <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>

## Considerations for Relational Properties

If your Notion database utilizes [[setting_up_a_database_in_notion | relational properties]] (linking to other databases), all related databases must also be connected to the same API key that is being used to integrate with the external service. <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a> <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a> This ensures that the external service can seamlessly fetch all necessary data from across the connected databases. <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>