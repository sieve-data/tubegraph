---
title: Confidentiality in AI model training and deployment
videoId: A0PxE39xaMc
---

From: [[aidotengineer]] <br/> 

AI is transforming various sectors, including healthcare, finance, automation, and digital marketing <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. However, a significant barrier to its widespread adoption is trust <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The challenge lies in running models on sensitive data without exposing it, deploying proprietary models without losing control, and collaborating in non-deterministic environments without relying solely on blind trust <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This is precisely what [[confidential_ai_and_its_applications | Confidential AI]] aims to solve <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

[[confidential_ai_and_its_applications | Confidential AI]] offers new possibilities for developers working with sensitive data, proprietary models, or untrusted partners <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

## Core Technology: Confidential Computing and TEEs

The foundation of [[confidential_ai_and_its_applications | Confidential AI]] is confidential computing <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This technology addresses the critical problem that data and models are most vulnerable during processing (training, fine-tuning, or inference), not just when stored or in transit <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

Trusted Execution Environments (TEEs) are central to this <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. A TEE is a secure and isolated part of a processor, such as Intel TDX, AMD SEVSMP, or Nvidia GPU TEs <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. It creates a confidential environment where code and data are protected during execution, even from the host OS, hypervisor, or anyone with system access, including the hardware owner <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. The chip itself provides this isolation using built-in instructions <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

Beyond isolation, a TEE generates a cryptographic attestation <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. This signed proof verifies that a workload ran inside verified hardware using unmodified code <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Attestation provides strong assurances that the workload is hardware-protected and confirms the nature of the workload itself, including that it's running in a real, properly manufactured TEE-capable chip <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This enables running sensitive computations securely and proving they ran as intended <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## Challenges Solved by Confidential AI

The shift to [[confidential_ai_and_its_applications | Confidential AI]] is critical for addressing several real-world challenges faced by developers:

### Healthcare Data Access
Building or fine-tuning medical AI models is often hindered by the difficulty of obtaining or getting permission to use sensitive patient data <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Hospitals and labs are reluctant to share raw datasets due to tight controls, high generation costs, and data silos <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. Current regulations and security policies often prevent bringing models to the data <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. [[confidential_ai_and_its_applications | Confidential AI]] helps solve this by allowing models to run on sensitive data without exposing it <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### Personal AI Agents and Privacy Concerns
Mass adoption of personal AI agents that manage inboxes, calendars, or documents is hampered by the need for deep access to private, sensitive data <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Users worry about data sharing, developers about storage and misuse, and enterprises/regulators about legal ramifications <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. Confidentiality is the missing piece for real-world adoption of these technologies <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

### Digital Marketing and Custom Analytics
In digital marketing, fine-tuning models on real user behavior data (tracking interactions with websites, content) often risks regulatory penalties or ethical breaches due to privacy laws like GDPR and CCPA <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. This creates a significant gap between what's technically possible and what's legally or ethically permissible <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

### AI Model Monetization
Monetizing specialized AI models (e.g., for legal, medical, or financial use) presents a dilemma <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. Model owners want to be paid without giving away their proprietary models or weights <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. Customers, in turn, are unwilling to expose their sensitive data for testing or production <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. [[confidential_ai_and_its_applications | Confidential AI]] allows both parties to benefit without relinquishing control <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

## Proof of Provenance in Model Training
A crucial, often overlooked problem is proving the provenance of trained AI models <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. It's difficult to guarantee that a model was truly trained where and how it was claimed <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. With attested execution, the provenance of data can be assured, proving that inference stage outputs relate solely to the initial data sets <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

## Super Protocol: A Solution for Confidential AI

Traditional cloud setups fall short as they rely on trust and legal contracts rather than provable guarantees <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. Super Protocol was built to make [[confidential_ai_and_its_applications | Confidential AI]] not just possible, but usable <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

Super Protocol is a [[confidential_ai_and_its_applications | Confidential AI]] cloud and marketplace designed for secure collaboration and monetization of AI models, data, and compute <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

Key features include:
*   **TE-agnostic infrastructure**: Runs on Intel, Nvidia, and AMD TEEs, with plans to support future TE developments from major chipmakers <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Edge-ready architecture**: Validated ARM confidential computing compatibility, aiming to deliver end-to-end [[confidential_ai_and_its_applications | Confidential AI]] from personal edge devices to the cloud <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Swarm computing principles**: Scales across distributed GPU nodes, ensuring no single point of failure and automatic workload redistribution <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Decentralized**: Fully decentralized with no human intervention, orchestrated by smart contracts on BNB chain <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
*   **Zero barrier to entry**: No TEE expertise is required to run or attest workloads <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Open source**: All parts of Super Protocol will be open source, functioning as a protocol similar to HTTPS for data protection during AI computing <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

### GPUless, Trustless, Limitless
Super Protocol enables AI workloads that are:
*   **GPUless**: It removes dependency on specific cloud vendors or centralized providers, allowing accelerated AI workloads across independent GPU nodes without needing to buy or rent GPUs for extended periods <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   **Trustless**: Due to the nature of TEEs and open-source architecture, no unauthorized access is technically possible by hardware providers, Super Protocol, or any third party <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. Confidential computing forms the foundation of trustless AI <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
*   **Limitless**: It removes legal, technical, and organizational barriers <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. Traditional cloud platforms impose limits on data, geography, and control <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. Super Protocol allows training, deployment, and monetization of AI across organizations and jurisdictions with full confidentiality and ownership <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>, even for agentic, non-deterministic AI <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.

## Real-world Use Cases

### Digital Marketing: Realize and Mars
Realize, a company using AI to measure ad reactions through facial expressions, needed more biometric video data to improve model accuracy <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. Privacy laws (GDPR, CCPA) and data ownership concerns made data providers reluctant to share sensitive footage <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.

Realize used Super Protocol's [[confidential_ai_and_its_applications | Confidential AI]] cloud for its Mars project <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. AI training ran inside secure TEE environments using powerful chips <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>. The process was automated by smart contracts and verified by hardware and Super Protocol's open-source certification, ensuring data and models remained completely secure and inaccessible to all parties <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

As a result, data providers shared four times more sensitive footage, growing the training set by 319% <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. This boosted accuracy to 75%, on par with human-level performance, and led to a 3-5% sales increase for Mars across 30 brands <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.

### Healthcare: BEAL and Titonix
BEAL (Brain Electrophysiology Laboratory) needed to submit perfect documentation for FDA approval of a new epilepsy diagnostic device <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. Manual audits typically took weeks, risked exposing trade secrets, and could cause significant delays <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. They sought to use Titonix's AI-powered audit tool but had concerns about data and model exposure in traditional cloud environments <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.

Titonix used Super Protocol's [[confidential_ai_and_its_applications | Confidential AI]] cloud <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. The audit ran inside secure hardware TEE environments <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>. All steps were automated, orchestrated by smart contracts, and backed by cryptographic proof <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>. Files and models remained encrypted and readable only within the secure environment, hidden from Super Protocol, BEAL, Titonix, and others <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.

This reduced audit time from weeks to 1-2 hours, eliminated leak risks, protected IP, and prevented FDA re-review delays <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>.

## Practical Application and Demos

### SuperAI Marketplace
The SuperAI Marketplace is built on a confidential and decentralized architecture with no centralized components <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. It uses a blockchain-based ecosystem to manage relationships and financial settlements between model providers, data providers, hardware providers, and clients <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>. [[data_governance_and_compliance_in_ai | Confidential computing]] ensures models remain private, and authors retain full control and ownership, allowing models to be leased but not downloaded <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. Nobody, not even clients, can access the TEE during processing, ensuring models and user data are off-limits <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.

### Secure Automated AI Workflows (Agentic AI)
Super Protocol enables building secure automated AI workflows for processing sensitive data, such as medical data, using tools like N8N <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. By running everything inside TEEs and combining low-code automation with a decentralized infrastructure, it delivers fully confidential, compliant, and verifiable medical AI <a class="yt-timestamp" data-t="00:21:58">[00:21:58]</a>. An example workflow involves a doctor uploading an X-ray image and patient data via a protected web form, which is then processed by an automated workflow in a TEE to analyze the X-ray, clean data, and generate a structured medical report emailed securely to the doctor <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>.

### Distributed Inference
Super Protocol supports distributed inference using VLLM across multiple GPU servers, removing reliance on any single provider <a class="yt-timestamp" data-t="00:26:19">[00:26:19]</a>. While VLLM partitions models by layers for memory efficiency and throughput, it typically runs in unprotected environments <a class="yt-timestamp" data-t="00:26:42">[00:26:42]</a>. Super Protocol secures this by running every VLLM node inside a confidential VM powered by TEE hardware, interconnected over a private overlay network <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>. Data, model weights, and intermediate activations are decrypted and processed only within each confidential environment, with encrypted inter-node communication <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>. This ensures no sensitive material leaves the secure boundary or is exposed to any host <a class="yt-timestamp" data-t="00:27:24">[00:27:24]</a>.

### Moving Beyond Trust: Cryptographic Proofs
Super Protocol replaces blind trust with built-in cryptographic proofs <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>. Every workload produces a cryptographic proof, verifiable independently and transparently down to the hardware level, showing what ran, where, and how, without exposing the actual workload data <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>.

When a workload runs on Super Protocol, it generates a cryptographic attestation – a signed proof from the hardware itself <a class="yt-timestamp" data-t="00:32:20">[00:32:20]</a>. This attestation verifies that the model executed in a real TEE using unmodified code on verified hardware inside a secure, open-source runtime <a class="yt-timestamp" data-t="00:32:35">[00:32:35]</a>. This means users don't have to trust the provider or platform because they can verify the execution <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>. If there are attempts to bypass security, the protocol prevents the application and data from loading and running <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>.

For multi-party training, such as training a cancer detection model on data from Alice's lab and Bob's clinic using Carol's training engine <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>, all three inputs run inside a TEE <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>. No one, including the cloud host, Super Protocol, or the participants, can access the raw data, source code, or weights <a class="yt-timestamp" data-t="00:34:02">[00:34:02]</a>. Training is automated and verified by a trusted engine and smart contracts <a class="yt-timestamp" data-t="00:34:15">[00:34:15]</a>.

Super Protocol automates the process, hides complexity, and removes trust barriers <a class="yt-timestamp" data-t="00:34:36">[00:34:36]</a>. A Confidential Virtual Machine (CVM) is launched and handles multiple jobs <a class="yt-timestamp" data-t="00:34:49">[00:34:49]</a>. On boot, the CVM contacts an open-source certification authority for remote attestation <a class="yt-timestamp" data-t="00:34:57">[00:35:05]</a>. If valid, a certificate is issued. An open-source security mechanism inside the CVM, the trusted loader, then attests itself, creates a signed key pair, and checks every component <a class="yt-timestamp" data-t="00:35:18">[00:35:18]</a>. If any check fails, the process stops to safeguard data and models <a class="yt-timestamp" data-t="00:35:33">[00:35:33]</a>.

Data owners (Alice, Bob) upload encrypted datasets, providing access to the CVM using its public key published on the blockchain <a class="yt-timestamp" data-t="00:36:41">[00:36:41]</a>. Carol places the main order to process the workload <a class="yt-timestamp" data-t="00:37:46">[00:37:46]</a>. The trusted loader verifies hashes of the engine, datasets, and configuration against an approved list; training only begins if all hashes match <a class="yt-timestamp" data-t="00:37:56">[00:37:56]</a>. Data and engine are only decrypted inside the TEE, inaccessible to participants or hardware owners during execution <a class="yt-timestamp" data-t="00:38:13">[00:38:13]</a>. Only Carol receives the encrypted output (trained model, artifacts) <a class="yt-timestamp" data-t="00:38:27">[00:38:27]</a>. After job completion, raw inputs are wiped, and an order report is published on-chain, providing public, tamper-proof evidence of the genuine run <a class="yt-timestamp" data-t="00:41:09">[00:41:09]</a>.

## Conclusion
[[confidential_ai_and_its_applications | Confidential AI]] addresses critical problems in AI deployment and training by enabling secure processing of sensitive data, protection of proprietary models, mitigation of compliance risks, and verifiable execution through cryptographic proofs <a class="yt-timestamp" data-t="00:42:21">[00:42:21]</a>. Super Protocol offers a practical, simple-to-use, transparent, and verifiable path forward for developers, being secure by design, GPUless, trustless, and limitless <a class="yt-timestamp" data-t="00:42:51">[00:42:51]</a>.