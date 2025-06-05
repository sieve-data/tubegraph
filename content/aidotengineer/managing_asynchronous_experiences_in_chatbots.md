---
title: Managing asynchronous experiences in chatbots
videoId: eJOjdjO45Sc
---

From: [[aidotengineer]] <br/> 

Building web research agents like Gemini Deep Research presents unique challenges, particularly when integrating long-running, asynchronous tasks into an inherently synchronous chatbot product <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## Core Challenges

### Synchronous Nature of Chatbots
Traditional chatbots are designed for quick, synchronous interactions, where a response is expected almost immediately after a query <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Deep research, however, can take several minutes to complete <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>, requiring a fundamental shift in how the user experience is managed <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### Setting User Expectations
It's crucial to differentiate research queries, which benefit from longer processing times, from simple queries (e.g., weather, jokes) where a five-minute wait would be unacceptable <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Users need to understand that the product is performing a different kind of task <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### Handling Long Outputs
Research reports can be thousands of words long <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Designing an interface that allows users to easily engage with and navigate such extensive content within a chat experience is vital <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## Solutions Implemented by Gemini Deep Research

### The Research Plan Card
To manage user expectations and introduce the asynchronous nature of Deep Research, Gemini first presents a "research plan" in a card format <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This step communicates that the experience is different from a standard chatbot interaction <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. It also allows users to review, edit, and steer the direction of the research, much like collaborating with an analyst <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Real-time Progress Transparency
Once the research begins, Gemini provides real-time transparency by showing the websites it is browsing <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This feature, developed before "thinking models" and "thoughts" became common, helps users understand what the model is doing under the hood <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Users can click through the websites and explore the content while waiting <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

### Engaging with Long Reports via Artifacts
Inspired by Anthropic's "artifacts," Gemini allows users to "pin" the generated long report <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This enables users to ask follow-up questions about the research directly while reading the material without needing to scroll back and forth <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. This design makes it easier to change the report's style, add/remove sections, or ask further questions <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

### Source Attribution and Trust
To build user trust and respect publishers, Deep Research always displays all sources read and used in the report <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. Even sources read but not directly used in the final report remain in context for potential follow-up questions <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. This information can also be exported to Google Docs with citations <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

## Technical Considerations for Asynchronous Agents

### Robustness to Failures
Long-running tasks, which involve many LLM calls and interactions with various services, are prone to failures <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. For a research agent that can take minutes or even hours <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>, it's critical to be robust to intermediate failures <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. This requires:
*   **State Management:** Building a strong state management solution <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **Error Recovery:** Effectively recovering from errors to avoid dropping the entire research task due to a single failure <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

### Cross-Platform Continuity
The asynchronous nature allows users to initiate a research task, walk away, and then be notified when it's complete <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. This capability enables cross-platform access, allowing users to pick up and read the report on different devices <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

### Iterative Planning with Partial Information
The model must iteratively plan its actions, deciding which sub-problems to tackle in parallel versus sequentially <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. It frequently operates with partial information and must constantly re-evaluate its next steps based on new findings <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. This means grounding its next steps on the information it has found so far <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. For example, if it finds D1 scholarship standards, it then needs to plan to find D2 and D3 standards <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

### Managing Context Growth
As the research progresses and streams of information are gathered, the context size can grow very quickly <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. This is further compounded by follow-up queries or requests to research related topics <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. Even with long context models like Gemini, effective context management strategies are essential <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. One approach involves a recency bias, where more information is kept about current and previous tasks, while older tasks are selectively summarized into "research notes" that the model can still access through a retrieval-augmented generation (RAG) system <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

## Future Directions for Research Agents

The success of systems like Deep Research opens doors for future advancements in [[ai_agents_beyond_chat_gpt | AI agents]]:

*   **Deeper Expertise:** Moving beyond aggregating and synthesizing information to provide expert-level insights, implications, and novel patterns, akin to a McKinsey partner or Goldman Sachs partner <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>. This could involve complex tasks like forming hypotheses in scientific research <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
*   **Personalized Experience and Presentation:** Tailoring information delivery based on the user's role and needs <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. For instance, a due diligence report for a general user would differ significantly from one for a Goldman Sachs banker, influencing how the web is browsed and the answer is framed <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. This speaks to the broader concept of [[building_user_experiences_with_ai | building user experiences with AI]].
*   **Multimodal Capabilities:** Combining web research with other AI capabilities like coding, data science, and even video generation <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>. This could involve an agent performing statistical analysis or building financial models to inform its research output <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.