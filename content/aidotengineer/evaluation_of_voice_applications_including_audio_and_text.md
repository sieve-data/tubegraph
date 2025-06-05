---
title: Evaluation of voice applications including audio and text
videoId: OC04sP_QgTI
---

From: [[aidotengineer]] <br/> 

Evaluating AI agents and assistants is crucial for ensuring they function correctly in the real world once deployed into production <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a> <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. While many discussions focus on building agents and the tools available, understanding their performance post-production is equally important <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a> <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## The Rise of Voice and Multimodal Agents

Historically, discussions often centered on text-based agents like chatbots <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a> <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. However, the next frontier is [[voice_ai_and_its_applications_in_enhancing_customer_experience | voice AI]], which is already revolutionizing call centers, handling over a billion calls worldwide with voice APIs <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a> <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

Modern applications are moving beyond just text to [[voice_and_text_integration_in_apps | multimodal agents]], which combine different input and output modalities <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a> <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. An example is the Price Line Pennybot, a real production application where users can book an entire vacation hands-free without text <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a> <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. Evaluating these [[evaluation_techniques_for_multimodal_and_voice_ai_agents | multimodal and voice AI agents]] requires specific approaches beyond traditional agent evaluation <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a> <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

## Core Components of an AI Agent

Regardless of the framework (e.g., LangGraph, CrewAI, LlamaIndex Workflow), AI agents typically consist of common components:

*   **Router**: Acts as the "boss," deciding the agent's next step <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a> <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. For instance, in an e-commerce agent, it directs a user query (like "I want to make a return" or "Are there any discounts?") to the appropriate skill <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a> <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Skills**: These are the actual logical chains that perform the work, often involving LLM calls or API calls <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a> <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   **Memory**: Stores the context of multi-turn conversations, preventing the agent from forgetting previous interactions <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a> <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

These components can be observed through "traces," which show the inner workings and execution flow of an agent, useful for engineers in troubleshooting <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a> <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

## [[steps_to_create_effective_evaluations_for_ai_applications | Evaluating AI Agent Components]]

Every step within an agent's operation is a potential point of failure, necessitating thorough evaluation <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

### Router Evaluation
For routers, the primary concern is whether it called the *right skill* with the *right parameters* <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a> <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. If a user asks for leggings but is routed to customer service or discounts, the router has failed <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a> <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. Teams should evaluate the router's control flow and ensure it correctly passes arguments like material type or cost range <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a> <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

### Skill Evaluation
Evaluating skills is more complex due to multiple internal components <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a> <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. Key [[evaluation_metrics_for_ai_conversational_systems | metrics]] include:
*   **Relevance**: Especially for RAG (Retrieval Augmented Generation) type skills, evaluating the relevance of the pulled information chunks <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a> <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Correctness**: The accuracy of the generated answer <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a> <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   **LLM as a judge evals** or **code-based evals** can be used to assess skill performance <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a> <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   **Convergence**: Evaluating the agent's path consistency and the number of steps it takes to complete a task <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a> <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. The goal is succinctness and reliability in the number of steps, as different LLMs (e.g., OpenAI vs. Anthropic) can lead to vastly different path lengths for the same skill <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a> <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

## Specifics of Voice Application Evaluation

[[ambient_agents_and_voice_technology | Voice applications]] are among the most complex applications to deploy, requiring additional evaluation considerations <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a> <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. Beyond evaluating the text or transcript, the audio chunk itself needs evaluation <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.

Key aspects for [[voicefirst_ai_overlays | voice-first AI]] evaluation include:
*   **User Sentiment**: Assessing the user's emotional state <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   **[[speech_recognition_technology_and_applications | Speech-to-text]] Transcription Accuracy**: Verifying the correctness of the generated transcript from audio <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a> <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.
*   **Tone Consistency**: Ensuring a consistent tone throughout the conversation <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
*   **Intent and Speech Quality**: Defining and evaluating these metrics specifically for audio <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a> <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

The challenge arises because the generated transcript often appears *after* the audio chunk is sent, adding a new dimension to evaluation <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a> <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

## Multi-Layered Evaluation in Practice

Effective evaluation involves setting up metrics throughout the entire application flow, not just at a single layer <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a> <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. This allows for precise debugging if an issue arises, pinpointing whether it occurred at the router level, skill level, or elsewhere in the flow <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a> <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.

For example, a co-pilot feature might be evaluated at multiple points during a user's interaction:
*   An overall evaluation to check if the generated response to a search query was correct <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.
*   Evaluation to confirm the correct router was selected and the right arguments were passed to it <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
*   Finally, an evaluation to ensure the task or skill was completed correctly during its execution <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.