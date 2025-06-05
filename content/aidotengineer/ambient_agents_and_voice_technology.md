---
title: Ambient agents and voice technology
videoId: y9YQc9a3gNw
---

From: [[aidotengineer]] <br/> 

Conversation is considered the oldest interface, with voice being our original API, mastered even before fire <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. While humans interact live, AI has historically been locked out of direct conversational assistance <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This article explores how more powerful [[AI agents beyond chatbots | AI agents]] can keep humans in the loop through voice, their most natural interface <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## The Horizon of Voice AI and Agents

The convergence of two significant developments makes this future possible:
1.  **Highly Specialized Agents**: These [[AI agents beyond chatbots | agents]] are becoming capable of performing complex tasks over longer time horizons <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This includes better Rag systems, multi-step tool calling, and enhanced agent orchestration <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
2.  **The [[Voice AI and its applications in enhancing customer experience | Voice AI]] Wave**: Conversational agents are making AI highly accessible, allowing users to interact via calls, search for information, and receive responses <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Improvements include reduced time to first token and latency, with full-duplex speech-to-speech models on the horizon <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

While these "explosions" are ongoing, the user experience for ambient agents that respond to events rather than text chats is still being defined <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## [[Voicefirst AI overlays | Voice-first AI Overlays]]

A [[voicefirst_ai_overlays | voice-first AI overlay]] sits alongside human-to-human calls, providing real-time assistance without becoming a third speaker <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. It is native to voice, enhancing and augmenting dialogue passively <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. Unlike typical voice AI interactions where a human speaks directly with an AI, the overlay paradigm involves an AI operating *between* two humans <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

### How Overlays Work
The overlay passively listens to natural dialogue and surfaces relevant help under specific contexts, such as language or phrase suggestions and definitions <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. It remains out of the way until needed, effectively enabling an ambient agent that is conversationally aware <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.

### Demonstration Example
A demo illustrates real-time conversational assistance in a live foreign language call, where the user may not speak the language fluently <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. The overlay pipeline involves:
*   Caption scraping <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>
*   Smart debouncing <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>
*   Managing context to provide relevant foreign language suggestions from the LM <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>
*   An entire LM pipeline for suggestion and translation endpoints <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>

### Placement in the AI Landscape
[[Voicefirst AI overlays | Overlays]] fit into the AI stack by sitting above core [[speech recognition technology and applications | speech models]] (speech-to-text, text-to-speech) and below intent and agent frameworks <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. They decide when and where an agent's help surfaces, without being concerned with the agent's internal workings <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Unlike meeting bots or notetakers that operate after a conversation, overlays function during live interactions <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. They do not participate directly in the dialogue but amplify the humans in the room <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

## Design Challenges
Designing effective overlays requires significant UX research, focusing on cognitive load, overlay design, and timing <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. The challenge lies in ensuring that assistance is provided optimally in a live conversation:
*   **Too Early**: If help arrives too early, it becomes an interruption <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   **Too Late**: If it comes too late, the opportunity for highest value is missed, making it useless <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   **Wrong Context**: If help is loaded with the wrong context, it becomes spam <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Derailment**: Even if timely and relevant, if it derails the conversation, it's not usable as it hasn't respected the conversational flow <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Latency**: Throughout all of this, latency must still be well-managed <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

In summary, the key challenges are **timing, relevance, attention, and latency** <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

## [[Challenges in building AI voice agents | Engineering Challenges]]: The Four Horsemen of Overlay Engineering
When building these systems, developers will likely encounter four main technical hurdles <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>:

1.  **Jitterbug Input**: Speech-to-text systems can pause when speakers take breaths, leading to inconsistent input. Debouncing is crucial to manage these moments <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.
2.  **Context Repair**: Providing live assistance requires a sub-second speed limit, meaning the entire processing pipeline must be highly optimized <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
3.  **Premature Interrupt or No Show**: Help can arrive too early (premature interrupt) or too late/not at all (no show) <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. Good conversational awareness is needed to know the right moment to intervene <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
4.  **Glancible Ghost**: Hints or suggestions tax a user's attention <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. The overlay should not obstruct the view, must be flexible, and dismissible, adhering to strong user interface principles <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

## Design Principles for Overlays
For any overlay, several principles should be considered:
*   **Transparency and Control**: Users should be able to decide how much the overlay intervenes in the conversation <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   **Minimum Cognitive Load**: Even the most intelligent system is unusable if it overloads speakers or derails their conversation <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
*   **Progressive Autonomy**: The system should allow users to moderate the amount of help they receive over time, supporting learning and natural progression <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

## Exciting Aspects of the Space
Several aspects make this field particularly promising:
*   **Latency Improvements**: Roundtrip calls to fast-provisioned LM providers can now be threaded within 500-700 milliseconds, with very low time to first token <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
*   **Privacy by Design**: Models are becoming increasingly capable while being smaller, raising the possibility of running them entirely on-device to ensure privacy by default <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.
*   **Strong User Experience Ethos**: Injecting a UX dance that values and respects human conversation, treating it as something native and needing protection <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
*   **Voice as a Linkable Surface**: The speculative idea of ambient agents in live human conversations being linked or orchestrated in new ways <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

## Open Questions and [[Future directions for voicefirst AI | Future Directions for Voice-first AI]]

Several challenges and areas for future exploration remain:
*   **ASR Errors Cascading**: [[Speech recognition technology and applications | Automatic Speech Recognition]] (ASR) errors can lead to incorrect advice (e.g., "don't" transcribed as "do") <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. Pairing ASR with extensive conversational context could be a solution <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
*   **Prosody and Timing Complexity**: Human ears are hardwired to detect micro-intonation signals, which are lost when converting speech straight to text <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. The impact of this information loss and whether relevant assistance is still possible needs further investigation <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
*   **Security Surface**: Agents interacting in live conversations introduce a new security surface that requires careful consideration <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

### Extensions and [[Future directions for voicefirst AI | Future Directions]]
*   **Full Duplex Speech Models**: These models, on the horizon, would process raw audio through a speech model directly without converting it to text, potentially offering contextual suggestions based on audio features <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
*   **[[Evaluation techniques for multimodal and voice AI agents | Multimodal Understanding]]**: Integrating live video alongside audio could provide additional information to make AI interaction more helpful <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>.
*   **Speculative Execution and Caching**: These techniques could further enhance responsiveness and efficiency <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.

The field is dynamic and interesting, with the future appearing conversational given the explosion of [[Voice AI and its applications in enhancing customer experience | voice AI]] <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. While the technology seems ready, the interfaces are still evolving <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.