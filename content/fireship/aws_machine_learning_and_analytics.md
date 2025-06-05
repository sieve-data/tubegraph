---
title: AWS Machine Learning and Analytics
videoId: JIbIYCM48to
---

From: [[fireship]] <br/> 

[[introduction_to_amazon_web_services_aws | Amazon Web Services (AWS)]] launched in 2006 with three core products: storage buckets, compute instances, and a messaging queue <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Today, [[introduction_to_amazon_web_services_aws | AWS]] offers over 200 services designed to meet the needs of virtually every developer <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Among these are comprehensive offerings for data [[aws_computer_services_and_tools | analytics]] and [[artificial_intelligence_and_aidriven_tools | machine learning]].

## Analytics

For analyzing data, [[introduction_to_amazon_web_services_aws | AWS]] provides a range of tools to store, process, and visualize information.

### Data Warehousing and Lakes
*   **Redshift** [[aws_database_offerings | Redshift]] is a data warehouse solution designed to facilitate the analysis of structured data <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. Enterprises often use it to consolidate multiple data sources for unified analysis and [[artificial_intelligence_and_aidriven_tools | machine learning]] initiatives <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   **[[aws_storage_solutions | AWS Lake Formation]]** This tool is used for creating data lakes, which are repositories for large amounts of unstructured data <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. Data lakes can complement data warehouses, allowing for queries across a wider variety of data sources <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

### Real-time Data Streaming and Processing
*   **Kinesis** Kinesis enables the capture of real-time data streams from infrastructure, which can then be visualized in business intelligence tools <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Elastic Map Reduce (EMR)** [[aws_computer_services_and_tools | EMR]] is a service that allows for efficient operation on massive datasets using parallel distributed algorithms, such as those found in stream processing frameworks like Apache Spark <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Amazon MSK** As an alternative to Kinesis for streaming data, Amazon MSK is a fully managed service for Apache Kafka, an open-source streaming platform <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

### Data Integration and Transformation
*   **Glue** Glue is a serverless product designed to simplify the extract, transform, and load (ETL) process for data <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. It can automatically connect to other [[introduction_to_amazon_web_services_aws | AWS]] data sources, including [[aws_database_offerings | Aurora]], [[aws_database_offerings | Redshift]], and [[aws_storage_solutions | S3]] <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. **Glue Studio** allows users to create ETL jobs without writing source code <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Machine Learning

Leveraging large datasets for prediction is a key advantage, and [[introduction_to_amazon_web_services_aws | AWS]] offers many tools in the [[artificial_intelligence_and_aidriven_tools | machine learning]] domain to facilitate this <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

### Data Acquisition for ML
*   **Data Exchange** If an organization lacks its own high-quality data, Data Exchange allows for the purchase and subscription to data from third-party sources <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

### Building and Training Models
*   **SageMaker** Once data is in the cloud, SageMaker can be used to connect to it and build [[artificial_intelligence_and_aidriven_tools | machine learning]] models using frameworks like TensorFlow or PyTorch <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. SageMaker operates on multiple levels to simplify [[artificial_intelligence_and_aidriven_tools | machine learning]], providing a managed Jupyter notebook that can connect to a GPU instance for training and deployment <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. This service is a key component for [[building_and_training_machine_learning_models_in_the_browser | building and training machine learning models]].

### Pre-built [[artificial_intelligence_and_aidriven_tools | AI]] Services
For those who prefer not to build [[artificial_intelligence_and_aidriven_tools | machine learning]] models from scratch, [[introduction_to_amazon_web_services_aws | AWS]] offers pre-trained [[artificial_intelligence_and_aidriven_tools | AI]] services:
*   **Recognition** The Recognition API is a robust option for image analysis, capable of classifying objects and images, often outperforming custom-built solutions <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   **Lex** Lex can be used to build conversational bots, leveraging the same technology that powers Amazon's Alexa devices <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

### Learning and Experimentation
*   **DeepRacer** For an engaging way to learn about [[artificial_intelligence_and_aidriven_tools | machine learning]], DeepRacer is a physical race car that can be driven using custom [[artificial_intelligence_and_aidriven_tools | machine learning]] code <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.