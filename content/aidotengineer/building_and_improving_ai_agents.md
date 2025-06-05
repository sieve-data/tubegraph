---
title: Building and Improving AI Agents
videoId: 0vBKv9yAQi4
---

From: [[aidotengineer]] <br/> 

Sierra is a conversational AI platform designed for businesses <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. While initially known for chat and customer service, Sierra is expanding its offerings to include phone interactions, sales, subscription management, and product recommendations <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. The company focuses on [[developing_and_optimizing_ai_agents | building and improving AI agents]] as a core product, recognizing that every agent is a product that requires a robust development and operations platform <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

## Historical Context of AI Development

The speaker reflects on the rapid pace of AI development, noting how recent milestones (2019-2023) are often perceived as "ancient history" <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. His own experience dates back to 2016, a period he refers to as the "AI caves" <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

In 2016, working at Google, the focus was on computer vision tasks like distinguishing between Chihuahuas and blueberry muffins, or dogs and bagels <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This work laid the foundation for Google Lens, which in its infancy was primarily good at identifying plants <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Initial testing of these early models often felt like a "slot machine" due to inconsistent accuracy <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

### Evolution of Google Lens
Today, Google Lens has evolved significantly, allowing users to:
*   Search and shop what they see on various platforms like Google Images and YouTube <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   Translate non-Latin character sets <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   Solve math homework <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   Still identify flowers <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

This progress is attributed to consistent, step-by-step iteration over a decade, emphasizing the need for a process similar to the [[software_development_life_cycle | software development life cycle]] to continuously improve without regressing <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### Software Eating the World
The presentation references Mark Andreessen's 2012 essay, "Software is eating the world," to set the stage for the growth of software-driven businesses <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. An example of a successful software-centric startup from that era is Chubbies, known for its online presence and customer-focused approach <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

## Partnering with AI Agents: The Chubbies Example

Chubbies recognized the growing need for businesses to have an [[importance_and_progress_of_ai_agents | AI agent]] to represent them and assist customers by 2025 <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. They partnered with Sierra to create their AI agent, "Duncan Smothers" <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

Duncan Smothers, available on the Chubbies website, is designed to be highly capable and engaging, handling various customer inquiries:
*   **Sizing and Fit**: Empathetically helps customers with sizing questions and offers product recommendations <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   **Inventory Tracking**: Informs customers about stock availability and helps them choose new items <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **Package Tracking and Refunds**: Provides multiple tracking numbers for orders and can issue refunds <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

These examples demonstrate autonomous actions taken by the agent, leading to improved customer support: more customers helped, more quickly, and with higher satisfaction <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

Sierra's approach involves dedicated agent engineering and product management teams who work closely with customers like Chubbies to ensure the best results <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

## The Agent Development Life Cycle (ADLC)

Sierra has developed its own process, the Agent Development Life Cycle (ADLC), for [[developing_and_optimizing_ai_agents | building and improving AI agents]] <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. While it borrows concepts from the traditional [[software_development_life_cycle | software development life cycle]], it addresses the unique [[challenges_in_developing_ai_agents | challenges in developing AI agents]] with Large Language Models (LLMs).

### Challenges with LLMs
Traditional software is deterministic, fast, cheap, rigid, and governed by strict logic. In contrast, LLMs can be:
*   Non-deterministic <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
*   Slow <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   Expensive to run <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   Flexible, creative, and capable of reasoning <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.

The ADLC is designed to leverage the strengths of LLMs while integrating traditional software where beneficial <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

### Iterative Refinement and Quality Assurance
A key aspect of ADLC is iterative refinement with customers in production <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. This includes:
*   **Sierra's Experience Manager**: Allows customers to review every conversation, monitor agent performance in real-time, and provide feedback <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.
*   **Issue Reporting and Testing**: If an issue arises (e.g., incorrect inventory information), it leads to an issue being filed, a test being created, and a new release once the test passes <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. This ensures that agents progressively accumulate more tests, from a handful at launch to hundreds and thousands over time <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   **"Delight Budget"**: Agents are empowered to go "above and beyond" for customers, such as arranging for products to be delivered from a retail location if unavailable online <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.

Initially, these processes were manual, but with advancements in AI, Sierra is increasingly able to apply AI to each part of the ADLC, accelerating improvements <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

### Scalability and External Factors
The ADLC becomes more effective with larger customer bases, especially those handling tens of millions of requests <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. Changes impacting the ADLC come from various sources:
*   Agent performance issues <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.
*   Model upgrades <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.
*   New paradigms like reasoning models <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
*   Multimodality <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.

Reasoning models act as a "force multiplier," enabling more effective application of AI to development, testing, and QA steps within the ADLC <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.

## Building for Voice AI Agents
Sierra launched its voice capabilities in October, with large customers like SiriusXM benefiting from the ability to answer customer calls immediately <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

Sierra conceptualizes voice capabilities similarly to responsive web design: under the hood, it's the same agent code and platform, but it's "responsive" to the channel (e.g., chat, phone) and modality (e.g., text, voice) of interaction <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>. Customization for layout, phrasing, and parallelized requests for lower latency are still possible <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.

## Empathy in AI Design
[[challenges_in_building_reliable_ai_agents | Building reliable AI agents]] with LLMs is complex because LLMs, in their unpredictability, slowness, and mathematical limitations, remind us of ourselves <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. This offers an opportunity for designers to develop empathy, allowing them to put themselves in the "shoes of the robot" to build better experiences <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. The goal is to create robust AI agents that can process complex inputs and experiences similar to humans <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.