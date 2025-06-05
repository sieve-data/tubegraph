---
title: Infrastructure as a Service and Platform as a Service
videoId: 1pBuwKwaHp0
---

From: [[fireship]] <br/> 

[[Overview of cloud computing services | Cloud computing]] offers various service models, with Infrastructure as a Service (IaaS) and Platform as a Service (PaaS) being two fundamental categories that abstract away different layers of the underlying hardware and software stack <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.

## Infrastructure as a Service (IaaS)
The modern cloud can trace its origins back to 2006, when [[Introduction to Amazon Web Services AWS | Amazon]] launched EC2 (Elastic Compute Cloud) and S3 (Simple Storage Service) <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>. These services are foundational examples of IaaS.

*   **EC2 (Elastic Compute Cloud)**: Essentially a virtual computer equipped with its own RAM, CPU, an operating system that can be administered, and an IP address for [[Network communication and cloud computing | networking]] <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>. When a server is created in the cloud, it's referred to as a virtual machine (VM) <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. This VM is a virtualized, simulated environment that resembles a piece of hardware, rather than an allocation of specific physical hardware <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>.
*   **S3 (Simple Storage Service)**: Functions as a hard drive with a file system in the cloud, used for storing data such as images and videos <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>.

IaaS provides the low-level building blocks of the cloud <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>. With IaaS, it is the developer's responsibility to manage and scale these resources <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. IaaS abstracts away the physical hardware, allowing developers to focus on higher-level tasks <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>.

> [!example] Dropbox Case Study
> In its early stages, Dropbox utilized [[AWS Storage Solutions | Amazon S3]] to store its users' files because the company lacked the funds to build out its own infrastructure <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>. This demonstrates how a billion-dollar business can be built by focusing on the front-end user experience, leveraging IaaS for backend needs <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. While Dropbox later moved much of its data to its own data centers to reduce [[cloud_computing_scalability_and_cost_management | operating expenses]], it still uses the cloud for about 10% of its file uploads, especially for edge cases and regions not covered by its data centers, illustrating a [[hybrid_cloud_and_multicloud_strategies | hybrid cloud]] approach <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.

## Platform as a Service (PaaS)
Building upon the availability of IaaS, [[Overview of cloud computing services | Platform as a Service]] (PaaS) emerged to provide an even higher level of abstraction <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>. When developing applications, developers face concerns beyond just hardware, such as security, workload scaling, and integrating various components <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. PaaS aims to address these issues <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.

Common examples of PaaS include:
*   [[AWS Computer Services and Tools | Elastic Beanstalk]] <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>
*   Heroku <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>
*   Google App Engine <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>

With PaaS, the platform is designed to handle the configuration of necessary components like databases and web servers <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>. In theory, a developer only needs to upload their code, and the cloud takes care of provisioning the database, providing security, and scaling the traffic <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>. This model provides a platform for creating Software as a Service (SaaS) <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.

## Beyond PaaS: Backend as a Service (BaaS)
The cloud can further provide Software Development Kits (SDKs) that integrate cloud services directly into front-end applications, potentially eliminating the need for any custom backend code <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>. This model is known as Backend as a Service (BaaS) <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>. Major players in this space include Google's Firebase and [[AWS Computer Services and Tools | Amazon's Amplify]] <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>. BaaS allows for the creation of real-time applications with features like user authentication and cloud database integration with minimal JavaScript code <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.

While BaaS simplifies development, relying heavily on specific cloud services can lead to [[using_apis_and_third_party_services | vendor lock-in]], making it challenging to switch providers later <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a>.