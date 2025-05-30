---
title: Vector databases and their impact on AI applications
videoId: 1gLHnRDiIms
---

From: [[redpointai]] <br/> 

Pinecone, a prominent [[the_role_of_vector_databases_in_semantic_search_and_data_management | vector database]] company, has emerged as a fundamental tool for building [[impact_of_ai_advancements_on_business_models | AI applications]] <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. With over $130 million raised and a $750 million valuation, Pinecone plays a crucial role in the evolving [[the_role_of_vector_databases_in_semantic_search_and_data_management | vector database]] landscape <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## The Rise of Vector Databases

Before the generative [[impact_of_ai_advancements_on_business_models | AI]] craze and the launch of ChatGPT, [[the_role_of_vector_databases_in_semantic_search_and_data_management | vector databases]] were largely underutilized despite their potential for semantic search, candidate generation, ranking, feed ranking, and recommendation systems <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Large companies like Google and Amazon used them internally, but educating the broader market was challenging <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. Many investors initially misunderstood the concept, often confusing it with [[the_role_of_vector_databases_in_semantic_search_and_data_management | ML Ops]] products <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

The launch of OpenAI's ChatGPT significantly elevated the discussion around [[impact_of_ai_advancements_on_business_models | AI]] to a wider audience <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. While the underlying technology for practitioners didn't change drastically, the increased capital and energy behind [[impact_of_ai_advancements_on_business_models | AI]] made it accessible to non-[[impact_of_ai_advancements_on_business_models | AI]] engineers <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

A particular moment that caused usage to spike was the emergence of AutoGPT, an open-source precursor to [[advancements_and_implications_of_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. This tool's popularity led to a surge in Pinecone sign-ups, reaching up to 10,000 new users daily <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This demand forced Pinecone to rethink its architecture for scale and efficiency, leading to the development of its serverless solution, which is two orders of magnitude more efficient <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## Pinecone's Scale and Efficiency

Pinecone now truly shines at scales of hundreds of millions to billions of vectors <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. Companies, often SaaS providers, leverage Pinecone to build deep [[impact_of_ai_advancements_on_business_models | AI solutions]] like Q&A and semantic search for their own customers' data <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. For instance, a company with 10,000 customers, each having millions of documents, might need to handle 10 billion embeddings across thousands of partitions <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

The new serverless architecture allows for highly [[cost_efficiency_and_accessibility_in_ai_technologies | cost-effective]] multi-tenant workloads, with costs for a single paying customer potentially as low as a dollar or even 50 cents per year <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. This focus on unit economics is crucial for companies building true products rather than just lab experiments <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

> [!NOTE] Internal Challenge of Serverless Transition
> The transition to a serverless model was financially painful for Pinecone, impacting revenue growth as existing customers saw significant cost reductions (sometimes 70-90%) <a class="yt-timestamp" data-t="00:37:29">[00:37:29]</a>. However, it was deemed the right decision for customers and for fitting snugly into the [[cost_efficiency_and_accessibility_in_ai_technologies | cost structure]] required for mass [[impact_of_ai_advancements_on_business_models | AI adoption]] <a class="yt-timestamp" data-t="00:39:28">[00:39:28]</a>.

## Applications of Vector Databases

Common applications leveraging [[the_role_of_vector_databases_in_semantic_search_and_data_management | vector databases]] include:
*   **Q&A and Semantic Search**: Widely understood and deployed, such as Notion's [[enterprise_applications_for_ai_including_business_intelligence_and_data_extraction | AI Q&A]] features <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   **Chatbots and Support Bots**: Special flavors of Q&A systems <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Discovery and Analytics**: Including legal discovery, medical history discovery, and other forms of analytics that can be thought of as specialized search <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
*   **Multimodal Data**: Applications involving images, audio, video, anomaly detection, security, and even Pharma and Drug Discovery <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. However, text and images remain the "meat and potato" <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

While multimodal [[impact_of_ai_advancements_on_business_models | AI]] shows amazing potential in research labs, its widespread adoption by mainstream technology developers is unlikely in the next year or two <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. Even today, many companies struggle to train any deep learning model, let alone large foundational models <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

## Addressing Hallucinations with RAG

One of the biggest barriers to building effective [[impact_of_ai_advancements_on_business_models | AI apps]] is the issue of "hallucinations" in Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. LLMs are designed to generate language, and when compelled to write about unknown subjects, they will produce text that may contain inaccuracies <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

Retrieval Augmented Generation (RAG) is a critical approach to mitigating hallucinations <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>. RAG, fundamentally based on semantic search, ensures that LLMs retrieve relevant, factual information from a [[the_role_of_vector_databases_in_semantic_search_and_data_management | vector database]] before generating a response <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. This process enhances the "faithfulness" of the output to the data it was trained on or provided with <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

> [!TIP] Overcoming Hallucinations
> Measuring hallucinations accurately is a complex challenge, as a model that always responds with "I don't know" won't hallucinate but also won't be useful <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>. The goal is to measure usefulness, correctness, and faithfulness <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
>
> Loading large amounts of data into a [[the_role_of_vector_databases_in_semantic_search_and_data_management | vector database]] and running an LLM with even "not incredibly sophisticated RAG" can outperform more advanced models like GPT-4 <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.

RAG also addresses issues related to data security, governance (e.g., GDPR compliance for data deletion), and the practical limitations of large context windows offered by model companies <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. While larger context windows allow models to ingest more data, they are slow, expensive, and often don't provide better results, especially when dealing with massive datasets like entire company documentation <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>. Using a [[the_role_of_vector_databases_in_semantic_search_and_data_management | vector database]] for retrieval can achieve similar or better performance with significantly lower costs, even for smaller-scale use cases <a class="yt-timestamp" data-t="00:29:02">[00:29:02]</a>.

## Industry Landscape and Future Trends

The [[the_role_of_vector_databases_in_semantic_search_and_data_management | vector database]] market is experiencing an "explosion of startups" and incumbents adding vector support, as people recognize vectors as a fundamental data type for [[impact_of_ai_advancements_on_business_models | AI]] <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>. However, merely adding vector support to existing databases doesn't make them true [[the_role_of_vector_databases_in_semantic_search_and_data_management | vector databases]] <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>. A genuine [[the_role_of_vector_databases_in_semantic_search_and_data_management | vector database]] uses the numeric array (vector) as the primary lookup and data organization mechanism, leading to highly optimized performance <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.

Regarding the "RAG stack," while OpenAI is a common default for models, smaller, cheaper, and open-source models often provide good performance without significant cost <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>. Partnerships with companies like AnyScale for bulk transformations and data movement, and Cohere and AI21 for models, are common <a class="yt-timestamp" data-t="00:21:37">[00:21:37]</a>. A key missing piece is robust evaluation technology <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.

> [!WARNING] Hardware Sustainability
> The current reliance on GPUs for [[impact_of_ai_advancements_on_business_models | AI]] is unsustainable due to high costs <a class="yt-timestamp" data-t="00:48:03">[00:48:03]</a>. Future shifts in hardware are expected, potentially involving more CPUs, specialized servers optimized for training or serving, and distributed infrastructure <a class="yt-timestamp" data-t="00:48:26">[00:48:26]</a>. Additionally, current data pipeline and management tools are insufficient, and changes are needed to reduce operational headaches, costs, and waiting times <a class="yt-timestamp" data-t="00:49:03">[00:49:03]</a>.

## Strategic Considerations for AI Application Developers

Most companies currently focus on simply getting [[impact_of_ai_advancements_on_business_models | AI applications]] to work <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>. Few have advanced to iterating over specific embedding models, retrieval methods, reranking, and filtering <a class="yt-timestamp" data-t="00:30:14">[00:30:14]</a>. Building a robust [[strategic_considerations_for_ai_application_developers | AI solution]] is not magic; it requires significant effort from scientists and engineers, involving continuous learning, iteration, and customization for each use case <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>.

A common failure mode for potential [[strategic_considerations_for_ai_application_developers | AI application]] builders is incorrect [[cost_efficiency_and_accessibility_in_ai_technologies | cost estimations]] <a class="yt-timestamp" data-t="00:35:02">[00:35:02]</a>. Miscalculating infrastructure costs can prevent companies from even starting projects that would otherwise be feasible <a class="yt-timestamp" data-t="00:36:10">[00:36:10]</a>.

> [!IMPORTANT] Overcoming Inertia
> The most common mode of failure in the [[strategic_considerations_for_ai_application_developers | AI]] field is "doing nothing" <a class="yt-timestamp" data-t="00:55:46">[00:55:46]</a>. Developers are encouraged to focus on building something exciting, and if a [[the_role_of_vector_databases_in_semantic_search_and_data_management | vector database]] like Pinecone becomes necessary, then use it <a class="yt-timestamp" data-t="00:55:27">[00:55:27]</a>.

## The Future of AI and Agents

The [[future_of_ai_in_industrial_applications_and_potential_impact | AI stack]] is still in its early stages, with many early adopters just reaching production <a class="yt-timestamp" data-t="00:39:54">[00:39:54]</a>. Eventually, almost every company is expected to utilize a [[the_role_of_vector_databases_in_semantic_search_and_data_management | vector database]] <a class="yt-timestamp" data-t="00:40:13">[00:40:13]</a>.

There is significant excitement in the [[future_of_ai_in_industrial_applications_and_potential_impact | application and solution space]] for [[impact_of_ai_advancements_on_business_models | AI]], much more so than in the infrastructure layer, which tends towards a "winner take all" phenomenon <a class="yt-timestamp" data-t="00:41:51">[00:41:51]</a>. New companies are emerging to disrupt established players, while incumbents are trying to reassert themselves as [[impact_of_ai_advancements_on_business_models | AI]] natives <a class="yt-timestamp" data-t="00:42:27">[00:42:27]</a>. This creates a "conveyor belt of innovation" from startups to enterprises <a class="yt-timestamp" data-t="00:42:54">[00:42:54]</a>.

One area of particular interest for [[impact_of_ai_on_education_and_unconventional_applications | unconventional applications]] is human communication data (emails, slack, Twitter, meeting transcriptions), where there's a vast amount of knowledge to be extracted <a class="yt-timestamp" data-t="00:43:46">[00:43:46]</a>.

Regarding [[advancements_and_implications_of_ai_agents | AI agents]], it's believed they are already functional, approaching human levels of task completion probability <a class="yt-timestamp" data-t="00:54:02">[00:54:02]</a>. While their mistakes might be "silly" or uncharacteristic for humans, their overall performance is improving <a class="yt-timestamp" data-t="00:54:37">[00:54:37]</a>.

The speaker finds foundational models to be overhyped, as they haven't seen significant qualitative progress for a long time <a class="yt-timestamp" data-t="00:50:54">[00:50:54]</a>. Conversely, coding assistance and code generation are considered exceedingly useful and underhyped [[impact_of_ai_on_education_and_unconventional_applications | applications of AI]] <a class="yt-timestamp" data-t="00:51:14">[00:51:14]</a>.