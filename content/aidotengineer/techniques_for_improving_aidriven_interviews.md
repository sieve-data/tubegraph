---
title: Techniques for improving AIdriven interviews
videoId: pzmbleiOfCM
---

From: [[aidotengineer]] <br/> 

Building AI voice agents, particularly for conversational user interfaces (UIs), presents significant challenges beyond those typically encountered with large language models (LLMs) alone <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. LLMs are inherently difficult to manage, prone to hallucination, and hard to evaluate with objective metrics, especially in conversational contexts <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. When audio is involved, the complexity increases, requiring handling transcription and streaming environments <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

This article details various [[techniques_and_patterns_in_ai_orchestration_and_prompt_engineering | techniques and patterns in AI orchestration and prompt engineering]] employed to overcome these hurdles in the [[case_study_of_ai_interview_agent_development | case study of AI interview agent development]] for automated consulting-style interviews.

## Case Study: Automating Consulting-Style Interviews

A specific application built is an AI interview agent designed to automate "consulting-style" interviews <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This differs from job interviews; it involves interviewing employees within large companies (e.g., Fortune 500) to gather information about how they perform their jobs <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

Human-led consulting interviews are:
*   **Expensive** and **inefficient** <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   Require **significant time** for consultants and **complex scheduling** <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

While forms might seem like an alternative, the human touch is crucial for these types of interviews <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. An interviewer needs to:
*   **Improvise** and build trust <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   Ask **relevant follow-up questions** <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   Encourage interviewees to **speak freely** and ramble, often yielding more information than typed answers <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

The goal was to build an AI interview agent that could:
*   **Conduct interviews like a human** <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   Feel like a **conversation, not a form** <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   Interview **hundreds of people concurrently** <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   Provide **automatic transcription** for data extraction and aggregation <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

## Initial Approach and Its Limitations

The initial development leveraged the OpenAI real-time API, using a monolithic prompt that outlined the interview's purpose, details, and all questions <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

However, this monolithic approach quickly revealed a limitation: the inability to display a dynamic "roadmap" of questions <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. It was impossible to know which question the LLM was currently addressing or to steer it to a different question if a user wanted to jump around <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

## Key Techniques and Solutions

To address the challenges and enhance the AI's conversational ability and control, several techniques were implemented:

### 1. Structured Questioning with Tool Use

Instead of a single large prompt, the system was redesigned to:
*   Feed **one question at a time** to the LLM <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   Introduce **tool use**, allowing the LLM to signal when it wanted to move to the next question <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This gave programmatic control over the conversation flow <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
*   **Inject additional prompts** when users clicked around the roadmap, informing the LLM about the navigation change <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. This enabled the agent to acknowledge the user's action, e.g., "Sure, let's move on to XYZ, we can come back to that later" <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

### 2. Drift Detector Agent for Contextual Steering

A challenge arose where the LLM, despite tool use, tended to "chitchat" and delve into "rabbit holes," asking too many follow-up questions and being reluctant to move on <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Forcing it too hard would eliminate its ability to improvise <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

The solution was to introduce a **background "Drift Detector Agent"** <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>:
*   It runs a **separate side thread**, listening to the conversation's transcript <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   It uses a **separate, non-voice text-based LLM call** <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   Its task is to decide if the conversation is "off track" or if the current question has been sufficiently answered, prompting a move to the next question <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   When the Drift Detector indicates a strong need to move on, it can **force the tool use** (e.g., "move to next question"), preventing further deviation <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

### 3. Goals, Priorities, and Next Question Agent

Achieving truly human-like interviews proved difficult; the AI would either follow up too little or too much, or rephrase questions in unhelpful ways <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. The linear flow (only "dig in" or "move next") was restrictive <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

To enhance natural flow and guidance:
*   **Goals and priorities** were introduced as first-class concepts for each question <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. Instead of just the question itself, the LLM is given the *why* behind the question <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. For example, for "What are your main responsibilities?", the goal might be "Get a clear picture of this person's regular activities" (high priority) and "Start to sus out where AI might be useful" (medium priority) <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. This guides rephrasing and follow-up questions <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
*   Another side agent, the **"Next Question Agent,"** was added <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. This agent, running on the transcript in the background, is "taught" how to be a good interviewer and decides what should be asked next, guiding the conversation flow <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

### 4. Transcript Hiding Agent for User Experience

The transcription of user input, handled by OpenAI's Whisper model (a side model to the core LLM), presented challenges <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. Whisper converts everything to text and doesn't operate in the sound domain like the core model <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. This led to surprising and embarrassing transcription errors for silence or background noise <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

To improve user experience (UX) without affecting the core model's understanding:
*   An **entirely separate agent** was added <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.
*   This agent reviews the entire conversation context and decides whether to **hide a piece of the transcript from the user** if a transcription error is suspected <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
*   The raw transcript is still captured for backend use, but users are spared the visual display of errors <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.
*   Crucially, the core model still receives and understands the actual audio, so it can respond appropriately (e.g., "I didn't really get that, can you rephrase?") even if the transcript is hidden from the user <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

## Overarching Development Challenges

The iterative process of adding multiple "Band-Aid" agents led to significant complexity:
*   Numerous prompts to update <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.
*   Difficulty in identifying which agent to update when an issue arose <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
*   Risk of **introducing regressions** (fixing one issue but worsening another) <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.

This highlights the [[challenges_in_aidriven_architecture_design | challenges in AI-driven architecture design]] and the need for systematic evaluation.

## Improving AI Evaluation Methods

To mitigate these challenges and guide development effectively, [[improving_ai_evaluation_methods | improving AI evaluation methods]] became critical <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>:

### Automated Test Suite with LLM as Judge
*   A set of metrics was defined to measure desired attributes like clarity, completeness, and professionalism <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
*   An **automated test suite** was developed, where another LLM acts as a "judge" to evaluate these metrics over a conversation <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. Each metric is backed by a finely tuned prompt for evaluation <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.
*   While not perfectly objective due to the lack of ground truth in conversational AI, this method provides a more metrics-driven approach to iteration, moving beyond purely "vibes-driven" development <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

### Synthetic Conversations for Comprehensive Testing
Since objective ground truth is often absent, a key technique was the introduction of [[use_of_synthetic_conversations_in_ai_testing | use of synthetic conversations in AI testing]] <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.
*   LLMs are used to **simulate "fake users"** or interviewees <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.
*   A "Persona" is created as a prompt to the LLM, defining the interviewee's characteristics (e.g., "snarky teenager" <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>). In practice, a roster of diverse personas based on expected interviewees (different personalities, job functions) is used <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>.
*   The AI agent then interviews these synthetic personas <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.
*   The same evaluation suite is run over these synthetic conversations to obtain average metrics across a broad population of user types <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>. This automates testing and helps detect edge cases before deployment <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

## Conclusion

Building robust AI voice agents, especially for complex conversational tasks, goes beyond simple prompt engineering with foundational APIs <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. Key takeaways for [[design_process_improvements_with_ai | design process improvements with AI]] include:

*   **Orchestration with Out-of-Band Checks**: Employing separate agents operating in the text domain to make decisions and guide the core AI back on track <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.
*   **Strategic Tool Use**: Leveraging tools within the LLM's capabilities to constrain behavior and provide instrumented insights into its actions <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
*   **Critical Role of Evals**: Implementing systematic evaluations, even without perfect objective ground truth, is essential for measuring success and guiding development <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. This includes using LLMs as judges and generating synthetic conversations for broad testing <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>.

By combining these techniques, developers can move beyond "vibes-driven" development to create more robust and effective AI-driven conversational systems.