---
title: Compound AI systems and their development
videoId: zG-kxc0q_cE
---

From: [[redpointai]] <br/> 
Lyn Chia, co-founder and CEO of Fireworks AI, discusses the evolution of AI systems from single models to complex [[Challenges and advancements in AI model development|compound AI systems]], focusing on efficient inference. Fireworks AI aims to provide a platform for developers to build these advanced systems, emphasizing quality, low latency, and low cost in the inference stack <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.

### What are Compound AI Systems?
A compound AI system is envisioned as a complex inference system that incorporates logical reasoning and can access hundreds of small expert models <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. It goes beyond a simple API call in and out <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. The core idea is to move beyond the notion of a "single model as a service" to a system where multiple models across different modalities work together with various APIs holding knowledge (databases, storage, knowledge bases) to deliver the best AI results <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.

### Why Compound AI Systems are Necessary
Traditional single AI models have several limitations <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>:
*   **Non-deterministic Nature**: Models are probabilistic by nature, which is undesirable for factual or truthful results <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>. Controlling verification is crucial <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>.
*   **Complex Business Problems**: Many business problems require assembling multiple models across various modalities (audio, visual, text) to solve them effectively <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. For instance, processing audio and visual information for interactive experiences <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.
*   **Specialized Models**: Even within the same modality, like Large Language Models (LLMs), there are many expert models specializing in tasks like classification, summarization, multi-turn chats, and tool calling <a class="yt-timestamp" data-t="03:23:00">[03:23:00]</a>. A single model is very limited for real-world problems <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.
*   **Knowledge Limitations**: Single models are limited by their finite training data <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>. Real-world information often resides behind APIs (public or proprietary) that models cannot access directly <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.
*   **No One-Model-Fits-All**: Due to the nature of the training process, models become highly specialized in certain areas and weak in others <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>. This leads to a future of hundreds of small expert models <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>, which is beneficial for the open-source community as it allows for customization and specialization <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>.

### [[Developing and utilizing AI models in the tech industry|Developing Compound AI Systems]]
Developing these systems involves specific design tools and considerations:

#### Imperative vs. Declarative Design
*   **Imperative Design**: Developers have full control over the workflow, inputs, and outputs, aiming for deterministic results <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.
*   **Declarative Design**: Developers define *what* problem the system should solve, allowing the system to determine *how* to solve it. SQL is an example of a declarative approach <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>.
*   Fireworks AI leans towards a more declarative system design, focusing on simplicity, debuggability, and maintainability, while hiding nitty-gritty details and complexity from the user <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>.

#### Building Blocks and Abstractions
Fireworks AI started with the lowest level of abstraction: single model as a service <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>. Today, they provide hundreds of models across various modalities (LLMs, audio, vision, embedding, image/video generation) as foundational building blocks <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>.
However, developers face challenges in assembling these pieces and controlling quality due to the rapid release of new models <a class="yt-timestamp" data-t="07:24:00">[07:24:00]</a>. This identified a "huge gap in usability," especially for enterprises <a class="yt-timestamp" data-t="07:56:00">[07:56:00]</a>.

#### Customization and Model Training
Customization is deeply valued at Fireworks AI <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.
*   **Prompt Engineering**: Often the starting point for developers to test a model's steerability <a class="yt-timestamp" data-t="11:07:00">[11:07:00]</a>. However, it can become unmanageable with thousands of lines of system prompts <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>.
*   **Fine-tuning**: The "prime time" for fine-tuning is when prompt engineering becomes too complex, allowing absorption of long system prompts into the model itself for faster, cheaper, and higher-quality inference <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>. Fireworks AI is working on making customization extremely easy <a class="yt-timestamp" data-t="10:51:00">[10:51:00]</a>.
*   **Pre-training**: While some enterprises pre-train models for core business reasons, it is very expensive <a class="yt-timestamp" data-t="13:08:00">[13:08:00]</a>. The ROI is generally stronger for post-training (fine-tuning) on strong base models, offering more agility <a class="yt-timestamp" data-t="13:39:00">[13:39:00]</a>. There is a general industry shift from pre-training investment to post-training and then inference, as data exhaustion becomes a concern <a class="yt-timestamp" data-t="37:43:00">[37:43:00]</a>.

### F1 and Function Calling
Fireworks AI developed F1, a complex logical reasoning inference system offered as a model API <a class="yt-timestamp" data-t="19:37:00">[19:37:00]</a>. Underneath, F1 comprises multiple models and logical reasoning steps, which is highly complex to build and maintain <a class="yt-timestamp" data-t="19:52:00">[19:52:00]</a>. It focuses on solving quality-related problems when models interact with each other <a class="yt-timestamp" data-t="20:14:00">[20:14:00]</a>.

A critical aspect of compound AI systems, and a key feature of F1, is **function calling** <a class="yt-timestamp" data-t="21:10:00">[21:10:00]</a>.
*   Function calling allows models to call external tools to enhance answer quality <a class="yt-timestamp" data-t="21:40:00">[21:40:00]</a>.
*   It's complex because it often involves multi-turn chat contexts, requiring the model to hold long conversations <a class="yt-timestamp" data-t="21:57:00">[21:57:00]</a>.
*   Models need to select from potentially hundreds of tools <a class="yt-timestamp" data-t="22:14:00">[22:14:00]</a>.
*   They must also coordinate calls, executing multiple tools in parallel and sequentially <a class="yt-timestamp" data-t="22:25:00">[22:25:00]</a>. F1 can perform parallel and sequential complex planning and orchestration <a class="yt-timestamp" data-t="22:37:00">[22:37:00]</a>.
*   The precision of tool calling is crucial, making the tuning process complicated <a class="yt-timestamp" data-t="23:20:00">[23:20:00]</a>.

Fireworks AI's decision to build F1 and its function calling capabilities in-house stems from the need to strategically invest in critical areas that tie everything together, rather than waiting for open-source solutions <a class="yt-timestamp" data-t="24:48:00">[24:48:00]</a>. They believe the hundreds of small expert models will come from the open-source community, and their role is to compose them efficiently <a class="yt-timestamp" data-t="24:01:00">[24:01:00]</a>.

### Reasoning [[Model architectures in AI|Models]]
Even for reasoning, there will be different [[Model architectures in AI|models]] specialized in various paths <a class="yt-timestamp" data-t="25:28:00">[25:28:00]</a>. Some approaches include:
*   Strong base models using self-inspection techniques like chain-of-thought and backtracking <a class="yt-timestamp" data-t="25:34:00">[25:34:00]</a>.
*   New [[Model architectures in AI|models]] performing logical reasoning in the latent space, akin to human thought processes that don't always use words <a class="yt-timestamp" data-t="26:01:00">[26:01:00]</a>.
Fireworks AI intends to integrate different flavors of logical reasoning into their system without being opinionated about which will "win" <a class="yt-timestamp" data-t="26:41:00">[26:41:00]</a>.

### [[Building and scaling AI infrastructure companies|Challenges and Strategies in AI Infrastructure]]
One of the major [[Challenges and strategies in AI model development|challenges]] in building an AI infrastructure company is the rapid pace of change in models and enterprise adoption <a class="yt-timestamp" data-t="47:01:00">[47:01:00]</a>.
*   **Hardware Agnosticism**: Fireworks AI absorbs the burden of integrating and determining the best hardware for specific workloads <a class="yt-timestamp" data-t="29:53:00">[29:53:00]</a>. They can route to different hardware even for mixed access patterns <a class="yt-timestamp" data-t="30:04:00">[30:04:00]</a>.
*   **Staying Ahead of the Curve**: Instead of constantly chasing new developments, Fireworks AI focuses on fundamental trends like specialization and customization, believing a single model won't fit all <a class="yt-timestamp" data-t="47:46:00">[47:46:00]</a>. Their Optimizer tool takes inference workload and customization objectives to suggest optimal deployment configurations <a class="yt-timestamp" data-t="48:59:00">[48:59:00]</a>.

### [[Experimenting and testing AI use cases|AI Use Cases with Product-Market Fit]]
Most successful AI applications currently involve "human-in-the-loop" automation rather than full "human-out-of-the-loop" automation <a class="yt-timestamp" data-t="14:03:00">[14:03:00]</a>. This is because AI systems need to be human-debuggable, understandable, maintainable, and operable to gain adoption <a class="yt-timestamp" data-t="14:21:00">[14:21:00]</a>.

Examples of successful use cases include:
*   **Assistants**: For doctors (scribing), teachers/students (education), coding (e.g., Cursor, Sourcegraph), and medical assistants <a class="yt-timestamp" data-t="14:50:00">[14:50:00]</a>.
*   **B2B Automation**: Call center automation, optimizing business logic, and workflow efficiency <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>.
*   **Digital SDRs/Marketing**: Early applications showing good adoption <a class="yt-timestamp" data-t="54:26:00">[54:26:00]</a>.

Regarding model adoption, there's a significant convergence around variations of Llama models due to their quality, strong base, good instruction following, and fine-tuning capabilities <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>.

### The Role of Evals
Many enterprises start with "vibe-based" evaluations for early product development <a class="yt-timestamp" data-t="17:02:00">[17:02:00]</a>. However, they quickly realize the need to consciously build robust evaluation systems <a class="yt-timestamp" data-t="17:26:00">[17:26:00]</a>. While A/B testing is the ultimate determinant of product impact, it has a longer cycle <a class="yt-timestamp" data-t="17:51:00">[17:51:00]</a>. Investing in generating good eval data sets is crucial for understanding what matters and staying on top of the rapidly evolving state-of-the-art models <a class="yt-timestamp" data-t="18:18:00">[18:18:00]</a>. As products mature, they move from open-ended design to more specialized features, requiring specialized models and corresponding evaluations <a class="yt-timestamp" data-t="18:48:00">[18:48:00]</a>.

### Local vs. Cloud Inference
Running [[Model architectures in AI|models]] locally is argued for cost savings and privacy <a class="yt-timestamp" data-t="33:25:00">[33:25:00]</a>.
*   **Cost Savings**: Offloading compute from cloud to desktop makes sense for applications like Zoom <a class="yt-timestamp" data-t="33:53:00">[33:53:00]</a>.
*   **Privacy**: While privacy is a concern, much personal data is already on the cloud, making the local privacy argument less straightforward <a class="yt-timestamp" data-t="35:00:00">[35:00:00]</a>.
*   **Mobile Limitations**: Offloading to mobile devices is more challenging due to limited power and the impact on application metrics like power consumption and latency <a class="yt-timestamp" data-t="34:02:00">[34:02:00]</a>. Practically deployable models on mobile are tiny (1B-10B parameters) with limited capabilities <a class="yt-timestamp" data-t="34:31:00">[34:31:00]</a>.

### The Open Source Ecosystem
Meta's open-source contributions, particularly the Llama models, are seen as a huge service, providing a strong base for fine-tuning and giving developers control <a class="yt-timestamp" data-t="09:20:00">[09:20:00]</a>. Meta is also building "Llama Stack" to standardize tools around Llama models, aiming for an "Android world" where components are standardized and easy to adopt <a class="yt-timestamp" data-t="36:02:00">[36:02:00]</a>. Investment in pre-training by major players like Meta is expected to continue as long as there's sufficient return on investment, which currently relies on access to diverse and high-quality data <a class="yt-timestamp" data-t="36:46:00">[36:46:00]</a>.

### The Future of AI Infrastructure
The competitive landscape for compound AI systems includes players like Databricks, which also recognizes the complexity and potential of this space <a class="yt-timestamp" data-t="39:38:00">[39:38:00]</a>. Fireworks AI differentiates itself by not being a GPU cloud provider but by building a complex inference stack on top of GPU clouds, specializing in the combination of engineering craftsmanship and deep research <a class="yt-timestamp" data-t="40:30:00">[40:30:00]</a>.

The company's original vision, formed before ChatGPT, anticipated the rise of AI due to insights from hyperscalers like Meta, which were already AI-powered <a class="yt-timestamp" data-t="41:39:00">[41:39:00]</a>. Generative AI fundamentally changed accessibility by providing foundation [[Model architectures in AI|models]] that absorbed a majority of knowledge, allowing companies to build applications directly or with smaller machine learning teams, driving rapid adoption <a class="yt-timestamp" data-t="43:16:00">[43:16:00]</a>. This accessibility shift led Fireworks AI to laser-focus on generative AI, leveraging their expertise in PyTorch models <a class="yt-timestamp" data-t="43:57:00">[43:57:00]</a>.

Future challenges in AI infrastructure include defining the right user experience and abstraction for agentic workflows <a class="yt-timestamp" data-t="27:03:00">[27:03:00]</a>. Research areas of interest include:
*   **Model-System Co-design**: Optimizing quality, latency, and cost together, as seen at Meta <a class="yt-timestamp" data-t="45:27:00">[45:27:00]</a>.
*   **Disruptive Technologies**: Looking for the next generation of Transformers and new approaches to agent communication and reasoning in latent space <a class="yt-timestamp" data-t="46:31:00">[46:31:00]</a>.

The rapid adoption curve of AI, even among traditional enterprises, indicates a "revolution" that changes not just applications but also technology adoption curves and go-to-market strategies, with shorter sales cycles and open procurement processes <a class="yt-timestamp" data-t="51:01:00">[51:01:00]</a>. While startups often prefer low-level abstractions to assemble components, traditional enterprises typically seek higher-level abstractions to avoid low-level details <a class="yt-timestamp" data-t="52:03:00">[52:03:00]</a>. Fireworks AI builds both, as the lowest level abstraction is necessary for internal development <a class="yt-timestamp" data-t="52:52:00">[52:52:00]</a>.

Fireworks AI offers a self-serve platform for developers at fireworks.ai, providing access to their playground and hundreds of model capabilities <a class="yt-timestamp" data-t="55:04:00">[55:04:00]</a>.