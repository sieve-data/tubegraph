---
title: Cloud computing scalability and cost management
videoId: 1pBuwKwaHp0
---

From: [[fireship]] <br/> 

[[overview_of_cloud_computing_services | Cloud computing]] offers significant advantages in both scalability and cost management, making it a "win-win" for both providers and users <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>. This article explores how cloud services enable dynamic scaling of applications and provide flexible billing models to optimize expenses.

## Why Companies Adopt the Cloud

A significant majority of companies, 90%, are on the cloud, with 60% of workloads running there, and 30% of IT budgets allocated to cloud services <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. This rapid adoption is driven by key benefits:

*   **Simplified Infrastructure Management** Companies can access all necessary infrastructure without buying or managing their own hardware <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.
*   **Reduced Operational Costs** Instead of needing an IT person to wire up equipment or manage server rooms, cloud providers handle the physical infrastructure <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. This can lead to substantial savings, as the cost of managing on-premises infrastructure (e.g., air conditioning for servers) can exceed cloud bills for the same resources <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>. Cloud providers build highly optimized "cloud campuses" near rivers for cooling and use state-of-the-art equipment <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.

## Cloud Billing and Cost Control

One of the primary advantages of [[benefits_and_challenges_of_adopting_cloud_computing | cloud computing]] is its flexible, pay-as-you-go billing model.

*   **Pay-as-You-Go** Users only pay for the resources they actually consume <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. Services are often billed down to the second, allowing instances to be shut off at any time to save costs <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>.
*   **Service Level Agreements (SLAs)** Cloud services come with SLAs, which are contracts guaranteeing certain uptime and error rates. If the provider fails to meet these, financial credits or refunds may be provided <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.
*   **Quotas** While the cloud can seem infinitely scalable, providers set quotas that define the limits for service usage, which clients must adhere to <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>.
*   **Egress Costs** When considering costs, it's important to monitor "egress" (outbound data sent from an instance to the outside world), as it can impact the bill <a class="yt-timestamp" data-t="08:59:00">[08:59:00]</a>. "Ingress" (inbound data) is the opposite <a class="yt-timestamp" data-t="09:05:00">[09:05:00]</a>.

## Managing Scalability in the Cloud

Cloud environments offer various ways to scale applications and manage compute resources:

*   **Vertical Scaling** This involves making a single virtual machine more powerful by adding additional CPU cores and more memory <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>. However, this has limitations <a class="yt-timestamp" data-t="09:54:00">[09:54:00]</a>.
*   **Horizontal Scaling** This method involves creating more virtual machines instead of making existing ones bigger <a class="yt-timestamp" data-t="09:58:00">[09:58:00]</a>. These can be distributed globally, with workload distribution handled by load balancers offered by cloud providers <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>.
*   **Infrastructure as a Service (IaaS)**
    *   [[aws_computer_services_and_tools | AWS]] EC2 (Elastic Compute Cloud) provides virtual computers with RAM, CPU, OS, and IP addresses <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.
    *   Virtual machines (VMs) create a simulated environment that resembles hardware <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. These are low-level building blocks that require the developer to manage and scale them <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.
*   **Platform as a Service (PaaS)**
    *   Services like Elastic Beanstalk, Heroku, and Google App Engine aim to simplify development by handling concerns like security, workload scaling, and configuration <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>. A developer only needs to upload their code, and the platform manages provisioning databases, security, and traffic scaling <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>.
*   **Containerization**
    *   Containers simulate an operating system, sitting on top of an underlying OS to simulate another OS or application <a class="yt-timestamp" data-t="10:47:00">[10:47:00]</a>. This allows applications to be deployed to any cloud, helping to avoid vendor lock-in <a class="yt-timestamp" data-t="10:56:00">[10:56:00]</a>.
    *   [[scaling_pocketbase_applications_on_the_cloud | Kubernetes]] orchestrates multiple containers (microservices), organizing them into "pods" and automatically scaling them up or down based on traffic or utilization <a class="yt-timestamp" data-t="11:22:00">[11:22:00]</a>. When traffic increases, Kubernetes allocates more VMs to run containers; when traffic decreases, it shuts down idle VMs to save money <a class="yt-timestamp" data-t="11:34:00">[11:34:00]</a>.
*   **[[introduction_to_serverless_computing | Serverless Computing]] (Functions as a Service)**
    *   First introduced with [[aws_computer_services_and_tools | AWS Lambda]] in 2014 <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>, [[benefits_of_serverless_architecture | serverless]] allows code to run in response to events (e.g., HTTP requests, database writes) <a class="yt-timestamp" data-t="11:56:00">[11:56:00]</a>.
    *   Code deployed to these functions scales automatically, eliminating concerns about containers or VMs <a class="yt-timestamp" data-t="12:06:00">[12:06:00]</a>.
    *   Billing is truly pay-as-you-go, with payment only for each individual function invocation <a class="yt-timestamp" data-t="12:12:00">[12:12:00]</a>.
    *   Recent advancements, such as the [[aws_computer_services_and_tools | AWS]] runtime API and Google Cloud Run, offer more control over the runtime environment, making serverless a highly cost-effective way to deploy scalable backend code <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>.

## Vendor Lock-in and Cloud Strategies

While convenient, relying heavily on a specific cloud provider's services can lead to "vendor lock-in" <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a>. Companies like Dropbox, initially using [[aws_storage_solutions | AWS S3]] for file storage, eventually moved most customer data to their own data centers in 2016, cutting operating expenses by at least $75 million <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.

*   **[[hybrid_cloud_and_multicloud_strategies | Hybrid Cloud]]** This strategy typically involves large enterprises running a private cloud on their own data centers combined with services on the public cloud <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>. Dropbox, for instance, still uses the cloud for about 10% of file uploads, especially for edge cases and regions not covered by their data centers <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>.
*   **[[hybrid_cloud_and_multicloud_strategies | Multicloud]]** This refers to an architecture that combines services from multiple public clouds, often to prevent vendor lock-in and optimize pricing <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>.

## [[network_communication_and_cloud_computing | Cloud Compute Resources]]

When deploying compute resources, considerations include:

*   **Regions and Zones** Cloud providers have physical data centers located in "regions," with each region containing multiple isolated "zones." Deploying mission-critical workloads across multiple zones within the same region ensures high availability and redundancy <a class="yt-timestamp" data-t="07:14:00">[07:14:00]</a>.
*   **Machine Types** Users can choose machine types that define the amount of memory and CPU for virtual machines, with larger machines costing more <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.
*   **IP Addresses** Instances have both internal (for communication within the same cloud) and external (for Internet communication) IP addresses, which are ephemeral by default but can be reserved as static for services relying on a consistent IP <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>.