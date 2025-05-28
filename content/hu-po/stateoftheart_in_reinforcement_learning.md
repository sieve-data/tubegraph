---
title: Stateoftheart in Reinforcement Learning
videoId: H5yd-uh9acY
---

From: [[hu-po]] <br/> 

The "state-of-the-art" in [[AI and Reinforcement Learning|Reinforcement Learning]] (RL) typically refers to performance on specific benchmarks, as RL is a broad and general approach [00:58:00]. If a general impressive demonstration were to be named, AlphaZero would be a strong contender [01:17:09]. [[reinforcement_learning_from_human_feedback|Reinforcement Learning from Human Feedback]] (RLHF) is also cited as a relatively simple but impactful RL algorithm [01:34:00].

## Modern AI Agents: A Manifestation of RL

Recent advancements in AI agent papers demonstrate significant progress in operating complex systems and tasks, often leveraging concepts found in [[AI and Reinforcement Learning|Reinforcement Learning]]. These agents are seen by some as evidence of reaching [[AI and Reinforcement Learning|Artificial General Intelligence]] (AGI) [02:49:00].

### OS Co-pilot (Mac OS)
Released in February 2024, "OS Co-pilot" focuses on developing generalist computer agents with self-improvement capabilities [03:46:00]. Developed by Chinese institutions including the University of Hong Kong, East China Normal University, and Shanghai AI Laboratory, it combines a vision language model with a large language model, specifically GPT-4 Turbo and GPT-4 Vision [04:27:00]. This agent can operate a Mac OS computer autonomously, performing tasks such as:
*   Calculating and drawing charts in Excel [05:03:00]
*   Creating and adjusting website layouts and themes [05:06:00]
*   Playing music [05:10:00]
*   Calculating and filling spreadsheets [05:11:00]
*   Generating files and building them into a web page [05:15:00]

### UFO: A UI-Focused Agent for Windows OS Interaction
Another significant paper, "UFO" (UI Focused Agent), was released in February 2024 by Microsoft [06:32:00]. Similar to OS Co-pilot, UFO uses GPT-4 Vision and GPT-4 to interact with the Windows OS [06:57:00]. Its capabilities include:
*   Extracting information from Word documents [07:39:00]
*   Scrolling through photo applications to find specific figures [07:42:00]
*   Creating PowerPoint presentations [07:44:00]
*   Sending PowerPoint presentations via email [07:50:00]

The agent operates across multiple applications and requires only high-level natural language commands from the user [08:09:00].

## The Rise of Self-Operating Computers
These papers highlight an emerging trend of "self-operating computers," where AI agents autonomously manage operating systems [05:42:00]. While earlier agents predominantly focused on smartphones and interacted via APIs [09:40:00], the new research demonstrates direct interaction with desktop OSs. The speaker suggests that the development of self-operating computers for PCs might precede that for smartphones, as PCs are currently more powerful for running local [[AI and Reinforcement Learning|Vision Language Models]] (VLMs) and [[AI and Reinforcement Learning|Large Language Models]] (LLMs) [10:02:00].

### Architecture and Challenges of Agents
AI agents often follow a "sense-plan-act" loop [1:54:00].
*   **Sensing** involves taking observations (e.g., screenshots), processing user requests, and retrieving historical information from memory [1:59:00].
*   **Planning** is executed by the LLM through internal Chain of Thought processes, where it "thinks out loud" to determine next steps [1:15:00].
*   **Acting** involves interacting with the operating system using programmatic controls via APIs, similar to how the Voyager agent operates in Minecraft [1:55:00].

A common motif in current agent architectures is the use of **memory**, including procedural (tools, functions, APIs) and declarative (user profiles, semantic knowledge) components [12:48:00]. This often involves [[AI and Reinforcement Learning|retrieval augmented generation]], where the LLM loads information from "cold storage" into its context [13:59:00]. However, with models like Gemini 1.5 significantly increasing context window size, the need for complex memory abstraction might diminish [14:54:00].

**Action Grounding** is a technique used to improve the performance of VLMs. This involves annotating screenshots with red rectangles or numbers to highlight clickable elements and facilitate the VLM's understanding of UI elements and their locations [18:10:00]. Google DeepMind's "Pivot Iterative Visual Prompting" paper, which also uses GPT-4V, further illustrates this by drawing arrows on images to elicit "actable knowledge" from VLMs [19:44:00].

The concept of **action tokens** and a predefined **action space** is prevalent, where discrete actions (e.g., specific buttons, joystick movements) are made available to the agent for a given task [29:40:00]. However, the speaker notes that defining a unique action space for every task (e.g., a robot operating in the real world versus an AI playing a video game) presents [[Challenges and Costs in Reinforcement Learning Implementation|a significant hurdle]]. This echoes the limitations of early [[AI and Reinforcement Learning|Deep Reinforcement Learning]] in Atari games, which relied on fixed action spaces [31:20:00]. The speaker predicts a shift towards text-based action spaces, where the agent generates functions or commands in natural language, making it compatible with any task that can be formulated in text [32:55:00].

### Impact on User Interfaces
The proliferation of AI agents could lead to **drastic changes in user interfaces (UIs)**. Current UIs are designed for human usability, but as AI agents become the primary users of applications, UIs may optimize for "agent usability." This could lead to simpler, more efficient UIs for machines, potentially making them less intuitive for human interaction [37:27:00]. This optimization would also be driven by a monetary incentive for companies to reduce the number of inferences (and thus cost) required for agents to perform tasks [38:54:00].

## Advancements in LLM Reasoning and Collaboration

Beyond direct interaction, research also explores improving LLM reasoning and leveraging multiple agents.

### Chain of Thought Reasoning Without Explicit Prompting
A Tencent paper, "Chain of Thought Reasoning Without Prompting," explores eliciting Chain of Thought reasoning paths from pre-trained LLMs by altering the decoding process, rather than requiring explicit prompting [01:13:40].
*   **Greedy Decoding vs. Alternative Tokens:** Traditionally, LLMs use greedy decoding, picking the single most probable next token [01:14:52]. However, by investigating the top-K alternative tokens (even just the top 10), researchers found that Chain of Thought paths often exist intrinsically within these sequences [01:15:01].
*   **Higher Confidence in CoT Paths:** Paths that lead to correct answers often emerge from these alternative token sequences and exhibit higher confidence in the final answer [01:18:03].
*   **Reduced Reliance on Prompt Engineering:** This approach reduces the need for extensive prompt engineering tricks (like "think step by step") to elicit Chain of Thought [02:03:55]. As models grow larger, this decoding method becomes less critical, suggesting that eventually, sufficiently large models may inherently perform complex reasoning without specialized prompting [02:50:00].

### More Agents Is All You Need (Ensembling LLMs)
Another Tencent paper, "More Agents Is All You Need," demonstrates that LLM performance scales with the number of agents used in an ensemble [01:39:01].
*   **Ensemble Power:** By asking multiple LLMs a question, gathering their answers, and using a similarity function for "majority voting," the collective response can outperform a single LLM, even a significantly larger one [01:44:23].
*   **Heterogeneous Ensembles:** The framework is compatible with heterogeneous LLMs, meaning different models from different companies can be combined [01:40:51]. This opens up the possibility of users building "teams" of agents from various providers, fostering competition and potentially increasing user control over their AI tools [01:41:00].
*   **Combinatorial Improvement:** This ensembling technique could be combined with Chain of Thought decoding for even better performance, albeit at a higher computational cost [01:42:58].

## Future Implications
The speaker emphasizes that these advancements, particularly in [[Reinforcement learning and selfplay in AI development|self-play loops]] for training and the continuous scaling of models, indicate a rapid progression towards [[AI and Reinforcement Learning|Artificial Superintelligence]] (ASI) [01:59:11]. The ability of models to learn from seemingly unrelated domains (e.g., [[Applications in machine learning and reinforcement learning|robotics and gaming data improving healthcare diagnostics]]) suggests broad positive transfer of knowledge [02:01:01]. This could render attempts by incumbents (like in healthcare or legal fields) to restrict data access ineffective, as AIs might achieve superhuman capabilities through self-generated data and internal "debates" [02:56:00].

The speaker also speculates on a future where human interaction with computers primarily involves speech-based commands to AI agents, potentially leading to a decline in traditional skills like typing and mouse usage [02:11:00]. The ability to learn and adapt may become a distinguishing characteristic of current generations compared to future ones who might rely entirely on AI for task completion [02:09:51]. This ongoing technological shift is described as a "singularity" that unfolds gradually, rather than a single, sudden event [01:00:13].

The overall trend points towards simpler, more generic, and highly capable multimodal models that can consume and output various types of tokens (text, visual, action) from a vast, universal vocabulary, eliminating the need for task-specific tokenization and complex architectural frameworks [01:58:47].