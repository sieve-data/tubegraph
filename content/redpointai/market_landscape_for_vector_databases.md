---
title: Market landscape for vector databases
videoId: 1gLHnRDiIms
---

From: [[redpointai]] <br/> 

Pinecone, a vector database, has raised over $130 million, recently at a $750 million valuation <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It has become a core tool for building [[AI infrastructure and vector databases | AI apps]] <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Evolution of the Vector Database Landscape

Before the generative [[AI infrastructure and vector databases | AI]] craze and the launch of ChatGPT, vector databases were largely underutilized <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. They have diverse use cases including semantic search, candidate generation, ranking, feed ranking, and recommendation <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Larger companies like Google and Amazon internally used vector databases for search, recommendation, feed ranking, and anomaly detection <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. However, educating the broader market about this technology was challenging <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Investors were often confused when presented with the concept of a "vector database" <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

The launch of ChatGPT significantly elevated the discussion about vector databases to a broader audience <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. While the underlying technology for practitioners didn't change dramatically, the increased capital and energy led to its adoption by non-[[AI infrastructure and vector databases | AI]] engineers <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### The AutoGPT Effect
A significant moment that spiked usage was the emergence of AutoGPT, an open-source "agent" gadget <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. This tool, though minimalistic, took off "like crazy" <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. Suddenly, Pinecone's onboarding users were not just systems engineers building [[enterprise_ai_deployment_models | AI platforms]] or RAG (Retrieval Augmented Generation) applications, but also individuals like dentists who remembered Python from college <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. This surge led to immense scaling challenges, with Pinecone experiencing up to 10,000 signups daily <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This forced a redesign of their solution, resulting in a serverless architecture that is two orders of magnitude more efficient <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## Applications and Scale
Today, a "million vectors" is considered a small scale <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Pinecone truly shines at handling hundreds of millions to billions of vectors <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. This scale is crucial for SaaS companies and software providers like Notion and Gong, who develop deep [[AI infrastructure and vector databases | AI solutions]] (e.g., [[understanding_the_market_for_aipowered_solutions | AI Q&A]], semantic search) for their customers' data <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. For instance, a provider with 10,000 customers, each with a million documents, would need a vector database to handle 10 billion embeddings across thousands of partitions <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

The focus is now on unit economics for true product building, not just lab experimentation <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. Pinecone's serverless architecture allows for multi-tenant workloads, reducing the cost per paying customer to potentially a dollar or even 50 cents per year <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

Common applications running on Pinecone include:
*   Q&A and semantic search <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>
*   Chatbots and support bots <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>
*   [[AI applications in the legal industry | Legal discovery]] and medical history discovery <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>
*   Analytics <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
*   Applications involving images, audio, and [[AI video tools in enterprises | video]] <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>
*   Anomaly detection and security <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>
*   Pharma and drug discovery <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>

RAG (Retrieval Augmented Generation) applications are largely based on semantic search, where the "magic sauce" happens at the semantic search layer <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

### Challenges in Enterprise Adoption
Despite rapid advancements, the average company still struggles to train even simple deep learning models <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. A major barrier for effective [[enterprise_ai_deployment_models | AI app deployment]] is the issue of "hallucinations" in Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. LLMs are designed to generate language, and when compelled to write on topics they "know nothing about," they will produce text that may contain inaccuracies <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.

### Addressing Hallucinations
Solutions are emerging to measure and mitigate hallucinations <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>. Key efforts include:
*   **Measurement**: Developing metrics to assess usefulness, correctness, and faithfulness to data <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
*   **Knowledge Layers**: Using RAG and vector databases to make data securely available to models, ensuring data governance and compliance (e.g., GDPR deletion requirements) <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>. This community has made significant progress in providing robust solutions <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
*   **Outperforming GPT-4**: Experiments have shown that loading a good chunk of the internet into Pinecone and running a language model with unsophisticated RAG can already outperform GPT-4 <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>.

## Competitive Landscape
"Vectors are the language of [[AI infrastructure and vector databases | AI]]" <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>. This realization has led to a "land grab" where many startups and incumbents are vying to store vectors <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>. Incumbent database providers are adding support for vector data types, seeing vectors as another data type like sentences or images <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.

However, simply storing a float array (vector) doesn't make a database a true vector database <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>. What makes vector databases unique is that the numeric array acts as the primary lookup key, organizing data on storage and enabling efficient searching <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>. Attempting to "bolt on" this data type to a traditional database often results in poor performance and serious issues <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.

### The RAG Stack
For building a RAG product, common components include:
*   **Models**: Smaller, cheaper, and sometimes open-source models often perform well for embedding and summarization <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.
*   **Data Transformation**: Tools like AnyScale's product are used for bulk transformations and data movement <a class="yt-timestamp" data-t="00:21:30">[00:21:30]</a>.
*   **Application Launch**: Collaborations with companies like Forel and others for building the application layer <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.
*   **Partnerships**: Close work with Cohere, AI21, and Hugging Face for models <a class="yt-timestamp" data-t="00:21:59">[00:21:59]</a>.
*   **Data Prep**: Companies like Unstructured focus on generating embeddings and preparing data for vector databases, especially for standardized data channels (e.g., importing data from Snowflake via Fivetran) <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>.

### Cost Optimization and Context Windows
The market is driven by finding a stable point between cost, compute, infrastructure, and output quality <a class="yt-timestamp" data-t="00:25:17">[00:25:17]</a>. Running massive models (e.g., 100 billion parameters) for every API call is not sustainable due to cost and environmental impact <a class="yt-timestamp" data-t="00:25:53">[00:25:53]</a>.

While model companies are expanding context windows, it often doesn't help more often than not <a class="yt-timestamp" data-t="00:27:09">[00:27:09]</a>. Sending all company data to an LLM on every query is clearly not the right approach <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>. Even for smaller cases where context windows are theoretically workable, using a vector database for retrieval (e.g., sending 3,000-10,000 tokens instead of 100,000) can achieve similar or better results at a tenth of the cost <a class="yt-timestamp" data-t="00:29:02">[00:29:02]</a>.

### Vendor Approach and Customer Education
Pinecone adopted a strategy of either fully handling a feature (e.g., automated infrastructure) or explicitly not doing it, clearly documenting their scope <a class="yt-timestamp" data-t="00:33:09">[00:33:09]</a>. This approach fostered customer independence, leading to thousands of successful customers who don't require direct support <a class="yt-timestamp" data-t="00:33:43">[00:33:43]</a>. However, Pinecone now offers consultation for customers who need help, though not full Professional Services <a class="yt-timestamp" data-t="00:34:40">[00:34:40]</a>.

A common failure mode for potential users is incorrect cost estimations <a class="yt-timestamp" data-t="00:35:02">[00:35:02]</a>. Companies might incorrectly estimate costs to be exorbitant (e.g., $50,000/month) when the actual cost could be significantly lower (e.g., $500/month) <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>. This miscalculation can prevent them from even starting a project <a class="yt-timestamp" data-t="00:36:13">[00:36:13]</a>.

The transition to a serverless model, while painful for the company's short-term revenue, is seen as the right thing for the customer and the platform's future <a class="yt-timestamp" data-t="00:37:29">[00:37:29]</a>. This shift can lead to significant cost reductions for customers (e.g., 50-90% reduction) <a class="yt-timestamp" data-t="00:38:45">[00:38:45]</a>. By fitting snugly into customers' cost structures, Pinecone aims to be a fundamental part of the future [[AI infrastructure and vector databases | AI stack]] as more companies adopt vector databases <a class="yt-timestamp" data-t="00:39:38">[00:39:38]</a>.

## Future Outlook for [[AI infrastructure and vector databases | AI Infrastructure]]
The current [[AI infrastructure and vector databases | AI infrastructure]] landscape is still in its very early stages <a class="yt-timestamp" data-t="00:40:47">[00:40:47]</a>.

### Hardware Shifts
There will be a significant shift in the types of hardware used for [[AI infrastructure and vector databases | AI]] <a class="yt-timestamp" data-t="00:47:56">[00:47:56]</a>. The current reliance on GPUs is not sustainable long-term <a class="yt-timestamp" data-t="00:48:03">[00:48:03]</a>. The future will likely involve a mix of CPUs, GPUs, and specialized servers optimized for training or serving, potentially with distributed infrastructure <a class="yt-timestamp" data-t="00:48:36">[00:48:36]</a>.

### Data Management
Existing data pipeline and data management tools from 5-10 years ago are no longer sufficient <a class="yt-timestamp" data-t="00:49:03">[00:49:03]</a>. Operational headaches, costs, and wait times are unreasonable, necessitating changes <a class="yt-timestamp" data-t="00:49:17">[00:49:17]</a>.

### Moderation and Governance
Future [[AI infrastructure and vector databases | AI stacks]] will require moderating systems to provide governance, visibility, and control, even when models are not self-owned <a class="yt-timestamp" data-t="00:49:34">[00:49:34]</a>.

### Application Layer Opportunities
While infrastructure has a "winner take all" phenomenon, the application and solution space offers immense energy, excitement, and opportunities for new companies to solve problems in creative ways <a class="yt-timestamp" data-t="00:41:51">[00:41:51]</a>. This includes startups challenging long-term players and enterprises learning to adopt these new technologies <a class="yt-timestamp" data-t="00:42:27">[00:42:27]</a>.

## Overhyped vs. Underhyped
*   **Overhyped**: Foundational models <a class="yt-timestamp" data-t="00:50:54">[00:50:54]</a>. The speaker believes their capabilities are well-understood, and there hasn't been significant qualitative progress recently <a class="yt-timestamp" data-t="00:50:58">[00:50:58]</a>.
*   **Underhyped**: [[AI coding tools and market dynamics | Code generation]] and coding assistance <a class="yt-timestamp" data-t="00:51:14">[00:51:14]</a>. This is considered one of the most exciting and useful applications of the technology <a class="yt-timestamp" data-t="00:51:21">[00:51:21]</a>.

### Agents
The speaker believes [[understanding_the_market_for_aipowered_solutions | AI agents]] "already work" <a class="yt-timestamp" data-t="00:54:02">[00:54:02]</a>, suggesting that the bar for reliability should be comparable to human assistants <a class="yt-timestamp" data-t="00:54:15">[00:54:15]</a>. While their mistakes can be "silly" (non-human-like), the probability of completing tasks is nearing human levels <a class="yt-timestamp" data-t="00:54:41">[00:54:41]</a>.