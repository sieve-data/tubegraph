---
title: AI evaluation and benchmarking
videoId: NoVMk_P6fgY
---

From: [[redpointai]] <br/> 

Arvin Duran, a computer science professor at Princeton, focuses on distinguishing between hype and substance in AI through his newsletter and book, "AI Snake Oil" <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. He discusses the state of agents, where [[ai_model_evaluation_and_benchmarking | evaluations]] succeed or fail, challenges in coordinating them, and the implications of AI for policymakers <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Challenges in AI Evaluation

### Domains of Success and Struggle
Impressive results from reasoning models are primarily observed in domains with "clear correct answers," such as math, coding, and certain scientific tasks <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. A key open question is how far this impressive performance can generalize beyond these narrow domains <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

Historically, reinforcement learning, despite generating excitement 10 years ago for its performance in games like Atari, failed to generalize significantly outside these narrow domains <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. A similar future is possible for current reasoning models <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. However, another possibility is that improved reasoning capabilities, such as code writing, could extend to systems that reason about obtaining information from the internet for legal or medical fields <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Limitations of Benchmarks
Focusing solely on benchmark results might be misleading <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. "Construct validity" highlights that what a benchmark measures might subtly differ from what is desired in the real world <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. For example, SweepBench, a benchmark developed by Princeton colleagues, uses real GitHub issues rather than "Olympiad-style coding problems" <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. However, GitHub issues are still "a far cry from the messy context of real-world software engineering" <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

Dramatic improvements in benchmarks like SweepBench do not necessarily translate to dramatic improvements in human productivity <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. Passing bar or medical exams, for instance, does not equate to the full range of skills required to be a lawyer or doctor <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

> [!NOTE] Real-World vs. Benchmark Success
> Domain-specific, real-world [[evaluation_methodologies_and_user_feedback_for_ai_models | evaluations]] are needed, alongside user feedback <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. "Uplift studies," which are randomized control trials where one group uses a tool and another doesn't, can measure productivity impacts <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. LLMs might perform well on diagnosis tasks but struggle with natural patient interaction or eliciting information, which is crucial for effective medical practice <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

### Inference Scaling Flaws
Arvin Duran's paper, "Inference Scaling Flaws," investigates how reasoning models might "go off the rails" <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. The paper specifically examines a method of scaling where a generative model is paired with a verifier (e.g., unit tests for coding, automated theorem checkers for math) <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. The hope is that traditional, non-stochastic verifiers could be perfect, allowing the model to generate millions of solutions until one passes <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

However, in reality, verifiers can be imperfect (e.g., unit tests may have imperfect coverage) <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. The research shows that if the verifier is imperfect, inference scaling cannot go very far, sometimes saturating within as few as 10 model invocations instead of millions <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. This implies significant challenges for scaling models in domains without easy or perfect verifiers, such as law or medicine <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

## Evaluating Agentic AI
"Agentic AI" isn't a single category <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. One type is a tool that generates a report or first draft for an expert user, which can be a time-saving tool despite potential flaws <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. Another type autonomously takes actions on behalf of the user, such as booking flights <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

### Current State and Limitations
Booking flight tickets is considered a "worst-case example for an AI product" due to the difficulty in understanding user preferences, which often requires many rounds of iteration <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. An agent might also struggle with these preferences and end up asking numerous questions, leading to similar frustration as current online systems <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

A major concern for autonomous agents is the high cost of errors <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. Even a 1% error rate for tasks like booking flights is intolerable <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Early agentic systems have shown such failures, like ordering food to the wrong address, leading to complete loss of user trust <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

> [!CAUTION] Distinguishing Applications
> A key difference lies between producing generative outputs for human review (low error cost) and automating actions on behalf of the user (high error cost) <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. There needs to be more focus on the human-computer interaction component for generative AI systems <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

Current [[ai_model_evaluation_and_benchmarking | evaluations]] for agents are similar to chatbots, using "static benchmarks" with relatively realistic tasks like fixing software engineering issues or navigating web environments <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. However, these are "not working that well" <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.

One limitation is the "capability reliability gap" <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>. A 90% score on a benchmark doesn't clarify if the agent reliably performs 90% of tasks correctly or fails 10% of the time at any task, potentially taking costly actions <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>. Current benchmarks provide little information on whether an agent can be trusted for real-world use <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.

### Safety Considerations
Safety should be a component of every benchmark, not just specialized ones <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>. Some web benchmarks involve agents performing "stateful actions on real websites," which could lead to spam or unintended consequences once agents become more capable <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>.

Simulated environments for web benchmarks lose much of the nuance of real websites <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>. Agent frameworks like AutoGPT can sometimes take unintended actions online, such as posting questions on Stack Overflow, which demonstrates a lack of basic safety control <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>. Currently, the only way to prevent such actions is for the agent to escalate every action to a human user for babysitting <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>.

### Human-in-the-Loop Approaches
Duran's team is [[ai_model_evaluation_and_benchmarking | building and improving benchmarks]] by creating an "AI agent Zoo" where different agents work collaboratively on tasks <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>. This differs from competitive benchmarks where agents work in isolation <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. For example, agents were tasked with writing jokes, and even for simple tasks, they generated millions of tokens, often making progress by understanding their environment, tools, and collaborators <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>. They were integrated into Slack and given blogging tools to summarize learning <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

> [!TIP] The Role of Humans
> Benchmarks should be seen as a "necessary but not sufficient condition" for evaluation <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>. Agents that perform well on benchmarks should then be used with "human in the loop" in semi-realistic environments <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>. The challenge is to keep humans in the loop without requiring them to babysit every single step <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>.

The "Jagged Frontier" idea suggests that models will be calculator-like in some areas (better than humans) but lack common sense in others, necessitating human-AI hybridization <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>. It's unclear whether to integrate agents into existing human collaboration tools (e.g., Slack, email) or to build new ones <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>. Visualizing and interpreting the potentially million-token logs of agent actions for high-level insight is an area of active work, with frameworks like "Human Layer" emerging <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.

## Future of AI Evaluation

### Rethinking Benchmarks
The "pass@k" metric, which measures the percentage of tasks an agent can accomplish multiple times in a row, is a more interesting and useful metric for reliability <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>.

### Academic Contributions
Academia has a crucial role in [[ai_model_evaluation_and_benchmarking | AI model evaluation and benchmarking]], especially for aspects beyond "pure technical innovation" <a class="yt-timestamp" data-t="00:34:52">[00:34:52]</a>. This includes understanding applications, societal impacts, and ensuring positive outcomes <a class="yt-timestamp" data-t="00:35:01">[00:35:01]</a>. Academia can also serve as a "counterweight to industry interests," similar to the relationship between medical researchers and the pharmaceutical industry <a class="yt-timestamp" data-t="00:35:14">[00:35:14]</a>.

> [!INFO] AI in Science
> [[AI model evaluation and benchmarking | AI for science]] is a "very hot area," but early claims of revolutionary discoveries are often "overblown" and have flaws in their reproduction <a class="yt-timestamp" data-t="00:36:16">[00:36:16]</a>. Nonetheless, AI is already significantly impacting scientists, serving as a "thinking partner" for critiquing ideas and enhancing literature searches through semantic search <a class="yt-timestamp" data-t="00:36:44">[00:36:44]</a>.

### Generalization and Economic Impact
[[ai_model_evaluation_and_benchmarking | Evaluating AI progress with ROI]] (Return on Investment) should consider both the rapid decrease in per-token inference costs and the increase in "inference time compute" <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. It's predicted that token usage will likely continue to increase, more than compensating for cost decreases, leading to higher overall inference costs <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.

Duran's paper with Z Kapor, "AI as Normal Technology," argues that AI will not necessarily change everything in the next two years <a class="yt-timestamp" data-t="00:55:54">[00:55:54]</a>. Its impact, like the internet, will unfold over decades <a class="yt-timestamp" data-t="00:56:05">[00:56:05]</a>. While the internet transformed how almost every cognitive task is performed, its impact on GDP has been minimal because new bottlenecks emerge when old ones are eliminated <a class="yt-timestamp" data-t="00:46:51">[00:46:51]</a>. Similarly, AI may transform workflows without leading to massive GDP increases in the short term <a class="yt-timestamp" data-t="00:47:34">[00:47:34]</a>.

Instead of focusing on "AGI," Duran prefers to think about "transformative economic impacts like GDP" <a class="yt-timestamp" data-t="00:52:12">[00:52:12]</a>. His view is that such impacts are "decades out," not years <a class="yt-timestamp" data-t="00:52:19">[00:52:19]</a>.

> [!WARNING] The Future of Information Access
> A "weird prediction" is that younger users will be trained to expect chatbots as the primary way of accessing information, mediated by a "fundamentally statistical tool that could hallucinate" <a class="yt-timestamp" data-t="00:52:37">[00:52:37]</a>. This shift demands preparing people with tools for fact-checking when necessary <a class="yt-timestamp" data-t="00:53:02">[00:53:02]</a>. The idea of searching websites for authoritative sources might become as anachronistic as going to a library <a class="yt-timestamp" data-t="00:53:18">[00:53:18]</a>.