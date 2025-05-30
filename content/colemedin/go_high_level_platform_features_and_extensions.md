---
title: Go High Level platform features and extensions
videoId: 1lvAvLXXA10
---

From: [[colemedin]] <br/> 

Go High Level is a comprehensive Customer Relationship Management (CRM) platform designed primarily for marketing agencies <a class="yt-timestamp" data-t="00:28:03">[00:28:03]</a>. It provides a vast suite of tools aimed at streamlining various agency operations, including landing pages, lead capture and nurturing, email campaigns, invoicing, marketing automations, Google reviews, and appointment scheduling <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>.

## Why Go High Level is a Niche for AI Agents

While Go High Level is an "amazing platform" that acts as a "jack of all trades," it also presents opportunities because it's not a "master of none" in every area <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. This creates gaps in functionality that can be filled by extensions, particularly through the integration of AI agents <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>. Although Go High Level has recently incorporated some AI features, it has "definitely fallen short" <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

The platform is built to support a large ecosystem, with "thousands of businesses" operating on it and leveraging its features <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.

### Enabling Extensions and Custom Apps

Go High Level offers a robust Application Programming Interface (API) that makes it exceptionally easy to extend the platform's functionality <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. Its API is described as so good that it feels like a "developer first platform," consistently updated and improved <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

Furthermore, Go High Level's App Marketplace facilitates the creation of custom applications <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. This encourages developers to build solutions that integrate seamlessly with the platform <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>. [[developing_custom_apps_with_go_high_level_api | Marketplace apps simplify handling authentication]], [[developing_custom_apps_with_go_high_level_api | integrating with the API]], setting up webhooks to manage platform events, and managing permissions for enhanced security <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.

This combination of an established platform, its extensibility, and the encouragement for developers creates a "perfect storm" for building AI agents to enhance existing features <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. A 14-day free trial is available for exploration, encouraging developers to find opportunities for AI extensions <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>.

## AI Agents for Lead Nurturing

One of the most significant applications for AI agents within Go High Level is personalized lead nurturing <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. Digital marketing prioritizes speed, volume, and personalization when reaching out to leads <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>. AI agents are an ideal solution for personalized lead nurturing at scale, enabling numerous conversations with individuals who have provided their information through ads or landing pages <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. The goal is to drive specific actions, such as product purchases, appointment scheduling, or event bookings <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>. This need for lead nurturing is universal across diverse businesses, from solar panel companies to chiropractic offices and personal trainers <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.

### Creating a Custom AI Agent for Lead Nurturing

The speaker developed an [[incorporating_ai_agents_and_advanced_development_features | AI agent]] for lead nurturing within Go High Level, utilizing LangChain, LangGraph, and Pinecone for Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.

#### Go High Level App Marketplace Setup
To create an app in the Go High Level Marketplace, developers access the "Apps" section and click "Create New App" <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>. Apps can be configured as private (for internal agency use) or public (for a broader Software as a Service - SaaS - offering) <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.

A crucial feature is the easy setup of webhooks <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>. By providing a webhook URL (e.g., a Google Cloud function URL) and selecting trigger events (like inbound or outbound SMS messages), the custom code can handle these requests <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>. This allows the AI agent to manage incoming and outgoing messages, acting as the lead nurturing bot <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>.

#### Backend Architecture and Logic
The backend of the AI agent is primarily handled by a Google Cloud Function that receives webhook requests from the Go High Level app <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>. Key steps include:
1.  **Authentication:** The system performs authentication upon receiving a request <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>.
2.  **ID Fetching:** It fetches the company ID (agency) and location ID (client sub-account) associated with the message <a class="yt-timestamp" data-t="09:42:00">[09:42:00]</a>.
3.  **Agent Determination:** The system determines which AI agent applies to a specific contact based on tagging set up through automation workflows in Go High Level <a class="yt-timestamp" data-t="09:52:00">[09:52:00]</a>. This allows for diverse agents with different prompts, models, and temperatures for various clients or even different lead sources within one client <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.
4.  **LangGraph Integration:** The determined agent's information is sent to a full LangGraph executable, which performs the lead nurturing <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>.

#### Tools and Dynamic Prompting
The LangGraph executable incorporates various tools that interact with the Go High Level API to perform necessary actions <a class="yt-timestamp" data-t="10:54:00">[10:54:00]</a>. These tools include:
*   Adding and removing tags <a class="yt-timestamp" data-t="11:09:00">[11:09:00]</a>
*   Invoking generic webhooks for custom events <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>
*   Fetching calendar availability <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>
*   Canceling and booking appointments <a class="yt-timestamp" data-t="11:37:00">[11:37:00]</a>

The platform allows agencies to define custom actions using natural language, instructing the large language model (LLM) when to use these tools <a class="yt-timestamp" data-t="11:55:00">[11:55:00]</a>. This ensures the conversation flow is tailored to unique client needs <a class="yt-timestamp" data-t="12:20:00">[12:20:00]</a>.

The prompts for the AI agents are built dynamically, incorporating:
*   **RAG (Retrieval Augmented Generation):** Queries a vector database (Pinecone) to include FAQs, enabling the agent to answer common questions <a class="yt-timestamp" data-t="12:57:00">[12:57:00]</a>.
*   **Extra Context:** Information about the client's location (address, phone number) <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>.
*   **Actions:** The custom actions defined for the agent <a class="yt-timestamp" data-t="13:18:00">[13:18:00]</a>.
*   **Date Information:** To prevent hallucinations and ensure accurate scheduling <a class="yt-timestamp" data-t="13:23:00">[13:23:00]</a>.
*   **Time Zone:** Critical for accurate scheduling <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a>.
*   **Base Prompt:** Defines the agent's goals and constraints <a class="yt-timestamp" data-t="13:37:00">[13:37:00]</a>.

This comprehensive prompt is then fed into the LangGraph executable to generate responses and trigger necessary tool calls, such as booking an appointment <a class="yt-timestamp" data-t="13:53:00">[13:53:00]</a>. The code for this backend is available in a GitHub repository <a class="yt-timestamp" data-t="14:51:00">[14:51:00]</a>. Further enhancements could include tools to request Google reviews after appointments <a class="yt-timestamp" data-t="14:38:00">[14:38:00]</a>.