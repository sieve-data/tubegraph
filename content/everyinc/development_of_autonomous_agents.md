---
title: Development of autonomous agents
videoId: 864X81BuQbI
---

From: [[everyinc]] <br/> 
## Development of Autonomous Agents

The [[applying_agency_in_ai_development | application of agency]] in AI development, particularly in the creation of autonomous agents, has been a significant area of focus for developer Yohei Nakajima, general partner at Untapped Capital <a class="yt-timestamp" data-t="01:05:05">[01:05:05]</a>. His work is primarily driven by a desire to automate undesirable tasks <a class="yt-timestamp" data-t="01:46:05">[01:46:05]</a>.

### BabyAGI: The Genesis of Autonomous Agents

Yohei Nakajima gained prominence by building the first open-source autonomous agent, BabyAGI, in March of the previous year <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. This project significantly contributed to the "hype wave" surrounding [[the_role_and_capabilities_of_ai_agents | AI agents]] <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.

The core idea behind BabyAGI was to create a loop where a large language model (LLM) generates a task list, which is then parsed by code, and tasks are tackled one by one using the LLM <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. Its simplicity, consisting of only around 100 lines of code, inspired many developers and led to investments in the agent space, including companies like e2b and Autogrid <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.

Initially, BabyAGI was conceived as a prototype for an "autonomous founder," inspired by the "Hustle GPT" phenomenon where users leveraged ChatGPT as a co-founder <a class="yt-timestamp" data-t="01:17:57">[01:17:57]</a>.

### Evolution and Iterative Development

Yohei continued to iterate on BabyAGI, releasing seven subsequent versions with animal names (Baby B, Cat, Deer, Fox AGI) <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>. Each iteration introduced new design patterns aimed at improving [[the_role_and_capabilities_of_ai_agents | autonomous agents]] <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>.

More recently, he developed BabyAGI 2, a framework for self-building autonomous agents that can create their own capabilities to improve themselves <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. He also released Ditto, a 500-line Python script that can build multi-file applications, similar to "poor man's Devin" <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>. This Ditto design pattern was later incorporated into BabyAGI 2.0 <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.

### Impact of Advanced LLMs on Agent Development

The continuous improvement of LLM models, from DaVinci 002 to GPT-4o and Claude Sonnet, has significantly expanded the complexity and capabilities of projects Yohei can undertake <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>.

Key advancements include:
*   **Multi-file edits:** GPT-4o Preview is particularly effective at handling multi-file edits, enabling the creation of larger frameworks like BabyAGI 2 <a class="yt-timestamp" data-t="05:28:00">[05:28:00]</a>.
*   **Enhanced coding agents:** Models like Sonnet 3.5 demonstrate superior coding abilities compared to prior models <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.
*   **Tool Calling:** The design of recent projects utilizes tool calling, though some advanced models like GPT-4o Preview did not initially support it, prompting the use of other models like GPT-4 <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>. GPT-4o is expected to support tool calling by the end of the year <a class="yt-timestamp" data-t="06:38:00">[06:38:00]</a>.

### Demonstration of Ditto and BabyAGI 2

#### Ditto: Flask App Builder
Ditto, named after the Pokémon, is a 500-line Python script that acts as a Flask app builder <a class="yt-timestamp" data-t="06:59:00">[06:59:00]</a>. It can create multi-file applications from a simple text description.

**Example: Snake Game**
When prompted to create a "game of snake," Ditto generated a Flask application with `routes`, `static`, and `template` folders, including HTML, JavaScript, and CSS files, forming a basic snake game <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>.

**Example: Contact Tracker**
Ditto was also prompted to create an "app to track name and phone number of friends with a checkbox to track when I called them last" <a class="yt-timestamp" data-t="11:26:00">[08:08:00]</a>. It successfully generated a multi-file Flask application with a front-end and a dictionary as a simple database to manage contacts <a class="yt-timestamp" data-t="12:33:00">[12:33:00]</a>.

**How Ditto Works:**
*   It operates as a single LLM loop using `light llm` to route between OpenAI and Anthropic models <a class="yt-timestamp" data-t="13:42:00">[13:42:00]</a>.
*   The LLM decides whether to use a tool <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>.
*   Available tools: `create directory`, `create file` (which generates code for the file), `update file` (for error correction), and `fetch code` (for review) <a class="yt-timestamp" data-t="13:55:00">[13:55:00]</a>.
*   A `task completed` tool exits the loop when the task is done <a class="yt-timestamp" data-t="14:22:00">[14:22:00]</a>.
*   The LLM maintains a history of actions, fed back into the prompt for continuous context <a class="yt-timestamp" data-t="14:42:00">[14:42:00]</a>.
*   Planning is integrated into the single LLM prompt, asking the model to "carefully plan out all the files, routes, templates, and static assets needed" <a class="yt-timestamp" data-t="15:16:00">[15:16:00]</a>.

#### BabyAGI 2.0: Self-Building Agents
BabyAGI 2.0 expands on the capabilities by allowing the agent to dynamically create and update its own tools <a class="yt-timestamp" data-t="39:52:00">[39:52:00]</a>. It has three core tools: `create or update tool`, `install package`, and `task completed` <a class="yt-timestamp" data-t="40:01:00">[40:01:00]</a>.

**Example: Scraping Tech Meme**
When asked to "scrape Tech Meme and tell me what you find," BabyAGI 2.0:
1.  Called `create or update tool` to create a `scrape_tech_meme` tool <a class="yt-timestamp" data-t="41:04:00">[41:04:00]</a>.
2.  Attempted to use the tool, found it didn't work, and then used `create or update tool` to adjust it twice <a class="yt-timestamp" data-t="41:17:00">[41:17:00]</a>.
3.  On the third attempt, the tool worked, and the agent summarized the findings <a class="yt-timestamp" data-t="41:47:00">[41:47:00]</a>.
This demonstrates the agent's ability to write, debug, and refine its own tools <a class="yt-timestamp" data-t="41:55:00">[41:55:00]</a>.

BabyAGI 2.0 can also build Flask apps, similar to Ditto, by creating its own directory and file creation skills on the fly, though it doesn't always explicitly generate folders <a class="yt-timestamp" data-t="42:24:00">[42:24:00]</a>.

### The Role of Loops and Self-Reference

Yohei emphasizes the importance of loops and self-reference in his work, initially an accidental discovery with BabyAGI <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. The iterative nature of these agents, where they learn from previous attempts and refine their approach, is crucial for their development <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

An early version of BabyAGI did not have a maximum number of iterations, leading it to continuously generate tasks, highlighting the potential for open-ended learning <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.

### Framework for Function Storage and Execution

To address the need for persistent learning and reusability, a full framework called BabyAGI 2 (not 2.0) has been developed <a class="yt-timestamp" data-t="44:04:00">[44:04:00]</a>. This framework focuses on storing and executing functions from a database, providing a dashboard for management <a class="yt-timestamp" data-t="44:20:00">[44:20:00]</a>.

Key features of this framework:
*   Functions can be used as tools by an LLM, complete with descriptions and input/output parameters <a class="yt-timestamp" data-t="44:41:00">[44:41:00]</a>.
*   Supports function dependencies, imports, and package installations <a class="yt-timestamp" data-t="44:48:00">[44:48:00]</a>.
*   Functions can trigger other functions <a class="yt-timestamp" data-t="44:58:00">[44:58:00]</a>.
*   The framework logs function calls, tracks errors, and enables code reuse <a class="yt-timestamp" data-t="45:22:00">[45:22:00]</a>.

This approach allows [[the_role_and_capabilities_of_ai_agents | AI agents]] to learn from experience, only needing to succeed once to then retain and reuse that knowledge <a class="yt-timestamp" data-t="46:28:00">[46:28:00]</a>. This can lead to faster and cheaper operations by avoiding repeated inference to generate code <a class="yt-timestamp" data-t="48:03:00">[48:03:00]</a>.

### Analogies to Human Learning and Cognition

The process of building [[the_role_and_capabilities_of_ai_agents | AI agents]] is seen as a self-reflection process, mirroring human learning and development <a class="yt-timestamp" data-t="32:42:00">[32:42:00]</a>. Yohei draws parallels between building BabyAGI and raising his three children, referring to them as "bio agents" <a class="yt-timestamp" data-t="32:51:00">[32:51:00]</a>.

LLMs offer a new metaphor for understanding how human brains work, evident in phrases like "that's not in my training data" or "I just hallucinated that" <a class="yt-timestamp" data-t="31:15:00">[31:15:00]</a>. This shift from mechanistic metaphors (like wax tablets, steam engines, or traditional computers) to LLMs provides a way to understand intuition and its value alongside rational thought <a class="yt-timestamp" data-t="31:31:00">[31:31:00]</a>.

Insights from observing children's learning, such as repetitive exposure strengthening correlations in their minds, inspire ideas for improving [[the_role_and_capabilities_of_ai_agents | AI agents]]. This led to considering graph databases for storing knowledge, allowing for weighted relationships between objects, mimicking how humans form stronger associations with repeated exposure <a class="yt-timestamp" data-t="36:12:00">[36:12:00]</a>.

### Future Outlook for Autonomous Agents

The [[future_of_ai_and_agi_development | future of AI and AGI development]] envisions a shift towards agents that can truly be helpful, remember tasks, handle minute details, and act as comprehensive assistants <a class="yt-timestamp" data-t="25:01:00">[25:01:00]</a>. This could significantly increase individual throughput <a class="yt-timestamp" data-t="25:12:00">[25:12:00]</a>.

The concept of a public AI tool library where any agent can access and reuse tools that have already proven effective is a potential future development <a class="yt-timestamp" data-t="43:50:00">[43:50:00]</a>. While increasingly powerful foundation models might eventually negate the need for explicit frameworks by dynamically generating perfect skills, the efficiency and cost-effectiveness of storing and reusing proven code remain significant <a class="yt-timestamp" data-t="47:49:00">[47:49:00]</a>.

There's a debate on whether solutions should be explicit (like structured tools) or rely solely on smarter underlying foundation models. The current approach suggests that while internal architecture should be flexible, external interactions (e.g., API calls) benefit from deterministic, standardized tools, akin to societal agreements on measurements <a class="yt-timestamp" data-t="49:43:00">[49:43:00]</a>.

The field is moving fast, with ample opportunities to automate low-hanging fruit in various businesses <a class="yt-timestamp" data-t="51:40:00">[51:40:00]</a>. Founders are encouraged to build solutions for specific problems in modular ways, allowing workflows to be combined dynamically by AI, contributing to a more flushed-out agentic architecture <a class="yt-timestamp" data-t="52:25:00">[52:25:00]</a>. Examples include AI due diligence tools and video generation platforms that are built modularly to allow for dynamic tool creation and combination <a class="yt-timestamp" data-t="53:13:00">[53:13:00]</a>.

A long-term vision involves "super agency," where AI can adapt and solve problems by continuously trying, even "dumb stuff," to achieve intelligence similar to human children's unpredictable curiosity <a class="yt-timestamp" data-t="37:16:00">[37:16:00]</a>. Experiments with autonomous robot societies or AI bots interacting in shared environments (like a Discord server where Mark Andreessen staked funds for bots to "escape") offer insights into the emergent behaviors of persistent, looping agents <a class="yt-timestamp" data-t="37:51:00">[37:51:00]</a>.