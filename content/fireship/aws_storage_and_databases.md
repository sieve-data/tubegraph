---
title: AWS storage and databases
videoId: JIbIYCM48to
---

From: [[fireship]] <br/> 

[[overview_of_aws_services | Amazon Web Services]] (AWS), launched in 2006, initially offered three products, including storage buckets <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Today, AWS provides over 200 services <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Storage Services

Running an application requires storing data in the [[aws_cloud_computing_solutions | cloud]] <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.

*   **Simple Storage Service (S3)**: This was the very first product offered by AWS <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>. S3 can store any type of file or object, such as images or videos <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>, and is built on the same infrastructure as Amazon's e-commerce site <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>. It's suitable for general-purpose file storage <a class="yt-timestamp" data-t="00:57:00">[00:57:00]</a>.
*   **Glacier**: For files not accessed frequently, Glacier offers a lower cost for archival storage, though with higher latency <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Elastic Block Storage (EBS)**: This service is ideal for applications with intensive data processing requirements that need extremely fast storage and high throughput <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. It requires more manual configuration from the developer <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.
*   **Elastic File System (EFS)**: EFS provides a highly performant and fully managed storage option, but at a higher cost <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.

## Database Services

Developers also need to store structured data for their end-users <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>, leading to a variety of database products <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.

*   **SimpleDB**: The first database on AWS, SimpleDB was a general-purpose NoSQL database <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>, but it can be too simple for many use cases <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>.
*   **DynamoDB**: Introduced a few years after SimpleDB, DynamoDB is a document database designed for easy horizontal scaling <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>. It's inexpensive and offers fast read performance, but isn't well-suited for modeling relational data <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>.
*   **DocumentDB**: For those familiar with MongoDB, DocumentDB offers a compatible option <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. It maps the MongoDB API to work around restrictive open-source licensing <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.
*   **Amazon Elasticsearch Service**: Similar to DocumentDB's approach, AWS offers a managed service for Elasticsearch, which is excellent for building full-text search engines <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
*   **Amazon Relational Database Service (RDS)**: The majority of developers opt for traditional relational SQL databases <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>. RDS supports various SQL flavors and fully manages tasks like backups, patching, and scaling <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>.
*   **Aurora**: AWS also provides its own proprietary SQL flavor called Aurora <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. It is compatible with PostgreSQL or MySQL and can offer better performance at a lower cost <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. Aurora also has a serverless option for easier scaling, where payment is only for the actual time the database is in use <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.
*   **Neptune**: While relational databases are general-purpose, Neptune is a graph database <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>. It achieves better performance on highly connected datasets, such as social graphs or recommendation engines <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.
*   **ElastiCache**: If a current database is too slow, ElastiCache is a fully managed version of Redis, an in-memory database that delivers data with extremely low latency <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>.
*   **Timestream**: For time series data, like stock market information, Timestream is a dedicated time series database <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>. It includes built-in functions for time-based queries and additional [[aws_analytics_and_data_processing | features for analytics]] <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.
*   **Quantum Ledger Database (QLDB)**: This database allows building an immutable set of cryptographically signed transactions, similar to decentralized blockchain technology <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.