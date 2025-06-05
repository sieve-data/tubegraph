---
title: Trusted Execution Environments TE in AI
videoId: A0PxE39xaMc
---

From: [[aidotengineer]] <br/> 

AI is transforming various sectors like healthcare, finance, automation, and digital marketing <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. However, a significant barrier to its widespread adoption is [[building_trust_in_ai_systems|trust]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. [[confidential_ai|Confidential AI]], which leverages Trusted Execution Environments (TEs), aims to solve this by allowing models to run on sensitive data without exposure, deploying proprietary models without loss of control, and enabling collaboration in non-deterministic environments without relying on blind [[building_trust_in_ai_systems|trust]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## What are Trusted Execution Environments (TEs)?

TEs address a critical, often overlooked problem in AI: the vulnerability of data and models during processing (training, fine-tuning, or inference), rather than just during storage or transit <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

At the hardware level, a TE is a secure and isolated part of a processor <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. Examples include:
*   Intel TDX <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>
*   AMD SEV-SMP <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
*   Nvidia GPU TEs <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>

A TE creates a "confidential environment" where code and data are protected even during execution <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. The chip itself provides isolation using instructions built in during manufacturing <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Once a workload enters this environment, it is protected in memory and is invisible to the host operating system, hypervisor, or anyone with system access, including the hardware owner <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

Beyond isolation, a TE also generates a cryptographic attestation <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. This is a signed proof that the workload ran inside verified hardware using unmodified code <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This attestation is crucial for two reasons:
1.  It provides strong assurances that the workload is truly protected by the hardware <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
2.  It allows for verifiable statements about the nature of the workload, confirming it's a real TE in a properly manufactured TE-capable chip <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

In essence, TEs enable sensitive computations to run securely and prove that they ran as intended <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. This means AI models can run on sensitive data without exposing either the model or the data <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. This capability forms the foundation of [[confidential_ai|confidential AI]] <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Real-World Problems Solved by [[confidential_ai|Confidential AI]]

[[confidential_ai|Confidential AI]] addresses several critical real-world challenges faced by developers:

### Healthcare
Building or fine-tuning medical AI models is difficult due to data access <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Hospitals and labs are reluctant to share raw data sets, and clinical data access is tightly controlled, expensive, and often siloed <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. Regulations and security policies prevent bringing models to the data <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. This can lead to months of negotiation for small datasets, and working across multiple providers' data sets is often impossible <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. [[confidential_ai|Confidential AI]] can help solve these data sharing obstacles <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### Personal AI Agents
Mass adoption of personal AI agents (managing inboxes, calendars, documents) is hindered because they require deep access to private, sensitive data <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Users fear data exposure, developers worry about storage security, and enterprises/regulators demand strong guarantees against misuse or lawsuits <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. Confidentiality is the missing piece for their real-world adoption <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### Digital Marketing and Custom Analytics
Fine-tuning models on real user behavior data (tracking website and content interactions) is restricted by privacy laws, internal security rules, and ethical considerations <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. This creates a significant gap between what is technically possible and what is legally or ethically allowed <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### AI Model Monetization
Model owners want to monetize their proprietary models without losing control or giving away their IP <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. Concurrently, customers are unwilling to expose their sensitive data for testing or production <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. [[confidential_ai|Confidential AI]] allows both parties to achieve their goals without relinquishing control <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

### Model Training and Provenance
Proving the origin and training methodology of an AI model, especially when sensitive data is involved, is a typically overlooked problem <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. With attested execution (a core feature of TEs), it becomes possible to guarantee a model was truly trained where and how it was stated, ensuring the provenance of data and that inference outputs relate only to original data sets <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

Traditional cloud setups, built on [[building_trust_in_ai_systems|trust]] and legal contracts, fall short in these areas <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## Super Protocol's Implementation of TEs

Super Protocol is a [[confidential_ai|confidential AI]] cloud and marketplace designed for secure collaboration and monetization of AI models, data, and compute <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. It leverages TEs to provide a "GPUless, trustless, limitless" environment <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

Key aspects of Super Protocol's TE implementation:

*   **TE Agnostic Infrastructure**
    *   Runs on Intel, Nvidia, and AMD TEs <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
    *   Validated ARM confidential computing compatibility, aiming for end-to-end [[confidential_ai|confidential AI]] from personal edge devices to the cloud <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Decentralized Architecture**
    *   Built on swarm computing principles, scaling across distributed GPU nodes without a single point of failure and automatic workload redistribution <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
    *   Fully decentralized with no human intervention, orchestrated by smart contracts on BNB chain <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
*   **Zero Barrier to Entry**
    *   Developers don't need TE expertise to run or attest workloads <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Open Source Protocol**
    *   All parts of Super Protocol are open source, functioning like HTTPS but for AI, protecting data during processing <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
*   **"Trustless" Means Verifiable by Design**
    *   Every workload produces a cryptographic proof, showing what ran, where, and how, without exposing the actual workload data <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>.
    *   When a workload runs on Super Protocol, it generates a cryptographic attestation – a signed proof from the hardware itself <a class="yt-timestamp" data-t="00:32:20">[00:32:20]</a>. This attestation verifies:
        *   The model executed in a real TE <a class="yt-timestamp" data-t="00:32:35">[00:32:35]</a>.
        *   Unmodified code was used <a class="yt-timestamp" data-t="00:32:43">[00:32:43]</a>.
        *   It ran on verified hardware inside a secure open-source runtime <a class="yt-timestamp" data-t="00:32:44">[00:32:44]</a>.
    *   Users don't have to [[building_trust_in_ai_systems|trust]] the provider or platform; they can verify it <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.
    *   If attempts to bypass the TE occur, the protocol prevents the application and data from loading and running, ensuring sensitive data is not exposed <a class="yt-timestamp" data-t="00:32:58">[00:32:58]</a>.

### Multi-Party Collaboration Example
Super Protocol enables secure multi-party collaboration, such as training an AI model for early cancer detection using sensitive data from multiple parties (e.g., Alice's lab, Bob's clinic, Carol's research center) <a class="yt-timestamp" data-t="00:33:13">[00:33:13]</a>.
*   All inputs (data from Alice and Bob, training engine from Carol) run inside a TE <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>.
*   No one—not the cloud host, Super Protocol, or even the participants—can access the raw data, source code, or model weights inside the TE <a class="yt-timestamp" data-t="00:34:02">[00:34:02]</a>.
*   Each party retains full custody of their assets outside the TE <a class="yt-timestamp" data-t="00:34:07">[00:34:07]</a>.
*   Training is fully automated and verified by the engine, Super Protocol's certification center, and smart contracts on BNB chains <a class="yt-timestamp" data-t="00:34:17">[00:34:17]</a>.
*   A Confidential Virtual Machine (CVM) is launched and handles multiple jobs <a class="yt-timestamp" data-t="00:34:49">[00:34:49]</a>.
*   On boot, the CVM contacts an open-source certification authority (also running in confidential mode) for a remote attestation <a class="yt-timestamp" data-t="00:34:57">[00:34:57]</a>. If this check passes, a certificate is issued, proving the CVM is genuine and running inside an attested TE <a class="yt-timestamp" data-t="00:35:05">[00:35:05]</a>.
*   Before any data enters, an open-source security mechanism inside the CVM, the "trusted loader," is attested and gets its own certificate <a class="yt-timestamp" data-t="00:35:17">[00:35:17]</a>. It then checks every component, automatically stopping the process if any check fails to safeguard all parties <a class="yt-timestamp" data-t="00:35:31">[00:35:31]</a>.
*   Carol uploads her engine image to her encrypted storage, providing its hash and source code for verification by data owners <a class="yt-timestamp" data-t="00:35:57">[00:35:57]</a>. Alice and Bob upload their encrypted data sets <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>. They grant access to the specified CVM using the verified engine's hash <a class="yt-timestamp" data-t="00:37:16">[00:37:16]</a>. Only that CVM has the private key to decrypt the data <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>.
*   When the job is submitted, the trusted loader verifies all hashes. Only if every hash matches does training start inside the TE <a class="yt-timestamp" data-t="00:37:56">[00:37:56]</a>. Data and the engine are only decrypted inside the TE, protected from all parties, including the system owner <a class="yt-timestamp" data-t="00:38:13">[00:38:13]</a>.
*   Only Carol receives the encrypted output (the newly trained model and artifacts) <a class="yt-timestamp" data-t="00:38:27">[00:38:27]</a>. Encryption keys never leave the TE <a class="yt-timestamp" data-t="00:38:35">[00:38:35]</a>.
*   Before training begins, an integrity report is signed inside the TE and later published on OPBNB as part of the order report <a class="yt-timestamp" data-t="00:39:53">[00:39:53]</a>. This provides public, tamper-proof evidence that the job ran in a certified environment with approved inputs <a class="yt-timestamp" data-t="00:40:06">[00:40:06]</a>.
*   After every job, all raw inputs are wiped <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a>.

## Benefits of TEs in AI

TEs, particularly through platforms like Super Protocol, offer several key benefits for AI development and deployment:
*   **Data and Model Protection:** Ensures data and models remain secure during execution, protected from host operators and even the platform itself <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Enhanced Collaboration:** Enables secure collaboration on sensitive data sets and proprietary models among multiple parties without exposing their underlying assets <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Regulatory Compliance:** Addresses privacy laws (like GDPR, CCPA) and internal security rules, allowing the use of sensitive data for training and analytics <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Model Monetization:** Allows model owners to monetize their IP without relinquishing control, while customers can use models on their sensitive data securely <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
*   **Verifiable Execution:** Provides cryptographic proof (attestation) that workloads ran as intended on verified hardware with unmodified code, replacing blind [[building_trust_in_ai_systems|trust]] with provable guarantees <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. This addresses [[controversies_and_trust_issues_in_ai_benchmark_systems|trust issues in AI benchmark systems]] and proves provenance.
*   **Unlocks Siloed Data:** By ensuring provable data privacy, TEs facilitate access to previously locked, sensitive data, leading to better models and business impact <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
*   **Reduced Barriers:** Simplifies complex multi-party workflows, removing the need for extensive legal paperwork, manual audits, or deep expertise in confidential computing <a class="yt-timestamp" data-t="00:34:36">[00:34:36]</a>.
*   **Performance and Scalability:** Enables [[efficiency_and_smart_execution_engines_in_ai_applications|distributed inference]] across multiple GPU servers using overlay networks, improving memory efficiency and throughput while maintaining confidentiality <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>.

[[confidential_ai|Confidential AI]] using TEs is not just a concept but a practical path forward for developers to run, scale, and monetize AI workloads securely <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.