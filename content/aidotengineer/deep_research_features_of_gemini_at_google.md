---
title: Deep research features of Gemini at Google
videoId: eJOjdjO45Sc
---

From: [[aidotengineer]] <br/> 

Deep Research is a personal [[design_challenges_in_building_web_research_agents | research agent]] available on Gemini Advanced (1.5 Pro) [00:00:41] that can browse the web to build reports on a user's behalf [00:00:51]. It allows Gemini to take as long as needed, up to 5 minutes, to browse the web for a comprehensive answer [00:02:01].

## Motivation for Building Deep Research

The motivation behind Deep Research was to help people "get smart fast" [00:01:08]. Research and learning queries are top use cases in Gemini [00:01:13]. However, traditional chatbots often provide a blueprint for an answer rather than the actual answer itself when faced with hard questions [00:01:20]. For example, asking about athletic scholarships for shot put would yield generic advice like "talk to coaches" or "have good grades," instead of specific details like grade boundaries or throw distances [00:01:30]. Deep Research aims to provide super comprehensive answers to such queries [00:01:53].

## Product Challenges and User Experience (UX) Solutions

Building Deep Research presented several product challenges:
*   **Synchronous vs. Asynchronous Experience**: Gemini is an inherently synchronous chatbot [00:02:22]. The team needed to build asynchronous experiences within this synchronous product [00:02:28].
*   **Setting User Expectations**: Deep Research is designed for specific, complex queries [00:02:35], unlike common requests for weather or jokes where a 5-minute wait is inappropriate [00:02:40].
*   **Engaging with Long Outputs**: Reports can be thousands of words long [00:02:47], requiring a way for users to easily engage with extensive content in a chat experience [00:02:51].

These challenges were addressed through the UX design:
*   **Research Plan Card**: When a query is made, Gemini first puts together a research plan presented in a card [00:03:22]. This communicates that the experience is different [00:03:28] and allows users to edit and steer the research direction, similar to how a good analyst would [00:03:36].
*   **Transparency of Browsing**: After initiation, Gemini shows the websites it is browsing in real time [00:03:56], providing transparency into the model's activity [00:04:08]. Users can click through these websites while waiting [00:04:12].
*   **Engaging with Long Reports (Artifacts)**: Inspired by Anthropic's artifacts, Deep Research allows users to "pin" the long report [00:04:37]. This enables users to ask questions about the research while reading the material without needing to scroll back and forth [00:04:49]. This feature makes it easy to change report style, add/remove sections, or ask follow-up questions [00:04:53].
*   **User Trust and Source Citation**: The system always shows all sources read and used in the report [00:05:08]. Not everything read is used, but it stays in context for follow-up questions [00:05:13] and can be exported to Google Docs as citations [00:05:19].

## Technical Challenges in Building a [[design_challenges_in_building_web_research_agents | Research Agent]]

Building a [[design_challenges_in_building_web_research_agents | research agent]] involves several core technical challenges [00:05:31]:

### Long-Running Nature of Tasks
Tasks running for multiple minutes and involving many LLM calls and service interactions are prone to failures [00:06:17]. Future [[design_challenges_in_building_web_research_agents | research agents]] could take multiple hours [00:06:32].
*   **Robustness to Intermediate Failures**: It's crucial to be robust to failures from various services with different reliabilities [00:06:36]. This requires a good state management solution and effective error recovery to prevent dropping the entire research task due to one failure [00:06:44].
*   **Cross-Platform Enablement**: The long-running nature enables cross-platform use, where users can register research tasks, walk away, and get notified on different devices when the task is complete [00:06:55].

### Iterative Planning and Effective Compute Usage
The model needs to plan iteratively and use its time and compute effectively [00:05:49], especially when interacting with the noisy web environment [00:05:58].
*   **Parallel vs. Sequential Sub-problems**: The model must determine which facets of a query can be tackled in parallel and which require sequential processing [00:07:40].
*   **Grounding on Partial Information**: The model frequently encounters states with partial information [00:07:58]. It must evaluate all information found so far before deciding the next step [00:08:02]. For instance, finding D1 qualifying standards for shot put means the model needs to then seek out D2 and D3 equivalents [00:08:09]. Similarly, if searching for "best roller coaster for kids" yields a "top 10 roller coasters" link without mentioning suitability for kids, the planner must recognize this and resolve the ambiguity in subsequent steps [00:08:34].
*   **Information Fragmentation**: Information is often spread across different sources [00:09:10]. The model must weave together facets from multiple sources to provide a complete picture, such as combining certification structure from one source with pricing from another for a scuba diving course [00:09:17].
*   **Entity Resolution**: The system must be able to reason about information indicators to determine if mentions of the same entity across different sources refer to the same entity, or if further exploration is needed to verify [00:09:50].
*   **Robust Browsing Mechanism**: The web is fragmented, with varying website layouts [00:10:14]. A robust browsing mechanism is essential for navigating the web effectively for research tasks [00:10:34].

### Effective Context Management
As the [[design_challenges_in_building_web_research_agents | research agent]] gathers streams of information during planning, its context size grows very quickly [00:10:46].
*   **Follow-up Queries**: Research tasks often don't end with the first query; users have follow-ups, adding pressure on the context [00:11:02].
*   **Strategies for Context Management**: While Gemini has long context models [00:11:20], effective context management is still necessary [00:11:26]. One strategy involves a recency bias, keeping more information about current and previous tasks, and selectively picking "research notes" from older tasks into a RAG (Retrieval Augmented Generation) system, allowing the model to access it selectively [00:11:37].

## What's Next for [[design_challenges_in_building_web_research_agents | Research Agents]]

The positive reception to Deep Research, which performs similarly to a McKinsey analyst [00:12:21], highlights the potential for future [[design_challenges_in_building_web_research_agents | research agents]] [00:14:42]. Future directions include:
*   **Enhanced Expertise**: Moving beyond simple aggregation and synthesis to mimic higher levels of expertise, like a McKinsey or Goldman Sachs partner [00:12:44]. This involves thinking through implications, "so what," and identifying the most interesting insights and patterns [00:12:54]. In sciences, this means reading many papers, forming hypotheses, finding patterns, and generating novel hypotheses [00:13:08].
*   **Personalization and Usefulness**: Making the output useful by personalizing the information presentation based on the user's role and needs [00:13:23]. For example, a due diligence report for a general user would focus on strategic positioning, while for a Goldman Sachs banker, it would include financial models and detailed financial analysis [00:13:30]. This personalization should shape how the agent browses the web, frames answers, and pursues questions [00:13:57].
*   **Multi-modal Capabilities**: Combining web research with other model abilities like coding, data science, and even video generation [00:14:11]. For a due diligence example, this could mean performing statistical analysis and building financial models to inform the research output [00:14:21].