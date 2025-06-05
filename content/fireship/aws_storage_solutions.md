---
title: AWS Storage Solutions
videoId: JIbIYCM48to
---

From: [[fireship]] <br/> 

[[Introduction to Amazon Web Services AWS | Amazon Web Services]] (AWS) launched in 2006 with an initial offering that included storage buckets <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Today, AWS offers a vast array of over 200 services to meet diverse developer needs <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## General Purpose File Storage

*   **Simple Storage Service (S3)**: S3 was the very first product offered by AWS <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. It can store any type of file or object, such as images or videos, and uses the same infrastructure as Amazon's e-commerce site <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. It is ideal for general-purpose file storage <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Glacier**: For files that are not accessed very often, Glacier provides an archiving solution with higher latency but a much lower cost than S3 <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## High-Performance and Specialized Storage

*   **Elastic Block Storage (EBS)**: EBS is designed for applications with intensive data processing requirements, offering extremely fast storage and high throughput <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. It requires more manual configuration by the developer <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   **Elastic File System (EFS)**: EFS provides a highly performant and fully managed file system solution, offering more features but at a higher cost <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

## [[AWS Database Offerings | Database Storage]]

Developers often need to store structured data for their end-users, leading to a wide variety of [[AWS Database Offerings | database products]]:

*   **SimpleDB**: The first database offered on AWS, it is a general-purpose NoSQL database, though often considered too simple for many applications <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **DynamoDB**: A document database that is easy to scale horizontally, inexpensive, and provides fast read performance. However, it is not well-suited for modeling relational data <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   **DocumentDB**: An alternative document database that offers a one-to-one mapping of the MongoDB API <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Amazon Elasticsearch Service**: A managed service for Elasticsearch, which is an excellent option for building full-text search engines <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Amazon Relational Database Service (RDS)**: Supports various SQL flavors (e.g., PostgreSQL, MySQL) and fully manages tasks like backups, patching, and scaling <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **Aurora**: Amazon's proprietary SQL flavor, compatible with PostgreSQL or MySQL. It offers better performance at a lower cost than traditional relational databases <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. Aurora also has a serverless option that simplifies scaling and charges only for the actual time the database is in use <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Neptune**: A graph database designed for better performance on highly connected datasets, such as social graphs or recommendation engines <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   **Elastic Cache**: A fully managed version of Redis, an in-memory database that delivers data to end-users with extremely low latency <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Timestream**: A time series database beneficial for data like stock market fluctuations. It includes built-in functions for time-based queries and analytics features <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **Quantum Ledger Database (QLDB)**: Allows the creation of an immutable set of cryptographically signed transactions, similar to decentralized blockchain technology <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

## [[AWS Machine Learning and Analytics | Data Warehousing and Lakes]]

For analyzing data, AWS provides specialized storage solutions:

*   **Redshift**: A data warehouse commonly used by large enterprises to consolidate multiple structured data sources for combined analysis, aiding in generating meaningful analytics and running [[AWS Machine Learning and Analytics | machine learning]] models <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   **AWS Lake Formation**: A tool for creating data lakes, which are repositories designed to store large amounts of unstructured data <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. These can be used alongside data warehouses to query a wider variety of data sources <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.