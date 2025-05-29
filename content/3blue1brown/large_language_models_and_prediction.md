---
title: Large language models and prediction
videoId: LPZh9BOjkQs
---

From: [[3blue1brown]] <br/> 

Large Language Models (LLMs) are sophisticated mathematical functions designed primarily to predict the next word in any given piece of text <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Instead of predicting a single word with certainty, an LLM assigns a probability to all possible next words <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## How LLMs Function as Chatbots

When interacting with a chatbot, the underlying [[generative_pretrained_transformers | large language model]] is continuously predicting the next word <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This process involves:
1.  Laying out text describing an interaction between a user and a hypothetical AI assistant <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
2.  Adding the user's input as the initial part of the interaction <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
3.  Having the model repeatedly predict the next word that such a hypothetical AI assistant would say in response <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

To make the output more natural, the model is often allowed to select less likely words randomly <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. This means that even though the model itself is deterministic, a specific prompt can yield a different answer each time it's run <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## The [[training_process_of_language_models | Training Process]]

LLMs learn to make these predictions by processing an enormous amount of text, typically sourced from the internet <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. For instance, [[parameters_and_architecture_of_models_like_gpt3 | GPT-3]] was trained on an amount of text that would take a human over 2600 years to read non-stop, and newer models train on even more data <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. The behavior of a language model is entirely determined by its many continuous values, known as [[parameters_and_architecture_of_models_like_gpt3 | parameters]] or weights <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. "Large" in "[[generative_pretrained_transformers | large language model]]" refers to the fact that these models can have hundreds of billions of these [[parameters_and_architecture_of_models_like_gpt3 | parameters]] <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Pre-training
No human explicitly sets these [[parameters_and_architecture_of_models_like_gpt3 | parameters]]; instead, they begin at random and are repeatedly refined through many example pieces of text <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. The refinement process works by:
1.  Passing all but the last word from a training example into the model <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
2.  Comparing the model's prediction with the true last word from the example <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
3.  Using an algorithm called backpropagation to tweak all [[parameters_and_architecture_of_models_like_gpt3 | parameters]], making the model more likely to choose the true word and less likely to choose others <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

When this process is applied to trillions of examples, the model not only becomes more accurate on [[importance_of_training_data_in_machine_learning | training data]] but also develops the ability to make reasonable predictions on text it has never encountered <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. This entire process is called pre-training <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

### [[computation_and_infrastructure_for_training_language_models | Computational Scale]]
The [[computation_and_infrastructure_for_training_language_models | scale of computation]] required for [[training_process_of_language_models | training]] a [[generative_pretrained_transformers | large language model]], given its immense number of [[parameters_and_architecture_of_models_like_gpt3 | parameters]] and vast [[importance_of_training_data_in_machine_learning | training data]], is astounding <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. Performing all the operations involved in [[training_process_of_language_models | training]] the largest LLMs would take well over 100 million years, even at a rate of a billion additions and multiplications per second <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. This is only possible due to special computer chips optimized for parallel operations, known as GPUs <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Reinforcement Learning with Human Feedback
Pre-training's goal of auto-completing random text differs from the goal of being a helpful AI assistant <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. To bridge this gap, chatbots undergo an additional [[training_process_of_language_models | training]] phase called reinforcement learning with human feedback <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. During this phase, human workers flag unhelpful or problematic predictions, and their corrections further adjust the model's [[parameters_and_architecture_of_models_like_gpt3 | parameters]], making it more likely to generate responses users prefer <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

## [[Neural Networks and Transformers | Transformers]]

Prior to 2017, most language models processed text word by word <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. However, a team at Google introduced the [[transformers_and_attention_in_language_models | Transformer]] model, which changed this paradigm <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. [[transformers_and_attention_in_language_models | Transformers]] process text in parallel, soaking it all in at once <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### Key Operations within a Transformer
1.  **[[token_embeddings_and_highdimensional_vectors | Token Embeddings]]:** The first step is to associate each word with a long list of numbers, also known as [[token_embeddings_and_highdimensional_vectors | high-dimensional vectors]] <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. This is necessary because the [[training_process_of_language_models | training process]] only works with continuous values, so language must be encoded numerically, with these lists of numbers encoding the meaning of the corresponding word <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
2.  **[[transformers_and_attention_in_language_models | Attention]]:** [[transformers_and_attention_in_language_models | Transformers]] uniquely rely on a special operation called [[transformers_and_attention_in_language_models | attention]] <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. This operation allows these lists of numbers (word embeddings) to "talk to one another" in parallel and refine their encoded meanings based on the surrounding context <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. For example, the numbers encoding the word "bank" might change based on context to specifically encode "riverbank" <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
3.  **Feed-Forward [[Neural Networks and Transformers | Neural Network]]:** [[transformers_and_attention_in_language_models | Transformers]] also include a second type of operation: a feed-forward [[Neural Networks and Transformers | neural network]] <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. This provides the model with additional capacity to store patterns about language learned during [[training_process_of_language_models | training]] <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

Data repeatedly flows through many iterations of these two fundamental operations. The goal is that each list of numbers becomes enriched to encode the information necessary for an accurate next-word prediction <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. At the end, a final function is performed on the last vector, which has been influenced by all context from the input text and the model's learned knowledge, to produce a probability prediction for every possible next word <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Emergent Behavior and Challenges

While researchers design the framework for how these steps work, the specific behavior of LLMs is an emergent phenomenon, arising from how the hundreds of billions of [[parameters_and_architecture_of_models_like_gpt3 | parameters]] are tuned during [[training_process_of_language_models | training]] <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. This makes it incredibly challenging to determine precisely why a model makes certain predictions <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. However, when [[generative_pretrained_transformers | large language model]] predictions are used for autocompletion, the generated words are remarkably fluent, fascinating, and useful <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.