---
title: Overview of cloud computing services
videoId: 1pBuwKwaHp0
---

From: [[fireship]] <br/> 

[[benefits_and_challenges_of_adopting_cloud_computing | Cloud computing]] is a rapidly expanding field where infrastructure is hosted remotely and provided as a service over the internet <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. As of 2019, 90% of companies utilize the cloud, with 60% of workloads running on it, allocating 30% of IT budgets to cloud services, generating hundreds of billions of dollars in revenue <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Benefits of Cloud Computing

[[benefits_and_challenges_of_adopting_cloud_computing | Cloud computing]] offers significant advantages for both service providers and users <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Providers like [[introduction_to_amazon_web_services_aws | AWS]] generate substantial revenue, with [[introduction_to_amazon_web_services_aws | AWS]] accounting for over 13% of Amazon's total sales at a higher profit margin than its retail business <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. For customers, it eliminates the need to purchase and manage their own hardware <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

Key benefits for users include:
*   **Cost Efficiency** Customers only pay for what they use <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Large providers build highly optimized "cloud campuses" near rivers for cooling, using state-of-the-art equipment to guarantee high uptimes <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This often makes it more cost-effective than building and maintaining on-premise infrastructure <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **[[cloud_computing_scalability_and_cost_management | Scalability]]** It requires minimal effort to scale resources up or down as needed <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Reduced Overhead** Companies do not need to hire IT personnel to manage physical infrastructure <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Cloud Service Models

Cloud services are categorized based on the level of abstraction provided to the user.

### Infrastructure-as-a-Service (IaaS)

IaaS provides the fundamental building blocks of the cloud, abstracting away hardware concerns <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. It gives developers control over managing and scaling these low-level components <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

*   **Virtual Machines (VMs)** First launched by [[introduction_to_amazon_web_services_aws | AWS]] in 2006 as Elastic Compute Cloud (EC2) <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>, a VM is a virtual computer with its own RAM, CPU, operating system, and IP address for [[network_communication_and_cloud_computing | networking]] <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. When a server is spun up in the cloud, it's a virtual machine, meaning the cloud has virtualized a simulated environment that resembles hardware <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   **[[aws_storage_solutions | Cloud Storage Buckets]]** [[introduction_to_amazon_web_services_aws | AWS]] S3 (Simple Storage Service), also launched in 2006, provides a hard drive with a file system in the cloud for storing data like images and videos <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Dropbox, for example, initially used S3 to store user files, focusing on the software experience rather than building its own infrastructure <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### Platform-as-a-Service (PaaS)

PaaS takes cloud computing to another level by abstracting away not just hardware, but also concerns like security, workload scaling, and integrating components into a cohesive unit <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. Examples include Elastic Beanstalk, Heroku, and Google App Engine <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. With PaaS, a developer uploads their code, and the cloud handles database provisioning, security, and traffic scaling <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

### Backend-as-a-Service (BaaS)

BaaS provides SDKs that integrate the cloud directly into front-end applications, often eliminating the need for any backend code at all <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. Major players include [[cloud_functions_and_integration_with_firebase | Firebase]] from Google and Amplify from [[introduction_to_amazon_web_services_aws | AWS]] <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. With BaaS, developers can create real-time applications with user authentication and cloud databases with just a few lines of JavaScript <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

### [[introduction_to_serverless_computing | Functions-as-a-Service (FaaS) / Serverless Computing]]

First introduced in 2014 with [[introduction_to_amazon_web_services_aws | AWS]] Lambda <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>, FaaS allows code to run in response to events, such as HTTP requests or database writes <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. Code deployed to these functions scales automatically, removing concerns about containers or VMs <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. It operates on a pay-as-you-go model, billing per function invocation <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. Initially, FaaS offered limited control over the runtime environment <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>, but advancements like [[introduction_to_amazon_web_services_aws | AWS]]'s Runtime API and Google's Cloud Run now allow for more flexibility <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. It is generally considered the easiest and most cost-effective way to deploy scalable backend code <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

## Cloud Capabilities and Features

### Service Level Agreements (SLAs)

All cloud services come with an SLA, which is a contract between the user and the cloud provider <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. The provider guarantees certain uptime and error rates and may offer financial credit or refunds if these are not met <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Users also typically have quotas that define the limits of service usage <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

### Identity and Access Management (IAM)

IAM is crucial for securing cloud infrastructure, controlling who can access services and resources <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Security policies can be attached to services, such as storage buckets, to control organizational access <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. Roles can group permissions for reuse throughout the cloud, and can be assigned to third parties like consultants <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. Resource-based policies or service accounts allow machines to communicate with each other, for instance, a virtual machine accessing a database <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

### Compute Resources

*   **Regions and Zones** Cloud providers offer options for creating VMs in specific regions, which are physical locations of data centers <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. Choosing a region closer to end-users can improve speed <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. Each region typically has multiple isolated data centers (zones), allowing for high availability and redundancy by distributing workloads across zones <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. Azure, for example, has the most data centers among cloud providers <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   **Machine Type and OS** Users can select the machine type to define the amount of memory and CPU for a VM <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. The operating system is chosen by selecting a disk image, with various Linux and Windows flavors available <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **Pricing** Cloud resources are generally pay-as-you-go, billed down to the second, with instances able to be shut off at any time <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

### [[network_communication_and_cloud_computing | Networking]]

*   **IP Addresses** Instances have both internal and external IP addresses <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. By default, these are ephemeral, meaning they change if the instance is rebuilt <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. Static IP addresses can be reserved for services that require a consistent address <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. Internal IPs are for communication between instances on the same cloud, while external IPs are for communication with services on the internet <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
*   **Egress and Ingress** Egress refers to outbound data sent from an instance to the outside world, while ingress is inbound data from the outside world into an instance <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. Egress is typically more impactful on billing <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **Cloud Shell** Users can access the command line of an instance directly in the console via a cloud shell session, providing a Linux or Windows terminal environment <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### [[cloud_computing_scalability_and_cost_management | Scalability]]

*   **Vertical Scaling** Involves adding more CPU cores and memory to a single VM to make it more powerful <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Horizontal Scaling** Involves creating more VMs and distributing the workload across them, potentially in regions worldwide <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Load Balancing** Necessary when distributing VMs horizontally to ensure traffic is evenly distributed among instances <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

### Containerization

Containers simulate an operating system, similar to VMs, but they sit on top of an underlying operating system rather than directly on hardware <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This allows applications to be packaged and deployed to any cloud, helping to avoid vendor lock-in <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. Cloud providers offer container registries for uploading and managing containers <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

*   **Kubernetes** For complex applications with multiple microservices running in different containers (e.g., web server, email service, machine learning algorithms), Kubernetes orchestrates these services <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. It organizes containers into "pods" and automatically scales them up or down based on traffic or utilization, allocating or shutting down VMs as needed <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.

## Cloud Strategies

### Vendor Lock-in

A significant drawback of relying heavily on specific cloud services is vendor lock-in, where it becomes difficult to move software off a given cloud provider <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. Dropbox, for instance, moved the majority of its customer data off [[introduction_to_amazon_web_services_aws | AWS]] to its own data centers in 2016, reducing operating expenses <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### [[hybrid_cloud_and_multicloud_strategies | Hybrid Cloud]]

[[hybrid_cloud_and_multicloud_strategies | Hybrid cloud]] refers to enterprises running a private cloud on their own data centers combined with services on the public cloud <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. Dropbox, for example, still uses the cloud for about 10% of its file uploads, particularly for edge cases and regions not covered by its data centers <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. A public cloud is one where anyone can sign up and start using services with an email address and credit card <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

### [[hybrid_cloud_and_multicloud_strategies | Multi-Cloud]]

[[hybrid_cloud_and_multicloud_strategies | Multi-cloud]] describes a single architecture or application that combines services from multiple public clouds <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. This strategy is often employed to prevent vendor lock-in and optimize pricing <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.