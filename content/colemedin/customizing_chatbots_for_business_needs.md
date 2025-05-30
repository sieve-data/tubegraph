---
title: Customizing chatbots for business needs
videoId: 1I0PvfHjaRE
---

From: [[colemedin]] <br/> 

AI offers many potential uses, but a highly effective and practical application for businesses is a lead generation agent on a website that can operate autonomously <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This type of agent can handle lead qualification, answer questions, suggest products or resources, and collect contact information for follow-ups <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. While many platforms exist for building such agents, many lack sufficient customizability, leading some to consider building agents from scratch using tools like [[n8n | n8n]] or [[setting_up_and_optimizing_chat_memory_for_ai_agents | Lang chain]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. However, platforms like [[building_a_chatbot_with_chatlink | Chatlink]] offer robust solutions for [[building_a_no_code_website_chatbot | building a no-code website chatbot]] tailored to specific needs <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Introducing Chatlink for Lead Generation
[[building_a_chatbot_with_chatlink | Chatlink]] enables the creation of full lead generation agents that sit on a website, qualify leads, and answer questions using a [[customizing_chatbot_with_rag | RAG knowledge base]] <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. It provides a generous free tier to build and test chatbots <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Chatlink Dashboard and Resources
Upon signing in, users are directed to a dashboard with various resources:
*   **API Documentation**: Allows management of agents, knowledge bases, and conversations via API <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Roadmap**: Shows current platform developments and allows users to submit suggestions, indicating an evolving platform <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Building a Lead Generation Agent
To create an agent in [[building_a_chatbot_with_chatlink | Chatlink]], navigate to the "My Agents" tab and click "Create Chatbot" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### Chatbot Template Options
[[building_a_chatbot_with_chatlink | Chatlink]] provides three main options for starting a chatbot <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>:
1.  **AI Chatbot**: A more basic chatbot not specifically geared towards lead generation <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
2.  **Basic Lead Generation Chatbot**: Does not leverage AI; designed for standard questions <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
3.  **Lead Generation Plus AI Chatbot**: Offers intelligent interaction for user qualification and recommendations <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
Users can also start from scratch, but using a template, especially the "Lead Generation Plus AI Chatbot" template, can quickly provide an understanding of [[building_a_chatbot_with_chatlink | Chatlink]] <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

### Workflow Builder
The "Builder" tab features a node workflow builder, similar to Vector Shift or Voice Flow <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   Workflows begin with a "Start" node (when the message first comes in) and conclude with an "End" node (when the chat widget interaction concludes) <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   The entire workflow represents a single conversation <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   Looping features allow for asking multiple questions to the agent <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### Using Widgets to Build Workflows
Actions and user input handling in [[building_a_chatbot_with_chatlink | Chatlink]] are performed using widgets available on the left-hand side <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Blocks**: Used for actions like sending hardcoded messages, getting AI responses, or adding buttons <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   **Custom Variables**: Any input or output from widgets can be saved into custom variables, which can then be referenced in subsequent nodes <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This ensures the agent maintains context of the user's responses <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **Diverse Actions**: Widgets support HTTP requests, sending emails, conditional logic to handle different user responses, and buttons for simple user choices (e.g., yes/no) <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
*   **AI Configuration**: Settings for AI models (e.g., GPT-4o mini) and their [[customizing_chatbot_with_rag | knowledge base]] can be set globally or individually for specific nodes <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### Example Lead Qualification Workflow
A typical lead generation workflow in [[building_a_chatbot_with_chatlink | Chatlink]] might involve <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>:
1.  **Greeting**: Displaying an image (like a logo) followed by several greeting messages <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
2.  **Service Inquiry**: Asking the user about their interest in specific services (e.g., AI consulting services like solution development, one-on-one consulting, pre-made agents) <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. The user's selection is stored as a variable <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
3.  **Qualification Questions**: The bot asks follow-up questions to understand the user's needs better, leveraging the selected service name and previous answers in the prompt <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. User outputs are captured in variables <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
4.  **Question Handling**: After qualification, the bot asks if the user has further questions, offering buttons for "yes" or "no" instead of free-form input <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
5.  **[[customizing_chatbot_with_rag | RAG Knowledge Base]] Interaction**: If the user has questions, the bot prompts them to ask and then answers based on its [[customizing_chatbot_with_rag | RAG knowledge base]] <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. The conversation loops back to ask if there are more questions, ensuring all queries are addressed <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
6.  **Contact Information Collection**: Once all questions are answered, the bot collects the user's name and email, which are stored as a contact record within [[building_a_chatbot_with_chatlink | Chatlink]] <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

## Knowledge Base and Customization
[[building_a_chatbot_with_chatlink | Chatlink]] offers powerful options for [[customizing_chatbot_with_rag | customizing chatbot with RAG]] through its knowledge base <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>:
*   **Website Link**: Crawl an entire website for information <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
*   **Sitemap**: Ideal for e-commerce stores, allowing the bot to understand all product URLs <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Custom URL List**: Up to 2,000 links can be included <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
*   **Document Uploads**: Ingest documents for the knowledge base <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Raw Text**: Directly input free-form text <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   **FAQs**: Directly input question-answer pairs for common queries <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

## Appearance Customization
[[customizing_ai_agent_interfaces | Customizing AI agent interfaces]] is crucial for branding. [[building_a_chatbot_with_chatlink | Chatlink]] provides extensive options to customize the chat widget's appearance to match business branding <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. This includes styling and changing the image for the AI agent <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

## Conversation Management and Integrations
[[building_a_chatbot_with_chatlink | Chatlink]] also functions as a light CRM, allowing users to view all conversations and link them to user contact information (email, phone) <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. This enables follow-ups with leads who have provided their contact details <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.

### Website Integration
[[integrating_chatbots_with_website | Integrating chatbots with a website]] is straightforward <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. [[building_a_chatbot_with_chatlink | Chatlink]] provides a script tag that can be embedded into virtually any website builder <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>, including Shopify, WordPress, Wix, Go High Level, or custom Next.js sites <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
*   **Floating Chat**: A common widget in the bottom right corner of a website <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.
*   **Inline/Full Screen**: The chatbot can be an integral part of the web page <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

### Other Integrations
[[building_a_chatbot_with_chatlink | Chatlink]] integrates with Zapier, which can be used to handle contact information submitted by users <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.

## Advanced Customization and Usefulness
[[building_a_chatbot_with_chatlink | Chatlink]]'s pipeline creation is highly customizable <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>. Users can send images or audio as messages <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>. HTTP requests allow for hooking into any API, including custom agents hosted with [[n8n | n8n]] or LangServe, as part of the workflow <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>. This level of customization ensures that almost any type of lead generation agent can be built <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>.

[[advantages_of_using_ai_tools_for_productivity_in_chat_platforms | Using AI tools for productivity in chat platforms]], like [[building_a_chatbot_with_chatlink | Chatlink]], to build powerful and [[customizing_ai_agent_interfaces | customizable agents]] for [[integrating_ai_chatbots_on_websites | integrating AI chatbots on websites]] for lead generation is especially useful for e-commerce stores, agencies, or consulting businesses <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>. It removes the need for busy professionals to build complex agents from scratch, without sacrificing customizability <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>. These front-facing chatbots typically do not handle private data, so hosting on a platform is a practical solution <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.