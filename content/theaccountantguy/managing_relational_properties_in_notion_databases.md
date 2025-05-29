---
title: Managing relational properties in Notion databases
videoId: 5lnQYIpvjnM
---

From: [[theaccountantguy]] <br/> 

When [[creating_and_managing_databases_in_notion | creating and managing databases]] in Notion, it's possible to include [[using_rollup_and_relation_properties_in_notion | relation properties]] <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. These properties link entries in one database to entries in [[creating_a_database_in_notion | another database]] <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>, enabling [[tracking_relationships_using_notion | tracking relationships]] between different sets of information.

## Connecting Relational Databases with API Keys

For applications that interact with your Notion data, such as generating PDF documents in bulk, it is crucial that any databases linked via [[using_rollup_and_relation_properties_in_notion | relation properties]] are also properly connected to the API key being used <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

> "If you are using any relation properties in the database, make sure that the relational database is also connected with the same API key." <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>

### Steps for Ensuring Connectivity

1.  **Generate an API Key**: An API key connects your database to external applications <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
2.  **Connect the Primary Database**: Ensure your main database is connected to the API key <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
3.  **Connect All Related Databases**: If you add a column that is [[using_rollup_and_relation_properties_in_notion | related to another database]] using a relation property, this second database *must also* be connected with the same API key <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

By ensuring that all databases involved in [[tracking_relationships_using_notion | relational properties]] are connected to the correct API key, operations will function seamlessly <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.