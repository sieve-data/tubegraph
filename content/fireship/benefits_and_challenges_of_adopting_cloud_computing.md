---
title: Benefits and challenges of adopting cloud computing
videoId: 1pBuwKwaHp0
---

From: [[fireship]] <br/> 

[[overview_of_cloud_computing_services | Cloud computing]] has seen rapid adoption, with 90% of companies reportedly using it, 60% of workloads running on it, and 30% of IT budgets allocated to it, generating hundreds of billions of dollars in revenue [00:00:24]. It is considered a "win-win" for both service providers and user companies [00:00:47].

## Benefits of Adopting Cloud Computing

*   **Cost Efficiency**
    *   Companies no longer need to purchase and manage their own hardware infrastructure [00:01:02].
    *   Users only pay for the resources they actually consume [00:01:10], with billing often down to the second [00:07:59].
    *   Providers like [[AWS Computer Services and Tools | AWS]] build highly optimized cloud campuses, often located next to rivers for efficient cooling, which can be significantly cheaper than maintaining on-premise server rooms [00:01:27].
    *   [[benefits_of_serverless_architecture | Serverless architecture]] is truly pay-as-you-go, with charges only for each function invocation, making it a cost-effective way to deploy backend code [00:12:12].
*   **[[Cloud computing scalability and cost management | Scalability and Flexibility]]**
    *   Scaling resources up or down requires almost no effort [00:01:12].
    *   Cloud providers offer high uptimes, often guaranteeing 99.99% and beyond through Service Level Agreements (SLAs) [00:01:33].
    *   Workloads can be placed in multiple isolated data centers (zones) within the same region to ensure high availability and redundancy [00:07:29].
    *   Horizontal scaling allows the creation of more virtual machines to distribute workload [00:09:58].
    *   [[benefits_of_serverless_architecture | Serverless functions]] automatically scale code, eliminating the need to manage containers or virtual machines [00:12:06].
*   **Reduced Management Overhead**
    *   Companies do not need to hire dedicated IT staff for wiring and managing hardware [00:01:14].
    *   [[Overview of cloud computing services | Infrastructure-as-a-Service (IaaS)]] abstracts away hardware [00:03:15].
    *   [[Overview of cloud computing services | Platform-as-a-Service (PaaS)]] handles concerns like security, workload scaling, and component integration [00:03:24]. For example, a PaaS can manage the configuration, database provisioning, security, and traffic scaling for an application once the code is uploaded [00:03:56].
    *   [[Overview of cloud computing services | Backend-as-a-Service (BaaS)]] offerings like [[introduction_to_firebase_and_benefits | Firebase]] (Google) and Amplify ([[AWS Computer Services and Tools | AWS]]) provide SDKs that integrate cloud services directly into front-end applications, potentially eliminating the need for any backend code [00:04:08]. These services enable the creation of real-time applications with features like user authentication and cloud databases that are often more reliable than custom-built backends [00:04:23].
*   **Global Reach and Accessibility**
    *   Applications can be deployed in regions closer to end-users for faster performance [00:07:18].
    *   Cloud providers have extensive global data center networks [00:07:44].

## Challenges of Adopting Cloud Computing

*   **Vendor Lock-in**
    *   The more an organization relies on specific services offered by a particular cloud provider, the greater the likelihood of vendor lock-in [00:04:33]. This can make it difficult and costly to migrate to a different provider later.
    *   Using containers can help avoid vendor lock-in as applications can be deployed to any cloud [00:10:56].
    *   Employing a [[hybrid_cloud_and_multicloud_strategies | multi-cloud]] strategy (combining services from multiple public clouds) is also a way to prevent vendor lock-in and optimize pricing [00:05:27].
*   **Cost Management and Quotas**
    *   While pay-as-you-go is a benefit, managing egress (outbound data) can impact the bill [00:09:11].
    *   Although the cloud is often described as scaling infinitely, each service has a quota, which defines the limits of its usage [00:06:08].
*   **Complexity**
    *   While [[benefits_of_serverless_architecture | serverless functions]] offer simplicity, prior to 2019, there was a trade-off regarding control over the runtime environment, making it difficult to install OS-level software [00:12:16]. However, recent developments like [[cloud_functions_and_integration_with_firebase | AWS's runtime API]] and Google Cloud Run address this limitation [00:12:26].
    *   Orchestrating multiple containers and microservices can become complex, requiring tools like Kubernetes [00:11:19].
    *   Manually creating virtual machines is rare for most applications, as there are better ways to manage compute resources [00:09:31].
*   **Data Residency Regulations**
    *   Some companies must adhere to data residency regulations that dictate where customer data can be stored, which influences region selection [00:07:22].