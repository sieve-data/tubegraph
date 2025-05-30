---
title: Regulatory and safety issues in AI model development
videoId: ZtY8VXswa2o
---

From: [[redpointai]] <br/> 

## Introduction to AI Safety and Regulation Concerns
The development and deployment of AI models, particularly large language models (LLMs), have brought forth significant [[concerns_and_considerations_for_ai_safety_and_regulation | concerns and considerations for AI safety and regulation]] <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. While the goal is to build smaller, cheaper, and more affordable models and applications <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>, the industry faces [[challenges_in_ai_model_training_and_deployment | challenges in AI model training and deployment]] related to costs, market risks, and the strategic implications of powerful AI <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

## Applying Lean Startup Principles in AI Development
Eric Reese, author of *The Lean Startup*, notes that many lessons from his book apply to AI, but the industry often deviates <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. He observes large funding rounds and significant spending on models and compute *before* market interaction <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. This approach is partly due to AI's ability to create "magical" demos, leading developers to believe they don't need extensive customer testing <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

> [!WARNING] The "SAS stack" problem:
> Many AI companies have directly copied the Software-as-a-Service (SaaS) stack model, assuming its principles apply unchanged to AI <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. This often pushes the product-market fit question to deeper layers of the value chain, creating a disconnect between the model builder and the end-user <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. If the AI stack operates differently from traditional software, this approach could lead to "a lot of carnage in applications" <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
>
> Eric Reese emphasizes the importance of understanding the "end end end customer" regardless of one's position in the stack <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. He draws parallels to physical manufacturing and deep infrastructure projects, where physical constraints and operating costs are significant <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## The Role of Moats and Defensibility
There's debate about whether AI companies should prioritize "moats" (defensibility) from the start <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. While large platforms (like OpenAI) theoretically could replicate anything a smaller startup does, their focus is limited <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. The historical lesson suggests that fast, adaptable startups can "pick up dimes in front of a steamroller" by addressing niche use cases <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. However, one misstep could be fatal <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

> [!NOTE] Strategic Humility:
> The current uncertainty in AI, regarding future model capabilities and societal impact, makes confident long-term predictions difficult <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. This necessitates building companies with mechanisms for rapid iteration and the ability to pivot, constantly testing assumptions <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. This ability to adapt and get feedback has "never been more important" <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

## The For-Profit R&D Lab Model: Answer AI
Jeremy Howard and Eric Reese co-founded Answer AI, a for-profit R&D lab, aiming to build the "Bell Labs of AI" <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Their mission is to maximize the public benefit of AI by making it more accessible, particularly through language modalities <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. This addresses Jeremy's concern that AI could lead to power centralization and decreased opportunities <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

This R&D lab model is distinct from traditional startups <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>. It embraces an integrated "research and development" (R&D) approach, unlike the modern hyperspecialization that separates research from practical application <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>. The core belief is that the best research occurs when the researcher is directly "coupled to the application" and customer needs <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

> [!EXAMPLE] Data Center Anecdote:
> In one instance, industrial researchers focused on making data center technology energy-efficient, requiring "fundamental physics breakthroughs" <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. However, taking an MVP to the data center builder revealed that their primary concern was the physical footprint (how many racks could be squeezed in), not operating cost <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>. This misaligned goal highlighted the importance of customer feedback driving scientific inquiry <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.

## Critiques of Current AI Model Development
Jeremy Howard views much of the current investment as "overinvestment in training Foundation models from scratch" on expensive hardware <a class="yt-timestamp" data-t="00:25:40">[00:25:40]</a>. There's an "underinvestment on like the real world which is resource constrained" <a class="yt-timestamp" data-t="00:25:49">[00:25:49]</a>. Bringing down the cost of AI, even if it's "just the same thing but cheaper," is critical for accessibility and wider use <a class="yt-timestamp" data-t="00:26:42">[00:26:42]</a>.

> [!NOTE] Cost as a "Difference in Kind":
> Making inference costs cheaper doesn't just improve margins; it makes previously impossible applications feasible <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>. Lowering costs could enable "continuous fine-tuning" of individual models on inexpensive virtual machines, allowing for hyper-personalization and memory in AI agents, unlike current "amnesiac models" <a class="yt-timestamp" data-t="00:28:45">[00:28:45]</a>. This focus on "manufacturability" and deployability, rather than just "splashy demos," is crucial for moving towards deployed products <a class="yt-timestamp" data-t="00:29:55">[00:29:55]</a>.

## Regulatory and Policy Implications of AI

### The California Bill SB147
Jeremy Howard expresses concern over California's proposed bill SB147, which aims to place limitations and regulatory checks on training foundation models <a class="yt-timestamp" data-t="00:38:22">[00:38:22]</a>. While created with good intentions, Jeremy believes it would be "uneffective" and "likely to cause the opposite" of its intended result, leading to a "less safe situation" <a class="yt-timestamp" data-t="00:40:01">[00:40:01]</a>.

> [!WARNING] The Dual-Use Technology Problem:
> The core issue, according to Jeremy, is that an AI model is a "purely kind of dual use technology" like a pen, paper, or calculator <a class="yt-timestamp" data-t="00:40:32">[00:40:32]</a>. If a model is released, it can be fine-tuned or prompted to do "whatever the hell you like" by the user <a class="yt-timestamp" data-t="00:40:55">[00:40:55]</a>. It's impossible to "ensure the safety" of the raw model itself <a class="yt-timestamp" data-t="00:41:17">[00:41:17]</a>.
>
> Imposing such regulations in practice means that models in their raw form cannot be released <a class="yt-timestamp" data-t="00:41:37">[00:41:37]</a>. Instead, only "products on top of them" can be offered (e.g., a service that writes things down for you, not a pen and paper) <a class="yt-timestamp" data-t="00:41:39">[00:41:39]</a>. This creates a situation where underlying models become "extremely rival risk good" and "a jealously guarded secret," accessible only to "big states and big companies" <a class="yt-timestamp" data-t="00:43:10">[00:43:10]</a>.
>
> This restriction prevents widespread use of models for beneficial, defensive purposes (e.g., improving cybersecurity, vaccines) and instead fosters a "highly competitive space," "massive centralization of power," and reduced transparency <a class="yt-timestamp" data-t="00:43:40">[00:43:40]</a>. This is a key concern in the [[regulation_and_policy_implications_of_ai | regulation and policy implications of AI]].

### Safety and Frontier Models
Eric Reese states that his primary concern is not with foundation model labs themselves, as their mission is often to discover whether AGI is possible <a class="yt-timestamp" data-t="00:44:54">[00:44:54]</a>. However, he highlights a "missing out on a lot of actual practical uses" because fundraising incentives push entrepreneurs toward "science fiction and speculative stuff" rather than utility <a class="yt-timestamp" data-t="00:45:22">[00:45:22]</a>.

> [!INFO] Safer Alternatives:
> If the only models available are large "Frontier models" (closest to AGI), deploying them in real-world systems poses significant safety risks <a class="yt-timestamp" data-t="00:45:50">[00:45:50]</a>. Many valuable applications could be built with "smaller models that are properly fine-tuned and are basically safer by definition" <a class="yt-timestamp" data-t="00:46:15">[00:46:15]</a>. If these intrinsically safer options are not provided, people will default to less safe alternatives <a class="yt-timestamp" data-t="00:46:38">[00:46:38]</a>.
>
> Internal tensions within large foundation model labs, particularly between safety research and commercial objectives, can lead to "schizophrenic" organizations where commercial teams prioritize "number go up" over safety <a class="yt-timestamp" data-t="00:47:06">[00:47:06]</a>. To address this, Eric suggests re-establishing the connection between research and customer needs, actively engaging with users to understand deployment challenges and ensure successful, safe application of technology <a class="yt-timestamp" data-t="00:47:40">[00:47:40]</a>.

## Current Perspectives on AI Trends
### Overhyped vs. Underhyped Areas
*   **Overhyped**: Agents <a class="yt-timestamp" data-t="00:48:34">[00:48:34]</a>. The desired functionalities of agents are often "not compatible with the mathematical foundations of the models" <a class="yt-timestamp" data-t="00:48:44">[00:48:44]</a>, especially for novel planning sequences not present in training data <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>.
*   **Underhyped**: Resource efficiency <a class="yt-timestamp" data-t="00:48:36">[00:48:36]</a>. Reducing energy and other resource requirements for AI models is seen as crucial for enabling new applications and widespread accessibility <a class="yt-timestamp" data-t="00:50:31">[00:50:31]</a>. This is a key aspect of [[economic_and_strategic_considerations_in_ai_model_deployment | economic and strategic considerations in AI model deployment]].

### Desired Breakthroughs
Two major breakthroughs that would change the current landscape of [[challenges_and_advancements_in_ai_model_development | challenges and advancements in AI model development]] are:
1.  **Massive reduction in energy/resource requirements**: Current models have huge energy demands, posing economic and physical obstacles <a class="yt-timestamp" data-t="00:50:34">[00:50:34]</a>.
2.  **Breakthrough in planning and reasoning beyond subgraph matching**: Current auto-regressive models (picking the next word) excel at pattern matching but struggle with complex, novel planning <a class="yt-timestamp" data-t="00:51:16">[00:51:16]</a>. Approaches like "Jeeper-based models" or "diffusion models for text" could overcome these limitations <a class="yt-timestamp" data-t="00:52:12">[00:52:12]</a>.

Ultimately, the goal is to "unlock" the full potential of language as a powerful modality for computing <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. This involves making AI broadly applicable and societally beneficial, particularly in areas like law and education, where language is central and societal impact can be significant <a class="yt-timestamp" data-t="00:34:43">[00:34:43]</a>.