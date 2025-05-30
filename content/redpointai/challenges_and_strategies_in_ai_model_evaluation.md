---
title: Challenges and strategies in AI model evaluation
videoId: xLtZ2kyoYic
---

From: [[redpointai]] <br/> 

Evaluating AI models, especially Large Language Models (LLMs), presents unique [[challenges_and_strategies_in_ai_model_development | challenges]] due to their non-deterministic nature and the rapid evolution of the field <a class="yt-timestamp" data-t="00:35:04">[00:35:04]</a>. Harrison Chase, founder and CEO of LangChain, emphasizes that the space is early and fast-moving, making it difficult to predict future developments <a class="yt-timestamp" data-t="00:34:30">[00:34:30]</a>.

## Current State of Evaluation

Teams are grappling with several key questions regarding LLM evaluation <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>:

### Data Set Gathering

The fundamental premise for evaluation is having a dataset against which to test the system <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
Common strategies include:
*   **Hand-labeling:** Initially, teams hand-label about 20 examples <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.
*   **Production data integration:** Incorporating edge cases that fail in production into the test set <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. This connection between production traces and evaluation sets is highly valuable <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   **Forcing function for product thinking:** Creating an evaluation dataset forces teams to consider what the system should actually do, what edge cases it should handle, and how users are expected to interact with it <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. This process is crucial at the start of a product-building journey <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. In traditional ML, this had to be done before building a model, and it's still beneficial for LLMs <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

### Evaluation Methods for Single Data Points

*   **Classification:** For straightforward classification tasks, traditional machine learning techniques can be used <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
*   **LLMs as judges:** For more complex scenarios, using LLMs to judge responses is an emerging popular technique <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. However, this method is not perfect, necessitating a human-in-the-loop component <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
*   **Human review:** Many teams still manually review responses, scoring them and comparing them side-by-side <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. This manual review is where significant value lies, as it helps teams understand how models work and identify unexpected behaviors <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. Observing the thought processes of agents and the inputs/outputs of each step provides deeper system understanding <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.

### Aggregating Metrics

Deciding how to aggregate evaluation metrics is varied <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>:
*   Some teams aim for perfectly scored results <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   Others simply seek to confirm if a new prompt or system is better than the previous one <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.
*   Accuracy percentages are used for specific, critical data points <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### Frequency of Evaluation

Evaluation can be expensive and slow <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>. Teams typically run evaluations before releases due to the significant manual component <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. The goal is to reduce this manual effort sufficiently to enable running evaluations in Continuous Integration (CI) like software unit tests <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.

## The Role of Human-in-the-Loop

The manual aspect of reviewing exceptions in AI models is crucial for understanding how these models behave <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. This manual review is not a "stigma" but a source of immense value, especially in the early, fast-moving stages of AI development <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. It helps developers "grock" these new systems and gain a deeper understanding <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.

## Generalizability and Best Practices

*   **Custom Data Sets:** Teams generally develop their own application-specific datasets <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>.
*   **Shared Metrics:** There is some sharing of metrics, such as using LLMs as judges with common prompts <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>.
*   **Emerging Best Practices:** After an initial period of intense experimentation (the first six months), the subsequent period (next six months) focused on getting applications into production <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>. Now, with impressive production deployments like Elastic's assistant, best practices are starting to emerge <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>. Facilitating discussion and sharing these learnings is an ongoing effort <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.

## Future of Evaluation

*   **Automation vs. Manual Review:** While full automation in the background would be convenient, the manual review of exceptions provides vital insights <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>. It's uncertain how evaluation will work with future models like GPT-7; it might be less critical but still important <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
*   **Abstraction Levels:** Evaluation tools should avoid overly high-level abstractions, focusing on low-level, important aspects like data gathering and understanding system behavior <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>. A code-first approach with API exposure is favored for developers <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
*   **Challenges in LLM Operations (LLMOps):** The LLM problem space differs from traditional applications due to non-determinism, API-based interaction, and prompting <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a>. Existing observability tools like Datadog focus on system-level monitoring and aggregate metrics (e.g., latency), while LLM-specific tools like LangSmith prioritize understanding application behavior and enabling faster iteration with confidence <a class="yt-timestamp" data-t="00:35:44">[00:35:44]</a>.

## Practical Advice for Startups

*   **Build First:** Given the rapid pace of AI, it's essential to build applications even if techniques or underlying models might change <a class="yt-timestamp" data-t="00:30:27">[00:30:27]</a>. Waiting for things to solidify would mean not building at all <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.
*   **Focus on Product-Market Fit (PMF):** Don't prematurely optimize for inference costs or latency; these will decrease over time <a class="yt-timestamp" data-t="00:45:10">[00:45:10]</a>. A common piece of advice is "no GPUs before PMF" or "use GPT-4 until product market fit" <a class="yt-timestamp" data-t="00:45:42">[00:45:42]</a>. The focus should be on building a product that actually works <a class="yt-timestamp" data-t="00:59:03">[00:59:03]</a>.
*   **UX Innovation:** The most interesting work in AI applications currently lies in User Experience (UX) <a class="yt-timestamp" data-t="00:43:27">[00:43:27]</a>. Figuring out how people want to interact with these new capabilities is a major area for innovation <a class="yt-timestamp" data-t="00:43:35">[00:43:35]</a>. For example, an "AI-native spreadsheet" that uses agents for cell population, though not instantaneous, presents a novel UX for handling multiple tasks simultaneously <a class="yt-timestamp" data-t="00:43:53">[00:43:53]</a>.
*   **Personalization and Memory:** A significant opportunity for [[Challenges and advancements in AI model development | AI application development]] is in personalization at the user level, which could lead to a "step change improvement" <a class="yt-timestamp" data-t="00:53:44">[00:53:44]</a>. This includes applications that remember user preferences and history, potentially through Retrieval-Augmented Generation (RAG) or fine-tuning <a class="yt-timestamp" data-t="00:54:22">[00:54:22]</a>. An example is a journal app that remembers personal details and initiates conversations based on past entries <a class="yt-timestamp" data-t="00:55:01">[00:55:01]</a>.
*   **Iterative Development:** The industry is still in the first wave of AI apps, similar to early iPhone development <a class="yt-timestamp" data-t="00:53:35">[00:53:35]</a>. Future "killer apps" are yet to be discovered, possibly emerging several years later as fundamental technologies mature <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>.
*   **Enterprise Adoption:** While consumer-facing AI products gain public attention, a substantial amount of AI work, especially in larger enterprises, is focused on internal tools <a class="yt-timestamp" data-t="00:26:04">[00:26:04]</a>. These internal applications often carry lower risk and allow for more advanced experimentation before external release <a class="yt-timestamp" data-t="01:03:51">[01:03:51]</a>.