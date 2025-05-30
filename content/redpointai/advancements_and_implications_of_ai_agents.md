---
title: Advancements and implications of AI agents
videoId: AU9Fdgs0ZaI
---

From: [[redpointai]] <br/> 

AI agents, also known as Large Action Models (LAMs), represent a significant frontier in artificial intelligence, moving beyond mere language generation to enabling models to take actions and interact with the world <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. David Luan, Head of the AGF Lab at Amazon and former co-founder of Adept, highlights the challenges and opportunities in this space <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Current State and Challenges of AI Agents
Early powerful Large Language Models (LLMs) like GPT-4, while capable of tasks like generating rap songs or performing three-digit addition, struggled with real-world actions such as ordering a pizza <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. This highlighted a major gap in their utility <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. The shift to agents involves enabling LLMs to use tools and decide when to perform actions <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

A primary challenge for agents is **reliability** <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. Early models, primarily behavioral cloners, tend to "go off the rails" when encountering unforeseen situations, leading to unpredictable behavior <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>. For enterprise adoption, such as invoice processing, agents must achieve near-perfect reliability, as even a small error rate (e.g., deleting a third of QuickBooks entries one in seven times) renders them unusable <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.

Currently, systems like "Operator" show impressive capabilities, but their end-to-end reliability for complex tasks is still very low, requiring frequent human intervention <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. The goal is for businesses to trust agents in a "fire and forget" manner <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.

## Advancements in Agent Development
To transform a base multimodal model into a Large Action Model (LAM), two main problems must be solved:
1.  **Engineering Problem:** Exposing what the model can do in a "model-legible" way, including APIs, UI elements, and teaching it about specific applications like Expedia or SAP <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.
2.  **Research Problem:** Teaching the model to plan, reason, replan, follow user instructions, and even infer user intent <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. This multi-step decision-making process involves backtracking, predicting action consequences, and understanding potential dangers (e.g., a "delete button") <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.

This development aligns with a progression seen in AI model training: pre-training (exposition), supervised fine-tuning (sample problems), and Reinforcement Learning (RL) (open-ended problems with answers in the back) <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.

### The Role of Reinforcement Learning (RL)
A key insight for advancing [[challenges_and_advancements_in_ai_technology | AI technology]] is that LLMs, by design, are penalized for discovering new knowledge because it wasn't part of their training data <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. To overcome this, combining LLMs with RL and search paradigms is crucial <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. RL, demonstrated by successes like AlphaGo, enables models to discover new knowledge <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This integration allows systems to leverage existing human knowledge while also building upon it <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

Models are also better at verifying their own work than generating correct answers, and RL exploits this by forcing models to repeatedly try to satisfy their internal sense of correctness <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

### Engineering as a Bottleneck
The development of advanced AI models and agents is shifting from "alchemy to industrialization" <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. A modern AI lab's job is to build a "factory that reliably turns out models," which requires significant investment in repeatability and infrastructure <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. Key engineering challenges include:
*   Managing massive computing clusters reliably over long periods, ensuring that job progress isn't lost if a node fails <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   Developing systems where data centers perform local inference, learn from new customer environments, and send new knowledge back to a centralized model for continuous improvement <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

## Implications and Future Outlook
### Generalization and Original Thinking
Models are capable of generalizing more broadly than often assumed <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. Improvements in verifiable domains (like coding and math) can transfer to fuzzier problems (like healthcare or law) <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. Examples from Open AI's early work with RL in flash games showed models discovering novel "speedrun techniques" (e.g., glitching through walls) that humans hadn't performed before, demonstrating original thinking <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

### [[future_of_ai_agents_in_productivity_tools | Future of AI Agents in Productivity Tools]]
The main milestone for agents is achieving 100% task completion during training <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>. This is analogous to the self-driving car problem, where impressive demos existed years ago, but full reliability is still elusive <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>. The belief is that with the right tools and training recipes, agents can achieve a level of reliability similar to "Level 4" self-driving, where they can execute any task perfectly after sufficient training time <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>.

### Human-Computer Interaction
Current human-AI interfaces, primarily chat-based, are "low bandwidth" and limit what can be achieved, akin to early, simplistic iPhone apps <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>. Future interfaces should be more dynamic and multimodal, with agents synthesizing custom UIs to best elicit information from users and foster shared context between human and AI <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. The goal is to increase the "leverage per unit energy a human spends with computing" <a class="yt-timestamp" data-t="00:25:10">[00:25:10]</a>. This includes ambient computing and other new tools, alongside existing interfaces like command lines and GUIs <a class="yt-timestamp" data-t="00:24:57">[00:24:57]</a>.

### [[enterprise_adoption_of_ai_agents | Enterprise Adoption of AI Agents]] and Market Dynamics
While there is some uncertainty, it's predicted that [[impact_of_ai_advancements_on_business_models | AGI (Artificial General Intelligence)]] (defined as a model capable of doing anything useful a human does on a computer and learning as fast as a generalist human) is "really not super far away" <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>. However, the diffusion of this technology into society will likely lag behind the technical capability, creating a "capability overhang" <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>. The bottleneck for adoption will be "people and processes," including social acceptance and figuring out how to co-design interfaces with human users <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>. This creates a significant opportunity for startups to bridge the gap between advanced model capabilities and end-user needs <a class="yt-timestamp" data-t="00:23:49">[00:23:49]</a>.

### Specialized vs. Generalist Models
Specialized models will exist, not primarily for technical reasons, but due to policy considerations, such as companies not wanting their data comingled or divisions within a company requiring information barriers (e.g., sales and trading vs. investment banking at a bank) <a class="yt-timestamp" data-t="00:25:45">[00:25:45]</a>.

### AI Robotics and World Models
Digital agents offer an opportunity to de-risk hard problems in physical agents by solving reliability in a simulated or digital space first, before engaging with costly real-world deployments <a class="yt-timestamp" data-t="00:34:11">[00:34:11]</a>. If 100% task reliability can be achieved in the digital space, it will likely transfer to the physical space <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>.

Another major open problem is developing "world models" <a class="yt-timestamp" data-t="00:36:04">[00:36:04]</a>. While RL can work where explicit verifiers or simulators exist (e.g., theorem proving, staging environments for apps), world modeling is the answer for problems without such explicit feedback mechanisms <a class="yt-timestamp" data-t="00:36:46">[00:36:46]</a>. This also relates to video models and their understanding of physics for open-ended exploration <a class="yt-timestamp" data-t="00:36:02">[00:36:02]</a>.

### [[state_and_future_of_ai_agents | State and Future of AI Agents]]
The overall [[effectiveness_of_ai_agents | effectiveness of AI agents]] is rapidly improving, with model progress this year expected to be even greater than last year, despite appearing similar on the surface <a class="yt-timestamp" data-t="00:42:43">[00:42:43]</a>. Underhyped aspects include solving extremely large-scale simulation for models to learn from <a class="yt-timestamp" data-t="00:43:07">[00:43:07]</a>. The belief is that the remaining open problems are solvable without needing fundamentally new computational paradigms like quantum computers or replacing gradient descent <a class="yt-timestamp" data-t="00:26:54">[00:26:54]</a>.

David Luan's experience at OpenAI highlighted the importance of team culture – hiring intrinsically motivated, intellectually flexible individuals, often earlier in their careers <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>. This approach fosters adaptation as the "optimal playbook changes" every few years <a class="yt-timestamp" data-t="00:32:37">[00:32:37]</a>. He also notes that [[challenges_and_advancements_in_ai_model_development | technical differentiation]] in AI models doesn't always compound as expected; breakthroughs in one area (e.g., text modeling) don't deterministically guarantee leadership in subsequent areas (e.g., multimodal, reasoning, agents) <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.