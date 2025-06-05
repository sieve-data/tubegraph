---
title: AWS cloud computing solutions
videoId: JIbIYCM48to
---

From: [[fireship]] <br/> 

[[overview_of_aws_services | Amazon Web Services (AWS)]] launched in 2006 with three initial products: storage buckets, compute instances, and a messaging queue <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Today, AWS offers over 200 services, many of which appear to perform similar functions <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This extensive catalog aims to meet the needs of virtually every developer <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Niche and Specialized Services

Beyond common applications, AWS offers services for highly specialized fields:
*   **RoboMaker**: Used to simulate and test robots at scale <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   **IoT Core**: Collects data from robots, updates their software, and manages them remotely once they are deployed <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   **Ground Station**: Allows connection to Amazon's global network of antennas to collect data from orbiting satellites <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   **Bracket**: For experimenting and researching the future of computing by interacting with a quantum computer <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Compute Services

Most developers leverage AWS for practical problems, starting with compute resources <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

### Core Compute
*   **Elastic Compute Cloud (EC2)**: One of the original AWS products and a fundamental building block. It enables users to create virtual computers in the cloud, selecting their operating system, memory, and computing power, and paying by the second <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. A common use case is hosting a [[web_application_tools_for_developers | web application]] server <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Elastic Load Balancing (ELB)**: Introduced in 2009, this service distributes traffic across multiple EC2 instances automatically, addressing the need for traffic distribution as applications grow <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **CloudWatch**: Collects logs and metrics from individual instances <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   **Auto Scaling**: Uses data from CloudWatch to define policies that automatically create new instances based on traffic and utilization <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### Abstracted & Managed Compute
*   **Elastic Beanstalk**: Provides an additional layer of abstraction over EC2 and auto-scaling features, simplifying the deployment of applications like Ruby on Rails by choosing a template and deploying code <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. This is often referred to as Platform as a Service (PaaS) <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   **Lightsail**: An alternative for those who don't care about the underlying infrastructure and want to deploy something like a WordPress site with a point-and-click interface <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **Lambda**: Launched in 2014, Lambda offers Functions as a Service (FaaS) or [[serverless_architecture_critique | serverless computing]] <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Users upload code and choose an event to trigger its execution, with traffic scaling and networking handled in the background. Payment is only for the exact number of requests and computing time used <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **Serverless Application Repository**: A place to find pre-built functions for quick deployment <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Outposts**: Allows enterprises to rent AWS APIs on their own on-premises infrastructure <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   **Snow devices**: Mini data centers designed to work without internet in remote or hostile environments like the Arctic <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Container Services
Many applications today are standardized with Docker containers for portability <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Elastic Container Registry (ECR)**: Stores Docker images <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Elastic Container Service (ECS)**: An API for starting, stopping, and allocating virtual machines to containers, and connecting them to other products like load balancers <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Elastic Kubernetes Service (EKS)**: For companies desiring more control over application scaling, it's a tool for running Kubernetes <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Fargate**: Makes containers behave like [[serverless_architecture_critique | serverless functions]], removing the need to allocate EC2 instances for containers <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **App Runner**: A newer product (2021) that simplifies container deployment by pointing it to a container image, handling orchestration and scaling automatically <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

## [[aws_storage_and_databases | Storage Services]]

Storing data is a critical aspect of cloud computing <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **Simple Storage Service (S3)**: The very first AWS product <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. It stores any type of file or object (like images or videos) and is based on the same infrastructure as Amazon's e-commerce site <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. It's excellent for general-purpose file storage <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Glacier**: For archiving files not accessed often, offering higher latency but much lower cost than S3 <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Elastic Block Storage (EBS)**: Provides extremely fast storage with high throughput, ideal for applications with intensive data processing requirements, though it requires more manual configuration <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Elastic File System (EFS)**: A highly performant and fully managed file system, offering many features at a higher cost <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

## [[aws_storage_and_databases | Database Services]]

AWS offers a diverse range of [[aws_storage_and_databases | databases]] to store structured data <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### NoSQL Databases
*   **SimpleDB**: The first [[aws_storage_and_databases | database]] on AWS, a general-purpose NoSQL database <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   **DynamoDB**: A document [[aws_storage_and_databases | database]] that is easy to scale horizontally, inexpensive, and provides fast read performance, but is not ideal for modeling relational data <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **DocumentDB**: A controversial option that is technically not MongoDB but offers a one-to-one mapping of the MongoDB API <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Elasticsearch (now OpenSearch Service)**: Useful for building full-text search engines <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

### Relational & Specialized Databases
*   **Relational Database Service (RDS)**: Supports various SQL flavors and fully manages aspects like backups, patching, and scaling <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **Aurora**: Amazon's proprietary SQL flavor, compatible with PostgreSQL or MySQL, offering better performance at a lower cost <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. Aurora also has a [[serverless_architecture_critique | serverless]] option that simplifies scaling, where users pay only for the time the [[aws_storage_and_databases | database]] is in use <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Neptune**: A graph [[aws_storage_and_databases | database]] designed for better performance on highly connected data sets, such as social graphs or recommendation engines <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   **ElastiCache**: A fully managed version of Redis, an in-memory [[aws_storage_and_databases | database]] that delivers data with extremely low latency <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Timestream**: A time series [[aws_storage_and_databases | database]] for time-based data (e.g., stock market data), with built-in functions for time-based queries and analytics features <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **Quantum Ledger Database (QLDB)**: Enables building an immutable set of cryptographically signed transactions, similar to decentralized blockchain technology <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

## [[aws_analytics_and_data_processing | Analytics and Data Processing]]

To analyze data, it first needs to be stored and processed <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Redshift**: A data warehouse often used by large enterprises to consolidate multiple data sources for combined analysis <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   **Lake Formation**: A tool for creating data lakes, which are repositories for large amounts of unstructured data that can be used alongside data warehouses <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
*   **Kinesis**: Captures real-time data streams from infrastructure, allowing visualization in business intelligence tools <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Elastic MapReduce (EMR)**: A service that allows users to operate on massive datasets efficiently using parallel distributed algorithms like Apache Spark <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Amazon MSK**: A fully managed service for Apache Kafka, a popular open-source alternative for streaming data <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Glue**: A [[serverless_architecture_critique | serverless]] product that simplifies Extract, Transform, Load (ETL) processes, connecting to other AWS data sources like Aurora, Redshift, and S3. Glue Studio allows job creation without writing source code <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

## [[aws_machine_learning_tools | Machine Learning]]

Leveraging large datasets for prediction is a key advantage, with AWS offering various [[aws_machine_learning_tools | machine learning]] tools <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
*   **Data Exchange**: Allows purchasing and subscribing to high-quality data from third-party sources if an organization lacks its own <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   **SageMaker**: Connects to data in the cloud to build [[aws_machine_learning_tools | machine learning]] models using frameworks like TensorFlow or PyTorch. It provides a managed Jupyter Notebook that can connect to a GPU instance for training and deployment <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   **Recognition API**: An API for image analysis, capable of classifying objects in images, often outperforming custom-built models <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   **Lex**: For building conversational bots, powered by the same technology as Alexa devices <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
*   **DeepRacer**: A physical race car that can be driven with custom [[aws_machine_learning_tools | machine learning]] code, serving as a fun way to learn about [[aws_machine_learning_tools | machine learning]] <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

## Essential Tools for Developers

Several other tools are widely used by developers across different AWS solutions:
*   **Identity and Access Management (IAM)**: Used to create rules and determine who has access to what on an AWS account <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Cognito**: Enables user authentication for web or mobile applications with various methods and manages user sessions <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
*   **Simple Notification Service (SNS)**: A tool for sending push notifications to users <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Simple Email Service (SES)**: For sending emails to users <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
*   **CloudFormation**: A way to provision services by creating templates in YAML or JSON, allowing the deployment of hundreds of services with a single click <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   **Amplify**: Provides SDKs to connect front-end applications (like those built with JavaScript frameworks, iOS, or Android) to AWS infrastructure <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

## Cost Management

Managing expenses is crucial when using AWS. [[managing_cloud_billing_alerts_and_expenses | AWS Cost Explorer]] and Budgets are essential tools to monitor and control cloud spending <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.