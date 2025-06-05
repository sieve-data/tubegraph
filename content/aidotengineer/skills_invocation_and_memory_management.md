---
title: Skills Invocation and Memory Management
videoId: n9rjuBuShko
---

From: [[aidotengineer]] <br/> 

LinkedIn's Generative AI (GenAI) platform evolved significantly to support complex AI applications, with key investments made in areas like [[importance_of_tool_calling_in_ai | tool calling]] (or skills invocation) and [[memory_management_in_ai | memory management]] <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>, <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. The platform classifies these components into four layers: orchestration, prompt engineering, tools and skills invocation, and content and [[memory_management_in_ai | memory management]] <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>, <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>, <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>, <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

## Skills Invocation (Tools and Skills)

In the era of AI agents, skills or APIs are a crucial aspect, as agents are expected to perform specific actions <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>, <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>, <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. LinkedIn made a significant investment in a "skill registry" to facilitate this <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

### Skill Registry
The skill registry provides a set of [[challenges_and_considerations_in_tool_creation_and_execution | tools]] that allow developers to publish their APIs into a centralized repository <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>, <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>, <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. This registry addresses key challenges:
*   **Skill Discovery** <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>
*   **Skill Invocation** <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>

By centralizing skills, it becomes very easy for applications to call APIs and perform tasks <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>, <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>, <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

The ability to uplift APIs into skills that can be easily called by agents is considered a critical new component for the agent era, requiring surrounding [[challenges_and_considerations_in_tool_creation_and_execution | tooling]] and infrastructure support <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>, <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>, <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>, <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>, <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>, <a class="yt-timestamp" data-t="00:15:58">[00:15:58]].

## Memory Management

[[memory_management_in_ai | Memory management]] is a crucial component for injecting rich data into the agent experience <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>, <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>, <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>, <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>, <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

### Conversational Memory
Initial platform capabilities included "conversational memory" infrastructure, which helps track LLM interactions and retrieval content. This content is then injected into the final product to enable conversational bots <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>, <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>, <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>, <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>, <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>, <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>, <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Experiential Memory
Beyond conversational memory, the platform expanded its capabilities to include "experiential memory" <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>, <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>, <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. This is a memory storage system designed to extract, analyze, and infer factual knowledge from interactions between the agent and the user <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>, <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>, <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>, <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

Memory is organized into different layers to help agents be aware of surrounding content <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>, <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>, <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>, <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>, <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. These layers include:
*   Working memory <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>
*   Long-term memory <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>
*   Collective memories <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>

LinkedIn has found success leveraging its existing messaging infrastructure to serve as a cost-efficient and scalable memory layer <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>, <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>, <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>, <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>, <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>.