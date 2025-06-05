---
title: Evaluation metrics for AI conversational systems
videoId: pzmbleiOfCM
---

From: [[aidotengineer]] <br/> 

Building robust [[conversational_ai_applications_in_business | conversational AI]] voice agents presents numerous challenges beyond those typically encountered with large language models (LLMs) <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. While LLMs alone struggle with hallucination, [[evaluating_ai_system_performance | evaluation]], and latency <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, voice agents add complexities like transcription in a streaming environment <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This makes [[evaluating_ai_agents_and_assistance | evaluation]] particularly difficult, especially given the lack of objective metrics for conversational quality <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Case Study: Automating Consulting-Style Interviews

A practical application for voice AI agents involves automating consulting-style interviews within large companies <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Consultants traditionally conduct these in-depth qualitative research interviews to understand how work is done <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This process is expensive, time-consuming, and inefficient due to scheduling overhead <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

While forms might suffice in some cases, the "human touch" is often necessary <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. A human interviewer can improvise, build trust, ask relevant follow-up questions, and encourage interviewees to speak freely, which often yields more information than typed answers <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

The goal was to build an AI interview agent that could conduct interviews like a human, feel like a conversation rather than a form, and enable interviewing hundreds of people simultaneously without scheduling issues or high costs <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. A key benefit would be automatic transcription for later data extraction and aggregation <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### Development Iterations and Challenges

Initially, a monolithic prompt with the OpenAI real-time API was used to conduct the interview <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. However, this approach lacked control, making it difficult to know which question the LLM was asking or to steer the conversation <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

#### Introducing Tool Use for Control

To address this, the system evolved to feed one question at a time into the prompt and introduce "tool use" <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. The LLM was given a tool to explicitly "move on to the next question" <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. Additional prompts were injected if the user navigated questions manually, allowing the agent to acknowledge shifts (e.g., "let's move on to XYZ") <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

A new problem emerged: LLMs' tendency to "chitchat," ask excessive follow-up questions, and go down "rabbit holes," making them reluctant to move to the next question <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Forcing progression too rigidly eliminated the LLM's ability to improvise <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

#### Drift Detector Agent

To combat "rabbit-holing," a separate "drift detector agent" was introduced <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. This background agent, running a non-voice, text-based LLM, listened to the conversation transcript <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. Its task was to decide if the conversation was off-track or if the current question had been sufficiently answered, allowing it to force the main LLM to use the "next question" tool and move on <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

#### Goals, Priorities, and the Next Question Agent

Despite these improvements, achieving human-like interview flow remained difficult <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. Agents either followed up too little or too much, rephrased questions poorly, and the linear "next question" flow felt restrictive <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

To enhance naturalness and guide the LLM, "goals and priorities" were added as a first-class concept <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. Instead of just the question, the LLM was informed of the "why" behind it, guiding rephrasing and follow-up questions (e.g., a high-priority goal to understand daily activities, a medium-priority goal to identify AI use cases) <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

A further "next question agent" was added, also running in the background on the transcript <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. This bot was "taught how to be a good interviewer" and could guide the conversation flow by determining what to ask next <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

#### Transcription Quality and User Experience

Transcription, a core component, posed its own challenges <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. While the OpenAI real-time API provides transcription via Whisper, Whisper operates in the text domain and can misinterpret non-speech sounds (e.g., silence, background noise) into erroneous text <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

To mitigate poor user experience from garbled transcripts, a separate agent was implemented at the UX level <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>. This agent, with full conversation context, determined whether to hide a piece of the transcript from the user if it was likely a transcription error <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. The core model still received the raw input, allowing it to correctly identify when it didn't understand and re-ask the question, which improved the user's perception <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

## The Critical Role of Systematic Evaluation (Evals)

The iterative process of adding multiple "Band-Aid" agents led to a complex system with many prompts <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. This "Vibes-driven" development made it hard to identify the root cause of issues, determine if fixes worked, and prevent regressions <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.

The solution is [[evaluating_ai_system_performance | evals]]—a systematic way to measure system performance <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. For conversational AI, this involves defining a set of desired attributes and creating an automated test suite <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.

Metrics were established, with an LLM acting as a "judge" to score conversations on attributes like:
*   Clarity <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>
*   Completeness <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>
*   Professionalism of the agent <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>

Each metric is backed by a tuned prompt <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. While not perfectly objective (lacking a perfect ground truth) and open to prompt improvements, this method significantly moves development from a purely "Vibes-driven" style to a metrics-driven approach <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

### Overcoming the Lack of Ground Truth with Synthetic Conversations

Unlike systems with objective historical data or clear ground truth, [[evaluations_versus_traditional_metrics_in_ai | conversational AI]] lacks straightforward objective metrics <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. To avoid discovering issues only after deployment, [[evaluating_ai_systems_at_scale | synthetic conversations]] were introduced <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

This involves using LLMs to act as "fake users" or interviewees <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>. Personas are created and used as prompts to guide the LLM's responses (e.g., "snarky teenager," various job functions, personalities) <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. A roster of these personas allows for running many automated interviews against them <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.

After these synthetic conversations, the same [[evaluating_ai_agents_methods_and_metrics | eval suite]] can be run, providing average metrics across a broad population of expected user types <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>. This method not only helps measure anticipated performance but also automates much of the tiring manual testing process <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.

In conclusion, while initial development can leverage basic API calls and prompt engineering, building robust voice applications requires additional strategies:
*   **Out-of-band checks:** Employing separate text-domain agents for decision-making and course correction <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.
*   **Tool use:** A powerful method for constraining LLM behavior and instrumenting its actions <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
*   **[[evaluating_ai_system_performance | Evals]]:** Critical for measuring success and guiding development, even when objective ground truth is elusive <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.