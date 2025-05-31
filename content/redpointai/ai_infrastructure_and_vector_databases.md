---
title: AI infrastructure and vector databases
videoId: 1gLHnRDiIms
---

From: [[redpointai]] <br/> 

Pinecone, a vector database that has raised over $130 million at a $750 million valuation, has become a core tool for building AI applications <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. CEO and founder Eo Liberty discusses the [[market_landscape_for_vector_databases | vector database landscape]], barriers for enterprises building AI apps, and future [[ai_infrastructure_and_startup_opportunities | AI infrastructure and opportunities]] <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Evolution and Impact of Generative AI
Before the generative AI "craze" and the launch of ChatGPT, vector databases were vastly underutilized for many use cases, including semantic search, candidate generation, ranking, feed ranking, and recommendations <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Larger companies like Google and Amazon used them internally, but educating the broader market was challenging <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Investors were often confused when vector databases were pitched <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Earlier, Eo Liberty had worked on AWS SageMaker, an MLOps product, and many initially mistook Pinecone for an MLOps solution <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

The launch of OpenAI's ChatGPT elevated the discussion to a broader audience <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. While the core technology of vector databases didn't significantly change for practitioners, the surge in capital and energy made it accessible to non-AI engineers <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Pinecone experienced an "insane" increase in demand, sometimes seeing 10,000 sign-ups daily, pushing them to exhaust cloud machine resources and spend millions monthly on their free tier <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. This necessitated a complete redesign, leading to their "serverless" solution, which is two orders of magnitude more efficient <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

A particular moment that spiked usage was the open-source gadget "AutoGPT," a minimalistic precursor to what is now called an agent <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. This tool's popularity meant Pinecone was suddenly being onboarded by people like "the dentist that remembers Python from college" rather than systems engineers <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. While this normalized, most current users are builders <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

## Scaling and Applications of Vector Databases
Pinecone truly excels at handling hundreds of millions to billions of vectors <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. For companies that are themselves SaaS providers, such as Notion or Gong, Pinecone allows them to develop deep AI solutions (Q&A, semantic search) for their customers' data <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. For example, a company with 10,000 customers, each with a million documents, would need a vector database capable of handling 10 billion embeddings across thousands of partitions cost-effectively <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. Pinecone's serverless architecture significantly reduces costs, potentially to a dollar or even 50 cents per paying user per year for their customers <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

Common applications built on Pinecone include:
*   Q&A and semantic search <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>
*   Chatbots and support bots <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>
*   Legal discovery <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>
*   Medical history discovery and analytics <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>
*   Applications involving images, audio, video <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>
*   Anomaly detection and security <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>
*   Pharma and drug discovery <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>

While there's interest in multimodal applications, text data still dominates for mainstream technology developers <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

## Barriers to AI Adoption and Solutions
One of the biggest barriers for companies deploying AI applications is hallucination <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. Large language models (LLMs) are designed to generate language, and they will produce text even when they "know nothing" about a topic, similar to a student in sixth grade <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

Solutions to address hallucinations include:
*   **Measurement**: The ability to truly measure hallucinations is only just beginning <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. A model that never hallucinates by always saying "I don't know" is useless <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>. The focus must be on measuring usefulness, correctness, and faithfulness to data <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
*   **Retrieval Augmented Generation (RAG)**: This involves making data available to the model in a secure, governed, and controllable way using vector databases <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>. RAG, based on semantic search, is where the "magic sauce" happens in AI applications <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. An LLM with a vector database and RAG can already outperform GPT-4 today in certain experiments <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.

## [[Market landscape for vector databases | Vector Database Market Landscape]]
Vectors are considered the "language of AI" <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>. The understanding that vectors are a fundamental data type, like sentences or images, has led to an explosion of startups and incumbents adding vector support <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>. However, simply adding a "float array" type doesn't make a database a true vector database <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>. True vector databases are unique because the numeric array *is* the key, organizing data and enabling search in a highly optimized way <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>. Bolting on vector support to a non-AI technology will lead to "incredibly poor performance" <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.

## Recommended RAG Stack and [[AI Infrastructure and Tooling | AI Infrastructure]]
For a RAG product, smaller, cheaper, and easier-to-manage open-source models can achieve good performance, eliminating the need to spend a lot of money on larger models <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.

Key components of a RAG stack:
*   **Vector Database**: Pinecone <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>
*   **Data Transformation/Movement**: AnyScale's product <a class="yt-timestamp" data-t="00:21:37">[00:21:37]</a>. Unstructured is also noted as a viable option for embedding generation and data generation into vector databases <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>. Companies like FiveTran that import data from Snowflake can leverage specialized companies to transform and fit data into a vector database <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>.
*   **LLMs**: Pinecone partners with Cohere, AI21, and Hugging Face <a class="yt-timestamp" data-t="00:21:59">[00:21:59]</a>.
*   **Evaluation Technology**: A leader has yet to emerge in this space <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.

The market will find a stable point with a good trade-off between cost, compute, infrastructure, and output quality <a class="yt-timestamp" data-t="00:25:17">[00:25:17]</a>. Running very large models for every API call is unsustainable due to cost and environmental impact <a class="yt-timestamp" data-t="00:25:53">[00:25:53]</a>. While context windows are getting longer, this is a pricing model for model companies <a class="yt-timestamp" data-t="00:27:09">[00:27:09]</a>. Sending all company data to an LLM on every query is slow, expensive, and often doesn't improve results <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>. Using a vector database for retrieval allows sending significantly fewer tokens (e.g., 3,000-10,000 instead of 100,000), reducing costs by 90% without performance loss <a class="yt-timestamp" data-t="00:29:02">[00:29:02]</a>.

Most companies are still in the early stages of getting AI applications to work <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>. Iteration over embedding models, retrieval, reranking, and filtering is less common <a class="yt-timestamp" data-t="00:30:14">[00:30:14]</a>. Building a complete AI solution around a vector database takes time and involves many considerations like speed, cost, accuracy, data freshness, and input/output format <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>.

## Business and Future Outlook
Pinecone's transition to a serverless model, though painful for revenue in the short term, was seen as necessary for long-term customer benefit and market fit <a class="yt-timestamp" data-t="00:37:29">[00:37:29]</a>. Some customers saw a 70-90% reduction in cost <a class="yt-timestamp" data-t="00:38:54">[00:38:54]</a>. This strategic move ensures Pinecone fits into the cost structure of tens of thousands of future AI workloads <a class="yt-timestamp" data-t="00:40:23">[00:40:23]</a>.

Regarding [[ai_infrastructure_and_startup_opportunities | startup opportunities in AI infrastructure]], Eo Liberty is more excited about the application and solution space <a class="yt-timestamp" data-t="00:41:15">[00:41:15]</a>. Infrastructure often follows a "winner take all" phenomenon, limiting space for new players <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>. The solution layer, however, is "teaming with innovation," with hundreds of new applications constantly emerging <a class="yt-timestamp" data-t="00:42:01">[00:42:01]</a>.

Future shifts in [[ai_infrastructure_and_tooling | AI infrastructure]] are predicted:
*   **Hardware**: A significant shift is expected away from the current unsustainable reliance on GPUs. This could involve more CPU workloads, models adapted for CPUs, or specialized servers optimized for training and serving <a class="yt-timestamp" data-t="00:47:56">[00:47:56]</a>.
*   **Data Pipelines**: Existing tools from 5-10 years ago are insufficient, leading to operational headaches, high costs, and long wait times <a class="yt-timestamp" data-t="00:49:03">[00:49:03]</a>.
*   **Governance and Visibility**: Moderating systems are needed to provide governance and control over AI stacks that currently run "open loop" for most companies <a class="yt-timestamp" data-t="00:49:34">[00:49:34]</a>.

## Overhyped, Underhyped, and Surprises
*   **Overhyped**: Foundational models are considered overhyped because, while powerful, qualitative progress has stagnated for some time <a class="yt-timestamp" data-t="00:50:54">[00:50:54]</a>.
*   **Underhyped**: [[ai_coding_assistants_and_their_uses | Code generation]] and [[ai_coding_assistants and their uses | coding assistants]] are "exceedingly useful" and considered one of the most exciting use cases <a class="yt-timestamp" data-t="00:51:11">[00:51:11]</a>.
*   **Biggest Surprise**: A complete rewrite of Pinecone's database in Rust, which was thought to be "borderline suicide" and take six months, was completed in 2-3 months and yielded significantly better results, avoiding the common pitfalls of rewrites <a class="yt-timestamp" data-t="00:51:51">[00:51:51]</a>.

## Reflections on AI in Larger Companies and Agents
Large companies like Amazon (where Eo Liberty previously worked on SageMaker), Google, and Microsoft have different innovation horizons and risk appetites <a class="yt-timestamp" data-t="00:46:02">[00:46:02]</a>. Their products need to generate hundreds of millions of dollars annually to "move the needle," whereas startups can focus on emerging parts of the stack years before they hit the mainstream market <a class="yt-timestamp" data-t="00:46:02">[00:46:02]</a>.

On AI agents, Eo Liberty believes they "work already," with the probability of completing a task getting close to human levels <a class="yt-timestamp" data-t="00:54:02">[00:54:02]</a>. While their mistakes might be "silly" or "embarrassing" compared to human errors, their overall performance is decent <a class="yt-timestamp" data-t="00:54:15">[00:54:15]</a>.

A common failure mode for those trying to implement AI solutions is incorrect cost estimation <a class="yt-timestamp" data-t="00:35:59">[00:35:59]</a>. Often, initial napkin math leads to inflated cost projections that deter companies from even starting a project <a class="yt-timestamp" data-t="00:35:02">[00:35:02]</a>. The most significant failure, however, is "doing nothing" <a class="yt-timestamp" data-t="00:55:49">[00:55:49]</a>.