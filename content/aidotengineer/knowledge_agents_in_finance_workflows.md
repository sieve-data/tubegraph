---
title: Knowledge agents in finance workflows
videoId: MWTJIAwAAnk
---

From: [[aidotengineer]] <br/> 

Mike Con, founder and CEO of Brightwave, describes how knowledge agents are transforming financial workflows by automating complex research and analysis tasks that are beyond human scale <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## The Challenge in Financial Research

Finance professionals face significant challenges when conducting research and due diligence <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>:
*   **Due Diligence**: In competitive deal processes, analysts must quickly gain conviction from data rooms containing thousands of pages of content, identify critical risk factors, and do so under extreme time pressure <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
*   **Earnings Season**: Mutual fund analysts cover 80-120 companies, sifting through calls, transcripts, and filings to understand market dynamics at both sector and individual ticker levels <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Contract Analysis**: In confirmatory diligence, reviewing hundreds of vendor contracts to spot early termination clauses or understand portfolio-wide negotiation themes is a "non-trivial problem" <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

These tasks are often beyond human-level intelligence, pushing junior analysts into a "meat grinder" with impossible demands and tight deadlines <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. The human cost of performing this work manually is substantial <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## The Agentic Solution

The emergence of [[AI agents and agentic workflows | AI agents]] and knowledge agents, like Brightwave's research agent, addresses these challenges <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. These systems can digest vast volumes of content and perform meaningful work, accelerating efficiency and time-to-value by orders of magnitude <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### Historical Parallel: Spreadsheets

The shift in finance workflows mirrors the impact of computational spreadsheets in the late 1970s <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. Before spreadsheets, accountants manually "ran the numbers" on physical ledger paper, a cognitively demanding, important, and time-intensive job <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Today, no one wants that manual job because tools have drastically increased the sophistication of thought that can be applied to financial analysis <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Similarly, [[role of AI agents in workflow automation | AI agents using humanlike interfaces and workflows]] are elevating the level of analysis possible in finance <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Technical Considerations for [[Agentic systems and workflows | Agentic Systems]]

### Reasoning and Error

Non-reasoning models primarily perform greedy local searches, leading to significant error rates when chained together. For instance, an error rate of 5-10% in extracting organizations from an article can lead to exponentially increasing errors in multi-step processes <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. The winning systems will perform end-to-end Reinforcement Learning (RL) over tool use calls, where API call results inform the RL sequence of decisions, allowing for locally suboptimal decisions to achieve globally optimal outputs <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. This remains an open research problem <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

### Product Design and User Experience

A critical design challenge is how to reveal the thought process of a system that has considered 10,000 pages of content in a useful and legible way to a human <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. The final form factor for such products has not been determined, and simple chat interfaces are likely insufficient <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

Instead of expecting users to become "prompting experts" (which can take thousands of hours), products should provide scaffolding to orchestrate workflows and shape system behavior <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. Verticalized product workflows are likely to endure because they explicitly define user intent <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

### Mimicking Human Decisions

Basic [[developing AI agents and agentic workflows | autonomous agents]] should mimic the human decision-making process <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. This involves decomposing tasks such as:
1.  **Assessing content**: From SEC filings, earnings transcripts, knowledge graphs, or news sources <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
2.  **Identifying relevant document sets**: Determining which documents pertain to the query <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
3.  **Distilling findings**: Extracting information that supports hypotheses or investment theses <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
4.  **Enriching and Error Correcting**: This includes adding intermediary notes ("think out loud") about what the system believes based on initial findings <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. Models can self-correct by being asked to verify factual entailment or object classification <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

### Synthesis and Limitations

Synthesis, the process of weaving together disparate fact patterns from multiple documents into a coherent narrative, is crucial <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. However, current models face limitations:
*   **Output Length**: Models often struggle to produce very long, coherent outputs (e.g., 50,000 tokens) because training data lacks such extensive human-generated content <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
*   **Compression Problem**: Large input context windows compress information, leading to less specific outputs <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. Decomposing research instructions into multiple sub-themes can yield higher quality, more information-dense results <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
*   **Combinative Reasoning**: Models lack sufficient training demonstrations for complex combinative reasoning across multiple documents, making it hard to generate truly thoughtful analysis <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.
*   **Complex World Situations**: Models struggle with factors like temporality (e.g., understanding changes from mergers or contract addendums) <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.

### Human Oversight and Product Interface

Human oversight remains extremely important <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. The ability to "nudge" the model with directives or select interesting threads to explore is crucial because human analysts possess information not yet digitized, such as conversations with management or insights from portfolio managers <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

The anthropomorphizing of systems (e.g., "portfolio manager agent") can constrain flexibility <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. Instead, a "Unix philosophy" approach with simple tools that do one thing well and work together via a universal interface (like text) is preferred <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

The "latency trap" is a key concern: if the feedback loop for user interaction is too long (e.g., 8-20 minutes), users cannot refine their mental models of the system or develop fluency <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

## Brightwave's Product Approach

Brightwave aims to reveal the agent's thought process by presenting information as a "surface" rather than just a chat <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. Key features include:
*   **Details on Demand**: Users can click on citations to get additional context about a finding, including what the model was "thinking" <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
*   **Interactive Outputs**: Structured outputs allow users to "pull the thread" on specific findings <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.
*   **Continuous Surface**: Users can highlight any passage of text to ask for more details or implications <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.
*   **Audit Trail**: The system provides an "audit trail" by laying out all findings (e.g., fundraising timelines, litigation details) discovered from reviewing documents, allowing users to drill in on points of interest <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. This "magnifying glass for text" empowers the analyst's "taste" in identifying critical information <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.

The final form factor for this class of products is still evolving <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>. Brightwave is actively involved in [[developing AI agents for productivity | developing AI agents for productivity]] and [[AI tools in financial research and due diligence | AI tools in financial research and due diligence]], hiring professionals for roles such as product designer and front-end engineer <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>. They believe the most powerful products will lean into human taste-making abilities <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.