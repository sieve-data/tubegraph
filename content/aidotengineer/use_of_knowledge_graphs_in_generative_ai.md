---
title: Use of Knowledge Graphs in Generative AI
videoId: OpVkWc3YnFc
---

From: [[aidotengineer]] <br/> 

Generative AI (GenAI) projects face significant challenges, with Gartner predicting that 30% of such projects will be abandoned by the end of 2025 <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. A primary reason for this failure rate is the absence of a clear business use case that solves real problems and is monetizable <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. While the desire to achieve "amazing things" with GenAI is strong, organizations often struggle with the right approach, internal sales, and suitable technologies <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. Often, executives have heard about GenAI and expect quick, all-encompassing solutions, leading to unrealistic timelines <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## Real-World Application: Technology Transfer in BioPharma

A successful implementation of GenAI, leveraging [[semantic_and_graphbased_data_in_ai_systems | semantic and graph-based data]], has been demonstrated in a large life sciences company like Pfizer <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. The core business case addressed was "technology transfer" in biopharma <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. This involves scaling up drug development from a lab bench (human scale) to industrial production (millions of doses per day) <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This process typically takes years because industrial teams must sift through hundreds of thousands of documents, notes, and test outcomes from the science level <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

A critical challenge exacerbating this problem is the significant drop in manufacturing worker tenure. A 2019 study showed an average tenure of 20 years, which has now fallen to three years <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. This "brain drain" means that immense expertise, often captured in documents or even tacit knowledge, is retiring <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. Generative AI is essential to capture this intelligence and transfer it to new employees <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### How Graphs are Used in this Context

Millions of documents are loaded into a graph database <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. Instead of loading entire documents, specific "chunks" (document, block, paragraph, line) are loaded, and their structure is maintained within the graph <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. This structuring allows for refined similarity search, identifying which chunks yield the most desired results <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. The ability to structure this chunking in the graph enables continuous learning and improvement in how documents are chunked in the first place <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

This application not only represents a strong business use case but also potentially saves lives by accelerating the delivery of life-saving drugs <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Overcoming Organizational Challenges

Implementing GenAI, especially with new technologies like graph databases, presents human and organizational challenges <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. Teams may exhibit "not invented here" syndrome, preferring existing platforms or frameworks <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. Cost is another major concern, as GenAI architectures can be significantly more expensive if not well-architected <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Convincing stakeholders to invest in an R&D-heavy GenAI architecture over an existing, albeit less efficient, system is a key hurdle <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

In large organizations (e.g., 50,000+ people), advocating for a new AI capability requires understanding the complex hierarchy and communication <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. While users at the bottom of the hierarchy value tools that eliminate "boring stuff" and provide accurate, performant results <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>, gaining executive buy-in is crucial.

Connecting with top executives (e.g., CEO) is difficult <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. These leaders often derive their vision from consultants <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>, focusing on high-level aspirations like "change a billion lives a year" <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. This message trickles down to C-level officers (Chief Digital Officer, Chief Scientific Officer, Chief Supply Officer) who translate it into their specific departmental goals, such as leading in AI, tackling diseases, or accelerating supply <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

Further down, level twos and threes prioritize tangible metrics like cost savings, cost avoidance, earlier revenue, or balanced headcount <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. Pitches at this level require specific numbers and timelines <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>. "Client partners" acting as intermediaries between digital teams and business units may have conflicting views, either limiting scope or demanding integration across all tools <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

Finally, internal "friendly fire" from colleagues (either above or at the same level) who perceive the new project as encroaching on their turf or demanding integration with their existing systems can be a hurdle <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. The key to navigating these complex organizational dynamics and [[best_practices_for_building_genai_teams | building effective AI agents]] is to know your audience, personalize your message, and communicate at the appropriate level <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.

## Technological Advantages: Why Graph Databases?

One of the biggest challenges in building Retrieval Augmented Generation (RAG) and enterprise applications is managing LLM hallucinations <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. While newer models and vector databases help feed the right information, [[benefits_of_graph_databases_in_ai_applications | graph databases]] offer a unique and powerful approach <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.

Graphs excel in applications involving complex connections like genealogic sequences, recipes, social networks, hierarchies, or time series <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>. Consolidating data in a graph significantly accelerates data scientists' and engineers' understanding of the data landscape, reducing data consolidation and cleanup time from three months to three weeks or less for a new project <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>. Beyond improved data traversal and search performance, using graphs also boosts team performance <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.

### Graph RAG Architecture

The concept of Graph RAG, where existing documents are chunked into a graph using LLMs, has been shown to yield superior results, as highlighted by a seminal Microsoft paper <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>.

*   **Direct LLMs** provide good results but lack enterprise context and knowledge <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.
*   **Vector databases** (baseline RAG) offer better results by pulling in organizational knowledge, but answers can still be generic with hallucinations <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.
*   **Graph RAG** leads to much more precise answers by leveraging the [[semantic_and_graphbased_data_in_ai_systems | knowledge graph]], which can be evolved over time <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.

A common [[knowledge_graph_mullet | architecture for graph RAG]] involves taking a GenAI application and creating both a vector and a knowledge graph representation of the data <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>. The application queries the vector for similarity and retrieves relationally close nodes from the graph database for additional context <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>. This information is then passed to the LLM, resulting in more contextually relevant output <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

This approach offers several key benefits:
*   **Better Governance**: Controls and properties can be applied to graph nodes to manage access to information <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.
*   **Improved Explainability**: Instead of statistical probabilities from vector space, answers can be traced back to graphs, nodes, and edges, allowing for reasoning about relationships <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.

For business-critical industries like life sciences and manufacturing, where accuracy is paramount, [[graphbased_fraud_detection_and_ai_technology | graph-based AI solutions]] provide the precision and contextual understanding needed to solve real problems and contribute to a good cause, such as accelerating drug delivery and saving lives <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.