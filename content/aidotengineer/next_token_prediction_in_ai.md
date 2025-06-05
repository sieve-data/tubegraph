---
title: Next token prediction in AI
videoId: 1XvN5EBDnDw
---

From: [[aidotengineer]] <br/> 

Next token prediction is one of two key [[future_directions_in_ai_model_training_and_scaling | scaling paradigms]] that have emerged in [[evolution_of_ai_models_and_their_application | AI research]] over recent years, particularly between 2020 and 2021 <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a> <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. This paradigm is also commonly referred to as "pre-training" <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

## How it Works
At its core, next token prediction operates as a "world-building machine" <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. The model learns to comprehend the world by predicting the subsequent word or token in a sequence <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. This learning is based on the fundamental principle that certain sequences are caused by initial actions and are irreversible <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. By predicting what comes next, the model inherently learns the physics of the world <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

The tokens used for pre-training can be diverse, including strings, words, or pixels <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. To accurately predict the next token, the model must develop an understanding of how the world functions <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

## Multitask Learning
Next token prediction can be viewed as a massive multitask learning process <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. During pre-training, some tasks are relatively easy for the model to learn, such as:
*   **Translation:** For example, learning that "boarding" in French translates to "embarquement" <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Factual Knowledge:** Understanding general world facts like "the capital of France is Paris" <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. This information is often readily available and prevalent on the internet, making it easier for the model to absorb <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## The Importance of Compute
Scaling compute during the pre-training stage is crucial because it allows the model to learn a class of tasks that are inherently more challenging <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. These difficult tasks include:
*   **Physics and Problem Solving:** The model learns about physics, problem-solving, generation, and logical expressions <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Spatial Reasoning:** While not yet perfect, models also learn some spatial reasoning <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Math:** Tasks requiring computation, such as complex math problems, demand significant compute for the model to derive the correct next token prediction <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This often necessitates techniques like Chain of Thought to aid in reasoning <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **Creative Writing:** This is exceptionally difficult for models. While they can predict writing style, creative writing involves world-building, storytelling, and maintaining plot coherence <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. It's much easier for a model to make a prediction error that deteriorates the plot <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Measuring "good" creative writing is also an open research problem, and enabling models to invent new forms of writing or create coherent novels over long periods remains a significant challenge <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

## Transition to Post-Training and Agents
The era of 2020-2021 saw significant scaling of pre-training at organizations like Anthropic and OpenAI <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Products like GitHub Copilot, which leveraged the model's pre-trained knowledge of code for autocomplete features, emerged from this paradigm <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. Researchers then applied techniques like Reinforcement Learning from Human Feedback (RLHF) and Reinforcement Learning from AI Feedback (RLAF) in a "post-training" stage to refine the model's usefulness <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a> <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. This post-training teaches models to complete functions, understand docstrings, generate multi-line completions, and apply diffs <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

Next token prediction forms the foundation upon which more advanced [[evolution of AI models and their application | AI models]] and [[the_impact_and_future_potential_of_ai_and_agents | agents]] are built, particularly those capable of highly complex reasoning through techniques like Chain of Thought and the use of real-world tools <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.