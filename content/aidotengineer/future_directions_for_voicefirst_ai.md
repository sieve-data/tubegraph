---
title: Future directions for voicefirst AI
videoId: y9YQc9a3gNw
---

From: [[aidotengineer]] <br/> 

The field of voicefirst AI is exploring new paradigms, particularly the "voicefirst AI overlay," which aims to keep humans actively involved in the progress of increasingly powerful AI systems through natural voice interfaces <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## The Voicefirst AI Overlay Explained

A [[voicefirst_ai_overlays | voicefirst AI overlay]] sits alongside human-to-human conversations, providing real-time assistance without becoming a third speaker <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. Unlike typical voice AI interactions where a human speaks directly with an AI, the overlay paradigm involves an AI operating in between two humans to enhance their dialogue <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. It passively listens to natural dialogue and surfaces relevant help under specific contexts, such as language suggestions, phrase suggestions, or definitions, staying out of the way until needed <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. This enables an [[ambient_agents_and_voice_technology | ambient agent]] that is conversationally aware <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Why Now?
The development of voicefirst AI overlays is becoming feasible due to two major ongoing "explosions":
*   **Agent Capability Wave:** Agents are becoming more powerful, with improved [[future_directions_for_software_architecture_using_ai | RAG systems]], multi-step tool calling, and the ability to act over longer time horizons, alongside advancements in agent orchestration <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a> <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   **Voice Technology Wave:** Time to first token is reducing, latency has significantly improved, and full duplex speech models are on the horizon <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

Combining these waves could offer real-time assistance via agents in an ambient, conversational setting <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Demonstration Example
An example demo illustrates real-time conversational assistance during a live foreign language call when one participant is not fluent <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. The overlay employs caption scraping, smart debouncing, and context management to provide foreign language suggestions aligned with the ongoing conversation <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. This includes an LM pipeline for suggestion and translation endpoints, all integrated into the voicefirst AI overlay <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

## Role in the AI Landscape
Overlays fit into the existing AI stack by leveraging core speech models (speech recognition, text-to-speech) and intent/agent frameworks <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. An overlay doesn't act as the agent itself but determines when and where an agent's help should surface <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Unlike meeting bots or notetakers that operate after a conversation, overlays function during live interaction <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. They aim to amplify the humans in the room rather than participating directly in the dialogue <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

## Challenges and Design Principles

### [[challenges_and_potential_of_ai_assistants | Challenges]]
Developing voicefirst AI overlays presents significant [[challenges_in_building_ai_voice_agents | challenges]]:
*   **Timing:** Help that arrives too early can interrupt, while help that arrives too late is useless <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   **Relevance:** Incorrect context leads to "spam" suggestions <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Attention:** Help that derails the conversation by not respecting conversational flow is unusable <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Latency:** Must be well-managed throughout the interaction <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

These are summarized as the "Four Horsemen of Overlay Engineering":
1.  **Jitterbug Input:** Managing pauses and speech-to-text interruptions, requiring effective debouncing <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.
2.  **Context Repair:** Optimizing the entire pipeline for sub-second speed limits to provide live assistance <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
3.  **Premature Interrupt / No Show:** Ensuring help arrives at the right time through strong conversational awareness <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
4.  **Glanceable Ghost:** Designing user interfaces that don't overload attention or obstruct views, being flexible and dismissible <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

Significant UX research on cognitive load, overlay design, and timing is crucial, intersecting human-computer interaction with AI UX <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

### Design Principles
Key principles for designing overlays include:
1.  **Transparency and Control:** Users should be able to decide the level of overlay involvement <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
2.  **Minimum Cognitive Load:** The system, however intelligent, should not overload or derail the speakers <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
3.  **Progressive Autonomy:** Users should be able to moderate the amount of help they receive over time to facilitate learning <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

## Exciting Aspects and Open Questions

### What's Exciting
*   **Latency:** Latency is within striking distance, allowing roundtrip calls to fast-provisioned LM providers in 500-700 milliseconds, with very low time to first token <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
*   **Privacy by Design:** Smaller, increasingly capable models raise possibilities for entirely on-device inference to maintain privacy <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.
*   **User Experience Ethos:** Injecting a strong UX ethos that values and respects human conversation as native and protected <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
*   **Voice as a Linkable Surface:** Speculative exploration of how ambient agents in calls could be linked and orchestrated <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

### Open Questions and Curiosities
*   **ASR Errors:** How to manage cascading errors from Automatic Speech Recognition (ASR), where a small word error rate can lead to incorrect advice (e.g., "do" vs. "don't") <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. Pairing with conversational context could be a solution <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
*   **Prosody and Timing Complexity:** The loss of micro-intonation signals when converting speech to text, and whether relevant assistance can still be provided despite this information loss <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   **Security Surface:** New security risks posed by agents interacting in live conversations, indicating a completely new security surface to consider <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

## [[future_opportunities_and_transformation_with_ai_agents | Future Directions]] for Voicefirst Overlays

Further extensions and [[future_directions_for_software_architecture_using_ai | future directions]] for voicefirst overlays include:
*   **Full Duplex Speech Models:** Moving beyond speech-to-text conversion to directly process raw audio through speech models and provide contextual suggestions based on audio features <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
*   **[[evaluation_techniques_for_multimodal_and_voice_ai_agents | Multimodal Understanding]]:** Incorporating live video or visual information to enhance AI interaction <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.
*   **Speculative Execution and Caching:** Optimizing performance through predictive processes <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.

Overall, with the explosion of [[voice_ai_and_its_applications_in_enhancing_customer_experience | voice AI]], the future appears conversational, with technology ready but interfaces still needing significant development <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.