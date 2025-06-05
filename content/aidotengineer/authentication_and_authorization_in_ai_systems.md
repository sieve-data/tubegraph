---
title: Authentication and authorization in AI systems
videoId: G7aSH6N7qY4
---

From: [[aidotengineer]] <br/> 

In the realm of AI agents, particularly within [[enterprise_ai_within_security_boundaries | enterprise AI]], establishing robust authentication and authorization mechanisms is crucial for ensuring safety and reliability <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. These security controls are vital to prevent unauthorized access, data leakages, and to maintain trust and compliance <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

## Importance in AI Agent Environments

AI agents operate in what can be considered a "zero-trust environment" <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a> <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. This is due to several factors:
*   **Shared Processes:** Current [[agent_frameworks_and_orchestration_layers_in_ai_engineering | agent frameworks]] often run the [[components_of_ai_agents | agent]], tasks, and tools within a single process <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This means if a tool requires database access or API calls, credentials or share tokens are present within that same process <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   **Super Admin Privileges:** These credentials often belong to a service user with super admin privileges, making the entire environment vulnerable if one component is compromised <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   **Unauthorized Access:** Without proper authentication, an attacker could impersonate a legitimate user, leading to the theft of confidential or sensitive information <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.
*   **Data Leakage:** Incorrectly designed or implemented agents can result in unauthorized access and data leakage of sensitive or confidential information <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a> <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Implementation of Authentication and Authorization

Implementing strong authentication and authorization in AI systems is a critical enforcement layer <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **Authentication:** This ensures the user making a request to an agent is who they claim to be <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
*   **Authorization:** This dictates what an authenticated user (or agent acting on their behalf) is permitted to do <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. It ensures that [[components_of_ai_agents | agents]] do not exceed their defined roles and that user permissions are enforced when an agent acts on behalf of a user <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. For example, an HR agent might access salary benefits for an employee, but an employee user should not access another's salary data <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

A key aspect of this implementation is the **propagation of user identity** <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. When a user request is made to an agent, which then calls a task, and that task calls a tool that makes an API call or accesses a database, the original user's identity must be passed along every step <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. This allows for the enforcement of the correct policies and access controls at the very last point of data access or API interaction <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.

## Approvals and Workflows

In traditional systems, workflows for approvals (e.g., leave requests) often involve human managers <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>. With AI agents, this can be automated:
*   **Automated Approvals:** An agent can be designed to handle most approvals automatically <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Thresholds and Guardrails:** Thresholds can be set for how much an agent can automatically approve <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. If an action or request exceeds a certain limit, proper guardrails can automatically bring a human into the loop for review <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

For organizations like credit bureaus, AI agents are treated similarly to human users, requiring adherence to strict regulations, onboarding processes, and training to ensure compliance with data privacy laws (e.g., California resident data, GDPR) <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. This underscores the need for robust authentication and authorization to integrate AI agents securely into existing compliance frameworks.