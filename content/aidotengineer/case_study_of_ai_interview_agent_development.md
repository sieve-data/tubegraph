---
title: Case study of AI interview agent development
videoId: pzmbleiOfCM
---

From: [[aidotengineer]] <br/> 

Eddie Seagull, CTO at Fractional AI, discusses the development of AI voice agents, focusing on the [[challenges_in_building_ai_voice_agents | challenges encountered]] and solutions implemented <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Developing AI voice agents presents significant difficulties beyond typical Large Language Model (LLM) issues <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## General Challenges with AI Voice Agents
Standard LLM challenges include:
*   Difficulty with reliability <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   Hallucinations <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>
*   Difficulty in evaluation <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>
*   Lack of objective metrics for conversational systems <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>
*   Latency, especially for fluid conversational user interfaces <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>

When dealing with audio and voice agents, these issues become "hard mode" <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Additional complexities include:
*   Transcription challenges <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>
*   Operating in a streaming environment instead of a batched back-and-forth interaction <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>
These factors make development very difficult <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Case Study: Automating Consulting-Style Interviews
A recent application built by Fractional AI aims to automate "consulting-style" interviews <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This involves interviewing employees within large companies to gather information, distinct from job interviews <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### The Problem with Human Interviews
*   **Expense**: Sending consultants to interview numerous employees is very costly <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **Inefficiency**: Requires significant time to schedule and conduct interviews, leading to high overhead <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **Human Touch**: While forms might suffice in some cases, the human element is often crucial for:
    *   Improvisation and navigation <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>
    *   Building trust <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>
    *   Asking effective follow-up questions <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>
*   **Answer Quality**: People answer differently when typing versus speaking freely, often providing more information when allowed to ramble <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### Goal of the AI Interview Agent
The objective was to build an AI interview agent that could:
*   Conduct interviews like a human <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   Feel more like a conversation than a form <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   Interview hundreds of people simultaneously, avoiding scheduling issues and high costs <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   Automatically transcribe conversations for data extraction and aggregation <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

A demo showed the agent conducting a basic interview, illustrating the conversational flow and the agent's ability to understand and respond to user input <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

## Initial Development Approach and Challenges
The initial approach involved a "naive" integration with the OpenAI real-time API <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   A large, monolithic prompt was used to explain the interview goal, provide questions, and guide navigation <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

A key early requirement was to display a roadmap of questions, allowing users to see current progress and jump between questions <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. This was not well-suited to the monolithic prompt because:
*   It was difficult to know which question the LLM was currently asking <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   Coaxing the LLM to move between questions if the user clicked around was challenging <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

## Iterative Improvements and Agent-Based Solutions
### One Question at a Time & Tool Use
To address the roadmap issue, the system was redesigned to:
*   Send only one question at a time to the LLM <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   Introduce "tool use" by giving the LLM a tool to signal when it wanted to move to the next question <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   Deterministically feed the next question once the tool was called <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   Inject additional prompts when users skipped or revisited questions via the roadmap, informing the LLM of the user's action <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. This allowed the agent to respond appropriately, e.g., "Sure, let's move on to XYZ" <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### The "Rabbit Hole" Problem and Drift Detector Agent
A new problem emerged: LLMs tended to go down "rabbit holes," chitchatting, asking too many follow-up questions, and being overly encouraging <a class="yt="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. This led to a reluctance to move on to the next question <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. Forcing it too hard would eliminate the desired improvisation <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

To counter this, a **Drift Detector Agent** was introduced <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>:
*   A separate background agent listens to the conversation <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   It runs a side thread with a non-voice, text-based LLM call <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   Its task is to assess from the transcript if the conversation is on or off track <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   It determines if the current question has been answered and if it's time to move on <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
*   If the agent strongly indicates it's time to move, it can force the tool use, preventing further rabbit-holing <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

### Tuning Human-like Interviews
Achieving human-like interviews remains challenging <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. Agents tend to:
*   Follow up too little or too much <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
*   Rephrase questions in unhelpful ways <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   The "one question at a time" approach limits the LLM's full understanding of the interview flow <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   The linear flow (only option is "next question") restricts natural conversation <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

To correct for this:
*   **Goals and Priorities**: Added as a first-class concept to the interview plan <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. The LLM is told the "why" behind each question, informing its rephrasing and follow-up questions <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. For example, a high-priority goal might be "get a clear picture of this person's regular activities," and a medium priority "start to sus out where AI might be useful" <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   **Next Question Agent**: Another side agent was introduced to determine what question should be asked next, running on the transcript in the background <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. This bot is "taught" to be a good interviewer and can guide the conversation flow <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

### Transcription Challenges
The system uses Whisper for transcription, provided by OpenAI's real-time API <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>. While the core model understands sound (e.g., claps, coughs), Whisper converts everything to text <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. This leads to issues:
*   Silence can be misinterpreted as non-English speech <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
*   Background noise can result in garbled or nonsensical transcriptions <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
*   The OpenAI API does not offer granular control or "knobs" to tune Whisper's behavior <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

To manage this user experience (UX) issue:
*   **Transcript Hiding Agent**: An additional agent was added to the UX layer <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>. This agent takes the full conversation context and decides whether a piece of the transcript should be hidden from the user due to a suspected transcription error <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
*   The incorrect transcript is still captured for internal use, but it's hidden from the user, preventing embarrassing displays <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.
*   The core model still understands what's happening (e.g., "I didn't really get that, could you rephrase?"), and hiding the transcript improves the user experience by reducing confusion <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

## Development Challenges and Evaluation
The development process became complex, involving many agents added as "Band-Aids" to fix issues discovered during testing <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. This "Vibes driven" approach, while acceptable initially, led to:
*   Increased complexity and numerous prompts to update <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   Uncertainty about which agent to update when an issue arose <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
*   Introduction of regressions (fixing one issue, breaking another) <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.
This is a common challenge in LLM-based [[developing_and_optimizing_ai_agents | development]], but it's particularly acute in the voice domain <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

### Evaluation (Evals)
To systematically measure performance, **evals** are crucial <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.
*   A set of metrics was developed to measure various attributes <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
*   An automated test suite runs over conversations, asking an LLM acting as a "judge" to measure attributes like clarity, completeness, and professionalism <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. Each metric is backed by a tuned prompt <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.
*   This approach, while not perfectly objective, moves development from a purely "Vibes driven" style to a "metrics driven" one <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

#### Lack of Ground Truth & Synthetic Conversations
For systems like this, there's no perfect ground truth or historical data to objectively measure success <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. To prevent shipping a system that annoys users or has edge cases <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>:
*   **Synthetic Conversations** were introduced <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.
*   LLMs are used to simulate various "users" (interviewees) and conduct fake interviews <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.
*   Personas are created (e.g., "snarky teenager in charge of a Fortune 500 company") and used as prompts for the LLM playing the interviewee <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. A roster of different personality types and job functions is maintained <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
*   The interview agent interacts with these personas, and the same [[evaluating_ai_agents_and_assistants | eval suite]] is run afterward <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>. This allows for measuring average metrics across a broad population of expected users <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>, and aids automation, reducing the need for manual testing <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.

## Key Takeaways for AI Agent Development
The development of AI voice agents, as demonstrated by this case study, highlights that simply calling an OpenAI API with voice capabilities is insufficient for a robust application <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.

Key [[best_practices_and_lessons_learned_in_ai_agent_development | lessons learned]] include:
*   **Prompt Engineering**: While helpful for initial development, it's not enough for robustness <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   **Out-of-Band Checks with Separate Agents**: Using separate agents operating in the text domain (not audio) to make decisions and guide the conversation is crucial for getting the system back on track <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.
*   **Tool Use**: Highly powerful for constraining LLM behavior and instrumenting it to understand its actions, as the LLM must call specific tools to perform desired actions <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
*   **Evals are Critical**: Essential for measuring success and guiding development, even when there's no objective source of truth <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. They enable a more robust development process <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.