---
title: Future trends in AI hardware and software
videoId: 1gLHnRDiIms
---

From: [[redpointai]] <br/> 

## AI Infrastructure and Opportunities

The AI ecosystem is still in its very early stages of adoption, with "Trailblazers just getting to production" <a class="yt-timestamp" data-t="00:40:09">[00:40:09]</a>. There is significant innovation happening across the stack, from tiny startups to large enterprises <a class="yt-timestamp" data-t="00:52:56">[00:52:56]</a>.

### Evolution of Vector Databases
Pinecone, a vector database, has become a core tool for building AI applications <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Initially, vector databases were vastly underutilized, a "well-known secret" used internally by large companies like Google and Amazon for tasks such as semantic search, recommendation, feed ranking, and anomaly detection <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Educating the market about their utility was challenging <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

The launch of ChatGPT by OpenAI elevated the discussion of AI to a broader audience, leading to a massive increase in demand for tools like Pinecone <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This surge, including periods of up to 10,000 signups per day, pushed Pinecone to rethink scale and efficiency, leading to a complete redesign and the introduction of a "serverless" solution that is two orders of magnitude more efficient <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

### The Vector Database Landscape
While many incumbents are adding support for vectors as a data type, true vector databases are unique because the numeric array itself becomes the conceptual key for data organization and retrieval <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>. Attempting to "bolt on" this data type to traditional databases can lead to incredibly poor performance <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>.

Pinecone excels at handling massive scales, from hundreds of millions to billions of embeddings across thousands of partitions, cost-effectively <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. This enables SaaS providers to offer deep AI solutions to their customers, where each customer might have millions of documents, but the provider itself manages billions of embeddings <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

### Applications of AI and Vector Databases
Common applications built on vector databases include:
*   Q&A and semantic search (e.g., Notion, Gong) <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>
*   Chatbots and support bots <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>
*   Legal and medical history discovery <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>
*   Anomaly detection and security <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>
*   Pharma and Drug Discovery <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>
The core "meat and potato" applications remain text and images, primarily for search and Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

## Challenges and Opportunities in AI Development

### Overcoming Hallucinations
One of the biggest barriers for enterprises building effective AI applications is hallucinations – the lack of trustworthiness in LLM outputs <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. LLMs are designed to generate language, which can lead to made-up information if they don't have relevant knowledge <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.

Solutions to combat hallucinations include:
*   **Measuring Hallucinations**: Efforts are underway to accurately measure usefulness, correctness, and faithfulness of model outputs to the data <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.
*   **Retrieval Augmented Generation (RAG)**: This approach, leveraging vector databases and knowledge layers, makes enterprise data securely and governably available to models, significantly reducing hallucinations <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>. RAG, based on semantic search, is seen as the "magic sauce" for improved performance <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

### The RAG Stack
For building RAG products, companies are increasingly defaulting to smaller, cheaper, and easier-to-manage open-source models, rather than exclusively relying on larger models like OpenAI's <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>. Key components of the RAG stack include:
*   **Data Transformation and Movement**: Tools like AnyScale are used for bulk transformations and data movement <a class="yt-timestamp" data-t="00:21:30">[00:21:30]</a>.
*   **Model Providers**: Coher, AI21, and Hugging Face are prominent model providers for embedding, ranking, and summarization <a class="yt-timestamp" data-t="00:21:59">[00:21:59]</a>.
*   **Data Preparation**: Companies like Unstructured and those integrating with tools like Fivetran help in generating embeddings and getting data into vector databases <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>.
*   **Evaluation Technology**: A significant gap remains in finding a strong, leading technology for evaluating AI outputs <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.

### Cost and Performance Optimization
The market is seeking a stable point that balances cost, compute, and infrastructure with output quality <a class="yt-timestamp" data-t="00:25:17">[00:25:17]</a>. Running large models (e.g., 100 billion parameters) for every API call is not economically sustainable <a class="yt-timestamp" data-t="00:25:53">[00:25:53]</a>.

While context windows for LLMs are expanding, using them to stuff all relevant data is expensive (charging per token) and often doesn't lead to better results <a class="yt-timestamp" data-t="00:26:51">[00:26:51]</a>. Storing documents in a vector database and sending only the most relevant, retrieved information to the LLM can lead to significantly lower costs (e.g., 10% of the cost) without a noticeable loss in performance <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>.

Many companies are in an "exploration mode," simply trying to get AI solutions to work <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>. Building a robust AI application involves significant work, requiring scientists and engineers to iterate and improve over multiple quarters <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>. Each use case and application has unique preferences for speed, cost, accuracy, and data freshness <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>.

A common failure mode for companies is incorrectly estimating the costs of AI infrastructure, leading them to abandon projects that would otherwise be viable <a class="yt-timestamp" data-t="00:35:02">[00:35:02]</a>.

## [[hardware_and_computation_in_ai_development | Hardware and Computation in AI Development]]
A significant shift in AI hardware is anticipated <a class="yt-timestamp" data-t="00:47:56">[00:47:56]</a>. The current reliance on GPUs is seen as unsustainable in the long term, suggesting a move towards a mix of CPUs, GPUs, and specialized servers optimized for training or serving models <a class="yt-timestamp" data-t="00:48:03">[00:48:03]</a>.

Existing data pipeline and management tools from 5-10 years ago are no longer sufficient for modern AI demands due to operational overhead, high costs, and slow processing times <a class="yt-timestamp" data-t="00:49:03">[00:49:03]</a>.

## [[future_of_software_development_and_ai | Future of Software Development and AI]] and AI Agents
Fundamental models, while impactful, are viewed as potentially overhyped, with no significant qualitative progress seen recently <a class="yt-timestamp" data-t="00:50:54">[00:50:54]</a>. However, [[future_of_coding_and_ai_integration | code generation]] and coding assistance are considered exceedingly useful and an incredibly exciting application of AI <a class="yt-timestamp" data-t="00:51:11">[00:51:11]</a>.

Regarding [[future_of_ai_agents_in_software_development | AI agents]], it's suggested that they already "work" to a decent extent, reaching human-level probability of task completion, although their mistakes can be "silly" and more embarrassing than human errors <a class="yt-timestamp" data-t="00:54:02">[00:54:02]</a>.

The field is teeming with innovative applications, where companies are finding unique ways to solve problems using AI <a class="yt-timestamp" data-t="00:43:06">[00:43:06]</a>. A particular area of interest is human communication (emails, Slack, Twitter, meeting transcriptions), as it holds vast amounts of extractable knowledge <a class="yt-timestamp" data-t="00:43:46">[00:43:46]</a>.