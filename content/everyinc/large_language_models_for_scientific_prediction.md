---
title: Large language models for scientific prediction
videoId: tNRMWNfrkxc
---

From: [[everyinc]] <br/> 

Bradley Love, a professor of cognitive and decision sciences in experimental psychology at UCL, is a key developer of BrainGPT, a large language model designed to aid neuroscience research. <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a> This tool aims to transform how scientific discovery is conducted by focusing on [[predictions_and_the_challenges_of_accuracy | prediction]] rather than just summarization. <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>

## The Motivation Behind BrainGPT

The primary motivation for developing BrainGPT stems from the exponentially increasing scientific literature, which has become "not really a human readable literature." <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a> Scientists struggle to keep pace with the volume of new information. <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a> While many tools focus on "backward-looking" tasks like summarization, instant reviews, or meta-analysis, BrainGPT takes a "forward-looking" approach. <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>

## BrainGPT's Focus on Prediction

BrainGPT's core function is to predict the outcomes of neuroscience studies before they occur. <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a> It investigates whether [[nature_of_language_models_and_language | large language models]], both off-the-shelf and fine-tuned, can predict the results of neuroscience experiments more accurately than human experts. <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a> BrainGPT has demonstrated superior predictive accuracy compared to neuroscience professors. <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>

The ability to predict future research is crucial because it allows scientists to:
*   **Run more informative studies**: If a study is predicted to have a 99.9% certainty of a specific outcome, it offers little information gain and might not be worth running. <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>
*   **Identify impactful discoveries**: If BrainGPT predicts an unlikely result, but a scientist has an intuition about a systematic bias in the literature, pursuing that study could lead to a significant, trailblazing discovery. <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>
*   **Address reproducibility and replication issues**: Many scientific findings fail to replicate. Systems like BrainGPT could help determine what is "true" and reliable, guiding future steps in scientific discovery. <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>

To make these predictions, the model draws on a vast amount of past information, aggregating findings from thousands of papers across different levels of neuroscience, from psychology and behavior to cellular and molecular findings. <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a> <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>

### BrainGPT's Training and Evaluation

BrainGPT was fine-tuned on 20 years of neuroscience scientific literature. <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a> The developers created a benchmark called "Brain Bench" using publications from the *Journal of Neuroscience*, a respected journal covering all areas of neuroscience. <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>

The evaluation method involved subtly altering the results section of scientific abstracts (e.g., changing "anterior hippocampus" to "posterior hippocampus" or "increases" to "decreases"). <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a> The model was then given two options (original vs. altered) and had to identify the original. <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>

Instead of traditional prompting, the system works by calculating the "perplexity" of each abstract version. <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a> Perplexity measures how "surprising" a text is to the model given its training data. <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a> The model chooses the version with lower perplexity (less surprising). <a class="yt-timestamp" data-t="17:01:00">[17:01:00]</a>

Using perplexity offers two significant advantages:
*   **Higher accuracy**: It results in much greater accuracy (around 83%) compared to prompting (around 61%), which is even better than human experts (63%). <a class="yt-timestamp" data-t="14:48:00">[14:48:00]</a> <a class="yt-timestamp" data-t="16:10:00">[16:10:00]</a>
*   **Confidence calibration**: The difference in perplexity between the correct and incorrect versions can serve as a measure of the model's confidence, which is calibrated to its accuracy. <a class="yt-timestamp" data-t="14:55:00">[14:55:00]</a> This is vital for human-machine teaming, allowing for better combined results than either alone. <a class="yt-timestamp" data-t="15:13:00">[15:13:00]</a>

The reason prompting is less effective in this specific task is likely due to the subtle differences between options in scientific abstracts and the task not aligning with how models are typically fine-tuned for conversational purposes. <a class="yt-timestamp" data-t="15:27:00">[15:27:00]</a>

## The Changing Nature of Science

The rise of [[role_of_language_models_in_knowledge_work | language models]] for [[predictions_and_the_challenges_of_accuracy | prediction]] may fundamentally alter the scientific endeavor. <a class="yt-timestamp" data-t="17:47:00">[17:47:00]</a> Traditionally, science has been "obsessed with explanations," which are powerful for making predictions and understanding the world. <a class="yt-timestamp" data-t="18:33:00">[18:33:00]</a> However, in fields like psychology or other "soft sciences," finding parsimonious causal explanations is exceptionally difficult, leading to replication issues. <a class="yt-timestamp" data-t="18:59:00">[18:59:00]</a>

[[understanding_language_models_and_agency | AI]] and machine learning approaches allow for "unbundling explanations from predictions," meaning good predictions can be achieved without explicit theories or human-understandable explanations. <a class="yt-timestamp" data-t="19:47:00">[19:47:00]</a> This could turn science into an "engineering problem," where phenomena like depression are predicted rather than explained. <a class="yt-timestamp" data-t="20:01:00">[20:01:00]</a> While a theory might exist within a neural network, it may be too vast to fit into human rational brains. <a class="yt-timestamp" data-t="20:21:00">[20:21:00]</a>

### The Dog Analogy and Cognitive Limits

The host and guest discuss the possibility that humans might become like "dogs" attempting to understand "quantum mechanics" – the complexity of biological and real-world systems might simply be beyond human cognitive capacity for clean, simple explanations. <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> <a class="yt-timestamp" data-t="24:16:00">[24:16:00]</a>

Biological systems are inherently messy, with thousands of interacting variables across multiple levels (DNA to behavior), feedback cycles, and delays. <a class="yt-timestamp" data-t="23:12:00">[23:12:00]</a> Unlike engineers who create abstraction layers to simplify systems, nature and biology do not adhere to such designs. <a class="yt-timestamp" data-t="35:54:00">[35:54:00]</a> In such a complex environment, a crisp, human-understandable explanation might not exist. <a class="yt-timestamp" data-t="23:31:00">[23:31:00]</a>

### Scientists as "New Priests" and [[storytelling_and_language_models | Storytelling]]

In a future "predictive world," where everything could be better through AI-driven [[predictions_and_the_challenges_of_accuracy | prediction]], scientists might become "the new priests," interpreting how systems work and providing meaning, possibly through [[storytelling_and_language_models | storytelling]] rather than definitive explanations. <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a> <a class="yt-timestamp" data-t="25:22:00">[25:22:00]</a> This suggests a future where explanation and [[predictions_and_the_challenges_of_accuracy | prediction]] diverge due to the world's inherent complexity. <a class="yt-timestamp" data-t="25:49:00">[25:49:00]</a>

### The Problem of Human Intuition and Parsimonious Explanations

Humans tend to favor simple, coherent narratives and explanations, akin to how politicians, lawyers, or children approach problems. <a class="yt-timestamp" data-t="41:05:00">[41:05:00]</a> This desire for parsimonious explanations, while useful in some contexts (like Occam's razor), can be limiting when dealing with highly complex systems. <a class="yt-timestamp" data-t="41:11:00">[41:11:00]</a> <a class="yt-timestamp" data-t="42:18:00">[42:18:00]</a>

This human bias can lead to misinterpretations. For example, in neuroscience, "intuitive cell types" (like "place cells" that light up in specific locations) have been celebrated with Nobel Prizes, but decades of subsequent research often show they are not as simple or exclusive as initially believed. <a class="yt-timestamp" data-t="37:57:00">[37:57:00]</a> A paper co-authored by Love, "The Inevitability and Superfluousness of Cell Types in Spatial Cognition," demonstrated that similar intuitive cell types can emerge even in random networks, suggesting that the brain's complexity is often forced into overly simple, human-understandable interpretations. <a class="yt-timestamp" data-t="38:09:00">[38:09:00]</a> This tendency to confirm existing frameworks also perpetuates simple stories longer than they should. <a class="yt-timestamp" data-t="44:15:00">[44:15:00]</a>

### Rebuilding Science for the Future

If science were to be rebuilt today, key changes would include:
*   **Philosophical training for scientists**: Encouraging deeper reflection on the nature and limits of explanation. <a class="yt-timestamp" data-t="45:22:00">[45:22:00]</a>
*   **Emphasis on computational skills and large-scale simulations**: As [[the_role_of_data_in_scientific_research | data]] sets grow massive (e.g., DNA, disease, brain recordings), computational approaches become essential for Sensor Fusion and understanding complex interactions. <a class="yt-timestamp" data-t="45:34:00">[45:34:00]</a> <a class="yt-timestamp" data-t="26:48:00">[26:48:00]</a>
*   **Consideration of naturalistic environments**: Moving beyond highly controlled, simplified lab studies, especially for human behavior or biological systems, to avoid creating "fake science" irrelevant to real-world concerns. <a class="yt-timestamp" data-t="45:42:00">[45:42:00]</a>
*   **Interplay between lab studies and big data**: Combining focused lab experiments to isolate specific questions with large-scale, real-world data analysis. <a class="yt-timestamp" data-t="46:44:00">[46:46:00]</a>

A successful example of this shift is in computer vision. The development of AlexNet, a convolutional network trained on a million natural images, led to a greater advance in understanding object recognition than a century of traditional vision science. <a class="yt-timestamp" data-t="47:49:00">[47:49:00]</a> This demonstrates the power of tackling problems at scale and embracing [[building_ai_applications_for_large_scale_use | real-world challenges]] through engineering and [[the_role_of_data_in_scientific_research | data-driven approaches]]. <a class="yt-timestamp" data-t="48:42:00">[48:42:00]</a>

### Philosophical Considerations for Future Science

Thomas Nagel's "The View from Nowhere" is recommended reading for scientists, as it clarifies what science is and is not, highlighting its strength in providing a "disembodied perspective" (the "view from nowhere") but also its limitations. <a class="yt-timestamp" data-t="50:03:00">[50:03:00]</a> Science excels at objective, quantifiable phenomena, but it has less to say about subjective human experiences (qualia) or first-person perspectives. <a class="yt-timestamp" data-t="53:14:00">[53:14:00]</a> This is why literature, religion, and music continue to be vital, exploring aspects of human experience that science cannot fully capture. <a class="yt-timestamp" data-t="53:55:00">[53:55:00]</a>

The future of science may involve accepting different forms of explanation, where understanding comes from seeing how complex systems like neural networks can solve problems, even if the underlying causal network cannot be fully charted. <a class="yt-timestamp" data-t="30:11:00">[30:11:00]</a> This shift towards [[predictions_and_the_challenges_of_accuracy | prediction]] and models that make intuition "usable" does not have to be dystopian; instead, it promises solutions to global challenges like disease and climate change. <a class="yt-timestamp" data-t="29:18:00">[29:18:00]</a> <a class="yt-timestamp" data-t="25:23:00">[25:23:00]</a> While there's ongoing work in [[mechanistic_interpretability_of_language_models | interpretable AI]], the inherent complexity of reality may mean that the "explanation" ultimately lies in the model's weights and training data, which humans may not fully grasp intuitively. <a class="yt-timestamp" data-t="32:42:00">[32:42:00]</a> This future involves using models to evaluate relationships between fields and make progress, even if the traditional "clean" explanations are not always available. <a class="yt-timestamp" data-t="31:37:00">[31:37:00]</a>