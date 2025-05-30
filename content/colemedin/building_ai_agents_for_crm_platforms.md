---
title: Building AI agents for CRM platforms
videoId: 1lvAvLXXA10
---

From: [[colemedin]] <br/> 

## The Gold Mine Niche: GoHighLevel

Recently, a significant niche for [[building_ai_agents | AI agents]] has been identified within the platform GoHighLevel, offering opportunities to create Software as a Service (SaaS) products or provide consultancy services to businesses <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. GoHighLevel is a comprehensive CRM (Customer Relationship Management) system designed specifically for marketing agencies <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. It provides a vast suite of tools to streamline operations such as landing pages, lead capture and nurturing, email campaigns, invoicing, marketing automations, Google reviews, and appointment scheduling <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Why GoHighLevel is an Ideal Platform

While GoHighLevel offers a broad range of functionalities, it is described as a "jack of all trades, master of none" <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This characteristic creates substantial opportunities to extend its capabilities, especially in the realm of AI <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. Although GoHighLevel has begun integrating AI, its current implementations have fallen short <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

Key features that make GoHighLevel attractive for AI agent development include:
*   **Robust API** The platform boasts an "incredible API" that makes extending its functionality straightforward, appearing as if it were built with developers in mind <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This API is consistently updated and improved <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **App Marketplace** GoHighLevel encourages custom app development through its app Marketplace, simplifying processes like authentication, API integration, webhook setup for event handling, and permission management for secure applications <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Extensive User Base** Thousands of businesses operate by leveraging GoHighLevel and its features, indicating a large market for extensions and improvements <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

The combination of a powerful API and an encouraging app marketplace makes it an ideal environment for developers to create specialized [[AI agents]] <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. A 14-day free trial is available for those interested in exploring the platform and identifying opportunities for AI integration <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## Lead Nurturing: A Prime Opportunity for AI Agents

One of the most significant opportunities for [[building_ai_agents | AI agents]] within GoHighLevel is in lead nurturing <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Marketing agencies prioritize reaching as many leads as possible, quickly, and with high personalization <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. [[AI agents]] are perfectly suited for personalized lead nurturing at scale, capable of handling numerous conversations with individuals who have provided their information through ads or landing pages <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

The goal of these conversations could be to encourage product purchases, schedule appointments, or book events <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This need is universal across diverse businesses, from solar panel companies to chiropractic offices, all of which rely on nurturing leads <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## Practical Implementation: An AI Agent for Lead Nurturing

An example of an [[AI agent]] built for lead nurturing in GoHighLevel utilizes LangChain, LangGraph, and Pinecone for RAG (Retrieval-Augmented Generation) <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### App Creation in GoHighLevel Marketplace

Creating an app in the GoHighLevel Marketplace involves a simple process:
1.  Navigate to the 'Apps' section <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
2.  Click to create a new app, providing a name and setting its visibility (private or public) <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
3.  For private apps, internal use within an agency is common <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. Public apps can be marketed to other agencies as a full-fledged SaaS <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

### Webhook Setup

A critical aspect of integration is setting up webhooks within the app settings <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. By providing a webhook URL (e.g., a Google Cloud function URL), the app can send requests to a custom endpoint whenever specific events occur, such as inbound or outbound SMS messages <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This endpoint then triggers the [[AI agent]] to handle messages, acting as a lead nurturing bot <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### AI Agent Backend Overview

The backend of such an [[AI agent]] typically includes:
*   **Endpoints:**
    *   A webhook endpoint for receiving text messages from GoHighLevel <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
    *   An emulator endpoint for testing different agents <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
    *   An endpoint to update the knowledge base (vector database like Pinecone) for FAQs <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   **Multi-Agency Support:** The application allows different agencies, each with their GoHighLevel accounts, to connect various [[AI agents]] to their respective clients (sub-accounts) <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. This enables configuration of custom agents with unique prompts, models, and temperatures for each client <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
*   **Agent Determination:** When a text message arrives, the system authenticates it, fetches the company (agency) and location (contact/sub-account) IDs, and determines which [[AI agent]] applies to that contact through tagging in GoHighLevel automation workflows <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
*   **LangGraph Executable:** The core of the AI agent is a full LangGraph executable that performs lead nurturing <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. It integrates various tools to interact with GoHighLevel:
    *   Add/Remove tags <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>
    *   Invoke generic webhooks for custom actions <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>
    *   Fetch calendar availability <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>
    *   Cancel/Book appointments <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>
    *   These tools enable a full conversation cycle leading to bookings or product purchases <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **Dynamic Prompting:** The platform allows defining custom actions using natural language, instructing the large language model when to use specific tools <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. Prompts are built dynamically, incorporating elements such as:
    *   Retrieval-Augmented Generation (RAG) using a vector database for FAQs <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
    *   Extra context about the location (address, phone number) <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
    *   Injected actions (tools) <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.
    *   Date information to prevent hallucinations <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.
    *   Time zone information <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.
    *   Base prompt with goals and constraints <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
    This creates a "massively useful prompt" for the LangGraph executable to generate responses and trigger necessary tool calls <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.

The underlying code, primarily in JavaScript, is part of an [[AI agents masterclass GitHub repo | AI agents masterclass GitHub repository]] <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. This detailed implementation allows for robust and unique lead nurturing conversations tailored to specific business needs <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. Further extensions could include tools for requesting Google reviews after appointments <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.

This niche for [[integrating_ai_agents_with_live_platforms | building AI agents on GoHighLevel]] offers significant value both for developers creating SaaS products and for businesses seeking to enhance their operations <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.