---
title: Generative AI project challenges and strategies
videoId: OpVkWc3YnFc
---

From: [[aidotengineer]] <br/> 

## Introduction

Generative AI (Gen AI) projects face significant hurdles despite widespread enthusiasm <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. Gartner predicted in the previous year that 30% of generative AI projects would be abandoned by the end of 2025 <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Many organizations struggle to get their Gen AI applications into production <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Success requires a strategic approach within organizations, effective leadership engagement, and the right technological foundations <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

## Key Challenges in Generative AI Projects

[[Challenges in scaling generative AI | Challenges]] in implementing Gen AI projects can manifest in various forms:

*   **Project Abandonment and Production Failure**: A significant portion of Gen AI projects are predicted to fail or not reach production <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, with a common reason being the lack of a clear business use case that solves real problems and is monetizable <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   **Unrealistic Leadership Expectations**: Executives, exposed to Gen AI through popular culture, may demand rapid deployment (e.g., "in production in two months") without understanding the technical complexities or organizational [[Challenges with current AI implementation | challenges]] involved <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **Organizational Silos and "Not Invented Here" Syndrome**: Teams may resist new solutions, preferring established platforms or frameworks, leading to internal friction <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. Large organizations (50,000+ people) often present [[Design challenges for AI agents | challenges]] in navigating internal politics and varied departmental objectives <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   **Cost Concerns**: Gen AI architectures can be significantly more expensive than classic or cloud computing if not well-designed, increasing organizational costs <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. This requires justifying substantial R&D investment for redevelopment <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   **Internal Resistance ("Friendly Fire")**: Colleagues at similar or higher levels may view new AI initiatives as encroaching on their "turf" or demand integration with their existing systems, complicating scope <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
*   **Vendor Influence**: External vendors often approach chief digital officers with "build vs. buy" arguments, potentially undermining internal development efforts <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
*   **LLM Limitations**: Large Language Models (LLMs) can produce "hallucinations," which is a significant challenge for enterprise applications requiring accuracy <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. While newer models are improving, ensuring accurate information remains a concern <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.

## Strategies for Success

To overcome these [[Challenges and innovations in AI engineering | challenges]], a multi-faceted approach is necessary:

*   **Identify a Strong Business Use Case**: Prioritize projects that address real business problems and offer clear monetization opportunities <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. A compelling use case can even involve critical applications, such as accelerating the delivery of life-saving drugs <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   **Navigate Organizational Dynamics**:
    *   **Know Your Audience**: Understand the motivations and priorities of different organizational levels, from C-suite executives who focus on broad vision (e.g., "change a billion lives a year") to middle managers who prioritize cost savings, cost avoidance, earlier revenue, or balanced headcount <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
    *   **Personalize Communication**: Tailor your message and data (e.g., numbers and timelines) to resonate with each audience <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
    *   **Engage Users Early**: While tempting to go to users first for direct feedback, remember that executive buy-in is crucial in large organizations <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Users will embrace tools that automate boring tasks, provided they deliver accurate and performant results <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Leverage Appropriate Technology**: Select technologies that directly address the specific use case and organizational needs.

## Case Study: Biopharma Technology Transfer with Graph RAG

One successful implementation involved a biopharma company addressing the [[Challenges and Opportunities in AI and Agent Capabilities | challenge]] of technology transfer <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

*   **The Problem**: Scaling drug development from lab bench to industrial production (e.g., millions of doses daily) typically takes years <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This process involves sifting through hundreds of thousands of scientific documents and notes <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. A significant factor compounding this is the drastic reduction in the average tenure of manufacturing workers, from 20 years in 2019 to just three years currently, leading to a loss of institutional knowledge <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **The Solution**: The company leveraged Gen AI and a Graph Database to capture and transfer intelligence from documents and tacit knowledge to new personnel <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. Millions of documents were loaded into a graph database, with content "chunked" and structured within the graph (document, block, paragraph, line) <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This structure allowed for learning and refining how documents were chunked over time <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Why Graph Databases?**: While traditionally used for genealogic sequences, social networks, or hierarchies, the graph database offered significant benefits for this application <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.
    *   **Faster Data Understanding**: Consolidating data in the graph reduced the time for data scientists, engineers, and developers to understand the data landscape from three months to three weeks or less <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.
    *   **Improved Team Performance**: The enhanced data traversal capabilities of graphs significantly boosted team performance <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.
    *   **Enhanced Contextual Knowledge**: Graphs make implicit connections explicit, allowing for a "neighborhood of related stuff" to be presented to the LLM for better contextual knowledge <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.
*   **Graph RAG Architecture**: This approach combines vector and knowledge graph representations of data <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>. The Gen AI application queries both the vector for an answer and the graph database for relationally close nodes, providing additional context to the LLM <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>. This yields more contextually relevant and precise results compared to direct LLM use or baseline vector database RAG, which can still be generic or suffer from hallucinations <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
*   **Benefits of Graph RAG**:
    *   **Better Governance**: Controls and properties can be applied to graph nodes to manage information access <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.
    *   **Improved Explainability**: Answers from the LLM can be reasoned about by examining graphs, nodes, and edges, allowing for a clear understanding of relationships and why certain information is relevant (or irrelevant) <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. This is crucial for business-critical industries where accuracy is paramount <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.

Ultimately, navigating the [[Challenges and insights in developing AI coding agents | challenges]] of Gen AI projects requires understanding diverse stakeholders, adopting a targeted communication strategy, and selecting robust technologies like Graph RAG to build reliable and explainable systems <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.