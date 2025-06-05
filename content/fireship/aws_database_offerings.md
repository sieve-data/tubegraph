---
title: AWS Database Offerings
videoId: JIbIYCM48to
---

From: [[fireship]] <br/> 

[[introduction_to_amazon_web_services_aws | Amazon Web Services]] (AWS) offers a wide range of database solutions to meet diverse application needs, addressing various data models, performance requirements, and scalability preferences. The platform provides over 200 services in total, with many appearing to perform similar functions, including those in the database category <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## NoSQL Databases

### SimpleDB
SimpleDB was the very first database offered on AWS <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>. It is a general-purpose NoSQL database <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>, though it is often considered "too simple" for many common use cases <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>.

### DynamoDB
Introduced a few years after SimpleDB, DynamoDB is a document database designed for high scalability <a class="yt-timestamp" data-t="05:48:00">[05:48:00]</a>. It is known for being easy to scale horizontally, inexpensive, and providing fast read performance <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>. However, it is not well-suited for modeling relational data <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>.

### DocumentDB
For developers familiar with MongoDB, DocumentDB offers an alternative document database option <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>. It provides a one-to-one mapping of the MongoDB API <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.

### Amazon Elasticsearch Service
Similar to the approach taken with DocumentDB, AWS offers a managed service for Elasticsearch, which is a powerful option for building full-text search engines <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.

## Relational (SQL) Databases

For the majority of developers who prefer traditional relational SQL databases <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>, AWS provides robust managed options.

### Amazon Relational Database Service (RDS)
RDS supports a variety of SQL database flavors, including PostgreSQL, MySQL, and more <a class="yt-timestamp" data-t="06:29:00">[06:29:00]</a>. It fully manages essential tasks like backups, patching, and scaling, reducing operational overhead <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>.

### Amazon Aurora
Aurora is AWS's proprietary SQL database flavor <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>. It is compatible with PostgreSQL and MySQL <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>, offering better performance at a lower cost compared to standard RDS options <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>. Aurora also features a serverless option that simplifies scaling and charges only for the actual time the database is in use <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>.

## Specialized Databases

Beyond traditional SQL and NoSQL, AWS offers specialized databases for specific use cases.

### Amazon Neptune
Neptune is a graph database designed to achieve better performance on highly connected datasets <a class="yt-timestamp" data-t="06:58:00">[06:58:00]</a>. It is ideal for applications like social graphs or recommendation engines <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>.

### Amazon Timestream
Timestream is a time series database built for managing time-ordered data, such as stock market data <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>. It includes built-in functions for time-based queries and additional features for analytics <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>.

### Amazon Quantum Ledger Database (QLDB)
QLDB allows users to build an immutable set of cryptographically signed transactions <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>. This service is very similar to decentralized blockchain technology <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>.

## Caching and In-Memory Databases

### Amazon ElastiCache
To accelerate existing databases, ElastiCache provides a fully managed version of Redis <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>. This in-memory database delivers data to end-users with extremely low latency <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>.