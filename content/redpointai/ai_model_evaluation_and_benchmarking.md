---
title: AI model evaluation and benchmarking
videoId: ZEi4OTuFa3I
---

From: [[redpointai]] <br/> 

Percy Liang, a leading AI researcher and co-founder of Together AI, provides insights into the current state and future of [[ai_evaluation_and_benchmarking | AI model evaluation]]. He emphasizes the evolving challenges and new approaches required as AI models become more capable and complex <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.

## Current State of Evaluations

Liang notes that [[ai_evaluation_and_benchmarking | AI model evaluation]] has become significantly more complex than in the past, where a simple train/test split was sufficient <a class="yt-timestamp" data-t="00:30:15">[00:30:15]</a>.

### Challenges in Evaluation
*   **Train-Test Overlap**: A major problem is the lack of transparency regarding training data, making it difficult to trust evaluation results and determine if models were inadvertently trained on test sets <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>. Companies are often unwilling to disclose this information <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.
*   **Raw Benchmarks vs. Real-World Use**: Simply looking at raw benchmark scores may not tell the full story, especially when models are integrated into larger systems. Compatibility issues can lead to unimpressive overall performance, even if a model improves on specific subtasks <a class="yt-timestamp" data-t="00:44:09">[00:44:09]</a>.
*   **Monotonic Progress**: The assumption of monotonic progress (models always getting better) is challenged when models don't fit into existing system architectures <a class="yt-timestamp" data-t="00:54:30">[00:54:30]</a>.
*   **Multi-dimensional Assessment**: [[ai_model_selection_and_evaluation_for_businesses | AI model selection and evaluation for businesses]] must consider various facets like cost, speed, accuracy, and customizability, not just a single "better" metric <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

### New Benchmarks and Approaches
Liang's team has developed new benchmarks to address current challenges:
*   **SideBench**: A Capture the Flag cyber security exercise benchmark that requires complex multi-step reasoning. The hardest challenges take human teams over 24 hours to solve, while current models can only solve those initially solved by humans in around 11 minutes <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   **ML Agent Bench**: Designed for solving machine learning research tasks <a class="yt-timestamp" data-t="00:47:44">[00:47:44]</a>.
*   **HELM (Holistic Evaluation of Language Models)**: Initially a manual framework covering various aspects of language models, it has evolved to support different "verticals" or domains, such as safety evaluations, specific languages, medical applications, and finance <a class="yt-timestamp" data-t="00:34:42">[00:34:42]</a>.

## Evolution of Evaluation Methodologies

### AI Evaluating AI
As models become increasingly capable, the field is moving towards using language models themselves to benchmark other language models. This is crucial because it's nearly impossible for humans to comprehensively test models that claim to "do anything" <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>.

*   **AutoBencher**: A system that leverages language models to automatically generate diverse inputs for evaluation. It uses an asymmetry where the question-generating model has information unknown to the test-taker, enabling more sensible evaluations <a class="yt-timestamp" data-t="00:32:13">[00:32:13]</a>.

### Beyond Superficial Judgments
Liang advocates for more structured and concrete [[evaluation_methodologies_and_user_feedback_for_ai_models | evaluation methodologies]].
*   **Rubrics**: Similar to grading exams, using rubrics can anchor evaluations in objective terms, moving beyond subjective "is this good?" assessments <a class="yt-timestamp" data-t="00:33:42">[00:33:42]</a>.
*   **Vertical-Specific Benchmarks**: There's a growing need for benchmarks tailored to specific industries or tasks, rather than general "cutting-edge math problems." For example, a model for diagnosing medical images would require a different benchmark than one for general reasoning <a class="yt-timestamp" data-t="00:34:31">[00:34:31]</a>.

## Role of Academia and Transparency

Academia plays a unique role in [[ai_evaluation_and_benchmarking | AI model evaluation]] and auditing due to its lack of commercial interests <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>.
*   **Orthogonal Research**: Academic research should focus on areas that are enhanced by or irrelevant to the progress of large, resource-rich labs like OpenAI. This includes novel use cases of language models (like generative agents) or developing benchmarks <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Open Science**: Academia should prioritize contributing to the [[open_source_ai_models_and_limitations | open source AI models and limitations]] community by creating and publicly sharing knowledge, including insights into data quality and weighting for pre-training <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
*   **Transparency and Auditing**: Academia is uniquely positioned to assess the transparency of different AI providers, a task difficult for commercial entities <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. Regulation should emphasize transparency and disclosure to help policymakers, researchers, and third-party auditors understand risks and benefits <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>.

## Connection to Interpretability

[[ai_production_and_evaluation_techniques | AI production and evaluation techniques]] are closely tied to interpretability, especially for regulated industries like finance and healthcare <a class="yt-timestamp" data-t="00:35:36">[00:35:36]</a>.
*   **Challenges**: Interpretability has become harder because access to model weights and training data is often withheld <a class="yt-timestamp" data-t="00:36:28">[00:36:28]</a>.
*   **Attribution**: Techniques like influence functions aim to attribute model predictions to specific training examples <a class="yt-timestamp" data-t="00:37:38">[00:37:38]</a>.
*   **Explanations**: While models can generate "Chain of Thought" explanations, research shows these don't always reflect what's truly happening internally <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>.
*   **Future**: Transparency from [[open_source_ai_models_and_limitations | open source AI models and limitations]] that show their internal steps (like OpenAI's 01 model) could potentially aid interpretability, making it easier to explain how a result was derived <a class="yt-timestamp" data-t="00:39:34">[00:39:34]</a>.

## Future Milestones

Significant milestones in AI model capability include:
*   **Solving Open Math Problems**: Achieving solutions to currently unsolved mathematical problems <a class="yt-timestamp" data-t="00:48:22">[00:48:22]</a>.
*   **Extending Human Knowledge**: Developing AI that can genuinely discover new research or solve problems humans haven't <a class="yt-timestamp" data-t="00:48:51">[00:48:51]</a>.
*   **Zero-Day Exploits**: In cybersecurity, finding a zero-day vulnerability would be a significant game-changer <a class="yt-timestamp" data-t="00:49:12">[00:49:12]</a>.

Liang believes that AI is still rapidly progressing, with qualitative changes like new approaches to using systems (e.g., agentic models) driving progress alongside quantitative scaling <a class="yt-timestamp" data-t="00:49:26">[00:49:26]</a>.