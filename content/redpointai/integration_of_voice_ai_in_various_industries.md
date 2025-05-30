---
title: Integration of voice AI in various industries
videoId: RNebPdvPB7k
---

From: [[redpointai]] <br/> 

The future of interacting with computers is envisioned to shift from traditional keyboards and mice to more natural human communication methods, primarily voice and camera interfaces <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This shift is driven by the development of human-like AI systems that will respond and act similarly to humans <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. The eyes will be cameras, ears microphones, and the mouth a speaker, forming a new form of human-computer interaction <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## LiveKit's Role as a "Nervous System" in AI Integration
LiveKit, founded by Russ D'Sa, serves as a "nervous system" for AI models like OpenAI's ChatGPT voice <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>. Initially, LiveKit's open-source project focused on connecting humans to other humans through video conferencing and live streaming <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. However, with the emergence of voice mode, their focus shifted to connecting human beings with machines <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. If foundational model companies like OpenAI and Anthropic are building the "brain" (AGI), LiveKit aims to build the "nervous system" to transport sensory information (from cameras and microphones) to the brain and deliver the brain's responses back out (through speakers) <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

### How LiveKit Works with ChatGPT Voice
LiveKit's process for voice AI interaction involves several steps <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>:
1.  **SDK on Device**: A LiveKit SDK on the user's device accesses the camera and microphone <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
2.  **Audio Transmission**: When the user speaks, the SDK captures the speech and sends it over LiveKit's global Edge Network <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
3.  **Agent Processing**: The audio reaches an "agent" (application server, e.g., built by OpenAI using LiveKit's framework) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
4.  **Traditional Voice Mode**: In older voice modes, audio is converted to text, sent to an LLM, and the LLM's text output is converted back to speech and sent to the client device <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
5.  **Advanced Voice (e.g., GPT-4o)**: For advanced voice, speech goes directly to the GPU machine via a real-time API (websocket connection) and is processed by models like GPT-4o, which are trained with joint embeddings of text and speech tokens <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. Speech is then generated directly by GPT-4o and sent back through LiveKit's network to the device <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Current and Emergent Use Cases of Voice AI

### Personal Learning and Tutoring
One common use case is using advanced voice AI like ChatGPT voice as a personal tutor <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Users can ask any question, from Frontier Tech topics like quantum theory and CRISPR to basic concepts like how lightning works <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This provides a non-judgmental environment to ask "dumb questions" and access the world's knowledge <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

### Creative Tools
[[potential_and_development_of_ai_in_music_and_other_industries | Creative tools]] are expected to become more voice-based, interactive, and multimodal <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. Users will act as "orchestrators" or "Maestros," shaping assets while the AI handles the mechanical work <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. The interface could resemble Iron Man's interaction with Jarvis, using natural voice commands to manipulate digital assets <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

### Telephony and Customer Support
A significant area for [[challenges_and_opportunities_in_ai_integration | AI integration]] is the telefony/telecom space, where existing processes occur at massive scale <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. Companies like Sierra and Parloa are disrupting this by integrating AI to reduce costs in customer support <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>. Billions of calls happen globally every month, making it a high-penetration use case for voice and AI <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>. Examples include automated insurance eligibility lookups where AI can call out to humans <a class="yt-timestamp" data-t="00:30:51">[00:30:51]</a>.

### Robotics
[[integration_of_ai_in_autonomous_vehicles | Humanoid robotics]] will heavily rely on a split between cloud and on-device AI models <a class="yt-timestamp" data-t="00:32:38">[00:32:38]</a>. While planning and reasoning might occur in the cloud, reflex actions and immediate movements must happen on-device for safety and responsiveness <a class="yt-timestamp" data-t="00:32:57">[00:32:57]</a>. For example, a robot walking needs on-device processing to react instantly to hazards like an approaching car <a class="yt-timestamp" data-t="00:33:51">[00:33:51]</a>.

### Autonomous Vehicles
Beyond robotics, [[integration_of_ai_in_autonomous_vehicles | self-driving cars]] like Tesla's are considered a "marvel of technology" <a class="yt-timestamp" data-t="00:42:19">[00:42:19]</a>. The experience of a car navigating complex environments autonomously highlights the visceral impact of integrated AI <a class="yt-timestamp" data-t="00:42:05">[00:42:05]</a>.

### Video Games
The future of video games is expected to feature expansive open worlds populated with dynamic, lifelike characters that users can interact with using natural human inputs, particularly voice <a class="yt-timestamp" data-t="00:43:47">[00:43:47]</a>. This could transform games into "Choose Your Own Adventure" experiences with infinite possibilities <a class="yt-timestamp" data-t="00:43:58">[00:43:58]</a>.

## Evolution of AI Interfaces and Challenges

### From Modes to Hybrid Modalities
Currently, AI interfaces often operate based on "modes" (e.g., voice mode in a car, text mode in a crowded space) <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>. However, the future will see more fluid blending of modalities, similar to human collaborative work <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. This means simultaneously using computer vision (looking at a screen), typing, and asking questions to an AI co-pilot, which might even take control of the keyboard to correct mistakes <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>.

### The "Thin Client" Dream
The concept of a "Thin Client" – where a powerful device isn't needed locally – aligns with the evolution of AI interfaces <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. Chat interfaces, which humans already use daily (texting, WhatsApp, Slack), could become the universal UI for all applications, integrating voice, on-the-fly generated UI, and text <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.

### AI Gaining "Senses"
LiveKit's development extends beyond hearing and speaking for AI. By enabling agents to control virtualized browser instances and stream them to users, AI is gaining the ability to "touch" applications, mimicking human interaction with touchscreens <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>. This allows AI to manipulate applications, fill out forms, and be unblocked by human input when stuck (e.g., for passwords or unclear choices) <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>.

### Latency and Systems Integration
While latency in conversational AI has drastically improved (from 4 seconds to ~320 milliseconds with GPT-4o and LiveKit) <a class="yt-timestamp" data-t="00:23:48">[00:23:48]</a>, enabling human-level conversational turnovers (around 300 milliseconds), the main hurdles for widespread adoption are systems integration <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>. AI models aren't perfect yet and still hallucinate, requiring human-in-the-loop oversight <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>. Integrating with bespoke or obscure backend systems (e.g., Salesforce, ticket trackers) presents a significant challenge <a class="yt-timestamp" data-t="00:25:40">[00:25:40]</a>.

### On-Device vs. Cloud Inference
The balance between on-device and cloud-based AI inference remains a key consideration <a class="yt-timestamp" data-t="00:32:09">[00:32:09]</a>.
*   **On-device**: Crucial for real-time, reflex actions, especially in robotics where immediate physical reactions are necessary <a class="yt-timestamp" data-t="00:33:51">[00:33:51]</a>. Also for privacy-sensitive use cases <a class="yt-timestamp" data-t="00:36:45">[00:36:45]</a>.
*   **Cloud**: Essential for accessing vast amounts of information (like a human using a phone to look up info) or for complex reasoning requiring extensive knowledge (e.g., troubleshooting a router) <a class="yt-timestamp" data-t="00:34:27">[00:34:27]</a>.
The ideal scenario, without resource constraints, would involve parallel processing by both local and cloud models, with the fastest real answer being delivered <a class="yt-timestamp" data-t="00:35:41">[00:35:41]</a>. Data for legal reasons or for updating training data will generally be sent to the cloud <a class="yt-timestamp" data-t="00:36:36">[00:36:36]</a>.

### Slowdown in AI Penetration
Despite rapid advancements, the penetration of AI, particularly contemporary forms like ChatGPT, into daily work and consumer habits has been slower than anticipated <a class="yt-timestamp" data-t="00:40:02">[00:40:02]</a>. Many people have heard of AI but do not actively use it <a class="yt-timestamp" data-t="00:40:26">[00:40:26]</a>.

## Underhyped AI Technology
Spiking Neural Networks (SNNs) are considered an "underhyped" or "under researched" area in AI <a class="yt-timestamp" data-t="00:37:33">[00:37:33]</a>. These analog neural networks are modeled more closely after the human brain's neuron interaction <a class="yt-timestamp" data-t="00:37:43">[00:37:43]</a>. While harder to train than Transformers, they hold significant promise for processing audio and video signals <a class="yt-timestamp" data-t="00:38:13">[00:38:13]</a>.