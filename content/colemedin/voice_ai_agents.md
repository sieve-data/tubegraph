---
title: Voice AI Agents
videoId: L9JqdwdCiyE
---

From: [[colemedin]] <br/> 

[[Voice AI advancements and applications | Voice AI agents]] allow users to interact with AI models by speaking to them, similar to chatting with a person <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This capability is highly sought after by users for various projects <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Challenges in Building Voice AI Agents

Historically, a significant hurdle in adopting [[Voice AI advancements and applications | voice AI agents]] has been the difficulty of implementing them on most platforms <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Vector Shift: A Solution for Voice AI Agents

Vector Shift is highlighted as a favored no-code AI automation platform that excels in implementing [[Voice AI advancements and applications | voice AI agents]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. It is comparable to other AI automation tools like Lang flow, Flowise, and n8n, but its capabilities around [[Voice AI advancements and applications | voice agents]] make it stand out for many use cases <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. While open-source platforms like Flowise and n8n are also used, Vector Shift is preferred for many tasks <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

With Vector Shift, users can [[building_ai_agents | build a full voice agent]] with a knowledge base from Google Drive in just a few minutes, without any coding <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Once built, these agents can be deployed to a user's own website <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

### Building a Voice AI Agent in Vector Shift

To build a [[Voice AI advancements and applications | voice agent]] from scratch in Vector Shift:

1.  **Knowledge Base Setup**: A knowledge base can be easily created and linked to Google Drive, allowing the system to ingest selected folders and documents <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Users can preview documents and their chunks within the knowledge base <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
2.  **Pipeline Creation**:
    *   **Input Node**: The workflow begins with an input node set to "audio" type, enabling integration with the platform's voice capabilities <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
    *   **Speech-to-Text Node**: An audio input is converted into text using a speech-to-text node, typically utilizing models like OpenAI Whisper <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
    *   **Large Language Model (LLM) Node**: The text is fed into an LLM, such as GPT-4o Mini <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
        *   **System Message**: Defines the LLM's behavior (e.g., "You are a personal assistant who helps answer user questions") <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
        *   **User Prompt with Parameters**: The user prompt is defined with dynamic parameters using squiggly brackets, allowing for multiple inputs like the transcribed user query and context from the knowledge base <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
    *   **Knowledge Base Node**: The knowledge base is queried using the text output from the speech-to-text node. The results are then provided as "context" to the LLM <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
    *   **Text-to-Speech Node**: The LLM's text response is converted back into audio using a text-to-speech node, with options like OpenAI or Eleven Labs for various voices <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
    *   **Output Node**: The final audio is directed to an output node, which must be set to "audio" type <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

This entire workflow can be completed in just a few minutes <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

### Deploying [[Voice AI Agents]] with Vector Shift

After building the workflow, it can be deployed by clicking "deploy" in the top right <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. The deployed workflow is then hooked into the "voice Bots" section of the Vector Shift dashboard <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

Customization options are available for the chat widget's UI, including icons, text, and branding <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. Once deployed, an export button provides a direct web page link for testing, as well as embed code (script tag for a chat widget or iframe for website integration) <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

Vector Shift also offers extensive documentation for [[building_ai_agents | building voice bots]] and other platform features <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

### Testing a Voice AI Agent

A basic [[Voice AI advancements and applications | voice agent]] linked to a Google Drive knowledge base can answer general questions and retrieve specific information from its knowledge base <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. For example, it can accurately recall "action items" from meeting notes stored in the knowledge base, even if the content is trivial <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. While the response generation might not be as fast as dedicated phone-calling platforms, it functions effectively for general interaction <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. The agent might attempt to cite sources, which can be modified through the prompt to suppress if desired <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

### Building a Front-End for the Voice AI Agent

To integrate the Vector Shift [[Voice AI advancements and applications | voice agent]] into a custom web presence, a front-end can be built around its iframe embed code <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. Tools like Autodev (part of Bolt.new) can generate simple HTML landing pages for this purpose <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.

*   **Embedding Iframe**: The iframe code from Vector Shift's export section is used <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
*   **Web Container Considerations**: Iframes may encounter connection refusal issues within certain web containers (e.g., Bolt.new's web container), necessitating the code to be run in an external HTML/CSS/JS editor like JSFiddle <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.
*   **Customization**: While a basic HTML page can be generated, further styling and integration into a full landing page can be achieved with more detailed prompts <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.

This process enables the Vector Shift [[Voice AI advancements and applications | voice agent]] to be seamlessly embedded and function within custom websites <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.

## Advantages of Vector Shift

Vector Shift simplifies the [[building_ai_agents | building of AI agents]], particularly [[Voice AI advancements and applications | voice agents]], which are often difficult to implement on other platforms <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. It offers unique features, analytics, and production-grade capabilities that might be absent in other platforms <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.