---
title: Case study on automating interviews with AI
videoId: pzmbleiOfCM
---

From: [[aidotengineer]] <br/> 

Building AI voice agents presents significant challenges, as they inherit common issues with large language models (LLMs) like hallucination and difficulty in evaluation, plus additional complexities specific to audio processing like transcription and streaming environments <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This case study details the development of an AI interview agent designed to automate consulting-style interviews, highlighting the practical challenges encountered and the iterative solutions implemented.

## Automating Consulting-Style Interviews

Traditionally, consultants engage in resource-intensive, qualitative interviews with employees within large companies to gather information about processes and jobs <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>. This method is expensive, inefficient, and fraught with scheduling overhead <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. While forms might seem like an alternative, the "human touch" of an interviewer is often crucial for navigating improvisation, building trust, and asking nuanced follow-up questions <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. People also tend to provide richer, more detailed answers when speaking freely rather than typing responses <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.

The goal was to develop an [[conversational_ai_applications_in_business | AI interview agent]] that could replicate this human-like interaction <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>. This system would feel more like a natural conversation than a form, but with the ability to interview hundreds of people simultaneously, eliminating scheduling conflicts and high costs <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. A key byproduct would be automatic transcription for data extraction and aggregation <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>.

## Iterative Development and Challenges

The development process involved several iterations to overcome fundamental limitations of LLM-based voice agents:

### Initial Approach: Monolithic Prompting
The first attempt involved integrating with OpenAI's real-time API using a single, large prompt that described the interview's purpose and included all questions <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.

**Challenge:** This "monolithic prompt" approach made it impossible to track which question the LLM was currently asking or to guide it to specific questions, which was crucial for a user interface featuring a roadmap allowing users to jump between questions <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>.

### Iteration 1: Structured Questions and Tool Use
To address navigation and tracking, the system was redesigned to feed the LLM one question at a time <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>. [[role_of_ai_agents_in_workflow_automation | Tool use]] was introduced, allowing the LLM to signal when it was ready to move to the next question. Specific prompts were also injected when a user clicked to a new question, informing the LLM of the jump <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>. This allowed the agent to acknowledge skips and revisits naturally <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>.

**Challenge:** Despite the new structure, LLMs tend to "chitchat," ask excessive follow-up questions, and "dig down rabbit holes," making them reluctant to move on <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>. Forcing it too hard would stifle its ability to improvise <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>.

### Iteration 2: The Drift Detector Agent
To manage the LLM's tendency to stray, a separate background [[role_of_ai_agents_in_workflow_automation | agent]], called the "drift detector," was introduced <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>. This agent, operating on a separate text-based LLM, listened to the conversation transcript and decided if the interview was going off-track or if the current question had been sufficiently answered <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a>. If the drift detector strongly indicated it was time to move on, it could force the main LLM to use the "next question" tool <a class="yt-timestamp" data-t="08:04:00">[08:04:00]</a>.

**Challenge:** Even with the drift detector, tuning for human-like interviews remained difficult <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>. Agents either followed up too little or too much, and rephrased questions in unhelpful ways. The linear "next question" flow was restrictive, limiting natural conversation <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>.

### Iteration 3: Goals, Priorities, and the Next Question Agent
To enhance the interview quality and natural flow, two further additions were made:
*   **Goals and Priorities:** Instead of just providing the question, the LLM was given the "why" behind each question, including high and medium priority goals (e.g., "get a clear picture of this person's regular activities" or "sus out where AI might be useful") <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>. This guided the LLM's rephrasing and follow-up questions <a class="yt-timestamp" data-t="09:16:00">[09:16:00]</a>.
*   **Next Question Agent:** Another side [[role_of_ai_agents_in_workflow_automation | agent]], the "next question agent," was specifically tasked with determining what question should be asked next <a class="yt-timestamp" data-t="09:27:00">[09:27:00]</a>. This bot, trained on principles of good interviewing, could actively guide the conversation path <a class="yt-timestamp" data-t="10:31:00">[10:31:00]</a>.

## Addressing Transcription and [[user_experience_design_with_ai | User Experience]]

While OpenAI's real-time API provides user transcripts, it relies on a separate "Whisper" model for transcription <a class="yt-timestamp" data-t="11:05:00">[11:05:00]</a>. Unlike the core LLM, Whisper operates purely on text and can produce surprising or inaccurate results when encountering non-speech sounds or silence <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>. For example, silence might be transcribed as a non-English phrase, or background noise as random words <a class="yt-timestamp" data-t="11:54:00">[11:54:00]</a>.

**Solution:** An additional agent was introduced to improve [[user_experience_design_with_ai | user experience]] <a class="yt-timestamp" data-t="12:37:00">[12:37:00]</a>. This agent takes the entire conversation context and decides whether to hide a piece of the transcript from the user if it suspects a transcription error <a class="yt-timestamp" data-t="12:40:00">[12:40:00]</a>. While the incorrect transcript is still captured internally, hiding it prevents embarrassing errors from showing up in the UI <a class="yt-timestamp" data-t="12:54:00">[12:54:00]</a>. Crucially, the core LLM still understands the audio input, allowing it to respond appropriately (e.g., "I didn't really get that, what do you hope to accomplish?") <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.

## The Importance of Evaluation (Eval)

The iterative process of adding multiple side agents to "Band-Aid" over issues led to increased complexity <a class="yt-timestamp" data-t="13:28:00">[13:28:00]</a>. With numerous prompts and agents, it became difficult to diagnose problems, implement fixes without introducing regressions, or measure overall performance <a class="yt-timestamp" data-t="13:48:00">[13:48:00]</a>.

**Solution: LLM-as-Judge Evals and Synthetic Conversations**
To systematically measure performance, a set of metrics was developed and evaluated by an LLM acting as a judge <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>. These metrics, such as "clarity," "completeness," and "professionalism," are derived from prompts that analyze conversation transcripts <a class="yt-timestamp" data-t="14:36:00">[14:36:00]</a>. While not perfectly objective due to the lack of ground truth, this approach provides a metrics-driven style of iteration over purely "vibes-driven" development <a class="yt-timestamp" data-t="15:01:00">[15:01:00]</a>.

To further refine evaluation and prevent real-world user issues, "synthetic conversations" were introduced <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>. This involves using LLMs to create "fake users" with specific personas (e.g., "snarky teenager" or various job functions and personalities) who then interact with the AI interview agent <a class="yt-timestamp" data-t="16:17:00">[16:17:00]</a>. The same evaluation suite can then be run over these synthetic conversations, allowing for automated testing and the generation of average metrics across a broad population of potential interviewees <a class="yt-timestamp" data-t="17:00:00">[17:00:00]</a>.

## Key Takeaways

Building robust [[conversational_ai_applications_in_business | AI voice applications]] requires more than just basic API calls and prompt engineering <a class="yt-timestamp" data-t="17:31:00">[17:31:00]</a>. Key strategies include:
*   **Out-of-Band Checks:** Employing separate [[role_of_ai_agents_in_workflow_automation | agents]] operating in the text domain to make decisions and guide the main conversation <a class="yt-timestamp" data-t="17:55:00">[17:55:00]</a>. This is an example of [[ai_in_workflow_automation | AI in workflow automation]].
*   **Tool Use for Constraint:** Leveraging tools to constrain LLM behavior and instrument its actions, providing insights into its decision-making process <a class="yt-timestamp" data-t="18:10:00">[18:10:00]</a>.
*   **Critical Evals:** Systematically measuring success and guiding development using [[case_studies_and_practical_examples_of_ai_implementation | evaluation]] metrics, even in domains without objective ground truth <a class="yt-timestamp" data-t="18:28:00">[18:28:00]</a>.