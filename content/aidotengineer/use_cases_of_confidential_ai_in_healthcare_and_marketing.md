---
title: Use cases of confidential AI in healthcare and marketing
videoId: A0PxE39xaMc
---

From: [[aidotengineer]] <br/> 

[[confidential_ai_and_its_impact | AI]] is transforming many sectors, including [[AI in healthcare | healthcare]], finance, automation, and digital marketing <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. However, a significant barrier to its widespread adoption is the lack of trust, particularly concerning the use of sensitive data and proprietary models <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. [[confidential_ai_and_its_impact | Confidential AI]] addresses this by enabling models to run on sensitive data without exposing it <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## The Foundation: Confidential Computing

The core technology behind [[confidential_ai_and_its_impact | confidential AI]] is confidential computing <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This technology solves the critical problem of data and model vulnerability during processing (training, fine-tuning, or inference) <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

At the hardware level, this is achieved through Trusted Execution Environments (TEEs) <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. A TEE is a secure, isolated part of the processor, such as Intel TDX, AMD SEV-SMP, or Nvidia GPU TEs <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. It creates a "confidential environment" where code and data are protected even during execution, invisible to the host OS, hypervisor, or even the hardware owner <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

TEEs also generate a cryptographic attestation, which is a signed proof that a workload ran inside verified hardware using unmodified code <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. This attestation ensures strong assurances that the workload is protected and verifies the authenticity of the TEE and the chip itself <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. In essence, TEEs allow sensitive computations to run securely and provide proof of their intended execution <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. This enables [[AI in healthcare | AI models]] to process sensitive data without exposing either the model or the data <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

## Use Cases of Confidential AI

### Healthcare

In [[AI in healthcare | healthcare]], building or fine-tuning medical [[AI in healthcare | AI models]] is challenging, not due to the model itself, but due to the difficulty of obtaining or getting permission to use raw data <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Hospitals and labs are reluctant to share raw datasets, even if it could improve patient outcomes, due to tight controls, high generation costs, and data siloing <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. Current regulations and security policies also prevent bringing models to the data <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. This leads to months of negotiation for access to even small datasets and makes working across multiple providers' datasets nearly impossible <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. [[confidential_ai_and_its_impact | Confidential AI]] helps [[solving_data_privacy_issues_in_ai_development | solve data privacy issues]] in this sector <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

#### Case Study: BEAL and FDA Documentation Audits

BEAL (Brain Electrophysiology Laboratory) sought to expedite FDA approval for a new epilepsy diagnostic device <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. Perfect documentation, typically requiring two to four weeks of manual audits with NDAs and risks of exposing trade secrets, was necessary <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. Even a minor mistake could cause a 120-day review delay, impacting patient access and ROI <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

To accelerate this, BEAL considered using Titonix's [[role_of_ai_in_research_and_data_analytics | AI-powered audit tool]] <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. The primary concern was keeping BEAL's data and Titonix's model safe from exposure in traditional cloud environments <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

Titonix utilized Super Protocol's [[confidential_ai_and_its_impact | confidential AI]] cloud <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. The audit ran within secure hardware environments (TEEs) using Nvidia H100/H200 GPUs and Intel TDX CPUs <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>. Every step was automated by smart contracts and verified by cryptographic proof <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>. All files and models remained encrypted, readable only inside the secure environment, and completely hidden from Super Protocol, BEAL, Titonix, or any other party <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.

The results were transformative:
*   Audit time drastically reduced from weeks to just one to two hours <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>.
*   Zero risk of leaks, ensuring both BEAL's and Titonix's IP remained fully protected <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.
*   No re-review delays, eliminating 120-day setbacks <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.

This demonstrated that guaranteed confidentiality can transform even highly sensitive processes like FDA clearance audits <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.

### Digital Marketing

In digital marketing and custom analytics, there's a strong desire to fine-tune models on real user behavior, tracking interactions across websites, content, and online services <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. However, privacy laws, internal security rules, and ethical considerations often make working with such data risky or blocked <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This creates a significant gap between what is technically possible and what is legally or ethically permissible <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

#### Case Study: Realize and Mars for Ad Performance

Mars, a confectionary company, runs hundreds of ad campaigns globally, facing substantial budget waste <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. Realize, a company using [[role_of_ai_in_research_and_data_analytics | AI]] to measure ad reactions by analyzing facial expressions, helps brands like Coca-Cola and Mars create more impactful ads <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. To improve their [[role_of_ai_in_research_and_data_analytics | AI]] accuracy, Realize needed more biometric video data from external partners <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.

The challenge arose from privacy laws such as GDPR and CCPA, coupled with data ownership concerns, making providers hesitant to share sensitive footage <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>. For its Mars project, Realize adopted Super Protocol's [[confidential_ai_and_its_impact | confidential AI]] cloud <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. [[case_studies_and_practical_examples_of_ai_implementation | AI training]] occurred within secure TEEs using powerful chips like Nvidia H100/H200s and Intel Xeons <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>. The entire process was automated by smart contracts and verified by hardware and Super Protocol's open-source certification <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. This ensured that data and models remained completely secure, proven to be inaccessible even to the cloud provider, Super Protocol, or Realize themselves <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.

Verifiable confidentiality changed the landscape:
*   Once providers understood their data was truly protected, they shared four times more sensitive footage, increasing the training dataset by 319% <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.
*   This boost improved [[role_of_ai_in_research_and_data_analytics | AI]] accuracy to 75%, on par with human-level performance <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.
*   For Mars, this translated to a 3-5% sales increase across 30 brands in 19 markets <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

This case illustrates that provable data privacy unlocks valuable data, leading to better models, smarter [[role_of_ai_in_research_and_data_analytics | AI]], and tangible business impact <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.

## Conclusion

[[confidential_ai_and_its_impact | Confidential AI]], powered by TEEs and verifiable attestations, offers a practical path forward for developers in industries handling sensitive data <a class="yt-timestamp" data-t="00:43:05">[00:43:05]</a>. It enables running models on private data without exposure, deploying proprietary models without losing control, fine-tuning without compliance risks, and verifying execution with cryptographic proof <a class="yt-timestamp" data-t="00:42:37">[00:42:37]</a>. This technology transforms privacy into performance and confidence into revenue across data-driven industries <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.