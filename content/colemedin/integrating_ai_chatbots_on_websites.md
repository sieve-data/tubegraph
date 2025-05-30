---
title: Integrating AI chatbots on websites
videoId: 1I0PvfHjaRE
---

From: [[colemedin]] <br/> 

[[integrating_ai_with_front_ends | Integrating AI]] chatbots on websites offers a powerful solution for businesses, particularly for lead generation and customer interaction <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. These AI agents can qualify leads, answer questions, suggest products or resources, and collect contact information for follow-ups, operating even while the business is closed <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Challenges with Building AI Agents
While many platforms exist for [[building_a_no_code_website_chatbot | building no-code website chatbots]], many are considered inadequate due to a lack of customizability and overall effectiveness <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This often leads users to attempt to build agents themselves using tools like [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n]] or Langchain <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. However, platforms like [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n]] may lack advanced features such as multi-select options or complex looping within their chat widgets <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

## Chatlink: A Robust Solution
Chatlink is highlighted as a platform designed for [[building_a_no_code_website_chatbot | building robust lead generation AI agents]] tailored to specific business needs <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

### Getting Started with Chatlink
Users can begin by visiting `chatlink.io` and selecting the "start for free" option <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The platform offers a generous free tier, allowing users to build multiple chatbots and conduct dozens of conversations for testing <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

Upon signing in, users access a dashboard with various resources <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **API Documentation**: Allows management of agents, knowledge bases, and conversations via API <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Roadmap**: Provides insight into current developments and allows users to submit suggestions <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Chatlink is an evolving platform <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### Building a Lead Generation Agent
To create an agent, users navigate to the "My Agents" tab and click "Create Chatbot" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

#### Chatbot Types
Chatlink offers three main options for creating chatbots <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>:
1.  **AI Chatbot**: A basic chatbot not primarily geared towards lead generation <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
2.  **Basic Lead Generation Chatbot**: Does not leverage AI, focusing on standard questions <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
3.  **Lead Generation Plus AI Chatbot**: Provides intelligent interactions for lead qualification and recommendations <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

Users can also start from scratch, though templates are recommended for quicker understanding <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

#### Workflow Builder
Chatlink uses a node-based workflow builder, similar to platforms like Vector Shift or Voice Flow <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   Workflows begin with a "Start" node when a message is first received <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   The workflow represents an entire conversation and can include looping for continuous interaction <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

#### Customization Options (Blocks and Variables)
Actions and user inputs are handled using "widgets" or "blocks" available on the left-hand side <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Sending Messages**: Text blocks allow sending hard-coded messages or AI responses <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   **User Input**: The "Capture Text" block allows waiting for user responses and storing them in custom variables <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Variables**: Custom variables can be used to store and reference information throughout the workflow, providing context to the AI <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Buttons**: Allows users to select from predefined options, useful for guiding conversations <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Advanced Blocks**: Includes HTTP requests (for custom agents or API interactions), sending emails, and conditional statements to handle different user responses <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   **AI Configuration**: Users can set the AI model (e.g., GPT-4o mini) and manage knowledge base settings <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. Models can be set globally or individually per node <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

### Knowledge Base (RAG)
The platform supports various data sources for its Retrieval Augmented Generation (RAG) knowledge base <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>:
*   **Website Link**: Crawls an entire website to ingest information <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
*   **Sitemap**: Ideal for e-commerce stores, allowing the AI to understand details about different products <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Custom URL List**: Supports up to 2,000 links <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
*   **Documents**: Uploading relevant files <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Raw Text**: Direct input of textual information <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   **FAQs**: Structured question-answer pairs for common queries <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

### Appearance Customization
Chatlink allows extensive customization of the chat widget's appearance to match business branding, including changing images (e.g., AI persona image) and styling options <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

### Conversation Management
The platform provides a view of all conversations, acting as a lightweight CRM. It can store user information like email and phone numbers, allowing businesses to follow up with leads who have provided their contact details <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

### Embedding the Widget on a Website
Chatlink agents can be embedded using a website widget integration <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. While it integrates with Zapier, direct [[integrating_ai_agents_in_n8n_using_open_web_ui | n8n]] integration is not explicitly mentioned <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.

Three display options are available <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>:
1.  **Floating Chat**: A common small widget typically found in the bottom right corner of a website <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.
2.  **Inline**: Becomes a part of the webpage itself <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.
3.  **Full Screen**: Occupies the entire screen <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

Embedding involves copying a script tag into the website's HTML, compatible with various website builders like Shopify, WordPress, Wix, GoHighLevel, or custom Next.js sites <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.

### Example Walkthrough
A demonstration shows a lead generation chatbot for an AI consulting agency. The bot greets the user, asks about their interests (e.g., "one-on-one Consulting sessions"), qualifies their needs through follow-up questions, answers questions using its RAG knowledge base (e.g., "what is involved in the one-on-one sessions"), and finally collects contact information <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. The AI generates relevant questions and can use the knowledge base to answer specific queries accurately <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.

## Conclusion
[[integrating_ai_agents_with_live_platforms | Integrating AI agents with live platforms]] like Chatlink on websites is particularly beneficial for businesses such as e-commerce stores, agencies, or consulting firms <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>. It provides a robust and customizable solution for lead generation without sacrificing customization or requiring local hosting, as front-facing chatbots typically do not handle private data <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.