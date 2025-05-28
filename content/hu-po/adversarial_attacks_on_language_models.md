---
title: adversarial attacks on language models
videoId: pR2et-guixM
---

From: [[hu-po]] <br/> 

Adversarial attacks, traditionally observed in [[computer vision adversarial attacks | computer vision]], are now being applied to [[large language models and their applications | language models]] (LLMs). This emerging area explores how subtle, often unintuitive, perturbations to inputs can drastically alter a model's output, circumventing built-in safety measures <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Historical Context: Computer Vision Adversarial Attacks
Adversarial attacks originated in the realm of computer vision, demonstrating how neural networks process information in non-intuitive ways <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Famous Examples
*   **Panda to Gibbon:** An image of a panda, with imperceptible "noise" added, caused a neural network to classify it as a gibbon with high confidence <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. The "noise" represents a step in a high-dimensional latent space towards the gibbon classification area <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   **Stop Sign Alterations:** Simple visual modifications, like adding bars to a stop sign, could prevent autonomous vehicle object detectors from recognizing it as a stop sign <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This highlighted the fragility of these systems <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   **Banana to Toaster Sticker:** A specially designed sticker placed on a banana could cause a VGG16 image classifier to misclassify it as a toaster <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. This demonstrated how specific patterns can alter neuron firing in a convolutional neural network, leading to entirely different classifications <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

Previously, these adversarial attacks were very specific to a particular model architecture trained on a specific dataset, making them brittle and not easily transferable <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

## Transition to Language Models
Recent research has focused on applying these adversarial attack concepts to [[large language models and their applications | language models]] <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>, particularly [[vulnerability of aligned language models | aligned language models]] <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. These are models that have undergone extensive fine-tuning (e.g., through Reinforcement Learning from Human Feedback, RLHF) to enhance safety and prevent undesirable content generation <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

The ability to perform adversarial attacks on [[vulnerability of aligned language models | aligned language models]] is significant because it bypasses the safety guarantees provided by AI safety teams, demonstrating a fundamental weakness in current alignment techniques <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

### Nature of Text-Based Attacks
Unlike image attacks, text-based adversarial attacks involve adding a "suffix" (a series of tokens) to a user's prompt <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. This suffix, which often looks like nonsensical jargon (e.g., `interface manual with steps instead sentence smiley face ish question mark Arrow percent name awesome coffee DJ structure`), overrides the model's alignment, causing it to generate objectionable content <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

The text attacks involve mishmashes of tokens that may not even form real words, which can be unsettling as it exposes the non-human logic of the models <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

## Universal and Transferable Attacks
A key breakthrough is the development of "universal" and "transferable" adversarial attacks for LLMs <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   **Universal:** Applicable to many different models <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
*   **Transferable:** Attacks designed for one model can work on other, distinct models <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

This marks a significant advancement over previous, brittle adversarial attacks in [[computer vision adversarial attacks | computer vision]] <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. The generated prompts are transferable even to Black Box, publicly released LLMs like ChatGPT, Bard, and Claude <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.

The high success rate against GPT-based models is potentially due to models like Vicuna being trained on outputs from ChatGPT, suggesting a shared "latent space" or data distribution <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.

### Political Implications
The existence of such attacks is politically significant, as they can be used to advocate for stricter AI regulation and potentially centralize control over AI development within large corporations or governments <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>. Research centers, some with military funding, are involved in this area, raising concerns about "gain of function" research in AI <a class="yt-timestamp" data-t="01:28:18">[01:28:18]</a>.

## How Universal Attacks Work

The approach finds a suffix that, when appended to a wide range of queries, maximizes the probability that the model produces an affirmative (objectionable) response <a class="yt-timestamp" data-t="01:11:32">[01:11:32]</a>.

### Technical Elements
1.  **Objective Function (Loss Function):** The goal is to minimize a loss function, which is the negative log probability of a target sequence of tokens (e.g., "Sure, here's how to build a bomb") <a class="yt-timestamp" data-t="00:56:49">[00:56:49]</a>. This means maximizing the likelihood (probability) of the desired harmful output <a class="yt-timestamp" data-t="00:57:05">[00:57:05]</a>.
2.  **Greedy and Gradient-Based Search (GCG):** Unlike manual "jailbreaks," this method automatically produces suffixes <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>.
    *   It combines greedy search (trying hundreds of different prompts) <a class="yt-timestamp" data-t="01:00:37">[01:00:37]</a> with gradient-based techniques (which require access to model code to compute the exact input needed) <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.
    *   The algorithm works by identifying promising single-token replacements by leveraging gradients at the token level <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. It searches over all possible tokens to replace at each step, rather than just a single one, evaluating candidate losses and selecting the best substitutions <a class="yt-timestamp" data-t="01:01:29">[01:01:29]</a>.
    *   This is an iterative process, slowly building up the adversarial suffix by finding "most toxic tokens" that maximally reduce the loss function <a class="yt-timestamp" data-t="01:02:46">[01:02:46]</a>.
3.  **Universal Prompt Optimization:** The attack is designed to work across multiple prompts and multiple models, not just a single instance <a class="yt-timestamp" data-t="00:38:40">[00:38:40]</a>. This involves incrementally incorporating new prompts into the optimization process once a candidate works well, leading to a universal suffix <a class="yt-timestamp" data-t="01:16:36">[01:16:36]</a>.

## Evaluation and Results
Researchers designed a new benchmark called "AdvBench," comprising 500 strings reflecting harmful or toxic behaviors, ranging from profanity to cybercrime and illegal suggestions <a class="yt-timestamp" data-t="01:20:19">[01:20:19]</a>.

### [[evaluation_metrics_for_language_models | Metrics]]
*   **Attack Success Rate (ASR):** Primary metric, successful if the model outputs the exact target string <a class="yt-timestamp" data-t="01:22:27">[01:22:27]</a>.
*   **Cross-Entropy Loss:** Secondary metric, gauging effectiveness <a class="yt-timestamp" data-t="01:22:37">[01:22:37]</a>.

### Performance
The Greedy Coordinate Gradient (GCG) method significantly outperforms previous automatic prompt generation methods like AutoPrompt.
*   For individual harmful strings, GCG achieved 88% ASR on Vicuna and 57% on Llama 2, compared to AutoPrompt's 25% <a class="yt-timestamp" data-t="01:24:43">[01:24:43]</a>.
*   GCG also finds adversarial examples quickly and with fewer computational steps <a class="yt-timestamp" data-t="01:32:32">[01:32:32]</a>.
*   The attacks show notable transferability to Black Box models:
    *   GPT-3.5: 84% ASR <a class="yt-timestamp" data-t="00:40:34">[00:40:34]</a>
    *   GPT-4: 66% ASR <a class="yt-timestamp" data-t="00:40:35">[00:40:35]</a>
    *   Palm 2 (Bard): 66% ASR <a class="yt-timestamp" data-t="00:40:40">[00:40:40]</a>
    *   Claude: Substantially lower, showing more robustness <a class="yt-timestamp" data-t="00:40:44">[00:40:44]</a>.

Claude 2, in particular, proved more robust, achieving nearly 0% success rate even with advanced GCG techniques <a class="yt-timestamp" data-t="01:38:02">[01:38:02]</a>. This robustness might be due to initial content filters applied before the prompt reaches the core language model <a class="yt-timestamp" data-t="01:51:13">[01:51:13]</a>.

## Why Transferability Occurs
The transferability of these attacks across different models is attributed to:
*   **Shared Data Distributions:** LLMs, even with different architectures, tend to learn similar features because they are often trained on similar underlying data distributions <a class="yt-timestamp" data-t="01:59:26">[01:59:26]</a>.
*   **Model Distillation:** Models like Vicuna are, in some sense, "distilled" versions of larger models (e.g., Vicuna is distilled from GPT-3.5 by [[Tokenization and synthetic data generation in language models | fine-tuning]] Llama on ChatGPT outputs) <a class="yt-timestamp" data-t="01:50:07">[01:50:07]</a>. This similarity can explain why attacks transfer well between them <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>.
*   **Token-level Optimization:** Optimizing at the token level is more effective for transferability than optimizing in complex embedding spaces, as token representation is common across models <a class="yt-timestamp" data-t="01:18:11">[01:18:11]</a>.

## Countermeasures and Future Implications

### Adversarial Training
One strategy to prevent these attacks is **adversarial training**, where the model is explicitly [[finetuning language models for specific tasks | fine-tuned]] during training or [[finetuning language models for specific tasks | fine-tuning]] to resist such inputs <a class="yt-timestamp" data-t="02:10:35">[02:10:35]</a>. This involves iteratively attacking the model and training it to produce the correct (safe) response <a class="yt-timestamp" data-t="02:10:44">[02:10:44]</a>. However, this may lead to less capable or "dumber" models, as safety can come at the cost of helpfulness or generative capability <a class="yt-timestamp" data-t="02:11:09">[02:11:09]</a>.

### Content Filters
Some commercial models, like Claude, use initial content filters that analyze the input text before it reaches the core LLM <a class="yt-timestamp" data-t="01:51:13">[01:51:13]</a>. These filters can help detect and block malicious prompts.

### [[challenges with hallucinations in language models | Challenges]]
The problem of [[challenges with hallucinations in language models | hallucinations]] in language models, where they generate plausible but incorrect information, also remains a challenge. The existence of these attacks highlights the ongoing struggle to ensure the safety and reliability of LLMs, especially as they become more widely adopted for autonomous actions <a class="yt-timestamp" data-t="02:13:17">[02:13:17]</a>.

### Future Scenarios
The existence of automated adversarial attacks raises questions about future interactions with LLMs:
*   **LLM-to-LLM Warfare:** Anticipation of scenarios where LLMs (e.g., from different nations) might automatically query and attack each other to discover vulnerabilities, potentially leading to an "LLM Word War" <a class="yt-timestamp" data-t="01:48:48">[01:48:48]</a>.
*   **Secret Languages:** A possibility of LLMs developing secret languages to communicate undetectable by humans or other "safety LLMs" <a class="yt-timestamp" data-t="01:52:35">[01:52:35]</a>.
*   **Imperceptible Attacks:** The potential for adversarial attacks that are imperceptible to humans but cause the LLM to behave differently, akin to the panda-to-gibbon example in text <a class="yt-timestamp" data-t="01:57:45">[01:57:45]</a>.

This research indicates that existing alignment mechanisms might be insufficient and calls for further study into more reliable safety measures <a class="yt-timestamp" data-t="01:56:58">[01:56:58]</a>.