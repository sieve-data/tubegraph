---
title: Role of transformers in language models
videoId: LPZh9BOjkQs
---

From: [[3blue1brown]] <br/> 

Introduced by a team of Google researchers in 2017, the [[generative_pretrained_transformer_architecture | Transformer]] model revolutionized [[large_language_models_and_their_function | language models]] by enabling parallel processing of text <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. Prior to 2017, most language models processed text one word at a time <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

## How Transformers Process Language

[[transformer_architecture_and_its_internal_workings | Transformers]] "soak in" text all at once, in parallel, rather than reading it from start to finish <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. This parallelization is crucial for the efficiency of modern [[large_language_models_and_their_function | large language models]], as it allows for the staggering scale of computation involved in their [[training_process_of_large_language_models | training]] <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>, which relies on special computer chips called GPUs that are optimized for running many operations in parallel <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

The internal workings of a [[generative_pretrained_transformer_architecture | Transformer]] involve several key steps:

1.  **Word Association with Numbers**: Each word is initially associated with a long list of numbers <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. This is because the [[training_process_of_large_language_models | training]] process operates only with continuous values, requiring language to be encoded using numbers, which may somehow encode the meaning of the corresponding word <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
2.  **[[attention_mechanism_in_transformers | Attention Mechanism]]**: [[generative_pretrained_transformer_architecture | Transformers]] are unique due to their reliance on a special operation known as [[attention_mechanism_in_transformers | attention]] <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. This operation allows all these lists of numbers to interact and refine the meanings they encode based on the surrounding context, all performed in parallel <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. For example, the numbers encoding the word "bank" might change based on context to represent "riverbank" <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
3.  **Feed-Forward Neural Networks**: [[generative_pretrained_transformer_architecture | Transformers]] also incorporate feed-forward neural networks, which provide additional capacity for the model to store more language patterns learned during [[training_process_of_large_language_models | training]] <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

Data flows repeatedly through many iterations of these two fundamental operations <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. The aim is for each list of numbers to be enriched with information necessary for an accurate prediction of the next word in a passage <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

## Prediction and Emergent Behavior

At the end of the process, a final function is performed on the last vector in the sequence, which has been influenced by all input text context and the knowledge gained during [[training_process_of_large_language_models | training]] <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. This produces a prediction of the next word, represented as a probability for every possible next word <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

While researchers design the framework for each step, the specific behavior of a [[generative_pretrained_transformer_architecture | Transformer]] is an emergent phenomenon resulting from how its hundreds of billions of [[role_of_parameter_tuning_in_machine_learning_models | parameters]] are tuned during [[training_process_of_large_language_models | training]] <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. This makes it challenging to pinpoint why a model makes exact predictions <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. When [[large_language_models_and_their_function | large language models]] use these predictions to autocomplete a prompt, the generated words are notably fluent, fascinating, and useful <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

For more details on [[transformer_architecture_and_its_internal_workings | transformers]] and [[attention_mechanism_in_transformers | attention]], refer to the video's suggested series on deep learning or a related talk given by the speaker <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.