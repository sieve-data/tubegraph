---
title: Evaluation techniques for multimodal and voice AI agents
videoId: OC04sP_QgTI
---

From: [[aidotengineer]] <br/> 

[[evaluating_ai_agents_and_assistance | Evaluating AI agents and assistance]] is crucial to ensure they function correctly in the real world once deployed into production <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. While many discussions focus on building agents and the tools available, understanding how to [[evaluating_ai_agents_methods_and_metrics | evaluate]] their performance is equally vital for all stakeholders, including leadership <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Evolution of AI Agents

Initially, many AI discussions centered on text-based agents like chatbots <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. However, the "next frontier" is [[ambient_agents_and_voice_technology | voice AI]], which is already revolutionizing call centers globally, handling over 1 billion calls with voice APIs <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. A real-world example is Price Line Pennybot, a voice-activated travel agent that allows users to book entire vacations hands-free <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

This shift means conversations are no longer just about text-based agents but also [[multimodal_ai_systems | multimodal agents]] <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. [[evaluation_of_voice_applications_including_audio_and_text | Evaluating these types of agents]] requires specific considerations beyond standard agent [[evaluation metrics for AI conversational systems | evaluation]], especially for voice and [[multimodal_ai_systems | multimodal]] interactions <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

## Components of an AI Agent

Regardless of the framework (e.g., LangGraph, CrewAI, LlamaIndex), AI agents typically consist of common patterns <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>:

*   **Router:** This component acts as the "boss" <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>, deciding the agent's next step <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. For an e-commerce agent, it funnels a user query (e.g., "I want to make a return") to the appropriate skill <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Skills:** These are the logical chains that perform the actual work <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. A skill flow might involve a series of LLM calls or API calls to execute a user's request <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   **Memory:** This component stores the context of multi-turn conversations, ensuring the agent remembers previous interactions and maintains state <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### Example of Agent Workflow

An example of an agent's inner workings, often visualized as "traces," shows how these components interact <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. If a user asks, "What trends do you see in my Trace latency?", the router first makes a tool call to run a SQL query to collect application traces <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. It then goes back to the router, which calls a second skill—a data analyzer—to process this data <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. All these steps are stored in memory <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

## Evaluation Points within the Agent Workflow

Every step of an agent's workflow is a potential point of failure and thus requires [[evaluating_ai_agents_methods_and_metrics | evaluation]] <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

### 1. Router Evaluation

For routers, the primary concern is whether it called the **right skill** and passed the **correct parameters** <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. For instance, if a user asks for leggings but is routed to customer service or discount information, the router failed <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. Teams must [[evaluating_ai_agents_methods_and_metrics | evaluate]] the router's control flow to ensure it correctly directs queries to the intended skills with appropriate arguments <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

### 2. Skill Evaluation

[[evaluation metrics for AI conversational systems | Evaluating a skill]] can be complex due to its many internal components <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. Key metrics include:

*   **Relevance:** For Retrieval Augmented Generation (RAG) type skills, [[evaluating_ai_agents_methods_and_metrics | evaluating]] the relevance of retrieved information chunks <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   **Correctness:** Assessing the accuracy of the generated answer <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   **Methodology:** Skills can be [[evaluating_ai_agents_methods and metrics | evaluated]] using LLM-as-a-judge evaluations or code-based evaluations <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

### 3. Path / Convergence Evaluation

One of the most challenging aspects to [[evaluating_ai_agents_methods_and_metrics | evaluate]] is the agent's path or "convergence" <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. This involves ensuring:

*   **Consistency:** The agent ideally takes a consistent and succinct number of steps to complete a task, even if the same skill is called hundreds of times <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   **Reliability:** Different LLM providers (e.g., OpenAI vs. Anthropic) might result in wildly different numbers of steps for the same skill, highlighting the importance of [[evaluation metrics for AI conversational systems | evaluating]] path reliability <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Efficiency:** The goal is to ensure the agent is succinct and reliably completes tasks <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

## Specifics for Voice and Multimodal Applications

[[challenges_in_building_ai_voice_agents | Voice applications]] are among the most complex applications ever built <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. [[evaluation of voice applications including audio and text | Evaluating voice agents]] requires additional considerations beyond just text:

*   **Audio and Text Evaluation:** It's not just the generated transcript that needs [[evaluation of voice applications including audio and text | evaluation]]; the audio chunk itself must also be assessed <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
*   **Post-Audio Processing:** Transcripts are often generated after the audio chunk is processed, adding another dimension to [[evaluation metrics for AI conversational systems | evaluation]] <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
*   **Voice-Specific Metrics:** Key metrics for voice include:
    *   User sentiment <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>
    *   Speech-to-text transcription accuracy <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>
    *   Tone consistency throughout the conversation <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>
    *   Intent and speech quality <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>

## Comprehensive Agent Evaluation

The goal of [[best_practices_for_building_ai_agents | building AI agents]] is to incorporate [[evaluation metrics for AI conversational systems | evaluations]] throughout the entire application's trace <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. This allows for pinpoint debugging, determining if an issue occurred at the router level, skill level, or elsewhere in the flow <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>. For example, in a co-pilot, evaluations can be run at the overall response level, the router selection, the argument passing to the router, and the correct task completion within the skill execution <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.