---
title: AI for lead generation
videoId: 1I0PvfHjaRE
---

From: [[colemedin]] <br/> 

One practical and essential use case for [[AI in marketing and lead nurturing | AI in marketing and lead nurturing]] is deploying a lead generation agent on a website <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This agent can manage the front end of a business, performing tasks such as lead qualification, answering questions, suggesting products or resources, and collecting contact information for follow-ups <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>, <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Current Landscape of AI Agent Development

While many platforms exist for [[Building AI Agents | building AI agents]], most are deemed insufficient due to lack of customizability and overall quality <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>, <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Building an agent from scratch using tools like n8n or LangChain is possible but not trivial <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>, <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Chatlink as a Solution
Chatlink is highlighted as a platform specifically designed for building comprehensive lead generation agents <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. It offers a generous free tier for users to experiment with building chatbots <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Key Features for Building a Lead Generation Agent in Chatlink

### Agent Creation
Users can create a chatbot by selecting "My Agents" and then "Create Chatbot" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Options include:
*   A basic AI chatbot <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   A basic lead generation chatbot (without AI) <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   A "Lead Generation + AI chatbot" template, recommended for intelligent user interaction and faster setup <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>, <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   Starting from scratch <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

### Workflow Builder
Chatlink utilizes a node workflow builder similar to platforms like Vector Shift or Voiceflow <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>, <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. This allows for:
*   **Actions and User Input:** Managing actions and handling user input <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Widgets:** Performing actions using widgets from the left-hand side, such as sending hardcoded messages, getting [[understanding_ai_agents | AI responses]], or adding buttons <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>, <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>, <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   **Custom Variables:** Inputs and outputs from widgets can be stored in custom variables, maintaining conversation context for better lead qualification and question answering <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>, <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>, <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Advanced Features:** The builder supports HTTP requests for custom agents, sending emails, conditional logic for different user responses, and buttons for specific inputs (e.g., yes/no) <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>, <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>, <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>, <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   **Looping:** Workflows can include looping mechanisms to allow users to ask multiple questions to the agent <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>, <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

### Knowledge Base (RAG)
Chatlink's knowledge base supports Retrieval Augmented Generation (RAG) and can ingest data from various sources <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>, <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>:
*   **Website Links:** Crawl entire websites for information <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
*   **Sitemap:** Useful for e-commerce stores to understand all product URLs <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>, <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.
*   **Custom URL List:** Up to 2,000 links can be included <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
*   **Documents:** Upload various document types <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Raw Text:** Input free-form text <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   **FAQs:** Create lists of question-answer pairs for common queries <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

### Customization and Integration
*   **Appearance:** The chat widget can be highly customized to match brand aesthetics, including styling options and AI persona images <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>, <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>. This is a significant advantage over building widgets in tools like n8n <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Conversation Management:** Chatlink logs all conversations with the bot and can tie them to user contact information (email, phone), functioning like a CRM <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>, <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>, <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Embedding Options:** Agents can be embedded on websites in three ways <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>, <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>, <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>:
    *   **Floating Chat:** A common widget in the bottom right corner <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.
    *   **Inline:** Integrated directly as part of the web page <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.
    *   **Full Screen:** Occupying the entire web page <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.
*   **API and Integrations:** Chatlink offers API documentation for managing agents, knowledge bases, and conversations programmatically <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. It also integrates with Zapier <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.
*   **Model Selection:** Users can choose the AI model (e.g., GPT-4o mini) for their agent globally or for individual nodes in the workflow <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>, <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>, <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.

## Benefits for Businesses
Using a platform like Chatlink to [[opportunities_for_ai_saas_in_digital_marketing | build AI agents]] for lead generation is especially beneficial for businesses such as e-commerce stores, agencies, or consulting businesses, as it allows them to create robust and customizable front-facing chatbots without significant time investment <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>, <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>, <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>. These chatbots typically don't handle private data, making cloud-based solutions practical <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>.