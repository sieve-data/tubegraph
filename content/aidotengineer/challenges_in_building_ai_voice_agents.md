---
title: Challenges in building AI voice agents
videoId: pzmbleiOfCM
---

From: [[aidotengineer]] <br/> 

Building AI voice agents presents significant [[Challenges in AI agent development | challenges]] beyond standard Large Language Model (LLM) applications <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. While LLMs themselves are difficult to wrangle due to issues like hallucination and evaluation <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, voice agents add layers of complexity, particularly in conversational user interfaces where fluidity is key <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## General Difficulties with Voice Models
Working with voice models is described as "hard mode" for AI development <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Existing AI problems are compounded by the need to handle:
*   **Transcription** <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>: Not as straightforward as it might seem.
*   **Streaming Environments** <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>: Unlike batch text interactions, voice is continuous.
*   **Evaluation** <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>: Measuring performance in conversational settings where there's no objective metric for success or failure <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   **Latency** <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>: Critical for fluid, human-like conversations <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

These factors make [[Development and Challenges of AI Agents | development]] particularly difficult <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Case Study: Automating Consulting-Style Interviews
A practical example of building an AI voice agent involves automating consulting-style interviews within large companies <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This process typically involves expensive, inefficient human interactions to gather qualitative research <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. The goal was to create an AI interview agent that could conduct interviews like a human, feel conversational, and provide automatic transcription, while being able to interview hundreds of people simultaneously <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

The initial approach involved a "naive" [[integrating_openai_api_with_voice_agents | OpenAI real-time API]] integration with a single, large prompt explaining the interview context and questions <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

### Specific Challenges and Solutions

#### Challenge 1: Structured Navigation and User Control
**Problem**: The monolithic prompt approach made it impossible to know which question the LLM was currently asking or to enable users to jump between questions via a roadmap <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
**Solution**:
*   **One Question at a Time**: The system was redesigned to feed the LLM one question at a time <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   **Tool Use**: The LLM was given a tool to signal when it wanted to move to the next question, allowing the system to deterministically feed it the subsequent question <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Injected Prompts**: Additional prompts were injected into the stream to inform the LLM when a user clicked around the roadmap, ensuring the agent was aware of user-driven navigation <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

#### Challenge 2: Avoiding "Rabbit Holes" and Off-Topic Conversations
**Problem**: LLMs tend to chitchat, ask excessive follow-up questions, and generally be reluctant to move on, leading to "rabbit holing" <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Forcing it too hard would eliminate its ability to improvise <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
**Solution**:
*   **Drift Detector Agent**: A separate, non-voice text-based LLM was introduced to run in a background thread, listening to the conversation transcript <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This "drift detector" agent decides if the conversation is off-track, if the question has been answered, and if it's time to move on <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. If it strongly indicates moving on, the system can force tool use to prevent further rabbit holing <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

#### Challenge 3: Maintaining Human-like Interview Flow and Purpose
**Problem**: Even with the drift detector, agents often followed up too little or too much, rephrased questions poorly, and struggled with the linear flow, limiting natural conversation <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. The LLM didn't always know the overall interview plan <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
**Solution**:
*   **Goals and Priorities**: Interview questions were augmented with explicit goals and priorities, providing the LLM with the "why" behind each question <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. This informed rephrasing and follow-up questions <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. For instance, a high-priority goal might be to get a clear picture of responsibilities, while a medium priority might be to identify areas for AI <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   **Next Question Agent**: Another side agent was introduced, running on the transcript in the background, specifically tasked with determining what question should be asked next <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. This agent is "taught how to be a good interviewer" and can guide the conversation path <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

#### Challenge 4: Handling Transcription Errors from Underlying Models
**Problem**: While [[integrating_openai_api_with_voice_agents | OpenAI's API]] provides transcripts, its side model (Whisper) for transcription can produce inaccurate results for non-speech sounds like silence or background noise, leading to strange and embarrassing transcriptions <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. There are no direct tuning options for this within the OpenAI real-time API <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.
**Solution**:
*   **Transcript Filtering Agent**: An additional agent was added to the UX layer <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>. This agent takes the full conversation context and decides whether to hide a piece of the transcript from the user if it's likely a transcription error <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. The core model still receives the full, potentially erroneous, transcript, allowing it to respond naturally (e.g., "I didn't get that, can you rephrase?") <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

## Overarching Development Challenges and Solutions

The iterative "Vibes-driven" approach of adding multiple agents to fix problems results in complex systems with many prompts <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. This leads to [[technical_challenges_in_ai_agent_development | challenges]] such as:
*   Difficulty determining which agent/prompt to update <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
*   Risk of introducing regressions (fixing one issue but worsening another) <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

To overcome these [[challenges_in_creating_effective_ai_agents | challenges]] and measure performance:

### Evaluation (Eval)
*   **Automated Test Suite**: A systematic way to measure performance is crucial <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. This involves running an automated test suite over conversations and using an LLM as a judge to measure attributes like clarity, completeness, and professionalism <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   **Objective vs. Subjective**: While still not perfectly objective due to the lack of ground truth, LLM-based evals offer a more metrics-driven approach compared to purely "Vibes-driven" iteration <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

### Synthetic Conversations
**Problem**: The lack of objective ground truth for human-like interviews and the impracticality of constant manual testing <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
**Solution**:
*   **Simulated Users**: Use LLMs to generate "synthetic conversations" by faking users and interviewees <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
*   **Personas**: Create detailed personas (e.g., "snarky teenager," different job functions, personalities) that are used as prompts for the LLM playing the interviewee role <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.
*   **Automated Measurement**: Run the AI agent through a roster of these synthetic personas, then apply the same evaluation suite to get average metrics across a broad population of expected users <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>. This helps identify edge cases before deploying to real users <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.

## Key Takeaways for [[building_effective_ai_agents | Building Effective AI Agents]]
*   **Beyond Naive API Calls**: Simply calling an API and doing prompt engineering is insufficient for robust voice applications <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.
*   **Out-of-Band Checks**: Incorporate separate, specialized agents operating in the text domain (not audio) to make decisions and guide the primary voice agent <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.
*   **Tool Use**: Leverage tools to constrain LLM behavior and instrument its actions, providing insights into its decision-making <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
*   **Evaluations (Evals)**: Crucial for measuring success and guiding [[Challenges in AI Development | development]] <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. Even without perfect objective truth, evals (like synthetic conversations) enable a robust development process <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>.