---
title: AI evaluation and risk scoring
videoId: G7aSH6N7qY4
---

From: [[aidotengineer]] <br/> 

Don B, co-founder and CTO for Private S, recently open-sourced a solution for safety and security for AI agents. He is also the creator and PMC member of the open-source project Apache Ranger, which handles data governance for Big Data and is used by cloud providers like AWS, GCP, and Azure <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This article discusses how to build a safe and reliable AI agent, focusing on evaluation and risk scoring.

## Understanding AI Agents <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>

From Don B's perspective, AI agents are autonomous systems capable of their own reasoning and workflow generation <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. They can call tasks to perform actions and use tools to make API calls <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

*   **Tasks** are specific actions that may use Large Language Models (LLMs), Retrieval-Augmented Generation (RAGs), or tools <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Tools** are functions that can fetch data from the internet, databases, or call service APIs <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **Memories** are contexts shared within the agents, tasks, and tools <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

Most current agent frameworks run as a single process, meaning agents, tasks, and tools share the same process <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. This can lead to security vulnerabilities, as credentials (often super admin privileges) and prompts within the process can be accessed by any third-party library <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This creates a "zero trust" issue <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Furthermore, agents' autonomous and non-deterministic nature introduces "unknown unknowns," significantly increasing attack vectors compared to traditional software <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

## Challenges in AI Agent Security and Safety <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>

Key challenges include:
*   **Security:** Improperly designed or implemented agents can lead to unauthorized access and data leakage <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Safety and Trust:** Unreliable models or an unsafe environment (e.g., altered prompts) can result in incorrect outcomes <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Compliance and Governance:** Many AI engineers are focused on getting agents to work, often overlooking critical aspects needed for enterprise readiness <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. Enterprises, such as a major credit bureau, treat AI agents like human users who must adhere to extensive regulations (e.g., data privacy laws like GDPR or California resident data protections) <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. Agents need onboarding processes and training to ensure they follow these regulations before production deployment <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

## Layered Solution for Safe and Reliable AI Agents <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>

Addressing these challenges requires a multi-layered approach <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>, categorized into three areas:

1.  **Evaluations (Evals):** Establishing criteria for production readiness <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
2.  **Enforcement:** Implementing strong controls <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
3.  **Observability:** Monitoring real-world usage and reacting to issues <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

### 1. [[testing_and_evaluation_of_ai_models | Evaluation]] (Evals) and Risk Scoring <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>

Just as traditional software development has gating factors for production deployment (e.g., test coverage, vulnerability scanning, CVE scanning, pen testing) <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>, so too must [[testing_and_evaluation_of_ai_models | AI agents]] <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

[[best_practices_for_ai_evaluation | Evaluation methods]] for AI agents should include:
*   Defining use cases and ground truth to ensure consistency when prompts, libraries, frameworks, or LLMs change <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   Scanning third-party LLMs for vulnerabilities and ensuring they are not poisoned <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   Scanning third-party libraries for Common Vulnerabilities and Exposures (CVEs) <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   [[testing_and_evaluation_of_ai_models | Prompt injection testing]] to ensure the application blocks malicious prompts <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   **Data leakage evaluation:** Crucial for enterprise agents handling sensitive information (e.g., HR data) to prevent malicious users from exploiting loopholes and accessing unauthorized data <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **Unauthorized actions evaluation:** Verifying that agents performing actions (not just read-only) do so only when authorized <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   **Runaway agent evaluation:** Testing for scenarios where agents enter infinite loops due to poor prompts or task definitions <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

> "The goal of this is to come with the risk score at the end of the day so that it gives a confidence that can you put this into production." <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>

This [[importance_of_evaluation_and_metrics_in_ai_systems | evaluation]] helps generate a **risk score**, which dictates whether an agent (whether internal or third-party) is confident enough for production <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

### 2. Enforcement <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>

Enforcement is vital as agents often operate in a [[ai_safety_and_security | zero-trust environment]] <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. Key enforcement mechanisms include:
*   **Authentication and Authorization:** Ensuring the user's identity is propagated through the entire agent-task-tool-API/database call chain <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. This prevents impersonation and ensures access controls are properly applied based on the user's and agent's roles <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
*   **Approvals:** Implementing workflows where agents can perform automated approvals up to a certain threshold <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. Proper guard rails can be set to automatically involve a human when limits are exceeded <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

### 3. Observability <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>

[[ai_safety_and_model_interpretability | Observability]] is particularly crucial for AI agents due to their dynamic nature <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. Unlike traditional software, agents involve rapidly changing models, evolving frameworks, and subjective user inputs <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.

Observability involves:
*   Monitoring user inputs and response behaviors <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
*   Tracking the transmission of Personally Identifiable Information (PII) and confidential data <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
*   Defining **metrics and thresholds** for failure rates <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. Automated alerts should trigger if rates exceed tolerance levels, indicating issues like misbehaving agents or malicious users <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
*   **Anomaly detection:** Similar to User Behavior Analytics (UBA) in traditional security, future systems will increasingly monitor agents' behavior to ensure they operate within accepted boundaries <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.

These observability efforts contribute to a real-time security posture, providing confidence in an agent's live performance <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.

## Conclusion <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>

To ensure safe and reliable AI agents, a layered approach is essential:
*   **Preemptive [[testing_and_evaluation_of_ai_models | evaluation]] and vulnerability assessment** to generate a risk score and determine production readiness <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>.
*   **Proactive enforcement** with robust guard rails and sandboxing to run agents securely <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.
*   **Observability** for real-time monitoring of agent performance, allowing for quick fine-tuning and anomaly detection <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.

Private S has open-sourced their Safety and Security Solutions, called page.ai <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.