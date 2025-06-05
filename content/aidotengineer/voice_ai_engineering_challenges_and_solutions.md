---
title: Voice AI engineering challenges and solutions
videoId: 2p2ErKRELHM
---

From: [[aidotengineer]] <br/> 

Nick from Superdial discussed the evolving landscape of voice AI, highlighting key [[challenges_in_developing_ai_agents | challenges in developing AI agents]] and practical solutions for building reliable voice AI applications, drawing from Superdial's experience as an "agents as a service" platform <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Voice AI in 2025: Current Landscape
The field of voice AI is dynamic and exciting <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Key developments and ongoing [[challenges_in_building_ai_voice_agents | challenges in building AI voice agents]] include:
*   **Large Language Models (LLMs)**: New, smart, fast, and affordable LLMs are emerging, supporting more complex conversational use cases <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. However, turning a chat agent into a voice agent still requires specific techniques <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Text-to-Speech (TTS) Models**: While low-latency, realistic, and highly generative TTS models exist, they can suffer from audio hallucinations and issues with pronunciation and spelling <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   **Infrastructure and Tooling**: There's an explosion in voice AI infrastructure, tooling, and evaluation systems, leading to questions about what components are truly worth owning <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Speech-to-Speech/Voice-to-Voice Models**: These models are not yet production-ready for many applications due to their tendency to output non-speech or unreliable conversational elements <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Superdial prioritizes reliability over realism for these models <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Superdial's "Agents as a Service" Approach
Superdial specializes in automating "annoying phone calls," specifically to insurance companies for healthcare administration businesses <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### Platform Features
Superdial's platform allows customers to:
*   Build conversational scripts to ask necessary questions <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   Send call requests via CSV, API, or EHR software integrations <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   Receive structured results within hours or a day <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Agentic Loop and Human Fallback
Superdial employs an internal agentic loop:
1.  Calls are made when offices or call centers are open <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
2.  A voice bot attempts the call <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
3.  If the bot cannot complete the call after a certain number of attempts, it's sent to a human fallback team <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. This ensures calls are completed regardless of bot or human involvement, providing reliable answers in a structured format <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
4.  The system learns from each call, updating office hours and optimizing phone tree traversal for future attempts <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Random audits ensure system reliability for sensitive healthcare calls <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

### Impact
Superdial has saved over 100,000 hours of human phone and calling time, with projections to save millions more <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. This was achieved with a lean team of four engineers building the full stack, EHR integrations, and the bot, while rapidly onboarding customers and supporting new use cases <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

## The Role of a [[the_role_and_skills_of_a_voice_ai_engineer | Voice AI Engineer]]
The success of Superdial is partly attributed to the team embracing the unique role of a [[the_role_and_skills_of_a_voice_ai_engineer | voice AI engineer]] <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

### Unique Characteristics
A [[the_role_and_skills_of_a_voice_ai_engineer | voice AI engineer]] typically deals with:
*   **Multimodal Data**: Including MP3s, audio bites, and transcripts <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   **Real-time Latency**: Crucial for real-time applications <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **Asynchronous Programming**: Heavy use of async Python <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   **Product Constraint**: Voice conversations with high user expectations <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

### Core Principles
Superdial's key principles for voice AI engineering include:
*   "Say the right thing at the right time" <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   "Build this plane while we fly it" <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   Focus on conversational content, design, and vertical integrations to make agents valuable <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

### Ethical Considerations
Given the nature of generative AI, ethical concerns are significant <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. [[challenges_in_building_ai_voice_agents | Voice AI apps]] can be biased against certain accents or dialects, or sound "spooky" if too realistic but say strange things <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. Without strong AI regulation, the onus is on engineers and leaders to prioritize:
*   **Accessibility**: Ensuring AI development is accessible and collaborative <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Inclusivity**: Designing AI that works for everyone by choosing tooling and infrastructure that allows diverse stakeholders to be involved from the start <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.

## [[challenges_and_innovations_in_ai_engineering | Last Mile Problems]] in Voice AI
Building a basic voice AI MVP is relatively easy, but making it reliable and production-ready involves significant "last mile" [[challenges_in_developing_ai_agents | challenges]] <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

### Conversation Design
One of the biggest changes in voice UI development is the shift from prescriptive (mapping every possible conversational direction) to descriptive (describing desired behavior and hoping the generative model executes) <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

*   **Challenge**: Deciding between open-ended questions or constraining user choices <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Solution**: For existing conversations, Superdial found it better to be general, hoping for comprehensive information from the call center representative, and adapting to their responses rather than preventing "wrong" things <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.
*   **Recommendation**: Hire a conversation designer, or perform "table reads" (role-playing the bot and user) to identify conversational gaps and awkwardness <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.

### Orchestration Framework
*   **Challenge**: Dealing with technical debt from initial, scrap-together pipelines <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.
*   **Solution**: Using PipeCat, an open-source framework by Daily, which is easy to extend, hack upon, and allows for self-hosting and scaling, crucial for long phone calls (up to 1.5 hours) <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.

### LLM Backbone (General AI Engineering)
While not unique to [[voice_and_multimodal_ai_agents | voice AI]], choices for the LLM backbone are critical:
*   **LLM Endpoint**: Superdial owns its OpenAI endpoint to better interface with new [[voice_and_multimodal_ai_agents | voice AI tools]], allowing routing to latency-sensitive models <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   **Generative Responses**: All generative responses are routed through TensorZero, which provides structured and typed LLM endpoints for experimentation in production <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
*   **Logging and Observability**: LaneFuse is self-hosted for logging and observability, enabling anomaly detection, evaluations, and dataset management, which is essential for HIPAA compliance in healthcare calls <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.

### Text-to-Speech (TTS) System
*   **Challenge**: Ensuring the LLM output, TTS engine output, and actual recording match, especially for sensitive data like member IDs (e.g., 12-digit strings) <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>. Pronouncing names correctly (e.g., "Kotus" vs. "Koutus") is a common issue <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.
*   **Solution**: Using custom pronunciation syntax (e.g., from Rhyme) to spell out exact pronunciations, and "spell functions" to manage pauses and breaks for long words or character strings <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>. Reviewing audio recordings is crucial <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.

### Mini Last Mile Problems and Solutions
*   **Bot Persona**: Avoid names that are easily misunderstood over the phone (e.g., "Billy" vs. "Billi") <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. Dial in the bot's persona early <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.
*   **Building from Scratch**: Don't build from scratch; leverage existing tools like PipeCat for a quick start, as the bot's uniqueness lies in the conversation <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.
*   **Latency Tracking**: Track "Time to First Byte" everywhere, as it's a critical metric for real-time voice AI <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.
*   **Upgrade Paths**: Plan for system improvements. Superdial uses Deepgram for speech-to-text, knowing they can fine-tune models for better transcription accuracy <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
*   **Fallbacks**: Have fallbacks ready for each part of the stack (e.g., when OpenAI goes down) to prevent service interruptions <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>. Tools like TensorZero can help set this up <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.
*   **End-to-End Testing**: This is unique for [[voice_and_multimodal_ai_agents | voice AI]]. Telephony is often used as a boundary layer. Methods include:
    *   Calling a fake phone number that plays an MP3 <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.
    *   Creating a simulated voice tree for the bot to navigate <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.
    *   Using generative services like Koval and V to have the bot talk to another bot <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

## Takeaways for [[the_role_and_skills_of_a_voice_ai_engineer | Voice AI Engineers]]
For those in vertical voice AI engineering:
*   **Choose your stack wisely**: Good decisions here allow focus on unique conversational experiences <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.
*   **Laser focus on the last mile**: This is where significant value can be provided and agents put to work reliably <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.
*   **Ride the wave**: Stay current with new models to use them quickly and safely <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.