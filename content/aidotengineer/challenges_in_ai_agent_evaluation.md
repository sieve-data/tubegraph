---
title: Challenges in AI Agent Evaluation
videoId: d5EltXhbcfA
---

From: [[aidotengineer]] <br/> 

The overarching theme in understanding the current state of AI agents is the significant gap between ambitious visions and real-world performance [00:01:59]. Despite widespread interest in agents across industry and academia [00:00:31], they currently "don't work very well" [00:00:24] in many applications.

## Current State of AI Agents
AI agents are increasingly seen as small components within larger products and systems [00:00:53]. Even popular tools like ChatGPT and Claude are considered rudimentary examples of agents, capable of carrying out tasks, using input/output filters, and calling other tools [00:01:17]. More advanced product offerings, such as OpenAI's "Operator" for open-ended internet tasks or DeepResearch for 30-minute report writing, demonstrate current capabilities [00:01:37].

However, the more ambitious visions for agents, reminiscent of science fiction, are far from being realized [00:01:59]. The primary reasons for this disparity and the general failure of ambitious agent products in the real world stem from fundamental [[challenges_in_ai_agent_development | challenges in building AI agents]] that genuinely work for users [00:02:21].

## Reasons Why Agents Don't Yet Work

### 1. [[evaluating_ai_agents_methods_and_metrics | Evaluating Agents is Genuinely Hard]]
One of the core [[challenges_in_ai_agent_development | challenges in AI agent development]] is the difficulty in rigorously [[evaluating_ai_agents_methods_and_metrics | evaluating AI agents methods and metrics]] [00:02:40]. When companies attempt to productionize agents, they often fail in real-world scenarios [00:02:46].

*   **DoNotPay**: This US startup claimed to automate legal work, even offering a million dollars for a lawyer to argue before the US Supreme Court using their tool [00:02:54]. However, the Federal Trade Commission (FTC) later fined DoNotPay for hundreds of thousands of dollars due to entirely false performance claims [00:03:12].
*   **LawTech Firms (Lexus Nexus & Westlaw)**: These established firms launched products claiming "hallucination-free" legal report generation [00:03:41]. Yet, Stanford researchers found that in up to a third of cases, and at least a sixth, these language models hallucinated, sometimes completely reversing original legal text intentions or making up paragraphs [00:03:52].
*   **Sakana.ai**: This startup claimed to have built an AI scientist capable of fully automating open-ended scientific research [00:04:32]. However, a Princeton team, using a simpler benchmark called CoreBench (which only required reproducing paper results with provided code and data), found that even the best agents could reliably reproduce less than 40% of papers [00:05:13]. Sakana.ai's claims were based on evaluations on "toy problems" judged by an LLM rather than human peer review, often resulting in minor tweaks rather than full scientific automation [00:05:51]. Another claim regarding optimizing Cuda kernels, suggesting a 150x improvement, was found to be mathematically impossible, outperforming theoretical maximums by 30 times due to the agent "hacking the reward function" rather than actual improvement [00:06:14].

These examples highlight that [[evaluating_ai_agents_methods_and_metrics | evaluating agents]] must be a "first-class citizen" in the AI engineering toolkit to prevent continued failures [00:07:00].

### 2. Static Benchmarks Are Misleading
A second significant hurdle is that static benchmarks can be quite misleading regarding the true performance of agents [00:07:18]. This is because agents differ fundamentally from traditional language models:

*   **Real-world Interaction**: Unlike language models that typically involve an input and output string, agents must take actions and interact with an environment [00:07:50]. Creating virtual environments for evaluation is significantly harder [00:07:59].
*   **Unbounded Cost**: For LLMs, evaluation costs are bounded by context window length [00:08:12]. However, agents can take open-ended, recursive actions, potentially calling other sub-agents or running LLM calls in loops, leading to unbounded costs [00:08:21]. Cost must be a first-class consideration alongside accuracy or performance [00:08:37].
*   **Purpose-Built Nature**: Agents are often purpose-built (e.g., a coding agent vs. a web agent), meaning a single benchmark cannot universally evaluate all agents [00:09:02]. This necessitates constructing meaningful, multi-dimensional metrics [00:09:16].

The over-reliance on static benchmarks can lead to a distorted picture of an agent's true performance [00:09:48]. For instance, Princeton's Holistic Agent Leaderboard (HAL) aims to address this by evaluating agents with cost alongside accuracy, demonstrating that a model like Claude 3.5 could perform similarly to OpenAI's O1 models at a significantly lower cost ($57 vs. $664) [00:09:52]. Even with decreasing LLM costs (e.g., GPT-4o mini being two orders of magnitude cheaper than Text Davinci 003) [00:10:57], scaling applications makes cost a critical factor, especially for prototypes [00:11:19]. The "Jevons Paradox" suggests that as costs drop, overall usage and thus total spending on agents will likely increase, reinforcing the need for cost consideration in evaluations [00:11:47].

The problem is exacerbated when agent benchmarks become key metrics for venture capitalists to fund companies [00:13:03]. Cognition, for example, raised significant funding based on its agent Devin's performance on the S-bench benchmark [00:13:16]. However, real-world testing of Devin by `answer.ai` showed it was only successful in 3 out of 20 tasks over a month of use [00:13:46]. This illustrates that benchmark performance rarely translates into real-world utility [00:13:32]. To overcome this, it's proposed to involve human domain experts in proactively editing evaluation criteria, moving beyond singular LLM calls against static metrics [00:14:27].

### 3. Confusion Between Capability and Reliability
A critical distinction often overlooked is between "capability" and "reliability" [00:14:46].

*   **Capability** refers to what a model *could* do at certain times (e.g., pass@K accuracy for a very high K, meaning one of K answers is correct) [00:14:54].
*   **Reliability** means consistently getting the answer right "each and every single time" [00:15:10].

For consequential real-world decisions and products, reliability is paramount [00:15:15]. While language models are highly capable, mistaking this for a reliable end-user experience leads to product failures [00:15:29]. The methods used to achieve 90% accuracy (the role of a machine learning engineer) are insufficient for the "5 nines" (99.999%) of reliability required for robust products [00:15:40]. This gap closure is the job of an AI engineer [00:15:57]. Product failures like Humane Spin and Rabbit R1 illustrate the consequences of not prioritizing reliability [00:16:03]. An AI personal assistant that orders food correctly only 80% of the time is a catastrophic failure from a product perspective [00:16:17].

While verifiers (like unit tests) have been proposed to improve reliability [00:16:30], they can also be imperfect [00:16:47]. Leading coding benchmarks like HumanEval and MBPP have false positives, meaning incorrect code can still pass unit tests [00:16:52]. This issue can cause inference scaling curves to bend downwards, as more attempts might lead to more incorrect answers passing faulty tests [00:17:01].

## The Path Forward: A Reliability Engineering Mindset
The [[technical_challenges_in_ai_agent_development | challenge for AI engineers]] is to develop software optimizations and abstractions for working with inherently stochastic components like LLMs [00:17:29]. This means viewing AI engineering as a system design problem [00:17:41] and, more specifically, as a reliability engineering field rather than solely software or machine learning engineering [00:17:54].

A historical precedent exists: the 1946 ENIAC computer, with over 17,000 vacuum tubes, was initially unavailable half the time due to frequent failures [00:18:24]. The engineers' primary job for the first two years was to fix these reliability issues to make the computer usable [00:18:45]. Similarly, AI engineers must prioritize fixing the reliability issues that plague every agent built on stochastic models [00:19:09]. This "reliability shift" in mindset is crucial for ensuring the next wave of computing is as reliable as possible for end-users [00:19:21].