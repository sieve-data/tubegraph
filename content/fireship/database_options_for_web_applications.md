---
title: Database Options for Web Applications
videoId: Sxxw3qtb3_g
---

From: [[fireship]] <br/> 

When developing a web application, choosing the right database is one of the most critical decisions for the backend layer <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>. The database stores user-generated data <a class="yt-timestamp" data-t="01:30:46">[01:30:46]</a>.

## Types of Databases

### Relational Databases (SQL)
Relational databases like MySQL and PostgreSQL are the most popular database option <a class="yt-timestamp" data-t="05:58:00">[05:58:00]</a>. They excel at handling relationships between data, making them suitable for complex data structures <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>. However, they are generally less flexible to changing requirements and can be more expensive to operate compared to some other options <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>. MySQL was part of the original LAMP stack <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a> and is considered a "gold standard" <a class="yt-timestamp" data-t="06:16:00">[06:16:00]</a>.

### NoSQL Document Databases
NoSQL document databases, such as MongoDB and Firestore, are known for being easy to learn, inexpensive, and capable of scaling to nearly any workload <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>. However, they may struggle to model certain types of relationships, such as a social graph <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>. MongoDB is a core component of the popular MEAN stack <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.

### In-Memory Databases
Redis is an example of an in-memory database often used as a cache <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>. It stores data in memory, allowing for much faster reads compared to disk-based databases <a class="yt-timestamp" data-t="06:28:00">[06:28:00]</a>. It can be added to a stack to improve performance for applications that might otherwise face speed issues at scale <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>.

### Graph Databases
More exotic options like graph databases also exist, though they are not detailed in this context <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>.

## [[comparison_of_sql_and_nosql_databases | Database Comparison Summary]]

| Feature              | Relational (e.g., MySQL)                                  | NoSQL Document (e.g., MongoDB, Firestore)                       | In-Memory (e.g., Redis)            |
| :------------------- | :-------------------------------------------------------- | :-------------------------------------------------------------- | :--------------------------------- |
| **Relationship Handling** | Great at handling relationships <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>    | May struggle with complex relationships <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a> | N/A (typically used for caching) |
| **Flexibility**      | Less flexible to changing requirements <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a> | More flexible to changing requirements                      | High                             |
| **Cost**             | Generally more expensive to operate <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>  | Inexpensive <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>                               | Can be cost-effective for caching  |
| **Scalability**      | Can scale, but often with more complexity                 | Can scale to practically any workload <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a> | Excellent for read-heavy workloads |
| **Ease of Learning** | Moderate to High                                        | Easy to learn <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>                                 | Moderate                         |

## Simplified Database Solutions

For simpler web applications, services like [[RealTime Database Implementation | Firebase]] offer a document database that can scale without the need for a separate backend server <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>. Firebase also handles user authentication and can be easily integrated into an application by adding a script tag to the document <a class="yt-timestamp" data-t="10:22:00">[10:22:00]</a>. This approach can eliminate the need for complex backend infrastructure like Docker, Kubernetes, or Terraform <a class="yt-timestamp" data-t="10:42:00">[10:42:00]</a>. This simplified approach is part of the "Petite Fire stack" <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>.