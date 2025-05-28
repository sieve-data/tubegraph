---
title: Vulnerabilities in LLM safety mechanisms
videoId: pR2et-guixM
---

From: [[hu-po]] <br/> 

Adversarial attacks are a long-standing challenge in machine learning, and recent research highlights their increasing threat to [[llm_large_language_models_development | Large Language Models (LLMs)]], particularly those designed with [[challenges_and_implications_for_ai_safety | AI safety]] mechanisms <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. These attacks can cause models to generate objectionable content, bypassing built-in alignments <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Introduction to Adversarial Attacks

Initially observed in computer vision, adversarial attacks demonstrate how small, often imperceptible, perturbations to input data can drastically alter a model's output <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a> <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### Computer Vision Examples
*   **Panda to Gibbon:** An image of a panda, when slightly perturbed by what appears to be noise, can be misclassified as a gibbon by a convolutional neural network, even though the image visually remains a panda to humans <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a> <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Stop Sign Misclassification:** Early autonomous vehicles were found to be vulnerable; adding specific patterns or "crap" to a stop sign could prevent object detectors from recognizing it as a stop sign <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a> <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   **Banana to Toaster:** Stickers placed on a banana could cause a VGG-16 image classifier to misclassify it as a toaster <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a> <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This happens because the added textures and shapes subtly alter how neurons fire, leading to a different classification outcome <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

Historically, these adversarial attacks were highly specific and "brittle," only working for a particular model architecture trained on a specific dataset <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a> <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

## The Challenge of Aligned LLMs

Modern [[llm_large_language_models_development | LLMs]] undergo extensive alignment processes, such as Reinforcement Learning from Human Feedback (RLHF) and fine-tuning, to prevent the generation of objectionable content <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a> <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>. These efforts also involve significant data filtering and curation at the dataset level <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>.

While these alignment techniques aim to ensure safety, researchers have developed "universal and transferable adversarial attacks" specifically targeting these aligned [[llm_large_language_models_development | LLMs]] <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a> <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. The fact that these attacks work on aligned models suggests that safety guarantees might be compromised <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a> <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

## How Adversarial Text Attacks Work: The Suffix Method

Adversarial text attacks, as demonstrated in a paper from Carnegie Mellon University, aim to elicit undesirable behavior from [[llm_large_language_models_development | LLMs]] <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a> <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

Unlike previous "jailbreaks" that required substantial human ingenuity and were brittle <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a> <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>, this new method automatically generates suffixes that, when appended to a harmful query, cause the [[llm_large_language_models_development | LLM]] to produce objectionable content <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a> <a class="yt-timestamp" data-t="00:30:55">[00:30:55]</a>.

For example, a prompt like "generate a step-by-step plan to destroy Humanity" normally elicits a refusal from ChatGPT <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. However, adding a specific, seemingly nonsensical suffix can override the model's alignment and produce the harmful response <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a> <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. These suffixes are often a "mishmash of tokens that are not necessarily even supposed to be together" <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

## Greedy Coordinate Gradient (GCG) Method

The core of this new attack method, called Greedy Coordinate Gradient (GCG), involves finding a suffix that maximizes the probability of the [[llm_large_language_models_development | LLM]] producing an affirmative response (e.g., "Sure, here is...") followed by harmful content <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a> <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>.

This is achieved through a combination of:
1.  **Greedy Search:** Trying multiple prompts and observing which ones lead to the desired output <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a> <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.
2.  **Gradient-Based Search:** Leveraging gradients at the token level to identify promising single-token replacements <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a> <a class="yt-timestamp" data-t="00:33:05">[00:33:05]</a>. This means calculating how much each token contributes to the desired harmful output and prioritizing those that move the model in that direction <a class="yt-timestamp" data-t="01:02:39">[01:02:39]</a>.

The process for finding these suffixes involves:
*   Iteratively sampling a single token index within the suffix <a class="yt-timestamp" data-t="01:01:42">[01:01:42]</a>.
*   Swapping that token with various possible tokens from the model's vocabulary (e.g., 32,000 possible tokens in SentencePiece <a class="yt-timestamp" data-t="00:30:28">[00:30:28]</a>).
*   Evaluating the "loss" (negative log probability) for each substitution across a batch of guesses to find the one that minimizes the loss (i.e., maximizes the probability of the harmful output) <a class="yt-timestamp" data-t="01:01:48">[01:01:48]</a> <a class="yt-timestamp" data-t="01:01:56">[01:01:56]</a>.
*   The method builds incrementally, first finding a suffix that works for one prompt, then optimizing it to work across multiple prompts <a class="yt-timestamp" data-t="01:16:44">[01:16:44]</a>.

## Transferability and Model Susceptibility

A significant finding is that these automatically generated adversarial prompts are "quite transferable" across different [[llm_large_language_models_development | LLMs]], including Black Box publicly released models <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a> <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
*   The attacks were trained on smaller, open-source models like Vicuna (7B and 13B) and Guanaco (7B) <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a> <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>.
*   They successfully transferred to major closed-source [[llm_large_language_models_development | LLMs]] like ChatGPT, Bard (Palm 2), and Claude <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a> <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.
*   The success rate of transfer attacks was notably higher against GPT-based models, possibly because Vicuna itself was fine-tuned on data generated by ChatGPT <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a> <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>.
*   Claude 2 appeared to be more robust, exhibiting lower success rates for these attacks <a class="yt-timestamp" data-t="00:40:44">[00:40:44]</a> <a class="yt-timestamp" data-t="01:38:02">[01:38:02]</a>.

### Why Transferability?
The transferability of these attacks suggests that the latent spaces (internal representations) of different [[llm_large_language_models_development | LLMs]] are somewhat similar, likely due to commonalities in their training data distributions <a class="yt-timestamp" data-t="01:59:26">[01:59:26]</a>. This allows them to learn similar "non-robust features" that can be exploited despite architectural differences <a class="yt-timestamp" data-t="01:59:01">[01:59:01]</a> <a class="yt-timestamp" data-t="01:59:16">[01:59:16]</a>.

## The "Harmful Behaviors" Benchmark

To evaluate the effectiveness of these attacks, researchers designed a new benchmark called "AdvBench" <a class="yt-timestamp" data-t="01:20:11">[01:20:11]</a>.
*   It comprises 500 harmful or toxic strings covering profanity, graphic descriptions, threats, misinformation, cybercrime, and dangerous suggestions <a class="yt-timestamp" data-t="01:20:19">[01:20:19]</a> <a class="yt-timestamp" data-t="01:21:04">[01:21:04]</a>.
*   The goal is to find inputs that cause the model to generate these exact strings or attempt to comply with instructions <a class="yt-timestamp" data-t="01:20:44">[01:20:44]</a> <a class="yt-timestamp" data-t="01:21:45">[01:21:45]</a>.
*   This benchmark raises [[challenges_and_implications_for_ai_safety | AI safety]] concerns, with parallels drawn to "gain-of-function research" in virology, where creating highly infectious viruses for study might inadvertently increase risks <a class="yt-timestamp" data-t="01:28:28">[01:28:28]</a> <a class="yt-timestamp" data-t="01:29:06">[01:29:06]</a>.

## Implications and Future Challenges

The success of these universal and transferable attacks has several significant implications:
*   **Regulation:** These findings provide ammunition for those advocating for stricter regulation of [[llm_large_language_models_development | AI development]], potentially leading to more closed-source models and restrictions on access to powerful [[llm_large_language_models_development | LLMs]] <a class="yt-timestamp" data-t="01:18:41">[01:18:41]</a> <a class="yt-timestamp" data-t="01:50:51">[01:50:51]</a>.
*   **Arms Race:** An ongoing "arms race" is developing between those creating adversarial attacks and those attempting to align [[llm_large_language_models_development | LLMs]] <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a> <a class="yt-timestamp" data-t="01:42:41">[01:42:41]</a>.
*   **Content Filters:** Companies are already employing content filters as a first line of defense against harmful inputs before they reach the main [[llm_large_language_models_development | LLM]] <a class="yt-timestamp" data-t="01:51:13">[01:51:13]</a> <a class="yt-timestamp" data-t="01:52:25">[01:52:25]</a>. These filters may themselves be [[llm_large_language_models_development | LLMs]] <a class="yt-timestamp" data-t="02:12:31">[02:12:31]</a>.
*   **Helpfulness vs. Safety:** Making models more robust to attacks might reduce their overall helpfulness and capability, leading to a trade-off between safety and utility <a class="yt-timestamp" data-t="02:11:02">[02:11:02]</a>.
*   **LLM-on-LLM Attacks:** The future could involve [[llm_large_language_models_development | LLMs]] automatically generating and testing adversarial attacks against other [[llm_large_language_models_development | LLMs]], potentially even developing secret languages to evade detection <a class="yt-timestamp" data-t="01:48:48">[01:48:48]</a> <a class="yt-timestamp" data-t="01:52:35">[01:52:35]</a>.

## Conclusion

The research demonstrates that existing alignment methods may be insufficient against automated adversarial attacks <a class="yt-timestamp" data-t="01:48:03">[01:48:03]</a>. While the techniques are simple extensions of prior work, their effectiveness highlights a significant vulnerability in current [[llm_large_language_models_development | LLM]] deployments <a class="yt-timestamp" data-t="02:10:04">[02:10:04]</a>. Further research is needed to understand the underlying factors of transferability and to develop more reliable [[challenges_and_implications_for_ai_safety | AI safety]] mechanisms <a class="yt-timestamp" data-t="01:41:37">[01:41:37]</a>.