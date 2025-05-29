---
title: Large language models and their function
videoId: LPZh9BOjkQs
---

From: [[3blue1brown]] <br/> 

Large Language Models (LLMs) are sophisticated mathematical functions designed to predict the next word for any given piece of text <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Instead of providing a single word with certainty, an LLM assigns a probability to all possible next words <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## How Large Language Models Work

When interacting with a chatbot, the underlying process involves an LLM repeatedly predicting the next word to complete a dialogue <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This is achieved by feeding the model existing text and allowing it to predict the subsequent word, then repeating this process with the growing script <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. To make the output appear more natural, LLMs are designed to sometimes select less likely words at random <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. This means that although the model itself is deterministic, a specific prompt can often yield a different answer each time it is run <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## [[training_process_of_large_language_models | Training Process]]

LLMs learn to make predictions by processing an enormous volume of text, typically sourced from the internet <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. For instance, the amount of text used to train GPT-3 would take a human over 2600 years to read non-stop <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Even larger models trained since then utilize significantly more data <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

The behavior of a language model is determined by continuous values known as parameters or weights <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. Changing these [[role_of_parameter_tuning_in_machine_learning_models | parameters]] alters the probabilities the model assigns to the next word for a given input <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. What makes LLMs "large" is that they can possess hundreds of billions of these parameters <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Parameter Refinement

No human explicitly sets these parameters; instead, they begin at random, causing the model to initially output gibberish <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. They are repeatedly refined based on numerous example texts <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. For each training example, all but the last word are fed into the model, and its prediction is compared against the true last word <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. An algorithm called backpropagation is then used to adjust the parameters, making the model more likely to choose the correct word and less likely to choose others <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. Repeating this process for trillions of examples leads to more accurate predictions on training data and reasonable predictions on unseen text <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### Computational Scale

The sheer number of parameters and vast amount of [[training_process_of_large_language_models | training data]] mean the computation involved in training an LLM is immense <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. For example, performing a billion additions and multiplications every second, it would still take over 100 million years to complete the operations needed to train the largest LLMs <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. This scale of computation is made possible by specialized computer chips called GPUs, optimized for parallel operations <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

### Pre-training and Reinforcement Learning with Human Feedback (RLHF)

The initial process of auto-completing random text passages is known as pre-training <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. However, being a good AI assistant requires a different goal. Chatbots undergo a second, crucial type of [[training_process_of_large_language_models | training]] called reinforcement learning with human feedback <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. Here, human workers flag unhelpful or problematic predictions, and their corrections further adjust the model's parameters to align with user preferences <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

## The [[role_of_transformers_in_language_models | Role of Transformers]]

Before 2017, most language models processed text sequentially, one word at a time <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. Google researchers introduced the [[role_of_transformers_in_language_models | transformer]] model, which revolutionized this by processing text all at once, in parallel <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### Core Operations within a Transformer

1.  **Word Embeddings**: The first step involves associating each word with a long list of numbers, known as [[highdimensional_vector_embeddings | high-dimensional vector embeddings]] <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. This is necessary because the [[training_process_of_large_language_models | training process]] operates only with continuous values, encoding language numerically <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. These number lists can somehow encode the meaning of the corresponding word <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
2.  **Attention Mechanism**: [[role_of_transformers_in_language_models | Transformers]] uniquely rely on a special operation called "attention" <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. This allows these lists of numbers to interact and refine their encoded meanings based on the surrounding context, all in parallel <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. For example, the numbers encoding "bank" might change to reflect "riverbank" based on context <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
3.  **Feed-Forward Neural Networks**: [[role_of_transformers_in_language_models | Transformers]] also incorporate feed-forward neural networks, which provide additional capacity for the model to store language patterns learned during [[training_process_of_large_language_models | training]] <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

Data flows through many iterations of these two fundamental operations <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. The goal is for each list of numbers to be enriched with the necessary information to accurately predict the next word in the passage <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. Finally, a function is performed on the last vector in the sequence, which has been influenced by all input text context and learned [[training_process_of_large_language_models | training]] data, to produce a probability prediction for every possible next word <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Challenges and Emergent Behavior

While researchers design the framework for how each step works, the specific behavior of an LLM is an [[challenges_in_understanding_model_predictions | emergent phenomenon]] determined by how its hundreds of billions of parameters are tuned during [[training_process_of_large_language_models | training]] <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. This makes it incredibly difficult to pinpoint precisely why a model makes certain predictions <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. Despite these complexities, the words generated by LLMs when auto-completing prompts are remarkably fluent, fascinating, and useful <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.