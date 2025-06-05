---
title: Introduction to Amazon Web Services AWS
videoId: JIbIYCM48to
---

From: [[fireship]] <br/> 

[[overview_of_cloud_computing_services | Amazon Web Services (AWS)]] launched in 2006 with three initial products: storage buckets, compute instances, and a messaging queue <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Today, [[overview_of_cloud_computing_services | AWS]] offers over 200 services designed to meet the needs of virtually every developer <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Specialized Services

[[overview_of_cloud_computing_services | AWS]] provides services for highly specialized use cases:
*   **RoboMaker**: Used for simulating and testing robots at scale <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   **IoT Core**: Enables data collection, software updates, and remote management for robots in people's homes <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   **Ground Station**: Allows connection to Amazon's global network of antennas to collect data from orbiting satellites <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   **Braket**: A service for experimenting and researching the future of computing by interacting with a quantum computer <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## [[aws_computer_services_and_tools | Compute Services]]

[[aws_computer_services_and_tools | Compute services]] are foundational for running applications in the cloud.
*   **[[aws_computer_services_and_tools | Elastic Compute Cloud (EC2)]]**: One of the original [[overview_of_cloud_computing_services | AWS]] products, [[aws_computer_services_and_tools | EC2]] allows users to create virtual computers in the cloud <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Users can choose their operating system, memory, and computing power, renting space by the second <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. A common use case is as a server for a [[introduction_to_web_development | web application]] <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Elastic Load Balancing (ELB)**: Introduced in 2009, ELB automatically distributes traffic across multiple [[aws_computer_services_and_tools | EC2]] instances <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **CloudWatch**: Collects logs and metrics from individual instances, which can be used to inform Auto Scaling policies <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   **Auto Scaling**: Defines policies to create new instances as needed based on traffic and current infrastructure utilization <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Elastic Beanstalk**: Provides an additional layer of abstraction on top of [[aws_computer_services_and_tools | EC2]] and Auto Scaling <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. It simplifies deployment by allowing users to choose a template and deploy code, with auto-scaling handled automatically <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. This is often referred to as Platform as a Service (PaaS) <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   **LightSail**: An alternative for simpler deployments like a WordPress site, offering a point-and-click interface that minimizes concern about underlying configuration <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **[[introduction_to_serverless_computing | Lambda]]**: Released in 2014, [[introduction_to_serverless_computing | Lambda]] enables functions as a service, or [[introduction_to_serverless_computing | serverless computing]] <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Users upload code and define events that trigger its execution; traffic scaling and networking are handled in the background, and payment is only for the exact number of requests and computing time used <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **Serverless Application Repository**: A place to find pre-built functions that can be deployed with a single click <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **Outpost**: Allows enterprises to rent [[overview_of_cloud_computing_services | AWS APIs]] on their own on-premises infrastructure <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   **Snow Devices**: Mini data centers designed to work without internet in remote or hostile environments <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

### Container Services
[[aws_computer_services_and_tools | AWS]] also provides robust support for Docker containers.
*   **Elastic Container Registry (ECR)**: Used to upload and store Docker images <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Elastic Container Service (ECS)**: An [[introduction_to_restful_apis | API]] for starting, stopping, and allocating virtual machines to containers, and connecting them to other products like load balancers <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Elastic Kubernetes Service (EKS)**: A tool for running Kubernetes, offering more control over application scaling <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Fargate**: Makes containers behave like [[introduction_to_serverless_computing | serverless]] functions, removing the need to allocate [[aws_computer_services_and_tools | EC2]] instances for containers <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **App Runner**: A newer product (2021) that simplifies container deployment by handling orchestration and scaling when pointed to a container image <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

## [[aws_storage_solutions | Storage Solutions]]

Storing data in the cloud is a critical aspect of application development.
*   **Simple Storage Service (S3)**: The very first product offered by [[overview_of_cloud_computing_services | AWS]] <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. [[aws_storage_solutions | S3]] can store any type of file or object (like images or videos) and is built on the same infrastructure as Amazon's e-commerce site <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. It is excellent for general-purpose file storage <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Glacier**: For files not accessed frequently, Glacier offers higher latency but a much lower cost for archiving <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Elastic Block Storage (EBS)**: Ideal for applications with intensive data processing requirements, providing extremely fast storage with high throughput <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. It requires more manual configuration <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   **Elastic File System (EFS)**: A highly performant and fully managed storage option that provides additional features at a higher cost <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

## [[aws_database_offerings | Database Offerings]]

[[aws_database_offerings | AWS]] offers a wide array of [[aws_database_offerings | database]] products for various structured data needs.
*   **SimpleDB**: The first [[aws_database_offerings | database]] on [[overview_of_cloud_computing_services | AWS]], a general-purpose NoSQL [[aws_database_offerings | database]], though often considered too simple for most applications <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   **DynamoDB**: A document [[aws_database_offerings | database]] that is easy to scale horizontally, inexpensive, and provides fast read performance <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. It is not ideal for modeling relational data <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   **DocumentDB**: Another document [[aws_database_offerings | database]] option, compatible with MongoDB [[introduction_to_restful_apis | API]] <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Amazon Elasticsearch**: A great option for building full-text search engines <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   **Amazon Relational Database Service (RDS)**: Supports various SQL flavors and fully manages aspects like backups, patching, and scaling for traditional relational SQL [[aws_database_offerings | databases]] <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **Aurora**: [[overview_of_cloud_computing_services | Amazon]]'s proprietary SQL flavor, compatible with PostgreSQL or MySQL, offering better performance at a lower cost <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. Aurora also provides a [[introduction_to_serverless_computing | serverless]] option for easier scaling, where users pay only for the actual time the [[aws_database_offerings | database]] is in use <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
*   **Neptune**: A graph [[aws_database_offerings | database]] that delivers better performance on highly connected datasets, such as social graphs or recommendation engines <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   **ElastiCache**: A fully managed version of Redis, an in-memory [[aws_database_offerings | database]] that provides data to end-users with extremely low latency <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Timestream**: A time-series [[aws_database_offerings | database]] with built-in functions for time-based queries and analytics, useful for data like stock market fluctuations <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **Quantum Ledger Database (QLDB)**: Allows building an immutable set of cryptographically signed transactions, similar to decentralized blockchain technology <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

## [[aws_machine_learning_and_analytics | Machine Learning and Analytics]]

[[aws_machine_learning_and_analytics | AWS]] provides tools for data analysis and [[aws_machine_learning_and_analytics | machine learning]].
*   **Redshift**: A data warehouse for storing and analyzing data, often used by large enterprises to consolidate data from various sources <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   **AWS Lake Formation**: A tool for creating data lakes, which are repositories for large amounts of unstructured data that can be used alongside data warehouses <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
*   **Kinesis**: Used to capture real-time data streams from infrastructure, enabling visualization in business intelligence tools <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Elastic MapReduce (EMR)**: A service that allows efficient operation on massive datasets using parallel distributed algorithms, supporting stream processing frameworks like Apache Spark <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Amazon Managed Streaming for Apache Kafka (MSK)**: A fully managed service for Apache Kafka, a popular open-source alternative for streaming data <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Glue**: A [[introduction_to_serverless_computing | serverless]] product that simplifies extracting, transforming, and loading (ETL) data <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. It connects to other [[overview_of_cloud_computing_services | AWS]] data sources and includes Glue Studio for creating jobs without writing source code <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   **Data Exchange**: Allows users to purchase and subscribe to high-quality data from third-party sources if they don't have their own <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   **SageMaker**: Connects to data in the cloud to build [[aws_machine_learning_and_analytics | machine learning]] models using frameworks like TensorFlow or PyTorch <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. It provides a managed Jupyter notebook that can connect to a GPU instance for training and deploying models <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
*   **Recognition API**: An [[introduction_to_restful_apis | API]] for image analysis that can classify objects in images <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   **Lex**: Used to build conversational bots, running on the same technology that powers Alexa devices <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
*   **DeepRacer**: A physical race car that can be driven with custom [[aws_machine_learning_and_analytics | machine learning]] code, serving as an interactive way to learn about [[aws_machine_learning_and_analytics | machine learning]] <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

## Essential Developer Tools and Management

[[overview_of_cloud_computing_services | AWS]] offers several essential tools for security, communication, and infrastructure management.
*   **Identity and Access Management (IAM)**: Used to create rules and determine who has access to what on an [[overview_of_cloud_computing_services | AWS]] account <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Cognito**: Enables user login for web or mobile apps with various authentication methods and manages user sessions <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
*   **Simple Notification Service (SNS)**: A tool for sending push notifications to users <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Simple Email Service (SES)**: Used for sending emails to users <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
*   **CloudFormation**: Allows users to create templates based on their infrastructure in YAML or JSON, enabling provisioning of hundreds of services with a single click <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   **[[features_and_pricing_of_aws_amplify | Amplify]]**: Provides SDKs to connect front-end applications (like JavaScript frameworks, iOS, or Android) to [[overview_of_cloud_computing_services | AWS]] infrastructure <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **AWS Cost Explorer and Budgets**: Tools for managing and monitoring [[overview_of_cloud_computing_services | AWS]] costs <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.