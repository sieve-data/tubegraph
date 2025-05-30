---
title: Market trends and future goals in AI
videoId: Fe4Svx-UFqs
---

From: [[customaistudio]] <br/> 

This article provides an update on a company's recent growth, operational changes, and future roadmap, focusing on their experiences building over 26 AI agent projects in 60 days <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. The insights shared cover market response, business model evolution, and the practicalities of [[developing_ai_agents_and_their_market_potential | developing AI agents]].

## Rapid Growth and Market Engagement

Following a period of silence, the company experienced significant growth driven by a viral YouTube video posted on August 6th <a class="yt-timestamp" data-t="01:57">[01:57]</a>. This video, which garnered 172,000 viewers, led to an immediate surge in interest, with 37 intro calls booked in a single week <a class="yt-timestamp" data-t="02:00">[02:00]</a>, <a class="yt-timestamp" data-t="02:30">[02:30]</a>. The success was attributed to striking the market at a time when there was high curiosity about AI agents, but a lack of clear understanding regarding their capabilities, limitations, and business applications <a class="yt-timestamp" data-t="02:47">[02:47]</a>.

This rapid influx of clients necessitated a swift expansion of the team beyond the initial two founders <a class="yt-timestamp" data-t="03:48">[03:48]</a>, <a class="yt-timestamp" data-t="04:34">[04:34]</a>.

## Operational Streamlining and Process Development

Initially, the company relied on disparate tools like Slack for client communication, Trello for project tracking, and Google Drive for file storage <a class="yt-timestamp" data-t="06:50">[06:50]</a>. Recognizing the need for efficiency, they are centralizing operations into a single platform called Motion, which provides dedicated client portals and direct communication channels for developers <a class="yt-timestamp" data-t="07:35">[07:35]</a>.

The delivery process for AI agent builds has also been streamlined <a class="yt-timestamp" data-t="08:23">[08:23]</a>. A key learning was the difficulty in accurately scoping [[challenges_in_ai_prompt_engineering_and_development | AI agent]] systems due to the inherent R&D and testing involved with Large Language Models (LLMs) <a class="yt-timestamp" data-t="09:02">[09:02]</a>. To address this, they adopted a "proof of concept" (POC) approach, aiming to get a basic working version of the desired agent system to the client within seven days <a class="yt-timestamp" data-t="09:31">[09:31]</a>. This approach improves client relationships and ensures alignment on the project's direction <a class="yt-timestamp" data-t="09:38">[09:38]</a>.

### Sales and Marketing Funnel

The current sales and marketing funnel is simple and relies heavily on organic content from YouTube and LinkedIn <a class="yt-timestamp" data-t="10:47">[10:47]</a>. Interested parties are directed to a landing page where they can join a community or book a call <a class="yt-timestamp" data-t="11:05">[11:05]</a>. The sales process typically involves one to two calls, leading to a quick close for straightforward agent builds <a class="yt-timestamp" data-t="11:21">[11:21]</a>.

### Client Demographics

The company has engaged with a wide range of clients and interested parties, including:
*   Solo founders and startup teams <a class="yt-timestamp" data-t="13:54">[13:54]</a>
*   Small businesses (online services, professional services, home services) <a class="yt-timestamp" data-t="13:59">[13:59]</a>
*   Investors and publicly traded companies <a class="yt-timestamp" data-t="14:16">[14:16]</a>
*   Mid-market companies <a class="yt-timestamp" data-t="14:23">[00:14:23]</a>
*   Big Four consulting firms <a class="yt-timestamp" data-t="14:34">[14:34]</a>
*   [[current_trends_in_ai_agent_platforms | Channel Partners]] interested in reselling services <a class="yt-timestamp" data-t="14:57">[14:57]</a>
*   Developers and job seekers <a class="yt-timestamp" data-t="16:11">[16:11]</a>

## Key AI Agent Projects and Learnings

The company has developed a variety of AI agent systems for diverse business needs. A fundamental learning has been the non-deterministic nature of LLMs, leading to the development of strategies to enhance reliability, such as converting text to plain text before hitting the LLM and implementing conversational error handling between agents and tools <a class="yt-timestamp" data-t="23:02">[23:02]</a>, <a class="yt-timestamp" data-t="24:50">[24:50]</a>.

### Project Examples
*   **Inbox Agent:** Cross-references incoming Gmail with a CRM and takes actions like labeling or notifying <a class="yt-timestamp" data-t="17:31">[17:31]</a>.
*   **Newsletter Agent:** Extracts, summarizes, and organizes newsletters from a specific email label into a Google Doc <a class="yt-timestamp" data-t="17:57">[17:57]</a>.
*   **Email Agent:** Configured to perform various email actions based on prompts <a class="yt-timestamp" data-t="18:47">[18:47]</a>.
*   **Lead Qualification Agent:** Gathers contact history from HubSpot and past messages to qualify leads and respond to inquiries <a class="yt-timestamp" data-t="19:04">[19:04]</a>.
*   **Reporting Agent:** Analyzes sales call transcripts (upserted into a vector database) to generate reports based on client criteria <a class="yt-timestamp" data-t="19:40">[19:40]</a>.
*   **Slack Agent:** Uses the same sales call vector database to enable natural language interaction about sales calls <a class="yt-timestamp" data-t="20:26">[20:26]</a>.
*   **Lead Enrichment Agent:** Scrapes websites and LinkedIn profiles for leads from Excel sheets, identifying decision-makers <a class="yt-timestamp" data-t="21:10">[21:10]</a>.
*   **Scrape LinkedIn Profile Tool:** A custom tool, emphasizing the need for API marketplaces like RapidAPI for external data scraping <a class="yt-timestamp" data-t="21:44">[21:44]</a>.
*   **SEO Agent:** Writes SEO-optimized descriptions and FAQs, reformatting output into a Google Sheet <a class="yt-timestamp" data-t="22:31">[22:31]</a>.
*   **Inbox Sorting Agent:** Sorts emails, with different setups for deterministic sorting (e.g., support inbox) versus personal inboxes <a class="yt-timestamp" data-t="25:29">[25:29]</a>.
*   **Lead Nurturing Agent:** Pulls leads from HubSpot, gets message history, and generates personalized emails in the user's style <a class="yt-timestamp" data-t="26:55">[26:55]</a>.
*   **Voice Reception Agent:** Advanced voice agents capable of transferring calls, seeking information, and even generating and sending reports during a live call <a class="yt-timestamp" data-t="28:08">[28:08]</a>. This includes after-hours call services <a class="yt-timestamp" data-t="29:04">[29:04]</a> and a voice call sales trainer <a class="yt-timestamp" data-t="29:09">[29:09]</a>.

A prevalent pattern observed is the request for Retrieval Augmented Generation (RAG) agents, where clients want to populate a vector database with their specific data (e.g., sales call transcripts, emails, company wikis) to enable natural language querying and analysis by an LLM <a class="yt-timestamp" data-t="29:21">[29:21]</a>. These RAG agents often serve as a foundation upon which additional capabilities, such as email sending or CRM updates, can be built <a class="yt-timestamp" data-t="30:23">[30:23]</a>.

## Business Model and Offers

The company's business model has evolved to address the complexities of [[challenges of building a SaaS in the emerging AI market | AI agent development and ongoing maintenance]] <a class="yt-timestamp" data-t="30:50">[30:50]</a>.

*   **AI Agent Development Partner:** This is the primary offer, where the company acts as an extension of a client's team. Instead of one-time builds, they provide dedicated AI agent developers on a flat-rate, month-to-month basis to continually build, maintain, and improve bespoke AI agent systems <a class="yt-timestamp" data-t="31:02">[31:02]</a>. This approach addresses scope creep and ensures the application of the latest learnings to client projects <a class="yt-timestamp" data-t="31:17">[31:17]</a>.
*   **Hosted Agents:** These are pre-built, ready-to-implement agents. Clients incur an initial implementation cost followed by a small monthly fee for hosting, management, and maintenance <a class="yt-timestamp" data-t="32:57">[32:57]</a>. The company handles integrations, data flow, and prompt configuration <a class="yt-timestamp" data-t="34:25">[34:25]</a>.
*   **SaaS Products:** The company is exploring building traditional self-service SaaS products for specific, single-use case agent systems in particular niches <a class="yt-timestamp" data-t="34:49">[34:49]</a>.
*   **Community:** A community platform has been soft-launched, initially free for discussion. It will later transition to a paid model, offering course modules and tutorial videos that delve deeper into the AI stack, RAG concepts, LLM mechanics, and advanced agent building techniques <a class="yt-timestamp" data-t="05:00">[05:00]</a>, <a class="yt-timestamp" data-t="35:40">[35:40]</a>. The tutorials focus on new learnings and best practices for building robust multi-agent systems and ensuring reliable tool calling <a class="yt-timestamp" data-t="36:47">[36:47]</a>.
*   **Other Revenue:** Includes affiliate fees from recommended tools and YouTube ad revenue <a class="yt-timestamp" data-t="37:30">[37:30]</a>.

## Roadmap and Future Vision

The company's long-term goal is to make a significant, exponential impact on the AI space <a class="yt-timestamp" data-t="38:23">[38:23]</a>. The "Northstar" is to contribute to the creation of the first [[future_of_ai_and_human_integration_in_business | one-person billion-dollar company]] by building the necessary AI systems <a class="yt-timestamp" data-t="39:06">[39:06]</a>, a concept often discussed by figures like Sam Altman <a class="yt-timestamp" data-t="39:15">[39:15]</a>. They believe this could be possible by 2026-2027 <a class="yt-timestamp" data-t="42:02">[42:02]</a>.

They acknowledge that no one yet knows the definitive "best way" to build agents, and new technologies are continuously emerging <a class="yt-timestamp" data-t="39:24">[39:24]</a>. OpenAI's developments, such as `01` (a new reasoning approach for GPT-4) and `Agency Swarm` (focused on function calling and structured outputs), indicate their clear direction towards providing tools for agent development <a class="yt-timestamp" data-t="39:30">[39:30]</a>, <a class="yt-timestamp" data-t="40:55">[40:55]</a>.

The company sees their role as taking these foundational tools the "last mile" – practically implementing them into business environments to provide 10x to 1000x leverage on employees or the business <a class="yt-timestamp" data-t="41:09">[41:09]</a>, contributing to the "Playbook" for AI implementation <a class="yt-timestamp" data-t="41:43">[41:43]</a>. The reasoning capabilities of GPT-4 and GPT-4o have been crucial, and further advancements like `01` API access for function calling are expected to make agents even more reliable <a class="yt-timestamp" data-t="42:42">[42:42]</a>.

The company is actively operating as a "lab," experimenting with new tools and architectures to build a solid playbook for implementing AI in any business <a class="yt-timestamp" data-t="44:10">[44:10]</a>. The year 2025 is anticipated to bring even more intense attention and excitement to the AI space <a class="yt-timestamp" data-t="43:50">[43:50]</a>.