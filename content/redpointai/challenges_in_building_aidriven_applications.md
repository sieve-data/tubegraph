---
title: Challenges in building AIdriven applications
videoId: 1gLHnRDiIms
---

From: [[redpointai]] <br/> 

Building effective AI applications presents numerous challenges, particularly for enterprises and those new to the field. These [[challenges_in_ai_product_development | challenges]] span from initial market education and infrastructure scaling to model trustworthiness and cost management <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Evolution of Vector Databases

Initially, vector databases were vastly underutilized, despite being a "well-known secret" used internally by large companies like Google and Amazon for tasks such as semantic search, recommendation, and anomaly detection <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Educating the broader market about their utility was difficult <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, with many investors and professionals confusing them with ML Ops products <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

The launch of ChatGPT and the broader generative AI craze significantly elevated public awareness, making the technology accessible to a wider audience, including non-AI engineers <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This led to an unprecedented surge in demand for vector databases, with Pinecone experiencing up to 10,000 signups daily at its peak <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This rapid growth exposed significant scaling challenges, including exhausting cloud machine resources and spending millions monthly on free tiers <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. The necessity to keep up with demand forced a complete redesign of Pinecone's architecture, resulting in a serverless solution that is two orders of magnitude more efficient <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## Core [[challenges_in_ai_adoption_and_deployment | Challenges in AI Adoption]] and Deployment

Despite technological advancements, the average company still finds it difficult to train even simple deep learning models <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. The gap between cutting-edge research and practical enterprise adoption can be five years apart <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

### Model Trustworthiness: The Hallucination Problem
One of the biggest [[challenges_in_deploying_ai_models_effectively | challenges in deploying AI models effectively]] is dealing with hallucinations, where models generate factually incorrect or nonsensical information <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. Large language models are designed to generate language, and when compelled to produce text on unfamiliar topics, they will do so, even if it contains fabrications <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

Addressing hallucinations is complex because merely preventing them by having the model say "I don't know" can render it useless <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>. The focus must be on measuring usefulness, correctness, and faithfulness to the underlying data <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>. Retrieval Augmented Generation (RAG) and vector databases are crucial in providing models with accurate, governed data to reduce hallucinations <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>. This also involves ensuring data security, governance (e.g., GDPR compliance for data deletion), and visibility into the data provided to the model <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.

### Cost Management
Miscalculating the costs of AI infrastructure is a common [[challenges_in_aidriven_transcription_and_summarization | failure mode]] that prevents companies from even starting AI projects <a class="yt-timestamp" data-t="00:35:02">[00:35:02]</a>. Many overestimate costs, believing a solution will be prohibitively expensive when in reality it might be far more affordable <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>. For example, a monthly cost estimated at $50,000 might actually be $500 <a class="yt-timestamp" data-t="00:35:12">[00:35:12]</a>.

Pinecone's transition to a serverless model, born out of necessity to handle demand, significantly reduced costs for customers, sometimes by 70-90% <a class="yt-timestamp" data-t="00:38:42">[00:38:42]</a>. While painful for the company's short-term revenue, this move was deemed essential for fitting into customers' product cost structures and promoting broader adoption, as many companies will eventually use vector databases for various workloads <a class="yt-timestamp" data-t="00:39:31">[00:39:31]</a>.

### Integration and Optimization
The current state of AI adoption sees most companies primarily focused on getting their AI solutions to work <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>. Few have gained enough experience to iterate on advanced aspects like embedding models, retrieval, reranking, or filtering <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>. Building a complete AI solution, including Q&A and chat support, requires significant time, effort, and iteration from scientists and engineers <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>. Each use case has unique preferences for speed, cost, accuracy, and data freshness <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>.

Companies like Pinecone emphasize empowering developers to build and tweak AI applications themselves, rather than acting as a professional services team <a class="yt-timestamp" data-t="00:32:10">[00:32:10]</a>. This strategy enables thousands of customers to use the product successfully without direct intervention <a class="yt-timestamp" data-t="00:33:41">[00:33:41]</a>.

## Future Outlook and [[Challenges in AI Product Development | Opportunities in AI Development]]
The AI landscape is rapidly evolving. Significant shifts are expected in hardware, with current GPU reliance considered unsustainable in the long term, potentially leading to more CPU workloads or specialized servers <a class="yt-timestamp" data-t="00:47:56">[00:47:56]</a>. Existing data pipeline and management tools are also proving inadequate for the scale and demands of AI, necessitating new solutions <a class="yt-timestamp" data-t="00:49:03">[00:49:03]</a>.

Furthermore, there is a need for robust moderating systems that provide governance and visibility into AI stacks, which currently often run in an open-loop fashion for most companies <a class="yt-timestamp" data-t="00:49:34">[00:49:34]</a>.

While infrastructure development continues, the most exciting opportunities lie in the application and solution layers <a class="yt-timestamp" data-t="00:41:15">[00:41:15]</a>. The market is "teaming with innovation," with new companies constantly emerging to solve problems in creative ways with AI <a class="yt-timestamp" data-t="00:42:54">[00:42:54]</a>. Examples include AI Q&A, semantic search for customer data, and applications in legal discovery, medical history, anomaly detection, security, and drug discovery <a class="yt-timestamp" data-t="00:37:33">[00:37:33]</a>. Multimodal AI applications are also emerging, though mainstream adoption may still be a few years away <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

A key takeaway for builders is to focus on practical application: "Don't try to learn about Pinecone, try to go build something exciting" <a class="yt-timestamp" data-t="00:55:27">[00:55:27]</a>. The most common [[challenges_of_building_ai_infrastructure_companies | mode of failure]] is doing nothing <a class="yt-timestamp" data-t="00:55:46">[00:55:46]</a>.