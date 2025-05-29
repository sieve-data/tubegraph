---
title: Causal modeling in healthcare and astronomy
videoId: CzL0pV6LyRk
---

From: [[causalpython]] <br/> 

Dr. Kieran Gilligan Lee, Head of Advanced Causal Inference Lab at Spotify, applies [[causal_inference_and_machine_learning | causal inference]] in diverse fields, ranging from quantum physics to astronomy and healthcare. He emphasizes that understanding problems from a causal perspective is crucial for businesses to take effective actions <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Causal Modeling in Healthcare

Dr. Gilligan Lee previously worked at a healthcare startup focused on automating medical triage <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. The goal was to help patients by extracting symptoms and risk factors via a chatbot, then triaging them to the appropriate medical professional (GP, pharmacist, or emergency room) <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. Trustworthy methods are critical in this high-stakes environment due to the potential consequences of wrong recommendations <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.

### The Problem with Correlation in Diagnosis

The startup initially used a traditional diagnostic approach based on a probabilistic graphical "disease model" created by medical professionals and epidemiologists <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>. This model included nodes for risk factors, diseases, and symptoms, with conditional distributions between them <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>. The standard method involved identifying the disease with the highest posterior likelihood given observed symptoms <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.

However, this correlation-based approach proved problematic. A clear example was a patient presenting with chest tightness and pain <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>. The model indicated type two diabetes as the most likely disease <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>. This was counter-intuitive to medical professionals, as type two diabetes does not cause chest pain <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>. The association was explained by a common confounder: being overweight. Patients with chest pain were more likely to be overweight, and overweight individuals had a higher chance of developing type two diabetes, creating a strong correlation without a causal link <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>.

### Counterfactual Reasoning for Improved Accuracy

To address this, the diagnosis problem was reframed as a counterfactual reasoning task <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>. This approach asked: given the observed symptoms, what would happen to those symptoms if a specific disease were cured (i.e., intervened upon and "turned off" in the model)? <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.

This causal approach significantly improved diagnostic accuracy <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>. When compared to 44 doctors, the counterfactual method achieved an accuracy comparable to the top 25% of doctors, whereas the correlation-based Bayesian inference was only as good as the top 50% <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. Notably, the underlying disease model remained the same; only the question asked of it changed from correlational to causal <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>. This demonstrated the power of [[causal_inference_and_machine_learning | causal inference]] in making better predictions and influencing future outcomes <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.

## Causal Modeling in Astronomy

Upon returning to physics research at University College London, Dr. Gilligan Lee applied [[causal_inference_and_machine_learning | causal inference]] to astronomy, an area where traditional controlled experiments are impossible <a class="yt-timestamp" data-t="00:37:07">[00:37:07]</a>. Causal tools are therefore essential for disentangling processes and understanding cause-and-effect relationships in the cosmos <a class="yt-timestamp" data-t="00:38:09">[00:38:09]</a>.

### Nature vs. Nurture in Galaxy Evolution

A central question in astronomy concerns the evolution of galaxies: whether "nature" (their environment) or "nurture" (internal processes) is more important <a class="yt-timestamp" data-t="00:38:29">[00:38:29]</a>. These factors are often entangled <a class="yt-timestamp" data-t="00:38:45">[00:38:45]</a>.

Dr. Gilligan Lee, in collaboration with Seil Mukes, Offer Laav, and Will Harley, investigated whether a galaxy's environment influences its star formation rate <a class="yt-timestamp" data-t="00:38:56">[00:38:56]</a>. Galaxies are typically classified as either large, red, massive galaxies (where stars generally don't form) or younger, blue galaxies (where stars do form) <a class="yt-timestamp" data-t="00:39:11">[00:39:11]</a>. Red galaxies tend to cluster, while blue galaxies are often isolated <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>. The research aimed to determine if this clustering behavior had a causal effect on star formation or if it was merely an association due to a common cause <a class="yt-timestamp" data-t="00:39:40">[00:39:40]</a>.

### Using DAGs and Confounders

The team meticulously analyzed astronomy literature and domain knowledge to construct a Directed Acyclic Graph (DAG) for galaxy evolution, mapping out causal arrows between different processes <a class="yt-timestamp" data-t="00:39:51">[00:39:51]</a>. They then identified confounders between the galaxy environment and star formation rate <a class="yt-timestamp" data-t="00:40:20">[00:40:20]</a>. By controlling for these confounders (using a "sufficient adjustment set"), they could ascertain the true causal effect <a class="yt-timestamp" data-t="00:40:37">[00:40:37]</a>.

The findings suggested that a denser environment generally suppresses star formation in galaxies <a class="yt-timestamp" data-t="00:40:51">[00:40:51]</a>. However, a surprising discovery was that in the early universe, a dense environment actually enabled star formation, a phenomenon not previously known <a class="yt-timestamp" data-t="00:41:14">[00:41:14]</a>. These results were submitted for publication <a class="yt-timestamp" data-t="00:41:30">[00:41:30]</a>. This project demonstrates how [[causal_inference_and_machine_learning | causal inference]] can answer fundamental questions about physical systems in contexts where controlled experiments are not feasible <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>.

## Building Trust in Causal Models

Dr. Gilligan Lee highlights that making assumptions upfront in causal modeling is a benefit, as it forces deep thought about the data generation process <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. While it's impossible to perfectly capture all relevant confounders, techniques like sensitivity analysis can quantify how much causal estimates might change if assumptions are slightly violated <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. By understanding how violations lead to changes in effect estimation, bounds can be set on the causal effect, providing confidence even if point identification isn't possible <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>. This ability to gain confidence despite uncertainty is a feature, not a bug, of [[causal_inference_and_machine_learning | causal inference]] <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

## Challenges in Causal Machine Learning Engineering

A key challenge in [[machine_learning_and_causal_inference_methodologies | causal machine learning engineering]] is the naive temptation to include all potential confounding variables <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. However, controlling for variables that are not true confounders (e.g., colliders) can lead to worse estimates <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. Therefore, a crucial prior step is to deeply analyze the causal DAG to determine the appropriate adjustment set before applying estimators <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. The characteristics of the data, such as variance in confounder values, should also guide the choice of methodology to ensure reasonable control over the variance of causal effect estimates <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.

## The Common Denominator

Dr. Gilligan Lee finds a unifying theme in all his diverse activities: the ability to ask deep, interesting questions <a class="yt-timestamp" data-t="00:42:26">[00:42:26]</a>. He views [[causal_inference_and_machine_learning | causal inference]] as a field that marries foundational philosophical inquiries (like Democratus's pursuit of true causes <a class="yt-timestamp" data-t="00:43:15">[00:43:15]</a>) with practical, useful applications <a class="yt-timestamp" data-t="00:43:31">[00:43:31]</a>. This combination of seeking fundamental understanding and building useful tools is what excites him <a class="yt-timestamp" data-t="00:43:45">[00:43:45]</a>.

His past experiences, from enjoying Lego as a child and wanting to be an engineer <a class="yt-timestamp" data-t="00:43:59">[00:43:59]</a>, to his academic pursuit of foundational questions in physics, led him to [[causal_inference_and_machine_learning | causal inference]] as the perfect area to combine applied work with answering fundamental questions about the world <a class="yt-timestamp" data-t="00:44:16">[00:44:16]</a>.

<br>
<br>
**References:**
*   Bell, John. *Speakable and Unspeakable in Quantum Mechanics*. <a class="yt-timestamp" data-t="00:47:40">[00:47:40]</a>
*   Pearl, Judea. *Causality: Models, Reasoning, and Inference*. <a class="yt-timestamp" data-t="00:48:51">[00:48:51]</a>
*   Vaart, Victor van der, and collaborators. *Sense and Sensitivity Analysis*. <a class="yt-timestamp" data-t="00:45:33">[00:45:33]</a>
*   Pearl, Judea, and collaborators. *Equality Constraints and Causal Inference*. <a class="yt-timestamp" data-t="00:46:27">[00:46:27]</a>