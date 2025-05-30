---
title: Using Vector Shift for Voice Bots
videoId: L9JqdwdCiyE
---

From: [[colemedin]] <br/> 

This article explores how to build and deploy [[voice_ai_agents | voice AI agents]] using the [[vectorshift_platform_for_building_ai_agents | VectorShift platform]], a no-code AI automation platform. While voice AI agents are powerful for enabling natural conversations with AI, their implementation can often be challenging on many platforms <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. [[vectorshift_platform_for_building_ai_agents | VectorShift]] simplifies this process, allowing users to create and deploy full voice agents with knowledge bases in minutes without coding <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

[[vectorshift_platform_for_building_ai_agents | VectorShift]] is compared to other AI automation tools like LangFlow, Flowise, and n8n, but it stands out due to key [[vector_shift_features | features]], especially its capabilities around [[voice_ai_agents | voice agents]] <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Building a Voice Agent Workflow with VectorShift

The process of [[creating_a_rag_ai_agent_with_vectorshift | creating a RAG AI agent with VectorShift]] involves setting up a workflow (pipeline) that handles audio input and output.

### Setting up the Knowledge Base

Before building the pipeline, a knowledge base needs to be set up. This example uses a Google Drive-hooked knowledge base, where specific folders can be ingested into the knowledge base <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. [[vectorshift_platform_for_building_ai_agents | VectorShift]] provides visibility into the documents and their chunks within the knowledge base <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

### Pipeline Construction

1.  **Input Node (Audio)**: The workflow begins by dragging in an input node. The input type is then changed from text to audio <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. This step is crucial for integrating with [[ai_voice_systems_and_integration | voice AI systems]] <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
2.  **Speech-to-Text Conversion**: A "Speech to Text" node (found under the Multimodal tab) is used to convert the audio input into text. OpenAI Whisper is recommended for this purpose <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
3.  **Large Language Model (LLM)**: A GPT-4o Mini model is used as the LLM <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
    *   **System Message**: Defines the behavior of the LLM, e.g., "You are a personal assistant who helps answer user questions to the best of your ability" <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
    *   **User Prompt with Parameters**: The user prompt is defined to include dynamic inputs using squiggly brackets, such as `{{prompt}}` for the user's question and `{{context}}` for information from the knowledge base <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
4.  **Knowledge Base Integration**: A "Knowledge Base" node queries relevant documents based on the text output from the speech-to-text node. The results are fed into the LLM as context <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
5.  **Text-to-Speech Conversion**: The text response from the LLM is fed into a "Text to Speech" node. Options include OpenAI and Eleven Labs, with Eleven Labs offering more voices and customization <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
6.  **Output Node (Audio)**: Finally, the audio output from the text-to-speech node is directed to an output node, which is set to audio type <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

The entire workflow can be built in just a few minutes <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

### Agent Flexibility and Integrations

[[vectorshift_platform_for_building_ai_agents | VectorShift]] offers extensive flexibility <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>:
*   **Integrations**: It supports integrations with numerous services, similar to Zapier or Make.com <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **API Node**: An API node allows users to hook into any API endpoint, enabling calls to custom agents built with Python or webhooks from other platforms like n8n <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
*   **Logic Tab**: Includes convenient nodes like a summarizer <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

## Deploying AI agents using Voice Flow

After building the workflow, it can be deployed as a voice bot within the "Voice Bots" section of the [[vectorshift_platform_for_building_ai_agents | VectorShift]] dashboard <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### Voice Bot Customization and Embedding
[[deploying_ai_agents_using_voice_flow | Deploying AI agents using Voice Flow]] (or rather, the voice bot feature in VectorShift) allows for significant customization:
*   Users can select the pipeline (workflow) made with audio input and output <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   Extensive UI customization options are available for the embedded widget, including changing icons and text <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   The voice bot can be exported as a standalone web page or embedded using an iframe or script tag for a chat widget <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

### Testing the Voice Agent
The voice agent, once deployed, can answer questions using its knowledge base. While there might be a slight delay in response generation compared to phone-calling platforms <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>, it works effectively. For instance, it can retrieve specific action items from meeting notes ingested into its knowledge base <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.

### Building a Front-end with AutoDev

To integrate the [[vectorshift_platform_for_building_ai_agents | VectorShift]] voice agent into a custom website, a front-end can be built using AutoDev (or bolt.new). AutoDev can generate a vanilla HTML landing page with an iframe for the voice agent <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.

> [!NOTE]
> Iframes from [[vectorshift_platform_for_building_ai_agents | VectorShift]] may not work directly within the web container of bolt.new, requiring the generated HTML to be run in an external HTML/CSS/JS editor like JSFiddle for testing <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

Despite this minor quirk, AutoDev successfully generates the necessary code to embed the voice agent into a custom front-end <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.

## Conclusion: Advantages of Vector Shift

[[vectorshift_platform_for_building_ai_agents | VectorShift]] significantly simplifies the creation of any AI agent, particularly [[voice_ai_agents | voice agents]], which are often difficult to implement on other platforms out-of-the-box <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. Beyond [[voice_ai_advancements_and_applications | voice AI advancements and applications]], [[vectorshift_platform_for_building_ai_agents | VectorShift]] offers unique [[vector_shift_features | features]] like analytics and other production-grade capabilities <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>, making it a highly recommended platform for building AI agents.