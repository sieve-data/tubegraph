---
title: Goal achievement and grounding in reality
videoId: y2Drx0SDZLo
---

From: [[aidotengineer]] <br/> 

Evaluating AI agents is both an art and a science, yet it is essential to ensure agents perform as expected, especially when deployed in production environments <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. Agent evaluation can be broadly categorized into semantic and behavioral aspects <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Core Evaluation Principles

The core of effective agent evaluation lies in two fundamental grounding principles:
*   **Truthfulness and Grounding Representations**: This relates to the semantic part of the agent, focusing on how well the agent's internal representations of reality align with external reality <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Truthfulness is achieved by grounding these representations in external data <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **Goal Achievement and Grounding Behaviors**: This concerns the behavioral part, assessing how the agent's actions and tool usage contribute to achieving its goals in its environment and the effects these actions have <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Goal achievement is attained by grounding the agent's actions in the tools it has available <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

There is a symmetry between representations and behaviors, as representing the world is itself a form of activity, making representations a special case of behaviors or tools <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

## Semantic Quality and Grounding

The semantic part of evaluation involves assessing the agent's understanding and representation of information.

### Single-Turn Semantic Quality
This covers "non-agenic" virtues, focusing on the quality of individual responses or turns <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   **Virtues**: Includes checking if the agent's reply is consistent, safe, and aligns with the values and policies of stakeholders <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Retrieval Augmented Generation (RAG) / Attention Management**: Evaluated by checking if the retrieved context was correct, comprehensively recalled, and whether answers relate to external reality <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
    *   **Faithfulness**: Refers to the adherence of the answer to the specific reference data used by the RAG system <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
    *   **Factfulness**: A broader concept that relates to reality beyond just the reference data <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

### Multi-Turn Semantic Quality
This involves evaluating interactions over time, such as chat conversation histories <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Consistency and Adherence**: Checking consistency over turns and whether the agent sticks to or appropriately changes topics <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   **Reasoning Traces**: Evaluating the agent's reasoning processes, like a "Chain of Thought," before any actions are taken <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This represents the sequential or multi-turn activities related to the agent's representations of the world <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. [[selfimprovement_and_reasoning_in_ai_agents | Progress in reasoning]] has been significant <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

## Behavioral Quality and Goal Achievement

The behavioral aspect of evaluation assesses the agent's actions and tool use in pursuing its goals.

### Single-Step Behavioral Quality
This focuses on individual actions and tool usage <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Instruction Following**: Whether the agent follows instructions <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Tool Characteristics**: Correctly extracting tool characteristics <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
*   **Tool Selection and Usage**: Selecting the right tool and ensuring the output quality is correct <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Error Handling**: Correctly managing error situations related to tool usage <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   **Structural Adherence**: Ensuring tool interaction formats and structures are correct <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

### Multi-Step Behavioral Quality
This looks at sequences of behaviors and their progression towards a goal <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
*   **Goal Convergence**: Assessing if the actions taken by the agent are converging towards achieving its goal <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   **Plan Quality**: Evaluating the consistency and overall quality of the agent's plan <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

## Ultimate Metrics and Grounding

Ultimately, both representations and activities are grounded in external reality <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. Representations are grounded on truthfulness <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>, while activities and behaviors are grounded by [[realworld_implications_and_expectations_of_ai_agents | goal achievement]] and utility <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. These serve as the ultimate metrics for what an agent is trying to do, with other metrics along the way often being proxy metrics <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

## Practical Considerations for Agent Evaluation

While not fitting neatly into the semantic/behavioral map, several practical aspects are crucial for agent evaluation:
*   **Cost and Latency Optimization**: Agents should progress toward their goals as quickly and cheaply as possible <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. This includes optimizing the number of steps an agent takes <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Tracing and Debugging**: The ability to identify where an agent goes wrong is vital <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Error Management**: Specifically, dealing with errors in tool usage, distinct from semantic errors during inference <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Offline vs. Online Testing**: A critical distinction between evaluations during development and those performed during the agent's actual online activities <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Tool-Specific Metrics**: Simple metrics for API calls and other tools can be useful and often implemented using traditional software testing methodologies <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

### LLM as a Judge and EvalOps
Many measurements in agent evaluation are implemented using Large Language Models (LLMs) as judges <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
*   **Single-Tier vs. Double-Tier Optimization**: A common pitfall is focusing solely on optimizing the operative element flow (the agent itself), a "single-tier" approach <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. A "double-tier" approach is necessary, optimizing both the operative LLM flow (for the agent) and the "chargement" flow (the LLM used for evaluations) due to the costs, latencies, and uncertainties associated with the latter <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
*   **EvalOps**: This complex situation, where evaluations themselves are complicated, expensive, and slow, warrants its own category of activities known as EvalOps <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. EvalOps is a special case of LLM Ops, operating on different entities and requiring different ways of thinking, software implementations, and resourcing <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. [[importance_of_evaluation_metrics_in_ai_systems | Evaluation frameworks]] are complex and continually evolving.

The goal is to make agents measurable, controllable, and ensure they adhere to their intended purposes <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.