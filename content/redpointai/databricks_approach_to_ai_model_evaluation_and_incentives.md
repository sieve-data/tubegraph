---
title: Databricks approach to AI model evaluation and incentives
videoId: 7-3IxVvWoxc
---

From: [[redpointai]] <br/> 

Jonathan Frankle, Chief AI Scientist at Databricks, outlines the company's comprehensive approach to supporting enterprises in their AI journey, emphasizing pragmatic [[ai_model_selection_and_evaluation_for_businesses | model selection and evaluation]], and the unique incentive structures fostering innovation within his team <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Enterprise AI Adoption Strategy
Databricks guides its 12,000 customers through the AI adoption journey by prioritizing flexibility and return on investment (ROI) <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. The initial recommendation is to "start small and work your way up" <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>:
*   **Prompting:** Begin by prompting an existing model (e.g., OpenAI or Llama on Databricks) for a "litmus test" to see if AI is suitable for a given use case <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Retrieval-Augmented Generation (RAG):** If initial prompting shows promise, integrate proprietary enterprise data via RAG to enhance model relevance, as generic models won't know internal data <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Fine-tuning:** For more significant value, fine-tuning can bake knowledge into the model, leading to better quality in a smaller package and reducing inference costs <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Continued Pre-training / Pre-training from Scratch:** This is the most significant undertaking, recommended only when justified by rigorous ROI and substantial usage <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. Databricks offers the capability to pre-train models from scratch, which is "not for the faint of heart" but has made a "huge difference" for some customers <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

A common mistake observed is waiting for "perfect data" or "perfect [[ai_model_evaluation_and_benchmarking | evaluation]]" before starting AI projects <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. Instead, the advice is to be agile: do just enough data work to interact with a model, build a quick evaluation, test, and then iterate based on real-world performance <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

## AI Model Evaluation and Benchmarking
[[evaluation_methodologies_and_user_feedback_for_ai_models | Evaluation methodologies]] are critical, and Databricks acknowledges that initial benchmarks are rarely perfect proxies for real-world scenarios <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

Key aspects of [[ai_evaluation_and_benchmarking | AI evaluation and benchmarking]]:
*   **Human-in-the-Loop Testing:** Involving human testers, even a single friend at the company not involved in the project, provides more valuable feedback than synthetic benchmarks <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. Jonathan's team conducts A/B testing of model outputs, including natural language and image generation, often without knowing if the output came from their model, Llama, or OpenAI <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Simple Eval Creation:** Start with five examples for evaluation data, and rate responses from one to five, even without perfectly correct answers. This can calibrate an LLM judge <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
*   **New Evaluation Product:** Databricks has released an "agent evaluation product" that assists users in creating meaningful evaluation sets, aiming to allow users to build a robust eval set of a few dozen examples in an afternoon <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>. This product is key because "until you have a measuring stick, anything else you do is kind of you're just making things up" <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.

## Databricks Platform and Innovation
Databricks' platform integrates various tools to support the entire AI lifecycle:
*   **Data Ingestion and Storage:** Utilizes Spark for ETL, Delta tables for storage, and Unity Catalog for tracking data sets <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. Spark dramatically reduced processing times from weeks to minutes <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
*   **Model Training and Experiment Tracking:** Leverages Mosaic tools for model training and MLflow for experiment tracking <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.
*   **Inference:** Uses Mosaic inference service <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.
*   **Product Development:** The philosophy is to build products that the internal team wants to use <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. The highest endorsement of Databricks' products is that Jonathan's team uses all of them <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.

## Jonathan Frankle's Incentive System
Jonathan Frankle employs a distinctive system to motivate his team and partners:
*   **Hair Dyeing:** He dyed his hair blue when their open source model (dbrx) was initially released, offering his "body on the line to incentivize them to do awesome work" <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   **Swords:** He buys swords for engineers, external partners, and the legal team who provide "great acts of service" to the research team, explicitly stating "swords go to the people who provide service to our team" <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. There is even a "Databricks approved sword vendor" <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Food:** His direct team receives "cookies," "cake," or "Chipotle" as incentives <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.
*   **Openness to new incentives:** He is "always open" to new tributes from his team that would warrant redyeing his hair <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## Views on AI Development and Challenges
*   **Transformer Dominance:** Frankle maintains a "long view" on his bet that Transformers will remain the dominant architecture, noting that current models are essentially the original Transformer with minor tweaks <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. New architectures are "hard to come by," and science tends to move in "big leaps" followed by consolidation <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   **Domain-Specific Models:** [[open_source_ai_models_and_limitations | Company-specific or domain-specific models]] are valuable when:
    *   General models are not good at the task, especially for non-English languages <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
    *   The task is fundamentally different (e.g., protein modeling) <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>.
    *   A really fast, specific model is needed where cost is a major factor (e.g., code completion for free tier users) <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.
    *   It's a cost decision, where upfront investment in pre-training pays for itself quickly through better quality or reduced inference costs <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
*   **"Fuzziness" of AI:** AI's "fuzziness" is both a superpower and a challenge <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>. While techniques like chaining models can push towards higher quality, achieving "perfection" or "five nines of quality" is hard with current technology <a class="yt-timestamp" data-t="00:24:07">[00:24:07]</a>.
*   **Product-Market Fit:** AI has found product-market fit in two main patterns:
    *   Scenarios where outputs don't need to be perfectly "right," such as brainstorming or creative applications <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.
    *   Scenarios where AI-generated answers are costly to produce manually but quick for a human to check, like code co-pilots <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>.
*   **AI Infrastructure Landscape:** Databricks seeks to have all tools available and working well together on one platform, while also partnering with "amazing Point Solutions" from startups to ensure customers have access to the best tools <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>. Acquisitions, like Lilac, happen when a product is amazing and aligns well with Databricks' offerings <a class="yt-timestamp" data-t="00:34:52">[00:34:52]</a>.
*   **Future Focus:** Databricks' priorities include [[ai_model_evaluation_and_benchmarking | evaluation creation]], navigating fine-tuning versus RAG, and developing compound AI systems to connect various pieces and make raw material useful to customers <a class="yt-timestamp" data-t="00:37:13">[00:37:13]</a>. He believes the [[open_source_ai_models_and_limitations | open-source model world]] is "exceedingly well covered," so Databricks focuses on other gaps <a class="yt-timestamp" data-t="00:38:29">[00:38:29]</a>.

## Policy and Trust in AI
Frankle emphasizes that AI experts "owe it to society" to participate in policy conversations, not just with self-interest, but to ensure responsible use <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>. Key policy considerations include:
*   **Determining Use Cases:** Society needs to decide when to allow AI systems and when not to, especially in high-stakes contexts like law enforcement, medicine, or autonomous vehicles where mistakes can have severe consequences <a class="yt-timestamp" data-t="00:55:19">[00:55:19]</a>.
*   **Standards for AI vs. Humans:** Holding AI to rigorous standards often reveals that human performance is also lacking, potentially leading to improved standards for both <a class="yt-timestamp" data-t="00:27:31">[00:27:31]</a>.
*   **Transparency and Honesty:** Building trust in the AI industry requires honesty about capabilities and limitations, clearly stating what is known and unknown <a class="yt-timestamp" data-t="00:57:52">[00:57:52]</a>.

## Areas of Interest
*   **Robotics/Embodied Systems:** While not "underexplored," Frankle is excited about the potential of robotics to perform unscalable tasks and interact with the physical world, similar to how digital technology interacts with the information world <a class="yt-timestamp" data-t="00:58:53">[00:58:53]</a>.
*   **AI for Smell (Osmo AI):** Highlighted as a "truly creative" application where AI is enabling new possibilities in unexpected domains <a class="yt-timestamp" data-t="00:48:06">[00:48:06]</a>.
*   **Human-AI Interaction (HCI):** This is a field where Databricks is seeking expertise <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.
*   **Data Annotation:** Essential for AI, requiring significant expertise and trust in partners like SuperAnnotate and Surge <a class="yt-timestamp" data-t="00:51:18">[00:51:18]</a>.
*   **[[experimentation_in_ai_and_data_science | Experimentation]] with New Products:** Frankle appreciates companies like Anthropic for their willingness to take risks and experiment with new AI-driven products <a class="yt-timestamp" data-t="00:46:04">[00:46:04]</a>.

Frankle concludes that Databricks is the "nexus" of science, policy, and society in AI, being on the ground floor to observe how AI is applied to "most economically useful tasks" across its 12,000 customers <a class="yt-timestamp" data-t="01:01:04">[01:01:04]</a>.