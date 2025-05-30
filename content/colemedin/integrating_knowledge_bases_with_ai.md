---
title: Integrating Knowledge Bases with AI
videoId: L9JqdwdCiyE
---

From: [[colemedin]] <br/> 

Integrating knowledge bases with AI agents is a key aspect of building intelligent systems that can retrieve and utilize external information to provide more accurate and relevant responses <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. This approach allows AI agents to access specific, domain-relevant data, enhancing their capabilities beyond their initial training data <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

## Vector Shift for AI Automation

Vector Shift is highlighted as a powerful no-code AI automation platform that simplifies the implementation of voice AI agents and the integration of knowledge bases <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. It is comparable to other AI automation tools like LangChain, Flowise, and n8n, but offers distinct features, especially for voice agent capabilities <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. While open-source platforms are valuable, Vector Shift offers convenience and unique features for many use cases <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### Knowledge Base Setup

[[using_google_drive_as_a_knowledge_base_for_ai_agents | Using Google Drive as a knowledge base for AI agents]] is a straightforward process within Vector Shift <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>:
*   Users can create a new knowledge base and connect it directly to their Google Drive <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   Specific folders can be selected for ingestion into the knowledge base <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   The platform provides visibility into ingested documents and their segmented "chunks" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

### Building a Voice Agent Workflow

The process of building a voice agent with a knowledge base in Vector Shift involves several nodes in a pipeline <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>:

1.  **Input Node**: Configured to accept audio input, which enables the voice part of the platform <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
2.  **Speech to Text Node**: Converts the incoming audio into text using models like OpenAI Whisper, making it consumable by a Large Language Model (LLM) <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
3.  **Large Language Model (LLM) Node**:
    *   An LLM like GPT-4o Mini can be selected <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
    *   A **system prompt** defines the LLM's behavior (e.g., "You are a personal assistant...") <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
    *   The **user prompt** integrates both the user's question (from speech-to-text) and the context from the knowledge base <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. Parameters can be defined in the prompt to accept multiple inputs <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
4.  **Knowledge Base Node**:
    *   The text output from the speech-to-text node serves as the query for the knowledge base <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
    *   The selected knowledge base (e.g., Google Drive) retrieves relevant documents <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
    *   The results from the knowledge base are fed into the LLM as "context," ensuring the LLM uses specific information to answer questions when applicable <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
5.  **Text to Speech Node**: The LLM's text response is converted back into audio using services like OpenAI or Eleven Labs <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
6.  **Output Node**: Configured to deliver the final audio response <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

This entire workflow can be built in minutes without coding <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

### Integration Capabilities

Vector Shift supports diverse [[integrations_and_collaboration_in_ai_platforms | integrations and collaboration in AI platforms]]:
*   It offers numerous built-in services, similar to Zapier or Make.com <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   For services not directly available, users can set up workflows in platforms like Zapier or Make.com and call into them within Vector Shift <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   An API node allows connection to any API endpoint, enabling the use of custom Python agents or n8n workflows as webhooks <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
*   The platform also includes convenience features such as a built-in summarizer node <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

### Deployment and Front-End Integration

Once the voice agent workflow is built, it can be deployed as a "voice bot" <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. This voice bot can then be embedded as a chat widget on a website using a script tag or as part of the website itself via an iframe <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

[[integrating_ai_with_front_ends | Integrating AI with Front Ends]] is further demonstrated by [[using_external_knowledge_in_ai_coding | AutoDev]] (a fork of Bolt.new) to create a simple HTML landing page around the Vector Shift voice agent's iframe <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. Although iframes might have limitations within certain web containers (like Bolt.new's), the generated code can be easily used in external HTML/CSS editors for deployment <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.

Vector Shift's robust documentation is also noted as a significant advantage for users <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. Its unique features, including analytics and other production-grade capabilities, differentiate it from other platforms <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.