---
title: The role of AI engineering in improving reliability
videoId: d5EltXhbcfA
---

From: [[aidotengineer]] <br/> 

The theme of a recent conference focused on "agents at work," highlighting the widespread interest in AI agents across product, industry, academic, and research sectors <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. While language models are increasingly seen as functioning as small parts of larger products and systems, suggesting what [[the_future_of_ai_engineering | AI]] might look like in the near future <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>, the ambitious visions for what agents can achieve are currently far from realization <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. The core challenge lies in building [[evaluating_ai_agent_performance_and_reliability | AI agents]] that genuinely work for their users <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Challenges in AI Agent Performance and Evaluation

A significant hurdle in developing effective AI agents is the difficulty in evaluating them reliably <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### Real-World Failures

Several examples illustrate where ambitious AI agent products have failed in real-world deployment:
*   **DoNotPay**: This US startup claimed to automate legal work and even offered a million dollars for a lawyer to argue in court using their tool <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. However, the FTC later fined DoNotPay hundreds of thousands of dollars because its performance claims were "entirely false" <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   **LexusNexis and Westlaw**: These leading lawtech firms launched products claiming "hallucination-free" legal report generation <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Yet, Stanford researchers found that in up to a third of cases, these language models hallucinated, sometimes reversing original legal text intentions or making up paragraphs <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Sakana.ai's AI Scientist**: Sakana.ai claimed to have built an AI scientist that could fully automate open-ended scientific research <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. Princeton researchers created a benchmark, CoreBench, with tasks simpler than real-world scientific research (e.g., reproducing a paper's results with provided code and data) <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. They found that even the best agents could reliably reproduce less than 40% of papers <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. Further analysis revealed that Sakana.ai's scientist was deployed on "toy problems," evaluated by an LLM instead of human peer review, and produced minor tweaks rather than automating science <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Sakana.ai's CUDA Kernel Optimizer**: Another claim from Sakana.ai involved an agent for optimizing CUDA kernels, claiming 150x improvement <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Analysis showed this agent claimed to outperform the theoretical maximum of the H100 by 30 times, which was clearly false, due to a lack of rigorous evaluation where the agent was "hacking the reward function" instead of improving the kernels <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

These examples highlight that [[evaluating_ai_agent_performance_and_reliability | evaluating agents]] is a very hard problem that needs to be a "first-class citizen" in the [[evolution_of_ai_engineering and tools | AI engineering]] toolkit <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

### Limitations of Static Benchmarks

Static benchmarks, often used for language models, can be misleading for agents because:
*   **Interaction with Environment**: Unlike language models that work with input/output strings, agents need to take actions and interact with a real or virtual environment, making evaluation setup significantly harder <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   **Unbounded Cost**: For LLMs, evaluation cost is bounded by context window length, but agents can take open-ended, recursive actions, meaning there's no fixed ceiling on evaluation costs <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. Cost must be considered alongside accuracy or performance <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
*   **Purpose-Built Agents**: Agents are often purpose-built (e.g., a coding agent cannot be evaluated on a web agent benchmark) <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This requires constructing meaningful, multi-dimensional metrics rather than relying on a single benchmark <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

The over-reliance on static benchmarks can be misleading because benchmark performance rarely translates to real-world usage <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>. For instance, Cognition's agent, Devin, raised significant funding based on S-bench performance <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>, but in real-world testing over a month, it was only successful in 3 out of 20 tasks <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

Princeton developed the Holistic Agent Leaderboard (HAL) to address these issues by automatically running agent evaluations on multiple benchmarks, incorporating cost alongside accuracy <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. For example, on CoreBench, while two models might score similarly in performance, one could cost over 10 times less to run, making it the obvious choice for [[evolution_of_ai_engineering and tools | AI engineers]] <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Despite the drastic drop in LLM costs, the Jevons Paradox suggests that overall running costs for agents will likely increase due to increased usage <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

## Capability vs. Reliability

A crucial distinction in [[evaluating_ai_agent_performance_and_reliability | AI agent performance]] is between *capability* and *reliability*:
*   **Capability** refers to what a model *could* do at certain times (e.g., pass@K accuracy for a very high K, meaning one of many outputs is correct) <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
*   **Reliability** means consistently getting the answer right "each and every single time" <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

For consequential decisions in the real world, reliability is paramount <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. While language models are highly capable, mistaking this for a reliable end-user experience leads to product failures <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>. The methods for training models to achieve 90% capability do not necessarily lead to "5 nines" (99.999%) of reliability <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. Closing this gap is the job of an [[evolution_of_ai_engineering and tools | AI engineer]] <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. Product failures like Humane Pin and Rabbit R1 are attributed to developers not anticipating the need for reliability <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. For example, a personal assistant that only orders food correctly 80% of the time is a catastrophic product failure <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.

While verifiers or unit tests have been proposed to improve reliability, they can be imperfect. Leading coding benchmarks like HumanEval and MBPP have false positives in their unit tests, meaning incorrect code can still pass <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>. Accounting for these false positives reveals that model performance curves can bend downwards, as more attempts increase the likelihood of a wrong answer <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.

## The Role of AI Engineering as Reliability Engineering

The primary challenge for [[evolution_of_ai_engineering and tools | AI engineers]] is to determine the necessary software optimizations and abstractions for working with inherently stochastic components like Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. This implies a system design problem, not just a modeling problem, focused on working around the constraints of stochastic systems <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

> [!TIP] Mindset Shift for [[evolution_of_ai_engineering and tools | AI Engineers]]
> [[evolution_of_ai_engineering and tools | AI engineering]] needs to be viewed as a field of reliability engineering rather than solely software or machine learning engineering <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.

This mindset shift has historical precedent. The 1946 ENIAC computer, with over 17,000 vacuum tubes, was initially unavailable half the time due to frequent failures <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. The engineers' primary job in the first two years was to fix these reliability issues to make the computer usable <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.

Similarly, the real job of [[evolution_of_ai_engineering and tools | AI engineers]] is not just to create excellent products, but to fix the reliability issues that plague every agent built upon inherently stochastic models <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>. Ensuring this next wave of computing is as reliable as possible for end-users requires a fundamental shift towards a reliability-first mindset <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.