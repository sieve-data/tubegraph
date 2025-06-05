---
title: Building a reliable conversation system for voice agents
videoId: 2p2ErKRELHM
---

From: [[aidotengineer]] <br/> 

Nick, an engineer at Superdial, highlights the exciting yet challenging landscape of [[Voice and multimodal AI agents | voice AI]] in 2025. While new smart, fast, and affordable Large Language Models (LLMs) support complex conversational use cases, and low-latency, realistic text-to-speech models are available, there are still significant hurdles to overcome to build reliable [[Voice and multimodal AI agents | voice AI agents]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Key challenges include dealing with audio hallucinations from generative text-to-speech models, managing pronunciation and spelling, and the current immaturity of speech-to-speech models for production applications due to their unreliable output <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Superdial's Approach: Agents as a Service

Superdial operates on an "Agents as a Service" model, focusing on the "Last Mile Problem" of ensuring reliability once an MVP (Minimum Viable Product) [[Voice and multimodal AI agents | voice agent]] is built <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The company specializes in automating phone calls for mid to large-sized healthcare administration businesses, particularly the often-annoying calls to insurance companies <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### Business Model and Agentic Contract
Superdial's platform allows customers to design conversation scripts and send calls via CSV, API, or EHR software integrations <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. The core of their "agentic contract" with customers is payment for results: customers specify who to call and what questions to ask, and Superdial provides the answers in a structured format <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

### The Internal Agentic Loop
Internally, Superdial employs an agentic loop to ensure call completion and learning <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>:
1.  **Call Attempts**: The system waits for offices and call centers to open before attempting calls with the [[Voice and multimodal AI agents | voice bot]] <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
2.  **Human Fallback**: If the [[Voice and multimodal AI agents | voice bot]] cannot complete the call after a certain number of attempts, it is seamlessly handed off to a human fallback team <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. This ensures the call gets made regardless of whether a human or bot completes it, providing reliable answers to customers <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
3.  **Continuous Learning**: The system learns from every call by updating office hours for specific phone numbers and refining phone tree traversal strategies to improve future call efficiency <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Random call audits are also conducted to ensure system integrity, especially given the sensitive nature of healthcare phone calls <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

Superdial's system has saved over 100,000 hours of human phone and calling time, with projections to save millions more <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. This was achieved with a lean team of four engineers handling the full stack, EHR integrations, and bot development <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

## The Role of the [[Voice AI engineering challenges and solutions | Voice AI Engineer]]

The success of Superdial is attributed to embracing the role of the [[Voice AI engineering challenges and solutions | voice AI engineer]] <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

### Unique Constraints
[[Voice AI engineering challenges and solutions | Voice AI engineers]] must deal with:
*   **Multimodal data**: Including MP3s, audio bites, and transcripts <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   **Real-time latency**: This becomes a critical factor for application performance <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Product constraint**: The application's core function is a voice conversation, requiring high expectations for natural interaction <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

### Guiding Principles
Superdial's internal sayings for grappling with these [[Challenges in building reliable AI agents | challenges in building reliable AI agents]] are:
*   "Say the right thing at the right time" <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   "Build this plane while we fly it" <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

The most unique aspect of a [[Voice and multimodal AI agents | voice bot]] is its conversational content and design, along with vertical integrations that make the agent's work valuable, rather than just its voice or interruption handling <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

### Ethical Considerations
Given the lack of AI regulation in the US, the onus is on AI engineers and leaders to consider potential biases in [[Voice and multimodal AI agents | voice AI apps]] against certain accents or dialects, and the "spooky" effect of realistic voices saying strange things <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. Developing AI should be accessible and collaborative, ensuring that the work AI does is for everyone. This requires choosing tooling and infrastructure that allows a diverse set of stakeholders to be involved from the start <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

## Addressing the [[Challenges in building reliable AI agents | Last Mile Problems in Voice AI]]

While it's easy to build an MVP for voice AI applications, scaling them faces immediate challenges, many of which are not new to voice UI, a field with 20 years of conversation design experience <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

### Conversation Design Paradigms
A significant shift in voice UI development is from **prescriptive** to **descriptive** development <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. Instead of mapping every possible conversational direction, developers describe what they want the bot to do and hope it happens <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

*   **Open-ended vs. Constrained Questions**: For existing conversations like healthcare calls, Superdial found it's often better to go general and hope the call center representative provides ample information, then adapt to whatever they say, rather than trying to prevent "wrong" responses <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Conversation Designers**: Hiring conversation designers is recommended as they are experts in this field <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
*   **Table Reads**: A practical tip for [[Voice AI engineering challenges and solutions | voice AI engineers]] is to perform "table reads," where one person pretends to be the bot and another a user, reading out a script. This immediately reveals gaps and awkwardness in the conversation <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.

### Orchestration Frameworks
Superdial found its stride by using **PipeCat** for [[Voice AI engineering challenges and solutions | voice AI orchestration]] <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. PipeCat is an open-source framework, easy to extend, and allows for self-hosting and scaling, which is crucial for long phone calls (up to 1.5 hours) <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

### LLM Integration and Tooling
For LLM work, Superdial made specific tooling choices:
*   **Owning OpenAI Endpoint**: This provides a better interface with new [[Voice and multimodal AI agents | voice AI tools]] and allows routing to different models for latency-sensitive responses <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   **TensorZero**: All generative responses are routed through TensorZero, an open-source tool that provides structured and typed LLM endpoints for production experimentation <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
*   **Logging and Observability**: Superdial self-hosts LaneFuse for logging and observability <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>. Self-hosting is also preferred for HIPAA compliance, given the rapid growth of the space <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. This setup facilitates anomaly detection, evaluations, and dataset management <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.

### Text-to-Speech Customization
A significant challenge is ensuring the Text-to-Speech (TTS) system accurately pronounces specific information, like names or long character strings (e.g., member IDs) <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   **LLM Output vs. TTS Input**: What the LLM outputs is not always what should be fed directly into the TTS engine, and neither may match the final recording <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.
*   **Pronunciation and Spelling**: Tools like Rhyme allow explicit spelling out of pronunciations (e.g., using SSML syntax) and managing pauses and breaks for long words <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>. Audio recordings are reviewed in addition to transcripts to ensure correct output <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.

### Operational Best Practices (Mini Last Mile Problems)
Several practical "mini Last Mile" problems arise when deploying [[Voice and multimodal AI agents | voice AI agents]] <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>:

*   **Persona**: Choose a bot persona carefully. A previous bot name, "Billy," caused confusion over the phone due to similar-sounding pronunciations <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
*   **Leveraging Existing Tools**: Don't build from scratch initially. The bot's uniqueness comes from conversation, and tools like PipeCat provide a quick jump start <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.
*   **Latency Monitoring**: Track latency everywhere, with "Time to First Byte" being the new most important metric for real-time voice applications <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.
*   **Upgrade Paths**: Ensure clear upgrade paths for critical components. For speech-to-text, Superdial uses Deep and can fine-tune models for improved accuracy <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
*   **Fallbacks**: Have fallbacks ready for every part of the stack (e.g., for LLM outages). Tools like TensorZero can help set this up <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.
*   **End-to-End Testing**: This is particularly unique for [[Voice and multimodal AI agents | voice AI]]. Telephony is often used as a boundary layer for testing <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>. Methods include:
    *   **Fake Phone Numbers**: Creating a fake number that plays an MP3 to test basic bot interaction <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.
    *   **Simulated Voice Trees**: Creating a simulated phone tree for the bot to navigate <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.
    *   **Bot-to-Bot Testing**: Using generative services like Koval and V to have the bot converse with another bot <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

## Key Takeaways
For [[Voice AI engineering challenges and solutions | voice AI engineers]], key takeaways for [[Building and Improving AI Agents | building and improving AI agents]] are:
*   **Choose your stack wisely**: Better decisions here allow focus on unique conversational experiences <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.
*   **Laser focus on the Last Mile**: This is where significant value can be added and agents can be put to work <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.
*   **Ride the wave**: Stay current with new models and advancements to integrate them quickly and safely <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.