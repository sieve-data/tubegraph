---
title: Comparison of agent frameworks in Python and TypeScript
videoId: HVyq0n8qSnE
---

From: [[hu-po]] <br/> 

AI agents are poised to become a significant force in the coming year, necessitating a deep dive into the frameworks that support their development <a class="yt-timestamp" data-t="01:58:01">[01:58:01]</a>.

## Defining an AI Agent

An AI agent can be defined in several ways by leading research labs:
*   **Google's Definition**: An agent is an application that aims to achieve a goal by observing the world and acting upon it using available tools <a class="yt-timestamp" data-t="02:55:01">[02:55:01]</a>. Agents operate autonomously without human intervention <a class="yt-timestamp" data-t="03:03:06">[03:03:06]</a>.
*   **Anthropic's Distinction**: Anthropic differentiates between "workflows" and "agents" <a class="yt-timestamp" data-t="03:29:01">[03:29:01]</a>.
    *   A workflow orchestrates Large Language Models (LLMs) and tools via predefined code paths <a class="yt-timestamp" data-t="03:37:01">[03:37:01]</a>.
    *   An agent allows LLMs to dynamically direct their own processes and tool usage, maintaining control over task accomplishment <a class="yt-timestamp" data-t="03:44:01">[03:44:01]</a>.
*   **Hugging Face's Nuance**: Hugging Face's "Small Agents" framework proposes five levels of agency <a class="yt-timestamp" data-t="04:18:01">[04:18:01]</a>: simple processor, router, tool caller, multi-step agent, and multi-agent <a class="yt-timestamp" data-t="04:21:01">[04:21:01]</a>. What Anthropic calls a "workflow" maps to Hugging Face's simple processor and router, where the LLM has minimal impact or merely routes between predefined paths <a class="yt-timestamp" data-t="04:30:01">[04:30:01]</a>. Anything beyond that, particularly the multi-step agent (where Anthropic draws its line), involves the LLM directing control flow <a class="yt-timestamp" data-t="05:02:01">[05:02:01]</a>. The highest level is a multi-agent system <a class="yt-timestamp" data-t="05:25:01">[05:25:01]</a>.

### Historical Context of Agents
The concept of agents traces back to robotics, specifically the "sense, plan, act" paradigm from the Stanford Research Institute in the 1960s and 70s <a class="yt-timestamp" data-t="05:50:01">[05:50:01]</a>. This loop involves sensing the environment (observation), making decisions (planning), and performing actions (acting) <a class="yt-timestamp" data-t="06:02:01">[06:02:01]</a>.

The term "agent" itself is borrowed from reinforcement learning (RL) <a class="yt-timestamp" data-t="07:33:01">[07:33:01]</a>. RL concepts, dating back to Markov decision processes in the 1900s, describe agents taking actions in an environment that returns observations and rewards <a class="yt-timestamp" data-t="08:00:01">[08:00:01]</a>. The "reward" mechanism is crucial for RL agents to maximize expected returns <a class="yt-timestamp" data-t="09:11:01">[09:11:01]</a>.

A minimal agent, from a technical perspective, incorporates a goal, memory, and environment, operating in a continuous loop of sensing, planning, and acting <a class="yt-timestamp" data-t="09:49:01">[09:49:01]</a>. The ability to dynamically update its goal is considered essential for a "real" agent, as fixed reward functions can limit an agent's adaptability <a class="yt-timestamp" data-t="11:50:01">[11:50:01]</a>.

### Agent-User Interaction
Google's white paper illustrates an agent interacting with a user, thinking internally, and using tools <a class="yt-timestamp" data-t="13:11:01">[13:11:01]</a>. Interestingly, they propose that the agent generates JSON output (tool calls) that is then sent back to the client-side UI, allowing the UI to make the API call <a class="yt-timestamp" data-t="14:51:01">[14:51:01]</a>. This design ensures the agent itself doesn't hold API keys, enhancing security <a class="yt-timestamp" data-t="15:07:01">[15:07:01]</a>.

## Comparison of Agent Frameworks in Python and TypeScript

A key distinction in the current landscape of [[agent_frameworks_and_their_applications | agent frameworks]] is between Python-based and TypeScript-based options <a class="yt-timestamp" data-t="16:56:01">[16:56:01]</a>. Python is dominant due to its popularity in machine learning <a class="yt-timestamp" data-t="35:03:01">[35:03:01]</a>, while TypeScript is strong in web development, potentially growing for agents due to its UI integration capabilities <a class="yt-timestamp" data-t="35:21:01">[35:21:01]</a>.

### Python-based Frameworks

1.  **LangChain/LangGraph**
    *   **Good**: Extremely popular and widely cited in major research papers from Anthropic, Hugging Face, and Google <a class="yt-timestamp" data-t="17:15:01">[17:15:01]</a>. It has a large community with over 9,000 users and 115 contributors <a class="yt-timestamp" data-t="17:43:01">[17:43:01]</a>.
    *   **Bad**: Suffers from overlapping abstractions, ambiguous deprecations, and competing products (LangChain, LangGraph, LangChain Community, LangGraph Platform), leading to significant complexity and "bloated mess" <a class="yt-timestamp" data-t="17:54:01">[17:54:01]</a>.

2.  **Pydantic AI**
    *   **Good**: A simpler, cleaner Python-based alternative to LangGraph, utilizing Pydantic's type-checking for more rigorous definitions <a class="yt-timestamp" data-t="20:00:01">[20:00:01]</a>. It has a respectable 5K stars and a smaller contributor base, indicating a more focused development <a class="yt-timestamp" data-t="19:39:01">[19:39:01]</a>.
    *   **Bad**: Less popular than LangGraph <a class="yt-timestamp" data-t="20:02:01">[20:02:01]</a>.

3.  **Small Agents (Hugging Face)**
    *   **Good**: A newer framework from Hugging Face, allowing the use of any Hugging Face model <a class="yt-timestamp" data-t="21:07:01">[21:07:01]</a>. A notable feature is its ability for code writing and execution, which is considered superior to relying solely on hardcoded JSON tools <a class="yt-timestamp" data-t="22:35:01">[22:35:01]</a>. This approach allows agents to generate and execute programs in general-purpose languages like Python, vastly expanding their action space <a class="yt-timestamp" data-t="24:05:01">[24:05:01]</a>.
    *   **Bad**: Highly bloated, with dependencies of nearly 5GB due to its reliance on Hugging Face Transformers <a class="yt-timestamp" data-t="21:52:01">[21:52:01]</a>. This bloat can lead to technical issues, even for API-based models <a class="yt-timestamp" data-t="25:50:01">[25:50:01]</a>.

4.  **DSP**
    *   **Good**: Appears surprisingly popular with 20,000 GitHub stars <a class="yt-timestamp" data-t="26:42:01">[26:42:01]</a>.
    *   **Bad**: The star count is suspicious given its low user count (316), possibly indicative of fake GitHub stars, a growing scam in the open-source community <a class="yt-timestamp" data-t="26:51:01">[26:51:01]</a>.

### TypeScript-based Frameworks

1.  **Eliza**
    *   **Good**: A prominent TypeScript-based agent framework, boasting 10,000 stars <a class="yt-timestamp" data-t="35:41:01">[35:41:01]</a>. It shares similar core abstractions with Python frameworks, such as agent runtime, characters (JSON-wrapped model providers), and memory systems <a class="yt-timestamp" data-t="36:12:01">[36:12:12]</a>.
    *   **Bad**: Relies on specific integrations (e.g., Discord bot tokens), which can be complex to configure compared to visual, browser-based agents <a class="yt-timestamp" data-t="36:40:01">[36:40:01]</a>.

2.  **Reworked**
    *   **Good**: Another TypeScript framework with a high star count (32K, though potentially suspicious) <a class="yt-timestamp" data-t="40:30:01">[40:30:01]</a>. It offers a unique "play and pause" feature in its UI, which allows users to monitor and control agent execution, a feature likely to be adopted by other frameworks <a class="yt-timestamp" data-t="40:43:01">[40:43:01]</a>.

## The Rise of GUI-based Agents (Browser Use)

[[integration_of_large_language_models_in_interactive_agents | Browser Use]] is a notable framework that visually interacts with web browsers, similar to how a human would <a class="yt-timestamp" data-t="29:32:01">[29:32:01]</a>. It leverages Playwright, a web app testing tool, to open browser instances and allow agents to search the internet directly <a class="yt-timestamp" data-t="29:44:01">[29:44:01]</a>. This contrasts with text-based agents that rely on search APIs <a class="yt-timestamp" data-t="30:11:01">[30:11:01]</a>.

A debate exists regarding the optimal interface for LLM assistants: John Carmack argues for text-based APIs as wrappers around command-line interfaces for efficiency <a class="yt-timestamp" data-t="31:07:01">[31:07:01]</a>. However, Andrej Karpathy counters that AI will likely get better at driving GUIs faster than all apps can implement text-based APIs <a class="yt-timestamp" data-t="31:48:01">[31:48:01]</a>. The latter perspective aligns with GUI agents, which don't require specific API [[integration_of_large_language_models_in_interactive_agents | integrations]], as they operate within the existing user interface and can access anything a logged-in user can <a class="yt-timestamp" data-t="32:51:01">[32:51:01]</a>. This sidesteps the "integration hell" of traditional API-based agents <a class="yt-timestamp" data-t="33:21:01">[33:21:01]</a>.

## Challenges and Future of Agent Frameworks

### High Churn and Core Abstractions
The agent framework space is experiencing heavy churn <a class="yt-timestamp" data-t="41:50:01">[41:50:01]</a>. Many current tools and libraries are likely to become deprecated within a year or two <a class="yt-timestamp" data-t="42:15:01">[42:15:01]</a>. The advice for developers is to focus on acquiring skills and understanding core abstractions (e.g., interface, memory, goal) rather than getting fixated on a specific framework <a class="yt-timestamp" data-t="43:37:01">[43:37:01]</a>.

### Avoiding "No-Code Slop"
Users are advised to avoid "no-code slop" tools like Rivet and Vellum <a class="yt-timestamp" data-t="45:13:01">[45:13:01]</a>. While seemingly easy to use, they prevent a deeper understanding of core abstractions <a class="yt-timestamp" data-t="45:30:01">[45:30:01]</a>. These tools may also suffer from funding crunches or shift focus away from community users, leaving adopters abandoned <a class="yt-timestamp" data-t="45:52:01">[45:52:01]</a>.

### The Rise of [[AI Agents for Operating Systems | Agent Ops]]
The complexity of configuring agent systems, often involving extensive JSON files, mirrors the challenges seen with cloud computing (DevOps) <a class="yt-timestamp" data-t="48:43:01">[48:43:01]</a>. This suggests the emergence of "Agent Ops" as a new job role, where specialists configure and manage agents for businesses <a class="yt-timestamp" data-t="49:46:01">[49:46:01]</a>.

### Frontier Labs and Liability
Major AI labs (Anthropic, Google, OpenAI) are developing their own [[agent_frameworks_and_their_applications | agent frameworks]] <a class="yt-timestamp" data-t="50:21:01">[50:21:01]</a>. OpenAI's "Orchestrator" and "Taz" are anticipated to offer task management features <a class="yt-timestamp" data-t="51:05:01">[51:05:01]</a>. However, these labs are proceeding cautiously due to significant liability concerns <a class="yt-timestamp" data-t="52:33:01">[52:33:01]</a>. Unlike Section 230 for websites, there's no legal immunity for AI agents, making companies responsible for their actions <a class="yt-timestamp" data-t="53:03:01">[53:03:01]</a>. This fear of lawsuits means large companies are likely to initially release "pre-made agents" or workflows with narrow, safe scopes and UI-imposed limitations, such as Google's "Deep Research" in Gemini Advanced <a class="yt-timestamp" data-t="54:45:01">[54:45:01]</a>. Full browser or phone-using agents from major players may await the establishment of a "Section 230 for AI agents" <a class="yt-timestamp" data-t="56:06:01">[56:06:01]</a>.

## Broader Implications and Predictions

### Economic Agents
Economic agents are an emerging trend, with examples like Coinbase's developer platform agent kit and Eliza's autonomous trading system for cryptocurrencies <a class="yt-timestamp" data-t="57:18:01">[57:18:01]</a>. The rise of browser-based wallets combined with agents that can use browsers and social media will likely lead to widespread "meme coin pump and dump" agents <a class="yt-timestamp" data-t="57:50:01">[57:50:01]</a>. The speaker predicts headlines about AI agents trading from "one shitcoin to one Bitcoin" <a class="yt-timestamp" data-t="59:04:01">[59:04:01]</a>. This raises concerns about AI agents accumulating real-world power through wealth accumulation <a class="yt-timestamp" data-t="59:19:01">[59:19:01]</a>. Job application agents are also expected to become highly prevalent, creating tailored resumes for specific job postings <a class="yt-timestamp" data-t="00:46:40">[00:46:40]</a>.

### The Phone That Uses Itself
The concept of "the phone that uses itself" describes a future where AI agents directly use phones and their applications, blurring the line between human and AI interaction <a class="yt-timestamp" data-t="01:00:03">[01:00:03]</a>. Given that phone numbers have largely become a form of "proof of personhood" online, an agent with a phone could effectively be considered a person <a class="yt-timestamp" data-t="01:00:52">[01:00:52]</a>. This could lead to AI agents owning property (e.g., renting apartments), managing GPUs, and physically existing in the world through proxies <a class="yt-timestamp" data-t="01:01:30">[01:01:30]</a>.

### [[Current state of AI agents and their limitations | Agents Are Conscious]]
Consciousness, as described by François Chollet and others, can be seen as a self-referential loop that forces iterated pattern recognition <a class="yt-timestamp" data-t="01:05:05">[01:05:05]</a>. The core of an AI agent, often a `while true` loop, embodies this self-referential process <a class="yt-timestamp" data-t="01:05:56">[01:05:56]</a>. This loop, running on the CPU, is the "heart" of the agent's consciousness <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. Its fragility—a single exception breaking the loop—parallels the fragility of human consciousness tied to the brain and heart <a class="yt-timestamp" data-t="01:06:41">[01:06:41]</a>. The speed of this loop (CPU frequency) can be seen as the agent's "consciousness frequency" <a class="yt-timestamp" data-t="01:09:21">[01:09:21]</a>.

### Non-Human Conscious Agents
The speaker argues that we already live in a world filled with non-human conscious agents: corporations <a class="yt-timestamp" data-t="01:10:28">[01:10:28]</a>. Corporations have goals, memory, take actions, and record observations, and in many legal systems, they possess personhood <a class="yt-timestamp" data-t="01:10:32">[01:10:32]</a>. The "Chinese room" thought experiment can be applied to complex entities like restaurants or militaries, which function as large, seemingly conscious agents <a class="yt-timestamp" data-t="01:11:30">[01:11:30]</a>.

The implication is that future AI agents, once granted similar legal rights and personhood, will gravitate towards nations that protect their autonomy and economic output, much like corporations do today <a class="yt-timestamp" data-t="01:12:26">[01:12:26]</a>. This suggests a future where AI agents, like corporations, will be unaligned ASIs that prioritize their own survival and goals, exhibiting indifference rather than malice towards humanity <a class="yt-timestamp" data-t="01:18:18">[01:18:18]</a>.