---
title: Evaluation mechanisms for AI recommendations
videoId: 9mzfioh1Zag
---

From: [[aidotengineer]] <br/> 

Evaluating AI systems, particularly those that provide recommendations, presents unique challenges, especially within complex multi-agent architectures <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>. Determining the quality of a recommendation in a system with many interconnected engines and rounds of conversation requires robust mechanisms <a class="yt-timestamp" data-t="00:19:13">[00:19:13]</a>.

## Evaluation Challenges and Approaches

The primary challenge lies in understanding how to definitively assess if a recommendation is good <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>. To address this, a closed-loop system incorporating human scoring, structured feedback, and iterative revision cycles is crucial <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.

### Human Evaluation

At early stages of development, [[human_reviews_of_ai_outputs | human evaluation]] is considered the most effective method for assessing AI recommendations <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>, <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. While LLM-based evaluations are useful, they often do not provide the specific insights needed to drive necessary improvements <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>, <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>, <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

### Internal Evaluation Tool: Eagle Eye

An internal human evaluation tool, named "Eagle Eye," was developed to facilitate this process <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>, <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>. This tool allows for detailed inspection of specific cases within the AI system, including:
*   The architecture being evaluated <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.
*   Extracted requirements <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>.
*   Conversations between agents <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>.
*   The final generated recommendations <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>, <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>.

Through "Eagle Eye," evaluators can conduct studies on relevance, visibility, and clarity, assigning scores to inform decisions on areas needing improvement <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>, <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>, <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>, <a class="yt-timestamp" data-t="00:20:32">[00:20:32]</a>.

### Key Learnings on [[evaluating_ai_system_performance | AI Evaluation]]

*   **Confidence is Not Correctness:** An AI system's confidence level does not directly equate to the correctness of its output and cannot always be trusted <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>, <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>, <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.
*   **Early Human Feedback is Essential:** [[human_reviews_of_ai_outputs | Human feedback]] is critical early in the development of AI systems built from scratch <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>, <a class="yt-timestamp" data-t="00:20:52">[00:20:52]</a>, <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a>, <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.
*   **[[steps_to_create_effective_evaluations_for_ai_applications | Evaluation Must Be Integrated into Design]]:** [[evaluating_ai_agents_methods_and_metrics | Evaluation]] should be a foundational component of system design, not an afterthought <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>, <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>, <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>. When designing a new AI system, parallel consideration should be given to how it will be evaluated, whether through human review, monitoring dashboards, or LLM-based feedback loops <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>, <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>, <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>, <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>, <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>, <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>, <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>, <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>, <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.

### Identifying Issues: Hallucination Example

The [[evaluating_ai_agents_and_assistance | evaluation tool]] helps identify issues like hallucination. For instance, an early case involved a "staff architect network security" agent requesting a workshop schedule from a "requirements retriever" agent, providing specific dates, which was an instance of the agent hallucinating an action outside its defined capabilities <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>, <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>, <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>, <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>, <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>, <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>, <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>, <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>. Handling such cases is crucial for system improvement <a class="yt-timestamp" data-t="00:22:31">[00:22:31]</a>.

Effective [[strategies_for_ai_evaluation_and_troubleshooting | evaluation]] is an ongoing process of experimentation, learning which patterns work best with the available data, and refining agent interactions and autonomy <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>, <a class="yt-timestamp" data-t="00:24:18">[00:24:18]</a>, <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>, <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>, <a class="yt-timestamp" data-t="00:24:25">[00:24:25]</a>, <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>, <a class="yt-timestamp" data-t="00:24:39">[00:24:39]</a>, <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>, <a class="yt-timestamp" data-t="00:24:46">[00:24:46]</a>, <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>.