---
title: Challenges and future directions for AI in various domains
videoId: AU9Fdgs0ZaI
---

From: [[redpointai]] <br/> 

The field of AI is rapidly evolving, presenting both significant [[challenges_and_advancements_in_ai_technology | challenges and advancements in AI technology]] and new opportunities across diverse domains. David Luan, Head of the AGF Lab at Amazon and former VP of Engineering at OpenAI, shares insights into the current state and future trajectory of AI, particularly focusing on agents, model development, and integration into society <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>.

## Evolution of AI Models and Efficiency

Early concerns arose regarding the implications of models like DeepSeek, which suggested that intelligence could be produced at a lower cost <a class="yt-timestamp" data-t="02:26">[02:26]</a>. Initially, this led to market fears, but it was quickly understood that increased efficiency doesn't reduce consumption of intelligence; rather, it often increases it <a class="yt-timestamp" data-t="02:52">[02:52]</a>.

A key trend in AI development is the training of "humongous teacher models" on vast compute resources, which are then refined internally into more efficient, faster-running models for customers <a class="yt-timestamp" data-t="03:30">[03:30]</a>. This approach aims to make every preceding "ring of intelligence" so cheap as to be commoditized <a class="yt-timestamp" data-t="04:16">[04:16]</a>.

## The Path to AGI and New Knowledge Discovery

The path to Artificial General Intelligence (AGI) is not solely about next-token prediction, as Large Language Models (LLMs) are penalized for discovering new knowledge not present in their training data <a class="yt-timestamp" data-t="05:05">[05:05]</a>. The solution involves combining LLMs with Reinforcement Learning (RL) and search paradigms, which are capable of discovering new knowledge <a class="yt-timestamp" data-t="05:27">[05:27]</a>. Examples like AlphaGo demonstrate the ability of RL to find novel solutions that humans haven't explored <a class="yt-timestamp" data-t="05:37">[05:37]</a>.

The challenge with pure RL approaches, like those initially pursued by DeepMind, was their random initialization, meaning they would take immense time to "rediscover human language" or complex human processes like filing taxes <a class="yt-timestamp" data-t="05:53">[05:53]</a>. The current successful models combine the vast knowledge contained in LLMs with RL's ability to build upon that knowledge <a class="yt-timestamp" data-t="06:19">[06:19]</a>.

## Generalization Across Diverse Domains

A significant debate exists regarding whether AI models, particularly those excelling in verifiable domains like coding and math, can generalize to "fuzzier" problems in sectors like healthcare or law <a class="yt-timestamp" data-t="06:26">[06:26]</a>. David Luan believes these models are "better at generalizing than you think" <a class="yt-timestamp" data-t="06:45">[06:45]</a>. Improvements in test-time compute for explicit, verifiable problems are already showing transfer to slightly fuzzier, similar domains <a class="yt-timestamp" data-t="07:04">[07:04]</a>.

The field is actively working on leveraging RL to satisfy human preferences for more complicated tasks, even when direct verification (like a math proof) is not possible <a class="yt-timestamp" data-t="07:23">[07:23]</a>. The fundamental principle is that models are often better at determining if they've done a good job than they are at generating the correct answer initially <a class="yt-timestamp" data-t="08:05">[08:05]</a>. This gap is exploited by RL, which forces the model to iterate until it satisfies its own sense of a good outcome <a class="yt-timestamp" data-t="08:11">[08:11]</a>. This has implications for [[challenges_and_opportunities_in_ai_applications_for_legal_and_education_sectors | AI applications for legal and education sectors]], where complex problem-solving and nuanced understanding are crucial.

## Research and Engineering [[challenges_in_ai_research_and_potential_solutions | Challenges in AI Research and Potential Solutions]]

Building advanced AI models involves several research problems:
1.  **Organizational and Process Challenges**: Establishing a reliable factory that consistently produces models, shifting from "Alchemy to industrialization" <a class="yt-timestamp" data-t="08:40">[08:40]</a>. This requires significant investment in repeatability and infrastructure <a class="yt-timestamp" data-t="09:03">[09:03]</a>.
2.  **Engineering for Scale**: Beyond algorithms, the engineering challenge of managing massive, reliable clusters that can operate for extended periods without wasting time due to node failures is crucial for pushing the frontier of AI <a class="yt-timestamp" data-t="09:45">[09:45]</a>. This relates directly to [[challenges_and_opportunities_in_ai_infrastructure_development | challenges and opportunities in AI infrastructure development]] and [[trends_and_challenges_in_ai_infrastructure | trends and challenges in AI infrastructure]].
3.  **Data Labeling and RL**: Data remains vital for two primary purposes:
    *   Teaching models the basics of a task by cloning human behavior with high-quality data <a class="yt-timestamp" data-t="31:15">[31:15]</a>.
    *   Teaching models "what good and bad looks like" for fuzzy tasks, especially through RL <a class="yt-timestamp" data-t="31:31">[31:31]</a>. The "middle chunk" of spamming human data labels for marginal improvements will likely be superseded by RL <a class="yt-timestamp" data-t="31:44">[31:44]</a>.

## The Agent Space: From "Tool Use" to Reliability

The concept of AI agents, initially called "tool use" or "large action models," aims to bridge the gap between LLMs' conversational abilities and their inability to perform real-world actions like ordering a pizza <a class="yt-timestamp" data-t="12:07">[12:07]</a>. Early agent development, such as that at Adept, required building everything from scratch, including custom models, due to the lack of powerful open-source or multimodal LLMs at the time <a class="yt-timestamp" data-t="13:03">[13:03]</a>.

A major [[challenges_and_strategies_in_ai_deployment | challenge in AI deployment]] for agents is reliability. Early LLMs, being "behavioral cloners," tend to go "off the rails" when encountering situations outside their training data, leading to unpredictable actions <a class="yt-timestamp" data-t="13:44">[13:44]</a>. For practical applications like invoice processing, even a small error rate (e.g., deleting QuickBooks entries one in seven times) renders the system unusable <a class="yt-timestamp" data-t="14:44">[14:44]</a>. Current end-to-end agent performance for complex tasks remains low, often requiring significant human intervention <a class="yt-timestamp" data-t="15:17">[15:17]</a>. The goal is "fire and forget" reliability for businesses <a class="yt-timestamp" data-t="15:29">[15:29]</a>.

Transforming a base multimodal model into a large action model involves:
1.  **Engineering**: Exposing to the model, in a legible way, what actions it can take, such as API calls or UI interactions, and teaching it how specific applications (e.g., expedia.com or SAP) work <a class="yt-timestamp" data-t="15:46">[15:46]</a>.
2.  **Research**: Teaching the model to plan, reason, replan, follow user instructions, and infer user intent <a class="yt-timestamp" data-t="16:18">[16:18]</a>. This multi-step decision-making process involves backtracking, predicting consequences of actions, and understanding dangerous actions (like a delete button) <a class="yt-timestamp" data-t="17:00">[17:00]</a>. Models are then set loose in sandboxes to learn independently <a class="yt-timestamp" data-t="17:19">[00:17:19]</a>.

## Interface Design for AI and Societal Diffusion

A significant [[challenges_and_opportunities_in_ai_integration | challenge and opportunity in AI integration]] lies in the lack of creativity in how people interface with increasingly smart LLMs and agents <a class="yt-timestamp" data-t="18:22">[18:22]</a>. Current chat-based interfaces are low-bandwidth and limiting <a class="yt-timestamp" data-t="18:50">[18:50]</a>. The next step involves product designers deeply understanding model limitations and technologists focusing on end-to-end user experience, leading to multimodal user interfaces that synthesize information and maintain shared context between humans and AI <a class="yt-timestamp" data-t="19:12">[19:12]</a>. The future vision is one where humans and AI operate "more like parallel rather than perpendicular" <a class="yt-timestamp" data-t="20:00">[20:00]</a>.

While AGI (defined as a model that can perform any useful human task on a computer, or learn as fast as a generalist human) may not be far off, its societal diffusion will likely be slow <a class="yt-timestamp" data-t="22:03">[22:03]</a>. Amdahl's Law suggests that speeding up one part of a system creates new bottlenecks <a class="yt-timestamp" data-t="22:42">[22:42]</a>. The "capability overhang" means society's ability to productively use these technologies will lag <a class="yt-timestamp" data-t="22:57">[22:57]</a>. The gaining factors will be people, processes, co-design of interfaces, and social acceptance <a class="yt-timestamp" data-t="23:10">[23:10]</a>. This creates an opportunity for startups to bridge the gap between model capabilities and user needs <a class="yt-timestamp" data-t="23:44">[23:44]</a>.

## [[prospects_and_challenges_in_robotics_and_ai_integration | Prospects and Challenges in Robotics and AI Integration]]

AI in robotics is seen as having many "raw materials" ready <a class="yt-timestamp" data-t="34:06">[34:06]</a>. Digital agents offer an opportunity to de-risk hard problems in physical agents before costly real-world deployment <a class="yt-timestamp" data-t="34:13">[34:13]</a>. For example, solving reliability in a digital warehouse simulation provides valuable training recipes and know-how before deploying physical robots <a class="yt-timestamp" data-t="34:30">[34:30]</a>. The ability to build training recipes that achieve 100% task completion in the digital space will ultimately transfer to the physical space <a class="yt-timestamp" data-t="35:31">[35:31]</a>. However, the bottleneck for household robots might still be the diffusion of the technology, not just the modeling <a class="yt-timestamp" data-t="35:48">[35:48]</a>.

## Video Models and World Modeling

The development of video models is crucial for solving a major remaining problem in AI: what happens when there is no explicit verifier or simulator for a task <a class="yt-timestamp" data-t="36:44">[36:44]</a>. World modeling is seen as the answer to this question, allowing for more open-ended exploration and understanding of physics <a class="yt-timestamp" data-t="36:04">[36:04]</a>, which is particularly relevant for [[challenges and opportunities in creative AI tools | creative AI tools]] as well.

## Specialized Models

The future will likely see specialized AI models, not necessarily for technical reasons, but for policy reasons <a class="yt-timestamp" data-t="25:45">[25:45]</a>. This could be due to companies not wanting their data commingled or regulatory requirements preventing information sharing between different divisions of a large organization (e.g., a bank's sales and trading vs. investment banking divisions) <a class="yt-timestamp" data-t="25:51">[25:51]</a>.

## Organizational Culture and Future of AI Labs

One key lesson learned is the paramount importance of building the right team culture <a class="yt-timestamp" data-t="32:08">[32:08]</a>. Hiring smart, energetic, intrinsically motivated people, especially earlier in their careers, is a powerful engine for progress <a class="yt-timestamp" data-t="32:16">[32:16]</a>. This is because the optimal playbook for AI development changes every couple of years, and individuals too "overfit" to previous playbooks can slow progress <a class="yt-timestamp" data-t="32:37">[32:37]</a>.

Early success at OpenAI was attributed to blurring the lines between research and engineering and a differentiated research strategy that focused on major scientific goals solved by larger, combined teams, regardless of whether solutions were "novel" by academic standards <a class="yt-timestamp" data-t="38:51">[38:51]</a>.

David Luan also noted a shift in perspective regarding technical differentiation: previous assumptions that mastery in one area (e.g., text modeling) would automatically lead to dominance in others (e.g., multimodal, reasoning, agents) have proven less true in practice <a class="yt-timestamp" data-t="32:51">[32:51]</a>. There's "so little compounding" because different labs are pursuing "relatively similar ideas" <a class="yt-timestamp" data-t="33:16">[33:16]</a>. While correlation exists between being ahead in one area and subsequent breakthroughs, it's not deterministic <a class="yt-timestamp" data-t="33:46">[33:46]</a>. Losing focus is seen as a significant danger for large AI companies <a class="yt-timestamp" data-t="41:44">[41:44]</a>.

## Future of Human-Computer Interaction

The interaction between humanity and AI will evolve beyond current interfaces. Future computers will offer new "tools in the toolbox" for interaction <a class="yt-timestamp" data-t="24:40">[24:40]</a>. Alongside command line, GUI, and voice interfaces, there will be more ambient computing <a class="yt-timestamp" data-t="24:47">[24:47]</a>. The key metric to watch is the "amount of leverage per unit energy a human spends with computing," which is expected to continue increasing <a class="yt-timestamp" data-t="25:10">[25:10]</a>.