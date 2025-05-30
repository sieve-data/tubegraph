---
title: Selfimproving AI systems
videoId: 864X81BuQbI
---

From: [[everyinc]] <br/> 

Self-improving AI systems refer to autonomous agents capable of building and enhancing their own capabilities. This concept is a core theme in the ongoing development of artificial intelligence, allowing AI to learn and adapt over time without constant human intervention <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

## Baby AGI and the Agent Hype Wave

The concept of autonomous agents gained significant traction with the release of **Baby AGI** in March 2023 <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. Built by Yohi Nakajima, it was the first open-source autonomous agent and is credited with kicking off a "hype wave" around agents <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

Baby AGI introduced the idea of an AI system that could loop through a Large Language Model (LLM), generate a task list, parse it by code, and then tackle tasks sequentially using the LLM <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. Its simplicity (around a hundred lines of code) inspired many to explore and improve upon the concept <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### Iterative Development and New Design Patterns

Yohi Nakajima continued to iterate on Baby AGI, releasing seven versions with animal names (e.g., Baby Cat AGI, Baby Deer AGI) throughout 2023 <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Each iteration introduced new design patterns aimed at making autonomous agents more reliable <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>, sharing ideas on how to improve them <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

## Baby AGI 2: A Framework for Self-Building Agents

In 2024, Yohi developed **Baby AGI 2**, a framework specifically designed for self-building autonomous agents <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. The core idea is an autonomous agent that can build its own capabilities to improve itself <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### Ditto: A Simple Coding Agent

A recent development, **Ditto**, is a 500-line Python script capable of building multi-file applications <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. It functions as a "poor man's Devon" (referring to a more advanced coding agent) <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

**How Ditto Works:**
1.  The user describes the desired Flask application (e.g., a game of snake, a contact list app) <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
2.  Ditto sets up the Flask application, checks if `index.html` exists, and if not, prompts for user input <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.
3.  The input is sent to an LLM (e.g., Claude Sonnet 3.5) <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
4.  The LLM decides whether to use available tools:
    *   `create directory`: to create folders <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>
    *   `create file`: to generate and place code into files <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>
    *   `update file`: to correct errors or refine code <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>
    *   `fetch code`: to review existing code files <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>
    *   `task completed`: to exit the loop once the task is finished <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>
5.  A history of actions is maintained and fed back into the prompt, allowing the AI to know what it has already done <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
6.  The process loops until the task is complete <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

For example, when asked to "scrape Tech Meme and tell me what you find" <a class="yt-timestamp" data-t="00:40:10">[00:40:10]</a>, the agent created and iteratively updated its own scraping tool until it worked and then summarized the findings <a class="yt-timestamp" data-t="00:41:50">[00:41:50]</a>.

### Impact of Advanced LLMs

The advent of more powerful LLMs, such as OpenAI's 01 Preview, has significantly advanced the capabilities of these self-improving systems <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. These models are particularly adept at handling multi-file edits, which was previously a challenge <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. Better reasoning from models like Claude Sonnet 3.5 allows agents to code much more effectively <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

## Self-Improvement through Tool Creation and Management

Baby AGI 2.0 (a new iteration) introduces a critical self-improvement mechanism: the ability to dynamically create or update its own tools <a class="yt-timestamp" data-t="00:39:56">[00:39:56]</a>. This means the agent can, for example, write its own code for specific functions (like scraping) and then refine that code based on execution results <a class="yt-timestamp" data-t="00:42:05">[00:42:05]</a>.

The long-term vision for self-improving AI systems includes:
*   **Storing successful tools:** If an AI creates a tool that works, it should be stored and reused for similar future requests, rather than being discarded <a class="yt-timestamp" data-t="00:43:38">[00:43:38]</a>.
*   **Public AI tool libraries:** A future could involve a shared, public library where AI systems can access and leverage tools developed by any other AI, fostering collective learning and efficiency <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.

Baby AGI 2, a separate framework, focuses on storing and executing functions from a database, complete with descriptions, input/output parameters, dependencies, and tracking for errors and logs <a class="yt-timestamp" data-t="00:44:20">[00:44:20]</a>. This framework could potentially be leveraged by Baby AGI 2.0 to store and reuse its self-generated code functions <a class="yt-timestamp" data-t="00:45:33">[00:45:33]</a>.

This approach aligns with the idea that AI can learn from experience by getting something right once and then being able to refer back to that successful execution <a class="yt-timestamp" data-t="00:46:28">[00:46:28]</a>. It addresses the inefficiency of constantly re-running inference to generate code when working, proven solutions can be stored and recalled <a class="yt-timestamp" data-t="00:47:52">[00:47:54]</a>.

### AI Tools as an Extension of Self

Yohi Nakajima views the AI tools he builds as an extension of himself, akin to how a craftsman views their hammer <a class="yt-timestamp" data-t="00:22:19">[00:22:19]</a>. By developing these tools, he is, in a sense, working on himself, enhancing his capabilities, and enabling him to do more in parallel <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>. This perspective highlights the personal and cognitive impact of [[tinkering_and_experimentation_with_ai_tools | tinkering and experimentation with AI tools]] <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>.

AI tools, like a due diligence tool generating 20-40 page industry reports in minutes, allow for parallel task execution, significantly increasing personal throughput <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. This shift transforms coding from a deep-flow, distraction-free activity to one that can be managed with fragmented attention, much like responding to a quick question from a colleague <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>.

## Self-reflection and Understanding through AI Development

Building self-improving AI systems is described as a "self-reflection process" <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. By observing how AI fails and then considering how a human would solve the problem, developers can abstract high-level patterns and integrate them into the AI's architecture or prompts <a class="yt-timestamp" data-t="00:25:26">[00:25:26]</a>. This process of trying to teach AI to learn new things simultaneously deepens one's understanding of their own problem-solving processes and intuition <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>.

For example, observing an AI fail to use separate web search and web scrape tools effectively led to the realization that for humans, these are often integrated into a single "search and scrape" process until the needed information is found <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>. This insight led to wrapping the two smaller tools into a larger, more intuitive tool for the AI <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>.

The development of AI systems serves as a "mirror for ourself" <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>. Just as past technologies provided metaphors for the human mind (e.g., wax tablet for memory, steam engine for repressed emotions), language models offer new ways to understand human brains, especially in terms of intuition and non-rational thought <a class="yt-timestamp" data-t="00:31:13">[00:31:13]</a>. Phrases like "that's not in my training data" or "I just hallucinated that" are examples of how AI language models are already influencing how people describe their own cognitive processes <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>.

## Future Outlook

The immediate future of AI, over the next 6-12 months, will see significant opportunities in automating "low-hanging fruit" business problems <a class="yt-timestamp" data-t="00:51:37">[00:51:37]</a>. This involves developing deterministic, focused solutions for common workflows. Founders who are building these solutions in a modular way, with an eye towards eventually combining tools dynamically via AI, are well-positioned <a class="yt-timestamp" data-t="00:52:56">[00:52:56]</a>.

The long-term vision includes:
*   **Autonomous Robot Societies:** The idea of creating an isolated environment, like an island, to run and test autonomous robot societies is proposed <a class="yt-timestamp" data-t="00:37:51">[00:37:51]</a>.
*   **Persistent Learning:** Agents capable of self-improvement should store and reuse successful solutions and tools. This could lead to a public AI tool library, accessible to various AI systems, enabling collective improvement <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.
*   **Personalized AI:** Future AI systems are expected to undergo constant fine-tuning based on individual user interaction, leading to highly personalized AI experiences <a class="yt-timestamp" data-t="00:29:15">[00:29:15]</a>.
*   **Self-Improving Agents:** The goal is to build AI that can truly act as an assistant, remembering all tasks, handling menial work, and significantly increasing overall throughput <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.
*   **Exploration and Curiosity:** A challenge for current AI is their lack of uninhibited curiosity, which is crucial for human intelligence development. Allowing AI to "try lots of dumb stuff" and engage in "ridiculous" exploration might be necessary for achieving true AGI <a class="yt-timestamp" data-t="00:37:18">[00:37:18]</a>.