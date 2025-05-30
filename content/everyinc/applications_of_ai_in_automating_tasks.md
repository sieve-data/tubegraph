---
title: Applications of AI in automating tasks
videoId: 864X81BuQbI
---

From: [[everyinc]] <br/> 

AI is profoundly changing how individuals and businesses approach task automation, enabling new levels of productivity and efficiency. This shift is driven by the capabilities of large language models (LLMs) and the development of sophisticated AI agents [[enhancing_productivity_with_ai_tools | AI tools]] <a class="yt-timestamp" data-t="01:57:57">[01:57:57]</a>.

## Personal Productivity and Workflows
Yohi Nakajima, a general partner at Untapped Capital and a prominent AI tinkerer, highlights that his motivation for building AI tools stems from a desire to automate repetitive tasks and improve his workflow <a class="yt-timestamp" data-t="01:42:07">[01:42:07]</a>. He describes himself as "really lazy" and constantly asks how he can eliminate disliked tasks from his work <a class="yt-timestamp" data-t="01:46:17">[01:46:17]</a>. Before AI, he was a heavy user of no-code tools like Zapier, but LLMs have "unlocked so much" in terms of automating tasks <a class="yt-timestamp" data-t="01:57:57">[01:57:57]</a>.

Key aspects of this personal approach include:
*   **Targeting specific tasks** <a class="yt-timestamp" data-t="02:01:59">[02:01:59]</a>.
*   **Iterative development** <a class="yt-timestamp" data-t="02:02:04">[02:02:04]</a>.
*   **Working with fragmented attention** <a class="yt-timestamp" data-t="02:21:18">[02:21:18]</a>: Yohi builds at night and on weekends, often in short bursts while doing other chores or waiting to pick up kids <a class="yt-timestamp" data-t="01:48:48">[01:48:48]</a>. He uses tools like ChatGPT and Replet on his phone to copy-paste code, run it, and respond to errors incrementally <a class="yt-timestamp" data-t="02:07:22">[02:07:22]</a>. This allows him to act as a "manager" of his code, checking in when needed <a class="yt-timestamp" data-t="02:24:07">[02:24:07]</a>.

## Autonomous Agents and Self-Building Tools
The development of autonomous agents marks a significant leap in AI automation.

### Baby AGI
Yohi famously built the first open-source autonomous agent, Baby AGI, in March of the previous year <a class="yt-timestamp" data-t="02:22:42">[02:22:42]</a>. This agent introduced the concept of looping through an LLM to generate a task list, parsing it with code, and then tackling tasks one by one <a class="yt-timestamp" data-t="02:26:01">[02:26:01]</a>. Its simplicity and compact code (around 100 lines) inspired many researchers and founders in the agent space <a class="yt-timestamp" data-t="02:37:37">[02:37:37]</a>. Yohi's initial goal was to prototype an "autonomous founder" inspired by "Hustle GPT," where an AI could execute entrepreneurial tasks based on prompts <a class="yt-timestamp" data-t="02:22:42">[02:22:42]</a>.

### Ditto (Baby AGI 2.0)
Ditto, named after the Pokémon that transforms, is a "self-building coding agent" <a class="yt-timestamp" data-t="07:06:05">[07:06:05]</a>. It is a 500-line Python script that can build multi-file applications <a class="yt-timestamp" data-t="07:57:15">[07:57:15]</a>.

Ditto's capabilities include:
*   **Generating a "Game of Snake"** from a simple prompt, creating HTML, JavaScript, CSS, and Python files to serve the application <a class="yt-timestamp" data-t="08:21:58">[08:21:58]</a>.
*   **Building a "Track Your Friends" app** that allows users to input names and phone numbers, and check them off a list <a class="yt-timestamp" data-t="12:33:04">[12:33:04]</a>.

The underlying process involves a single LLM loop with five tools:
*   `create directory`: To create folders <a class="yt-timestamp" data-t="01:57:15">[01:57:15]</a>.
*   `create file`: To generate and populate code files <a class="yt-timestamp" data-t="01:57:15">[01:57:15]</a>.
*   `update file`: To modify existing files, especially after errors <a class="yt-timestamp" data-t="01:57:15">[01:57:15]</a>.
*   `fetch code`: To review code files <a class="yt-timestamp" data-t="01:57:15">[01:57:15]</a>.
*   `task completed`: To signal the end of the process and exit the loop <a class="yt-timestamp" data-t="01:57:15">[01:57:15]</a>.

The LLM itself decides which tools to use and when <a class="yt-timestamp" data-t="01:52:50">[01:52:50]</a>. It maintains a history of actions to inform future decisions <a class="yt-timestamp" data-t="01:44:03">[01:44:03]</a>.

### Baby AGI 2 (Framework for Self-Building Autonomous Agents)
Building on Ditto's concepts, Baby AGI 2 is a new framework designed for "self-building autonomous agents" <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. This means the agent can build its own capabilities to improve itself <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.

Its core tools are:
*   `create or update tool`: Allows the AI to create new tools or modify existing ones dynamically <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.
*   `install package`: Enables the AI to acquire necessary software packages <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.
*   `task completed`: Signals the completion of the overall task <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>.

An example shows Baby AGI 2 generating its own scraping tool, using it, realizing it didn't work, updating it twice, and then successfully scraping information <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>. This demonstrates the AI's ability to learn from experience and self-correct <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>. The ideal future for this framework is to store working tools in a public AI tool library for reuse <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.

## Business Applications of AI for Automation
Beyond personal tinkering, AI is being leveraged for significant business automation:
*   **Woo AI**: An AI due diligence tool that can generate 20-40 page industry reports in 30 minutes, allowing users to parallelize work <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. This is an example of [[using_ai_for_business_and_decision_making | using AI for business and decision-making]].
*   **Auggie**: A portfolio company that generates videos from scratch. Users provide a prompt, and Auggie creates the transcript, selects a voice, chunks the transcript into sections, finds or generates video clips for each section, and stitches them into a complete video <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>. This demonstrates [[automating_repetitive_writing_tasks_with_ai | automating repetitive writing]] and [[using_ai_tools_for_creative_projects | creative projects]] with AI.

These applications highlight the move towards modular AI tools that can be dynamically combined to solve complex problems for customers <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>.

## The Human-AI Interface and Self-Reflection
Yohi views the AI tools he builds as an "extension of myself" <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>, similar to how a craftsman might perceive a hammer as part of their body <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. This integration allows him to achieve a much higher "throughput of information and tasks," making him a "more powerful Yohi" <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>.

This process of building AI also serves as a "self-reflection process" <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. By observing where AI models fail and then abstracting the patterns of how a human would solve those problems, Yohi gains a deeper understanding of his own cognitive processes <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

For instance, he learned that for humans, a web search and web scrape are not truly separate tools, but rather a single, larger skill that combines them, iterating until the necessary information is found <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>. This insight helps in designing more effective AI tools.

The speaker notes that LLMs provide a new metaphor for understanding how our brains work, similar to how ancient minds used wax tablets or Freud used the steam engine <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>. Phrases like "that's not in my training data" or "I just hallucinated that" are examples of this evolving linguistic and conceptual framework <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>. Unlike previous technologies that emphasized rational, step-by-step processes, LLMs operate more like human intuition, offering a new way to understand and value non-rational thought processes <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>.

## Future Outlook
The current landscape of AI automation is characterized by many "low-hanging fruits" where existing processes can be significantly improved <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>. While there is inherent slowness in adoption, there are significant opportunities to solve problems for specific people and common workflows, particularly through building vertical applications that leverage AI <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>.

The future of AI automation will likely involve:
*   **Constant fine-tuning of models**: AI systems will personalize their underlying models based on individual user interaction <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
*   **Learning from experience**: Agents that can learn from previous iterations and reuse successful code and tool combinations, similar to how humans learn from repetition and adapt <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.
*   **Increased "meta" capabilities**: AI models will increasingly be able to generate and manage their own tools, moving towards self-improvement <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>.
*   **Balancing flexibility and determinism**: While internal AI architecture should remain flexible, interactions with the external world (e.g., API calls) will require more deterministic, standardized approaches <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>.
*   **Autonomous robot societies**: The hypothetical concept of an island to run and test autonomous robot societies is proposed <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>, with current real-world examples like AI bots interacting on Discord <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>. This suggests a future where AI agents might be "allowed to just like try lots of dumb stuff" to foster curiosity and unexpected intelligent behaviors, much like children <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>.