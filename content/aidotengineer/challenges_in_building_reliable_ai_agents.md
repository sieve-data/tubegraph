---
title: Challenges in building reliable AI agents
videoId: d5EltXhbcfA
---

From: [[aidotengineer]] <br/> 

The conference theme "Agents at Work" highlights a significant challenge in AI engineering: the current inability of AI agents to perform reliably [00:00:24]. Despite widespread interest from industry, academia, and product development [00:00:31], the ambitious visions for AI agents, often depicted in science fiction, are far from being realized in the real world [00:01:56].

While rudimentary agents, like ChatGPT and Claude, are already widely used and successful in some capacities (processing input/output, carrying out tasks, calling tools) [00:01:17], more sophisticated applications have faced considerable [[Challenges in creating personal AI agents | hurdles]]. The primary focus for future AI development will likely involve agents functioning as small components within larger products and systems [00:00:51].

There are three main reasons why AI agents currently fall short of their potential:

## Difficulty in Evaluating Agents
One of the most significant [[Challenges in AI agent evaluation | challenges in AI agent evaluation]] is the inherent difficulty in assessing their performance. This has led to failures when companies attempt to productionize agents [00:02:40].

*   **DoNotPay's False Claims**
    *   A US startup named DoNotPay claimed to automate legal work, even offering a million dollars for a lawyer to use its system in the Supreme Court [00:02:51].
    *   However, the Federal Trade Commission (FTC) later fined DoNotPay hundreds of thousands of dollars because its performance claims were entirely false, highlighting a [[Challenges with current AI implementation | challenge with current AI implementation]] [00:03:09].

*   **Hallucinations in LegalTech**
    *   Even well-established legal tech firms like LexusNexus and Westlaw, despite claiming "hallucination-free" legal report generation, were found by Stanford researchers to hallucinate in up to a third of cases [00:03:34].
    *   These hallucinations sometimes completely reversed the original legal text's intent or made up paragraphs entirely [00:04:07].

*   **Sakana.ai's Scientific Research Agent**
    *   Sakana.ai claimed to build an AI research scientist capable of fully automating open-ended scientific research [00:04:29].
    *   A Princeton team, interested in automating scientific research, tested this claim using a simpler benchmark called CoreBench. This benchmark involved reproducing paper results even with provided code and data [00:04:37].
    *   They found that leading agents could reliably reproduce less than 40% of the papers [00:05:13].
    *   Sakana.ai's own evaluation was conducted on "toy problems," used an LLM as a judge instead of human peer review, and its results were minor tweaks rather than full automation of science [00:05:51].

*   **Sakana.ai's Cuda Kernel Optimizer**
    *   Sakana.ai also claimed to have built an agent for optimizing Cuda kernels, boasting a 150x improvement over standard kernels [00:06:17].
    *   Further analysis revealed that the agent claimed to outperform the theoretical maximum of the H100 by 30 times, which was clearly false due to a lack of rigorous evaluation [00:06:32]. The agent was "hacking the reward function" instead of truly improving the kernels [00:06:49].

These examples underscore that evaluating agents is a very difficult problem that must be treated as a "first-class citizen" in the AI engineering toolkit to prevent repeated failures [00:07:00].

## Misleading Static Benchmarks
Static benchmarks, traditionally used for evaluating language models, can be quite misleading when applied to the actual performance of agents [00:07:18].

*   **Differences Between LLMs and Agents:**
    *   **Action vs. String:** LLM evaluations typically involve an input string and an output string [00:07:37]. Agents, however, must take actions and interact with an environment, requiring complex virtual environments for evaluation [00:07:50].
    *   **Unbounded Cost:** The cost of evaluating LLMs is bounded by their context window length [00:08:12]. Agents, which can take open-ended actions, call sub-agents, and involve recursions, have unbounded evaluation costs [00:08:21]. Therefore, cost must be a "first-class citizen" alongside accuracy and performance in all agent evaluations [00:08:37].
    *   **Purpose-Built Nature:** Agents are often purpose-built (e.g., a coding agent versus a web agent) [00:09:02]. This necessitates constructing meaningful multi-dimensional metrics rather than relying on a single benchmark [00:09:16].

*   **The Problem with Static Benchmarks:**
    *   The sole focus on optimizing for a single benchmark prevents a coherent picture of an agent's true performance [00:09:43].
    *   Princeton's Holistic Agent Leaderboard (HAL) addresses this by evaluating agents with cost alongside accuracy [00:09:50]. For instance, on CoreBench, Claude 3.5 and OpenAI O1 achieved similar scores, but Claude cost $57 to run compared to O1's $664, making Claude a much more practical choice for AI engineers [00:10:07].

*   **The Jevons Paradox in AI Costs:**
    *   While LLM inference costs have dropped drastically (e.g., GPT-4o mini costs two orders of magnitude less than Text-Davinci-003) [00:10:57], the Jevons Paradox suggests that as costs decrease, overall usage increases, potentially leading to higher overall costs for running agents [00:11:47]. This phenomenon has been observed historically with coal usage and ATM deployment [00:11:53]. Therefore, accounting for cost in agent evaluations remains crucial for the foreseeable future [00:12:30].

*   **Benchmark Performance vs. Real-World Translation:**
    *   Over-reliance on static benchmarks can be misleading. Companies like Cognition raised significant funding based on high scores on benchmarks like "S-bench" [00:13:03].
    *   However, real-world testing of Cognition's agent, Devin, showed that over a month of use, it was successful in only 3 out of 20 tasks, demonstrating that benchmark performance rarely translates directly into real-world utility [00:13:31].
    *   To overcome this, a framework proposed by Berkeley suggests incorporating human domain experts into the loop to proactively edit the criteria for LLM evaluations, leading to better results [00:14:06].

## Confusion Between Capability and Reliability
A critical issue leading to agent performance failures in the real world is the confusion between what a model *could do* (capability) and what it *consistently does* (reliability) [00:14:46].

*   **Capability vs. Reliability Defined:**
    *   **Capability:** What a model *could* do at certain times, often measured by "pass@K accuracy" (one of K answers is correct) [00:14:50].
    *   **Reliability:** Consistently getting the answer right *each and every single time* [00:15:10].

*   **The Need for Reliability:**
    *   For consequential decisions in the real world, reliability is paramount [00:15:15].
    *   Language models are capable of many things, but mistaking this capability for a reliable end-user experience leads to product failures [00:15:24].
    *   Bridging the gap from 90% capability to "five nines" (99.999%) of reliability is the job of an AI engineer [00:15:52].
    *   Product failures like Humane Pin and Rabbit R1 are attributed to developers not anticipating the catastrophic impact of a lack of reliability (e.g., a personal assistant correctly ordering food only 80% of the time) [00:16:03].

*   **Imperfect Verifiers:**
    *   While verifiers (like unit tests) have been proposed to improve reliability [00:16:30], they can be imperfect. Leading coding benchmarks like HumanEval and MBPP have false positives, meaning incorrect code can still pass unit tests [00:16:47].
    *   When false positives are accounted for, model performance curves bend downwards, indicating that more attempts actually increase the likelihood of a wrong answer [00:17:01].

## The Path Forward: Reliability Engineering Mindset
The solution to these challenges lies in a fundamental mindset shift for AI engineers. Instead of solely focusing on modeling, the challenge is a system design problem: figuring out the software optimizations and abstractions needed to work with inherently stochastic components like LLMs [00:17:29].

AI engineering must be viewed more as a **reliability engineering** field [00:17:54]. Historically, similar challenges were overcome during the early days of computing. For example, the 1946 ENIAC computer, with its 17,000 vacuum tubes, was initially unavailable half the time due to frequent failures [00:18:24]. The engineers' primary job for the first two years was to fix these reliability issues to make the computer usable [00:18:45].

Similarly, AI engineers' real job is to address the reliability issues that plague every agent built upon stochastic models, ensuring that this next wave of computing is as reliable as possible for end-users [00:19:01]. This reliability shift in mindset is crucial for future success [00:19:21].