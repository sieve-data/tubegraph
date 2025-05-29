---
title: Training process of language models
videoId: LPZh9BOjkQs
---

From: [[3blue1brown]] <br/> 

[[large_language_models_and_prediction | Large language models]] (LLMs) are sophisticated mathematical functions that predict the next word for any given piece of text <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Instead of predicting with certainty, they assign probabilities to all possible next words <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. When interacting with a chatbot, this process is continuously repeated to complete the dialogue <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. The output tends to appear more natural if the model is allowed to randomly select less likely words, leading to different answers for the same prompt each time it's run, despite the model itself being deterministic <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

The training of a language model involves two primary stages: pre-training and reinforcement learning with human feedback.

## Pre-training: Learning from Vast Text Data

The initial stage, known as pre-training, focuses on teaching the model to predict the next word by processing an enormous amount of text data, typically sourced from the internet <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

### Scale of Training Data and Computation
The sheer volume of [[importance_of_training_data_in_machine_learning | training data]] is immense; for example, reading the text used to train [[parameters_and_architecture_of_models_like_gpt3 | GPT-3]] nonstop would take a human over 2,600 years, and subsequent larger models train on even more data <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

The behavior of a language model is entirely determined by its many continuous values, known as [[parameters_and_architecture_of_models_like_gpt3 | parameters]] or weights <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. What makes [[large_language_models_and_prediction | large language models]] "large" is that they can contain hundreds of billions of these [[parameters_and_architecture_of_models_like_gpt3 | parameters]] <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

The scale of [[computation_and_infrastructure_for_training_language_models | computation]] required to train an LLM is staggering. If one could perform a billion additions and multiplications every second, training the largest models would still take well over 100 million years <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. This is only made possible by using specialized computer chips, called GPUs, which are optimized for running many operations in parallel <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

### The Learning Process
The training process can be thought of as "tuning the dials" on a large machine <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. No human deliberately sets these [[parameters_and_architecture_of_models_like_gpt3 | parameters]]; instead, they begin at random, causing the model to initially output gibberish <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. They are then repeatedly refined based on numerous example pieces of text <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

For each training example, all but the last word is fed into the model, and its prediction is compared with the true last word <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. An algorithm called backpropagation is used to adjust all of the [[parameters_and_architecture_of_models_like_gpt3 | parameters]] <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. This adjustment makes the model slightly more likely to choose the correct last word and less likely to choose others <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. By repeating this process for many trillions of examples, the model begins to make more accurate predictions on both the [[importance_of_training_data_in_machine_learning | training data]] and text it has never encountered before <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. This refinement process is part of the broader [[neural_network_learning_process | neural network learning process]] <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

### Model Architecture: Transformers
Prior to 2017, most language models processed text one word at a time <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. However, the introduction of the [[transformers_and_attention_in_language_models | Transformer]] model by Google researchers revolutionized this by allowing models to process text in parallel, "soaking it all in at once" <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

Within a [[transformers_and_attention_in_language_models | Transformer]], words are first associated with long lists of numbers, or embeddings, to encode language using continuous values that the training process can work with <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

A key feature of [[transformers_and_attention_in_language_models | Transformers]] is their reliance on [[the_process_of_updating_embeddings_using_attention | attention]], a special operation that allows these lists of numbers to interact and refine their encoded meanings based on context, all done in parallel <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. For instance, the numbers for "bank" might change to reflect "riverbank" based on surrounding words <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. [[transformers_and_attention_in_language_models | Transformers]] also typically include feed-forward neural networks, which provide additional capacity to store language patterns learned during training <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. This data repeatedly flows through many iterations of these operations, enriching the embeddings with information needed for accurate next-word prediction <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

At the end of this process, a final function is applied to the last vector in the sequence, which has been influenced by all context and learned information, to produce a probability prediction for every possible next word <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Reinforcement Learning with Human Feedback (RLHF)

Pre-training's goal of auto-completing random text differs from the goal of being a helpful AI assistant <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. To address this, chatbots undergo a crucial second type of training called reinforcement learning with human feedback <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. In this stage, human workers flag unhelpful or problematic predictions <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. Their corrections further modify the model's [[parameters_and_architecture_of_models_like_gpt3 | parameters]], making it more likely to generate responses preferred by users <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## Emergent Behavior and Challenges

While researchers design the framework for each step, the specific behavior of LLMs is an emergent phenomenon, resulting from how billions of [[parameters_and_architecture_of_models_like_gpt3 | parameters]] are tuned during training <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. This makes it incredibly challenging to determine the exact reasons behind a model's specific predictions <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. Nevertheless, the predictions generated by [[large_language_models_and_prediction | large language models]] are consistently fluent, fascinating, and useful <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.