---
title: Progress and bottlenecks in AI and robotics
videoId: AU9Fdgs0ZaI
---

From: [[redpointai]] <br/> 

This article explores the current state, advancements, and persistent challenges within the fields of AI and robotics, drawing insights from industry leaders.

## Current State of AI Models

The AI landscape is rapidly evolving, with significant strides made in model efficiency and capability.

### Deep Seek and Model Efficiency

The emergence of models like Deep Seek R1 has highlighted a shift towards increased efficiency in AI systems <a class="yt-timestamp" data-t="02:44:11">[02:44:11]</a>. Initially, there was a perception that more efficient intelligence might reduce the demand for intelligence itself, causing market reactions like the NVIDIA stock crash <a class="yt-timestamp" data-t="01:40:02">[01:40:02]</a>. However, the market has since come to understand that increased efficiency tends to *increase* the consumption of intelligence, leading to a return to sanity <a class="yt-timestamp" data-t="02:50:52">[02:50:52]</a>.

A key trend observed is the training of "humongous teacher models" on vast compute resources, which are then distilled internally into faster, more efficient versions for customers <a class="yt-timestamp" data-t="03:34:25">[03:34:25]</a>. This approach makes previous levels of intelligence "so cheap as to be commoditized" <a class="yt-timestamp" data-t="04:17:51">[04:17:51]</a>.

### Limitations of Next Token Prediction and the Role of RL

Early discussions pondered whether next-token prediction alone could achieve AGI <a class="yt-timestamp" data-t="05:05:08">[05:05:08]</a>. The prevailing view became that an LLM trained purely on next-token prediction is penalized for discovering new knowledge, as new knowledge wasn't part of its training set <a class="yt-timestamp" data-t="05:16:16">[05:16:16]</a>.

The solution involves combining Large Language Models (LLMs) with Reinforcement Learning (RL) and search paradigms <a class="yt-timestamp" data-t="05:43:53">[05:43:53]</a>. While RL alone (as seen in early DeepMind work with randomly initialized models) would take an immense amount of time to rediscover basic human knowledge, combining it with LLMs allows systems to leverage existing human knowledge and build upon it <a class="yt-timestamp" data-t="05:53:35">[05:53:35]</a>.

### Generalization to Complex Domains

There's debate on whether this "test time compute" paradigm can extend to domains that are not easily verifiable, such as healthcare or law <a class="yt-timestamp" data-t="06:26:26">[06:26:26]</a>. The strong view is that these models are "better at generalizing than you think" <a class="yt-timestamp" data-t="06:45:03">[06:45:03]</a>. Improving models through problems with explicit verification (like math or coding) can lead to transfer effects on "slightly fuzzier problems" in similar domains <a class="yt-timestamp" data-t="07:04:47">[07:04:47]</a>. The core principle being exploited is that models are generally better at determining if they did a good job than at generating the correct answer initially <a class="yt-timestamp" data-t="08:05:04">[08:05:04]</a>. RL is used to force the model to iteratively try to satisfy its own sense of a good outcome <a class="yt-timestamp" data-t="08:11:47">[08:11:47]</a>.

## [[Challenges and advancements in AI technology|Challenges and Advancements in AI Technology]]

The development of advanced AI models involves overcoming significant technical and organizational hurdles.

### Research and Engineering Problems

Solving the research problems required to release models like Deep Seek involves:
1.  **Organizational Structure**: Building an organization and process to reliably produce models. The job of a modern AI lab is to "build a factory that reliably turns out models" <a class="yt-timestamp" data-t="08:51:24">[08:51:24]</a>. This represents a shift from "alchemy to industrialization" <a class="yt-timestamp" data-t="09:16:03">[09:16:03]</a>.
2.  **Engineering Infrastructure**: Mastering large-scale clusters to reliably push the frontier at scale, ensuring jobs aren't wasted if nodes fail <a class="yt-timestamp" data-t="09:48:47">[09:48:47]</a>.
3.  **RL for Human Preferences**: Working to learn human preferences for complex tasks and then using RL to satisfy them <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>.

### Debunking Limitations: Original Thinking

Some critics, like Yann LeCun, have highlighted perceived limitations of LLMs regarding original thinking <a class="yt-timestamp" data-t="10:25:22">[10:25:22]</a>. However, counter-examples demonstrate AI's capacity for original thought:
*   **AlphaGo**: Showed the ability to discover new knowledge <a class="yt-timestamp" data-t="10:42:07">[10:42:07]</a>.
*   **OpenAI's Flash Games Work**: RL algorithms learned "speedrun techniques by like glitching through walls" to solve levels, which humans had never done <a class="yt-timestamp" data-t="11:09:59">[11:09:59]</a>.

### Data Labeling and Training

Data remains crucial, serving two main purposes:
1.  **Basic Task Learning**: Teaching models the basics of a task by cloning human behavior using high-quality data <a class="yt-timestamp" data-t="31:17:15">[31:17:15]</a>.
2.  **Fuzzy Task Evaluation**: Teaching models what "good and bad" looks like for subjective or complex tasks <a class="yt-timestamp" data-t="31:31:00">[31:31:00]</a>.
The middle ground of "spamming human data labels to marginally improve models" is becoming the job of RL <a class="yt-timestamp" data-t="31:47:29">[31:47:29]</a>.

## The Agent Space

AI agents, sometimes referred to as "large action models" (LAMs), represent a significant frontier in AI.

### Current State and Reliability

Early LLMs struggled with basic real-world tasks like ordering a pizza, instead "cosplay[ing] being like a Domino's Pizza rep" <a class="yt-timestamp" data-t="12:07:44">[12:07:44]</a>. This highlighted a major gap in utility <a class="yt-timestamp" data-t="12:14:14">[12:14:14]</a>.

Early agent development, such as work at Adept, focused on "useful intelligence" and reliability over viral demos <a class="yt-timestamp" data-t="14:04:14">[14:04:14]</a>. A key challenge was the "behavioral cloner" nature of early LLMs, making them prone to unpredictable behavior when encountering unseen situations <a class="yt-timestamp" data-t="14:43:58">[14:43:58]</a>. For tasks like invoice processing, reliability is paramount; a model deleting QuickBooks entries even one in seven times renders it unusable <a class="yt-timestamp" data-t="14:43:58">[14:43:58]</a>.

Current agents, while impressive, still struggle with end-to-end reliability for complex tasks, often requiring significant human intervention <a class="yt-timestamp" data-t="15:17:34">[15:17:34]</a>. The goal is to reach a point where businesses can "fire and forget" tasks to agents <a class="yt-timestamp" data-t="15:29:43">[15:29:43]</a>.

### Developing Large Action Models

Turning a base multimodal model into a large action model involves two main components:
1.  **Engineering Problem**: Exposing what the model "can do" in a "model legible way," such as APIs or UI elements, and teaching it about specific platforms (e.g., Expedia, SAP) <a class="yt-timestamp" data-t="15:46:11">[15:46:11]</a>.
2.  **Research Problem**: Teaching the model to plan, reason, replan, follow user instructions, and even infer user intent <a class="yt-timestamp" data-t="16:18:14">[16:16:18]</a>. This differs from typical LLM work as it involves multi-step decision-making, backtracking, predicting action consequences, and understanding concepts like a "delete button is probably dangerous" <a class="yt-timestamp" data-t="16:59:44">[16:59:44]</a>. Models are then set loose in sandboxes to learn independently <a class="yt-timestamp" data-t="17:19:14">[17:19:19]</a>.

### Milestones and Future Outlook for Agents

The primary milestone for agents is a "recipe where I can hand this agent in training any task and come back N days later and it's 100% at it" <a class="yt-timestamp" data-t="21:11:47">[21:11:47]</a>. This means the agent autonomously figures out how to solve the problem reliably, rather than relying on human fine-tuning for marginal improvements <a class="yt-timestamp" data-t="21:29:00">[21:29:00]</a>.

## [[Prospects and challenges in robotics and AI integration|Prospects and Challenges in Robotics and AI Integration]]

Robotics, particularly physical agents, stands to benefit significantly from advancements in AI.

### Digital Agents as a De-risking Step

The current state of AI and robotics suggests that many "raw materials" for physical agents are available <a class="yt-timestamp" data-t="34:06:06">[34:06:06]</a>. Digital agents offer an opportunity to de-risk hard problems in physical agents before incurring the high costs of real-world implementation <a class="yt-timestamp" data-t="34:11:30">[34:11:30]</a>. For example, optimizing a warehouse layout can first be learned in a digital space, where training recipes and algorithms for simulated data can be perfected before deployment in the physical world <a class="yt-timestamp" data-t="34:31:00">[34:31:00]</a>. The confidence in robotics progress stems from the ability to build training recipes that achieve 100% task completion in the digital space, believing it will transfer to the physical <a class="yt-timestamp" data-t="35:32:00">[35:32:00]</a>.

### Timelines for Robots in the Home

Similar to other AI applications, the bottleneck for widespread adoption of home robots is not solely modeling capability but rather the "diffusion of the modeling" <a class="yt-timestamp" data-t="35:48:00">[35:48:00]</a>.

### Video Models and World Models

Video models and "world models" are crucial for solving complex problems where explicit verifiers or simulators are absent <a class="yt-timestamp" data-t="36:44:11">[36:44:11]</a>. These models represent a major step towards understanding and interacting with physics, allowing for more open-ended exploration in AI systems <a class="yt-timestamp" data-t="36:04:11">[36:04:11]</a>.

## [[Challenges and opportunities in AI integration|Challenges and Opportunities in AI Integration]]

Integrating AI into society and various domains presents its own set of [[Challenges and future directions for AI in various domains|challenges and opportunities]].

### The Definition and Diffusion of AGI

AGI is defined as a model that can perform "anything useful that a human does on a computer" and "learn how to do that thing as fast as a generalist human can" <a class="yt-timestamp" data-t="22:10:00">[22:10:00]</a>. While AGI is considered "not super far away" <a class="yt-timestamp" data-t="22:05:00">[22:05:00]</a>, its diffusion through society is expected to be slow. This is due to "Amdahl's Law" – speeding up one part of a process often uncovers other bottlenecks <a class="yt-timestamp" data-t="22:42:00">[22:42:00]</a>. A significant "capability overhang" will exist where society's ability to productively use these new technologies lags behind the technological advancements <a class="yt-timestamp" data-t="22:57:00">[22:57:00]</a>.

The main "gaining factor" will be people and processes, including co-designing interfaces, startup decisions on model usage, and social acceptance <a class="yt-timestamp" data-t="23:10:00">[23:10:00]</a>.

### Future of Human-Computer Interaction

Humanity's interaction with computers will evolve, gaining "new quivers" or tools in the toolbox <a class="yt-timestamp" data-t="24:37:00">[24:37:00]</a>. This includes continued use of command lines, GUIs, voice interfaces, and more "ambient computing" <a class="yt-timestamp" data-t="24:49:00">[24:49:00]</a>. The ultimate metric is the "amount of leverage per unit energy a human spend[s] with Computing," which is expected to "continue to go up and to the right" <a class="yt-timestamp" data-t="25:10:00">[25:10:00]</a>.

### Specialized Models

Specialized models are anticipated, not primarily for technical reasons, but for "policy reasons" <a class="yt-timestamp" data-t="25:44:00">[25:44:00]</a>. This includes concerns about data commingling between companies or internal divisions (e.g., sales and trading vs. investment banking within a bank) <a class="yt-timestamp" data-t="25:51:00">[25:51:00]</a>. However, even specialized models would benefit from a "general college degree" (broad basic facts) before specialization <a class="yt-timestamp" data-t="25:32:00">[25:32:00]</a>.

## [[Challenges in AI research and potential solutions|Challenges in AI Research and Potential Solutions]]

Beyond technical hurdles, the nature of AI research itself presents challenges.

### Team Culture and Technical Differentiation

A significant shift in perspective is the increasing importance of building the right team culture <a class="yt-timestamp" data-t="32:08:00">[32:08:00]</a>. Hiring smart, energetic, intrinsically motivated people earlier in their careers is seen as a highly effective engine for progress <a class="yt-timestamp" data-t="32:16:00">[32:16:00]</a>. This is because the "optimal playbook changes" every couple of years, and those "overfit to the previous optimal playbook" can hinder progress <a class="yt-timestamp" data-t="32:37:00">[32:37:00]</a>.

A surprising realization is the "little compounding" in technical differentiation <a class="yt-timestamp" data-t="33:00:00">[33:00:00]</a>. The idea that being good at text modeling would automatically lead to success in multimodal, reasoning, or agents hasn't held true as strongly as once thought <a class="yt-timestamp" data-t="33:07:00">[33:07:00]</a>. Labs are often "trying relatively similar ideas," and breakthroughs don't necessarily chain deterministically from prior successes <a class="yt-timestamp" data-t="33:18:00">[33:18:00]</a>.

### Evaluation and Benchmarks

Evaluating new models is challenging. While benchmarks exist, they are often "gamed" and not perfectly aligned with what people truly need from the models <a class="yt-timestamp" data-t="28:05:00">[28:05:00]</a>. Many labs rely on internal evaluations that they trust more than public benchmarks <a class="yt-timestamp" data-t="28:40:00">[28:40:00]</a>. More prestige and attention should be given to the difficulty of measurement in AI <a class="yt-timestamp" data-t="28:31:00">[28:31:00]</a>.

### OpenAI's Early Culture

The success of OpenAI during the GPT-1 through GPT-4 era was attributed to specific cultural aspects:
*   **Blurred Lines**: Blurring the lines between research and engineering <a class="yt-timestamp" data-t="37:51:00">[37:51:00]</a>.
*   **Scientific Goals**: Focusing on "major scientific goals" with large, combined teams of researchers and engineers, regardless of whether solutions were considered "novel" by academic standards <a class="yt-timestamp" data-t="39:01:00">[39:01:00]</a>.
*   **Betting on Talent**: Betting on intrinsically motivated individuals, often earlier in their careers and without traditional academic credentials (e.g., PhDs) <a class="yt-timestamp" data-t="39:39:00">[39:39:00]</a>. Key traits observed in successful researchers include "intrinsic motivation and intellectual flexibility" <a class="yt-timestamp" data-t="40:20:00">[40:20:00]</a>.

### NVIDIA's Impact

NVIDIA's success is deeply admired due to strategic long-term decisions:
*   **In-house Interconnect**: Bringing interconnect technology in-house <a class="yt-timestamp" data-t="42:22:00">[42:22:00]</a>.
*   **Systems-Oriented Business**: Choosing to orient their business around systems rather than just individual components <a class="yt-timestamp" data-t="42:28:00">[42:28:00]</a>.

## Future [[Future development areas for AI and efficiency optimizations|Development Areas for AI and Efficiency Optimizations]]

While progress is rapid, key areas for future focus remain.

### Overhyped vs. Underhyped Concepts

*   **Overhyped**: The idea that "scale is dead" and we should stop investing in chips <a class="yt-timestamp" data-t="42:54:00">[42:54:00]</a>.
*   **Underhyped**: How to solve "extremely large scale simulation" for models to learn from <a class="yt-timestamp" data-t="43:07:00">[43:07:00]</a>.

> [!NOTE] Model Progress
> Visibly, model progress this year may appear similar to last year, but in reality, it will be more significant <a class="yt-timestamp" data-t="42:43:00">[42:43:00]</a>.
