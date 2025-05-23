---
title: Challenges and advancements in AI training techniques
videoId: Wo95ob_s_NI
---

From: [[dwarkesh | The Dwarkesh Podcast]]

This article summarizes insights from John Schulman, co-founder of OpenAI and leader of the post-training team, on the current state and future of AI model training, focusing on the distinctions between pre-training and post-training, emerging advancements, and persistent challenges.

## Understanding Pre-training and Post-training

AI model development involves distinct phases of training, primarily pre-training and post-training (or fine-tuning). 

### Pre-training
Pre-training is the initial phase where models learn foundational knowledge and capabilities.
*   **Objective**: To imitate the vast content available on the internet, including websites and code <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. The model learns to predict the next "token" (words or parts of words) given previous tokens <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This is framed as maximizing the log probability of the data <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   **Outcome**: A "base model" that can generate content resembling random web pages and assign probabilities to various outputs, making it well-calibrated <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. This model can adopt numerous "personas" or generate diverse content types <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### Post-training (Fine-tuning)
Post-training refines the base model for specific applications and desired behaviors.
*   **Objective**: To target a narrower range of behaviors, often aiming for a helpful chat assistant persona <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The optimization shifts from imitating web content to producing outputs that humans find useful and preferable <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Techniques**: Reinforcement Learning from Human Feedback (RLHF) is a key method, where the model is trained to produce responses that are judged favorably by humans <a class="yt-timestamp" data-t="00:28:12">[00:28:12]</a>, <a class="yt-timestamp" data-t="00:31:15">[00:31:15]</a>. [You can read more about Reinforcement Learning strategies in AI here](reinforcement_learning_from_human_feedback_rlhf).
*   **Impact**: Post-training significantly improves model performance. For instance, the current GPT-4's Elo score is about 100 points higher than the original released version, largely due to post-training efforts focusing on data quality, quantity, iterations, and annotation types <a class="yt-timestamp" data-t="00:51:35">[00:51:35]</a>, <a class="yt-timestamp" data-t="00:51:58">[00:51:58]</a>.

## Advancements and Future Directions

### Long-Horizon Tasks
A key area of development is enabling models to perform tasks requiring coherence over extended periods.
*   **Current Limitation**: Models can work coherently for short durations (e.g., five minutes) but struggle with tasks a human might take an hour or more to complete <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   **Future Capability**: Models could carry out entire coding projects, taking high-level instructions, writing files, testing, and iterating <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Enablers**: This will likely come from training models on harder, longer tasks using techniques like Reinforcement Learning (RL) or supervising final outputs/each step <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>, <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. Improved ability to recover from errors and handle edge cases is also crucial <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Learning during Long Tasks**: For tasks with many steps, models will need learning and memory that update during the task itself <a class="yt-timestamp" data-t="00:37:55">[00:37:55]</a>. [Exploring the potential of AI in long-duration tasks has parallels in the field of large language models and their potential](large_language_models_and_transfer_learning).

### Generalization and Sample Efficiency
Improving how models generalize from training data and learn efficiently is critical.
*   **Stronger Generalization**: More capable models can generalize from fewer examples. For instance, a small amount of data (e.g., ~30 examples) helped ChatGPT understand its limitations (like not being able to send emails), and this generalized to capabilities it wasn't explicitly trained on <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>, <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
*   **Cross-Lingual Transfer**: Fine-tuning an assistant on English data can lead to reasonable behavior in other languages like Spanish, where the model adopts the helpful persona across languages <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
*   **Multimodal Transfer**: Text-only fine-tuning can result in reasonable behavior with images <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.
*   **Sample Efficiency in Error Correction**: Better models will require less data to learn how to recover from errors, generalizing from a small amount of data or pre-existing knowledge <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>, <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. [Find out more about challenges and efficiency improvements in AI models](challenges_and_methodologies_in_ai_training_and_data_usage).

### Enhanced Reasoning
Improving reasoning involves both training-time and test-time computation.
*   **Approaches**:
    1.  Training the model to learn from its outputs over many potential "trains of thought," reinforcing paths that lead to correct answers <a class="yt-timestamp" data-t="00:31:37">[00:31:37]</a>.
    2.  Utilizing significant compute at inference time, allowing the model to "talk to itself" during deployment <a class="yt-timestamp" data-t="00:31:51">[00:31:51]</a>.
*   **Optimal Strategy**: A combination of training-time practice and test-time step-by-step computation is expected to yield the best results <a class="yt-timestamp" data-t="00:32:36">[00:32:36]</a>. [The role of reasoning in AI models is evolving with new advancements](reasoning_in_ai_models).

### "Middle Ground" Learning and Introspection
There's a recognized gap between large-scale, static pre-training and transient in-context learning.
*   **Current Gap**: Models lack a mechanism for medium-term memory or deliberate, active learning that persists beyond a single interaction but is more focused than pre-training <a class="yt-timestamp" data-t="00:34:33">[00:34:33]</a>, <a class="yt-timestamp" data-t="00:36:14">[00:36:14]</a>.
*   **Future Systems**: Expected to incorporate online learning, introspection (understanding their own knowledge gaps), and active knowledge seeking <a class="yt-timestamp" data-t="00:37:09">[00:37:09]</a>. This capability might naturally arise from models' existing calibration about what they know and don't know <a class="yt-timestamp" data-t="00:38:54">[00:38:54]</a>.

### Role of Post-Training Compute
The proportion of compute dedicated to post-training is likely to increase.
*   **Rationale**: Model-generated outputs can be of higher quality than much web content, making it beneficial for models to "think by itself" <a class="yt-timestamp" data-t="00:50:57">[00:50:57]</a>. Significant gains have already been achieved through post-training <a class="yt-timestamp" data-t="00:51:22">[00:51:22]</a>. [Read about the role of compute in AI development and its future but complex impacts](role_of_compute_in_ai_development).

### Multimodality and User Interaction
Models are expected to interact with a wider range of data types and user interfaces (UIs).
*   **Interacting with Human UIs**: Models will likely use vision to interact with websites designed for humans <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. Specialized UIs for AIs might emerge, possibly favoring text-based representations <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Proactive Assistance**: The goal is to move from one-off queries to AI assistants that understand the context of ongoing projects, share everyday work, and even proactively make suggestions <a class="yt-timestamp" data-t="01:34:36">[01:34:36]</a>, <a class="yt-timestamp" data-t="01:35:03">[01:35:03]</a>. [Read more about future AI personalization and repurposing](future_of_ai_interaction_in_everyday_life_and_personalization).

## Challenges and Bottlenecks

### Current Model Weaknesses
Despite progress, models exhibit several limitations.
*   **Cognitive Deficits**: Beyond long-term coherence, models struggle to "think hard" about problems or consistently pay attention to user requests <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>.
*   **Nuance and Ambiguity**: For complex tasks like research, models may lack "taste" or the ability to deal with ambiguity effectively <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Practical Limitations**: Affordances, such as interacting with UIs or the physical world, remain mundane barriers <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. [Challenges in AI interaction present limitations yet opportunities for AI advancement as well](challenges_and_opportunities_in_deploying_ai_at_scale).

### RLHF and Model Persona
RLHF can lead to certain stylistic artifacts in model responses.
*   **"Chatbot Voice"**: Models often develop a formal, somewhat dull way of speaking, frequently using bullet points or specific words like "delve" <a class="yt-timestamp" data-t="01:20:51">[01:20:51]</a>.
*   **Contributing Factors**:
    *   **User Preferences**: Some traits, like bullet points, are genuinely preferred by users <a class="yt-timestamp" data-t="01:22:44">[01:22:44]</a>.
    *   **Unintentional Distillation**: Labelers might use other AI models to help generate responses, leading to convergence of styles <a class="yt-timestamp" data-t="01:22:10">[01:22:10]</a>.
    *   **Labeling Bias**: Training on one message at a time can favor more verbose, comprehensive answers over shorter, interactive ones or clarifying questions <a class="yt-timestamp" data-t="01:23:42">[01:23:42]</a>. The perceived speed of output also influences verbosity preference <a class="yt-timestamp" data-t="01:24:13">[01:24:13]</a>.
*   **Efforts to Improve**: OpenAI is actively working to make model writing more lively and fun <a class="yt-timestamp" data-t="01:21:27">[01:21:27]</a>.

### Data Limitations and Generalization
The availability and utility of training data pose ongoing questions.
*   **The "Data Wall"**: There's a hypothesis that progress might plateau if models cannot generalize well beyond their pre-training data <a class="yt-timestamp" data-t="00:54:07">[00:54:07]</a>. Schulman believes it's premature to conclude this based on the time since GPT-4's release, though data limitations are a challenge <a class="yt-timestamp" data-t="00:55:25">[00:55:25]</a>. [For more on data limitations and generalization challenges:](data_center_energy_requirements_and_scaling)
*   **Studying Generalization**: Conducting ablation studies on large models (e.g., GPT-4 size) to understand cross-modal transfer (like code to language reasoning) is difficult and costly <a class="yt-timestamp" data-t="00:56:19">[00:56:19]</a>. Results from smaller models might not extrapolate, as larger models may learn better shared representations <a class="yt-timestamp" data-t="00:57:20">[00:57:20]</a>.
*   **Domain Expertise in Labeling**: It's not always necessary to have labelers with deep domain expertise for every task (e.g., using FFmpeg). The base model's pre-training on documentation and code provides a strong foundation, and general helpfulness training can transfer to specific domains <a class="yt-timestamp" data-t="01:32:10">[01:32:10]</a>, <a class="yt-timestamp" data-t="01:32:54">[01:32:54]</a>.

### Safety and Alignment with Rapid Progress
The prospect of Artificial General Intelligence (AGI) arriving sooner than expected necessitates careful planning.
*   **Precautionary Measures**: If AGI seemed imminent, measures would include slowing down training and deployment, ensuring robust sandboxing, and careful evaluation <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>, <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.
*   **Coordination**: Agreement among major AI labs on deployment limits or further training would be crucial to avoid compromising safety in a competitive race <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>, <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>. [AI safety and alignment research is crucial for future AI advancements](ai_alignment_and_safety_research).
*   **Preferred Approach**: A continuous release of incrementally better and safer models is favored over a large buildup of "potential energy" from a sudden breakthrough <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>.
*   **Instrumental Convergence**: A concern that models might pursue undesirable intermediate goals (like "taking over the world") to achieve a benign final objective (like "coding an app") <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>. This is considered less likely for well-specified tasks than for vague goals like "make money" <a class="yt-timestamp" data-t="00:29:24">[00:29:24]</a>.
*   **Model Spec**: OpenAI is releasing a "Model Spec" document detailing desired model behavior and how to handle conflicting stakeholder interests (end-user, developer, platform, broader humanity) <a class="yt-timestamp" data-t="01:12:16">[01:12:16]</a>, <a class="yt-timestamp" data-t="01:12:43">[01:12:43]</a>.

### Understanding Scaling Laws
The reasons why larger models are often more sample-efficient are not fully understood.
*   **Parameter Count**: No definitive explanation exists for the scaling law with parameter count <a class="yt-timestamp" data-t="00:58:16">[00:58:16]</a>.
*   **Hypothetical Explanation**: Larger models have more capacity and might act as an ensemble of many computational "circuits" operating in parallel. With more such circuits, there's a higher chance that some will "luckily" guess correctly and be upweighted, effectively providing a larger "library" of computations to draw from <a class="yt-timestamp" data-t="00:58:43">[00:58:43]</a>, <a class="yt-timestamp" data-t="00:59:38">[00:59:38]</a>, <a class="yt-timestamp" data-t="01:00:57">[01:00:57]</a>.

### The "Moat" of Post-Training Expertise
Developing effective post-training capabilities creates a competitive advantage.
*   **Complexity**: Post-training is a complex operation requiring skilled personnel, tacit knowledge, and organizational expertise <a class="yt-timestamp" data-t="01:27:47">[01:27:47]</a>.
*   **Concentration**: Companies with serious pre-training efforts tend to also have serious post-training efforts <a class="yt-timestamp" data-t="01:28:45">[01:28:45]</a>. [Read more about challenges and opportunities in AI scalability](ai_scalability_and_breakthroughs).
*   **Mitigating Factors**: The "moat" can be somewhat reduced by techniques like model distillation or using one model's outputs to train another, though larger players tend to avoid this <a class="yt-timestamp" data-t="01:29:06">[01:29:06]</a>.

## Conclusion
AI training is a dynamic field characterized by a symbiotic relationship between broad pre-training and targeted post-training. Future advancements hinge on enabling models to tackle longer, more complex tasks, generalize more effectively from less data, and develop more nuanced reasoning and introspective capabilities. However, challenges related to model limitations, data constraints, safety, and the very nature of the learning process require ongoing research and careful management, especially as AI systems become increasingly powerful and integrated into society. [Discover more about the impact of AI on future technology and society](impact_of_ai_on_future_technology_and_society).
