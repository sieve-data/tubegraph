---
title: AI and neuroscience
videoId: tNRMWNfrkxc
---

From: [[everyinc]] <br/> 

Bradley Love, Professor of Cognitive and Decision Sciences in Experimental Psychology at UCL, is a lead developer of BrainGPT, a large language model designed to enhance neuroscience research. The project explores the profound implications of [[ai_and_its_impact_on_science|AI]] on the future of science itself <a class="yt-timestamp" data-t="01:07:07">[01:07:07]</a>, particularly in fields like neuroscience <a class="yt-timestamp" data-t="01:34:01">[01:34:01]</a>.

## BrainGPT: Predicting Scientific Outcomes
The primary motivation for BrainGPT stems from the exponentially growing scientific literature, which has become "unreadable" for humans <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>. While many tools focus on summarizing past research, BrainGPT takes a "forward-looking" approach by focusing on predicting study outcomes before they happen <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.

### How it Works
BrainGPT was developed to predict the results of neuroscience studies and experiments, outperforming human experts, including neuroscience professors <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.

To predict the future, the model draws upon an understanding of the past, aggregating findings from thousands of papers across different levels of neuroscience, from psychology and behavior down to cellular and molecular findings, including DNA <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>.

Prediction in science offers several benefits:
*   **More informative studies** <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>: If BrainGPT predicts a study will work with 99.9% certainty, there's little information gain in running it <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>. Conversely, if the system predicts unexpected results, and a researcher has an intuition that the literature has a systematic bias, pursuing that study could lead to impactful discoveries <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.
*   **Addressing reproducibility issues**: Many scientific findings do not replicate <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>. Systems like BrainGPT could help determine what findings are reliable and guide future research steps <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>.

### Training and Testing
The model is trained on 20 years of neuroscience literature <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>. It addresses issues like p-hacking and noisy, incomplete data by aggregating thousands of papers, similar to an ensemble method in machine learning <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>. The assumption is that the signal will emerge in the correct direction when enough data is aggregated <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>.

A benchmark called "BrainBench" was created using abstracts from the *Journal of Neuroscience*, which covers all subfields of neuroscience <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>. Abstracts were subtly altered (e.g., changing "anterior hippocampus" to "posterior hippocampus" or "increases" to "decreases") to create two-option multiple-choice questions <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>. Both neuroscientists and large language models (including fine-tuned ones) were tested for accuracy <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a>.

Instead of traditional prompting, BrainGPT leverages "perplexity" – how surprising a text is to the model given its training <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>. Comparing the perplexity of the original and altered abstract versions allows the model to choose the less surprising (more likely) one <a class="yt-timestamp" data-t="14:50:00">[14:50:00]</a>. This method is significantly more accurate (83% vs. human 63%) and allows for a measure of confidence in the model's prediction <a class="yt-timestamp" data-t="16:10:00">[16:10:00]</a>.

## [[intersection_of_ai_and_philosophy|Intersection of AI and Philosophy]]: A Shifting Paradigm in Science
The traditional scientific emphasis has been on explanations, which are powerful for predictions and understanding <a class="yt-timestamp" data-t="18:33:00">[18:33:00]</a>. This has worked well in fields like physics and chemistry <a class="yt-timestamp" data-t="18:52:00">[18:52:00]</a>. However, in "soft sciences" like psychology, causal, parsimonious explanations are extremely difficult to find, leading to reproducibility issues <a class="yt-timestamp" data-t="19:07:00">[19:07:07]</a>.

[[ai_and_its_impact_on_science|Machine learning and AI]] approaches can "unbundle explanations from predictions," allowing for good predictions without necessarily having clear theories or explanations <a class="yt-timestamp" data-t="19:47:00">[19:47:00]</a>. This transforms a science problem into an engineering problem, focusing on prediction (e.g., predicting depression rather than explaining it) <a class="yt-timestamp" data-t="20:01:00">[20:01:00]</a>.

It is proposed that in complex biological systems, explanations may diverge from predictions over time <a class="yt-timestamp" data-t="23:41:00">[23:41:00]</a>. If the underlying reality is messy, with 10,000 interacting variables at different levels (DNA to behavior), a clean, human-understandable explanation may not be possible <a class="yt-timestamp" data-t="23:17:00">[23:17:00]</a>.

### The "Dog Analogy" and the Limits of Human Understanding
The discussion highlights that humans may be like dogs trying to understand quantum mechanics: the theory is well-specified, but it's simply beyond a dog's comprehension <a class="yt-timestamp" data-t="24:16:00">[24:16:00]</a>. Similarly, some complex systems might be beyond human capacity to fully understand or explain in a concise manner <a class="yt-timestamp" data-t="24:25:00">[24:25:00]</a>.

> "imagine explaining quantum mechanics to a dog quantum mechanics is a very well specified Theory but it's just beyond a dog and like you know maybe at some point we're the dogs you know like we're not gonna understand what's going on" <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>

This could lead to a future where science becomes more predictive and less about finding simple, elegant explanations. Scientists might become "new priests," interpreting and providing meaning to complex systems without necessarily understanding every underlying causal interaction <a class="yt-timestamp" data-t="25:22:00">[25:22:00]</a>.

### Critiquing Intuitive Explanations
A paper titled "*The Inevitability and Superfluousness of Cell Types and Spatial Cognition*" critiques the human tendency to force intuitive understandings onto complex systems, particularly in neuroscience <a class="yt-timestamp" data-t="37:00:00">[37:00:00]</a>.

Traditional neuroscience has seen major discoveries based on recording from single cells and attributing clear, intuitive functions (e.g., "place cells" as a brain GPS system) <a class="yt-timestamp" data-t="37:34:00">[37:34:00]</a>. However, this paper found that when large networks are placed in virtual reality environments, similar "cell types" can pop up even in random networks not serving a navigation function <a class="yt-timestamp" data-t="38:22:00">[38:22:00]</a>.

This highlights the danger of forcing intuitive understanding:
*   It can lead to a "seductive but ultimately limiting" view <a class="yt-timestamp" data-t="40:35:00">[40:35:00]</a>.
*   Nobel-prize-winning discoveries are often followed by decades of research explaining why the initial simple explanation was incomplete or distorted <a class="yt-timestamp" data-t="39:04:00">[39:04:00]</a>.
*   Humans naturally prize coherent, simple narratives, similar to how politicians or lawyers craft stories <a class="yt-timestamp" data-t="41:05:00">[41:05:00]</a>. This preference for parsimonious explanations, while sometimes useful (Occam's razor), can obscure deeper truths in complex, high-dimensional systems <a class="yt-timestamp" data-t="41:51:00">[41:51:00]</a>.

## Rebuilding Science in an [[ai_and_its_impact_on_science|AI-Driven World]]
To navigate this complex future, a shift in scientific orientation is suggested:
*   **Philosophical training**: Scientists should be more thoughtful and philosophical about the nature and limits of explanations <a class="yt-timestamp" data-t="45:22:00">[45:22:00]</a>.
*   **Computational skills and large-scale simulations**: Greater emphasis on [[ai_and_its_impact_on_science|AI]] and computational approaches for handling large datasets and complex interactions <a class="yt-timestamp" data-t="45:34:00">[45:34:00]</a>.
*   **Naturalistic environments**: More consideration of the complexity of real-world environments, rather than overly simplified lab conditions that might miss key variables <a class="yt-timestamp" data-t="45:42:00">[45:42:00]</a>.
*   **Interplay of lab and real-world data**: Combine large-scale naturalistic data with targeted lab studies to resolve specific questions, ensuring science remains relevant to real-world problems <a class="yt-timestamp" data-t="46:26:00">[46:26:00]</a>.

In the field of computer vision, a significant advance occurred when deep learning models like AlexNet, trained on millions of natural images, outperformed traditional vision science models. This demonstrated that taking on the "whole problem at once" at scale, driven by engineering challenges, could lead to breakthroughs that decades of hypothesis-driven research had not achieved <a class="yt-timestamp" data-t="48:38:00">[48:38:00]</a>.

### The View From Nowhere
Thomas Nagel's book *The View from Nowhere* is recommended for understanding the strengths and weaknesses of science <a class="yt-timestamp" data-t="50:01:00">[50:01:00]</a>. Science, by its nature, aims for an objective, "disembodied perspective" – a "view from nowhere" <a class="yt-timestamp" data-t="50:48:00">[50:48:00]</a>. This is its strength in achieving verifiable results (e.g., launching a probe to Mars) <a class="yt-timestamp" data-t="51:03:00">[51:03:00]</a>. However, much valuable human experience is subjective, which is where meaning in life comes from <a class="yt-timestamp" data-t="51:15:00">[51:15:00]</a>.

Psychology, while striving to be science, grapples with operationalizing subjective experiences like depression <a class="yt-timestamp" data-t="52:25:00">[52:25:00]</a>. When focusing on observable and quantifiable measures, psychology abstracts away from the richness of individual differences. Science can provide correlates of experience or predict outcomes (e.g., anesthesia effects) <a class="yt-timestamp" data-t="53:20:00">[53:20:00]</a>, but it may have little to say about the deeper, first-person subjective experiences, which are often explored through literature, religion, and the arts <a class="yt-timestamp" data-t="53:51:00">[53:51:00]</a>.

In conclusion, the future of [[ai_and_neuroscience|AI and neuroscience]] may involve a shift from seeking simplified, human-understandable explanations to embracing complex, predictive models that operate beyond our intuitive grasp, leading to more practical and beneficial outcomes for society <a class="yt-timestamp" data-t="29:20:00">[29:20:00]</a>.