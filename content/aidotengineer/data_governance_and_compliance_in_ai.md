---
title: Data governance and compliance in AI
videoId: G7aSH6N7qY4
---

From: [[aidotengineer]] <br/> 

AI agents are autonomous systems capable of reasoning, creating their own workflows, performing tasks, and using tools to make API calls <a class="yt-timestamp" data-t="00:00:57">[00:01:09]</a>. Tasks are specific actions that might utilize large language models (LLMs), Retrieval-Augmented Generation (RAGs), or other tools <a class="yt-timestamp" data-t="00:01:13">[00:01:19]</a>. Tools are functions designed to retrieve data from the internet, databases, or service APIs <a class="yt-timestamp" data-t="00:01:24">[00:01:33]</a>, while memories are contexts shared across agents, tasks, and tools <a class="yt-timestamp" data-t="00:01:36">[00:01:39]</a>.

## Security Challenges in AI Agents

A significant challenge arises because most agent frameworks operate as a single process, meaning the agent, tasks, and tools reside within the same environment <a class="yt-timestamp" data-t="00:02:07">[00:02:15]</a>. This configuration means that if a tool requires access to a database or API, it needs to possess the necessary credentials or share tokens <a class="yt-timestamp" data-t="00:02:15">[00:02:24]</a>. These credentials often carry super admin privileges <a class="yt-timestamp" data-t="00:02:28">[00:02:30]</a>.

This shared process introduces security vulnerabilities, as one tool could technically access credentials or prompts intended for another <a class="yt-timestamp" data-t="00:02:33">[00:02:49]</a>. This creates a "zero-trust" issue and a high attack surface <a class="yt-timestamp" data-t="00:02:53">[00:03:33]</a>. Given the autonomous and non-deterministic nature of AI agents, which can generate their own workflows, predicting their exact actions becomes difficult, leading to "unknown unknowns" in security <a class="yt-timestamp" data-t="00:03:10">[00:03:30]</a>.

Key challenges include:
*   **Security:** Improperly designed or implemented agents can lead to unauthorized access and [[confidentiality_in_ai_model_training_and_deployment | data leakages]] of sensitive and confidential information <a class="yt-timestamp" data-t="00:03:46">[00:03:58]</a>.
*   **Safety and Trust:** Unreliable models or an unsafe environment where prompts can be altered may lead to incorrect results <a class="yt-timestamp" data-t="00:04:00">[00:04:14]</a>.
*   **Compliance and Governance:** Many organizations struggle with making AI agents [[enterprise_ai_within_security_boundaries | enterprise-ready]] due to neglected compliance and governance requirements <a class="yt-timestamp" data-t="00:04:16">[00:04:26]</a>. For instance, a credit bureau customer treats AI agents similarly to human users, requiring adherence to strict onboarding, training, and regulatory processes, including regional data regulations (e.g., California resident data consent, Europe data access rules) <a class="yt-timestamp" data-t="00:04:28">[00:05:21]</a>. Without such adherence, agents cannot be moved into production <a class="yt-timestamp" data-t="00:05:23">[00:05:24]</a>.

## Multi-Layered Solutions for Safe and Reliable AI Agents

Addressing these challenges requires a multi-layered approach, as there is "no silver bullet" in security and compliance <a class="yt-timestamp" data-t="00:05:38">[00:05:46]</a>. The proposed solution involves three layers: pre-production evaluation (evals), in-production enforcement, and post-deployment observability <a class="yt-timestamp" data-t="00:05:47">[00:05:50]</a>.

### 1. Pre-Production Evaluation (Evals)

Evals determine the criteria for an agent to enter production, focusing on security and safety rather than just model performance <a class="yt-timestamp" data-t="00:05:53">[00:06:12]</a>. The goal is to generate a risk score to decide if an agent can be promoted to production, even if it's a third-party agent <a class="yt-timestamp" data-t="00:06:16">[00:06:30]</a>.

Similar to traditional software development, AI agents require:
*   **Code Quality:** Ensuring adequate test coverage <a class="yt-timestamp" data-t="00:07:37">[00:07:41]</a>.
*   **Vulnerability Scanning:** For Docker containers and third-party software, including checking for Common Vulnerabilities and Exposures (CVEs) <a class="yt-timestamp" data-t="00:07:44">[00:07:58]</a>.
*   **Penetration Testing:** To identify vulnerabilities like cross-site scripting <a class="yt-timestamp" data-t="00:08:01">[00:08:06]</a>.

Specific evals for AI agents include:
*   **Use Cases and Baselines:** Defining clear use cases and ground truth to ensure that changes (e.g., prompt modifications, new libraries, frameworks, or LLMs) do not alter the baseline behavior <a class="yt-timestamp" data-t="00:08:11">[00:08:27]</a>.
*   **LLM and Library Vulnerability:** Ensuring third-party LLMs are not poisoned and are scanned for vulnerabilities <a class="yt-timestamp" data-t="00:08:31">[00:08:36]</a>. Third-party libraries must meet minimum vulnerability criteria <a class="yt-timestamp" data-t="00:08:38">[00:08:45]</a>.
*   **Prompt Injection Testing:** Verifying that the application has controls to block prompt injections, even if LLMs are generally doing this <a class="yt-timestamp" data-t="00:08:48">[00:09:04]</a>.
*   **[[confidentiality_in_ai_model_training_and_deployment | Data Leakage]] Evals:** Especially critical in [[enterprise_ai_within_security_boundaries | enterprise AI]], agents must not leak sensitive or confidential data. This requires testing to ensure malicious users cannot exploit loopholes to access unauthorized information (e.g., an HR agent leaking salary benefits) <a class="yt-timestamp" data-t="00:09:09">[00:09:53]</a>.
*   **Unauthorized Actions:** For agents that can initiate actions or change data, ensuring these actions are performed by authorized entities <a class="yt-timestamp" data-t="00:09:55">[00:10:11]</a>.
*   **Runaway Agent Testing:** Testing for scenarios where agents enter infinite loops due to bad prompts or task/agent configurations <a class="yt-timestamp" data-t="00:10:11">[00:10:32]</a>.

These evaluations collectively produce a risk score, providing confidence in an agent's readiness for production <a class="yt-timestamp" data-t="00:10:32">[00:10:40]</a>.

### 2. In-Production Enforcement

Enforcement ensures that an agent's strong build is maintained during operation, particularly in a zero-trust environment <a class="yt-timestamp" data-t="00:10:43">[00:10:57]</a>.
*   **Authentication and Authorization:** Crucial for preventing impersonation and theft of confidential information <a class="yt-timestamp" data-t="00:11:18">[00:11:44]</a>. When a user requests an agent, the user's identity must be propagated through the agent, tasks, and tools to the final API call or database access point <a class="yt-timestamp" data-t="00:11:24">[00:11:52]</a>. This ensures that the agent's actions and data access are enforced based on the user's permissions, preventing agents from exceeding their designated roles or accessing data the user is not authorized for <a class="yt-timestamp" data-t="00:11:54">[00:12:20]</a>.
*   **Approvals:** Agents can automate many tasks, but there's a need for automated approval mechanisms <a class="yt-timestamp" data-t="00:12:30">[00:12:51]</a>. This can involve another agent overseeing approvals, with defined thresholds for automatic approval and guardrails to involve human intervention when limits are exceeded <a class="yt-timestamp" data-t="00:12:53">[00:13:11]</a>.

### 3. Post-Deployment Observability

Observability is vital for AI agents due to the numerous variables involved and the rapid evolution of models and frameworks <a class="yt-timestamp" data-t="00:13:56">[00:14:25]</a>.
*   **Continuous Monitoring:** Unlike traditional software, AI agent behavior is highly subjective to user input <a class="yt-timestamp" data-t="00:14:32">[00:14:35]</a>. Monitoring is needed to track how user inputs affect responses and to detect any anomalous outflow of sensitive or confidential data <a class="yt-timestamp" data-t="00:14:38">[00:15:11]</a>.
*   **Thresholds and Metrics:** It's impractical to monitor every request <a class="yt-timestamp" data-t="00:15:15">[00:15:19]</a>. Establishing thresholds and metrics, such as failure rates, can trigger alerts for investigation when anomalies occur, potentially indicating misbehaving agents or malicious users <a class="yt-timestamp" data-t="00:15:21">[00:15:53]</a>.
*   **Anomaly Detection:** Similar to user behavior analytics in traditional security, anomaly detection for agents aims to ensure they operate within accepted boundaries <a class="yt-timestamp" data-t="00:15:53">[00:16:24]</a>. This leads to a real-time security posture, indicating how well the agent is performing in a live environment <a class="yt-timestamp" data-t="00:16:27">[00:16:33]</a>.

In summary, a comprehensive approach involves preemptive vulnerability evaluation for a risk score, proactive enforcement with guardrails and sandboxing for secure operation, and robust observability for real-time monitoring and anomaly detection to fine-tune agents <a class="yt-timestamp" data-t="00:16:42">[00:17:24]</a>. Private AI has open-sourced their Safety and Security Solutions called page.ai to contribute to this field <a class="yt-timestamp" data-t="00:17:28">[00:17:34]</a>.