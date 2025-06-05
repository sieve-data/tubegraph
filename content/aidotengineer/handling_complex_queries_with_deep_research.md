---
title: Handling complex queries with deep research
videoId: eJOjdjO45Sc
---

From: [[aidotengineer]] <br/> 

Deep Research, a feature available on Gemini Advanced, is designed to address the challenges of answering complex research and learning queries that traditional chatbots often struggle with <a class="yt-timestamp" data-t="01:13:15">[01:13:15]</a>. It functions as a personal research agent capable of browsing the web to build comprehensive reports on behalf of the user <a class="yt-timestamp" data-t="00:51:38">[00:51:38]</a>.

## Motivation for Deep Research

The primary motivation behind building Deep Research was to help users "get smart fast" <a class="yt-timestamp" data-t="01:08:16">[01:08:16]</a>. While research queries are a top use case for Gemini, bringing hard questions to general chatbots often results in a "blueprint for an answer" rather than a comprehensive one <a class="yt-timestamp" data-t="01:20:07">[01:20:07]</a>. For instance, a query about athletic scholarships for shot put might yield generic advice like "talk to coaches" or "have good grades," instead of specific details such as grade boundaries or throwing distances <a class="yt-timestamp" data-t="01:28:16">[01:28:16]</a>.

The goal was to remove constraints on compute and latency, allowing Gemini to take as long as needed (up to 5 minutes) to browse the web and provide a much more comprehensive answer <a class="yt-timestamp" data-t="01:57:02">[01:57:02]</a>.

## Product Challenges and Solutions

Building Deep Research within an inherently synchronous chatbot product like Gemini presented several [[design_challenges_in_building_web_research_agents | product challenges]] <a class="yt-timestamp" data-t="02:19:35">[02:19:35]</a>:

*   **Asynchronous Experience:** Integrating a long-running research task into a real-time chat interface <a class="yt-timestamp" data-t="02:28:01">[02:28:01]</a>.
*   **Setting User Expectations:** Differentiating Deep Research from quick queries like "what's the weather" where a 5-minute wait is not appropriate <a class="yt-timestamp" data-t="02:34:04">[02:34:04]</a>.
*   **Engaging with Long Outputs:** Making it easy for users to interact with reports that can be thousands of words long <a class="yt-timestamp" data-t="02:47:01">[02:47:01]</a>.

To overcome these, the following user experience (UX) and user interface (UI) solutions were implemented:

1.  **Research Plan Card:** Upon receiving a complex query, Gemini first presents a research plan in a card format <a class="yt-timestamp" data-t="03:22:04">[03:22:04]</a>. This communicates that the experience is different from a standard chatbot and allows users to edit and steer the direction of the research <a class="yt-timestamp" data-t="03:37:11">[03:37:11]</a>.
2.  **Real-Time Browsing Transparency:** While Deep Research is working, it shows the websites it is browsing in real-time, providing transparency into the model's actions <a class="yt-timestamp" data-t="03:56:06">[03:56:06]</a>. Users can click through these websites while waiting <a class="yt-timestamp" data-t="04:12:02">[04:12:02]</a>.
3.  **Pinned Reports (Artifacts):** For long outputs, the generated report can be pinned like an artifact, allowing users to ask questions about the research while reading the material without scrolling back and forth <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>. This also facilitates changing the report's style, adding/removing sections, or asking follow-up questions <a class="yt-timestamp" data-t="04:53:23">[04:53:23]</a>.
4.  **Source Citation:** Deep Research always displays all sources read and used in the report, building user trust and acknowledging publishers. These sources can be exported as citations to Google Docs <a class="yt-timestamp" data-t="05:03:09">[05:03:09]</a>.

## Technical Challenges in Building Research Agents

Building a [[practical_project_creating_a_deep_research_clone | web research agent]] involves significant [[design_challenges_in_building_web_research_agents | technical challenges]] <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>:

### 1. Long-Running Nature of Tasks
Research tasks can run for multiple minutes or even hours, making many LLM calls and service interactions <a class="yt-timestamp" data-t="06:17:01">[06:17:01]</a>.
*   **Robustness to Failures:** It's crucial to be robust to intermediate failures of various services, ensuring the entire research task isn't dropped due to a single failure <a class="yt-timestamp" data-t="06:36:08">[06:36:08]</a>. This requires effective state management and error recovery <a class="yt-timestamp" data-t="06:44:11">[06:44:11]</a>.
*   **Cross-Platform Enablement:** The long-running nature allows users to initiate tasks and receive notifications across devices, enabling them to pick up reading the results later <a class="yt-timestamp" data-t="06:58:08">[06:58:08]</a>.

### 2. Iterative Planning and Compute Effectiveness
The model must plan iteratively and effectively manage its time and compute resources <a class="yt-timestamp" data-t="05:49:09">[05:49:09]</a>.
*   **Parallel vs. Sequential Problem Solving:** For multi-faceted queries (e.g., athletic scholarships), the model must determine which sub-problems can be tackled in parallel versus those that are inherently sequential <a class="yt-timestamp" data-t="07:40:02">[07:40:02]</a>.
*   **Handling Partial Information:** The model frequently lands in states with partial information. It must assess all information found so far before deciding the next step <a class="yt-timestamp" data-t="07:58:24">[07:58:24]</a>. For example, if it finds D1 division standards for shot put, it then needs to plan to find D2 and D3 equivalents <a class="yt-timestamp" data-t="08:08:12">[08:08:12]</a>.
*   **Information Disambiguation:** When search results provide partial or ambiguous information (e.g., "top 10 roller coasters" without mentioning kid-friendliness), the planner must recognize this and plan further steps to resolve the ambiguity <a class="yt-timestamp" data-t="08:44:10">[08:44:10]</a>.
*   **Weaving Dispersed Information:** Information for a single answer is often spread across different sources. The model must weave these facets together, like combining scuba diving certification structure from one source with pricing from another <a class="yt-timestamp" data-t="09:10:04">[09:10:04]</a>.
*   **Entity Resolution:** Identifying if mentions of the same entity across different sources refer to the same thing, requiring reasoning about information indicators or further exploration <a class="yt-timestamp" data-t="09:50:09">[09:50:09]</a>.

### 3. Interacting with a Noisy Web Environment
The web is fragmented and inconsistent <a class="yt-timestamp" data-t="10:14:14">[10:14:14]</a>.
*   **Robust Browsing:** A robust browsing mechanism is essential to navigate varied website layouts and extract information effectively for research tasks <a class="yt-timestamp" data-t="10:34:04">[10:34:04]</a>.

### 4. Effective Context Management
As the model performs research and receives streams of information, its context size grows very quickly <a class="yt-timestamp" data-t="10:49:05">[10:49:05]</a>.
*   **Follow-up Queries:** Research tasks typically involve follow-up questions, adding further pressure on the context <a class="yt-timestamp" data-t="11:04:14">[11:04:14]</a>.
*   **Selective Information Retention:** While models like Gemini have long contexts, effective management strategies are crucial. One approach involves a recency bias, retaining more information for current and previous tasks, while selectively picking "research notes" from older tasks and putting them into a Retrieval Augmented Generation (RAG) system so the model can still access them <a class="yt-timestamp" data-t="11:37:07">[11:37:07]</a>.

## Future Directions for Research Agents

Future developments for research agents, including [[deep_research_features_of_gemini_at_google | Gemini's Deep Research]], are envisioned in several key areas <a class="yt-timestamp" data-t="13:36:06">[13:36:06]</a>:

*   **Expertise:** Moving beyond aggregation and synthesis to providing deeper insights, implications, and novel hypotheses, akin to a "Mackenzie partner" or "Goldman Sachs partner" <a class="yt-timestamp" data-t="12:40:02">[12:40:02]</a>. This could apply to professional services or scientific domains <a class="yt-timestamp" data-t="13:03:04">[13:03:04]</a>.
*   **Personalization:** Customizing the way information is browsed, framed, and presented based on the user's specific role and needs (e.g., presenting financial due diligence differently to a general user versus a banker) <a class="yt-timestamp" data-t="13:31:07">[13:31:07]</a>.
*   **Multimodal Capabilities:** Combining web research with other model abilities such as coding, data science, or video generation to enrich research outputs (e.g., building financial models or statistical analyses to inform due diligence) <a class="yt-timestamp" data-t="14:11:04">[14:11:04]</a>. This aligns with [[developing_custom_ai_tools_and_functions | developing custom AI tools and functions]].