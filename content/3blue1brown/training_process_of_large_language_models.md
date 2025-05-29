---
title: Training process of large language models
videoId: LPZh9BOjkQs
---

From: [[3blue1brown]] <br/> 

A [[large_language_models_and_their_function | large language model]] (LLM) is a sophisticated mathematical function designed to predict the next word in any given piece of text <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Instead of predicting a single word with certainty, an LLM assigns a probability to all possible next words <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. When interacting with a chatbot, this predictive process occurs repeatedly to complete the dialogue <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. The output appears more natural if the model is allowed to randomly select less likely words, meaning a specific prompt can produce different answers each time, even though the model itself is deterministic <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## How LLMs Learn: Pre-training

[[Large language models and their function | LLMs]] learn to make predictions by processing an immense volume of text, primarily sourced from the internet <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. For instance, to read the amount of text used to train [[generative_pretrained_transformer_architecture | GPT-3]] non-stop, it would take over 2600 years for a human <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Larger models developed since then require even more data <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. This emphasizes the [[importance_of_training_data_in_machine_learning | importance of training data in machine learning]].

The behavior of a language model is determined by its many continuous values, known as [[role_of_parameter_tuning_in_machine_learning_models | parameters or weights]] <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. The term "large" in [[large_language_models_and_their_function | large language model]] refers to the hundreds of billions of these parameters <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Parameter Refinement

These parameters are not set deliberately by humans; they begin randomly, causing the model to initially output gibberish <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. They are repeatedly refined based on numerous text examples <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. During this refinement:
1.  All but the last word from a training example is fed into the model <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
2.  The model's prediction is compared to the true last word <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
3.  An algorithm called backpropagation is used to adjust the parameters, making the model more likely to choose the correct word and less likely to choose others <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

Performing this process for trillions of examples not only improves accuracy on training data but also enables the model to make reasonable predictions on new, unseen text <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### Computational Scale

The computation involved in training an [[large_language_models_and_their_function | LLM]] is immense, requiring well over 100 million years of operations if one could perform a billion additions and multiplications per second <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. This "pre-training" is made possible by specialized computer chips, like GPUs, which are optimized for parallel operations <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## Reinforcement Learning with Human Feedback (RLHF)

Pre-training primarily focuses on auto-completing random text passages <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. To function effectively as an AI assistant, chatbots undergo a second, equally important training phase called reinforcement learning with human feedback <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. In this phase, human workers flag unhelpful or problematic predictions, and their corrections further adjust the model's parameters to align with user preferences <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

## Role of Transformers

Prior to 2017, most language models processed text sequentially, one word at a time <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. However, the introduction of the [[role_of_transformers_in_language_models | transformer]] model by Google researchers revolutionized this by allowing models to process text in parallel, taking in all information at once <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### Core Operations within a Transformer
*   **Word Embedding**: Each word is associated with a long list of numbers, encoding its meaning, as the training process operates on continuous values <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **[[role_of_transformers_in_language_models | Attention]]**: Unique to [[role_of_transformers_in_language_models | transformers]], this operation enables these numerical lists (embeddings) to interact with each other in parallel, refining their encoded meanings based on context. For example, the numerical representation of "bank" might change to reflect "riverbank" based on surrounding words <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **[[role_of_transformers_in_language_models | Feed-Forward Neural Network]]**: [[role_of_transformers_in_language_models | Transformers]] also include this operation, providing additional capacity to store language patterns learned during training <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

Data flows through many iterations of these two fundamental operations, enriching each numerical list with the information needed to accurately predict the next word <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. Ultimately, a final function processes the last vector in the sequence, producing a probability distribution for every possible next word <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Challenges in Understanding Model Predictions

While researchers design the framework for how each step works, the specific behavior of an [[large_language_models_and_their_function | LLM]] is an emergent phenomenon, stemming from how billions of parameters are tuned during training <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. This makes it incredibly [[challenges_in_understanding_model_predictions | challenging to determine why a model makes the exact predictions that it does]] <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. Despite this complexity, the words generated by [[large_language_models_and_their_function | LLMs]] are uncannily fluent, fascinating, and useful <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.