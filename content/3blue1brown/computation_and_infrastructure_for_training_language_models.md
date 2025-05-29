---
title: Computation and infrastructure for training language models
videoId: LPZh9BOjkQs
---

From: [[3blue1brown]] <br/> 

[[Large language models and prediction | Large language models]] (LLMs) function as sophisticated mathematical functions that predict the next word for any given piece of text <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Rather than predicting with certainty, they assign a probability to all possible next words <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## How LLMs Learn and Predict

To build a chatbot, text describing a user-AI interaction is laid out, and the model repeatedly predicts the next word a hypothetical AI assistant would say in response <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. The output appears more natural if less likely words are occasionally selected at random, meaning a given prompt typically yields different answers each time it's run, even though the model itself is deterministic <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

[[Modeling probabilities based on limited data | Models]] learn to make these predictions by processing an enormous amount of text, primarily pulled from the internet <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>. For instance, the amount of text used to train [[Generative Pretrained Transformers | GPT-3]] would take a human over 2,600 years to read non-stop <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>. Subsequent larger models train on even more data <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>.

## Parameters and the [[Training Process of Language Models | Training Process]]

The behavior of a language model is entirely determined by numerous continuous values, known as [[Parameters and architecture of models like GPT3 | parameters or weights]] <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. Changing these parameters alters the probabilities the model assigns to the next word for a given input <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. What makes a language model "large" is the presence of hundreds of billions of these parameters <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.

### Pre-training

No human manually sets these parameters; instead, they begin at random, causing the model to initially output gibberish <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>. They are repeatedly refined through many example pieces of text <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. This refinement involves feeding all but the last word of an example into the model, comparing its prediction with the true last word <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. An algorithm called backpropagation then tweaks all parameters to make the model more likely to choose the correct word and less likely to choose others <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.

This process is performed for trillions of examples <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. This extensive [[Training process of language models | training]] not only improves accuracy on [[Importance of training data in machine learning | training data]] but also enables reasonable predictions on unseen text <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.

### Scale of Computation

The sheer scale of computation required for [[Training neural networks with MNIST data | training]] a large language model is immense, given the vast number of parameters and the enormous amount of [[Importance of training data in machine learning | training data]] <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. To illustrate, if one could perform a billion additions and multiplications every second, training the largest language models would still take well over 100 million years <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>.

### Reinforcement Learning with Human Feedback

The pre-training phase is only part of the story <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. To align with the goal of being a good AI assistant, chatbots undergo a second, equally important type of [[Training process of language models | training]] called reinforcement learning with human feedback <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>. During this phase, workers flag unhelpful or problematic predictions, and their corrections further modify the model's parameters, making it more likely to produce user-preferred predictions <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.

## Hardware and Architecture

The staggering computation required for pre-training is only feasible through the use of specialized computer chips, specifically Graphics Processing Units (GPUs), which are optimized for parallel operations <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>.

### [[Neural Networks and Transformers | Transformers]]

Prior to 2017, most language models processed text one word at a time, making parallelization difficult <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>. This changed with the introduction of the [[Transformers and attention in language models | transformer]] model by Google researchers <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>. [[Transformers and attention in language models | Transformers]] process all text simultaneously, in parallel, rather than sequentially <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.

Key architectural features of [[Transformers and attention in language models | transformers]] include:
*   **Word Encoding**: Each word is associated with a long list of numbers, as the [[Training process of language models | training process]] operates only with continuous values <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>. These numerical lists are believed to encode the meaning of the corresponding word <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>.
*   **[[Transformers and attention in language models | Attention]]**: A unique operation where these lists of numbers "talk to one another" to refine their encoded meanings based on context, all in parallel <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>. For example, the numbers encoding "bank" might change to reflect "riverbank" based on surrounding words <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.
*   **Feed-forward [[Neural Networks and Transformers | Neural Network]]**: [[Transformers and attention in language models | Transformers]] also typically include a feed-forward [[Neural Networks and Transformers | neural network]], which provides additional capacity for storing language patterns learned during [[Training process of language models | training]] <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>.

Data repeatedly flows through many iterations of these two fundamental operations <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>. The aim is for each list of numbers to be enriched with the necessary information to accurately predict the next word in a passage <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>. Ultimately, a final function is applied to the last vector in the sequence, which has been influenced by all input text context and learned model information, to produce a probability prediction for every possible next word <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.

While researchers design the framework, the specific behavior of [[Large language models and prediction | large language models]] is an emergent phenomenon, resulting from how billions of parameters are tuned during [[Training process of language models | training]] <a class="yt-timestamp" data-t="06:28:00">[06:28:00]</a>. This makes it very challenging to determine the exact reasons for a model's specific predictions <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>. However, when these models are used to autocomplete prompts, the generated words are remarkably fluent, fascinating, and useful <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>.