---
title: The role and potential of open source models in AI
videoId: MvxtIIqJRUQ
---

From: [[redpointai]] <br/> 

Peter Welinder, VP of Product and Partnerships at OpenAI, offers a nuanced perspective on the future of open source AI models, contrasting them with proprietary, closed-source approaches. While acknowledging the potential of open source in the very long run, he believes that the most advanced AI systems will likely remain proprietary for the foreseeable future due to significant investment and safety considerations.

## Peter Welinder's Perspective: Open vs. Closed Source
Peter Welinder admits his view on open source models might be an "unpopular opinion" [00:15:21]. He believes that while [[open_source_models_and_adoption_challenges | open source]] models might eventually catch up in the very long run due to increasing compute power [00:15:46], there will always be a category of AI systems that are "way way better than the [[open_source_models_and_adoption_challenges | open source]] kind of versions" [00:16:18].

He draws a parallel to desktop Linux, which, despite existing for 30 years, has not "caught up to like you know Mac OS X and and iOS and and windows" due to insufficient investment in details [00:16:30]. Similarly, the capital and engineering required for training and inference in advanced AI models are "very non-trivial and it's just hard to replicate at at an [[open_source_models_and_adoption_challenges | open source]] level" [00:17:15]. Companies making significant investments are unlikely to [[open_source_versus_closed_source_models_in_ai | open source]] their models due to investment and safety standpoints [00:17:24]. OpenAI's strategy focuses on providing broad access to their models through an API rather than open-sourcing their most advanced ones [00:17:44].

## Benefits and Role of Open Source Models
Despite his skepticism about parity with leading proprietary models, Welinder expresses excitement about [[the_evolution_and_sustainability_of_open_source_projects_with_ai | open source]] development [00:17:59]. He identifies several critical roles for [[open_source_models_and_adoption_challenges | open source]] models:
*   **Research Advancement**: They are "extremely useful for pushing the research forward" [00:18:10].
*   **Experimentation**: They enable people to "try out new approaches" and "different kinds of ways of training these models" [00:18:16].
*   **Specific Product Areas**: [[open_source_models_and_adoption_challenges | Open source]] models are valuable for specific product areas such as:
    *   Smaller models for devices or edge deployments [00:18:36].
    *   On-premise deployments where control over latency and recomputing embeddings is important [00:18:42].
*   **Enabling Broader Use Cases**: OpenAI itself engages in [[open_source_versus_closed_source_models_in_ai | open source]] investments where it can enable more complex AI use cases without focusing on direct monetization. The **Whisper model** is cited as an example, open-sourced to allow accurate audio transcription, which then feeds into large language models to build more applications [00:24:39].

## Competitive Landscape and Model Performance
Welinder doesn't see [[open_source_vs_closed_source_large_language_models | open source]] models as a meaningful competitive risk to OpenAI's business model [00:21:49]. He argues that "most of the value is ultimately going to be in the smartest models" [00:21:54]. Just as companies hire the best people, they will want the smartest models to build the best products [00:22:09]. Opting for a "dumber" model would put a company at a competitive disadvantage [00:22:28].

OpenAI's bet is that "most of the value over time will just accrue in the smart models" [00:22:40], enabling the tackling of "most economically valuable problems" [00:22:44]. These models can serve as co-pilots for professions like lawyers and medical providers [00:22:58] and eventually lead to "science AI scientist that come up with new drugs or come up with um you know solutions to climate change" [00:23:10].

## The Role of Generality and Specialization
A key consideration is how "smart" a model needs to be for a given task [00:19:56]. While simpler tasks like summarization might not require the smartest model [00:20:02], products tend to "go towards generality over time" [00:20:14]. If a product starts with a specialized [[open_source_models_and_adoption_challenges | open source]] model, it risks hitting issues when attempting to operate slightly outside its initial domain [00:20:21].

For applications like customer service bots, the smartest model is needed to handle "all the edge cases" [00:20:44]. Welinder notes that each smarter model covers more use cases, and while some applications may always find smaller [[open_source_models_and_adoption_challenges | open source]] models sufficient, the highest economic value lies with the state-of-the-art, more general models [00:20:54].

### Hallucinations and Model Reliability
A significant challenge in enterprise adoption is the problem of models "hallucinating facts" [00:26:20]. This is an active [[challenges_and_advancements_in_ai_model_development | open research problem]] [00:26:38]. Companies often mitigate this by "grounding the models in external data" [00:26:55], using vector databases to provide relevant context to the language models [00:27:11]. This allows the model to state "I don't know" if an answer isn't found in the provided context [00:27:34].

OpenAI prioritizes improving model reliability, lowering prices, and reducing latency as fundamental to their service, which then enables the ecosystem to build specialized tooling [00:29:17]. Without strong fundamentals, tooling "doesn't matter" [00:29:38].