---
title: Business case and value propositions for GenAI
videoId: OpVkWc3YnFc
---

From: [[aidotengineer]] <br/> 

GenAI projects face significant challenges, with Gartner predicting that 30% of [[generative_ai_project_challenges_and_strategies | generative AI projects]] will be abandoned by the end of 2025. <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a> A primary reason for this failure rate is the lack of a clear business use case that solves real problems and can be monetized <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>. Many organizations struggle to move their GenAI applications into production <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.

## Identifying a Strong Business Case

A successful GenAI implementation requires a strategic approach within organizations, coupled with strong leadership buy-in <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>. Executives often have unrealistic expectations, envisioning GenAI as a universal problem-solver ready for production within months <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>.

### Case Study: Biopharma Technology Transfer

Jonathan Low successfully implemented GenAI capabilities within a large life sciences company, addressing a critical business need: technology transfer in biopharma <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>.

#### The Problem
*   **Scaling Production:** The process of scaling drug development from lab bench (human scale) to industrial scale (e.g., making a million doses a day) takes years <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.
*   **Information Overload:** Industrial teams must sift through hundreds of thousands of documents, notes, and test outcomes created at the science level <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.
*   **Loss of Expertise:** The average tenure of manufacturing workers has drastically decreased from 20 years to 3 years <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>. This, combined with the impending retirement of "boomers," means significant expertise is being lost <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.

#### The GenAI Solution and Value Proposition
Generative AI was identified as a necessary tool to capture intelligence from documents and individuals' heads and transfer it to new employees <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>.
*   **Accelerated Processes:** By using GenAI to manage and retrieve information, the time taken for technology transfer can be significantly reduced <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>.
*   **Knowledge Preservation:** It provides a mechanism to retain and disseminate critical knowledge that would otherwise be lost due to workforce changes <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>.
*   **Real-World Impact:** This particular use case not only streamlines business operations but also has the potential to save lives by accelerating the delivery of life-saving drugs <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.

The solution involved loading millions of documents into a graph database, where chunks of information (document, block, paragraph, line) were structured. This approach enabled the system to learn and improve how documents were chunked, leading to more refined storage and management <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.

## Overcoming Internal Challenges

Even with a strong business case, [[generative_ai_project_challenges_and_strategies | challenges]] persist in convincing internal stakeholders to adopt expensive R&D investments into GenAI architectures <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>.

### Addressing Stakeholder Concerns
*   **"Not Invented Here" Syndrome:** Teams may resist new solutions like graph RAG, preferring established frameworks or research papers <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>.
*   **Cost Concerns:** GenAI architectures can be significantly more expensive than classic or cloud computing if not well-architected, potentially increasing organizational costs <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>.
*   **Leadership Alignment:** In large organizations (50,000+ people), promoting a new idea requires navigating various levels of leadership <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>.
    *   **Executive Level (CEO):** Focused on broad, inspirational goals like "change a billion lives a year" <a class="yt-timestamp" data-t="11:08:00">[11:08:00]</a>.
    *   **Mid-Level Management (Chief Digital/Scientific/Supply Officers):** Translate executive vision into specific departmental goals, e.g., "lead the industry in AI" or "accelerate supply" <a class="yt-timestamp" data-t="11:36:00">[11:36:00]</a>.
    *   **Operational Level (Level Twos/Threes):** Prioritize tangible metrics such as "cost savings," "cost avoidance," "earlier realized revenue," or "more balanced headcount" <a class="yt-timestamp" data-t="12:15:00">[12:15:00]</a>. Presentations at this level must include numbers and timelines <a class="yt-timestamp" data-t="12:36:00">[12:36:00]</a>.
*   **Client Partners:** Act as intermediaries between digital teams and the business, often departmentalized (e.g., R&D, Supply). They might challenge proposals by citing existing solutions ("R&D already has five search engines") or suggest extreme scope changes ("incorporate into every tool") <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>.
*   **Vendor Pressure:** External vendors may advocate for buying their tools over in-house development, engaging with Chief Digital Officers on build-versus-buy decisions <a class="yt-timestamp" data-t="13:56:00">[13:56:00]</a>.
*   **Internal Competition ("Friendly Fire"):** Colleagues may claim ownership of similar initiatives or demand integration with their existing systems <a class="yt-timestamp" data-t="14:26:00">[14:26:00]</a>.

To succeed, it's crucial to understand your audience, personalize the message for each stakeholder, and communicate the value proposition in a language relevant to their specific concerns <a class="yt-timestamp" data-t="15:12:00">[15:12:00]</a>.

## Technological Underpinnings and Further Value

The chosen technology must be appropriate for the use case <a class="yt-timestamp" data-t="15:53:00">[15:53:00]</a>. A significant challenge in RAG (Retrieval Augmented Generation) and [[integration_of_ai_in_business_operations | enterprise applications]] is dealing with LLM hallucinations <a class="yt-timestamp" data-t="15:58:00">[15:58:00]</a>, although newer models and vector databases are improving this <a class="yt-timestamp" data-t="16:06:00">[16:06:00]</a>.

### The Value of Graph Databases for GenAI (Graph RAG)
Using graph databases offers unique advantages for GenAI implementations, particularly in complex domains with intricate connections:
*   **Contextual Understanding:** Graphs excel at representing genealogic sequences, recipes, social networks, hierarchies, and time series, all prevalent in a company like Pfizer <a class="yt-timestamp" data-t="16:29:00">[16:29:00]</a>.
*   **Accelerated Data Understanding:** Consolidating data in a graph significantly speeds up data scientists' and engineers' understanding of the data landscape, reducing data consolidation and cleanup time from months to weeks <a class="yt-timestamp" data-t="16:50:00">[16:50:00]</a>.
*   **Improved Team Performance:** Beyond just faster data traversal and search performance, using graphs also boosts overall team performance <a class="yt-timestamp" data-t="17:12:00">[17:12:00]</a>.
*   **Enhanced Precision and Context:** [[Generative AI project challenges and strategies | Graph RAG]], as highlighted by Microsoft's seminal paper, involves taking existing documents, using LLMs to chunk them into a graph, and yielding superior results <a class="yt-timestamp" data-t="17:38:00">[17:38:00]</a>.
    *   Direct LLMs may lack context <a class="yt-timestamp" data-t="17:55:00">[17:55:00]</a>.
    *   Baseline RAG with vector databases provides organizational knowledge but answers can be generic with hallucinations <a class="yt-timestamp" data-t="18:02:00">[18:02:00]</a>.
    *   Graph RAG offers more precise answers from the knowledge graph, which can evolve over time <a class="yt-timestamp" data-t="18:13:00">[18:13:00]</a>.
*   **Relationship Discovery:** In industries with complicated data, graph databases expose connections that might not be explicitly joined in relational databases. Searching for one piece of information immediately reveals its related "neighborhood" <a class="yt-timestamp" data-t="18:38:00">[18:38:00]</a>.
*   **Dual Data Representation:** A practical [[building_and_scaling_ai_use_cases_for_enterprises | architecture for graph RAG]] involves both vector and knowledge graph representations of data. The system queries both for answers and relationally close nodes, passing additional context to the LLM for more relevant results <a class="yt-timestamp" data-t="19:06:00">[19:06:00]</a>.
*   **Governance and Explainability:** Graph RAG enables better governance through controls and properties on graph nodes to manage access, and enhanced explainability as answers are derived from understandable graphs, nodes, and edges, rather than statistical probabilities <a class="yt-timestamp" data-t="19:47:00">[19:47:00]</a>. This allows reasoning about relationships and distinguishing relevant information <a class="yt-timestamp" data-t="20:05:00">[20:05:00]</a>.