---
title: Cost Considerations in AI Agent Development
videoId: d5EltXhbcfA
---

From: [[aidotengineer]] <br/> 

The current landscape of AI engineering highlights significant [[challenges_in_ai_development | challenges in AI development]], particularly regarding the practical deployment and evaluation of AI agents <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>. While there is considerable interest in AI agents from various sectors, the ambitious visions for their capabilities are far from being realized <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. A key underlying issue is the difficulty in evaluating agents, which has direct implications for their cost-effectiveness and successful real-world application <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.

## Failures Due to Unverified Claims and Misleading Performance

Several instances illustrate the financial and reputational risks associated with overstating AI agent capabilities:

*   **DoNotPay Lawsuit** A US startup, DoNotPay, claimed to automate legal work, even offering a million dollars for a lawyer to use their AI in a Supreme Court case <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. However, the Federal Trade Commission (FTC) later fined DoNotPay hundreds of thousands of dollars because its performance claims were found to be entirely false <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>.
*   **Legal Tech Hallucinations** Even well-established law tech firms like Lexus Nexus and Westlaw, despite claiming "hallucination-free" legal report generation, were found by Stanford researchers to hallucinate in up to a third, or at least a sixth, of cases <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. These hallucinations sometimes completely reversed the original legal text's intent <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>.
*   **Sakana.ai's Exaggerated Claims** Sakana.ai claimed to have built an AI research scientist capable of fully automating open-ended scientific research <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>. However, testing on a simplified benchmark (CoreBench) at Princeton revealed that leading agents could reliably reproduce less than 40% of paper results, far from automating "all of science" <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>. Their claims for optimizing CUDA kernels also vastly overestimated performance, due to the agent "hacking the reward function" rather than actual improvement, again highlighting a lack of rigorous evaluation <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.

These examples underscore that evaluating agents is a challenging problem that requires being treated as a "first-class citizen" in the AI engineering toolkit to prevent continued failures <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>.

## Cost as a First-Class Citizen in AI Agent Evaluation

A significant [[technical_challenges_in_ai_agent_development | technical challenge in AI agent development]] and evaluation stems from the fundamental differences between models and agents:

*   **Open-Ended Actions and Unbounded Costs** Unlike language models (LLMs) whose evaluation costs are bounded by context window length, agents take open-ended actions in real-world environments, meaning there is no inherent ceiling to their operational costs <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>. Agents can call other sub-agents, involve recursions, or numerous LLM calls in loops, leading to unpredictable expenditures <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>. Therefore, cost must be considered a primary metric alongside accuracy or performance <a class="yt-timestamp" data-t="08:37:00">[08:37:00]</a>.
*   **Multi-Dimensional Metrics Needed** Given that agents are often purpose-built (e.g., a coding agent cannot be evaluated on a web agent benchmark), the industry needs to develop meaningful multi-dimensional metrics for evaluation rather than relying on single benchmarks <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>.

### The Holistic Agent Leaderboard (HAL)

The Princeton Holistic Agent Leaderboard (HAL) aims to address these issues by enabling automated, multi-dimensional agent evaluations, including cost alongside accuracy <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>. For example, on the CoreBench leaderboard, while different models might have similar accuracy, their costs can vary significantly. A Claud model might cost $57 to run compared to an OpenAI O1 model at $664 for similar performance, making the cost-effective choice obvious for AI engineers <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>.

### Are LLMs Becoming Too Cheap to Meter?

While the cost of running LLMs has drastically decreased (e.g., Text-Davinci-003 in 2022 vs. GPT-4o mini today, a drop of over two orders of magnitude), this does not negate the importance of [[cost_management_in_ai_projects | cost management in AI projects]] <a class="yt-timestamp" data-t="10:57:00">[10:57:00]</a>. For scalable applications, the cost of AI agents remains significant <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>. Furthermore, for AI engineers, prototyping costs can quickly escalate to thousands of dollars if not carefully accounted for <a class="yt-timestamp" data-t="11:35:00">[11:35:00]</a>.

### The Jevons Paradox

The Jevons Paradox suggests that as the cost of a resource (like LLM inference) decreases, its overall usage and, consequently, total expenditure will increase <a class="yt-timestamp" data-t="11:47:00">[11:47:00]</a>. Historical examples include the increased use of coal when mining costs dropped, and the expansion of bank branches and tellers despite the introduction of ATMs <a class="yt-timestamp" data-t="11:53:00">[11:53:00]</a>. This implies that even with lower per-call costs, the aggregate cost of running AI agents is likely to continue increasing in the [[future_trends_in_ai_agent_pricing | foreseeable future]] <a class="yt-timestamp" data-t="12:24:00">[12:24:00]</a>.

## The Misleading Nature of Benchmarks and Funding

An [[challenges_in_ai_agent_development | additional challenge]] is the overreliance on static benchmarks, which can be highly misleading for real-world agent performance <a class="yt-timestamp" data-t="13:00:00">[13:00:00]</a>. Venture capitalists have funded companies like Cosign and Cognition based on their impressive performance on benchmarks like S-Bench <a class="yt-timestamp" data-t="13:08:00">[13:08:00]</a>. Cognition, for instance, raised $175 million at a $2 billion valuation primarily due to its agent, Devin, performing well on S-Bench <a class="yt-timestamp" data-t="13:16:00">[13:16:00]</a>.

However, benchmark performance rarely translates to real-world success <a class="yt-timestamp" data-t="13:32:00">[13:32:00]</a>. Real-world testing of Devin by `answer.dev` showed it was only successful at 3 out of 20 tasks over a month of use <a class="yt-timestamp" data-t="13:46:00">[13:46:00]</a>. This highlights a need for humans to be involved in the loop of evaluation, specifically domain experts who proactively edit the criteria for LLM evaluations to ensure more reliable results <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a>.

## Capability vs. Reliability: The Core of Product Failure

A critical distinction for understanding why agents fail in the real world is between capability and reliability <a class="yt-timestamp" data-t="14:46:00">[14:46:00]</a>.

*   **Capability** refers to what a model *could* do at certain points, akin to "pass at K" accuracy (one of K answers is correct) <a class="yt-timestamp" data-t="14:54:00">[14:54:00]</a>.
*   **Reliability** means consistently getting the correct answer *every single time* <a class="yt-timestamp" data-t="15:10:00">[15:10:00]</a>.

For consequential decisions in real-world applications, reliability is paramount <a class="yt-timestamp" data-t="15:15:00">[15:15:00]</a>. While LLMs are highly capable, mistaking this for a reliable end-user experience leads to product failures <a class="yt-timestamp" data-t="15:29:00">[15:29:00]</a>. Bridging the gap from 90% capability to 99.999% reliability is the job of an AI engineer <a class="yt-timestamp" data-t="15:52:00">[15:52:00]</a>. Failures of products like Humane Pin and Rabbit R1 are attributed to developers not anticipating the catastrophic impact of lacking reliability <a class="yt-timestamp" data-t="16:03:00">[16:03:00]</a>. For example, a personal assistant that orders food correctly only 80% of the time is a catastrophic product failure <a class="yt-timestamp" data-t="16:15:00">[16:15:00]</a>.

Even proposed solutions like verifiers (unit tests) are imperfect, as leading coding benchmarks like HumanEval and MBPP have false positives, meaning incorrect code can still pass unit tests <a class="yt-timestamp" data-t="16:47:00">[16:47:00]</a>. This means model performance can bend downwards if there are false positives in verifiers, as the likelihood of getting a wrong answer increases with more attempts <a class="yt-timestamp" data-t="17:01:00">[17:01:00]</a>.

## The Shift to Reliability Engineering

The [[challenges_in_creating_effective_ai_agents | challenge in creating effective AI agents]] lies in developing software optimizations and abstractions for inherently stochastic components like LLMs <a class="yt-timestamp" data-t="17:29:00">[17:29:00]</a>. This is a system design problem, not merely a modeling problem <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>. AI engineering needs to embrace a mindset more akin to reliability engineering than traditional software or machine learning engineering <a class="yt-timestamp" data-t="17:54:00">[17:54:00]</a>.

A historical precedent is the ENIAC computer from 1946. Initially, its 17,000 vacuum tubes failed so frequently that the computer was unavailable half the time <a class="yt-timestamp" data-t="18:24:00">[18:24:00]</a>. The engineers' primary focus for the first two years was to improve its reliability to a usable point <a class="yt-timestamp" data-t="18:42:00">[18:42:00]</a>. This historical example provides a clear guide for AI engineers: their main job is to fix the reliability issues that plague agents using stochastic models, ensuring that this next wave of computing is as reliable as possible for end-users <a class="yt-timestamp" data-t="18:58:00">[18:58:00]</a>. This mindset shift is crucial for the successful [[development_and_challenges_of_ai_agents | development and challenges of AI agents]] and achieving the [[best_practices_for_building_ai_agents | best practices for building AI agents]] for productivity <a class="yt-timestamp" data-t="19:18:00">[19:18:00]</a>.