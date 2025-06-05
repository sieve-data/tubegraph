---
title: AI tools in financial research and due diligence
videoId: MWTJIAwAAnk
---

From: [[aidotengineer]] <br/> 

Brightwave, led by founder and CEO Mike Khan, develops a research agent designed to digest extensive content corpuses within the financial domain <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This technology addresses the non-trivial task of quickly gaining conviction in competitive deal processes, spotting critical risk factors, and analyzing market trends at both sector and individual ticker levels <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## The Challenge of Manual Financial Research

Financial professionals, particularly junior analysts, often face immense pressure to perform impossible tasks under extremely tight deadlines <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Examples of these demanding tasks include:
*   **Due Diligence**: Stepping into data rooms with thousands of pages of content pre-term sheet and needing to quickly assess risks and opportunities <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
*   **Earnings Season Analysis**: Mutual fund analysts covering 80-120 names must process calls, transcripts, and filings to understand market happenings <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Confirmatory Diligence**: Reviewing hundreds of vendor contracts to identify early termination clauses or thematic negotiation patterns across an entire portfolio <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

Such tasks are "frankly not a human-level intelligence task" <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, leading to significant human cost and stress when performed manually <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## The Role of AI in Finance Workflows

The integration of AI into finance workflows draws parallels to the early adoption of spreadsheets <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. Before computational spreadsheets, accountants manually "ran the numbers," a cognitively demanding, important, and time-intensive job <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Today, no one wants that manual job because tools have allowed for a substantial increase in the sophistication of thought applied to problems, enabling more effective and efficient work <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

Similarly, systems like Brightwave and other [[knowledge_agents_in_finance_workflows | knowledge agents]] are capable of digesting vast volumes of content and performing meaningful work that accelerates efficiency and time-to-value by orders of magnitude <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## Brightwave's Approach and Design Philosophy

Brightwave aims to build a high-fidelity research agent <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. A core design problem is how to reveal the thought process of an AI that has considered thousands of pages of content in a useful and legible way, as the final form factor for such products is still evolving beyond simple chat interfaces <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Addressing Model Limitations
Non-reasoning models often perform "greedy local search," leading to fidelity issues <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. For example, if a model has a 5-10% error rate when extracting organizations from an article and these calls are chained, the likelihood of error increases exponentially <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. Winning systems will perform end-to-end Reinforcement Learning (RL) over tool use calls, where API call results influence the RL sequence of decisions, allowing for locally suboptimal decisions to achieve globally optimal outputs <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. However, intelligently leveraging tools to achieve global optimality remains an open research problem <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### Product Building and User Experience
While the "bitter lesson" suggests that more data, more compute, and better models will dominate <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>, the reality for product development today involves being "circumspect about what is the scope of behaviors that the system the agent is going to engage in" <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. This constrains model complexity, reducing the likelihood of degenerate outputs <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

Users are generally not expected to become prompting experts, as developing such a skill can take over a thousand hours <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. Therefore, verticalized product workflows that provide scaffolding to orchestrate these systems and specify user intent are likely to be enduring <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

## Archetypal Design Patterns for Autonomous Agents

To design effective autonomous agents, it's crucial to mimic the human decision-making process <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. This involves decomposing complex tasks into steps:
1.  **Assess Relevant Documents**: Like an analyst looking for public market comparables in SEC filings or earnings call transcripts <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
2.  **Distill Findings**: Extracting information that substantiates hypotheses or investment theses <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. Intermediate notes, or "thinking out loud," are extremely useful at this stage <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
3.  **Enrich and Error Correct Findings**:
    *   Models can be asked to verify accuracy, e.g., "is this factually entailed by this document?" or "is this an organization?" <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
    *   Performing this validation as a secondary call is often more powerful than within a Chain of Thought JSON, as models can be "primed to be credulous" otherwise <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

Through this process, the system synthesizes disparate fact patterns across many documents into a coherent narrative <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. Human oversight is extremely important, allowing users to nudge the model with directives or pull interesting threads, leveraging non-digitized information or specific insights <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

Applying the Unix philosophy, it's beneficial to think of these systems not as anthropomorphized agents (e.g., "portfolio manager agent") but as simple tools that do one thing and work well together, with text as the universal interface <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. This approach maintains flexibility as the compute graph's design needs change <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

## Challenges and Considerations for AI Systems

### The Latency Trap
The "latency trap" refers to the impact of the feedback loop on a user's mental model <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. If the feedback loop is long (e.g., 8-20 minutes), users cannot perform many iterations in a day, hindering their faculty with the system and product <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. The user's mental model develops based on the difference between their expectation for a report and its actual output, which is the "loss" <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.

### Synthesis Limitations
While models boast large context windows (e.g., 100,000 tokens), producing very long (e.g., 50,000 token) coherent and novel responses is difficult in practice <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. This is because instruction tuning datasets typically have characteristic output lengths; it's hard to write 50,000 coherent words as a human demonstration <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

This implies a "compression problem" where a large input context window is compressed into a shorter output <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. Higher quality and more information-dense outputs can be achieved by decomposing research instructions into multiple sub-themes, allowing the model to be more granular and specific <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

Furthermore, the presence of recombinative reasoning demonstrations in instruction tuning and post-training corpuses is low <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. It's easy for models to internalize a fixed corpus and generate variations (e.g., new epilogues for *The Great Gatsby*), but true synthesis involves weaving together disparate fact patterns from multiple documents, which is challenging <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

### Managing Complex Real-World Situations
Current models face limitations in managing complex real-world situations, such as:
*   **Temporality**: Understanding the sequence and impact of events, like how proforma financial statements change after a merger and acquisition <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.
*   **Addendums**: Propagating evidentiary passages with metadata that contextualizes their importance and relation to other evidence, especially for contract addendums <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

## Brightwave Product Features and UI/UX

Brightwave aims to reveal the AI's thought process through an interface that acts more like a "surface" <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. Key features include:
*   **Details on Demand**: Users can click on a citation to get additional context about the document and understand what the model was thinking <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   **Structured Interactive Outputs**: Allows users to "pull the thread" on a specific point, like inquiring about rising capital expenditure (capex) <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.
*   **Text Interrogation**: Users can highlight any passage of text and ask for more information or implications, similar to how Open AI's Canvas allows increasing the reading level of a passage <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.
*   **Audit Trail**: The system treats its discovered findings as a high-dimensional data structure, with the report being one view <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>. Users need to be able to "turn over that cube" to see the "receipts" or audit trail of the system's analysis, by clicking into documents or viewing laid-out findings like a fundraising timeline or ongoing litigation <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.
*   **"Magnifying Glass for Text"**: This allows analysts to drill in and get additional details on demand for specific items that catch their attention, such as patent litigation or a critical supply chain disruption <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.

The final form factor for this class of products is still evolving, representing an interesting design problem <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.