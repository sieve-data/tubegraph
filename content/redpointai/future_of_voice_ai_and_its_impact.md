---
title: Future of voice AI and its impact
videoId: RNebPdvPB7k
---

From: [[redpointai]] <br/> 

The way humans interact with computers is undergoing a profound transformation, moving away from traditional keyboards and mice towards more natural, human-like interfaces. This shift is largely driven by advancements in voice AI, which aims to enable seamless communication between humans and machines <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## LiveKit: The Nervous System of AI
LiveKit, founded by Russ D'Sa, plays a crucial role in this evolution by powering applications like ChatGPT Voice <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. D'Sa describes LiveKit as the "nervous system" for AI, where foundational models (like those from OpenAI, Anthropic, or Gemini) serve as the "brain." LiveKit's technology enables the transfer of information from sensory inputs (cameras as eyes, microphones as ears, speakers as mouths) to the AI brain, and then transmits the AI's responses back out to the user <a class="yt-timestamp" data-t="08:07:07">[08:07:07]</a>.

### How LiveKit Powers AI Interactions
LiveKit utilizes an SDK on the user's device to access cameras and microphones. When a user speaks, the speech is captured and sent over LiveKit's global Edge Network to a backend "agent" (an application server built with LiveKit's framework, e.g., OpenAI's agent) <a class="yt-timestamp" data-t="03:00:03">[03:00:03]</a>.

There are two primary modes for processing this audio:
*   **Traditional Voice Mode**: Audio is converted from speech-to-text, sent to a Large Language Model (LLM), and then the LLM's text output is converted back to speech and sent to the client device <a class="yt-timestamp" data-t="04:14:15">[04:14:15]</a>.
*   **Advanced Voice Mode (e.g., GPT-4o)**: Audio is sent directly to the GPU machine and processed by models like GPT-4o, which are trained with a joint embedding of text and speech tokens. The inference is done directly on audio embeddings, and speech is generated and returned to the device <a class="yt-timestamp" data-t="04:48:09">[04:48:09]</a>.

## Personal Use Cases and Learning
Russ D'Sa personally uses [[the_future_of_ai_in_human_communication | ChatGPT Voice]] as a portable tutor during commutes. He asks it to teach him about frontier tech topics like Quantum Theory or CRISPR, or even basic concepts like how lightning works <a class="yt-timestamp" data-t="01:19:10">[01:19:10]</a>. This provides a judgment-free learning environment where one can ask any "dumb question" and access the world's knowledge <a class="yt-timestamp" data-t="02:11:11">[02:11:11]</a>.

## The Future of Interfaces and Work
If computers become effectively like human brains, the primary way of interfacing with them will likely be through natural human communication—using eyes (cameras), ears (microphones), and mouths (speakers) <a class="yt-timestamp" data-t="07:50:07">[07:50:07]</a>.

### Shifting Work Environments
The nature of work is expected to change drastically, potentially moving away from traditional keyboard and mouse setups <a class="yt-timestamp" data-t="08:54:19">[08:54:19]</a>.
*   **Jarvis-like Interfaces**: The vision includes interfaces similar to Tony Stark's Jarvis, where interactions are highly multimodal and conversational <a class="yt-timestamp" data-t="09:00:52">[09:00:52]</a>.
*   **Creative Tools**: Creative tools are anticipated to become more voice-based, interactive, and multimodal, allowing users to orchestrate or "maestro" transformations without doing all the mechanical work <a class="yt-timestamp" data-t="09:17:59">[09:17:59]</a>.

### Co-pilots vs. Agents
The future will likely see a hybrid model of co-pilots and agents, mirroring how humans work with other humans. Some AI will act autonomously (agents), while others will pair with users in collaborative roles (co-pilots), similar to human colleagues <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>. The key difference is that much of this collaboration will be with AI rather than solely with humans <a class="yt-timestamp" data-t="11:03:09">[11:03:09]</a>.

### Modality Blending
While voice will be prominent, text, computer vision, and eventually video generation will still have their place <a class="yt-timestamp" data-t="11:48:19">[11:48:19]</a>.
*   **Hybrid Interactions**: In certain contexts, a hybrid approach of voice plus text or dynamically generated UI elements will be optimal. For instance, when ordering from a new restaurant, reading a menu is more efficient than having it recited <a class="yt-timestamp" data-t="12:40:48">[12:40:48]</a>.
*   **Hands-Free Contexts**: Voice is a natural modality for hands-free situations like driving or cooking, or for smart devices like Siri or Alexa <a class="yt-timestamp" data-t="13:10:04">[13:10:04]</a>.
*   **Chat Interface as "Thin Client Dream"**: The familiar chat interface (texting, Telegram, WhatsApp, Slack) could evolve into a universal UI for nearly any application, incorporating voice, on-the-fly generated UI, and text into a single, familiar stream of messages <a class="yt-timestamp" data-t="15:46:00">[15:46:00]</a>.
*   **Fluid Modalities**: Future UI explorations will treat modalities more fluidly. An example is pair programming, where multiple modalities (computer vision from looking at the screen, typing, asking questions, voice responses) are mixed dynamically <a class="yt-timestamp" data-t="17:28:07">[17:28:07]</a>.

## [[integration_of_voice_ai_in_various_industries | Integration of Voice AI in Various Industries]]

### Emergent Use Cases
New applications of voice AI are pushing the envelope of interaction and capability. These include:
*   **AI as Tutor/Therapist**: Systems like OpenAI, Gemini Live, Character AI, and Perplexity offer voice interfaces for information lookup, asking questions, and even therapeutic support <a class="yt-timestamp" data-t="19:04:36">[19:04:36]</a>.
*   **Computer Use API**: Companies like Anthropic are developing APIs that allow AI to interact with and control computers, indicating significant future potential <a class="yt-timestamp" data-t="19:37:37">[19:37:37]</a>.

### Low-Hanging Fruit: Telephony and Telecom
A massive, immediate area for voice AI penetration is the telephony and telecom space, where existing processes can be optimized for cost reduction <a class="yt-timestamp" data-t="19:55:54">[19:55:54]</a>.
*   **Customer Support**: AI is rapidly disrupting customer support, from IVR (Interactive Voice Response) phone trees to full AI agents. Companies like Sierra and Parloa are integrating AI to handle billions of calls monthly, automating tasks like insurance eligibility lookups <a class="yt-timestamp" data-t="20:39:56">[20:39:56]</a>.
*   **Outbound AI Calls**: AI agents can also initiate calls to humans, reversing the traditional direction <a class="yt-timestamp" data-t="30:51:19">[30:51:19]</a>.

## [[challenges_and_advancements_in_ai_technology | Challenges and Advancements in AI Technology]]

### Latency Improvements
Latency in conversational AI has significantly improved. In early 2023, conversational latency was around 4 seconds. With advancements like GPT-4o and real-time APIs, it has decreased tenfold to an average of 320 milliseconds, approaching human-level conversational turnover speed (around 300 milliseconds) <a class="yt-timestamp" data-t="23:43:08">[23:43:08]</a>. In some cases, AI can even respond too quickly, leading to models interrupting users <a class="yt-timestamp" data-t="24:42:07">[24:42:07]</a>.

### Imperfection and Systems Integration
Despite speed improvements, AI models are not perfect; they can still hallucinate and make mistakes <a class="yt-timestamp" data-t="22:52:43">[22:52:43]</a>. This necessitates a "human in the loop" to correct agents or take over tasks <a class="yt-timestamp" data-t="23:11:15">[23:11:15]</a>. A larger challenge lies in [[integration_of_voice_ai_in_various_industries | systems integration]], where AI agents need to access and update backend systems like Salesforce or bespoke software, which can be complex and slow <a class="yt-timestamp" data-t="25:06:05">[25:06:05]</a>.

### AI's "Sense of Touch"
LiveKit is developing technology to give AI the "ability to touch" applications. This involves running virtualized or headless Chrome instances in the cloud, allowing AI agents to interact with browsers using a Playwright interface (e.g., loading web pages, clicking buttons, filling forms) <a class="yt-timestamp" data-t="26:47:33">[26:47:33]</a>. When an agent gets stuck (e.g., needing a password or clarification), it can stream the browser as video to a human user, who can then interact directly with the streamed interface to unblock or guide the AI <a class="yt-timestamp" data-t="27:27:54">[27:27:54]</a>.

## On-Device vs. Cloud Models
The future of AI processing will likely involve a hybrid approach, with some models running on devices and others in the cloud <a class="yt-timestamp" data-t="32:31:00">[32:31:00]</a>.
*   **Humanoid Robotics**: For [[future_of_ai_in_industrial_applications_and_potential_impact | humanoid robots]], reflex actions and physical movements (kinematics) will likely be handled on-device due to real-time safety requirements, while higher-level planning and reasoning might occur in the cloud <a class="yt-timestamp" data-t="32:51:30">[32:51:30]</a>.
*   **Human Analogy**: Similar to humans not storing all world knowledge in their brains but accessing it from external sources (like a phone or calling support), AI will rely on cloud inference for vast knowledge and complex problem-solving <a class="yt-timestamp" data-t="34:11:06">[34:11:06]</a>.
*   **Optimal Performance**: Ideally, both local and cloud models would run in parallel, with the fastest and most accurate responder providing the answer <a class="yt-timestamp" data-t="35:41:40">[35:41:40]</a>.
*   **Privacy**: While much data will likely be sent to the cloud for training and legal reasons, privacy-sensitive use cases may drive the development of purely local, on-device AI <a class="yt-timestamp" data-t="36:36:00">[36:36:00]</a>. Even new technologies like Apple Intelligence still involve sending data to secure cloud environments <a class="yt-timestamp" data-t="36:59:30">[36:59:30]</a>.

## Overhyped, Underhyped, and Shifting Perspectives in AI

### Overhyped
*   **Transformers**: While powerful, the speaker considers them overhyped <a class="yt-timestamp" data-t="37:20:00">[37:20:00]</a>.

### Underhyped
*   **Spiking Neural Networks (SNNs)**: These analog neural networks are modeled more closely after the human brain and how neurons interact, showing promise for audio and video signal processing, though they are harder to train than Transformers <a class="yt-timestamp" data-t="37:33:00">[37:33:00]</a>.
*   **[[future_possibilities_and_visions_for_ai_and_music_collaboration | Video Games with Voice AI]]**: The future of video games will be "incredible" with dynamic, lifelike characters and "infinite" story possibilities through natural human inputs like voice, leading to "Choose Your Own Adventure" experiences <a class="yt-timestamp" data-t="43:40:53">[43:40:53]</a>.

### Changing Mindsets
*   **AI Moats**: Initial thoughts on building applications with genuine "moats" (defensible advantages) in AI have shifted. The underlying models change too rapidly, making it difficult to establish lasting moats. Success now relies on being deeply embedded with customers and building products very quickly <a class="yt-timestamp" data-t="38:31:00">[38:31:00]</a>.
*   **Speed of Penetration**: The speaker initially believed AI would penetrate more rapidly and deeply into daily use, but observes that many people, while aware of ChatGPT, still do not use it or other contemporary forms of AI in their daily work <a class="yt-timestamp" data-t="40:02:00">[40:02:00]</a>.

## Exciting AI Startups and Future Ideas
*   **Tesla**: The speaker is most excited about Tesla due to the "magical" experience of its self-driving capabilities, likening it to a "Marvel of Technology." The integration of the car with AI (e.g., voice control via API) and the potential of the Tesla Bot represent "sci-fi dreams" <a class="yt-timestamp" data-t="41:06:33">[41:06:33]</a>. The self-driving car offers a "visceral experience" that is highly impactful upon first use <a class="yt-timestamp" data-t="41:55:00">[41:55:00]</a>.
*   **Future AI Application Idea**: If starting a new AI application, the speaker would build a video game with a novel way of interacting with non-player characters (NPCs) <a class="yt-timestamp" data-t="43:17:15">[43:17:15]</a>. This game would feature expansive, open worlds filled with dynamic, lifelike characters that users could interact with using natural human inputs, particularly voice <a class="yt-timestamp" data-t="43:42:00">[43:42:00]</a>.

For more information on LiveKit and its open-source projects, visit their GitHub at github.com/livekit, their website at livekit.io, or their X (formerly Twitter) page at x.com/livekit <a class="yt-timestamp" data-t="44:45:34">[44:45:34]</a>.