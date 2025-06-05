---
title: AI security and observability
videoId: z4zXicOAF28
---

From: [[aidotengineer]] <br/> 

The [[AI in enterprise and startups | AI]] field is undergoing a revolution, marked by real adoption and impressive scale <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. As [[AI implementation and best practices | AI applications]] move from demos to production, crucial aspects like security and observability come to the forefront <a class="yt-timestamp" data-t="03:00:10">[03:00:10]</a>. These are not merely optional features, but fundamental requirements for building trustworthy and reliable [[ai_application_frameworks_and_architecture | AI systems]] <a class="yt-timestamp" data-t="00:48:20">[00:48:20]</a>.

## The Need for Trust and Accountability
The rapid deployment of AI, particularly [[ai_agents_in_devops | AI agents]], necessitates building trust and ensuring accountability <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>. This means addressing concerns around lack of transparency, misaligned goals, erosion of human oversight, and the potential for deception <a class="yt-timestamp" data-t="01:45:47">[01:45:47]</a>. Human tolerance for errors, hallucinations, or lack of reliability in [[ai_agents_in_devops | AI agents]] dramatically decreases as latency increases <a class="yt-timestamp" data-t="01:19:21">[01:19:21]</a>. Therefore, making the "right thing to do the easiest thing to do" is key in designing secure and observable systems <a class="yt-timestamp" data-t="02:57:51">[02:57:51]</a>.

## Key Aspects of AI Security and Observability

### 1. Robust Evaluation and Testing
Developing and maintaining high-quality [[AI agents in DevOps | AI agents]] requires continuous evaluation <a class="yt-timestamp" data-t="00:48:16">[00:48:16]</a>.
*   **Evaluation SDKs:** Leading evaluation SDKs are crucial for measuring performance and ensuring agents deliver consistent, high-quality results <a class="yt-timestamp" data-t="00:48:16">[00:48:16]</a>.
*   **Red Teaming:** Employing red teaming techniques helps identify vulnerabilities and biases in [[AI agents in DevOps | AI agents]] <a class="yt-timestamp" data-t="00:48:18">[00:48:18]</a>.
*   **CI/CD Integration:** Integrating evaluations directly into the CI/CD pipeline ensures agents are consistently assessed every time updates are made <a class="yt-timestamp" data-t="00:56:35">[00:56:35]</a>.
*   **Designing Errors:** Error messages should be designed as effective context for both humans and [[AI agents in DevOps | AI agents]], enabling proper reasoning and debugging <a class="yt-timestamp" data-t="03:31:03">[03:31:03]</a>.

### 2. Comprehensive Observability
[[the_importance_of_observability_in_ai_systems | Observability]] is fundamental for understanding how [[AI systems]] operate and identifying issues.
*   **[[cloud_observability_with_open_telemetry | Telemetry]]**: [[cloud_observability_with_open_telemetry | Telemetry]] is non-optional and can be integrated using frameworks like [[cloud_observability_with_open_telemetry | Open Telemetry]] to provide continuous observability regardless of where an agent is built <a class="yt-timestamp" data-t="00:48:20">[00:48:20]</a>.
*   **Debugging and Logging:** Tools like the Inspector are vital for debugging and logging [[MCP | MCP]] servers, ensuring transparent operation <a class="yt-timestamp" data-t="02:42:14">[02:42:14]</a>.
*   **Centralized Context:** A central repository for all context that models request and receive allows for easier auditing and analysis <a class="yt-timestamp" data-t="03:02:31">[03:02:31]</a>. This is greatly aided by standardized message formats, such as those provided by [[MCP | Model Context Protocol (MCP)]] <a class="yt-timestamp" data-t="03:02:49">[03:02:49]</a>.

### 3. Secure [[enterprise_ai_deployment_within_security_boundaries | Enterprise AI Deployment]]
Security considerations are paramount when deploying [[AI in enterprise and startups | AI]] in enterprise environments.
*   **Authentication and Authorization:** Standardized authentication models, particularly using [[OAUTH | OAUTH 2.1]] with remote environments, are critical for managing access and ensuring secure interactions between agents and services <a class="yt-timestamp" data-t="02:56:07">[02:56:07]</a>. Centralizing credential management within a gateway can simplify deployment and enhance security <a class="yt-timestamp" data-t="02:58:34">[02:58:34]</a>.
*   **Data Residency and Compliance:** For sensitive domains like healthcare, models must operate locally to adhere to compliance and privacy regulations, even if the cloud can access the data <a class="yt-timestamp" data-t="00:57:39">[00:57:39]</a>. This requires platforms that seamlessly move models from cloud to edge <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>.
*   **Controlling Context:** As models integrate memory features, managing and controlling the context provided to them becomes increasingly important to prevent unintended behavior or data leakage <a class="yt-timestamp" data-t="01:34:50">[01:34:50]</a>.
*   **Prompt Engineering and Safety:** Tinkering with system prompts is risky <a class="yt-timestamp" data-t="01:40:16">[01:40:16]</a>. There is a need for robust prompt engineering that guides models towards desired behaviors and away from harmful ones <a class="yt-timestamp" data-t="01:40:01">[01:40:01]</a>.
*   **Mitigating Prompt Injection:** [[Prompt injection]] remains a significant concern, where malicious instructions can trick [[AI agents in DevOps | AI agents]] into unintended actions, especially if they have access to private data and mechanisms for exfiltration <a class="yt-timestamp" data-t="01:42:32">[01:42:32]</a>. Organizations must be cautious about allowing random [[MCP | MCP]] tools and should only trust those that have earned it <a class="yt-timestamp" data-t="02:57:18">[02:57:18]</a>.
*   **API Design:** When building [[MCP | MCP]] servers, it's critical not to simply expose raw APIs. Instead, the design should prioritize how the AI model will reason about the context and respond effectively <a class="yt-timestamp" data-t="02:55:51">[02:55:51]</a>. Simplified outputs like Markdown are often more effective for model understanding than complex JSON <a class="yt-timestamp" data-t="03:29:44">[03:29:44]</a>. This also helps in managing token costs <a class="yt-timestamp" data-t="03:31:52">[03:31:52]</a>.
*   **Centralized Auditing:** Centralizing [[Enterprise AI deployment within security boundaries | AI security]] and auditing functions is essential for visibility and control over internal [[AI agent in DevOps | agent]] proliferation <a class="yt-timestamp" data-t="02:57:34">[02:57:34]</a>.

### 4. [[Confidential AI and its impact | Confidential AI]]
The concept of [[Confidential AI and its impact | confidential AI]] extends security to processing data securely at the edge, particularly for sensitive information that cannot be stored in the cloud due to compliance reasons <a class="yt-timestamp" data-t="00:57:39">[00:57:39]</a>.

## Evolution of AI Engineering
The discussion around AI security and observability reflects the broader evolution of [[AI implementation and best practices | AI engineering]]. The field is moving from simple GPT wrappers to more complex, multi-disciplinary systems <a class="yt-timestamp" data-t="02:52:01">[02:52:01]</a>. This involves a shift from shipping binaries to shipping [[AI agents in DevOps | agents]] that can retrain, redeploy, and change post-deployment <a class="yt-timestamp" data-t="00:46:42">[00:46:42]</a>. This continuous loop, known as the "signals loop," where models are fine-tuned to specific outcomes, highlights the importance of robust infrastructure and continuous monitoring <a class="yt-timestamp" data-t="00:45:52">[00:45:52]</a>.

Ultimately, while the underlying model capabilities are becoming commoditized, the value lies in building "thick" [[AI application frameworks and architecture | applications]] and [[AI agents in DevOps | agents]] that provide valuable user experiences, ensure security, and address real-world problems <a class="yt-timestamp" data-t="01:15:10">[01:15:10]</a>.