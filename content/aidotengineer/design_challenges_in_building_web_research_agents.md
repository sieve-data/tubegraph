---
title: Design challenges in building web research agents
videoId: eJOjdjO45Sc
---

From: [[aidotengineer]] <br/> 

Google's Deep Research feature within Gemini Advanced aims to address the challenge of providing comprehensive answers to complex research and learning queries that traditional chatbots struggle with <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Unlike general chatbots that might offer a "blueprint" for an answer, Deep Research is designed to deliver a full, detailed report by extensively browsing the web <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This requires the system to operate with fewer constraints on compute and latency, taking up to five minutes to generate a thorough response <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## [[Design challenges for AI agents | Product Challenges]] and Solutions

Building Deep Research presented several [[Design challenges for AI agents | product challenges]] due to Gemini's inherently synchronous chatbot nature <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Challenges
*   **Asynchronous Experience**: Integrating a long-running, asynchronous feature into a synchronous chatbot product <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   **Setting User Expectations**: Differentiating Deep Research for complex queries from quick requests like weather updates or jokes, where a five-minute wait is inappropriate <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   **Engaging with Long Outputs**: Designing an interface that allows users to easily interact with reports that can be thousands of words long <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

### UX Solutions
To address these challenges, the following user experience (UX) elements were implemented:

*   **Research Plan Card**: When a query is submitted, Gemini first generates and presents a research plan in a card <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. This immediately signals that this is not a standard chatbot interaction and allows users to review and even edit the plan, similar to how an analyst would present their approach <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Real-time Browsing Display**: As the research progresses, the system shows the websites Gemini is browsing in real time <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This provides transparency and allows users to click through to the sources while they wait. An unexpected side effect was users attempting to "game" the system by pushing the number of browsed websites into the thousands <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   **Pinned Report (Artifact)**: Inspired by Anthropic's artifacts, the final report is pinned, enabling users to ask follow-up questions about the research directly within the chat interface without needing to scroll back and forth <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This facilitates changing the report's style, adding or removing sections, and continuing the conversation <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   **Source Citation**: To build user trust and support publishers, Deep Research always displays all sources read and specifically those used in the report <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. Even sources read but not directly used are kept in context for potential follow-up questions and are carried over as citations if the report is exported to Google Docs <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## [[Design challenges for AI agents | Technical Challenges]] in Building a Research Agent

Developing a web research agent like Deep Research involves several significant [[Design challenges for AI agents | technical challenges]]:

### Long-Running Nature of Tasks
Research tasks can run for multiple minutes, making many LLM calls and service interactions <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. This introduces the inevitability of failures <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Robustness to Failures**: It's crucial to build a robust system that can handle intermediate failures of various services with differing reliabilities <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **State Management and Error Recovery**: Effective state management and error recovery are essential to prevent the entire research task from failing due to a single component error <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **Cross-Platform Enablement**: The ability to register research tasks, walk away, and receive notifications across different devices allows users to pick up where they left off <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

### Iterative Planning and Compute Management
The agent's model must plan iteratively and efficiently manage its time and computational resources <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Parallel vs. Sequential Problem Solving**: The model needs to determine which sub-problems within a query can be tackled in parallel and which require sequential processing <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Handling Partial Information**: The agent frequently encounters situations with partial information. It must be able to assess all information found so far before deciding on the next steps, grounding its plans on discovered data <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. For instance, if it finds D1 division standards for a scholarship, it needs to recognize the need to find D2 and D3 equivalents <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. Similarly, if a search yields a "top 10" list without mentioning suitability for kids, the planner must recognize this ambiguity and plan to resolve it <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
*   **Information Aggregation**: Information is often spread across multiple sources <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. The model must weave together facets of information from different websites to form a complete picture, such as combining certification steps from one source with pricing from another <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
*   **Entity Resolution**: The classic problem of identifying if mentions across different sources refer to the same entity is critical, requiring the model to reason about information indicators or explore further to verify <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

### Interacting with a Noisy Web Environment
The web is a fragmented and noisy environment <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   **Robust Browsing Mechanism**: Websites have varied layouts and structures. A robust browsing mechanism is necessary for effective navigation and information extraction, regardless of the website's design <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

### Context Management
As the agent processes information, especially in long-running tasks, the context size can grow rapidly <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Handling Follow-up Queries**: Research tasks often involve follow-up questions or new topics, adding further pressure on context management <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   **Long Context Models**: While Gemini has access to long context models, effective management strategies are still needed <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. One approach involves a recency bias, keeping more detailed information about current and previous tasks, while selectively extracting "research notes" for older tasks to be accessed via a retrieval-augmented generation (RAG) system <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

## [[Future directions for research agents | Future Directions for Research Agents]]

The success of Deep Research suggests significant potential for future development in [[future_of_browser_agents_and_technological_advancements | research agents]] <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. Key directions include:

*   **Expertise**: Moving beyond aggregation and synthesis to provide deeper insights, implications, and novel patterns, akin to a "Mackenzie partner" or expert in scientific domains who can form hypotheses <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
*   **Personalization**: Tailoring information presentation and the research process itself (browsing, framing answers, questions pursued) to the specific user and their needs <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. For example, a due diligence report for a general user would differ from one for a Goldman Sachs banker <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
*   **Multimodality**: Combining web research with other capabilities such as coding, data science, or video generation to enrich research outputs, like performing statistical analysis or building financial models to inform a business due diligence report <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.