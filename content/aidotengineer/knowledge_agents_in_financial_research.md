---
title: Knowledge agents in financial research
videoId: MWTJIAwAAnk
---

From: [[aidotengineer]] <br/> 

Knowledge agents are advanced research tools designed to digest large volumes of content, particularly in the financial domain, to aid professionals in complex analysis and decision-making processes <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Brightwave, for instance, builds such a research agent specifically for financial applications <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## The Problem: Challenges in Financial Research

Financial professionals often face immense pressure to process vast amounts of information under tight deadlines <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Examples include:
*   **Due Diligence:** In competitive deal processes, analysts entering a data room with thousands of pages of content need to quickly reach conviction and identify critical risk factors that could diminish asset performance <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   **Earnings Season:** Mutual fund analysts covering 80-120 companies must navigate numerous calls, transcripts, and filings to understand market dynamics at both sector and individual ticker levels <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Confirmatory Diligence:** Reviewing hundreds of vendor contracts to spot early termination clauses or understand thematic negotiation strategies across an entire portfolio is a non-trivial task that can be beyond human capacity <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

The manual execution of these tasks is described as a "meat grinder" for junior analysts, highlighting the significant human cost and the impossible demands placed on them <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## The Solution: Efficiency Improvements with AI

The advent of knowledge agents is compared to the introduction of computational spreadsheets in the late 1970s <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Just as spreadsheets transformed the role of accountants from manually "running the numbers" to applying more sophisticated thought to financial problems, knowledge agents aim to similarly elevate the work of financial analysts <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

Systems like Brightwave can digest large volumes of content and perform meaningful work, accelerating [[efficiency_improvements_with_ai_in_financial_analysis | efficiency improvements]] by orders of magnitude and reducing time to value in financial markets <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## Design and Technical Considerations for Knowledge Agents

Building high-fidelity research agents involves significant [[design_considerations_for_financial_ai_tools | design considerations for financial AI tools]] and technical challenges <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. A primary [[design_challenges_in_building_web_research_agents | design challenge]] is how to reveal the thought process of a system that has considered thousands of pages of content in a useful and legible way to a human <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. The final form factor for these products is still evolving, with simple chat interfaces likely being insufficient <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

### Model Limitations and "Greedy Local Search"
Non-reasoning models often perform "greedy local search," meaning they might not achieve globally optimal outputs <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. For example, a model might fail to extract all organizations from an article, and a 5-10% error rate can exponentially increase errors when calls are chained together <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. Winning systems will likely perform end-to-end Reinforcement Learning (RL) over tool use calls, where API call results influence subsequent decisions to achieve globally optimal outcomes, although this remains an open research problem <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### The "Latency Trap"
The "latency trap" refers to the time it takes for an agentic system to produce realized value <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. If feedback loops are too long (e.g., 8-20 minutes), users cannot perform enough repetitions in a day to refine their mental model of how prompts elicit desired behaviors from the system, hindering their fluency and overall product experience <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.

### Synthesis and Output Length
A significant limitation is the characteristic output length of current models, often around 2,000-3,000 tokens, even with large context windows <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. This means models are designed to produce summarized or compressed information rather than extensive, novel text <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. To achieve higher quality, more information-dense outputs, research instructions need to be decomposed into multiple, granular sub-themes <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

Another challenge is the low presence of combinative reasoning demonstrations in training data <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. It's easy for a model to write a new epilogue for a book it has effectively "read," but it's much harder to synthesize disparate fact patterns from multiple documents, like in biomedical literature synthesis, to produce useful and thoughtful analysis <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

### Real-World Complexities
[[domain_specific_language_models_in_finance | Domain specific language models in finance]] still have limitations in managing complex real-world situations, such as understanding temporality (e.g., how financial statements change after a merger) or propagating metadata that contextualizes evidentiary passages <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.

## Design Patterns and Product Features

Effective knowledge agents mimic the human decision-making process by decomposing tasks <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. This involves:
1.  **Assessing relevant document sets:** Identifying public market comparables, SEC filings, earnings call transcripts, or even internal knowledge graphs from previous deals <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
2.  **Distilling findings:** Extracting information that substantiates hypotheses about an investment thesis <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
3.  **Enriching and Error Correcting:** Generating intermediary notes (e.g., "think out loud" about beliefs based on findings) and allowing the model to self-correct for factual accuracy <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. It can be more powerful to perform self-correction as a secondary call rather than within the same chain of thought <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
4.  **Synthesis:** Weaving together fact patterns from many documents into a coherent narrative <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

### Human Oversight and Control Loop
Human oversight is crucial <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. The ability to "nudge" the model with directives or to select an interesting thread to "pull" is vital because human analysts often have access to non-digitized information, such as conversations with management or insights from portfolio managers <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. This "taste making" ability will be where the most powerful products lean <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

### Brightwave's Approach: Revealing Thought Processes
Brightwave aims to make the agent's thought process transparent to the user, similar to how human visual processing allows quick recognition even in a low-precision product <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. Features include:
*   **Clickable Citations:** Users can click on a citation to get not just the source document, but also context about what the model was "thinking" <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   **Structured Interactive Outputs:** These allow users to "pull the thread" on specific findings, like rising capital expenditure <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.
*   **Highlighting for More Information:** Any passage of text can be highlighted to ask for more details or implications <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.
*   **High-Dimensional Data Structure:** The model's discoveries are viewed as a high-dimensional data structure, with the report being one view <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>. This provides an audit trail and allows users to "turn over that cube" to see all findings, such as fundraising timelines or ongoing litigation <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>.
*   **Drill-in Capability:** Users can click on any interesting finding, like patent litigation or a factory fire, to get additional details on demand <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>.

## Future Outlook

The final form factor for this class of products is still evolving, representing an extremely interesting [[future_directions_for_research_agents | design problem]] <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>. The "Pareto Frontier" for compute and performance/price trade-off will continue to move, requiring careful selection of tools and models for each node in a compute graph <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.