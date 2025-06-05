---
title: Innovations in AI training methods and new benchmarks
videoId: U3MVU6JpocU
---

From: [[aidotengineer]] <br/> 

Over the past few years, a significant shift has occurred in the development of reliable AI solutions, moving towards more advanced agentic workflows [00:00:10]. Initially, many companies built AI wrappers, but the landscape changed dramatically as [[advancements_in_ai_model_technology_and_performance | models got better at coding]] and AI adoption skyrocketed [01:11:39].

## The Evolution and Limits of AI Models

The success of AI-powered tools like Cursor AI, which achieved $100 million ARR in 12 months, highlights not just [[advancements_in_ai_model_technology_and_performance | improved models]], but also new techniques for orchestrating these models to work effectively in production [01:01:00]. This orchestration is crucial because there are clear limits to model performance; issues like hallucinations and overfitting persist, and developers require more structured outputs [01:38:00].

For years, making [[advancements_in_ai_model_technology_and_performance | models bigger and fitting them more data]] led to smarter AI [02:01:83]. However, this approach eventually "hit a wall," with [[advancements_in_ai_model_technology_and_performance | improvements slowing down]] despite additional data, as [[advancements_in_ai_model_technology_and_performance | models reached their limits]] on existing tests [02:06:00]. This led to the exploration of new avenues and [[data_collection_and_training_techniques_for_ai_models | new training methods]] [02:24:26].

## New Training Methods Pushing the Field Forward

In recent months, new [[data_collection_and_training_techniques_for_ai_models | training methods]] have emerged that are advancing the field [02:38:48]:
*   **Deep Seek R1 Model** The Deep Seek R1 model is notable as the first model [[data_collection_and_training_techniques_for_ai_models | trained without using any labeled data]] [02:45:30]. This method is referred to as "real reinforcement learning," meaning the model learned on its own [02:49:50]. This approach was reportedly used by OpenAI to train their reasoning models like 01 and 03 [02:57:97].
*   **Chain of Thought Thinking** Modern reasoning models utilize Chain of Thought thinking at inference or response time to generate answers [03:03:00]. This allows models to "think" before providing an answer, enabling them to solve more complex reasoning problems [03:12:00].

Additionally, model providers are enhancing their models with more capabilities, such as tool use, improved research capabilities, and near-perfect OCR accuracy (e.g., Gemini 2.0 Flash) [03:24:00].

## The Need for New Benchmarks

As [[advancements_in_ai_model_technology_and_performance | models get better]] and the field progresses, [[challenges_and_trust_issues_with_ai_benchmarks | traditional benchmarks have become saturated]] [03:41:20]. Consequently, new benchmarks are being introduced to [[improving_ai_evaluation_methods | capture the performance of these new reasoning models]] [03:44:80]. For example, the Humanities Last Last Exam measures performance on truly difficult tasks, where even the latest smart models still struggle [03:52:04].

## Beyond Models: The Importance of Building Around AI

Ultimately, for an AI product to work effectively in production, success extends beyond just the models themselves; it hinges on "how you build around it" [04:10:95]. This involves evolving parallel to model training by learning to prompt models better and developing advanced techniques like Chain of Thought [04:20:00]. Other crucial advancements include:
*   **Retrieval-Augmented Generation (RAG)**: Grounding model responses with proprietary data [04:31:00].
*   **Memory**: Essential for multi-threaded conversations and capturing context in long interactions [04:42:00].
*   **Long Context Models**: Enabling new use cases with extended context windows [04:47:00].
*   **Graph RAG**: Experimenting with hierarchical responses [04:52:00].
*   **Agentic RAG**: Making workflows more powerful and autonomous [05:12:00].

While the field is still evolving, these techniques are critical. Deep understanding of the problem and a test-driven development approach are essential to find the right combination of techniques, models, and logic for a specific use case [05:22:00]. This approach involves continuous experimentation, evaluation, deployment, and monitoring to continuously improve the product for customers [05:52:00].