---
title: Building a chatbot with Chatlink
videoId: 1I0PvfHjaRE
---

From: [[colemedin]] <br/> 

Many people have ideas for using AI, but some are impractical or a waste of time <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, a proven and essential use case for any business is a lead generation agent that operates on your website, handling front-end tasks even while you're offline <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. These agents can qualify leads, answer questions, suggest products or resources, and collect contact information for follow-ups <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

While many platforms exist for [[integrating_ai_chatbots_on_websites | building these types of AI agents]], most lack sufficient customizability or quality, making it seem preferable to build an agent yourself using tools like n8n or LangChain <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. However, Chatlink is highlighted as a robust platform that provides the necessary flexibility without the complexity of building from scratch <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. [[building_a_powerful_chatbot_using_llama_3_1_405b | Building a powerful chatbot using Llama 3 1 405B]] for lead generation on your website to qualify leads and answer questions using a RAG knowledge base is made accessible through Chatlink <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Getting Started with Chatlink

To begin, visit chatlink.com and click "start for free" <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Chatlink offers a generous free tier, allowing users to build a few chatbots and conduct dozens of conversations to ensure the lead generation agent meets their needs <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

Upon signing in, you'll access a dashboard with various resources <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>:
*   **API Documentation**: Manage agents, knowledge bases, and conversations programmatically <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Roadmap**: View current development, upcoming features, and submit your own suggestions <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This indicates an actively evolving platform <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

## Creating a Chatbot (Agent)

To create an agent within your project, navigate to the "My Agents" tab and click "Create Chatbot" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. You are presented with three template options <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>:
1.  **AI Chatbot**: A basic chatbot not necessarily geared towards lead generation <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
2.  **Basic Lead Generation Chatbot**: Does not leverage AI, answering standard questions <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
3.  **Lead Generation Plus AI Chatbot**: Offers an intelligent interaction with the user for qualification and recommendations <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

You can also start from scratch <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>, but using the "Lead Generation Plus AI Chatbot" template is recommended for quickly understanding Chatlink <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

### The Builder Interface

The core of [[building_a_no_code_website_chatbot | chatbot creation]] in Chatlink is the "Builder" tab, which features a node workflow builder <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. This is similar to platforms like VectorShift or Voiceflow <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. A workflow starts when a message is first received and ends when the chat concludes within the widget <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. The workflow represents an entire conversation and can include looping for multiple questions <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

### Workflow Blocks and Variables

Any action or user input handling, such as making an HTTP request for a custom agent, is done using "widgets" or "blocks" available on the left-hand side <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. These blocks allow you to:
*   Send hard-coded messages <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   Get AI responses <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   Add buttons for user interaction <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   Capture user input into custom variables <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   Perform HTTP requests <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   Send emails <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   Set conditions to handle different user responses <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   Manage all variables on the left-hand side <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   Configure AI settings, including the model (e.g., GPT-4o mini) and knowledge base <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

## Building a Lead Generation Agent Example

An example workflow for a lead generation agent (e.g., for an AI consulting agency) demonstrates the following stages <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>:

1.  **Greeting**: Display an image (like a logo) and send multiple greeting messages consecutively <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
2.  **Initial Qualification**: Ask the user about their interest in specific services (e.g., solution development, one-on-one consulting, pre-made agents) using buttons <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. The user's choice is saved into a `selected_service_name` variable <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
3.  **Contextual Follow-up**: The system prompts the large language model, stating the lead's interest and asking for follow-up questions to understand their needs better <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. User outputs are captured into variables (e.g., `first_question_answer`), maintaining conversation context <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
4.  **Looping for Questions**: After a short qualification process, the agent asks if the user has any questions, providing "Yes" or "No" buttons <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. If "Yes," the user is prompted to ask, and the answer is generated using a [[customizing_chatbot_with_rag | RAG knowledge base]] <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. The workflow then loops back to ask if they have more questions, ensuring all queries are addressed <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
5.  **Contact Information Collection**: If the user has no more questions, the agent collects their name and email, which are stored as a contact record within Chatlink, functioning as a basic CRM <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. A concluding "thank you" message is sent <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

## Knowledge Base (RAG)

Chatlink's knowledge base feature is crucial for [[customizing_chatbots_for_business_needs | customizing chatbots for business needs]] and enabling them to answer questions based on your specific data <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. Various data sources can be ingested for Retrieval-Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>:
*   **Website Link**: Crawl a website to extract information <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
*   **Sitemap**: Ideal for e-commerce stores, allowing the bot to understand all product URLs <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Custom URL List**: Up to 2,000 links can be included <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
*   **Documents**: Upload files <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Raw Text**: Input free-form text directly <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   **FAQs**: A list of question-answer pairs for common queries <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. When a user asks a related question, the AI retrieves and customizes the answer from the FAQs <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

## Customization and Integration

Chatlink offers extensive options for [[customizing_chatbots_for_business_needs | customizing chatbots for business needs]] and appearance <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>:
*   **Appearance**: Customize the chat widget to match your branding, including styling and the AI's image <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. This level of customization is often missing in other platforms <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
*   **Conversations**: Monitor all ongoing conversations with your bot. It can tie conversations to users, saving their email and phone number, effectively acting as a simple CRM <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

### Website Integration

To integrate the chatbot with your website, use the website widget integration <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>. There are three display options <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>:
*   **Floating Chat**: The common small widget in the bottom right corner of a website <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
*   **Inline**: The chat is embedded as part of the web page itself <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.
*   **Full Screen**: The chat takes up the entire page <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

The integration is done by embedding a script tag into virtually any website builder <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. Integration guides are available for platforms like Shopify, WordPress, and Wix <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>, but it can also be used with Go High Level or custom Next.js sites <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.

### Other Integrations

Chatlink also integrates with Zapier, allowing for actions like transferring collected contact information <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>. Additionally, the platform supports HTTP requests, enabling integration with any external API <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>. This means you can hook into custom agents hosted on platforms like n8n or LangServe as part of your Chatlink workflow <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.

## Conclusion

Chatlink provides a powerful and customizable solution for [[integrating_chatbots_with_website | integrating chatbots with website]] for lead generation <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>. It is particularly useful for businesses like e-commerce stores, agencies, or consulting firms <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>. By using Chatlink, businesses can avoid the time and complexity of [[using_folder_for_chatbot_creation | building a chatbot from scratch]] while still achieving a robust and tailored agent <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>. The solution doesn't sacrifice customizability and is suitable for front-facing chatbots that don't handle private data locally <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.