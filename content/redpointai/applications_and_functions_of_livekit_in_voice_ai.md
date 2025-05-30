---
title: Applications and functions of LiveKit in voice AI
videoId: RNebPdvPB7k
---

From: [[redpointai]] <br/> 

LiveKit is a foundational technology that powers applications like ChatGPT Voice, aiming to revolutionize human-computer interaction by replacing traditional keyboards and mice with microphones and cameras <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Founded and led by CEO Russ D'sa, LiveKit provides the infrastructure for seamless, real-time voice and multimodal AI interactions <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## LiveKit as the "Nervous System" of AI
Russ D'sa describes LiveKit as the "nervous system" for AI, drawing an analogy to human biology <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. If foundational model companies like OpenAI, Anthropic, and Gemini are building the "brain" (AGI), LiveKit is building the "nervous system" that transports information to and from that brain <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>, enabling [[voicedriven_humancomputer_interaction|voice-driven human-computer interaction]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

This means taking information from "senses" like cameras (eyes) and microphones (ears), transporting it to the AI brain, and then returning the brain's output via speakers (mouth) <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. The core idea is that if a computer acts like a human brain, communication should be similar to how humans communicate with each other <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## How LiveKit Powers ChatGPT Voice
LiveKit's architecture enables seamless voice interactions with large language models (LLMs) like ChatGPT <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>:

1.  **LiveKit SDK on Device**: An SDK sits on the user's device, accessing the camera and microphone <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
2.  **Speech Capture and Transmission**: When a user speaks, the SDK captures the speech and sends it over LiveKit's global Edge Network, a mesh network of servers around the world <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
3.  **Agent Framework**: The audio data is transmitted to an "agent" on the backend, which acts as an application server <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. OpenAI, for example, builds an agent using LiveKit's framework <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
4.  **Processing (Traditional vs. Advanced Voice)**:
    *   **Traditional Voice Mode**: The audio is converted from speech to text, which is then sent to the LLM <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
    *   **Advanced Voice (GPT-4o)**: The audio is sent directly to the GPU machine via a real-time API (websocket connection) <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. GPT-4o, being trained on joint text and speech embeddings, performs inference directly on the audio embeddings <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
5.  **Response Generation and Delivery**:
    *   For traditional mode, tokens stream out of the LLM and are converted back into speech <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
    *   For advanced voice, speech is generated directly by GPT-4o <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
    Both are then sent back over LiveKit's network to the client device and played out <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

Latency for voice AI has drastically improved, with GPT-4o and LiveKit achieving an average of 320 milliseconds, nearing human-level conversational turnover speeds <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>.

## Applications and Use Cases

### Enhanced Human-Computer Interaction
LiveKit facilitates a shift towards more natural human-computer interaction <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Russ D'sa uses ChatGPT Voice as a personal tutor while driving, asking "dumb questions" about various topics like quantum theory, CRISPR, or how lightning works, without judgment <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This highlights the potential for AI to act as an accessible, non-judgmental learning resource <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### Creative Tools and Agents
In the [[future_of_voice_ai_and_its_impact|future of voice AI]], creative tools are expected to become more voice-based and multimodal <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. Users will act as "orchestrators" or "maestros," shaping creative assets while the AI performs the mechanical work <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. This envisions scenarios similar to Tony Stark interacting with Jarvis <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

The future workplace will likely involve a hybrid of co-pilots and autonomous agents <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. These AI counterparts will perform tasks autonomously or engage in collaborative "pairing" sessions, similar to human teamwork <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

### Enabling AI to "Touch" Applications
LiveKit is expanding AI capabilities beyond just seeing, hearing, and speaking, by giving AI the "ability to touch" applications <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>. This is achieved through a beta API that allows agents to control virtualized browser instances (headless Chrome) in the cloud via a Playwright interface <a class="yt-timestamp" data-t="00:26:49">[00:26:49]</a>. Agents can:
*   Load web pages <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>
*   Click on buttons <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>
*   Fill out forms <a class="yt-timestamp" data-t="00:27:16">[00:27:16]</a>

Crucially, if an agent gets "stuck" (e.g., encountering a password field or needing a decision), it can stream the browser as video to a human user <a class="yt-timestamp" data-t="00:27:27">[00:27:27]</a>. The human can then interact directly with the streamed browser (clicking on "video pixels") to unblock or "nudge" the agent, with inputs replayed back to the cloud, creating a shared, interactive session <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>. This aligns with Anthropic's computer use API, showing a direction for [[the_future_potential_and_development_of_ai_assistance_apis|AI assistance APIs]] to interact with and manipulate digital environments <a class="yt-timestamp" data-t="00:26:06">[00:26:06]</a>.

### [[integration_of_voice_ai_in_various_industries|Integration of Voice AI in Various Industries]]
There are two main categories of voice AI use cases <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>:
1.  **Emergent Use Cases**: These involve pushing the envelope with new capabilities and interactions, such as AI as a tutor or therapist <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>. Companies like Character AI and Perplexity are building voice interfaces for their systems <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.
2.  **Existing, High-Scale Applications**: These focus on margin optimization by integrating AI into established voice-native systems like telephony or telecom <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>. Examples include:
    *   **Customer Support**: AI is rapidly entering the telephone-dominated customer support space, reducing costs <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>. Challenges remain with AI model perfection and the need for human-in-the-loop systems <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>.
    *   **Insurance Eligibility Lookups**: Millions of calls happen daily for hospitals to verify insurance coverage, a process ripe for AI automation <a class="yt-timestamp" data-t="00:30:20">[00:30:20]</a>. This includes AI calling out to humans <a class="yt-timestamp" data-t="00:30:51">[00:30:51]</a>.

### Future of AI in Human Communication
The [[future of AI in human communication|future of AI in human communication]] will be multimodal, combining text, voice, and computer vision <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. While voice is ideal for hands-free interfaces (driving, cooking), text will always have its place, particularly when consuming information like menus <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

The "chat interface" is seen as a universal "Thin Client" for AI, combining voice, on-the-fly generated UI, and text within a familiar messaging format <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>. Ultimately, the AI interface will become more fluid, blending modalities seamlessly, similar to how humans naturally mix speech, typing, and visual cues during collaborative work <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.

### On-Device vs. Cloud Inference
The balance between on-device and cloud-based AI models is an evolving area <a class="yt-timestamp" data-t="00:32:09">[00:32:09]</a>.
*   **On-Device Models**: Crucial for real-time "reflex actions" in robotics (e.g., a humanoid robot avoiding a car) where immediate response is critical <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>.
*   **Cloud Models**: Necessary for complex planning, reasoning, and accessing the "world's information" that no single device can hold (e.g., understanding the latest router specifications) <a class="yt-timestamp" data-t="00:34:29">[00:34:29]</a>.

The ideal scenario for the [[future of voice AI and its impact|future of voice AI]] might involve parallel processing by both local and cloud models, with the fastest and most accurate response winning <a class="yt-timestamp" data-t="00:35:41">[00:35:41]</a>. Data will generally be sent to the cloud for legal reasons, updated training data, and error correction, though purely local, privacy-sensitive use cases will also exist <a class="yt-timestamp" data-t="00:36:36">[00:36:36]</a>.

### Future of Gaming
Voice AI applied to video games is seen as an "underhyped" area <a class="yt-timestamp" data-t="00:44:21">[00:44:21]</a>. The [[future_of_voice_ai_and_its_impact|future of video games]] will feature expansive open worlds filled with dynamic, lifelike characters that players can interact with using natural human inputs, creating infinitely permutations of "Choose Your Own Adventure" stories <a class="yt-timestamp" data-t="00:43:42">[00:43:42]</a>.

## Learning More
For more information about LiveKit and its open-source projects, visit their GitHub <a class="yt-timestamp" data-t="00:44:46">[00:44:46]</a> ([github.com/livekit](https://github.com/livekit)), their website ([livekit.io](https://livekit.io)), or their X (formerly Twitter) page ([x.com/livekit](https://x.com/livekit)) <a class="yt-timestamp" data-t="00:45:02">[00:45:02]</a>.