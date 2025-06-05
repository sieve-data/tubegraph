---
title: AWS analytics and data processing
videoId: JIbIYCM48to
---

From: [[fireship]] <br/> 

[[overview_of_aws_services | Amazon Web Services (AWS)]] offers a suite of tools for analytics and data processing, enabling users to store, query, analyze, and gain insights from vast amounts of data <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

## Data Warehousing
To analyze data, a primary step is to store it in a structured way <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Redshift** is a data warehouse service, often used by large enterprises to consolidate multiple data sources from their business <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. By having all data in one location, it becomes easier to generate meaningful analytics and run [[aws_machine_learning_tools | machine learning]] models <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## Data Lakes
While data warehouses handle structured data, there's also a need to manage large amounts of unstructured data <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **AWS Lake Formation** is a tool for creating data lakes, which are repositories designed to store large volumes of unstructured data <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. These data lakes can be used alongside data warehouses to query a wider variety of data sources <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

## Real-time Data Streaming
For analyzing data as it arrives:
*   **Kinesis** enables the capture of real-time streams from infrastructure, allowing users to visualize this data in their preferred business intelligence tools <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Apache Kafka** is a popular open-source alternative for streaming data <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. [[overview_of_aws_services | Amazon]] offers **Amazon MSK** (Managed Streaming for Kafka) as a fully managed service for Apache Kafka <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

## Massive Data Processing
For operating on large datasets:
*   **Elastic Map Reduce (EMR)** is a service that allows users to process massive datasets efficiently using parallel distributed algorithms <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. It can run stream processing frameworks like Apache Spark <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

## ETL (Extract, Transform, Load)
Simplifying the data processing pipeline:
*   **Glue** is a serverless product that simplifies the process of extracting, transforming, and loading data <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. It can automatically connect to other [[aws_storage_and_databases | AWS data sources]] like [[aws_storage_and_databases | Aurora]], [[aws_storage_and_databases | Redshift]], and [[aws_storage_and_databases | S3]] <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
    *   **Glue Studio** is a tool within Glue that allows users to create ETL jobs without needing to write any source code <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

A significant benefit of collecting massive amounts of data through these services is the ability to use it for predictive analytics and [[aws_machine_learning_tools | machine learning]] <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.