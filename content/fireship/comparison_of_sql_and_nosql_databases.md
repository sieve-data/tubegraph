---
title: Comparison of SQL and NoSQL databases
videoId: 2CipVwISumA
---

From: [[fireship]] <br/> 
Databases are a common pain point when building applications <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. Developers frequently debate the advantages of SQL versus NoSQL databases <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## SQL Databases

[[introduction_to_relational_databases_and_sql | SQL databases]] are known for:
*   Safety <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>
*   Security <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>
*   Consistency <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>

In SQL databases, a collection is similar to a table <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. They use foreign keys to join data from multiple collections <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## NoSQL Databases

NoSQL databases are often highlighted for their:
*   Flexibility <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>
*   Scalability <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>
*   Productivity <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>

NoSQL databases, such as document-oriented databases like MongoDB or [[firestore_data_modeling_techniques | Firestore]], manage data in collections <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## FaunaDB's Position

FaunaDB is presented as a cloud database that aims to bridge the gap between SQL and NoSQL, potentially ending the debate between them <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

Key features of FaunaDB that relate to this comparison:
*   **Ease of Use**: It is as easy to use as a document database <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
*   **Scalability**: It scales infinitely in the cloud <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   **Data Modeling**: It can handle complex data modeling use cases found in [[using_faunadb_for_relational_and_graph_data_modeling | relational]], graph, or time series databases <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **ACID Compliance**: FaunaDB is 100% ACID compliant, meaning database transactions are globally consistent, and future reads will reflect the value of the write, even when distributed across many users <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
*   **References**: Documents in FaunaDB can contain references to other documents, which are similar to foreign keys in an [[introduction_to_relational_databases_and_sql | SQL database]] for joining data <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   **History**: It retains all changes to a document over time, creating a copy with changes and archiving the original to history, useful for time series data and time traveling <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.