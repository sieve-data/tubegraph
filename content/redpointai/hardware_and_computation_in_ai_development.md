---
title: Hardware and computation in AI development
videoId: zG-kxc0q_cE
---

From: [[redpointai]] <br/> 

Lyn Chia, co-founder and CEO of Fireworks, a company focused on fast and efficient inference for compound AI systems, highlights the critical role of hardware and computation in the evolving AI landscape. Fireworks aims to deliver the best quality at the lowest latency and cost in the inference stack <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

## The Complexity of AI Inference

Inference is not a simple "single model as a service" operation <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The future of inference involves complex systems with logical reasoning, accessing hundreds of small expert models <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Fireworks envisions a world where they route user queries to the best-performing model for that specific query <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

This complexity arises because models are probabilistic, not deterministic, which is undesirable for factual results <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. Solving complex business problems often requires assembling across multiple models and modalities <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Additionally, single models have limited knowledge based on their finite training data <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. The next barrier in AI is moving beyond single models to [[challenges_and_opportunities_in_ai_model_development_and_infrastructure | compound AI systems]] that combine multiple models across modalities and integrate with APIs, databases, and knowledge bases <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## Hardware Landscape and Optimization

The AI hardware space is experiencing rapid change, with new hardware generations emerging annually instead of every three years <a class="yt-timestamp" data-t="00:29:09">[00:29:09]</a>. There is a scarcity of developers with low-level hardware optimization expertise <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>.

Key considerations in the hardware landscape:
*   **No "One Size Fits All"**: There is no single "best" hardware for every workload pattern, even for the same model <a class="yt-timestamp" data-t="00:29:27">[00:29:27]</a>. Different hardware skills are best for removing specific bottlenecks <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>.
*   **Abstraction**: Fireworks abstracts the burden of integrating and determining the best hardware for a given workload <a class="yt-timestamp" data-t="00:29:53">[00:29:53]</a>. They can even route mixed access patterns to different hardware <a class="yt-timestamp" data-t="00:30:02">[00:30:02]</a>.
*   **Support for Diverse Chips**: Fireworks supports AMD chips for inference, alongside Nvidia <a class="yt-timestamp" data-t="00:28:45">[00:28:45]</a>.
*   **Focus on Product**: Developers should focus on building products, while Fireworks manages the complexity of hardware optimization <a class="yt-timestamp" data-t="00:30:12">[00:30:12]</a>.

## Cost and Efficiency in Inference

The goal of fireworks is to deliver the best quality, lowest latency, and lowest cost in the inference stack <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

*   **Prompt Engineering vs. Fine-tuning**: While prompt engineering is useful for quick testing, long system prompts become difficult to manage and lead to increased cost and slower model performance <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. Fine-tuning can absorb these long prompts into the model itself, resulting in faster, cheaper, and higher-quality results <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.
*   **Pre-training**: Pre-training models is very expensive, requiring significant money and human resources <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. The ROI is much stronger with post-training (fine-tuning) on top of a strong base model <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. While some enterprises do pre-train due to core business reasons, it is often a question of differentiation <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
*   **Compound AI Systems for Cost Optimization**: Fireworks' F1 system, a complex logical reasoning inference system, operates underneath using multiple models and logical steps <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>. This complexity makes overall inference latency and cost a key area of focus <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>.
*   **Hyperscalers vs. Specialized Providers**: Hyperscalers aim to be vertically integrated like Apple, building data centers, acquiring power, and deploying vast machines for large-scale storage and compute <a class="yt-timestamp" data-t="00:31:01">[00:31:01]</a>. Fireworks specializes in solving problems that require a combination of engineering craftsmanship and deep research, deploying scalable inference systems, which cannot be solved by simply throwing more people or money at them <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>.

## On-Device vs. Cloud Inference

Running models locally (on desktop or mobile) is often argued for two main reasons:
1.  **Cost Saving**: Avoiding GPU costs on the cloud <a class="yt-timestamp" data-t="00:33:34">[00:33:34]</a>.
2.  **Privacy**: Keeping data on local disk <a class="yt-timestamp" data-t="00:33:42">[00:33:42]</a>.

However, there are nuances:
*   **Mobile Limitations**: Offloading compute to mobile is different due to limited power, affecting application metrics like cold start time and power consumption, which impact user adoption <a class="yt-timestamp" data-t="00:34:02">[00:34:02]</a>. Models practically deployable on mobile are tiny (1B-10B parameters) with limited capabilities <a class="yt-timestamp" data-t="00:34:33">[00:34:33]</a>.
*   **Privacy Concerns**: Much personal data is already on the cloud, making the privacy argument for local execution less straightforward <a class="yt-timestamp" data-t="00:35:05">[00:35:05]</a>.
*   **Desktop Use Cases**: For many consumer-facing applications, offloading to desktop makes sense <a class="yt-timestamp" data-t="00:34:54">[00:34:54]</a>.

## Future of AI Development and Research

The future of AI lies in hundreds of small expert models <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. This aligns with the open-source community, which provides control and customization opportunities for specialized models through fine-tuning <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

Key areas of focus and excitement:
*   **Agentic Workflows**: The industry is still in the early stages of defining the right user experience and abstraction for [[role_of_ai_in_general_intelligence_and_application_development | agentic workflows]] <a class="yt-timestamp" data-t="00:27:03">[00:27:03]</a>.
*   **F1 System**: Fireworks is building and will generally release F1, a logical reasoning engine that helps understand system abstraction and complexity <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>. This will lead to developer-facing plugins, allowing developers to build their own F1-like systems <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>.
*   **Function Calling**: Function calling, crucial for building agents, involves complex multi-turn chat contexts, selecting from hundreds of tools, and often requires parallel and sequential orchestration <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. This capability ties together different models and tools <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>.
*   **Reasoning Models**: Research into different paths to solve reasoning problems is ongoing <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>. This includes self-inspection techniques like Chain of Thought, as well as new models that can do logical reasoning in latent space, mimicking human thought processes without explicit words <a class="yt-timestamp" data-t="00:25:56">[00:25:56]</a>.
*   **Model-System Co-design**: Optimizing across quality, latency, and cost requires thinking about models and systems together <a class="yt-timestamp" data-t="00:45:32">[00:45:32]</a>.
*   **Disruptive Technologies**: The search for the "next generation of Transformers" that can fundamentally change how models are trained and inference is performed is a significant area of research <a class="yt-timestamp" data-t="00:46:27">[00:46:27]</a>.

## Industry Shifts

The [[evolution_of_ai_models_and_infrastructure | AI industry]] is undergoing a revolution driven by accessibility. Before generative AI, companies needed to hire large machine learning teams to train models from scratch, curate data, and invest significant resources <a class="yt-timestamp" data-t="00:42:27">[00:42:27]</a>. Generative AI changed this by providing foundation models that absorb most knowledge, allowing companies to build on top of them directly or with small fine-tuning efforts, dramatically lowering the barrier to adoption <a class="yt-timestamp" data-t="00:43:12">[00:43:12]</a>. This has led to a much faster adoption curve and shorter sales cycles for AI products <a class="yt-timestamp" data-t="00:51:01">[00:51:01]</a>.

The shift in ROI is moving from pre-training to post-training, and then to inference <a class="yt-timestamp" data-t="00:37:43">[00:37:43]</a>. While pre-training investment will continue until hitting a data wall, there is a clear trend towards optimizing and customizing models for specific uses <a class="yt-timestamp" data-t="00:37:07">[00:37:07]</a>.