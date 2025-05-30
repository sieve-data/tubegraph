---
title: Using AI to handle customer queries
videoId: 1I0PvfHjaRE
---

From: [[colemedin]] <br/> 

Artificial Intelligence (AI) offers practical applications for businesses, particularly in managing customer interactions and generating leads. While many AI ideas can be impractical, a proven use case is a lead generation agent that operates on a website to handle customer queries and business operations even when staff are unavailable <a class="yt-timestamp" data-t="00:00:00"></a>.

## Benefits of AI Lead Generation Agents
An AI lead generation agent can perform several crucial tasks:
*   **Lead qualification** <a class="yt-timestamp" data-t="00:00:20"></a>
*   **Answering questions** <a class="yt-timestamp" data-t="00:00:21"></a>
*   **Suggesting products or resources** <a class="yt-timestamp" data-t="00:00:22"></a>
*   **Collecting contact information for follow-ups** <a class="yt-timestamp" data-t="00:00:25"></a>

## Building Your Own vs. Using Platforms
The use of AI for lead generation is common, and numerous platforms exist for building such agents <a class="yt-timestamp" data-t="00:00:29"></a>. However, many of these platforms are considered inadequate due to a lack of customizability <a class="yt-timestamp" data-t="00:00:36"></a>. An alternative is to [[understanding_ai_agents | build the agent yourself]] using tools like n8n or LangChain <a class="yt-timestamp" data-t="00:00:40"></a>. Building from scratch can be a non-trivial process <a class="yt-timestamp" data-t="00:01:17"></a>.

Fortunately, some effective platforms are available that provide the necessary customizability <a class="yt-timestamp" data-t="00:00:50"></a>.

## Chatlink: A Platform for AI Lead Generation Agents
Chatlink is presented as an example of a platform that enables users to [[integrating_ai_chatbots_on_websites | build a full lead generation agent]] tailored to specific business needs <a class="yt-timestamp" data-t="00:00:59"></a>. This agent can sit on a website, qualify leads, and answer questions using a RAG (Retrieval-Augmented Generation) knowledge base <a class="yt-timestamp" data-t="00:01:05"></a>.

### Getting Started with Chatlink
To begin using Chatlink, users can visit their website and access a generous free tier that allows building multiple chatbots and having dozens of conversations to ensure the agent meets their requirements <a class="yt-timestamp" data-t="00:01:28"></a>.

Upon signing in, users are directed to a dashboard offering various resources, including:
*   **API documentation:** For managing agents, knowledge bases, and conversations programmatically <a class="yt-timestamp" data-t="00:02:00"></a>.
*   **Roadmap:** Shows current platform developments, suggestions being taken, and allows users to submit their own <a class="yt-timestamp" data-t="00:02:08"></a>.

### Creating an AI Agent
Within a project, users can create a chatbot by choosing from three main options <a class="yt-timestamp" data-t="00:02:30"></a>:
1.  **AI Chatbot:** A basic chatbot <a class="yt-timestamp" data-t="00:02:35"></a>.
2.  **Basic Lead Generation Chatbot:** Does not leverage AI for responses, using standard pre-set answers <a class="yt-timestamp" data-t="00:02:44"></a>.
3.  **Lead Generation Plus AI Chatbot:** Features intelligent interactions with users for qualification and recommendations <a class="yt-timestamp" data-t="00:02:50"></a>.

Users can also start from scratch, but using a template (like the Lead Generation Plus AI chatbot template) is recommended for quick understanding and building <a class="yt-timestamp" data-t="00:03:02"></a>.

### Workflow Builder
Chatlink utilizes a node workflow builder, similar to platforms like VectorShift or Voiceflow <a class="yt-timestamp" data-t="00:03:37"></a>. A workflow represents an entire conversation, starting with an initial message and ending when the chat widget closes <a class="yt-timestamp" data-t="00:03:51"></a>. Workflows can include looping to allow for multiple questions and answers <a class="yt-timestamp" data-t="00:04:03"></a>.

**Workflow Components (Widgets/Blocks):**
Actions and user input handling are managed using widgets on the left-hand side <a class="yt-timestamp" data-t="00:04:16"></a>:
*   **Text Blocks:** Send hard-coded messages <a class="yt-timestamp" data-t="00:04:44"></a>.
*   **Capture Text:** Wait for user responses and store them in custom variables <a class="yt-timestamp" data-t="00:05:05"></a>.
*   **AI Response:** Generate responses from a large language model (LLM) using variables as prompts <a class="yt-timestamp" data-t="00:05:22"></a>.
*   **Buttons:** Provide pre-defined options for user interaction (e.g., "yes" or "no" choices), which offer robustness not easily implemented in tools like n8n's chat widget <a class="yt-timestamp" data-t="00:05:53"></a>.
*   **HTTP Requests:** Enable the bot to make custom API calls, including headers and body, to interact with external services or custom agents hosted on platforms like n8n or LangServe <a class="yt-timestamp" data-t="00:05:46"></a>.
*   **Conditions:** Handle different types of user responses <a class="yt-timestamp" data-t="00:05:49"></a>.
*   **Sending Emails:** Integrate email communication into the workflow <a class="yt-timestamp" data-t="00:05:48"></a>.
*   **Variables:** Managed on the left-hand side, allowing for dynamic content and context within the conversation <a class="yt-timestamp" data-t="00:06:00"></a>.

Every element placed within a lighter gray box in the builder represents an individual message sent to the user <a class="yt-timestamp" data-t="00:06:29"></a>. Images can be displayed at the start of a conversation, such as a company logo <a class="yt-timestamp" data-t="00:06:36"></a>.

### Knowledge Base (RAG)
The knowledge base feature is crucial for enabling the AI to answer questions <a class="yt-timestamp" data-t="00:10:29"></a>. Chatlink allows ingestion from various resources for its RAG system <a class="yt-timestamp" data-t="00:10:31"></a>:
*   **Website Link:** Crawls a website to gather information <a class="yt-timestamp" data-t="00:10:40"></a>.
*   **Sitemap:** Excellent for e-commerce stores, as it can go through all product URLs to answer specific questions about them <a class="yt-timestamp" data-t="00:10:50"></a>.
*   **Custom URL List:** Supports up to 2,000 links for RAG <a class="yt-timestamp" data-t="00:11:03"></a>.
*   **Documents:** Upload various document types <a class="yt-timestamp" data-t="00:11:07"></a>.
*   **Raw Text:** Free-form text input for knowledge <a class="yt-timestamp" data-t="00:11:09"></a>.
*   **FAQs:** Allows inputting question-and-answer pairs for common queries <a class="yt-timestamp" data-t="00:11:13"></a>.

The AI can match user questions to the knowledge base content and customize the answer to fit the conversation context <a class="yt-timestamp" data-t="00:15:45"></a>.

### Customization and Integrations
Chatlink provides extensive customization options for the chat widget's appearance, allowing it to match business branding <a class="yt-timestamp" data-t="00:11:44"></a>. Users can change styling, images for the AI avatar, and more <a class="yt-timestamp" data-t="00:11:59"></a>.

The platform also acts as a basic CRM by recording conversations and saving user contact information (name, email, phone) <a class="yt-timestamp" data-t="00:12:09"></a>. This enables businesses to follow up with leads <a class="yt-timestamp" data-t="00:12:20"></a>.

For [[integrating_ai_with_front_ends | website integration]], Chatlink offers three embedding options <a class="yt-timestamp" data-t="00:12:48"></a>:
*   **Floating Chat:** A common widget in the bottom right corner of a website <a class="yt-timestamp" data-t="00:12:50"></a>.
*   **Inline:** The chat widget is part of the webpage content <a class="yt-timestamp" data-t="00:12:54"></a>.
*   **Full Screen:** The chat takes up the entire browser window <a class="yt-timestamp" data-t="00:12:56"></a>.

The integration is done by embedding a script tag, compatible with various website builders like Shopify, WordPress, Wix, GoHighLevel, or custom Next.js sites <a class="yt-timestamp" data-t="00:13:08"></a>. Chatlink also [[ai_voice_systems_and_integration | integrates with Zapier]] for actions like sending contact information, though n8n is not a direct integration <a class="yt-timestamp" data-t="00:12:38"></a>.

The ability to make HTTP requests within workflows allows users to connect to virtually any external API, making the platform highly extensible for [[building_ai_agents_for_crm_platforms | custom AI agents]] or specific business logic <a class="yt-timestamp" data-t="00:17:13"></a>.

## Conclusion
Using platforms like Chatlink for lead generation AI agents on websites is highly useful for businesses, especially e-commerce stores, agencies, or consulting firms <a class="yt-timestamp" data-t="00:18:03"></a>. These platforms save time that would otherwise be spent building a robust agent from scratch, while still providing significant customizability without needing a local solution or handling private data <a class="yt-timestamp" data-t="00:18:12"></a>.