---
title: AI inference and compound AI systems
videoId: zG-kxc0q_cE
---

From: [[redpointai]] <br/> 

Lynn Chio, co-founder and CEO of Fireworks, leads a company focused on building fast and efficient inference for compound AI systems [00:00:00]. Chio was also one of the creators of PyTorch at Meta [00:00:04]. Fireworks has raised over $75 million from investors like Coatue and Benchmark [00:00:08].

## Fireworks' Vision and Approach
Fireworks is a Generative AI (GenAI) platform with a laser focus on inference [00:01:14]. Its primary goal is to deliver the best quality, lowest latency, and lowest cost inference [00:01:19]. The company envisions a future where the inference system is complex, featuring logical reasoning and access to hundreds of small expert models [00:01:41]. This approach is in contrast to simple API calls for single models [00:01:54].

### The Need for Compound AI Systems
Models are probabilistic by nature, making it challenging to deliver consistently factual and truthful results [00:02:21]. Complex business problems often require assembling multiple models across different modalities [00:02:40]. For instance, human interaction involves processing audio, visual, and textual information simultaneously [00:03:00]. Even within the same modality, such as Large Language Models (LLMs), there are many expert models specialized in tasks like classification, summarization, multi-turn chats, and tool calling [00:03:23].

Single models are also limited by their training data, which is finite [00:03:43]. A lot of real-world information resides behind APIs (public or proprietary Enterprise APIs) that models cannot access directly [00:03:51]. This necessitates a shift beyond single models as a service [00:04:09]. The industry is moving towards a concept called **compound AI system**, which involves multiple models across different modalities, integrated with various APIs and knowledge sources like databases, storage systems, and knowledge bases, all working together to deliver optimal AI results [00:04:16].

## Tools for Building Compound AI Systems
When building complex [[developers_approach_to_ai_models_and_agents | AI systems]], developers face a choice between two design approaches [00:04:41]:
*   **Imperative Design:** Developers have full control over the workflow, inputs, and outputs, aiming for deterministic results [00:04:49]. This is akin to explicitly designing each part of a house [00:05:05].
*   **Declarative Design:** Developers define *what* problem the system should solve, allowing the system to figure out *how* to solve it [00:05:10]. An example from the database world is SQL, where users define the desired data, and the database management system determines the most efficient execution plan [0005:35].

Fireworks leans towards a more declarative system design, emphasizing simplicity for the user while hiding underlying complexity, without sacrificing iteration speed [00:06:17].

## Evolution of Fireworks' Product
Fireworks started with the lowest level of abstraction: single model as a service [00:06:51]. Today, they provide hundreds of models, including Large Language Models, audio models (transcription, translation, speech synthesis), vision models (PDF, images, screenshots), and embedding/image generation models [00:06:57]. While developers can assemble these building blocks, controlling quality and managing constant model releases (including version control) becomes difficult [0007:24]. Recognizing a usability gap, especially for enterprises, Fireworks aims to bridge it [00:07:56].

## Barriers to GenAI Application Adoption
Several factors limit the widespread adoption of GenAI applications [00:08:07]:
*   **No "One Model Fits All":** Due to the nature of the training process, models excel at specific problems where significant resources were dedicated to data acquisition and quality, but perform poorly in other areas [00:08:13].
*   **Future of Small Expert Models:** The future lies in hundreds of small expert models, as shrinking the problem space allows smaller models to achieve higher quality [00:09:01]. Open-source base models enable customization, with many providers focusing on post-training or fine-tuning to deliver specialized models [00:09:15]. Enterprises are moving towards having more control and steerability [00:09:48].

## Model Customization and Strategy
Fireworks deeply believes in customization [00:10:25]. There's a trade-off between prompt engineering and fine-tuning [00:10:43]:
*   **Prompt Engineering:** Offers immediate results and responsiveness, making it a common starting point for testing model steerability [00:10:57]. However, it can lead to thousands of lines of system prompts, becoming unmanageable [00:11:17].
*   **Fine-tuning:** Becomes crucial when prompt engineering becomes too complex, absorbing long system prompts into the model itself [00:11:59]. This makes the model faster, cheaper, and higher quality [00:12:30]. Fine-tuning is typically adopted post-product-market fit during product scaling [00:12:23].
*   **Pre-training:** While the industry is moving towards pre-training consolidating data into hyperscalers, some enterprises pre-train models if it's core to their business [00:12:54]. However, pre-training is expensive, requiring significant money and human resources, making its return on investment (ROI) harder to justify compared to post-training on strong base models [00:13:28].

## GenAI Use Cases with Product Market Fit
Most successful GenAI use cases involve human-in-the-loop automation, not yet fully human-out-of-the-loop automation [00:14:03]. A GenAI system must be human-debuggable, understandable, maintainable, and operable to gain adoption [00:14:21].

Successful applications include:
*   **Assistants for Professionals and Consumers:**
    *   Doctors for scribing [00:14:52]
    *   Teachers and students for learning foreign languages [[ai_in_language_learning | AI in language learning]] and [[ai_and_education_technology | education technology]] [00:14:58]
    *   Coding assistants (e.g., Cursor, Sourcegraph) [00:15:04]
    *   Medical assistants addressing nurse shortages [00:15:15]
*   **B2B Automation:**
    *   Call center automation, building assistants for human agents to improve productivity and answer questions [00:15:41]
    *   Optimizing business logic and workflow efficiency [00:16:05]

## Model Trends and Evaluation
There's a significant convergence around variations of [[evolution_of_ai_models_and_infrastructure | Llama models]], which are seen as strong base models for instruction following and fine-tuning [00:16:16].

### The State of Evaluations (Evals)
Many enterprises initially use "vibe-based" evaluations during early product development to get a sense of how products feel with different models [00:17:02]. However, they quickly realize the need to consciously build dedicated evaluation processes as an investment area to stay current with the state-of-the-art [00:17:26]. While A/B testing is the ultimate determinant of product impact, it has a longer cycle [00:17:51]. Investing in generating good eval datasets helps enterprises clearly understand what matters for quality [00:18:18]. As models become more specialized, enterprises harden their product design and seek specialized models for specific features [00:18:48].

## Fireworks' F1 Model and Function Calling
Fireworks released F1 as an API [00:19:28]. F1 is not a single model but a complex logical reasoning inference system built upon multiple underlying models and logical reasoning steps [00:19:37]. Building such a system is complex, involving challenges in managing information flow between models and controlling quality [00:20:04].

A key part of F1's capability is function calling, which acts as an extension point for models to integrate with other tools to enhance answer quality [00:21:10]. Function calling is complex:
*   It requires models to hold a long context of conversation to influence tool selection [00:22:02].
*   Models need to call into multiple tools (potentially hundreds) [00:22:11].
*   It involves complex planning for parallel and sequential tool execution [00:22:22].
*   Precision in understanding when and how to call a tool is crucial [00:22:43].

Fireworks heavily builds on the open-source community, believing that hundreds of small expert models will emerge from it [00:23:55]. However, they strategically invest in areas like the compound AI system and the orchestration layer (e.g., function calling models) because these are critical ingredients for tying everything together and cannot wait for open-source development [00:24:10].

## Future of Reasoning Models and AI Infrastructure
Even for reasoning, there are different approaches [00:25:23]:
*   Strong base models using self-inspection techniques like Chain-of-Thought and Tree-of-Thoughts [00:25:34].
*   New models that perform logical reasoning in latent space, rather than just the prompt space, similar to how human thinking processes might not always be verbal [00:26:01].

Fireworks plans to integrate different flavors of logical reasoning into its system [00:26:41].

### Unsolved Problems in AI Infrastructure
A major unsolved problem is building [[evolution_of_ai_models_and_infrastructure | agentic workflows]] [00:27:03]. The industry is still in the early stages of determining the right user experience and system abstractions – what should be hidden vs. exposed to developers [00:27:10]. Fireworks aims to expose developer-facing plugins to allow others to build their own "F1s" [00:28:13].

### Hardware Landscape
There's a scarcity of developers skilled in low-level hardware optimization [00:29:00]. The hardware development cadence is accelerating, with new hardware skills emerging annually from vendors [00:29:06]. There's no single "best hardware" as it depends on the workload pattern and bottlenecks [00:29:27]. Fireworks absorbs the burden of integrating and determining the best hardware for specific workloads, even routing mixed access patterns to different hardware, to allow developers to focus on product building [00:29:57].

### Hyperscalers vs. Specialized Providers
Hyperscalers aim to build vertically integrated stacks like Apple [00:30:57]. Their biggest benefit is solving massive resource-intensive problems, such as building data centers and deploying machines [00:31:30]. Fireworks specializes in problems requiring a combination of engineering craftsmanship and deep research, deploying at scale [00:32:03]. The complexity of compound logical reasoning inference systems is not easily solved just by throwing people and money at it [00:33:01].

### Local vs. Cloud Inference
Arguments for running models locally include cost savings (avoiding cloud GPU fees) and privacy [00:33:25]. While offloading compute from cloud to desktop makes sense for cost, offloading to mobile is challenging due to limited power and its impact on application metrics like cold start time and power consumption [00:34:02]. Regarding privacy, much personal data is already on the cloud, making the local privacy argument less straightforward [00:35:03].

### Open Source and Meta's Role
Meta has significantly contributed to the ecosystem by open-sourcing Llama models [00:35:26]. They are also building a standard called "Llama Stack" to standardize tools around Llama models [00:36:00]. Meta's ambition is to create an "Android world" for AI, with standardized, pluggable components [00:36:28]. There's continuous investment in pre-training, which will likely persist until a "data wall" is hit, where training data becomes exhausted [00:36:46]. Investment is already shifting from pre-training to post-training and then to inference as ROI transitions [00:37:43].

## Fireworks' Journey and Market Insights
Fireworks started a few months before ChatGPT [00:40:48]. When the company began, there was active debate about whether AI was truly "here" [00:41:15]. Hyperscalers typically lead the industry by 3-5 years, and Meta, a massive AI-powered company, showed the wave was coming [00:41:39].

ChatGPT heavily skewed the adoption curve of AI by fundamentally changing accessibility [00:42:05]. Before GenAI, companies needed large machine learning teams to train models from scratch, curate data, and invest heavily in scarce talent [00:42:27]. GenAI created foundation models that absorbed most knowledge, allowing development teams to build on top directly or with small machine learning teams for fine-tuning, massively unblocking accessibility [00:43:21]. This shift led Fireworks to laser-focus on GenAI, leveraging their PyTorch expertise [00:43:57].

### Overhyped vs. Underhyped
*   **Overhyped:** The perception that GenAI is magical and a universal solution to all problems [00:49:50]. There is no single model that solves all problems perfectly [00:50:06].
*   **Underhyped:** The speed of the adoption curve [00:50:58]. The market is experiencing a revolution where technology adoption and go-to-market strategies are different, with shorter sales cycles and different procurement processes [00:51:20].

### Enterprise vs. Startup Needs
Startups typically seek access to lower-level abstractions to customize and assemble components [00:51:57]. Traditional enterprises, however, prefer higher-level abstractions, wanting to avoid low-level details [00:52:22]. Fireworks builds both, as the lowest-level abstraction is needed internally, and adoption will occur at different layers [00:52:52].

## Future Research and Spending
*   **Model-system codesign:** Research focusing on the trade-offs between quality, latency, and cost in tandem [00:45:27].
*   **Disruptive technologies:** Next-generation Transformer architectures and how different agents will communicate, particularly "thinking in latent space" [00:46:19].

It's unlikely someone will spend $100 billion on training a model unless it uses a fundamentally different, disruptive model architecture [00:53:48]. The [[role_of_ai_in_general_intelligence_and_application_development | agentic world]] is still being figured out [00:54:12], with early applications seen in digital SDRs and digital marketing [00:54:26].

To learn more about Fireworks, visit fireworks.ai [00:55:09].