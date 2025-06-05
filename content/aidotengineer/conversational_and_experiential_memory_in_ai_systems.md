---
title: Conversational and experiential memory in AI systems
videoId: n9rjuBuShko
---

From: [[aidotengineer]] <br/> 

## Evolution of Memory in LinkedIn's Generative AI Platform

Initially, LinkedIn's generative AI (GenAI) product experience focused on simple prompt-in, string-out applications, such as collaborative articles utilizing the GPT-4 model <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. This first generation, while leveraging models like GPT-4, lacked the capability to inject rich data into the product experience <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

### Conversational Memory

In mid-2023, as LinkedIn developed its second generation of GenAI products, internally known as "co-pilot" or "coach," a critical component emerged: [[Stateful Agents and AI Memory Management | conversational memory]] <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Purpose**: This infrastructure helps to keep track of Large Language Model (LLM) interactions and retrieved content, injecting this information into the final product <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   **Application**: It is crucial for building conversational bots <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>, enabling personalized recommendations, such as suggesting job fits based on a user's profile and job description via a Retrieval Augmented Generation (RAG) process <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

### Experiential Memory

With the launch of LinkedIn's first multi-agent system, the "LinkedIn H assistant," the platform extended its memory capabilities beyond just conversational memory <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Definition**: [[Stateful Agents and AI Memory Management | Experiential memory]] is a memory storage system designed to extract, analyze, and infer factual knowledge from interactions between an agent and its users <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Structure**: This memory is organized into different layers, including:
    *   Working memory <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>
    *   Long-term memory <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>
    *   Collective memories <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>
*   **Benefit**: These layers help the agent become aware of the surrounding content, enhancing its autonomy and decision-making <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. Agents, by definition, are autonomous, deciding which APIs and LLMs to call <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

## Role of Memory in the GenAI Platform Architecture

Memory management is classified as one of the four core layers of the GenAI platform, alongside orchestration, prompt engineering, and tools/skills invocation <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   [[Memory management and delegation in AI | Memory]] is a critical component for injecting rich data into the agent experience <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
*   LinkedIn has leveraged its existing messaging infrastructure as a memory layer, proving to be both cost-efficient and scalable <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.

The overarching goal of the GenAI platform is to provide a unified interface for a complex ecosystem, enabling developers to easily access various components without needing to understand every individual part <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. This includes simplified model switching and reduced infrastructure integration complexity <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.