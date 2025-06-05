---
title: Adoption of knowledge graphs in enterprise AI
videoId: OpVkWc3YnFc
---

From: [[aidotengineer]] <br/> 

The [[implementing_ai_in_enterprises | implementation of AI]] projects, particularly with generative AI (GenAI), presents significant challenges within enterprises. Gartner predicted that 30% of GenAI projects would be abandoned by the end of 2025 <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. A primary reason for this failure rate is the lack of a clear business use case that solves real problems and can be monetized <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. Furthermore, many projects struggle to reach production <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

## Case Study: Life Sciences Technology Transfer

A successful application of GenAI, leveraging [[knowledge_graph_and_its_role_in_ai | knowledge graphs]], was developed in a large life sciences company to address "technology transfer" <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### The Business Challenge
In biopharma, scaling drug development from lab bench to industrial scale (making millions of doses daily across multiple factories) typically takes years <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This lengthy process is due to industrial teams needing to sift through hundreds of thousands of scientific documents, notes, and test outcomes <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

An additional challenge is the significant decline in manufacturing worker tenure, from an average of 20 years in 2019 to just three years currently <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This means a vast amount of institutional expertise is retiring or will soon retire, highlighting the urgent need for GenAI to capture and transfer intelligence from documents and individuals' minds to new employees <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

### The Solution: Graph-based GenAI
To address this, millions of documents were loaded into a [[Graph data structures in AI and its benefits | graph]] <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. Rather than loading entire documents, specific "chunks" (documents, blocks, paragraphs, lines) were loaded and structured within the [[Graph data structures in AI and its benefits | graph]] <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. This structuring allowed for the refinement of how chunks were stored and managed, improving the accuracy of similarity searches and eventually leading to better document chunking over time <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

### Impact
This solution not only serves as a strong business use case but also potentially saves lives by accelerating the delivery of life-saving drugs <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Navigating Organizational Challenges in [[implementing_ai_in_enterprises | AI Adoption]]
[[integrating_ai_into_business_operations | Integrating AI into business operations]] within large organizations (50,000+ employees) presents significant human and financial challenges <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

### Common Obstacles
*   **"Not Invented Here" Syndrome**: Resistance from existing teams who may prefer other platforms or frameworks <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **Cost**: GenAI architectures can be significantly more expensive than classic or cloud computing if not well-architected <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Convincing stakeholders to invest in an R&D-heavy, potentially more expensive system is difficult <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
*   **Organizational Hierarchy**: Navigating the varied perspectives of different management levels is crucial <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>:
    *   **Top Executives (CEO)**: Focus on high-level, aspirational goals (e.g., "change a billion lives a year") <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
    *   **Mid-Level Leaders (CDO, CSO, CPO)**: Translate executive vision into departmental objectives (e.g., "lead the industry in AI," "accelerate supply") <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.
    *   **Operational Managers (Level Twos/Threes)**: Require concrete promises of cost savings, cost avoidance, earlier revenue, or balanced headcount, backed by specific numbers and timelines <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
*   **Client Partners**: Can either limit project scope ("Why build another search engine?") or expand it to an unmanageable degree ("Incorporate into every tool in the organization") <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.
*   **Vendors**: Introduce "build versus buy" dilemmas, influencing leadership on economic realism <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
*   **"Friendly Fire"**: Internal colleagues may claim turf, or demand integration with their existing systems <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

### Recommendations
To succeed in such environments, it is essential to "know your audience," personalize your message, and speak the appropriate language at each level of the organization <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.

## Technical Advantages of [[knowledge_graph_and_its_role_in_ai | Knowledge Graphs]] for Enterprise AI

A key technical challenge in [[ai_in_enterprise_applications | AI in enterprise applications]], especially with Retrieval Augmented Generation (RAG), is mitigating hallucinations from Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. While vector databases improve results by pulling organizational knowledge, answers can still be generic and prone to hallucinations <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.

### Why Choose a Graph Database?
Graph databases excel at representing complex relationships like genealogical sequences, recipes, social networks, hierarchies, and time series <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>. Beyond traditional benefits like easier traversal and improved search performance, consolidating data in a [[knowledge_graph_and_its_role_in_ai | graph]] significantly boosts team performance. Data scientists and engineers can understand the data landscape much faster—from three months to three weeks or less for new projects <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>. In a graph, relationships are inherently present, allowing for the discovery of related information ("neighborhood of related stuff") when searching <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.

### Graph RAG for Enhanced Precision
[[knowledge_graph_and_its_role_in_ai | Graph RAG]] (Retrieval Augmented Generation) represents an advanced approach to enterprise AI. Microsoft's seminal paper on Graph RAG demonstrated superior results by chunking existing documents into a [[Graph data structures in AI and its benefits | graph]] for LLM use <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>.

The architecture for Graph RAG combines both vector and [[knowledge_graph_and_its_role_in_ai | knowledge graph]] representations of data <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>:
1.  The vector database provides an initial answer <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.
2.  The [[Graph data structures in AI and its benefits | graph]] database provides relationally close nodes, offering additional context to the LLM <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.
3.  This results in more contextually relevant and precise answers from the expert system <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

### Benefits of Graph RAG
*   **Superior Results**: Achieves more precise answers compared to direct LLMs or baseline RAG with vector databases <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.
*   **Better Governance**: Allows for controls and properties on [[Graph data structures in AI and its benefits | graph]] nodes to manage access to information <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.
*   **Improved Explainability**: Instead of relying on statistical probabilities from vector space, answers are derived from [[Graph data structures in AI and its benefits | graph]] nodes and edges, which are easier for humans to reason about and understand relationships <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.
*   **Critical for High-Stakes Industries**: Essential for business-critical sectors like life sciences and manufacturing, where accuracy is paramount and errors are unacceptable <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.