---
title: Challenges in synthesizing vast financial data
videoId: MWTJIAwAAnk
---

From: [[aidotengineer]] <br/> 

Brightwave, a company specializing in research agents for the financial domain, focuses on solving the challenge of synthesizing vast amounts of content to aid financial professionals <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This includes tasks such as due diligence, competitive deal processes, mutual fund analysis during earnings season, and reviewing hundreds of vendor contracts <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. These tasks are described as "non-trivial" and frankly, "not a human level intelligence task" <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>, often placing junior analysts in a "meat grinder" with impossible deadlines <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## The Need for AI in Financial Data Synthesis

The role of an individual in finance workflows and financial research today is compared to an accountant in 1978 before computational spreadsheets <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. Previously, "running the numbers" was a cognitively demanding, time-intensive task done by hand <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. With the advent of spreadsheets, the sophistication of thought applied to financial problems increased substantially <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

Similarly, systems like Brightwave, or any class of knowledge agents, can digest volumes of content and perform meaningful work that accelerates efficiency and time to value by orders of magnitude <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. These [[AI tools in financial research and due diligence | AI tools]] are designed to handle tasks that are beyond human capacity <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Core [[Challenges in building AI applications | Challenges in Building AI Applications]] for Data Synthesis

Building effective AI systems for synthesizing vast financial data presents several complex [[Challenges and solutions in AI driven data processing | challenges and solutions in AI driven data processing]].

### Technical and Model Limitations

*   **Error Propagation**: Non-reasoning models often perform "greedy local search," meaning a small error rate (e.g., 5-10%) in a single call can introduce exponential likelihood of error when calls are chained together <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   **Global Optimality**: Achieving "end to end RL over tool use calls" where API call results influence subsequent decisions for globally optimal outputs is "still an open research problem" <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. This includes intelligently availing oneself of knowledge graphs <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   **Output Length Constraints**: Despite claims of large context output lengths, current models typically produce shorter coherent outputs (e.g., A1 is around 2,000-3,000 tokens, better than 40) <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. It is difficult for models to produce tens of thousands of coherent novel words <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.
*   **Compression Problem**: A large input context window compresses information into a smaller set of output tokens. To get high-fidelity, information-dense outputs, research instructions must be decomposed into multiple sub-themes <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.
*   **Lack of Combinative Reasoning**: The training corpuses for instruction tuning and post-training have a low presence of combinative reasoning demonstrations <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. It's easy to ask a model to write an epilogue based on a single book, but it's much harder to get high-quality, thoughtful analysis by weaving together disparate fact patterns from many documents, like in biomedical literature synthesis <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.
*   **Real-World Complexity**: Even state-of-the-art models struggle with complex real-world situations, including factors like temporality (e.g., understanding changes from mergers and acquisitions or contract addendums) <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.

### Product Design and User Experience Challenges

*   **Revealing Thought Process**: A significant design problem is how to reveal the thought process of a system that has considered 10,000 pages of content in a useful and legible way to a human <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Current chat interfaces are likely "not enough" <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **User Prompting Expertise**: People generally do not want to become deep prompting experts, which can take "easily a thousand hours" to master <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. Products need to provide scaffolding to orchestrate workflows and shape system behavior, with "verticalized product workflows" enduring because they specify intent and offload complexity from the user <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **The Latency Trap**: If the feedback loop for a user's prompt is too long (e.g., 8-20 minutes), they won't perform many interactions in a day, which hinders their ability to develop faculty with the system and refine their mental model of its behavior <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
*   **Anthropomorphizing Systems**: Avoid "needless anthropomorphizing" of AI systems (e.g., "portfolio manager agent," "fact checker") as it constrains flexibility if compute graph design needs change <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. Instead, focus on simple tools that do one thing well and work together, akin to the Unix philosophy <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   **Maintaining Human Oversight**: Human oversight is "extremely important," allowing users to nudge the model with directives or select interesting threads to explore <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. The human analyst will always have access to non-digitized information, like conversations with management or insights from portfolio managers, which is where "taste making" comes into play <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

### Designing Autonomous Agents

Autonomous agents should mimic human decision-making processes, decomposing tasks such as:
*   Identifying relevant public market comparables (e.g., SEC filings, earnings call transcripts) <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   Assessing relevant document sets and distilling findings <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   Enriching and error-correcting those findings <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

A useful design pattern involves asking the model to think aloud, generating intermediary notes about what it believes based on initial findings <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. Additionally, models can self-correct by being asked to verify accuracy or factual entailment in a secondary call, as they might be "primed to be credulous" in a single call <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

Ultimately, synthesis involves weaving together fact patterns across many documents into a coherent narrative <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

## Brightwave's Solutions

Brightwave is building a product that aims to reveal the AI's thought process when considering vast amounts of text <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>. Key features include:

*   **Interactive Reports**: The ability to click on citations to get additional context, including the document source and the model's reasoning <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   **Structured Interactive Outputs**: Users can "pull the thread" and ask for more details on any finding, such as "tell me more about that Rising capex spend" <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.
*   **Details on Demand**: Users can highlight any passage of text and ask for implications, effectively using it as a "magnifying glass for text" <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.
*   **Audit Trail**: The system provides an "audit trail" for findings, laying out all discovered information (e.g., fundraising timeline, ongoing litigation) and allowing users to click in for more details on specific points of interest <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>.

The final form factor for this class of products is still evolving, representing an "extremely interesting design problem" <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.