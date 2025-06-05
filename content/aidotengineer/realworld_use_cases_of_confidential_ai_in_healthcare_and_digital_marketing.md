---
title: Realworld use cases of confidential AI in healthcare and digital marketing
videoId: A0PxE39xaMc
---

From: [[aidotengineer]] <br/> 

[[confidential_ai_and_its_applications | AI]] is transforming various industries, including healthcare and digital marketing <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. However, a major impediment is trust, specifically how to run models on sensitive data without exposing it, deploy proprietary models without losing control, and collaborate in non-deterministic environments without relying on blind trust <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. [[confidential_ai_and_its_applications | Confidential AI]] addresses these challenges <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Foundation of Confidential AI: Confidential Computing
[[confidential_ai_and_its_applications | Confidential AI]] is built on the foundation of confidential computing <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. The most overlooked problem in [[applications_and_future_of_ai_technology | AI]] is that data and models are most vulnerable during processing (training, fine-tuning, inference), not just when stored or in transit <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Trusted Execution Environments (TEs)
Trusted Execution Environments (TEs) are hardware-level secure and isolated parts of a processor (like Intel TDX, AMD SEV-SMP, or Nvidia GPU TEs) <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. A TE creates a confidential environment where code and data are protected during execution, even from the host OS, hypervisor, or hardware owner <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

Beyond isolation, a TE generates a cryptographic attestation – a signed proof that the workload ran inside verified hardware using unmodified code <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. This attestation provides strong assurance that the workload is truly hardware-protected and confirms that the TE is real and properly manufactured <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. In essence, a TE allows secure execution of sensitive computations and proof of their intended operation <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. This enables running [[applications_and_future_of_ai_technology | AI]] models on sensitive data without exposing either the model or the data <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

## Real-World Problems Solved by Confidential AI

### Healthcare
Building or fine-tuning medical [[applications_and_future_of_ai_technology | AI]] models is challenging due to the difficulty of obtaining or getting permission to use sensitive patient data <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Hospitals and labs are reluctant to share raw datasets, and access to clinical data is tightly controlled, expensive, and often siloed <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. Current regulations and security policies often prevent models from being brought directly to the data <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. This leads to months of negotiation for access to even small datasets, making cross-provider data training nearly impossible <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. [[confidential_ai_and_its_applications | Confidential AI]] helps solve this <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### [[personal_private_ai_agents | Personal AI Agents]]
Mass adoption of [[personal_private_ai_agents | personal AI agents]] (e.g., for managing inboxes or documents) is hindered because they require deep access to private, sensitive data <a class="yt-timestamp" data-t="00:04:50">[00:05:01]</a>. Users fear data exposure, developers worry about storage security, and enterprises/regulators demand strong guarantees against misuse or lawsuits <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. Confidentiality is the missing piece for their real-world adoption <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### Digital Marketing and Custom Analytics
In [[customer_success_with_ai_solutions | digital marketing]] and custom analytics, fine-tuning models on real user behavior is desired <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. However, privacy laws (like GDPR and CCPA), internal security rules, and ethics often block or risk upsetting regulators when working with such data <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This creates a significant gap between technical possibility and legal allowance <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

### [[confidentiality_in_ai_model_training_and_deployment | AI Model Monetization]]
For domain-specific models (legal, medical, financial), developers want to monetize their use without giving away proprietary models or weights <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. Simultaneously, customers are unwilling to expose their sensitive data for testing or production <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. [[confidential_ai_and_its_applications | Confidential AI]] allows both parties to benefit without relinquishing control <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Model Training and Provenance
Proving the provenance of a model (i.e., guaranteeing it was trained where and how stated) is a typically overlooked problem <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. With attested execution, the provenance of the data can be assured, linking inference outputs back to only the original data sets <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

Traditional cloud setups, built on trust and legal contracts, fall short in addressing these limitations <a class="yt-timestamp" data-t="00:07:58">[00:08:01]</a>.

## Super Protocol: Enabling Confidential AI
Super Protocol is a [[enterprise_ai_within_security_boundaries | confidential AI cloud]] and marketplace designed for secure collaboration and monetization of [[applications_and_future_of_ai_technology | AI]] models, data, and compute <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. Key features include:
*   **TE Agnostic Infrastructure:** Runs on Intel, Nvidia, and AMD TEs, with future support for new platforms <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Edge-Ready Architecture:** Validated ARM confidential computing compatibility, aiming for end-to-end [[confidential_ai_and_its_applications | confidential AI]] from personal edge devices to the cloud <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Swarm Computing Principles:** Scales across distributed GPU nodes with no single point of failure and automatic workload redistribution <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   **Decentralized:** Fully decentralized with no human intervention, orchestrated by smart contracts on BNB Chain <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
*   **Zero Barrier Entry:** No TE expertise is required to run or attest workloads <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Open Source:** All parts of Super Protocol are open source, acting as a protocol like HTTPS but for [[applications_and_future_of_ai_technology | AI]], protecting data while it's being processed <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

Super Protocol is "GPUless" in that it removes dependency on specific cloud vendors or centralized providers, allowing accelerated [[applications_and_future_of_ai_technology | AI]] workloads across independent GPU nodes. Users don't need to buy or rent GPUs long-term <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. Thanks to TEs and open-source architecture, unauthorized access is technically impossible, making it the foundation of trustless [[applications_and_future_of_ai_technology | AI]] <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

It is also "limitless" by removing legal, technical, and organizational barriers <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. It bypasses traditional cloud limits on data, geography, and control, especially crucial for agentic, non-deterministic [[applications_and_future_of_ai_technology | AI]] where autonomous agents interact and evolve <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. With Super Protocol, users can train, deploy, and monetize [[applications_and_future_of_ai_technology | AI]] across organizations and jurisdictions with full confidentiality and ownership <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

## Case Studies

### Digital Marketing: Realize and Mars
Realize, a company using [[applications_and_future_of_ai_technology | AI]] to measure ad reactions by analyzing facial expressions, needed more biometric video data to improve accuracy for brands like Coca-Cola and Mars <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. Privacy laws (GDPR, CCPA) and data ownership concerns made providers reluctant to share sensitive footage <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.

Realize used Super Protocol's [[enterprise_ai_within_security_boundaries | confidential AI cloud]] for their Mars project <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. [[confidentiality_in_ai_model_training_and_deployment | AI training]] ran inside secure TEs using Nvidia H100s/H200s and Intel Xeons <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>. Smart contracts automated every step, verified by hardware and Super Protocol's open-source certification, ensuring data and models remained completely secure and inaccessible even to the cloud provider, Super Protocol, or Realize themselves <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

Verifiable confidentiality led to providers sharing four times more sensitive footage, growing the training set by 319% <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. This boost increased accuracy to 75%, on par with human-level performance <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. For Mars, this resulted in a 3-5% sales increase across 30 brands in 19 markets <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.

> "When data privacy is provable, locked data gets unlocked, powering better models, smarter AI, and real business impact." <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>

### Healthcare: BEAL and Titonix
The Brain Electrophysiology Laboratory (BEAL) was racing to submit a new epilepsy diagnostic device to the FDA <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. To get FDA approval, perfect documentation was needed, which typically took two to four weeks of manual audits, multiple NDAs, and risked exposing trade secrets <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>. Even a small mistake could cause a 120-day delay <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>. BEAL wanted to speed this up using Titonix's [[applications_and_future_of_ai_technology | AI]]-powered audit tool but had concerns about keeping BEAL's data and Titonix's model safe from exposure in traditional cloud environments <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.

Titonix used Super Protocol's [[enterprise_ai_within_security_boundaries | confidential AI cloud]] <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>. The audit ran inside secure hardware environments (TEs) using Nvidia H100 and H200 GPUs and Intel TDX CPUs <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>. Every step was automated by smart contracts and backed by cryptographic proof <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>. All files and models stayed encrypted, readable only inside the secure environment, completely hidden from Super Protocol, BEAL, Titonix, or anyone else <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.

The results were substantial: audit time dropped from weeks to just one to two hours <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>. There was zero risk of leaks, both BEAL's and Titonix's IP remained fully protected, and no re-review delays occurred <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>. This helped BEAL move faster, stay secure, and deliver life-saving tools to patients sooner <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.

> "When confidentiality is guaranteed, even the most sensitive and high-stakes processes like FDA clearance audits can be transformed." <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>

## Conclusion
[[confidential_ai_and_its_applications | Confidential AI]], powered by Trusted Execution Environments and platforms like Super Protocol, directly addresses critical real-world challenges across various industries <a class="yt-timestamp" data-t="00:42:21">[00:42:21]</a>. It enables:
*   Running models on private data without exposure <a class="yt-timestamp" data-t="00:42:37">[00:42:37]</a>.
*   Deploying proprietary models without losing control <a class="yt-timestamp" data-t="00:42:40">[00:42:40]</a>.
*   Fine-tuning without compliance risk <a class="yt-timestamp" data-t="00:42:42">[00:42:42]</a>.
*   Verifying execution with cryptographic proof <a class="yt-timestamp" data-t="00:42:45">[00:42:45]</a>.

Super Protocol makes this simple to use, transparent, verifiable, secure by design, GPUless, trustless, and limitless <a class="yt-timestamp" data-t="00:42:53">[00:42:53]</a>. It represents a practical path forward for developers in data-driven industries like healthcare and [[customer_success_with_ai_solutions | digital marketing]] <a class="yt-timestamp" data-t="00:43:03">[00:43:03]</a>.