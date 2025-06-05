---
title: Singleturn and multiturn semantics in agent evaluation
videoId: y2Drx0SDZLo
---

From: [[aidotengineer]] <br/> 

[[evaluating_ai_agent_performance_and_reliability | Agent evaluation]] is considered both an art and a science, and is crucial for ensuring that AI agents perform as expected, especially when deployed in production <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. The evaluation process can be broadly divided into [[semantic_and_behavioral_evaluation_of_agents | semantic and behavioral components]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Semantic Evaluation Defined
The semantic part of agent evaluation focuses on how an agent's internal representations of reality accurately relate to external reality <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Truthfulness in these representations is achieved by grounding them in data <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

Semantic evaluation is further categorized into single-turn (or single-step) and multi-turn aspects <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

## Single-Turn Semantic Quality
Single-turn semantic quality involves assessing individual responses or outputs from the agent. This includes:
*   **Universal Virtues** <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>: These are general qualities, often non-agenic, but essential for a complete evaluation <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Examples include:
    *   **Coherence and Consistency**: Is the agent's reply consistent? <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a> <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>
    *   **Safety**: Is the content safe? <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>
    *   **Alignment**: Does the agent's output align with the values of stakeholders and adhere to organizational policies? <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>
*   **Retrieval-Augmented Generation (RAG) and Attention Management**: This requires specific evaluators to measure aspects such as:
    *   Whether the retrieved context was correct <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
    *   Whether all relevant information was comprehensively recalled <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
    *   **Faithfulness**: How well the answers relate to external reality, which is distinct from answer/question relevance or general factfulness <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a> <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. RAG evaluations involve examining relationships between different parts of the RAG pipeline <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

## Multi-Turn Semantic Quality
Multi-turn semantic quality extends evaluation to sequences of interactions and the agent's reasoning processes:
*   **Chat Conversation Histories**: Assessing how chat conversation histories develop <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>, including:
    *   Overall consistency and adherence <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
    *   Sticking to topics when necessary, or allowing topic changes if desired by the user <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **Reasoning Traces**: Evaluating the agent's internal reasoning processes, such as the Chain of Thought <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. This provides a way to assess sequential or multi-turn activities performed by the agent in its reasoning and world representation before taking any actions <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

## Practical Considerations
Many of these semantic measurements are implemented using LLMs as judges <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. A common pitfall is focusing solely on optimizing the operative element flow (the agent itself), neglecting the cost, latency, and uncertainty of the judging LLM (the "chargement" flow) <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. It is crucial to adopt a "Double Tier" approach, optimizing both the operative LLM flow powering the agent and the chargement flow powering the evaluations <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a> <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. This complex situation is referred to as "Eval Ops," which is a specialized form of LLM Ops, requiring different thinking, software implementations, and resourcing <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a> <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.