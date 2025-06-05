---
title: Addressing transcription errors and user interface
videoId: pzmbleiOfCM
---

From: [[aidotengineer]] <br/> 

Developing AI voice agents presents unique challenges beyond those found in traditional Large Language Model (LLM) applications, particularly concerning user interfaces and the accurate handling of speech-to-text transcription. While LLMs themselves can hallucinate, are difficult to evaluate, and face latency issues, voice agents magnify these problems by operating in a streaming audio environment and requiring robust transcription capabilities <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Case Study: Automating Consulting-Style Interviews

To illustrate these challenges and their solutions, Fractional AI developed an AI interview agent designed to automate the process of conducting qualitative interviews within large organizations <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. Consultants typically perform these costly and inefficient interviews to gather information about job functions or internal processes <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. The goal was to create an AI system that could conduct these interviews naturally, feeling more like a conversation than a form, while being able to interview hundreds of people simultaneously and provide automatic transcriptions <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

## User Interface (UI) Challenges and Solutions

Initially, a naive approach using OpenAI's real-time API with a monolithic prompt was attempted <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. This prompt would include all interview questions and instructions on how to navigate them <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

### Enabling Navigation and Control

A key desired UI feature was a roadmap displaying interview questions, indicating the current question, and allowing users to jump between them <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. The monolithic prompt approach proved unsuitable because:
*   There was no way for the system to know which question the LLM was currently asking <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   It was difficult to make the LLM move to a different question if the user clicked around <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

The solution involved a more modular approach:
*   **One Question at a Time**: Only one question is sent to the LLM at a time <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   **Tool Use**: The LLM is given access to a tool to explicitly request moving to the next question. When this tool is called, the next question is fed deterministically <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Contextual Prompts**: Additional prompts are injected into the LLM's stream when a user clicks around the roadmap, informing the agent that the user has navigated to a new or revisited question <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. This allows the agent to respond appropriately, such as saying, "sure, let's move on to XYZ, we can come back to that later" <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### Managing Conversation Flow with Side Agents

Even with tool use, LLMs tended to "chitchat" or "dig down rabbit holes," being reluctant to move to the next question <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Forcing the LLM too hard would eliminate its ability to improvise, which was undesirable <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

To address this, a "Drift Detector Agent" was introduced <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This is a separate, non-voice, text-based LLM running in a side thread that listens to the conversation's transcript <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. Its task is to decide if the conversation is off-track, if the current question has been answered, and if it's time to move on <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. If the Drift Detector strongly indicates it's time to move, it can force the main LLM to use its "next question" tool, preventing "rabbit holing" <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

To further refine the human-like interview flow:
*   **Goals and Priorities**: Instead of just the question, the LLM is given the *why* behind each question as "goals" (e.g., "high priority goal of getting a clear picture of responsibilities") <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. This guides rephrasing and follow-up questions <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Next Question Agent**: Another side agent, the "Next Question Agent," runs in the background on the transcript <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. It is "taught how to be a good interviewer" and decides what question should be asked next, guiding the conversation <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

## Addressing Transcription Errors

The interview system displays a live transcript of the conversation <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. While OpenAI's API provides a transcript of user input via its Whisper model, Whisper solely converts audio to text <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. Unlike the core model, which operates in the sound domain and understands non-speech sounds, Whisper can produce surprising or erroneous transcriptions from silence or background noise <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. Examples include silence being transcribed as a language change <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a> or background noise as nonsensical words like "creeping Dippity Dippity Dippity Dippity" <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. There are no API knobs to directly tune Whisper's behavior for this <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.

### UI-Level Solution for Transcription Errors

To improve the [[Improving user experience with multimodal interaction | user experience]] and avoid displaying embarrassing transcription errors, an entire separate agent was added to the system <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>. This agent's sole task is to take the entire conversation context and determine if a specific piece of the transcript should be hidden from the user due to a likely transcription error <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. While the incorrect transcript is still captured internally, hiding it prevents a poor user experience <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. Crucially, the core model still processes the original audio, so if a user's input was unintelligible, the core model's response (e.g., "I didn't really get that, could you rephrase?") still aligns with the user's perception, even if the erroneous text isn't displayed <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

## Development Challenges and Evaluation

The iterative process of adding multiple "Band-Aid" agents to fix issues creates complexity, making it difficult to know which prompt to update or if changes introduce regressions <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. This is a common problem in LLM-based development <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

To address this, systematic evaluation ("evals") is critical <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>:
*   **Automated Test Suite**: A set of metrics is used to measure attributes like clarity, completeness, and professionalism of the conversation <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. These metrics are evaluated by an LLM acting as a judge against tuned prompts <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. While not perfectly objective due to the lack of ground truth, this provides a more metrics-driven approach to iteration <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
*   **Synthetic Conversations**: To test robustness across a broad population and automate testing, LLMs are used to simulate users with specific personas (e.g., a "snarky teenager" or various job functions and personalities) <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>. The AI agent interviews these synthetic users, and the same evaluation suite can then be run over the generated conversations to get average metrics <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>.

## Conclusion

Building robust AI voice applications goes beyond simply calling an API and performing prompt engineering <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. Key additions for a robust application include:
*   **Out-of-Band Checks**: Using separate, text-domain agents to make decisions about the conversation's progress and keep it on track <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.
*   **Tool Use**: Empowering the LLM with specific tools can constrain its behavior and allow for better instrumentation and understanding of its actions <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
*   **Evaluations**: [[ChatGPT design issues | Evals]] are critical for measuring success and guiding development, even in domains without objective ground truth <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.