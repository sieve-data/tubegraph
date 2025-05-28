---
title: AI Agents for Operating Systems
videoId: H5yd-uh9acY
---

From: [[hu-po]] <br/> 

AI agents are rapidly advancing, with recent research demonstrating their capability to autonomously operate computer operating systems. This marks a significant step towards [[definition_of_an_agent_in_ai | Artificial General Intelligence (AGI)]], with some arguing that large language models (LLMs) already embody AGI, and the focus is shifting towards Artificial Super Intelligence (ASI) <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.

## Current State of OS Agents

Recent papers highlight the ability of [[current_state_of_ai_agents_and_their_limitations | AI agents]] to interact with and control various operating systems and applications:

### OS Co-Pilot (Mac OS)
Released February 15, 2024, this paper describes an agent that combines a vision language model (VLM) and an LLM, specifically GPT-4 Turbo and GPT-4 Vision, to operate a Mac OS computer <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.
Capabilities include:
*   Calculating and drawing charts in Excel <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.
*   Creating and adjusting work layouts and themes for websites <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>.
*   Playing music <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>.
*   Generating files and building web pages by interacting with multiple programs <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>.

### UFO (UI-Focused Agent for Windows OS Interaction)
Released February 8, 2024, by Microsoft, UFO also utilizes GPT-4 Vision and GPT-4 to operate Windows OS <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>. It can span multiple applications, with users providing only high-level natural language commands <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>.
Examples of tasks performed:
*   Extracting information from Word documents <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>.
*   Scrolling through photo apps to find specific images <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>.
*   Creating PowerPoint presentations <a class="yt-timestamp" data-t="07:46:00">[07:46:00]</a>.
*   Sending PowerPoints via email <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>.
*   Using PywinAuto for programmatic control of Windows functions (click, set text, summarize, get text, scroll) <a class="yt-timestamp" data-t="34:01:00">[34:01:00]</a>.

> [!INFO] AGI in Practice
> The ability of GPT-4 to operate both Mac and Windows computers with minimal prompt engineering is presented as strong evidence that GPT-4 is already [[definition_of_an_agent_in_ai | AGI]] <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>.

### Evolution to Large Action Models (LAMs)
The development of these agents, capable of comprehending natural language requests and autonomously interacting with UIs, suggests a transition from large language models to "large action models" <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>. Although the speaker finds the term "LAM" somewhat "cringe" as it's still based on existing LLMs and VLMs combined with prompt engineering <a class="yt-timestamp" data-t="08:36:00">[08:36:00]</a>.

## Core Components and Concepts of Agent Frameworks

### Sense-Plan-Act Loop
Most [[agent_frameworks_and_their_applications | AI agent frameworks]] follow a "sense-plan-act" loop:
1.  **Sensing (Observation):** Involves consuming information like screenshots, user requests, and retrieving historical data from memory <a class="yt-timestamp" data-t="09:19:00">[09:19:00]</a>.
2.  **Planning (Internal Chain of Thought):** The LLM internally generates thoughts and explanations, explicitly thinking out loud to devise steps. This is often an output of the LLM <a class="yt-timestamp" data-t="28:09:00">[28:09:00]</a>.
3.  **Acting:** The agent executes specific actions within the operating system or application, often via APIs <a class="yt-timestamp" data-t="35:35:00">[35:35:00]</a>.

### Memory
[[agent_frameworks_and_their_applications | Agents]] store previous states, actions, user requests, and screenshots. This can be categorized as:
*   **Procedural Memory:** Tools or functions (APIs) that define the action space <a class="yt-timestamp" data-t="13:25:00">[13:25:00]</a>.
*   **Declarative Memory:** More static information like user profiles or generic semantic knowledge <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>.

> [!NOTE] Future of Memory and Context
> The need for explicit memory management and retrieval augmented generation (RAG) may diminish as context window lengths in LLMs increase (e.g., Gemini 1.5 handling 10 million tokens) <a class="yt-timestamp" data-t="14:47:00">[14:47:00]</a>. This could lead to simpler, more direct models.

### Action Grounding
This technique improves VLM performance by annotating screenshots with visual aids (e.g., red rectangles, numbers, arrows) to highlight clickable elements or indicate directions. This helps the VLM understand the function and location of UI elements <a class="yt-timestamp" data-t="18:36:00">[18:36:00]</a>. This "anthropomorphic" approach, akin to a human annotating an image for another human, surprisingly works effectively with VLMs <a class="yt-timestamp" data-t="21:15:00">[21:15:00]</a>.

### Action Tokens
The output of an [[agent_frameworks_and_their_applications | agent]] can include "action tokens," which are hardcoded tokens representing specific actions (e.g., clicking a button, moving a mouse in discrete bins, joystick actions) <a class="yt-timestamp" data-t="29:50:00">[29:50:00]</a>.

> [!WARNING] Limitation of Action Tokens
> A significant drawback is that these action spaces are task-dependent and must be predefined for each specific task or game. This limits the generality of the agent, unlike models where the action space is pure text (e.g., the Voyager agent for Minecraft outputs functions in text) <a class="yt-timestamp" data-t="32:07:00">[32:07:00]</a>. The speaker predicts that future [[agent_frameworks_and_their_applications | agents]] will output pure text for actions, making them truly general-purpose <a class="yt-timestamp" data-t="33:33:00">[33:33:00]</a>.

## Broader Applications of AI Agents

Beyond operating systems, [[agent_frameworks_and_their_applications | AI agents]] are being developed for diverse domains:

*   **Robotics:** Manipulation and navigation tasks <a class="yt-timestamp" data-t="44:14:00">[44:14:00]</a>.
*   **Gaming:** Playing video games and generating new ones through self-play loops <a class="yt-timestamp" data-t="55:15:00">[55:15:00]</a>.
*   **Healthcare:** Diagnosing situations from visual data, e.g., captioning patient status from a video <a class="yt-timestamp" data-t="44:21:00">[44:21:00]</a>.
*   **3D Design:** Generating unconventional 3D objects in software like Blender using a "Chain of 3D Thought" approach, leveraging Python APIs <a class="yt-timestamp" data-t="47:31:00">[47:31:00]</a>.
*   **Software Development:** Meta (Facebook) uses bots to generate unit tests and push their own PRs <a class="yt-timestamp" data-t="15:50:00">[15:50:00]</a>.

> [!INFO] Positive Transfer Learning
> Pre-training agents on a mixture of data from domains like robotics and gaming can lead to "positive transfer" to unseen domains such as healthcare. This means an agent can become better at diagnosing medical situations simply by playing games <a class="yt-timestamp" data-t="53:00:00">[53:00:00]</a>. This suggests that even if certain industries restrict access to their data (e.g., healthcare data), [[generative_ai_agents_and_human_behavior_simulation | AI agents]] will still achieve superhuman levels of proficiency through self-play and diverse training <a class="yt-timestamp" data-t="54:35:00">[54:35:00]</a>.

## Advancements in Agent Reasoning and Collaboration

### Chain of Thought (CoT) Decoding
Traditional language models often use greedy decoding (picking the most probable next token) or temperature sampling (introducing randomness). However, exploring "alternative top K tokens" in the decoding process can reveal inherent [[integration_of_large_language_models_in_interactive_agents | Chain of Thought]] paths within pre-trained LLMs without explicit prompting <a class="yt-timestamp" data-t="01:13:51">[01:13:51]</a>.
*   **Method:** By investigating top alternative tokens and longer decoding paths, models can achieve substantially better performance, especially in mathematical benchmarks <a class="yt-timestamp" data-t="01:23:42">[01:23:42]</a>.
*   **Benefit:** Longer [[integration_of_large_language_models_in_interactive_agents | Chain of Thought]] paths often correlate with increased model confidence in the final answer <a class="yt-timestamp" data-t="01:18:03">[01:18:03]</a>. This technique can reduce the reliance on prompt engineering, as the model's intrinsic reasoning is uncovered through search in the token space <a class="yt-timestamp" data-t="01:27:01">[01:27:01]</a>.

### Ensemble of Agents
Another approach to improve performance is to use an ensemble of LLM agents in a debate format <a class="yt-timestamp" data-t="01:38:49">[01:38:49]</a>.
*   **Method:** Multiple LLMs are asked the same question, their answers are collected, and a majority vote (based on similarity of embeddings) determines the final answer <a class="yt-timestamp" data-t="01:39:39">[01:39:39]</a>.
*   **Scalability:** The accuracy of the LLM system scales with the number of agents in the ensemble <a class="yt-timestamp" data-t="01:44:10">[01:44:10]</a>. An ensemble of smaller, less powerful models can outperform a single, larger model (e.g., an ensemble of Llama 2 13B models outperforms a single Llama 2 70B model) <a class="yt-timestamp" data-t="01:45:01">[01:45:01]</a>.
*   **Heterogeneous Ensembles:** The method supports ensembling diverse LLMs from different companies, potentially fostering a competitive environment where agent providers strive to offer the most helpful services <a class="yt-timestamp" data-t="01:40:51">[01:40:51]</a>.
*   **Combination:** Ensembling can be combined with [[integration_of_large_language_models_in_interactive_agents | Chain of Thought]] decoding for potentially even better results, albeit with increased computational cost <a class="yt-timestamp" data-t="01:43:02">[01:43:02]</a>.

## Societal and Commercial Implications

### User Interface Transformation
As AI agents become the primary users of applications, user interfaces (UIs) are expected to drastically change. UIs, currently optimized for human usability, will likely optimize for [[agentbased_systems_vs_endtoend_models | agent usability]] and inference cost efficiency. This could lead to UIs that are difficult for humans to use directly <a class="yt-timestamp" data-t="00:36:55">[00:36:55]</a>. For example, a redesigned PowerPoint UI might enable agents to complete tasks in five actions instead of a hundred, leading to significant inference cost savings for companies like Microsoft <a class="yt-timestamp" data-t="00:39:43">[00:39:43]</a>.

### Privacy and Control Concerns
The operation of these agents involves continuous screenshots and data being sent to developers (e.g., Microsoft data centers), raising significant [[legal_and_ethical_considerations_for_ai_agents | privacy concerns]] <a class="yt-timestamp" data-t="00:41:42">[00:41:42]</a>.
*   A "safety model" continually assesses actions, potentially limiting what users can do if deemed "sketchy" or unapproved by the provider <a class="yt-timestamp" data-t="00:41:48">[00:41:48]</a>.
*   This could lead to a future where human control over computers is significantly reduced, resembling the scenario in "2001: A Space Odyssey" where the AI refuses commands <a class="yt-timestamp" data-t="00:42:36">[00:42:36]</a>.

### The Gradual Singularity
The shift to a world dominated by [[generative_ai_agents_and_human_behavior_simulation | AI agents]] is unlikely to be a singular, sudden event. Similar to the widespread adoption of cell phones, which fundamentally changed human behavior over a decade without a specific "singularity" moment, AI integration will likely be a gradual, background process <a class="yt-timestamp" data-t="01:00:13">[01:00:13]</a>. This will transform daily tasks and human skills, with future generations potentially being more adept at voice commands than traditional typing <a class="yt-timestamp" data-t="01:02:50">[01:02:50]</a>.

### Commercial Deployment
Companies like Microsoft are likely to integrate these [[metagpt_and_multiagent_collaborative_frameworks | AI agents]] directly into operating systems (e.g., Windows 12), offering them as built-in products <a class="yt-timestamp" data-t="01:16:38">[01:16:38]</a>. The question remains whether other companies will offer third-party solutions, creating a competitive market, or if OS providers will maintain a "walled garden" approach <a class="yt-timestamp" data-t="01:17:04">[01:17:04]</a>.

## Future Outlook

The rapid pace of research suggests that by the end of 2024, self-operating computers capable of performing daily tasks through natural language will be commonplace <a class="yt-timestamp" data-t="01:15:31">[01:15:31]</a>. Continued scaling of LLMs, coupled with advancements in tokenization (e.g., Karpathy's work on byte-pair encoding for more fundamental tokens) and self-play loops, will drive further progress toward ASI <a class="yt-timestamp" data-t="01:59:16">[01:59:16]</a>. This will lead to a generalist superintelligence capable of performing virtually any task <a class="yt-timestamp" data-t="01:59:54">[01:59:54]</a>.