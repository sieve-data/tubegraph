---
title: Designing conversational copilots
videoId: y9YQc9a3gNw
---

From: [[aidotengineer]] <br/> 

A "voice-first AI overlay," also known as a conversational copilot, is a system designed to sit alongside human-to-human conversations and offer real-time assistance without becoming a third speaker <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. Its purpose is to enhance and augment the dialogue between two humans <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. Voice is considered the original interface, or "our original API," mastered even before fire <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

The core question driving this concept is how to keep humans in the loop with the progress of powerful AI systems, using voice as the most natural interface <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Driving Forces Behind Conversational Copilots

The development of conversational copilots is influenced by two major ongoing waves in AI:

1.  **Agent Capability Wave** <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>: This involves the creation of highly specialized AI agents that can perform complex tasks over extended periods <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. Advancements include better RAG (Retrieval Augmented Generation) systems, multi-step tool calling, and [[multiagent_orchestration_in_ai_copilot_systems | agent orchestration]] <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
2.  **Voice Technology Wave** <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>: This wave has made [[conversational_ai_applications_in_business | conversational agents]] highly accessible <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Key improvements include reduced time to first token and lower latency, with full duplex speech models on the horizon <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

The goal is to combine these waves to offer real-time assistance via agents in an ambient, conversational setting <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Demo Example: Foreign Language Call Assistance

A practical demonstration of a conversational copilot involves providing real-time assistance during a live foreign language call, especially when the user is not fluent <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. This system incorporates:
*   Caption scraping <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>
*   Smart debouncing <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>
*   Context management to ensure LM suggestions are relevant to the call <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>
*   An LM pipeline for suggestion and translation endpoints <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>

The overlay listens passively to natural dialogue and surfaces relevant help (e.g., language suggestions, phrase suggestions, definitions) under specific contexts, otherwise staying out of the way <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.

## Overlay Paradigm vs. Traditional AI Interaction

*   **Typical Voice AI Interaction**: A human speaks directly with an AI, which may access tools and information to respond <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   **Overlay Paradigm**: Two humans speak with each other, and an AI operates in the background to enhance and augment their dialogue <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

Overlays are distinct from meeting bots or notetakers, which function *after* the live interaction <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>, and also differ from voice avatars or full AI callers, as overlays aim to amplify the humans in the room rather than participate directly <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

## Challenges in Designing Conversational Copilots

### Design Challenges

Significant [[user_experience_design_with_ai | UX research]] is required for cognitive load, overlay design, and timing, bridging human-computer interaction with [[usercentric_ai_design_and_feedback_loops | AI UX research]] <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

### Engineering Challenges

Unlike standard voice AI systems where latency is paramount, overlays introduce unique timing considerations:
*   **Early help**: Becomes an interruption <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Late help**: Misses the opportunity for value and is useless <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   **Wrong context**: Leads to "spam" <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Derailing the conversation**: Makes the help unusable as it disregards conversational flow <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Summary**: The core challenges revolve around timing, relevance, attention, and latency <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

### The Four Horsemen of Overlay Engineering

1.  **Jitterbug Input**: Handling pauses in speech where speech-to-text momentarily stops, requiring effective debouncing <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.
2.  **Context Repair**: Ensuring the entire pipeline is optimized for sub-second speed limits when providing live assistance <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
3.  **Premature Interrupt/No Show**: Delivering help at the precise right moment, which necessitates high [[conversational_and_experiential_memory_in_ai_systems | conversational awareness]] <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
4.  **Glanceable Ghost**: Designing the overlay to be non-obstructive and flexible, minimizing the "attention tax" on the user <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

## Design Principles for Overlays

*   **Transparency and Control**: Users should be able to decide the level of overlay involvement <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   **Minimum Cognitive Load**: The system must not overload or derail the speakers' conversation, regardless of its intelligence <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
*   **Progressive Autonomy**: The system should allow users to moderate the amount of help received over time, supporting their learning process <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

## Areas of Excitement and Future Directions

The field of conversational copilots is exciting due to:
*   **Low Latency**: Latency is now within striking distance, with roundtrip calls to fast-provisioned LM providers achievable in 500-700 milliseconds, and very low time to first token <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
*   **Privacy by Design**: The increasing capability of smaller models makes on-device inference a possibility, allowing for private-by-default systems <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.
*   **Strong User Experience Ethos**: Injecting a UX approach that values and protects the native human conversation <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
*   **Voice as a Linkable Surface**: Speculating on how ambient agents in live human conversations could be linked and orchestrated <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

Areas for further research and development include:
*   **ASR Errors**: Mitigating the cascade of Automatic Speech Recognition (ASR) errors (e.g., misinterpreting "don't" as "do"), possibly by pairing with more conversational context <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.
*   **Prosody and Timing Complexity**: Addressing the loss of micro-intonation signals when converting speech to text, and understanding the quantity of information loss <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   **Security Surface**: Exploring new security risks posed by agents interacting in live conversations <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

Future directions include full duplex speech models that process raw audio directly without text conversion <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>, multimodal understanding (e.g., seeing live video for more helpful AI interaction) <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>, and speculative execution with caching <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.

The future of AI appears to be conversational, with the technology ready, but the interfaces still being defined <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.