---
title: AWS Computer Services and Tools
videoId: JIbIYCM48to
---

From: [[fireship]] <br/> 

[[introduction_to_amazon_web_services_aws | Amazon Web Services]] (AWS) launched in 2006 <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> with three initial products: storage buckets, compute instances, and a messaging queue <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Today, AWS offers over 200 services <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, many of which appear to perform similar functions <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. These services aim to meet the needs of virtually every developer <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Niche and Specialized Services

Beyond common applications, AWS offers highly specialized services:
*   **RoboMaker** allows for simulating and testing robots at scale <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   **IoT Core** enables collecting data from robots, updating their software, and managing them remotely once they are deployed <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   **Ground Station** connects to orbiting satellites via Amazon's global network of antennas to collect data <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   **Bracket** facilitates experimenting and researching the future of computing by interacting with a quantum computer <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## The Compute Aisle

Most developers utilize the cloud to solve practical problems, focusing on compute services <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

### Virtual Machines and Scalability

*   **Elastic Compute Cloud (EC2)** was one of the original AWS products <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. It's a fundamental building block that allows users to create virtual computers in the cloud, selecting their operating system, memory, and computing power <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Instances are rented by the second <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. A common use case for an EC2 instance is as a server for a web application <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Elastic Load Balancing (ELB)**, introduced in 2009 <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>, automatically distributes traffic across multiple EC2 instances as an application grows <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **CloudWatch** collects logs and metrics from individual instances <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Auto Scaling** uses data from CloudWatch to define policies that create new instances based on traffic and utilization, ensuring resources scale with demand <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### Platform-as-a-Service and Managed Solutions

*   **Elastic Beanstalk** simplifies deployment by providing an abstraction layer over EC2 and auto-scaling features <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Developers can choose a template, deploy code, and let auto-scaling happen automatically <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. This is often referred to as Platform as a Service (PaaS) <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   **Lightsail** offers a simpler alternative for deploying applications like WordPress sites with a point-and-click interface, minimizing concerns about underlying configuration <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Serverless Computing

*   [[key_serverless_platforms_aws_lambda_google_cloud_functions_azure_functions | Lambda]], launched in 2014 <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, is a Functions-as-a-Service (FaaS) or [[overview_of_cloud_computing_services | serverless computing]] offering <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Users upload code and define events that trigger its execution <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Traffic scaling and networking are handled automatically <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Payment is based only on the exact number of requests and computing time used <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   **Serverless Application Repository** provides pre-built Lambda functions that can be deployed with a single click <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### Hybrid and Edge Computing

*   **Outposts** allows enterprises to rent AWS APIs and run them on their own on-premises infrastructure <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   **Snow Devices** are mini data centers designed to work without internet in remote or hostile environments, such as the Arctic <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Containerization Services

*   **Elastic Container Registry (ECR)** is used to store Docker images <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Elastic Container Service (ECS)** is an API for starting, stopping, and allocating virtual machines to containers, and connecting them to other products like load balancers <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Elastic Kubernetes Service (EKS)** is a tool for running Kubernetes, offering more control over application scaling <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Fargate** makes containers behave like serverless functions, removing the need to allocate EC2 instances for them <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **App Runner**, a new product in 2021 <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>, simplifies deployment of containerized applications by handling orchestration and scaling automatically when pointed to a container image <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

## [[AWS Storage Solutions | Data Storage Solutions]]

Storing data is crucial for applications <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

### Object and Archival Storage

*   **Simple Storage Service (S3)** was the very first product offered by AWS <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. It stores any file or object (like images or videos) and is built on the same infrastructure as Amazon's e-commerce site <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. It's ideal for general-purpose file storage <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Glacier** is used for archiving files that are not accessed frequently, offering lower cost but higher latency <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

### Block and File Storage

*   **Elastic Block Storage (EBS)** provides fast storage with high throughput, ideal for applications with intensive data processing requirements, but requires more manual configuration <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Elastic File System (EFS)** offers highly performant and fully managed file storage with more features, though at a higher cost <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

## [[AWS Database Offerings | Database Offerings]]

AWS offers a variety of databases for structured data <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### NoSQL Databases

*   **SimpleDB** was the first general-purpose NoSQL database on AWS, but is often considered too simple for many use cases <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   **DynamoDB** is a document database designed for easy horizontal scaling <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. It's inexpensive and provides fast read performance, but is less suited for relational data <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   **DocumentDB** is a controversial option that provides a one-to-one mapping of the MongoDB API <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Elasticsearch** (now OpenSearch Service) is an option for building full-text search engines <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

### Relational (SQL) Databases

*   **Amazon Relational Database Service (RDS)** supports various SQL flavors and fully manages tasks like backups, patching, and scaling <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **Aurora** is Amazon's proprietary SQL flavor, compatible with PostgreSQL or MySQL <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. It offers better performance at a lower cost <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. Aurora also provides a serverless option for easier scaling, where users only pay for the actual time the database is in use <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

### Specialized Databases

*   **Neptune** is a graph database optimized for highly connected datasets, such as social graphs or recommendation engines <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   **ElastiCache** is a fully managed version of Redis, an in-memory database that delivers data with extremely low latency <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Timestream** is a time series database with built-in functions for time-based queries and analytics, suitable for data like stock market information <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **Quantum Ledger Database (QLDB)** allows building an immutable set of cryptographically signed transactions, similar to decentralized blockchain technology <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

## [[AWS Machine Learning and Analytics | Analytics and Machine Learning]]

AWS provides tools for analyzing and leveraging data.

### Data Warehousing and Lakes

*   **Redshift** is a data warehouse used by large enterprises to consolidate multiple data sources for combined analysis <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   **AWS Lake Formation** is a tool for creating data lakes, which are repositories for large amounts of unstructured data <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. These can be used alongside data warehouses to query a wider variety of data sources <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

### Data Streaming and Processing

*   **Kinesis** captures real-time data streams from infrastructure, which can then be visualized or processed <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Elastic Map Reduce (EMR)** is a service for operating on massive datasets efficiently using parallel distributed algorithms, supporting frameworks like Apache Spark <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Amazon MSK** is a fully managed service for Apache Kafka, a popular open-source alternative for streaming data <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
*   **Glue** is a [[overview_of_cloud_computing_services | serverless]] product that simplifies Extract, Transform, Load (ETL) processes <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. It connects to other AWS data sources (Aurora, Redshift, S3) and offers Glue Studio for creating jobs without writing source code <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

### [[Artificial intelligence and AIdriven tools | Machine Learning]]

*   **Data Exchange** allows users to purchase and subscribe to high-quality data from third-party sources if they don't have their own <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   **SageMaker** connects to cloud data to build machine learning models using frameworks like TensorFlow or PyTorch <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. It operates on multiple levels to simplify ML, providing a managed Jupyter notebook that can connect to GPU instances for model training and deployment <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
*   **Recognition API** offers image analysis capabilities for classifying objects in images, often outperforming custom-built solutions <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   **Lex** is used to build conversational bots, running on the same technology as Alexa devices <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
*   **DeepRacer** is a physical RC car that users can drive with their own machine learning code, serving as an engaging way to learn about ML <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

## Essential Developer Tools

AWS offers a range of fundamental tools for security, communication, and infrastructure management.

### Security and Identity

*   **Identity and Access Management (IAM)** allows users to create rules and determine access permissions for their AWS accounts <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Cognito** enables user authentication for web and mobile applications, supporting various methods and managing user sessions <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

### Messaging and Communication

*   **Simple Notification Service (SNS)** is used for sending push notifications to users <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Simple Email Service (SES)** handles sending emails to users <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

### Infrastructure Management

*   **CloudFormation** allows users to create infrastructure templates using YAML or JSON <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>, enabling the provisioning of hundreds of different services with a single click <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
*   [[features_and_pricing_of_aws_amplify | Amplify]] provides SDKs to connect front-end applications (iOS, Android, web) to AWS infrastructure from JavaScript frameworks <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

### [[cloud_computing_scalability_and_cost_management | Cost Management]]

*   **AWS Cost Explorer** and **Budgets** are essential tools for monitoring and managing AWS spending <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.