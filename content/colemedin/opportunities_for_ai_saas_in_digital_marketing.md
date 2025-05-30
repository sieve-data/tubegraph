---
title: Opportunities for AI SaaS in digital marketing
videoId: 1lvAvLXXA10
---

From: [[colemedin]] <br/> 

Recently, a significant niche has emerged for building [[building_ai_agents_for_crm_platforms | AI agents]] within the GoHighLevel platform, offering opportunities for creating Software as a Service (SaaS) products or providing consultancy services to businesses <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This niche is considered a "gold mine" due to its potential for generating substantial revenue <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## GoHighLevel: A Core Platform for Marketing Agencies

GoHighLevel is a comprehensive Customer Relationship Management (CRM) platform primarily designed for marketing agencies <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. It provides a vast suite of tools to help agencies streamline various operations, including:
*   Landing page creation <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>
*   [[ai_for_lead_generation | Lead capture]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>
*   [[ai_in_marketing_and_lead_nurturing | Lead nurturing]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>
*   Email campaigns <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>
*   Invoicing <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>
*   Marketing automations <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>
*   Google reviews management <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
*   Appointment scheduling <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>

### Why GoHighLevel is Ideal for AI Agents

While GoHighLevel offers extensive features, it tends to be a "jack of all trades but a master of none," particularly concerning [[integrations_and_collaboration_in_ai_platforms | AI integrations]] <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. This presents a significant opportunity for developers to build [[building_ai_agents_for_crm_platforms | AI agents]] that enhance its functionality <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

Key reasons GoHighLevel is a perfect platform for AI agent development:
*   **Widespread Adoption**: Thousands of businesses operate entirely around GoHighLevel and its features, indicating a large existing market <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>.
*   **Functionality Gaps**: There are many opportunities to extend its core functionality, especially where its native [[integrations_and_collaboration_in_ai_platforms | AI capabilities]] fall short <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>.
*   **Robust API**: GoHighLevel provides an "incredible API" that makes it very easy to extend the platform, resembling a developer-first platform with constant updates and improvements <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.
*   **Custom App Marketplace**: The platform encourages developers to create custom applications through its app Marketplace <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. This marketplace simplifies:
    *   Handling authentication for SaaS products <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>
    *   Integrating with the GoHighLevel API <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>
    *   Setting up webhooks to manage platform events <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>
    *   Managing permissions for app security <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>

This combination of a vast user base, functional gaps in AI, and developer-friendly tools creates a "perfect storm" for building [[building_ai_agents_for_crm_platforms | AI agents]] <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>.

## [[AI in marketing and lead nurturing | AI Agents for Lead Nurturing]]

One of the most significant opportunities is in building [[ai_in_marketing_and_lead_nurturing | AI agents for lead nurturing]] <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. Digital marketing prioritizes speed, volume, and personalization in reaching leads <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>. [[AI in marketing and lead nurturing | AI]] excels at achieving personalized lead nurturing at scale, by facilitating numerous conversations with individuals who have provided their information <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. The goal of nurturing leads can be to encourage product purchases, schedule appointments, or book events <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>. This need is universal across diverse businesses, from solar panel companies to chiropractic offices <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.

### Example: A Lead Nurturing AI Agent ("Textually")

An example [[AI in marketing and lead nurturing | AI agent]] created for [[ai_in_marketing_and_lead_nurturing | lead nurturing]] within GoHighLevel utilizes Langchain, Langgraph, and Pinecone for Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.

#### Technical Implementation Overview
1.  **App Creation**: Developers can create a private or public app in the GoHighLevel Marketplace <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.
2.  **Webhook Setup**: A webhook URL (e.g., a Google Cloud function URL) is configured within the app's settings <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>. This endpoint receives requests whenever an inbound or outbound SMS message occurs <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>.
3.  **Backend Processing**:
    *   The Google Cloud function endpoint receives the webhook request <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>.
    *   It performs authentication and fetches the company ID (agency) and location ID (contact/sub-account) <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>.
    *   The agent tied to a specific contact is determined through tagging in GoHighLevel automation workflows <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>. Different tags allow for different [[building_ai_agents_for_crm_platforms | AI agents]] and nurturing approaches based on lead source or specific needs <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.
    *   Agencies can connect different [[building_ai_agents_for_crm_platforms | AI agents]] to their various clients (sub-accounts) within the platform, configuring custom prompts, models, and temperatures for each <a class="yt-timestamp" data-t="08:46:00">[08:46:00]</a>.
4.  **Langgraph Executable**: The system sends the message and context to a full Langgraph executable that handles the lead nurturing <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>. This executable integrates with GoHighLevel via various tools:
    *   Adding and removing tags <a class="yt-timestamp" data-t="11:09:00">[11:09:00]</a>
    *   Invoking generic webhooks for custom actions <a class="yt-timestamp" data-t="11:15:00">[11:15:00]</a>
    *   Fetching calendar availability <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>
    *   Canceling and booking appointments <a class="yt-timestamp" data-t="11:37:00">[11:37:00]</a>
5.  **Dynamic Prompt Building**: For every agent, custom actions can be defined using natural language to instruct the Large Language Model (LLM) when to use specific tools <a class="yt-timestamp" data-t="11:55:00">[11:55:00]</a>. The prompt is dynamically built, incorporating:
    *   FAQs from a Vector database (Pinecone) for common questions <a class="yt-timestamp" data-t="12:57:00">[12:57:00]</a>
    *   Extra context about the location (address, phone number) <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>
    *   The defined actions <a class="yt-timestamp" data-t="13:18:00">[13:13:00]</a>
    *   Date information to prevent hallucinations <a class="yt-timestamp" data-t="13:23:00">[13:23:00]</a>
    *   Time zone data <a class="yt-timestamp" data-t="13:32:00">[13:32:00]</a>
    *   A base prompt with goals and constraints configured in the front end <a class="yt-timestamp" data-t="13:37:00">[13:37:00]</a>

This robust application allows for highly customized conversation flows that cater to unique business needs <a class="yt-timestamp" data-t="13:30:00">[13:30:00]</a>. All the necessary actions for a full conversation leading to bookings or product purchases are handled by these tools <a class="yt-timestamp" data-t="11:42:00">[11:42:00]</a>.

The backend code for this [[building_ai_agents_for_crm_platforms | AI agent]] is available in a public GitHub repository under the "go highlevel SAS backend" folder within an "AI agents masterclass" repo <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>.