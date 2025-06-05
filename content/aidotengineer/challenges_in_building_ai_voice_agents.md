---
title: Challenges in building AI voice agents
videoId: pzmbleiOfCM
---

From: [[aidotengineer]] <br/> 

Building AI voice agents presents significant [[challenges_in_developing_ai_agents | challenges]], as highlighted by Eddie Seagull, CTO at Fractional AI <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. These difficulties are compounded by the inherent complexities of working with large language models (LLMs) themselves <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## General LLM Challenges Amplified in Voice Agents

Working with LLMs is inherently difficult due to issues like:
*   **Hallucination** <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>
*   **Difficulty in Evaluation**: It's tough to evaluate LLM performance and establish metrics, especially for conversational systems where objective measures are scarce <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.
*   **Latency**: While a challenge for many LLM applications, latency is particularly critical for conversational user interfaces that require fluid, human-like interactions <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

When dealing with audio and [[voice_and_multimodal_ai_agents | voice agents]], these existing AI problems operate on "hard mode" <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Additional complexities include:
*   **Transcription**: It is not as straightforward as it might seem <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Streaming Environment**: Unlike text-based batch interactions, voice agents operate in a streaming environment, which adds complexity to development <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## Case Study: Automating Consulting Interviews

Fractional AI recently developed an AI interview agent to automate consultation-style interviews, where consultants gather information from employees within large companies through qualitative research <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This process is typically expensive and inefficient <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. The goal was to create an AI system that could conduct interviews like a human, feel conversational rather than like a form, and interview hundreds of people simultaneously without scheduling issues or high costs <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### Initial Approach and Limitations

The initial approach involved a naive integration with the OpenAI real-time API, using a monolithic prompt to instruct the LLM on conducting interviews and listing all questions <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

### Design Challenges and Solutions

Several [[design_challenges_for_ai_agents | design challenges for AI agents]] emerged:

#### 1. Guiding Conversation Flow and User Experience
*   **Challenge**: The monolithic prompt made it difficult to show a roadmap of questions, indicate the current question, or allow users to jump between questions <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. There was no way for the system to know which question the LLM was currently asking <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Solution**:
    *   **One Question at a Time**: Only one question is sent to the LLM's prompt at a time <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
    *   **Tool Use**: The LLM was given access to a "move on to the next question" tool <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
    *   **Injected Prompts**: Additional prompts are injected into the stream to inform the LLM when a user clicks around or skips questions, allowing for natural responses like "Sure, let's move on..." <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

#### 2. Preventing "Rabbit Holes" and Maintaining Focus
*   **Challenge**: LLMs tend to "chitchat," ask excessive follow-up questions, and dig into "rabbit holes," being reluctant to move on to the next question. Forcing it too hard would eliminate improvisation <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Solution**:
    *   **Drift Detector Agent**: An additional background agent runs a separate side thread, using a non-voice, text-based LLM to listen to the conversation transcript <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. This agent determines if the conversation is off-track, if the current question has been answered, and if it's time to move on <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. If strongly advised, it can force the main LLM to use the "next question" tool <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

#### 3. Enhancing Human-like Interview Nuance
*   **Challenge**: Even with the previous solutions, it was hard to tune for human-like interviews. Agents followed up too little or too much, rephrased questions in unhelpful ways, and the linear flow was restrictive <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Solution**:
    *   **Goals and Priorities**: The system now provides the "why" behind each question, allowing the LLM to be informed when rephrasing or asking follow-up questions. For instance, a question might have a high-priority goal of "getting a clear picture of daily activities" and a medium-priority goal of "sussing out where AI might be useful" <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
    *   **Next Question Agent**: Another side agent, trained to be a good interviewer, runs in the background on the transcript, determining what should be asked next and guiding the conversation <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

#### 4. Addressing Transcription Errors
*   **Challenge**: The OpenAI real-time API uses Whisper for transcription, which converts everything to text. It doesn't understand non-speech sounds like claps or coughs, leading to nonsensical transcriptions for silence or background noise <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. There are no direct controls to tune this via the API <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
*   **Solution**:
    *   **Transcript Hiding Agent**: A separate agent takes the entire conversation context and decides whether to hide a piece of the transcript from the user if a transcription error is suspected <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>. The full, potentially erroneous, transcript is still captured internally. This improves user experience, as the core model still understands the user's intent even if the displayed transcript is garbled <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.

## Overarching Development Challenges and Evaluation

Building these systems leads to significant complexity, with numerous agents "Band-Aiding" different issues. It becomes challenging to update prompts, identify which agent to fix, or avoid regressions <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. This is common in LLM development but particularly hard in the voice domain <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

### 1. Lack of Objective Evaluation Metrics
*   **Challenge**: There is no perfect ground truth or objective metric to definitively measure how well a conversational AI system performs <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
*   **Solution**:
    *   **LLM-as-Judge Evals**: An automated test suite measures various attributes of the conversation (e.g., clarity, completeness, professionalism) by asking an LLM acting as a judge <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. While not perfectly objective, this provides a more metrics-driven iteration style <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

### 2. Testing and Identifying Edge Cases
*   **Challenge**: Manual testing is tiresome, and it's hard to anticipate all user behaviors and edge cases that might lead to a poor user experience in practice <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.
*   **Solution**:
    *   **Synthetic Conversations**: LLMs are used to create "fake users" or interviewees with defined personas (e.g., "snarky teenager" or various job functions and personalities) <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>. The AI agent interviews these synthetic personas, and the same evaluation suite can be run over the conversations to get average metrics across a broad population of expected users <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>. This helps automate testing and identify how the system would perform against different user types <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

## Key Takeaways
*   The naive approach of simply calling an API and relying on prompt engineering is often insufficient for building robust voice AI applications <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>.
*   **Out-of-Band Checks**: Employing separate agents operating in the text domain (rather than audio) to make decisions and guide the conversation is highly beneficial <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.
*   **Tool Use**: Giving LLMs access to tools is powerful for constraining behavior and instrumenting the LLM to understand its actions <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
*   **Evals are Critical**: As with all LLM-based projects, evaluations are essential for measuring success and guiding development, even when objective ground truth is unavailable <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.