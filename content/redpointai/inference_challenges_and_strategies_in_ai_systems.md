---
title: Inference challenges and strategies in AI systems
videoId: zG-kxc0q_cE
---

From: [[redpointai]] <br/> 

Fireworks is a platform focused on fast and efficient inference for [[challenges_and_optimizations_in_ai_model_training_and_inference | compound AI systems]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The primary goal of Fireworks is to deliver the best quality, lowest latency, and lowest cost in the inference stack <a class="yt-timestamp" data-t="01:19:19">[01:19:19]</a>.

## Limitations of Single-Model Inference
The traditional approach of viewing inference as a single model as a service is overly simplistic <a class="yt-timestamp" data-t="01:28:09">[01:28:09]</a>. There are significant limitations with single models that make them insufficient for real-world problems:
*   **Non-Determinism:** Models are probabilistic by nature, which is undesirable when factual and truthful results are required <a class="yt-timestamp" data-t="02:20:90">[02:20:90]</a>.
*   **Complex Business Problems:** Many business problems require assembling multiple models across different modalities to solve them effectively <a class="yt-timestamp" data-t="02:40:90">[02:40:90]</a>.
    *   For example, current interactive applications process audio and visual information, similar to how GenAI-based native applications need to process multiple modalities <a class="yt-timestamp" data-t="03:00:70">[03:00:70]</a>.
    *   Even within the same modality (like Large Language Models, LLMs), there are many expert LLMs specializing in classification, summarization, multi-turn chats, and tool calling <a class="yt-timestamp" data-t="03:22:90">[03:22:90]</a>.
*   **Knowledge Limitations:** Single models are limited by their training data, which is finite <a class="yt-timestamp" data-t="03:43:40">[03:43:40]</a>. A lot of real-world information exists behind public or proprietary APIs, which models cannot directly access <a class="yt-timestamp" data-t="03:51:70">[03:51:70]</a>.

## The Need for Compound AI Systems
The industry is moving beyond single-model services to a concept called [[challenges_and_advancements_in_ai_technology | compound AI systems]] <a class="yt-timestamp" data-t="04:09:40">[04:09:40]</a>. These systems involve multiple models across different modalities, combined with various APIs that hold knowledge (databases, storage systems, knowledge bases) working together to deliver the best AI results <a class="yt-timestamp" data-t="04:16:10">[04:16:10]</a>.

## Building Compound AI Systems: Design and Tools
Developing these complex systems requires specific tools and design philosophies.

### Imperative vs. Declarative Design
There are two main schools of thought for system design:
*   **Imperative:** Developers have full control over the workflow, inputs, and outputs, aiming for deterministic outcomes <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.
*   **Declarative:** Developers define *what* problem the system should solve, and the system figures out *how* to solve it <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>. SQL in databases is an example of a declarative approach <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>.

Fireworks leans towards a more declarative system design with full debuggability and maintainability <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>. The goal is to provide the simplest user experience by hiding complex details in the backend without sacrificing the speed of iteration <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.

### Evolution of Offerings
Fireworks started with the lowest level of abstraction: single models as a service <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>. Today, they offer hundreds of models across various modalities (Large Language Models, Audio models, Transcription, Translation, Speech Synthesis, Vision models, Embedding models, Image generation, Video models) <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>.

However, assembling these numerous building blocks and maintaining quality control is difficult for developers, especially with new models being released weekly <a class="yt-timestamp" data-t="07:24:00">[07:24:00]</a>. This led to the realization of a "huge gap of usability" for enterprises <a class="yt-timestamp" data-t="07:56:00">[07:56:00]</a>.

### The "No One Model Fits All" Problem
A core observation is that there is no single model that fits all needs <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>. Due to the nature of the training process, models become exceptionally good at specific tasks they are optimized for, and weaker at others <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.

The future lies in hundreds of small expert models <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>. Shrinking a problem to a narrower space inevitably makes it easier for smaller models to achieve higher quality <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>. The open-source community plays a crucial role by providing base models that can be customized and fine-tuned to deliver specialized models <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>.

## Customization and Fine-tuning
Fireworks deeply believes in customization <a class="yt-timestamp" data-t="10:25:00">[10:25:00]</a>. The challenge is making this process extremely easy for enterprises.

### Prompt Engineering vs. Fine-tuning
*   **Prompt Engineering:** Developers often start with prompt engineering to quickly test if a model can be steered in a desired direction <a class="yt-timestamp" data-t="11:07:00">[11:07:00]</a>.
*   **Limitations of Prompt Engineering:** As systems become more complex, managing thousands of lines of system prompts becomes problematic and difficult to change <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>.
*   **Transition to Fine-tuning:** When prompt engineering becomes unwieldy, it's an opportune time for fine-tuning <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>. Fine-tuning allows absorbing the long system prompt into the model itself, making it faster, cheaper, and higher quality <a class="yt-timestamp" data-t="12:28:00">[12:28:00]</a>. This often aligns with a transition from pre-product market fit to post-product market scaling <a class="yt-timestamp" data-t="12:22:00">[12:22:00]</a>.

### Pre-training for Enterprises
While the general trend is towards hyperscalers pre-training models <a class="yt-timestamp" data-t="12:54:00">[12:54:00]</a>, some enterprises do pre-train models if it's core to their business <a class="yt-timestamp" data-t="13:08:00">[13:08:00]</a>. However, pre-training is very expensive and requires significant money and human resources <a class="yt-timestamp" data-t="13:28:00">[13:28:00]</a>. Post-training on top of strong base models often offers a much stronger ROI and greater agility for testing ideas <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a>.

## Use Cases with Product Market Fit: Human-in-the-Loop Automation
Most successful GenAI applications today are human-in-the-loop automation, not fully automated systems <a class="yt-timestamp" data-t="14:03:00">[14:03:00]</a>.

The hypothesis is that a GenAI system must be human-debuggable, understandable, maintainable, and operable <a class="yt-timestamp" data-t="14:16:00">[14:16:00]</a>. If humans cannot evaluate, maintain, or operate a system in production, it's hard to gain adoption <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a>.

Examples of successful human-in-the-loop applications include:
*   **Assistants for Professionals:** Doctors (scribing), teachers/students (education, foreign languages) <a class="yt-timestamp" data-t="14:52:00">[14:52:00]</a>.
*   **Coding Assistants:** Cursor, Sourcegraph <a class="yt-timestamp" data-t="15:04:00">[15:04:00]</a>.
*   **Medical Assistants:** Addressing the shortage of nurses <a class="yt-timestamp" data-t="15:15:00">[15:15:00]</a>.
*   **B2B Automation:** Call center automation, where AI assists human agents to be more productive <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>.
*   **Business Workflow Optimization:** Improving efficiency in various business processes <a class="yt-timestamp" data-t="16:05:00">[16:05:00]</a>.

### Model Adoption Trends
There's a significant convergence of variations of Llama models, which is a testament to their quality as strong base models for instruction following and fine-tuning <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>.

## [[challenges_and_strategies_in_ai_model_evaluation | Challenges and Strategies in AI Model Evaluation]] (Evals)
Many enterprises start with "vibe-based" evaluations during early product development <a class="yt-timestamp" data-t="16:59:00">[16:59:00]</a>. However, they quickly realize the need to consciously build dedicated evaluation datasets, as this is a crucial investment area <a class="yt-timestamp" data-t="17:23:00">[17:23:00]</a>.

*   **Importance of Evals:** Evals are essential for tracking quality, especially when moving into deeper prompt engineering or fine-tuning <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>. While A/B testing is the ultimate determinant of product impact, it has longer cycles <a class="yt-timestamp" data-t="17:47:00">[17:47:00]</a>.
*   **Navigating a Dynamic Landscape:** Enterprises invest in generating good eval datasets to understand what matters most in a constantly evolving landscape of specialized models <a class="yt-timestamp" data-t="18:18:00">[18:18:00]</a>. This allows them to harden their product design and move from open-ended products to specialized features requiring specialized models <a class="yt-timestamp" data-t="18:48:00">[18:48:00]</a>.

## Fireworks' F1 Model and Function Calling
Fireworks developed its own model, F1, as a complex logical reasoning inference system offered via an API <a class="yt-timestamp" data-t="19:23:00">[19:23:00]</a>.

*   **Underlying Architecture:** F1 consists of multiple models and logical reasoning steps implemented within the system <a class="yt-timestamp" data-t="19:52:00">[19:52:00]</a>.
*   **Complexity:** Building such a system is more complex than simple single-model inference, especially regarding quality problems when models interact with each other <a class="yt-timestamp" data-t="20:04:00">[20:04:00]</a>. The complexity is compared to building a database management system <a class="yt-timestamp" data-t="20:36:00">[20:36:00]</a>.
*   **Optimization:** Fireworks, with its expertise in optimizing inference, focuses on managing overall inference latency and cost within this multi-step process <a class="yt-timestamp" data-t="20:52:00">[20:52:00]</a>.

### Function Calling
Function calling is a critical extension point for models to call other tools and enhance answer quality <a class="yt-timestamp" data-t="21:38:00">[21:38:00]</a>.

*   **Growing Demand:** Many F1 waiting list users are building agents and require function calling <a class="yt-timestamp" data-t="21:32:00">[21:32:00]</a>.
*   **Complexity:** Function calling is not just about calling a single tool <a class="yt-timestamp" data-t="21:50:00">[21:50:00]</a>. It often involves:
    *   Holding long contexts in multi-turn chat scenarios <a class="yt-timestamp" data-t="21:57:00">[21:57:00]</a>.
    *   Selecting from hundreds of tools <a class="yt-timestamp" data-t="22:14:00">[22:14:00]</a>.
    *   Executing multiple tools in parallel and sequentially <a class="yt-timestamp" data-t="22:22:00">[22:22:00]</a>.
    *   A complex coordination plan in one shot <a class="yt-timestamp" data-t="22:27:00">[22:27:00]</a>.
*   **Precision:** The model's ability to understand *when* to call a tool and drive precision is vital <a class="yt-timestamp" data-t="23:16:00">[23:16:00]</a>.

### Strategic Decision to Build
Fireworks heavily leverages the open-source community, as it aligns with their vision of hundreds of small expert models <a class="yt-timestamp" data-t="23:55:00">[23:55:00]</a>. However, they also invest in strategically critical areas, such as the orchestration layer for [[challenges_and_opportunities_in_ai_integration | compound AI systems]], where an intelligent model can call into different tools (including other expert models) <a class="yt-timestamp" data-t="24:10:00">[24:10:00]</a>.

## Reasoning Models and Future Research
Even for reasoning, there are different approaches. One path involves strong base models using self-inspection techniques like Chain-of-Thought or Tree-of-Thoughts <a class="yt-timestamp" data-t="25:24:00">[25:24:00]</a>.

A very exciting area of research is new models that can perform logical reasoning not in the prompt space, but in the latent space <a class="yt-timestamp" data-t="25:56:00">[25:56:00]</a>. This aims to make the thinking process more efficient and native to the model's internal workings, similar to how human thinking doesn't always rely on words <a class="yt-timestamp" data-t="26:08:00">[26:08:00]</a>.

Fireworks plans to integrate different flavors of logical reasoning into their system <a class="yt-timestamp" data-t="26:41:00">[26:41:00]</a>. The company's F1 model development serves as an exercise to understand system abstraction and the complexity of building logical reasoning engines <a class="yt-timestamp" data-t="27:55:00">[27:55:00]</a>. This knowledge will then be used to expose developer-facing plugins, allowing others to build their own "F1s" <a class="yt-timestamp" data-t="28:13:00">[28:13:00]</a>.

## [[challenges_and_strategies_in_ai_deployment | Hardware and Infrastructure Challenges]]
A significant challenge in AI infrastructure is the scarcity of developers who understand low-level hardware optimization <a class="yt-timestamp" data-t="29:00:00">[29:00:00]</a>. The hardware development cadence has also accelerated, with new hardware skills emerging annually from vendors <a class="yt-timestamp" data-t="29:09:00">[29:09:00]</a>.

*   **Workload-Dependent Optimization:** There isn't a single "best hardware" for all models or even for one model, as it depends on the workload pattern and specific bottlenecks <a class="yt-timestamp" data-t="29:25:00">[29:25:00]</a>.
*   **Fireworks' Approach:** Fireworks absorbs the burden of integrating and determining the best hardware for different workloads, even routing to different hardware for mixed access patterns <a class="yt-timestamp" data-t="29:49:00">[29:49:00]</a>. This allows developers to focus on product building <a class="yt-timestamp" data-t="30:12:00">[30:12:00]</a>.
*   **Hyperscalers vs. Specialized Platforms:** While hyperscalers aim to be vertically integrated (like Apple building iPhones) by offering massive infrastructure for data centers and machines <a class="yt-timestamp" data-t="30:57:00">[30:57:00]</a>, companies like Fireworks specialize in problems requiring a combination of engineering craftsmanship and deep research, which can then be deployed at scale <a class="yt-timestamp" data-t="32:03:00">[32:03:00]</a>. Inference systems are complex and not easily solved by simply throwing more people and money at them <a class="yt-timestamp" data-t="33:03:00">[33:03:00]</a>.

## Local Model Deployment
Arguments for running models locally include cost saving (avoiding cloud GPU fees) and privacy <a class="yt-timestamp" data-t="33:25:00">[33:25:00]</a>.

*   **Desktop vs. Mobile:** Offloading compute from the cloud to desktop can save costs, similar to applications like Zoom <a class="yt-timestamp" data-t="33:53:00">[33:53:00]</a>. However, offloading to mobile is a different story due to limited power, which affects application metrics like cold start time and power consumption, influencing user adoption <a class="yt-timestamp" data-t="34:02:00">[34:02:00]</a>. Models practically deployable on mobile are tiny (1B, 10B parameters) and have limited capabilities <a class="yt-timestamp" data-t="34:31:00">[34:31:00]</a>.
*   **Privacy Nuance:** The privacy argument for local deployment is debatable, as much personal data is already stored in the cloud, not on local disks <a class="yt-timestamp" data-t="35:03:00">[35:03:00]</a>.

## Open Source Ecosystem and Future of AI Investment
Meta's strategy with open-source Llama models and the Llama Stack aims to standardize the tool stack around these models <a class="yt-timestamp" data-t="35:58:00">[35:58:00]</a>. This creates an "Android world" where components are standardized and easy to adopt <a class="yt-timestamp" data-t="36:28:00">[36:28:00]</a>.

Investment in pre-training by large model providers will likely continue until the ROI diminishes, primarily when hitting a "data wall" (exhausting internet, synthetic, and multimedia data) <a class="yt-timestamp" data-t="36:57:00">[36:57:00]</a>. However, there's already a shift in investment and ROI from pre-training to post-training, and then to inference <a class="yt-timestamp" data-t="37:43:00">[37:43:00]</a>.

## [[challenges_in_ai_research_and_potential_solutions | Challenges in AI Research and Potential Solutions]]
The rapid pace of change in models and enterprise adoption poses a challenge for infrastructure companies <a class="yt-timestamp" data-t="47:01:00">[47:01:00]</a>. The key is to anticipate trends rather than constantly chasing new developments <a class="yt-timestamp" data-t="47:40:00">[47:40:00]</a>.

*   **Enduring Trends:** Fundamental trends like specialization and customization are unlikely to change <a class="yt-timestamp" data-t="48:10:00">[48:10:00]</a>. Fireworks' stack is built to heavily enable easy customization, including an "Optimizer" that takes inference workload and customization objectives as input to spit out optimized deployment configurations <a class="yt-timestamp" data-t="48:47:00">[48:47:00]</a>.
*   **Overhyped/Underhyped:** The perception of GenAI as a magical solution to all problems is overhyped <a class="yt-timestamp" data-t="49:50:00">[49:50:00]</a>. There is no single magical model that solves all problems in the best or correct way <a class="yt-timestamp" data-t="50:06:00">[50:06:00]</a>.
*   **Shifting Adoption Curve:** The adoption curve for GenAI has been much faster and broader than initially imagined <a class="yt-timestamp" data-t="50:58:00">[50:58:00]</a>. Startups, digital natives, and traditional enterprises are all adopting GenAI simultaneously <a class="yt-timestamp" data-t="50:47:00">[50:47:00]</a>. This revolution is changing not only applications and technology adoption but also go-to-market strategies, with shorter sales cycles and different procurement processes <a class="yt-timestamp" data-t="51:22:00">[51:22:00]</a>.
*   **Tailoring for Users:** Startups typically prefer access to lower-level abstractions for more control, while traditional enterprises often prefer higher-level abstractions that hide low-level details <a class="yt-timestamp" data-t="51:57:00">[51:57:00]</a>. Fireworks aims to provide both layers of abstraction <a class="yt-timestamp" data-t="52:52:00">[52:52:00]</a>.

## Further Information
To learn more about Fireworks, visit their self-serve platform at fireworks.ai, which offers access to their playground and hundreds of model capabilities <a class="yt-timestamp" data-t="55:01:00">[55:01:00]</a>.