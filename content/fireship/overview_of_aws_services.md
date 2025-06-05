---
title: Overview of AWS services
videoId: JIbIYCM48to
---

From: [[fireship]] <br/> 

Amazon Web Services ([[AWS cloud computing solutions | AWS]]) launched in 2006 with three core products: storage buckets, compute instances, and a messaging queue <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Today, [[AWS cloud computing solutions | AWS]] offers over 200 services <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, many of which appear to serve similar purposes <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. These services aim to meet the needs of virtually every developer <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Niche [[AWS cloud computing solutions | AWS]] Offerings

Beyond the common services, [[AWS cloud computing solutions | AWS]] provides tools for specialized use cases:
*   **RoboMaker**: Simulates and tests robots at scale <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   **IoT Core**: Collects data from robots in homes, updates their software, and manages them remotely <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   **Ground Station**: Connects satellites to Amazon's global network of antennas to collect data <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   **Bracket**: Enables experimentation and research into the future of computing by interacting with a quantum computer <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Compute Services

For most practical problems, developers utilize [[AWS cloud computing solutions | AWS]]'s compute services <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

### Virtual Machines & Managed Hosting
*   **Elastic Compute Cloud (EC2)**: One of the original [[AWS cloud computing solutions | AWS]] products and a fundamental building block <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. It allows users to create a virtual computer in the cloud, choosing the operating system, memory, and computing power, paying by the second <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. A common use case is as a server for web applications <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Elastic Load Balancing (ELB)**: Introduced in 2009, this service distributes traffic across multiple [[AWS cloud computing solutions | EC2]] instances automatically <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **CloudWatch**: Collects logs and metrics from individual instances <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   **Auto Scaling**: Uses data from CloudWatch to define policies that create new instances as needed, based on traffic and utilization <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Elastic Beanstalk**: Provides an additional layer of abstraction on top of [[AWS cloud computing solutions | EC2]] and Auto Scaling <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, making it easier to deploy applications like a [[Ruby on Rails framework overview | Ruby on Rails]] app <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This is often referred to as Platform as a Service (PaaS) <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   **Lightsail**: A simpler alternative for deploying static servers like WordPress sites, requiring less concern about underlying configuration <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Serverless Computing
*   **Lambda**: Launched in 2014, Lambda provides [[Serverless architecture critique | serverless computing]] or functions as a service <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Users upload code and choose an event to trigger its execution <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Traffic scaling and networking are handled automatically, and users only pay for the exact number of requests and computing time used <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **Serverless Application Repository**: Offers pre-built functions that can be deployed with a single click <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Outpost**: Allows enterprises to rent [[APIs and thirdparty services in web development | AWS APIs]] to run on their own on-premises infrastructure <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   **Snow Devices**: Mini data centers designed to work without internet in hostile environments, useful for remote interactions with [[AWS cloud computing solutions | AWS]] <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Container Services
*   **Elastic Container Registry (ECR)**: Stores Docker images <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Elastic Container Service (ECS)**: An [[APIs and thirdparty services in web development | API]] for starting, stopping, and allocating virtual machines to containers, and connecting them to other [[AWS cloud computing solutions | AWS]] products like load balancers <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Elastic Kubernetes Service (EKS)**: A tool for running Kubernetes, offering more control over application scaling <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Fargate**: Makes containers behave like [[Serverless architecture critique | serverless]] functions, removing the need to allocate [[AWS cloud computing solutions | EC2]] instances for them <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **App Runner**: A newer product (2021) that simplifies deploying containerized applications to [[AWS cloud computing solutions | AWS]] by handling orchestration and scaling <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

## [[AWS storage and databases | Storage Services]]

Storing data is crucial for applications <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Simple Storage Service (S3)**: The very first product offered by [[AWS cloud computing solutions | AWS]], it can store any type of file or object (like images or videos) <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   **Glacier**: For files not accessed frequently, Glacier offers lower cost but higher latency for archiving <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **Elastic Block Storage (EBS)**: Provides extremely fast storage with high throughput, ideal for applications with intensive data processing requirements, but requires more manual configuration <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Elastic File System (EFS)**: A highly performant and fully managed option, though at a higher cost <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

## [[AWS storage and databases | Database Services]]

[[AWS storage and databases | AWS]] offers a wide variety of database products for structured data <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### NoSQL Databases
*   **SimpleDB**: The first [[AWS storage and databases | database]] on [[AWS cloud computing solutions | AWS]], a general-purpose NoSQL [[AWS storage and databases | database]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   **DynamoDB**: A document [[AWS storage and databases | database]] that is very easy to scale horizontally, inexpensive, and provides fast read performance, but is not ideal for modeling relational data <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **DocumentDB**: A controversial option that provides a one-to-one mapping of the MongoDB [[APIs and thirdparty services in web development | API]] <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Elasticsearch Service**: A great option for building full-text search engines <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

### Relational & Specialized Databases
*   **Relational Database Service (RDS)**: Supports various SQL flavors and fully manages tasks like backups, patching, and scaling <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **Aurora**: Amazon's proprietary SQL flavor, compatible with PostgreSQL or MySQL, offering better performance at a lower cost <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. Aurora also offers a [[Serverless architecture critique | serverless]] option, where users only pay for the actual time the [[AWS storage and databases | database]] is in use <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Neptune**: A graph [[AWS storage and databases | database]] that achieves better performance on highly connected data sets, such as social graphs or recommendation engines <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   **ElastiCache**: A fully managed version of Redis, an in-memory [[AWS storage and databases | database]] that delivers data with extremely low latency <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **Timestream**: A time series [[AWS storage and databases | database]] with built-in functions for time-based queries and analytics features, useful for data like stock market information <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **Quantum Ledger Database (QLDB)**: Allows building an immutable set of cryptographically signed transactions, similar to decentralized blockchain technology <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

## [[AWS analytics and data processing | Analytics and Data Processing]]

[[AWS analytics and data processing | AWS]] provides tools to store and analyze data for insights and machine learning.
*   **Redshift**: A data warehouse often used by large enterprises to consolidate multiple data sources for combined analysis <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   **[[AWS analytics and data processing | AWS]] Lake Formation**: A tool for creating data lakes, which are repositories for large amounts of unstructured data that can be used alongside data warehouses <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
*   **Kinesis**: Captures real-time data streams from infrastructure, allowing visualization in business intelligence tools <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Elastic Map Reduce (EMR)**: A service for operating on massive data sets efficiently with parallel distributed algorithms, often used with stream processing frameworks like Apache Spark <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Amazon Managed Streaming for Apache Kafka (MSK)**: A fully managed service for Apache Kafka, a popular open-source alternative to Kinesis for streaming data <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Glue**: A [[Serverless architecture critique | serverless]] product that simplifies extracting, transforming, and loading (ETL) data <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. It can automatically connect to other [[AWS cloud computing solutions | AWS]] data sources like [[AWS storage and databases | Aurora]], [[AWS analytics and data processing | Redshift]], and [[AWS storage and databases | S3]], and features Glue Studio for creating jobs without writing source code <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

## [[AWS machine learning tools | Machine Learning Services]]

The ability to collect massive amounts of data allows for predicting the future using [[AWS machine learning tools | machine learning]] <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
*   **Data Exchange**: Allows purchasing and subscribing to high-quality data from third-party sources if you don't have your own <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   **SageMaker**: Connects to data in the cloud to build [[AWS machine learning tools | machine learning]] models using frameworks like TensorFlow or PyTorch <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. It provides a managed Jupyter notebook that can connect to a GPU instance for training and deployment <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Recognition [[APIs and thirdparty services in web development | API]]**: For image analysis, it can classify objects and images, often outperforming custom-built solutions <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   **Lex**: Used to build conversational bots, running on the same technology that powers Alexa devices <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
*   **DeepRacer**: A physical RC car that users can drive with their own [[AWS machine learning tools | machine learning]] code, serving as a fun way to learn how [[AWS machine learning tools | machine learning]] works <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

## Essential Developer Tools

Several [[AWS cloud computing solutions | AWS]] tools are essential for a wide variety of developers.
*   **Identity and Access Management (IAM)**: Allows creating rules and determining who has access to what on an [[AWS cloud computing solutions | AWS]] account for security <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Cognito**: Manages user authentication and sessions for web or mobile apps, enabling various login methods <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   **Simple Notification Service (SNS)**: A tool for sending push notifications to users <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Simple Email Service (SES)**: Used for sending emails to users <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **CloudFormation**: Allows creating templates based on infrastructure in YAML or JSON, enabling the provisioning of hundreds of different services with a single click <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   **Amplify**: Provides SDKs to connect to [[AWS cloud computing solutions | AWS]] infrastructure from front-end applications like iOS, Android, or web JavaScript frameworks <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

## Cost Management
*   **[[Tradeoffs in cloud architecture | AWS]] Cost Explorer and Budgets**: Essential tools for managing and monitoring spending on [[AWS cloud computing solutions | AWS]] services <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.