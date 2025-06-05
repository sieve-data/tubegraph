---
title: AI safety and security
videoId: G7aSH6N7qY4
---

From: [[aidotengineer]] <br/> 

Don B., co-founder and CTO for Private S, discusses the importance of building safe and reliable [[challenges_of_ai_agents_in_security | AI agents]] and the challenges involved in their deployment in enterprise environments <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. His company recently open-sourced its solution for [[ai_safety_and_model_interpretability | Safety and Security]] for Generative AI and [[challenges_of_ai_agents_in_security | AI agents]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Key Terminology <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   **[[challenges_of_ai_agents_in_security | AI agents]]**: Autonomous systems capable of their own reasoning, workflow generation, and task execution <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. They can call tasks to perform actions and use tools to make API calls <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   **Tasks**: Specific actions that may utilize Large Language Models (LLMs), Retrieval Augmented Generation (RAGs), or tools <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Tools**: Functions used to retrieve data from the internet, databases, or through service APIs <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **Memories**: Contexts shared between agents, tasks, and tools <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## [[challenges_of_ai_agents_in_security | Challenges of AI Agents in Security]] <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>
Many current agent frameworks run as a single process, meaning agents, tasks, and tools share the same process <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This presents several [[ai_sandbox_security | security]] challenges:
*   **Shared Credentials**: Tools needing database or API access often use service user credentials with super admin privileges <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Within the same process, one tool could technically access credentials meant for another <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Third-Party Library Access**: Any third-party library running within the process can access prompts and other sensitive information <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. This creates a zero-trust issue <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **Insecure LLMs**: If agents or tasks interact with an insecure LLM, it can be exploited <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Autonomous and Non-Deterministic Behavior**: Agents are autonomous by definition, creating their own workflows <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. This leads to "unknown unknowns" in [[ai_sandbox_security | security]], as it's non-deterministic what an agent will do, resulting in a high number of attack vectors <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### Consequences of Improper Agent Design <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>
*   **Unauthorized Access and Data Leakage**: Poorly designed agents can lead to unauthorized access and leakage of sensitive or confidential information <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Safety and Trust Issues**: Unreliable models or unsafe environments (e.g., modified prompts) can lead to incorrect results <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Compliance and Governance**: Many organizations struggle to make agents [[enterprise_ai_within_security_boundaries | enterprise ready]] due to a lack of focus on regulatory compliance and governance during development <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. For example, a credit bureau treats an [[challenges_of_ai_agents_in_security | AI agent]] similarly to a human user, requiring it to adhere to training, regulations (e.g., California resident data consent, international data access), and onboarding processes <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

## Addressing [[ai_safety_and_model_interpretability | Safety and Security]] in [[challenges_of_ai_agents_in_security | AI Agents]] <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>
There is no "silver bullet" for [[ai_sandbox_security | security]] and compliance; a multi-layered approach is necessary <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. This involves three key layers:
1.  [[ai_evaluation_and_risk_scoring | Evaluation]]
2.  Enforcement
3.  Observability

### 1. [[ai_evaluation_and_risk_scoring | Evaluation (Evals)]] <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>
This layer defines the criteria for promoting an agent to production <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. Unlike traditional model evaluations that focus on response quality, [[ai_evaluation_and_risk_scoring | AI agent evals]] must also be [[ai_safety_and_model_interpretability | security and safety focused]] <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. The goal is to generate a [[ai_evaluation_and_risk_scoring | risk score]] to determine if an agent can be promoted or if a third-party agent can be used <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

Similar to traditional software development, [[ai_evaluation_and_risk_scoring | AI agent evaluations]] should include:
*   **Test Coverage**: Ensuring adequate testing when writing code <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Vulnerability Scanning**: For Docker containers <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   **Third-Party Software Scanning**: Checking for Common Vulnerabilities and Exposures (CVEs) and remediating high/critical risks <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Penetration Testing**: To prevent cross-site scripting and other vulnerabilities <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

Specific [[ai_evaluation_and_risk_scoring | evaluations]] for [[challenges_of_ai_agents in_security | AI agents]] include:
*   **Baseline Preservation**: Ensuring changes (e.g., prompt modifications, new libraries, frameworks, or LLMs) don't alter the established baseline behavior <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   **Third-Party LLM and Library Scans**: Verifying that third-party LLMs are not poisoned and meet minimum vulnerability criteria <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Prompt Injection Testing**: Ensuring the application has controls to block prompt injections <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   **Data Leakage Prevention**: Testing to prevent sensitive information from being leaked, especially in [[enterprise_ai_within_security_boundaries | enterprise]] contexts where agents handle confidential data (e.g., HR data) <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **Unauthorized Actions**: Verifying that agents performing actions (e.g., changing data) do so only with proper authorization <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   **Runaway Agent Detection**: Testing for scenarios where agents enter infinite loops due to bad prompts or task/agent design issues <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

### 2. Enforcement <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>
Enforcement is crucial for ensuring the proper implementation of [[ai_sandbox_security | security]] controls <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. [[challenges_of_ai_agents_in_security | AI agents]] operate in a near zero-trust environment due to shared libraries and access to backend systems <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. Key enforcement mechanisms include:
*   **[[authentication_and_authorization_in_ai_systems | Authentication and Authorization]]**: Essential to prevent impersonation and theft of confidential information <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. User identity must be propagated from the initial request through tasks and tools to the final data access or API call point, where policies can be enforced <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. [[challenges_of_ai_agents_in_security | Agents]] have their own roles, but user-specific roles must also be enforced if the agent acts on behalf of a user <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.
*   **Approvals**: Automated workflows can be designed where agents handle routine approvals up to certain thresholds <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. Guardrails can be set to automatically involve a human when limits are exceeded <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
*   **[[ai_sandbox_security | Sandboxing]]**: Providing a secure environment for running agents <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.

### 3. Observability <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>
Observability is critical for [[challenges_of_ai_agents_in_security | AI agents]] due to constantly changing variables like models, frameworks, and third-party libraries <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. User inputs are highly subjective, requiring continuous monitoring of responses and potential Personally Identifiable Information (PII) or confidential data leakage <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
*   **Metrics and Thresholds**: It's impractical to monitor every request <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. Instead, define thresholds and metrics (e.g., failure rates) that trigger alerts when exceeded, indicating misbehaving agents or malicious users <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.
*   **Anomaly Detection**: While still evolving for [[challenges_of_ai_agents_in_security | agents]], this concept from traditional [[ai_sandbox_security | security]] (User Behavior Analytics) will become crucial for detecting if an agent is behaving within accepted boundaries <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.
*   **[[ai_network_infrastructure | Security Posture]]**: All these elements contribute to a real-time [[ai_network_infrastructure | security posture]] that reflects how well the agent is performing in a live environment <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.

## Recap <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>
To ensure [[ai_safety_and_model_interpretability | safety and security]] for [[challenges_of_ai_agents_in_security | AI agents]]:
*   **Preemptive [[ai_evaluation_and_risk_scoring | Eval]]**: Conduct vulnerability assessments to gain confidence in promoting agents to production or using third-party agents <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>.
*   **Proactive Enforcement**: Implement robust guardrails, [[ai_sandbox_security | sandboxes]], and [[authentication_and_authorization_in_ai_systems | enforcement]] mechanisms to run agents securely <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.
*   **Observability**: Maintain real-time monitoring to understand agent performance and quickly fine-tune in case of anomalies <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.

## Further Information <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>
Private S has open-sourced its [[ai_safety_and_model_interpretability | Safety and Security]] solution called `page.ai` <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. They are seeking design partners and contributors <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>.