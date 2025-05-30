---
title: Nocode AI Automation Platforms
videoId: L9JqdwdCiyE
---

From: [[colemedin]] <br/> 

Nocode AI automation platforms allow users to [[building_ai_agents_with_nocode_tools | build AI agents]] and automate workflows without writing code. These platforms are designed to simplify the implementation of complex AI functionalities, such as voice AI agents and knowledge base integrations <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. While many platforms exist, some excel in specific areas like voice agent implementation <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Vector Shift: A Leading Platform

Vector Shift is highlighted as a favored [[no_code_ai_app_builders | no code AI app builder]] and automation platform, particularly for its capabilities around voice agents <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. It is comparable to other [[ai_automation_with_n8n | AI automation]] tools like Langflow, Flowise, and [[ai_automation_with_n8n | n8n]] <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Although open-source platforms like Flowise and [[ai_automation_with_n8n | n8n]] are valuable, Vector Shift offers unique features for various use cases <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

Vector Shift provides:
*   A user-friendly dashboard for managing pipelines <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   A knowledge base builder that can ingest data from sources like Google Drive <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   Visibility into documents and chunks within the knowledge base <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   Extensive documentation across its features <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
*   Unique features like analytics and other production-grade capabilities <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

## Building a Voice AI Agent with Vector Shift

The process of [[building_ai_agents_with_nocode_tools | building a voice agent]] with Vector Shift involves a workflow within its pipeline builder <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

### Workflow Steps

1.  **Input Node Configuration**: Begin by dragging an input node and changing its type from text to audio <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. This enables the workflow to receive audio inputs <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
2.  **Speech-to-Text Conversion**: Use a speech-to-text node (e.g., OpenAI Whisper model) to convert the incoming audio into text <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>, <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
3.  **Large Language Model (LLM) Integration**: Incorporate an LLM node (e.g., GPT-4o Mini) <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
    *   **System Message**: Define the LLM's behavior (e.g., "You are a personal assistant who helps answer user questions") <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
    *   **User Prompt with Dynamic Inputs**: Create parameters within the prompt using squiggly brackets (e.g., `{prompt}` for user input and `{context}` for knowledge base integration) <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>, <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
4.  **Knowledge Base Integration**: Drag in a knowledge base node, select a pre-configured knowledge base (e.g., linked to Google Drive) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>, and feed the text output from the speech-to-text node as the query <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. The knowledge base results are then sent as context to the LLM <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
5.  **Text-to-Speech Conversion**: Feed the LLM's text response into a text-to-speech node (e.g., OpenAI or Eleven Labs) to convert it back into audio <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
6.  **Output Node Configuration**: Connect the audio output from the text-to-speech node to an output node, ensuring the output node's type is set to audio <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

### Agent Flexibility and Integrations

Vector Shift offers an "Integrations" tab with numerous services, similar to Zapier or Make.com <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. It also provides an API node, enabling connection to any API endpoint, allowing users to call custom agents built with Python or [[ai_automation_with_n8n | n8n]] workflows that are webhooks <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. This flexibility allows users to build "pretty much any agent" they desire <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>, <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. The platform also includes convenient built-in logic and summarizer nodes <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

## Deploying and Embedding Voice Agents

Once a workflow is completed, it can be deployed within Vector Shift <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. The deployed workflow can then be integrated into a "Voice Bot" section of the platform <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>, <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### Voice Bot Customization and Embedding
*   Voice bots can be embedded as a chat widget or through an iframe on a website <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
*   Users can customize the UI of the embed, including icons and text <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   The platform provides an export option to get a direct web page link, as well as script tags for chat widgets and iframe code for embedding <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

### Frontend Development with Autodev
To create a simple frontend for the voice agent, tools like [[using_ai_coding_assistance | Autodev]] (specifically, `bolt.new`, an [[opensource_ai_coding_assistant_development | open source AI coding assistant]]) can be used <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>, <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>. While `bolt.new`'s web container might block iframes from Vector Shift, the generated HTML code can be used in other online editors like JSFiddle to preview the embedded agent <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>, <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

## Performance Notes
While the voice agent functionality works well, response generation can be slower compared to dedicated phone calling platforms like Vapi <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. The voice agent might also attempt to cite URLs during its response, which can be addressed by adjusting the LLM prompt <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

## Benefits of Nocode AI Automation Platforms
These platforms, particularly Vector Shift, offer significant [[benefits_of_no_code_platforms_for_ai_agents | benefits for building AI agents]], making it easy to create various types of agents, especially voice agents, out-of-the-box <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>, <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. They also provide features like analytics and production-grade tools that might be absent in other platforms <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.