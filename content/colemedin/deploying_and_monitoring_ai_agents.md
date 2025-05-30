---
title: Deploying and monitoring AI agents
videoId: k-Cj6H6Zwos
---

From: [[colemedin]] <br/> 

Successfully bringing AI agents into production and ensuring their continued reliability requires specific strategies for deployment, monitoring, and evaluation <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

## Deploying AI Agents

[[embedding_and_production_deployment_of_ai_agents | Productionizing AI agents]] is a crucial step <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

### Key Deployment Tool: Docker

The primary tool for [[configuring_ai_agents_for_cloud_deployment | deploying AI agents]] to production is **Docker** <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   Docker enables containerization of agents into an isolated environment <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
*   This isolated environment allows the agent to be deployed anywhere in the cloud <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.
*   Using Docker creates a standardized process for [[deploying_and_scaling_ai_agents_with_docker | deploying agents]] <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

### Cloud Platforms for Deployment

Various cloud platforms are available for [[deploying_ai_applications_to_the_cloud | deploying AI applications]] <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>:
*   **Easy-to-use options:** Digital Ocean, Hostinger <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
*   **Enterprise-level platforms:** Amazon Web Services (AWS), Google Cloud Platform (GCP) <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
*   **GPU instances (for larger local LLMs):** Vast AI, RunPod <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
*   The process of containerizing and [[deploying_ai_applications_to_the_cloud | deploying AI agents]] is similar across most cloud platforms due to Docker's standardization <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

## Monitoring AI Agents

Once an AI agent is running in a live environment, monitoring becomes essential <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

### Agent Observability

Monitoring is often referred to as "agent observability" <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>. It provides a way to "peer into" the AI agent to understand its operations <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.
*   **Key aspects to observe:**
    *   Requests received from users <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
    *   Decisions made by the agent, particularly around tool calling <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.
    *   The output provided to end-users <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.
*   **Purpose:**
    *   Detecting errors with the agents <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
    *   Identifying opportunities to improve the AI agent's performance <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.
*   Continuous improvement is crucial for agents <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

### Tools for Agent Observability

Several tools are available for agent observability <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>:
*   Langfuse <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>
*   Helicone <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>
*   Langsmith <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>
*   Logfire <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>
*   Impidantic AI <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>

Observability is considered **100% necessary** for agents in production <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

## Agent Evaluation

[[importance_of_monitoring_and_iterating_ai_agents | Agent evaluation]] is distinct from traditional code testing and focuses on behavior correctness <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.
*   Building AI agents is estimated to be only 25% coding or automating; the remaining 75% involves evaluating and making adjustments <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

### Evaluation vs. Testing

*   **Testing:** Focuses on general code correctness, ensuring the application doesn't crash or fail to produce any result <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Evaluation:** Focuses on *agent behavior correctness*. A negative result in evaluation doesn't mean a crash, but rather that the agent's output is not acceptable <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

### Methods of Evaluation

*   **LLM as a Judge:** Using another large language model to evaluate the output of the agent <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.
*   **Task Completion Testing:** Centered around tool calling, verifying if the agent invoked the necessary tools based on a request (e.g., updating a task in Asana, drafting an email) <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.
*   **Human Evaluation:** Involves people (e.g., end-users) trying out the agents, providing feedback via surveys, and determining if results are acceptable <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.

Evaluating agents is critical for ensuring they deliver the required results for the system being built <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>. This step ensures that the effort put into building a reliable and effective agent translates into desired outcomes <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.