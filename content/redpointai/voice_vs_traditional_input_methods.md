---
title: Voice vs Traditional Input Methods
videoId: RNebPdvPB7k
---

From: [[redpointai]] <br/> 

The evolution of Artificial Intelligence (AI) is fundamentally reshaping how humans interact with computers, moving beyond traditional input methods like keyboards and mice towards more natural, human-like interfaces such as voice and multimodal communication. This shift is driven by the increasing sophistication of AI models that can process and generate various forms of data, mimicking human senses and interaction patterns <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## The Shift to Natural Interfaces

The analogy often used to describe this evolution is that if a computer functions like a human brain, the interface should resemble how humans communicate with each other <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This means leveraging "human I/O" (Input/Output) where eyes are equivalent to cameras, ears to microphones, and mouths to speakers <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The traditional keyboard and mouse are increasingly being replaced by the microphone and camera <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

[[The Role of Live Kit in Voice AI Applications | LiveKit]], for instance, positions itself as the "nervous system" connecting human senses (input from cameras and microphones) to the AI "brain" (foundational models like OpenAI's GPT-4o) and transmitting the AI's "responses" back out through speakers <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

### How Voice AI (e.g., ChatGPT Voice) Works

The interaction with [[Speech recognition and AI | voice AI applications]] like ChatGPT Voice involves several steps:
1.  **Client-side Capture:** A [[The Role of Live Kit in Voice AI Applications | LiveKit]] SDK on the user's device (phone, desktop) accesses the microphone (and camera) to capture speech <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
2.  **Network Transmission:** The captured audio is sent over [[The Role of Live Kit in Voice AI Applications | LiveKit]]'s global Edge Network, a mesh network fabric of servers that ensures efficient transmission to a backend "agent" <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
3.  **Agent Processing:** The agent (e.g., an OpenAI-built agent using [[The Role of Live Kit in Voice AI Applications | LiveKit]]'s framework) receives the audio data <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
    *   **Traditional Voice Mode:** Audio is converted from speech to text, sent to the Large Language Model (LLM), and as tokens stream out, they are converted back into speech (text-to-speech) and sent back to the client device <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
    *   **Advanced Voice Mode (e.g., GPT-4o):** Audio is sent directly to the GPU machine via a real-time API (websocket connection) into GPT-4o. GPT-4o is trained with a joint embedding of text and speech tokens, allowing inference to be done directly on audio embeddings, and speech is generated directly by GPT-4o <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This allows for faster, more natural conversational turns.
4.  **Client-side Playback:** The [[The Role of Live Kit in Voice AI Applications | LiveKit]] SDK on the device receives the generated speech and plays it through the phone or computer's speaker <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

### Benefits of Voice Interaction

Voice AI offers unique advantages:
*   **Hands-free Operation:** Ideal for scenarios like driving or cooking where using hands for input is impractical or unsafe <a class="yt-timestamp" data-t="01:00:58">[01:00:58]</a> <a class="yt-timestamp" data-t="01:13:12">[01:13:12]</a>.
*   **Accessible Tutoring:** Provides an unjudgmental environment to ask any question, no matter how "dumb," leveraging the model's vast knowledge base <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.
*   **Immediate Information:** Quickly access information and learn about new topics, similar to having a personal tutor or expert <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.

## The Future of Interfaces

The future workplace and daily interactions are envisioned to be significantly transformed by AI, moving towards seamless, multimodal interfaces.

### AGI and Human-like Interaction
The concept of Artificial General Intelligence (AGI) implies AI as "tool builders building tool builders" – synthetic human beings <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. If computers are effectively human brains, interaction will naturally mirror human communication: through eyes (cameras), ears (microphones), and mouths (speakers) <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

### Creative Tools and Workflow Transformation
Creative tools are expected to become more voice-based, interactive, and multimodal <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. Users will act as the "orchestrator" or "Maestro," shaping outcomes while the AI handles the mechanical work <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. The debate between "co-pilots" (AI assisting) and "agents" (AI autonomously performing tasks) will likely result in a hybrid approach, mirroring how humans collaborate in the workplace <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>.

### Hybrid Modalities: Voice, Text, and Vision
While voice is poised for a dominant role, text-based communication will persist <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. Humans still text, read, and type daily <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. Computer vision will also be a critical part of the future, as humans are visual creatures <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. The future will involve a hybrid of voice, text, and computer vision, often presented within a familiar chat interface <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

For instance, ordering food at a new restaurant might involve voice commands for general preferences, but the AI might display a dynamically generated UI with menu options that users can tap, rather than reading out the entire menu <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

### The "Thin Client" Dream and Chat Interfaces
The concept of a "Thin Client" – where powerful devices aren't needed to render complex UIs – might be realized through a single, versatile chat interface <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. Chat is seen as the "native human interface" for communication when not speaking <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. This single UI could incorporate voice, text, and dynamically generated interfaces, making interactions with any application familiar and accessible <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>.

Current AI interfaces tend to be mode-based (e.g., voice in a car, text in a crowded space) <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>. The future will see a more fluid blending of these modalities, akin to human pair programming, where visual input, typing, and verbal communication are seamlessly mixed <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

## Current State and Challenges in Voice Adoption

### Emergent vs. Existing Use Cases
[[The Future of Voice Interfaces in AI | Voice AI]] is seeing emergent use cases from companies like OpenAI (GPT-4o), Gemini Live, Character AI, and Perplexity, which are pushing the boundaries of interaction and capabilities <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.
Alongside these, there are "low-hanging fruit" areas, particularly in telephony and telecommunications, where voice is already dominant and AI can optimize margins <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>. This includes [[The role and future of human translators in the AI era | customer support]] and tasks like insurance eligibility lookups, where billions of calls happen monthly <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>.

### [[Latency and System Integration Challenges in AIbased Voice Systems | Latency and System Integration]]
While chatbots have seen significant adoption due to being less [[Latency and System Integration Challenges in AIbased Voice Systems | latency]]-sensitive, voice applications in customer support have been slower to take off <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>. However, significant progress has been made in reducing [[Latency and System Integration Challenges in AIbased Voice Systems | latency]]:
*   In early 2023, conversational [[Latency and System Integration Challenges in AIbased Voice Systems | latency]] for AI models was around 4 seconds <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.
*   With GPT-4o and [[The Role of Live Kit in Voice AI Applications | LiveKit]]'s real-time API, [[Latency and System Integration Challenges in AIbased Voice Systems | latency]] has decreased tenfold to approximately 320 milliseconds on average, achieving human-level conversational speed (around 300 milliseconds) <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.
*   In some cases, AI models can respond *too* fast (e.g., 100 milliseconds), interrupting users, indicating that the threshold for optimal speed has been met or even exceeded <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>.

The primary blockers for widespread voice AI adoption are no longer [[Latency and System Integration Challenges in AIbased Voice Systems | latency]] but rather [[Latency and System Integration Challenges in AIbased Voice Systems | system integration]] challenges and the current imperfections of AI models <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>. AI models can still hallucinate and require human-in-the-loop oversight, meaning existing human contact centers cannot be entirely replaced <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>. Integrating AI with bespoke backend systems (e.g., Salesforce for ticket tracking) also presents a significant challenge <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>.

## AI's "Senses" Beyond Voice

To enable more comprehensive interaction, AI is being equipped with more "senses." [[The Role of Live Kit in Voice AI Applications | LiveKit]] has historically given AI the ability to see (via cameras), hear (via microphones), and speak (via speakers) <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. The next step is giving AI the ability to "touch" applications <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.

This "touch" capability involves running virtualized or headless Chrome instances in the cloud, allowing an AI agent to hook into these browser instances and perform actions like loading web pages, clicking buttons, and filling out forms using a Playwright interface <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>. If an agent gets stuck (e.g., encountering a password field), it can stream the browser as video to a human user, who can then interact directly with the streamed browser pixels to unblock or guide the agent <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>. This technology aligns with Anthropic's "computer use API," where AI is given the ability to interact with and manipulate digital applications <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.

## On-Device vs. Cloud Models

The future of AI inference will likely be a hybrid of on-device and cloud processing <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>.
*   **On-device models** are crucial for immediate, reflex-like actions, especially in robotics (e.g., a humanoid robot reacting to a car) <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>.
*   **Cloud models** will handle complex planning, reasoning, and access to the world's vast knowledge, similar to how humans "go to the cloud" to look up information or seek expert help <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>.

A parallel-path approach, where both local and cloud models perform inference simultaneously and the fastest, most accurate responder is chosen, represents an ideal scenario if resource constraints were not an issue <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>. Data from interactions will generally be sent to the cloud for legal reasons, updated training data, and error analysis, though privacy-sensitive use cases may drive purely local processing <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.

## Overhyped and Underhyped in AI

*   **Overhyped:** Transformers, a foundational architecture in modern AI <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>.
*   **Underhyped:** Spiking Neural Networks (SNNs), an analog neural network design that models the human brain more closely. SNNs are challenging to train but show promise for processing audio and video signals <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>. Additionally, the application of [[The Future of Voice Interfaces in AI | voice AI]] to video games, enabling natural interaction with non-player characters (NPCs) and dynamic, open-world storytelling, is considered underhyped <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

## Personal Insights

*   **Changing Views on AI Moats:** Initially, it was thought that AI applications would quickly develop defensible "moats" (unique advantages). However, the rapid evolution of underlying models means that sustained competitive advantage comes from deeply embedding with customers and building products extremely fast, rather than relying solely on unique data assets <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>.
*   **Speed of AI Penetration:** The penetration of AI into daily life has been slower than initially expected. While generative AI models like ChatGPT have a large user base, many people are aware of them but do not actively use them in their work or personal lives <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.
*   **Most Exciting AI Startup (besides LiveKit):** Tesla, particularly its self-driving technology. The experience of autonomous driving is described as "magical" and a "marvel of technology," akin to the initial experience of using ChatGPT <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.
*   **AI Application to Build:** An AI-powered video game with a novel way of interacting with NPCs, creating expansive worlds with dynamic, lifelike characters and infinite story permutations <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.