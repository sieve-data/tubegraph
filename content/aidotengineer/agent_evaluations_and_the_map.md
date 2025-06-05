---
title: Agent evaluations and the map
videoId: y2Drx0SDZLo
---

From: [[aidotengineer]] <br/> 

[[evaluating_ai_agents_and_assistants | Agent evaluation]] is a combination of art and science, essential to ensure that AI agents perform as expected, especially when deployed in production environments <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## The Agent Evaluation Map

The [[evaluating_ai_agents_and_assistants | agent evaluation]] process can be divided neatly into two main categories: [[semantic_and_behavioral_evaluation_of_agents | semantic and behavioral parts]] <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

### Semantic Evaluation

[[semantic_and_behavioral_evaluation_of_agents | Semantic evaluation]] focuses on how an agent's representations of reality relate to actual reality <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Truthfulness in semantic evaluation is ultimately achieved by grounding representations in data, often with Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

It is further divided into:

*   **Single-Turn Items**: These involve universal virtues, which are non-agenic but covered for completeness to understand agent-specific parts through contrast <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. Examples include:
    *   **Coherence & Consistency**: Whether the agent's reply is consistent <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
    *   **Safety**: If the content provided is safe <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
    *   **Alignment & Policies**: Whether the agent's statements align with organizational values or stakeholder policies <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
    *   **RAG/Attention Management**: This requires specific evaluators to measure aspects like:
        *   Correctness of the retrieved context <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
        *   Comprehensive recall of the context <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
        *   **Faithfulness**: Relating answers to external reality, which is distinct from answer-question relevance and general factfulness <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. RAG evaluations can take many forms and exhibit symmetries, essentially looking at relationships between parts of the RAG pipeline <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Multi-Turn Aspects**: These relate to conversational histories and reasoning <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
    *   **Chat Conversation Histories**: Looking for consistency and adherence to topics (or allowing changes when appropriate) <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
    *   **Reasoning**: Evaluating reasoning traces, such as "Chain of Thought," which represents sequential activities and world representations before any actions are taken <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

### Behavioral Evaluation

The [[semantic_and_behavioral_evaluation_of_agents | behavioral part]] focuses on how an agent's actions and tool usage contribute to achieving its goals within its environment, and the effects it has on that environment <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Goal achievement is realized by grounding the agent's activities in the tools it has available <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

This is also distinguished by:

*   **Individual Tool Selection & Usage**: Evaluating aspects even before a chain of behaviors <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>:
    *   Following instructions <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
    *   Correctly extracting tool characteristics <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
    *   Selecting the right tool <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
    *   Tool output quality <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
    *   Correct handling of error situations <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
    *   Adherence to structured tool formats <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
*   **Task Progression & Planning (Multi-Step)**: Evaluating the overall sequence of actions <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>:
    *   Whether actions converge towards achieving the agent's goal <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
    *   Consistency and quality of the agent's plan <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Symmetry in Evaluation

There is an intentional symmetry between semantic and behavioral evaluations, stemming from the analogy between representations and behaviors <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Representing the world is considered a type of activity, meaning representations can be seen as a special case of behaviors or tools <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. Both semantic (truthfulness) and behavioral (goal achievement/utility) aspects are grounded in external reality, with goal achievement being the ultimate metric <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. Other metrics are often considered proxies <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

## Other Practical Considerations

Beyond the main evaluation map, several practical aspects are crucial for [[challenges_with_agent_evaluations_and_behavior_analysis | agent evaluations]] <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>:

*   **Cost and Latency Optimization**: Agents should progress towards their goals as quickly and cheaply as possible, including optimizing the number of steps <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **Tracing and Debugging**: The ability to identify where an agent went wrong <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Error Management**: Specifically dealing with errors in tool usage, distinct from semantic errors during inference <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   **Offline vs. Online Testing**: A critical distinction between evaluations during development and those performed during live agent activity <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. These are distinct dimensions that could further complicate the evaluation map <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   **Special Cases & Tool-Specific Metrics**: More refined and advanced evaluation methods, potentially research-oriented <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. Tool-specific metrics, often simple to implement for API calls, can be added <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

## EvalOps: Optimizing the Evaluator LLM

Many measurements in [[ai_evaluation_and_risk_scoring | AI evaluation]] are implemented using "LLM as a judge" techniques <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. A common pitfall is the "single-tier" approach, where optimization focuses only on the agent's operational flow, overlooking the cost, latency, and uncertainty of the "judge" LLM itself <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

A "double-tier" optimization is necessary, optimizing both the operative LLM flow powering the agent and the "chargement" flow powering the evaluations <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. This complex situation is termed **EvalOps** <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. EvalOps represents a distinct category of activity because evaluations can be so complicated, expensive, and slow <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. It is a special case of LLM Ops, operating on different entities, requiring different thinking, software implementations, and resourcing <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.

The goal of these evaluations is to make agents measurable and controllable, ensuring they adhere to their intended purposes <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.