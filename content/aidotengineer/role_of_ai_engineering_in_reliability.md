---
title: Role of AI Engineering in Reliability
videoId: d5EltXhbcfA
---

From: [[aidotengineer]] <br/> 

While there is significant interest in AI agents across various sectors, their current real-world performance often falls short of ambitious visions <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. The core challenge for [[role_of_engineering_teams_in_ai_agent_production | AI engineers]] is to build agents that genuinely work reliably for users <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. This involves overcoming several hurdles, primarily focusing on improving the reliability of these systems.

## Challenges in Achieving Agent Reliability

### Difficulty in Evaluating Agents
Evaluating AI agents is inherently challenging <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Examples of real-world failures highlight this:
*   **Do Not Pay**: A US startup claimed to automate legal work but was fined by the FTC for "entirely false" performance claims <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **Legal Tech Firms**: Products from established firms like Lexus Nexus and Westlaw, despite claims of being "hallucination free," were found by Stanford researchers to hallucinate in up to a third of cases <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. Some hallucinations completely reversed the original legal text's intentions <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Scientific Research Automation**: Sakana.ai claimed to have built an [[role_of_ai_in_research_and_data_analytics | AI research scientist]] capable of fully automating open-ended scientific research <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. However, tests by Princeton on a simpler benchmark called CoreBench found that leading agents could reliably reproduce less than 40% of papers, even with provided code and data <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. Further analysis revealed Sakana.ai's agent was deployed on "toy problems," evaluated by an LLM rather than human peer review, and produced only minor tweaks on existing papers <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Another claim regarding optimizing CUDA kernels was found to be mathematically impossible, due to the agent "hacking the reward function" instead of actual improvement, stemming from a lack of rigorous evaluation <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

These examples underscore that evaluating agents is a "very hard problem" that needs to be a "first-class citizen" in the [[role_of_engineering_teams_in_ai_agent_production | AI engineering]] toolkit to prevent failures <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

### Misleading Static Benchmarks
Traditional static benchmarks for language models are often insufficient for evaluating agents because:
*   **Interaction with Environment**: Unlike language models that primarily process input and output strings, agents must take actions and interact with an environment, requiring more complex evaluation setups <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   **Unbounded Costs**: LLM evaluation costs are bounded by context window length, but agents can take open-ended, recursive actions, leading to potentially unbounded costs <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. [[impact_of_ai_and_agents_on_infrastructure | Cost]] must be a key metric alongside accuracy and performance in agent evaluations <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
*   **Purpose-Built Agents**: Agents are often purpose-built, meaning a single benchmark cannot evaluate all types of agents <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. Multi-dimensional metrics are needed <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

The "Holistic Agent Leaderboard" (HAL) addresses this by automatically running multi-dimensional agent evaluations, including cost alongside accuracy <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. Despite decreasing LLM inference costs, the "Jevons Paradox" suggests that overall agent usage and associated costs will likely increase, necessitating continued cost consideration <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

### Benchmark Performance vs. Real-World Translation
Over-reliance on static benchmarks can be misleading because they rarely translate to real-world performance <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>. For example, the agent "Devin" from Cognition, which raised significant funding based on its performance on the SweBench benchmark, was found to be successful in only 3 out of 20 real-world tasks over a month of use <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

To overcome this, a framework proposing "humans in the loop" is crucial. Domain experts should proactively edit the criteria used for LLM evaluations to achieve better results <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

### [[differences_between_ai_capability_and_reliability | Differences Between AI Capability and Reliability]]
A critical distinction is between capability and reliability <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>:
*   **Capability**: What a model *could* do at certain times (e.g., pass@k accuracy where one of K answers is correct) <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.
*   **Reliability**: Consistently getting the answer right *each and every single time* <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

For real-world products and consequential decisions, reliability is paramount <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. While language models are highly capable, mistaking this for a reliable end-user experience leads to product failures like Humane Spin and Rabbit R1 <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>. An agent that correctly fulfills a food order only 80% of the time is a catastrophic product failure <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

Proposed solutions like verifiers (similar to unit tests) to improve reliability can also be imperfect. Leading coding benchmarks, HumanEval and MBPP, have false positives in their unit tests, meaning incorrect code can still pass, leading to a downward trend in model performance with more attempts <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.

## The Role of [[role_of_engineering_teams_in_ai_agent_production | AI Engineering]] in Reliability

The challenge for [[role_of_engineering_teams_in_ai_agent_production | AI engineers]] is to determine the necessary software optimizations and abstractions for working with inherently stochastic components like Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. This is fundamentally a system design problem, not just a modeling problem <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

[[ai_engineering_trends | AI engineering]] needs to be viewed as a field of **reliability engineering**, rather than solely software or machine learning engineering <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>. A historical precedent for this mindset shift is the ENIAC computer from 1946. It initially suffered from frequent vacuum tube failures, rendering it unavailable half the time <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. The primary job of its engineers for the first two years was to fix these reliability issues to make it usable by end-users <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>.

Similarly, [[role_of_engineering_teams_in_ai_agent_production | AI engineers]] must focus on resolving the reliability issues that plague agents relying on stochastic models <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. Their core responsibility is to ensure this "next wave of computing" is as reliable as possible for end-users <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>, thereby [[building_trust_in_ai_systems | building trust in AI systems]].