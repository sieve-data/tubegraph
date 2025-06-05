---
title: Role of machine learning and language models in finance
videoId: MWTJIAwAAnk
---

From: [[aidotengineer]] <br/> 

## Introduction to Brightwave's Research Agent
Brightwave, founded by Mike Cohn, specializes in building research agents designed to digest vast amounts of content within the financial domain <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This technology is particularly useful for tasks like due diligence in competitive deal processes, where professionals need to quickly achieve conviction when facing thousands of pages of content <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. The goal is to rapidly identify critical risk factors that could diminish asset performance <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### Current Challenges in Financial Research
Traditional financial research involves highly demanding and time-intensive tasks for professionals, such as mutual fund analysts reviewing earnings calls, transcripts, and filings for 80-120 companies during earning season <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Identifying early termination clauses in hundreds of vendor contracts during confirmatory diligence is another example of a non-trivial problem <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. These tasks are often described as "not a human-level intelligence task" and can put junior analysts in a "meat grinder" due to impossible deadlines <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Transformation of Financial Workflows
The advent of computational tools, similar to how spreadsheets revolutionized accounting in 1978, is increasing the sophistication of thought applied to financial problems <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. [[knowledge_agents_in_finance_workflows | Knowledge agents]], such as Brightwave's system, can digest large volumes of content and perform meaningful work, accelerating efficiency and time-to-value by orders of magnitude in financial markets <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### Technical Insights and Design Considerations
[[integration_of_large_language_models_in_development | Integrating large language models]] into financial tools requires careful design. A key challenge is revealing the thought process of a system that has considered 10,000 pages of content in a useful and legible way <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. The final form factor for such products is still evolving, with chat interfaces likely being insufficient <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

#### Limitations of Non-Reasoning Models
Non-reasoning models typically perform greedy local search, which can lead to high error rates when chained in successive calls <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. For example, if an LLM has a 5-10% error rate extracting organizations from a Reuters article, chaining such calls exponentially increases the likelihood of error <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

#### The Need for End-to-End RL Over Tool Use
Winning systems will perform end-to-end Reinforcement Learning (RL) over tool use calls, where the results of API calls influence subsequent decisions <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. This allows models to make locally suboptimal decisions to achieve globally optimal outputs <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. However, intelligently availing oneself of tools in this manner remains an open research problem <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

#### Building Practical Products Today
Despite ongoing research, practical product development today focuses on constraining the scope of an agent's behaviors <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. This "regularization parameter" limits the likelihood of the model producing degenerate output <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. Effective use of [[using_language_models_to_generate_text | language models to generate text]] requires skill in "steering" the model through multi-turn conversations, guiding its activations towards solving the problem <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. Since most professionals won't become prompting experts, products must provide scaffolding to orchestrate workflows and shape system behavior <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. Verticalized product workflows are likely to endure because they specify intent and reduce the burden on the user <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

#### Mimicking Human Decision-Making
An autonomous agent should mimic the human decision-making process by decomposing tasks. This involves:
*   Looking for public market comparables <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   Assessing relevant document sets (SEC filings, earnings call transcripts, [[knowledge_agents_in_finance_workflows | Knowledge Graphs]] from past deals, news) <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   Distilling findings that substantiate hypotheses <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
*   Enriching and error-correcting those findings <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
*   Asking models to self-correct by verifying factual entailment or organization classification <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. It's often more powerful to perform this as a secondary call rather than within a single Chain of Thought <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

#### Synthesis Across Documents
Synthesis involves weaving together disparate fact patterns from numerous documents into a coherent narrative <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. This is analogous to biomedical literature synthesis, where one needs to read many papers and provide useful insights that integrate facts across them <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. However, generating high-quality, intelligent analysis from many documents faces practical limitations in even state-of-the-art models <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>. Complex real-world factors like temporality (e.g., changes due to mergers or contract addendums) are difficult for models to manage <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.

#### Human Oversight and Model Nudging
Human oversight is crucial. The ability to "nudge" the model with directives or by selecting interesting threads for it to explore is vital <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. Analysts possess information not yet digitized, such as conversations with management or portfolio manager insights, which can guide the model <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. Over-anthropomorphizing systems by assigning them roles like "portfolio manager agent" can constrain flexibility <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

#### The Latency Trap
The "latency trap" highlights that long feedback loops hinder user learning and product adoption <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. If a user's prompt results in an 8-minute or 20-minute wait for feedback, their faculty with the system will remain low <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.

## Product Design for Interpretability and Interaction
Effective products aim to reveal the model's "thought process" on vast datasets. This can be achieved through:
*   **Continuous Surface**: Providing a dynamic interface rather than static chat <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.
*   **Details on Demand**: Allowing users to click citations for additional context, including what the model was "thinking" <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
*   **Structured Interactive Outputs**: Enabling users to "pull the thread" on specific findings, like asking for more details on rising capex spend <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.
*   **Highlighting and Interrogating**: Allowing users to highlight any text passage and ask for implications or further information <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.
*   **Audit Trail ("Receipts")**: Providing an ability to "turn over that cube" of high-dimensional data and see the underlying findings, such as a fundraising timeline or ongoing litigation <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>. This acts as a "magnifying glass for text," enabling human analysts to drill into crucial details that catch their eye <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.

The final form factor for this class of products is still being determined, representing a significant design problem <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.