---
title: Probability Distributions and Softmax Function
videoId: wjZofJX0v4M
---

From: [[3blue1brown]] <br/> 

In machine learning models like GPT-3, the final output often takes the form of a [[probability_distribution_pdf | probability distribution]] <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This is a list of numbers representing the likelihood of different possible outcomes, such as the next token or word in a sequence <a class="yt-timestamp" data-t="00:10:09">[10:09]</a>.

## Generating Text with Probability Distributions
When a model like ChatGPT predicts the next word, it generates a [[probability_distribution_pdf | probability distribution]] over all possible tokens that might follow <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. To create a longer piece of text, the model can:
1.  Receive an initial text snippet <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
2.  Take a random sample from the generated [[probability_distribution_pdf | distribution]] <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
3.  Append that sample to the text <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
4.  Run the entire process again to make a new prediction based on the updated text <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
This repeated prediction and sampling process is fundamental to how large language models produce text one word at a time <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

## The Softmax Function
To ensure that the output of a neural network can be interpreted as a [[probability_distribution_pdf | probability distribution]], a specific function called **Softmax** is used <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.

### Purpose
A valid [[probability_distribution_pdf | probability distribution]] requires each value to be between 0 and 1, and all values must sum up to 1 <a class="yt-timestamp" data-t="00:22:31">[00:22:31]</a>. However, the raw outputs from matrix-vector multiplications in deep learning models often include negative values, values much larger than 1, and do not sum to 1 <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>. Softmax transforms an arbitrary list of numbers into a valid distribution <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.

### How it Works
Softmax ensures that:
*   The largest input values correspond to probabilities closest to 1 <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>.
*   Smaller input values correspond to probabilities very close to 0 <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>.

The computational steps for Softmax are <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>:
1.  Raise the mathematical constant `e` to the power of each number in the input list. This makes all values positive <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a>.
2.  Calculate the sum of all these positive values <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>.
3.  Divide each term by that sum, which normalizes the list so it adds up to 1 <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.

If one input number is significantly larger than the rest, its corresponding term will dominate the [[probability_distribution_pdf | distribution]] <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>. However, if multiple values are similarly large, they will also receive meaningful weight, and the output changes continuously as inputs vary <a class="yt-timestamp" data-t="00:23:42">[00:23:42]</a>.

### Temperature Parameter
In some applications, like when ChatGPT uses this [[probability_distribution_pdf | distribution]] to select the next word, an additional constant `T` (called "temperature") can be introduced into the denominator of the exponents in the Softmax function <a class="yt-timestamp" data-t="00:23:59">[00:23:59]</a>.

The effect of `T` is as follows <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>:
*   **Larger T**: Gives more weight to lower values, making the [[probability_distribution_pdf | distribution]] more uniform <a class="yt-timestamp" data-t="00:24:18">[00:24:18]</a>. This can lead to more creative but potentially nonsensical outputs <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.
*   **Smaller T**: Causes larger values to dominate more aggressively <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>.
*   **T = 0**: All the weight goes to the maximum value, resulting in the most predictable word being chosen <a class="yt-timestamp" data-t="00:24:26">[00:24:26]</a>. This can lead to trite or derivative outputs <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>.

For instance, GPT-3's API typically restricts temperature to a maximum of 2 to prevent overtly nonsensical generations <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>.

### Logits
The raw, unnormalized input values that are fed into the Softmax function, before they are transformed into probabilities, are often referred to as "logits" <a class="yt-timestamp" data-t="00:25:33">[00:25:33]</a>. When word embeddings flow through a network and are then multiplied by the unembedding matrix, the components of that raw output are the logits for the next word prediction <a class="yt-timestamp" data-t="00:25:46">[00:25:46]</a>.