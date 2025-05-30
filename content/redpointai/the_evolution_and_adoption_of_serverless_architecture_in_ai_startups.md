---
title: The evolution and adoption of serverless architecture in AI startups
videoId: 1gLHnRDiIms
---

From: [[redpointai]] <br/> 

Pinecone, a vector database, has raised over $130 million, recently achieving a $750 million valuation. It has become a fundamental tool for building AI applications <a class="yt-timestamp" data-t="00:00:03">[00:00:11]</a>.

## Early Challenges and Market Education

Before the generative AI "craze" and the launch of ChatGPT, vector databases were vastly underutilized for many use cases like semantic search, candidate generation, ranking, and recommendation <a class="yt-timestamp" data-t="00:00:54">[00:01:10]</a>. While larger companies like Google and Amazon used this technology internally, educating the broader market was challenging <a class="yt-timestamp" data-t="00:01:16">[00:01:29]</a>. Investors were often confused when the founder, who previously helped build Amazon SageMaker (an MLOps product), spoke about building a vector database, frequently mistaking it for an MLOps solution <a class="yt-timestamp" data-t="00:01:54">[00:02:20]</a>.

## The "ChatGPT Effect" and Rapid Scaling

The launch of ChatGPT and OpenAI's broader efforts significantly elevated the discussion around AI to a wider audience <a class="yt-timestamp" data-t="00:02:23">[00:02:30]</a>. While the underlying technology for practitioners didn't change drastically, there was a massive influx of capital and energy, making it accessible to non-AI engineers <a class="yt-timestamp" data-t="00:02:32">[00:02:49]</a>.

This led to an "insane" surge in demand for Pinecone:
*   The company started rapidly ramping up, exhausting machines in GCP and AWS clouds <a class="yt-timestamp" data-t="00:02:53">[00:03:04]</a>.
*   They were spending millions of dollars a month on their free tier <a class="yt-timestamp" data-t="00:03:05">[00:03:07]</a>.
*   At peak, they experienced 10,000 signups daily <a class="yt-timestamp" data-t="00:03:20">[00:03:23]</a>.

A particular moment that dramatically spiked usage was the emergence of an open-source tool called AutoGPT <a class="yt-timestamp" data-t="00:05:06">[00:05:18]</a>. This minimalist, agent-like gadget, often just a single Python file, "took off like crazy" <a class="yt-timestamp" data-t="00:05:33">[00:05:51]</a>. The shift in user base was notable: instead of systems engineers building AI platforms, Pinecone was being onboarded by individuals like "the dentist that remembers Python from college and wants to play with AI" <a class="yt-timestamp" data-t="00:05:57">[00:06:13]</a>.

## The Transition to Serverless Architecture

The overwhelming demand forced Pinecone to rethink [[Scaling and Innovation in AI Infrastructures | scale]] and efficiency in a completely different way <a class="yt-timestamp" data-t="00:03:26">[00:03:30]</a>. They had to go back to the drawing board and redesign their entire solution, resulting in their current serverless architecture <a class="yt-timestamp" data-t="00:03:32">[00:03:42]</a>. This new architecture is two orders of magnitude more efficient and was born out of sheer necessity, as they literally couldn't handle the load <a class="yt-timestamp" data-t="00:03:42">[00:03:51]</a>.

The serverless model significantly reduces costs for customers. For a company with millions of vectors, the cost might be as low as $100 per month <a class="yt-timestamp" data-t="00:07:07">[00:07:08]</a>. Pinecone truly shines at the hundreds of millions to billions scale, where companies (often SaaS providers themselves like Notion or Gong) develop deep AI solutions for their own customers' data <a class="yt-timestamp" data-t="00:07:17">[00:07:41]</a>. These customers might have millions of documents each, and with 10,000 customers, they need a vector database that can handle 10 billion embeddings across thousands of partitions cost-effectively <a class="yt-timestamp" data-t="00:07:44">[00:08:02]</a>.

> "Because of our new architecture, because we went through this insane spike a year and a half ago and we've re architected everything and now we've launched it as serverless, we can run this multi-tenant workload such that one of you your cost for one of your paying customers on Pine Cone might be a dollar a year like like sometimes 50 cents a year right for a paying user right and then the unit economics really shine." <a class="yt-timestamp" data-t="00:08:23">[00:08:50]</a>

## Business Implications and Strategic Decisions

The transition to a serverless model was "very painful" for Pinecone as a company <a class="yt-timestamp" data-t="00:37:29">[00:37:31]</a>. It's a "hard transition" for founders, as investors might see revenue flatten out even as workloads grow faster, due to the product being significantly cheaper <a class="yt-timestamp" data-t="00:37:35">[00:38:03]</a>. The CEO advises founders to make such transitions earlier rather than later, taking the hit as soon as possible <a class="yt-timestamp" data-t="00:38:25">[00:38:37]</a>.

Pinecone estimates they are "leaving on the table more than half of our revenue" <a class="yt-timestamp" data-t="00:38:42">[00:38:45]</a>. For some customers, especially in storage-heavy industries like Pharma, the cost reduction could be 70%, 80%, or even 90% <a class="yt-timestamp" data-t="00:38:50">[00:39:07]</a>. Some companies that used to pay $100,000 now pay only $2,000 a month/year <a class="yt-timestamp" data-t="00:39:09">[00:39:13]</a>. While investors may not be happy, it is considered the right thing for the customer and for building solutions on the platform <a class="yt-timestamp" data-t="00:39:25">[00:39:40]</a>.

[!NOTE|Early Stage of AI Adoption]
The AI stack is in its very early stages, with mostly trailblazers and early adopters in production <a class="yt-timestamp" data-t="00:39:54">[00:40:11]</a>. The expectation is that almost every company will eventually utilize a vector database <a class="yt-timestamp" data-t="00:40:13">[00:40:19]</a>. To fit "snugly" into the cost structure for tens or hundreds of thousands of different workloads, cost-effectiveness is paramount, even if it means short-term pain <a class="yt-timestamp" data-t="00:40:25">[00:40:38]</a>.

## [[Enterprise AI adoption challenges | Challenges in AI Adoption for Enterprises]]

One of the biggest [[Enterprise AI adoption and deployment models | barriers to enterprise AI adoption]] is hallucination in models, leading to a lack of trustworthiness <a class="yt-timestamp" data-t="00:13:04">[00:13:09]</a>. Models are designed to generate language, and when compelled to write on unfamiliar topics, they will produce text that "contains stuff" <a class="yt-timestamp" data-t="00:13:13">[00:13:30]</a>. This is a significant problem that needs societal and technological solutions <a class="yt-timestamp" data-t="00:13:55">[00:14:03]</a>.

Solutions involve:
*   **Measuring Hallucinations:** The ability to accurately measure hallucinations, usefulness, correctness, and faithfulness to data is still a complex challenge <a class="yt-timestamp" data-t="00:15:20">[00:16:21]</a>.
*   **Retrieval Augmented Generation (RAG):** Using vector databases and knowledge layers helps make data available to models in a secure, governed, and manageable way (e.g., for data deletion requirements like GDPR) <a class="yt-timestamp" data-t="00:16:28">[00:17:13]</a>. Even today, running a language model with unsophisticated RAG can outperform large models like GPT-4 <a class="yt-timestamp" data-t="00:17:40">[00:17:59]</a>.

Most companies are still focused on making basic AI implementations work <a class="yt-timestamp" data-t="00:30:01">[00:30:04]</a>. Only a few have enough experience to iterate on embedding models, retrieval, re-ranking, and filtering <a class="yt-timestamp" data-t="00:30:09">[00:30:22]</a>. Building a complete AI solution for specific use cases (like Q&A or chat support) requires significant work from scientists and engineers over multiple quarters, involving learning, iteration, and customization for different preferences in speed, cost, accuracy, and data freshness <a class="yt-timestamp" data-t="00:31:00">[00:31:53]</a>.

A common [[challenges_in_ai_adoption_for_startups | failure mode]] for companies attempting to build AI solutions is incorrect cost estimations. People often significantly overestimate the cost of using vector databases like Pinecone, leading them to abandon projects that would otherwise be viable <a class="yt-timestamp" data-t="00:35:02">[00:36:26]</a>.

## [[Trends and challenges in AI infrastructure | Trends in AI Infrastructure]] and Applications

While "storing vectors" is a common understanding, the uniqueness of vector databases lies in how the numeric array becomes the primary key for organizing and searching data, reflecting how the human brain processes information <a class="yt-timestamp" data-t="00:19:53">[00:20:18]</a>. Bolting on vector support to traditional databases (like "Bongo" - a likely reference to Mongo) results in poor performance <a class="yt-timestamp" data-t="00:20:23">[00:20:33]</a>.

There is a market dynamic pushing towards more efficient and cost-effective AI solutions:
*   **Smaller Models:** There is no reason to spend a ton of money on large models; smaller, cheaper, and easier-to-manage open-source models often provide good performance <a class="yt-timestamp" data-t="00:21:11">[00:21:20]</a>.
*   **Economic Trade-offs:** The market will find a stable point with a good trade-off between cost, compute, infrastructure, and output quality <a class="yt-timestamp" data-t="00:25:17">[00:25:31]</a>. Making models bigger on GPUs is often not reasonable or sustainable in the long term due to cost and environmental impact <a class="yt-timestamp" data-t="00:25:37">[00:26:07]</a>. Smaller models, when used correctly, can yield comparable or better results at cents on the dollar <a class="yt-timestamp" data-t="00:26:13">[00:26:30]</a>.
*   **Context Window Limitations:** While larger context windows are available (a pricing model incentive from LLM providers), sending all company data on every query is clearly not the right approach due to cost, slowness, and often limited benefit <a class="yt-timestamp" data-t="00:27:09">[00:28:15]</a>. Even for small cases, using a vector database to retrieve only relevant documents (e.g., sending 3,000-10,000 tokens instead of 100,000) can lead to 90% cost savings without performance loss <a class="yt-timestamp" data-t="00:29:01">[00:29:16]</a>.

### Future Outlook for [[Building and scaling AI infrastructure companies | AI Infrastructure]]

The future of [[trends_in_ai_model_training_and_deployment | AI model training and deployment]] will see significant shifts:
*   **Hardware:** The current GPU-centric model is not sustainable. There will be changes in hardware, potentially involving more CPUs, specialized servers optimized for training or serving, and distributed infrastructure <a class="yt-timestamp" data-t="00:47:56">[00:48:45]</a>.
*   **Data Pipelines:** Current data pipeline and management tools are insufficient, leading to operational headaches, high costs, and slow processing <a class="yt-timestamp" data-t="00:49:01">[00:49:27]</a>.
*   **Moderating Systems:** There will be a need for moderating systems that offer governance, visibility, and control over the AI stack, which currently often runs open-loop for most companies <a class="yt-timestamp" data-t="00:49:34">[00:49:58]</a>.

While there is a "win or take all" phenomenon in [[building_and_scaling_ai_infrastructure_companies | AI infrastructure]], limiting the space for new companies <a class="yt-timestamp" data-t="00:41:31">[00:41:51]</a>, the application and solution layer offers immense opportunities <a class="yt-timestamp" data-t="00:41:51">[00:42:04]</a>. This layer is a "conveyor belt of innovation," with numerous new applications emerging weekly <a class="yt-timestamp" data-t="00:42:54">[00:43:27]</a>.

For [[building_ai_startups_and_the_challenges_of_scaling | AI startups]], the CEO finds coding assistance to be an "exceedingly useful" and exciting use case <a class="yt-timestamp" data-t="00:51:14">[00:51:24]</a>. Looking ahead, he is particularly excited about low-level challenges such as high-performance optimization and compiling for AI models, as the current integrated execution and training software stack is "insane" <a class="yt-timestamp" data-t="00:53:31">[00:53:57]</a>. He believes that agents are already functional to a decent extent, performing tasks with a probability close to human levels, although their mistakes can be "more embarrassing" <a class="yt-timestamp" data-t="00:54:02">[00:54:49]</a>.

[!INFO|Recommendation for Builders]
For those looking to get started, the CEO advises focusing on building something exciting. If that endeavor leads to needing a vector database, then great; if not, you've still built something valuable. The most common mode of failure is "doing nothing" <a class="yt-timestamp" data-t="00:55:27">[00:55:49]</a>.