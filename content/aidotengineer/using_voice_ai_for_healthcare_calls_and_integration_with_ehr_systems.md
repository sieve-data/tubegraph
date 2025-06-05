---
title: Using voice AI for healthcare calls and integration with EHR systems
videoId: 2p2ErKRELHM
---

From: [[aidotengineer]] <br/> 

Superdial is a company that specializes in using voice AI for phone calls, particularly those to insurance companies within the healthcare administration sector <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Their platform aims to automate and streamline these often complex and annoying interactions <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

## Superdial Platform Capabilities

The Superdial platform offers several key features for businesses:
*   **Script Building** Customers can design their conversations and outline the questions needed to gather information over the phone <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   **Call Submission** Calls can be submitted via CSV, API, or through integrations with existing Electronic Health Record (EHR) software systems <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **Structured Results** Superdial delivers results back to the customer in a structured format within hours or a day <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

### The Agentic Contract

Superdial operates on an "agentic contract" with its customers, where clients pay for results. They specify who to call and what questions to ask, and Superdial provides the answers <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### Internal Agentic Loop

Internally, Superdial employs an agentic loop to manage calls:
1.  **Timing Calls** The system waits for offices and call centers to open before attempting calls <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
2.  **Voice Bot Attempts** Calls are first attempted using their voice bot <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
3.  **Human Fallback** If the voice bot cannot complete the call after a certain number of attempts, it is seamlessly handed over to a human fallback team <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. This human intervention is often inevitable for complex healthcare calls, and the transparency of this process is a benefit to customers, ensuring calls are always completed <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
4.  **Continuous Learning** The system learns from each call, updating office hours for specific phone numbers and improving its phone tree traversal strategies for future interactions <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
5.  **Auditing** Due to the sensitive nature of healthcare calls, a random selection of calls are audited to ensure system functionality <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

### Example: Prior Authorization Call

An example demonstration showcased a prior authorization call where the bot, after navigating a phone tree, successfully communicated with a human representative to obtain information for a customer <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. The speaker noted that a "boring call" is an "excellent call" in this context, as it signifies successful automation of routine, yet critical, tasks <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

### Impact and Efficiency

The Superdial system has saved over 100,000 hours of human phone and calling time and is projected to save millions more in 2025 <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. This achievement was made possible by a lean team of four engineers who built the full-stack web application, EHR integrations, and the voice bot, while simultaneously onboarding new customers and supporting new conversational use cases <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

## [[the_role_and_skills_of_a_voice_ai_engineer | The Role of a Voice AI Engineer]] in Healthcare

The success of Superdial highlights the unique role of a [[the_role_and_skills_of_a_voice_ai_engineer | voice AI engineer]]. They deal with [[voice_and_multimodal_ai_agents | multimodal data]] (audio and transcripts), develop real-time applications where latency is critical, and navigate complex asynchronous programming <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. The primary product constraint is a voice conversation, requiring high expectations for conversational flow and integration into existing business interactions <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

Superdial's approach to these [[voice_ai_engineering_challenges_and_solutions | challenges]] is guided by two sayings: "Say the right thing at the right time" and "Build this plane while we fly it" <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. They focus on customizing scripts for each customer while relying on a horizontal voice AI stack for technical challenges <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

## Addressing [[ethical_considerations_and_biases_in_voice_ai_applications | Ethical Considerations and Biases]]

Given the rapid development of generative AI, [[ethical_considerations_and_biases_in_voice_ai_applications | ethical considerations and biases]] are crucial, especially in healthcare applications. Voice AI apps could potentially be biased against people with certain accents or dialects, or create "spooky" realistic but flawed interactions <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. The speaker emphasizes that in the absence of stringent AI regulation, the onus is on engineers and leaders to prioritize [[ethical_considerations_and_biases_in_voice_ai_applications | ethical development]] <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. It's important to choose tools and infrastructure that promote accessibility and collaboration, allowing a diverse range of stakeholders to be involved in the development process from the start <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

## [[voice_ai_engineering_challenges_and_solutions | Last Mile Problems]] in Voice AI

Scaling a voice AI system involves overcoming several "last mile" challenges:

### Orchestration Frameworks
Superdial found their stride using Pipe Chat, an open-source framework for voice AI orchestration <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. Its extensibility and the ability to self-host and scale it were crucial for managing long phone calls (up to 1.5 hours) and features like call transfers <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

### LLM Integration and Observability
*   **OpenAI Endpoint Ownership** Superdial chose to own their OpenAI endpoint, which allows them to route to different models based on latency sensitivity <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   **Structured LLM Responses** All generative responses are routed through TensorZero, an open-source tool that provides structured and typed LLM endpoints for experimentation in production <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.
*   **Logging and Observability** For logging and observability, Superdial self-hosts Lane Fuse. Self-hosting is beneficial for HIPAA compliance, especially with rapid growth in the space <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>. This allows for anomaly detection, evaluations, and dataset management <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.

### Text-to-Speech System Challenges
A significant challenge involves the text-to-speech (TTS) system, particularly for conveying sensitive information like member IDs (e.g., 12-digit strings) <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   **Pronunciation Control** What the LLM outputs and what the TTS engine says may not match the actual recording <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. Tools like Rhyme allow for precise phonetic spellings to ensure correct pronunciation of names or specific terms <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Spelling and Pauses** For long words or sequences, custom functions can be used to control pauses and breaks during spelling <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.
*   **Audio Review** Recordings are frequently reviewed to ensure the audio output sounds natural and correct, in addition to checking transcripts <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.

### Mini Last Mile Problems
*   **Persona Naming** An example given was Superdial's previous bot name, "Billy," which caused confusion on calls due to pronunciation <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>. Dialing in the bot's persona early is crucial <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.
*   **Avoid Building from Scratch** For new projects, leveraging existing tools like Pipe Chat can provide a quick start, allowing focus on unique conversational aspects <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.
*   **Latency Tracking** Time to First Byte for each processor is a critical metric to monitor <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.
*   **Upgrade Paths** Ensuring high transcription accuracy is vital. Partnerships (e.g., with Deep for speech-to-text) enable fine-tuning models for continuous improvement <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
*   **Redundant Fallbacks** Having fallbacks ready for each part of the stack is essential to prevent system outages (e.g., if OpenAI goes down) <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
*   **End-to-End Testing** For [[voice_and_multimodal_ai_agents | voice AI]], end-to-end testing is unique.
    *   **Fake Phone Numbers** Testing with a fake phone number that plays an MP3 file can reveal immediate problems <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.
    *   **Simulated Phone Trees** Creating a simulated voice tree allows the bot to pseudo-navigate it <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.
    *   **Bot-to-Bot Communication** Using generative services like Koval and V allows bots to interact with each other <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

## Key Takeaways for [[the_role_and_skills_of_a_voice_ai_engineer | Voice AI Engineers]]
*   **Strategic Stack Choice** Wisely choosing your technology stack enables focus on unique conversational experiences <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.
*   **Last Mile Focus** Concentrating on the "last mile" challenges provides significant value and ensures agents are effective <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.
*   **Adaptability and Safety** Staying updated with new models and integrating them quickly and safely is crucial for success in the rapidly evolving voice AI space <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.