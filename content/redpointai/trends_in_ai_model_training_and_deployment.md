---
title: Trends in AI model training and deployment
videoId: zG-kxc0q_cE
---

From: [[redpointai]] <br/> 

Lyn Chia, co-founder and CEO of Fireworks, discusses the evolving landscape of AI model training and deployment, highlighting the shift towards complex, compound AI systems and the challenges and opportunities within the industry.

## Fireworks' Core Vision: Compound AI Systems

Fireworks, a generative AI platform with a focus on inference, aims to deliver the best quality, lowest latency, and lowest cost inference solutions <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. The company envisions future inference systems as complex networks involving logical reasoning and access to hundreds of small expert models <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. This approach moves beyond simple "model as a service" API calls, addressing the limitations of single models <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>.

## [[Challenges in AI model training and deployment|Challenges in AI Model Deployment]]

Current models face limitations because they are probabilistic, making it difficult to deliver consistently factual results to end-users <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>. Complex business problems often require assembling multiple models across various modalities (e.g., audio, visual, text) to achieve solutions <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. Even within the same modality, like large language models (LLMs), different expert models specialize in tasks such as classification, summarization, or tool calling <a class="yt-timestamp" data-t="03:23:00">[03:23:00]</a>. Furthermore, single models have limited knowledge, constrained by their finite training data <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>, with much real-world information residing behind public or proprietary APIs <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.

The solution, according to Fireworks, is the "compound AI system," which integrates multiple models across different modalities with various APIs, databases, storage systems, and knowledge bases to deliver optimal AI results <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.

### Approaches to Building AI Systems: Imperative vs. Declarative

When building these complex systems, two design philosophies emerge:
*   **Imperative**: Developers have full control over the workflow, inputs, and outputs, making the system deterministic <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.
*   **Declarative**: Developers define "what" problem the system should solve, allowing the system to figure out "how" to achieve it <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>. An example is SQL, where users define the desired data, and the database system determines the most efficient execution plan <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a>.

Fireworks leans towards a more declarative system with full debuggability and maintainability, aiming to deliver the simplest user experience by hiding complex details <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>.

## [[Challenges and advancements in AI model development|Evolution of AI Model Development and Customization]]

Fireworks started by offering the lowest level of abstraction: single models as a service, including hundreds of models across various modalities like LLMs, audio, vision, and embedding models <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>. However, developers faced significant challenges in assembling these pieces and controlling quality due to the constant release of new models <a class="yt-timestamp" data-t="07:24:00">[07:24:00]</a>. This highlighted a usability gap, especially for enterprises <a class="yt-timestamp" data-t="07:56:00">[07:56:00]</a>.

### The "No One Model Fits All" Observation

There is no single AI model that fits all problems <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>. Model training is an iterative process where resources are heavily dedicated to specific problems, leading to models that excel in certain areas but perform poorly in others <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>. Lyn Chia believes the future lies in "hundreds of small expert models" that can thrive in narrower problem spaces by pushing quality <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>. This trend is beneficial for the open-source community, allowing for greater customization and specialized model development through post-training or fine-tuning <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>.

### Prompt Engineering vs. Fine-tuning vs. Pre-training

*   **Prompt Engineering**: Many enterprises start with prompt engineering due to its immediate results and responsiveness, allowing quick testing of a model's steerability <a class="yt-timestamp" data-t="10:55:00">[10:55:00]</a>. However, managing thousands of lines of system prompts becomes a complex problem <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>.
*   **Fine-tuning**: When prompt engineering becomes unwieldy, fine-tuning is the next step to absorb long system prompts into the model itself <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>. This makes the model faster, cheaper, and higher quality <a class="yt-timestamp" data-t="12:28:00">[12:28:00]</a>. This typically occurs as a product moves from pre-product market fit to post-product scaling <a class="yt-timestamp" data-t="12:22:00">[12:22:00]</a>.
*   **Pre-training**: While hyperscalers consolidate pre-training data, the ROI for most enterprises in pre-training models is often not justified given the expense and human resources required <a class="yt-timestamp" data-t="12:54:00">[12:54:00]</a>. Post-training on strong base models offers a much stronger ROI and greater agility <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a>.

Fireworks believes in customization and aims to make the customization process extremely easy <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.

## Enterprise AI Adoption and Deployment Models

Successful generative AI applications tend to involve "human-in-the-loop" automation rather than full "human-out-of-the-loop" automation <a class="yt-timestamp" data-t="14:03:00">[14:03:00]</a>. A generative AI system must be human-debuggable, understandable, maintainable, and operable to gain adoption <a class="yt-timestamp" data-t="14:16:00">[14:16:00]</a>.

Examples of successful applications include:
*   Assistants for doctors (scribing), teachers, and students (educational, foreign languages) <a class="yt-timestamp" data-t="14:52:00">[14:52:00]</a>.
*   Coding assistants (e.g., Cursor, Sourcegraph) <a class="yt-timestamp" data-t="15:04:00">[15:04:00]</a>.
*   Medical assistants addressing nursing shortages <a class="yt-timestamp" data-t="15:15:00">[15:15:15]</a>.
*   B2B automation, such as call center assistants that make human agents more productive <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>.

In terms of model adoption, Lyn Chia observes a strong convergence and adoption of various Llama models due to their quality, strong base, excellent instruction following, and fine-tuning capabilities <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>.

### Evaluations (Evals) in Enterprise AI

Many enterprises initially use "vibe-based" evaluations <a class="yt-timestamp" data-t="16:59:00">[16:59:00]</a>. However, they quickly recognize the need to consciously invest in building evaluation datasets to stay on top of the state of the art and evaluate quality, especially when moving into deeper prompt engineering or fine-tuning <a class="yt-timestamp" data-t="17:23:00">[17:23:00]</a>. While A/B testing is the ultimate method for determining product impact, it has a longer cycle <a class="yt-timestamp" data-t="17:47:00">[17:47:00]</a>. Generating good eval data helps companies understand what truly matters amidst the constant stream of new, specialized models <a class="yt-timestamp" data-t="18:18:00">[18:18:00]</a>.

## Fireworks' F1 and Function Calling

Fireworks developed F1, a complex logical reasoning inference system available as an API, which comprises multiple underlying models and implements logical reasoning steps <a class="yt-timestamp" data-t="19:37:00">[19:37:00]</a>. Building such a system is complex, involving challenges in inter-model communication and quality control <a class="yt-timestamp" data-t="20:14:00">[20:14:14]</a>.

**Function Calling** is a critical extension point that allows models to call other tools to enhance answer quality <a class="yt-timestamp" data-t="21:38:00">[21:38:00]</a>. Key challenges include:
*   Models needing to hold long contexts in multi-turn chats to influence tool selection <a class="yt-timestamp" data-t="21:57:00">[21:57:00]</a>.
*   The ability to call into multiple tools (potentially hundreds) <a class="yt-timestamp" data-t="22:11:00">[22:11:00]</a>.
*   Complex coordination requiring parallel and sequential tool execution planning <a class="yt-timestamp" data-t="22:20:00">[22:20:00]</a>.

Fireworks has invested in this area for about a year, noting that when they initially launched their function calling model, they were ahead of the adoption curve <a class="yt-timestamp" data-t="23:24:00">[23:24:00]</a>. They strategically invest in these critical areas, such as orchestration, viewing each small expert model as a tool itself, to tie everything together in a compound AI system <a class="yt-timestamp" data-t="24:10:00">[24:10:00]</a>.

## [[Trends and challenges in AI infrastructure|Hardware and Infrastructure Trends]]

There is a scarcity of developers who understand low-level hardware optimization <a class="yt-timestamp" data-t="28:54:00">[28:54:00]</a>. The pace of hardware development has accelerated, with new hardware generations emerging annually from vendors <a class="yt-timestamp" data-t="29:06:00">[29:06:00]</a>. Accessing the "best" hardware is complex, as it depends on the workload pattern and specific bottlenecks <a class="yt-timestamp" data-t="29:22:00">[29:22:00]</a>. Fireworks absorbs the burden of integrating and determining the optimal hardware for different workloads, even routing to mixed hardware for varying access patterns <a class="yt-timestamp" data-t="29:49:00">[29:49:00]</a>. Their goal is to alleviate this concern for developers, allowing them to focus on product building <a class="yt-timestamp" data-t="30:08:00">[30:08:00]</a>.

### Local Model Deployment

Arguments for running models locally include cost savings (avoiding cloud GPU payments) and privacy <a class="yt-timestamp" data-t="33:25:00">[33:25:00]</a>.
*   **Desktop**: Offloading compute from the cloud to desktop for consumer-facing applications makes sense, similar to how Zoom saves costs <a class="yt-timestamp" data-t="34:51:00">[34:51:00]</a>.
*   **Mobile**: Offloading to mobile is a different story due to limited power, where application metrics like power consumption directly affect user adoption and experience <a class="yt-timestamp" data-t="34:02:00">[34:02:00]</a>. Models practically deployable to mobile are tiny (1B-10B parameters) with limited capabilities <a class="yt-timestamp" data-t="34:31:00">[34:31:00]</a>.
*   **Privacy**: The privacy argument is nuanced, as most personal data already resides in the cloud <a class="yt-timestamp" data-t="35:03:00">[35:03:00]</a>.

## Open Source and Meta's Role

Meta has provided a significant service to the AI ecosystem by training and open-sourcing larger models, such as Llama <a class="yt-timestamp" data-t="35:21:00">[35:21:00]</a>. They are also building a standard called "Llama Stack" to standardize tools around Llama models <a class="yt-timestamp" data-t="36:00:00">[36:00:00]</a>, aiming to create an "Android world" where components are easily pluggable and adoptable <a class="yt-timestamp" data-t="36:28:00">[36:28:00]</a>. Lyn Chia expects continuous investment from Meta in this area, anticipating Llama 4 <a class="yt-timestamp" data-t="36:45:00">[36:45:00]</a>.

The investment in pre-training by model providers will continue as long as there is sufficient ROI <a class="yt-timestamp" data-t="36:57:00">[36:57:00]</a>. However, the industry is approaching a "soft wall" of data, as everyone has crawled the same internet data and exhausted synthetic and multimedia data combinations <a class="yt-timestamp" data-t="37:07:00">[37:07:00]</a>. This will lead to a shift in investment and ROI from pre-training towards post-training and, ultimately, inference <a class="yt-timestamp" data-t="37:43:00">[37:43:00]</a>.

## [[Economic and strategic considerations in AI model deployment|Competitive Landscape and Fireworks' Differentiation]]

Fireworks maintains compatibility with imperative agentic tools like LangChain, viewing them as complementary rather than competitive, and aims to simplify the layer above single-model services <a class="yt-timestamp" data-t="38:17:00">[38:17:00]</a>.

The concept of "compound AI systems" (coined by Berkeley) is a new and meaningful category where multiple players, including Databricks, are emerging <a class="yt-timestamp" data-t="39:32:00">[39:32:00]</a>. Fireworks aims to be a key player in this space by providing tools to make development more efficient <a class="yt-timestamp" data-t="40:11:00">[40:11:00]</a>. Unlike GPU cloud providers, Fireworks builds *on top* of GPU clouds to offer a complex inference stack, rather than providing cheap GPU access <a class="yt-timestamp" data-t="40:28:00">[40:28:00]</a>.

## Fireworks' Journey and Evolution

Fireworks was founded a few months before ChatGPT's release <a class="yt-timestamp" data-t="40:48:00">[40:48:00]</a>, at a time when there was debate about whether AI had truly arrived <a class="yt-timestamp" data-t="41:15:00">[41:15:00]</a>. Lyn Chia, coming from Meta (which was heavily AI-powered), saw the coming wave of AI, driven by PyTorch adoption <a class="yt-timestamp" data-t="41:39:00">[41:39:00]</a>.

ChatGPT fundamentally changed the accessibility of AI <a class="yt-timestamp" data-t="42:01:00">[42:01:00]</a>. Before generative AI, companies needed to hire large machine learning teams to train models from scratch and curate data <a class="yt-timestamp" data-t="42:27:00">[42:27:00]</a>. Generative AI's foundation models absorb a majority of knowledge, allowing companies to build directly on top of them (as-is or with fine-tuning) without needing extensive ML teams <a class="yt-timestamp" data-t="43:22:00">[43:22:00]</a>. This massive unblocking of accessibility led to the rapid adoption of generative AI <a class="yt-timestamp" data-t="43:43:00">[43:43:00]</a>. Fireworks pivoted to laser focus on generative AI due to this strong pull and their expertise in operating PyTorch models in production <a class="yt-timestamp" data-t="43:57:00">[43:57:00]</a>.

## [[Challenges and strategies in AI model development|Unsolved Problems and Future Research in AI Infrastructure]]

Key areas of ongoing development and research include:
*   **Agentic Workflows**: The industry is still in the early stages of defining the right user experience and abstraction for building agentic workflows <a class="yt-timestamp" data-t="47:03:00">[47:03:00]</a>.
*   **Model-System Codesign**: Research focusing on optimizing quality, latency, and cost by considering model and system design together <a class="yt-timestamp" data-t="45:32:00">[45:32:00]</a>.
*   **Next-Generation Transformer Architectures**: Research into disruptive technologies beyond current Transformer architectures that will change how models are trained and inference is performed <a class="yt-timestamp" data-t="46:27:00">[46:27:00]</a>.
*   **Agent Communication in Latent Space**: Exploring new ways agents can communicate, for instance, by "thinking" in latent space rather than words, potentially leading to more efficient thinking processes <a class="yt-timestamp" data-t="46:43:00">[46:43:00]</a>.

### [[Challenges in AI model development and commoditization|Challenges of an Infrastructure Company in a Fast-Changing Field]]

The rapid pace of change in model capabilities and enterprise adoption poses a challenge for an infrastructure company <a class="yt-timestamp" data-t="47:01:00">[47:01:00]</a>. Fireworks avoids constantly chasing new trends by anchoring to core beliefs:
*   **Specialization and Customization**: The fundamental trend of models becoming more specialized and customizable will not change <a class="yt-timestamp" data-t="48:16:00">[48:16:00]</a>. There is no "one size fits all" solution for proprietary data and diverse workloads <a class="yt-timestamp" data-t="48:27:00">[48:27:00]</a>.
*   **Control over Destiny**: Providing users with the ability to customize, steer, and control their AI destiny is crucial <a class="yt-timestamp" data-t="48:42:00">[48:42:00]</a>.

Fireworks addresses this by offering an inference engine that fits all, alongside an "Optimizer" that takes workload and customization objectives as input to spit out optimized inference deployment configurations and potentially adjusted models <a class="yt-timestamp" data-t="48:55:00">[48:55:00]</a>. This process closes the loop and makes customization easy, a fundamental principle that Lyn Chia believes will persist <a class="yt-timestamp" data-t="49:23:00">[49:23:00]</a>.

## Overhyped vs. Underhyped

*   **Overhyped**: The perception that generative AI is "magical" and a panacea for all problems, capable of providing correct answers to any question <a class="yt-timestamp" data-t="49:50:00">[49:50:00]</a>. This view is currently undergoing a correction <a class="yt-timestamp" data-t="50:00:00">[50:00:00]</a>.
*   **Underhyped**: The "agentic world" has not been fully figured out yet but holds significant potential <a class="yt-timestamp" data-t="54:10:00">[54:10:00]</a>.

## Shift in Go-to-Market Strategy

Initially, Lyn Chia hypothesized a sequential adoption curve: startups first, then digital natives, and finally traditional enterprises <a class="yt-timestamp" data-t="50:25:00">[50:25:00]</a>. However, in reality, Fireworks is working with all segments simultaneously, demonstrating a dramatically accelerated adoption curve driven by a "revolution" in AI <a class="yt-timestamp" data-t="50:47:00">[50:47:00]</a>. This has led to shorter sales cycles and different procurement processes <a class="yt-timestamp" data-t="51:35:00">[51:35:00]</a>.

For startups, there's typically a desire for lower-level abstractions, allowing them more control <a class="yt-timestamp" data-t="51:57:00">[51:57:00]</a>. Traditional enterprises, conversely, often prefer higher-level abstractions that hide complex details <a class="yt-timestamp" data-t="52:22:00">[52:22:00]</a>. Fireworks builds both, as the lowest-level abstraction is necessary for internal development, and anticipates adoption across different layers <a class="yt-timestamp" data-t="52:52:00">[52:52:00]</a>.

To learn more about Fireworks, visit their self-serve platform at fireworks.ai <a class="yt-timestamp" data-t="55:01:00">[55:01:00]</a>.