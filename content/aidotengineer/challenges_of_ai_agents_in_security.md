---
title: Challenges of AI agents in security
videoId: G7aSH6N7qY4
---

From: [[aidotengineer]] <br/> 

AI agents are defined as autonomous systems capable of reasoning, creating their own workflows, calling tasks, and using tools to make API calls [00:00:57]. Tasks are specific actions that may use LLMs, RAGs, or tools [00:01:13]. Tools are functions used to retrieve data from the internet, databases, or service APIs [00:01:24]. Memories are contexts shared between agents, tasks, and tools [00:01:36].

## Inherent Security Risks of Current AI Agent Implementation

Current agent frameworks often run as a single process where the agent, task, and tools reside in the same process [00:02:03]. This architecture presents several [[challenges_with_current_ai_implementation | challenges]]:
*   **Shared Credentials**: If a tool needs access to a database or an API, it requires credentials or share tokens, which are often service user credentials with super admin privileges [00:02:15].
*   **Process-level Access**: Within the same process, one tool can technically access credentials meant for another [00:02:33]. Similarly, any third-party library running within the process can access prompts and other data [00:02:47]. This creates an unsecure, "zero trust" environment [00:02:51].
*   **Insecure LLMs**: If agents and tasks communicate with unsecured LLMs, these can be exploited [00:02:58].
*   **Autonomous and Non-Deterministic Behavior**: Agents are autonomous by definition, meaning they generate their own workflows based on tasks [00:03:10]. This non-deterministic nature introduces "unknown unknowns" in security, making it difficult to predict what an agent might do [00:03:21]. The attack vectors in a typical AI agent are significantly higher compared to traditional software [00:03:30].

## Major [[challenges_in_developing_ai_agents | Challenges]] with AI Agent Security

Due to these inherent risks, several [[challenges_in_developing_ai_agents | challenges]] arise when building and deploying AI agents:

### Security Risks
*   Improperly designed or implemented agents can lead to unauthorized access [00:03:46].
*   Data leakages of sensitive or confidential information are a significant concern [00:03:51].

### Safety and Trust
*   Using unreliable models or having an unsafe environment can lead to wrong results, especially if prompts are maliciously altered [00:04:00].

### Compliance and Governance
*   Many AI engineers are focused solely on getting agents to work, often overlooking crucial aspects like compliance and governance necessary for enterprise readiness [00:04:16].
*   Organizations, such as credit bureaus, treat AI agents similarly to human users [00:04:40]. This means agents must adhere to the same onboarding, training, and regulatory compliance processes as human employees [00:04:45]. This includes regulations around data access for specific regions (e.g., California resident data, Europe data) [00:04:52]. Without meeting these regulatory requirements, agents cannot be moved into production [00:05:23].

## Addressing the [[challenges_in_developing_ai_agents | Challenges]]: A Multi-Layered Approach

There is no "silver bullet" for security and compliance [00:05:38]. A layered approach involving evaluation, enforcement, and observability is recommended [00:05:43].

### 1. Evaluations (Evals)
Evals determine the criteria for deploying an agent to production and aim to generate a risk score [00:05:53]. This risk score helps decide if an agent, even a third-party one, is safe enough to be promoted [00:06:16].

Similar to traditional software development (e.g., test coverage, vulnerability scanning for Docker containers, CVE scanning for third-party software, pen testing for cross-site scripting) [00:07:22]:
*   **Baseline Testing**: Establish a baseline using appropriate use cases and ground truth to ensure that changes (e.g., prompt changes, new libraries, frameworks, or LLMs) do not alter the expected behavior [00:08:11].
*   **LLM and Library Vulnerability Scanning**: Ensure third-party LLMs are not poisoned and have been scanned for vulnerabilities [00:08:31]. Similarly, third-party libraries must meet minimum vulnerability criteria [00:08:38].
*   **Prompt Injection Testing**: Test for prompt injection attacks and ensure the application has controls to block them [00:08:48].
*   **Data Leakage Evaluation**: Verify that agents do not leak sensitive data [00:09:04]. For example, an HR agent should not allow an employee to access another's salary benefits, or prevent malicious users from exploiting loopholes [00:09:39].
*   **Unauthorized Actions**: For agents that perform actions or change things, ensure these actions are performed by authorized personnel [00:09:55].
*   **Runaway Agents**: Test for scenarios where agents can enter a tight loop due to bad prompts or task/agent design issues, preventing them from going into production [00:10:14].

### 2. Enforcement
Enforcement ensures the proper implementation of security controls, particularly in a zero-trust environment where libraries can access various resources [00:10:39].
*   **Authentication and Authorization**: These are crucial for enterprise-level security [00:11:18].
    *   **Authentication**: Prevents impersonation and theft of confidential information by ensuring proper user identification throughout the agent's interaction flow (user request to agent, task, tools, and API/database calls) [00:11:25]. The user's identity must be propagated to the final data access point [00:13:30].
    *   **Authorization**: Ensures that access control policies are properly applied [00:11:46]. Agents have their own roles and should not exceed their defined scope [00:11:54]. If an agent acts on behalf of a user, the user's specific role and permissions must be enforced, preventing access to data or APIs beyond their authorized scope [00:12:06].
*   **Approvals**: Integrate workflows where agents can automatically approve certain actions based on defined thresholds and guard rails [00:12:30]. For actions exceeding a certain limit, a human can be brought into the loop for approval [00:13:06].

### 3. Observability
Observability is critical in the agent world due to its dynamic nature, unlike traditional software which is more static [00:13:56].
*   **Continuous Monitoring**:
    *   **Model Changes**: Models evolve rapidly [00:14:18].
    *   **Framework and Library Evolution**: Agent frameworks and third-party libraries constantly change their behavior [00:14:23].
    *   **User Input Variability**: Agent behavior is highly subjective to user input [00:14:32]. Agents must be monitored to see how they behave with diverse user queries beyond initial testing [00:14:51].
    *   **Data Leakage**: Monitor for anomalies in the amount of PII or confidential data being sent out, allowing for quick action if detected [00:15:03].
*   **Metrics and Thresholds**: It's impractical to monitor every request [00:15:15]. Instead, define thresholds and metrics such as failure rates [00:15:21]. Alerts can be triggered when failure rates exceed tolerance levels, indicating potential misbehaving agents or malicious users [00:15:37].
*   **Anomaly Detection**: Similar to User Behavior Analytics in traditional security, anomaly detection for agents involves monitoring whether an agent behaves within accepted boundaries [00:15:53]. This will contribute to a security posture report, providing near real-time confidence in how an agent is performing in a live environment [00:16:27].

## Recap
To ensure safe and reliable AI agents:
*   **Preemptive Vulnerability Evaluation**: Conduct comprehensive evals to get a risk score, providing confidence to promote agents (or use third-party agents) to production [00:16:44].
*   **Proactive Enforcement**: Implement robust guard rails, enforcement mechanisms, and sandboxing to run agents securely [00:16:59].
*   **Real-time Observability**: Maintain strong observability to know how agents are performing in real-time and quickly fine-tune them if anomalies are detected [00:17:12].

The speaker mentions that Private AI has open-sourced their Safety and Security Solutions called "page.ai" and is looking for design partners and contributors [00:17:28].