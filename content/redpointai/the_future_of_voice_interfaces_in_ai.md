---
title: The Future of Voice Interfaces in AI
videoId: RNebPdvPB7k
---

From: [[redpointai]] <br/> 

The future of human-computer interaction is moving beyond traditional keyboards and mice towards more natural, human-like interfaces, primarily driven by advancements in voice AI <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This shift envisions computers interacting with users through "eyes" (cameras), "ears" (microphones), and "mouths" (speakers), mirroring human communication <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Current State and Key Applications

Companies like OpenAI are at the forefront of this transformation, with products such as ChatGPT Voice demonstrating the potential of voice interfaces <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. [[The Role of Live Kit in Voice AI Applications | LiveKit]], for instance, powers applications like ChatGPT Voice, acting as the "nervous system" connecting human users with machines <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

Russ D'sa, CEO of [[The Role of Live Kit in Voice AI Applications | LiveKit]], personally uses ChatGPT Voice as a tutor, asking questions about frontier technology like quantum theory or basic science topics like how lightning works <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This provides a "judgment-free" environment to ask "dumb questions" and access the "entire world's knowledge" <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### How LiveKit Powers Voice AI

[[The Role of Live Kit in Voice AI Applications | LiveKit]] employs an SDK on the user's device to access the camera and microphone <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. When a user speaks, the speech is captured and sent over [[The Role of Live Kit in Voice AI Applications | LiveKit]]'s global Edge Network to a backend agent <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

For traditional voice mode:
1.  Audio from the user's device is converted to text <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
2.  This text is sent to a Large Language Model (LLM) <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
3.  As tokens stream from the LLM, they are converted back into speech <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
4.  The speech is sent back over [[The Role of Live Kit in Voice AI Applications | LiveKit]]'s network to the client device and played out <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

For advanced voice (like GPT-4o):
1.  Speech goes directly from the client device over the network to the agent <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
2.  The agent sends the audio directly via a real-time API (websocket) to a GPU machine <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
3.  The audio is directly processed by GPT-4o, which is trained with joint embeddings between text and speech <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
4.  Speech is generated directly by GPT-4o and returned through the network to the device <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

### Emergent and Existing Use Cases

Emergent use cases for voice AI include:
*   Voice interfaces for information lookup <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>.
*   Tutors or therapists <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
*   New capabilities like Anthropic's "computer use API" <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>.

Existing, large-scale applications where voice AI is driving margin optimization:
*   Telephony and telecom space <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.
*   Customer support, replacing IVR phone tree systems with AI <a class="yt-timestamp" data-t="00:20:32">[00:20:32]</a>.
*   Automated tasks like insurance eligibility lookups, where AI agents can both receive and make calls to humans <a class="yt-timestamp" data-t="00:30:18">[00:30:18]</a>.

## The Vision: AGI and Human-like Interaction

If companies are building [[future_of_artificial_general_intelligence_agi | AGI]] (Artificial General Intelligence) – "tool builders building tool builders" <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a> – the primary interface will shift from keyboards and mice to microphones and cameras <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This is because a computer resembling a human brain would naturally interact like a human <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. [[The Role of Live Kit in Voice AI Applications | LiveKit]] aims to be the "nervous system" that transports sensory information (from cameras/microphones) to the AI "brain" and delivers the brain's output back out <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

### The Office of the Future

The nature of work will change drastically <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. Instead of traditional offices, future interactions might resemble "Jarvis" from Iron Man, with voice-controlled interfaces permeating everything <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. Creative tools will become more voice-based, interactive, and multimodal, with AI serving as the orchestrator or "Maestro" for tasks, reducing the mechanical work for humans <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

The future will likely see a hybrid of "co-pilots" and "agents," mimicking human collaboration in the workplace, where some tasks are owned autonomously by agents, while others involve pairing or collaborative meetings <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

## Challenges and Hybrid Modalities

While voice is powerful, it won't entirely replace other modalities <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. Text will retain its place for certain scenarios (e.g., privacy, personal preference for reading, messaging apps) <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. Computer vision will also be crucial as humans are visual creatures <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.

### When Voice Makes Sense

Voice is a natural modality for:
*   Hands-free interfaces (driving, cooking) <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
*   Interactions with devices that are far away (like Siri or Alexa) <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
*   Situations where reading an entire menu, for example, would be a poor user experience <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

### The "Thin Client Dream" and Fluid Modalities

The idea of a "Thin Client" – a less powerful device relying on cloud processing – could manifest in a universal chat interface <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. Just as humans communicate frequently via chat (texting, Telegram, WhatsApp), a chat interface could serve as a single UI for all applications, incorporating voice, on-the-fly generated UI, and text <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.

Future AI interfaces will treat modalities more fluidly <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. This is akin to human pair programming, where multiple modalities are mixed on the fly: looking at a screen (computer vision), typing (text), and asking questions or giving instructions verbally (voice) <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>. This blending of experiences, especially with [[future_trends_in_ai_and_multimodal_models | computer vision]] integration, is expected to become prevalent <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.

### Technical Hurdles in Voice AI Deployment

[[Latency and System Integration Challenges in AIbased Voice Systems | Latency]] in voice AI has drastically improved. From approximately 4 seconds in early 2023, conversational turn-around time with GPT-4o and [[The Role of Live Kit in Voice AI Applications | LiveKit]] is now around 320 milliseconds on average, close to human-level conversational speed (300ms) <a class="yt-timestamp" data-t="00:23:43">[00:23:43]</a>. In some cases, inference can be so fast (e.g., Cerebras at ~100ms) that models respond too quickly, interrupting users <a class="yt-timestamp" data-t="00:24:26">[00:24:26]</a>.

However, the main challenge isn't [[Latency and System Integration Challenges in AIbased Voice Systems | latency]] but rather [[Latency and System Integration Challenges in AIbased Voice Systems | systems integration]] <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>. AI models are not yet perfect; they can hallucinate, requiring human-in-the-loop oversight <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>. Integrating AI into existing, often bespoke, backend systems (like updating records in Salesforce or tracking tickets) presents a significant hurdle <a class="yt-timestamp" data-t="00:25:28">[00:25:28]</a>.

### Giving AI the Sense of "Touch"

[[The Role of Live Kit in Voice AI Applications | LiveKit]] is working on giving AI the ability to "touch" applications, going beyond seeing, hearing, and speaking <a class="yt-timestamp" data-t="00:28:40">[00:28:40]</a>. This involves allowing AI agents to interact with virtualized browser instances in the cloud, using a Playwright interface to load web pages, click buttons, and fill forms <a class="yt-timestamp" data-t="00:26:49">[00:26:49]</a>. If an agent gets stuck (e.g., needing a password or user choice), it can stream the browser video to a human user, who can then interact by clicking on "video pixels" to unblock the agent <a class="yt-timestamp" data-t="00:27:27">[00:27:27]</a>. This capability aligns with Anthropic's "computer use API" <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>.

## Architecture: On-Device vs. Cloud Inference

The split between on-device and cloud model inference is crucial. In [[the_future_of_ai_in_robotics_and_its_impact | humanoid robotics]], for example, planning and reasoning might occur in the cloud, while "reflex action" and movement (kinematics) run on-device to ensure immediate responses to physical world events <a class="yt-timestamp" data-t="00:32:53">[00:32:53]</a>.

Drawing an analogy to humans, who don't possess all world information in their heads, AI models will likely always have some inference occurring in the cloud for knowledge lookup or complex problem-solving <a class="yt-timestamp" data-t="00:34:11">[00:34:11]</a>. Ideally, both local and cloud models could run in parallel, with the fastest accurate responder being used <a class="yt-timestamp" data-t="00:35:41">[00:35:41]</a>.

Privacy-sensitive use cases may push for purely local, on-device processing <a class="yt-timestamp" data-t="00:36:45">[00:36:45]</a>. However, even with initiatives like Apple Intelligence, data often still goes to a highly secure cloud for advanced processing <a class="yt-timestamp" data-t="00:36:59">[00:36:59]</a>. Data will generally be sent to the cloud for legal reasons, generating updated training data, and addressing erroneous examples <a class="yt-timestamp" data-t="00:36:36">[00:36:36]</a>.

## Emerging Trends and Predictions

*   **Multimodal Models**: The advent of fully multimodal models like GPT-4o, trained on speech and text, capable of taking any combination of modalities as input and outputting any combination, is a significant development <a class="yt-timestamp" data-t="00:31:18">[00:31:18]</a>.
*   **Underhyped Architectures**: While Transformers are currently overhyped, "spiking neural networks" are underhyped and under-researched <a class="yt-timestamp" data-t="00:37:20">[00:37:20]</a>. These analog neural networks are modeled more closely after the human brain and are potentially perfect for audio and video signal processing, though harder to train <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>.
*   **AI Penetration Speed**: The penetration of AI into everyday usage has been slower than anticipated, despite rapid growth, with many people still not using contemporary AI forms like ChatGPT <a class="yt-timestamp" data-t="00:40:02">[00:40:02]</a>.
*   **[[Future of AI in VR and personal agents | AI in Video Games]]**: Voice AI applied to video games is underhyped <a class="yt-timestamp" data-t="00:44:21">[00:44:21]</a>. The [[Future of AI in VR and personal agents | future of video games]] will feature open worlds filled with dynamic, lifelike characters that players can interact with using natural human inputs, leading to infinite possibilities and changing storylines <a class="yt-timestamp" data-t="00:43:42">[00:43:42]</a>.
*   **Tesla's Self-Driving**: Tesla's self-driving technology is seen as a "marvel of technology" and a "visceral experience," demonstrating science fiction-like capabilities that don't receive enough recognition <a class="yt-timestamp" data-t="00:41:52">[00:41:52]</a>.