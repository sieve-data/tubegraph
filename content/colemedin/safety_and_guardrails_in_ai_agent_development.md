---
title: Safety and guardrails in AI agent development
videoId: TlbcAphLGSc
---

From: [[colemedin]] <br/> 

The internet offers vast amounts of information on [[understanding_ai_agents | what AI agents are]] and [[building_ai_agents | how to build them effectively]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Three key resources for understanding agents are Google's agent white paper, Anthropic's "Building Effective Agents" article, and OpenAI's "Agent Guide" <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. These documents, totaling over 14,000 words, provide comprehensive insights synthesized into a concise presentation <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## The Need for Guardrails
While [[building_ai_agents | AI agents]] are powerful due to their enhanced reasoning capabilities, they also introduce challenges. Giving agents significant responsibility makes systems more unpredictable and potentially dangerous <a class="yt-timestamp" data-t="02:59:01">[02:59:01]</a>. For example, an agent might decide to look at a file when it shouldn't, or skip analyzing a file when it should <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>. These types of mistakes are less likely in traditional, linear workflows where processes are hardwired <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>.

A crucial point is that even the most powerful Large Language Models (LLMs) are prone to hallucinating <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>. Therefore, [[ensuring_reliability_in_ai_agents_with_guardrails_and_fallback_nodes | ensuring reliability in AI agents with guardrails and fallback nodes]] is paramount to prevent these hallucinations from negatively impacting the entire AI system <a class="yt-timestamp" data-t="11:42:00">[11:42:00]</a>.

## Types of Guardrails
Guardrails are essential for mitigating the risks associated with AI agent unpredictability and hallucinations. The OpenAI guide is particularly strong in its coverage of guardrails <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a>.

Key types of guardrails include:
*   **Limiting Actions**: Restricting the actions an agent can take. For instance, an agent interacting with a database might only be permitted to use read-only tools <a class="yt-timestamp" data-t="11:50:00">[11:50:00]</a>.
*   **Human Review (Human-in-the-Loop)**: Integrating human oversight into the agent's workflow. This involves adding humans to approve actions or provide feedback to guide the agent <a class="yt-timestamp" data-t="11:56:00">[11:56:00]</a>.
*   **Filtering Outputs**: Implementing mechanisms to filter out undesirable outputs, such as Personally Identifiable Information (PII), or ensuring relevance classifiers for Retrieval Augmented Generation (RAG) applications <a class="yt-timestamp" data-t="12:04:00">[12:04:00]</a>.
*   **Evaluator Loops**: Using a separate LLM to evaluate the output of an agent and, if necessary, initiate a self-correction loop until the output meets expectations <a class="yt-timestamp" data-t="12:27:00">[12:27:00]</a>. This is similar to the "evaluator and optimizer" pattern discussed by Anthropic <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>.

> [!INFO] Example of an Evaluator Loop
> An AI agent produces an output, which then passes through a "critic node" (a guardrail). This node evaluates if the output meets the process expectations. If not, the agent retries, creating a loop until an accepted output is achieved <a class="yt-timestamp" data-t="12:54:00">[12:54:00]</a>.

## Best Practices for [[secure_deployment_of_ai_agents | Secure Deployment of AI Agents]]
When [[building_productiongrade_ai_agents | building production-grade AI agents]], several practices ensure safety and reliability:

*   **Test in a Safe Environment**: Always test agents thoroughly in a controlled environment before deploying them to production <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>. This helps identify situations where the agent might fail or where guardrails prove insufficient <a class="yt-timestamp" data-t="12:13:00">[12:13:00]</a>.
*   **Start Simple**: Begin with simple implementations and gradually add complexity <a class="yt-timestamp" data-t="13:35:00">[13:35:00]</a>.
*   **Visibility into Reasoning**: Ensure you have visibility into the agent's decision-making process, allowing you to observe how it uses tools and arrives at conclusions <a class="yt-timestamp" data-t="13:39:00">[13:39:00]</a>.
*   **Clear Instructions**: Provide clear instructions through the system prompt and precise descriptions for the tools given to the agent. This ensures the agent knows how and when to use its tools effectively <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>.
*   **Constant Evaluation**: Evaluation is a critical component of [[creating_a_robust_ai_agent_development_environment | creating a robust AI agent development environment]]. It's suggested that [[building_ai_agents | building AI agents]] is 25% coding and 75% evaluating <a class="yt-timestamp" data-t="14:07:00">[14:07:00]</a>. Continuous evaluation and tweaking of tools, fine-tuning, system prompts, and knowledge bases are essential for achieving high performance <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>.
*   **Maintain Human Oversight**: Implement human-in-the-loop mechanisms for crucial decisions, as it's not advisable to trust agents 100% in many use cases <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>.

> [!CAUTION] Focus on Outcomes, Not Complexity
> When [[building_ai_agents | building AI agents]], especially those with [[advanced_architecture_for_agents | advanced architecture for AI agents]] or multi-agent systems, it can be tempting to focus on complexity <a class="yt-timestamp" data-t="16:37:00">[16:37:00]</a>. However, the most important aspect is the **outcomes** and **results** the agent delivers <a class="yt-timestamp" data-t="16:59:00">[16:59:00]</a>. Prioritize the return on investment over intricate designs <a class="yt-timestamp" data-t="17:16:00">[17:16:00]</a>.