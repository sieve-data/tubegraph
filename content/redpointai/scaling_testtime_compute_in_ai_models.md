---
title: Scaling testtime compute in AI models
videoId: atMRWzgHEGg
---

From: [[redpointai]] <br/> 

Scaling [[the_role_of_testtime_compute_in_ai_models | test-time compute]] in AI models is a significant area of focus, especially for models like Google's Gemini LLMs [00:00:39]. Discussions with experts like Nnoma Gome shazir and Jack Ray highlight its potential and limitations [00:00:57].

## Understanding Test-Time Compute

Initially, efforts to build [[the_role_of_testtime_compute_in_ai_models | test-time compute]] capabilities into Gemini models concentrated on reasoning tasks such as math and code [00:02:44]. A surprising discovery was the generalization of "thinking" beyond these specific reasoning tasks to improve creative outputs, like composing essays [00:02:59]. Models trained with "thinking" and refined for style produced creative work with enjoyable thought content and revisions [00:03:16].

A key aspect of [[the_role_of_testtime_compute_in_ai_models | test-time compute]] is the model's ability to "think" or process information internally before generating a final response [00:12:32]. While this can introduce a slight latency of a couple of seconds, users find the improved quality of the answer a small price to pay [00:12:43]. This "thinking" process, where models go through various ideas and revisions, has been observed to enhance engagement, even with complex philosophical questions like "what is the meaning of life" [00:13:17].

## Advantages and Economic Considerations

One of the significant advantages of [[the_role_of_testtime_compute_in_ai_models | test-time compute]] is its cost-effectiveness. Large Language Model (LLM) searches are extremely cheap, with operations costing less than 10^-18 dollars [00:19:58]. Users can get over a million tokens per dollar, which is orders of magnitude cheaper than reading a paperback book or paying for human labor [00:20:19]. This massive margin allows for the application of more compute at inference time to make models smarter [00:21:14].

By applying more compute at inference time through techniques like Chain of Thought thinking or other algorithms, a new [[scaling_ai_models_and_test_time_compute | scaling curve]] is emerging [00:22:30]. This approach also leads to significant improvements in data efficiency by training models to think deeply with reinforcement learning when solving tasks [00:24:48].

## Infrastructure and Hardware Needs

The shift towards AI development becoming primarily an inference problem means that infrastructure needs will change significantly from the large batch [[pretraining_and_finetuning_ai_models | pre-training]] paradigm [00:01:02, 00:18:00, 00:18:11]. [[advancements_in_ai_model_infrastructure_for_testtime_compute | Test-time compute]] allows for greater flexibility in compute distribution, potentially spreading model training across many different data centers without requiring very strong, fast interconnects [00:07:09]. This distributed nature can further drive down costs [00:07:30].

However, [[hardware_and_compute_scalability_challenges_in_ai | hardware challenges]] remain. Inference can lose a lot of the parallelism inherent in the Transformer architecture, often becoming memory bound when looking at attention keys and values for every generated token [01:08:04]. Ongoing research aims to address this from both model architecture and hardware perspectives to fully apply massive computational power to inference [01:08:30]. Companies like Google leverage co-design links with their TPU team to feed them compute profiles, allowing them to tweak chip and data center designs for future needs [01:07:41].

## The Path to AGI and Novel Thought

While [[the_role_of_testtime_compute_in_ai_models | test-time compute]] is highly promising, it is not expected to lead directly to Artificial General Intelligence (AGI) on its own [00:23:31]. Other crucial components, such as the ability to act in complex environments and research into acting agents, are also required [00:23:36].

The debate continues on whether current models can have truly novel thoughts or merely interpolate known ideas [00:29:00]. While some scientific discoveries involve associating disjoint pieces of information, accelerating science through better association is a form of interpolation that still leads to new properties [00:28:25]. The ability for models to ask novel questions, particularly in open-ended fields like mathematics, is seen as the hardest part of the challenge, with solving existing problems being a more confident path [00:31:38].