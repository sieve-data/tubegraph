---
title: Causal inference in healthcare and astronomy
videoId: CzL0pV6LyRk
---

From: [[causalpython]] <br/> 

Dr. Kieran Gilligan Lee, Head of the Advanced Causal Inference Lab at Spotify, has a diverse background spanning quantum physics and machine learning, with a strong focus on [[Causal inference concepts and applications | causal inference]] <a class="yt-timestamp" data-t="01:50:48">[01:50:48]</a>. His work extends to various domains, including healthcare and astronomy, demonstrating the broad applicability of [[Causal inference and its applications | causal modeling]] <a class="yt-timestamp" data-t="02:09:12">[02:09:12]</a>.

## Causal Inference in Healthcare

Dr. Lee applied [[Causal AI in medicine | causal inference]] <a class="yt-timestamp" data-t="01:51:53">[01:51:53]</a> at a healthcare startup focused on automating medical triage <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. The goal was to help patients interact with a chatbot to extract symptoms and risk factors, then triage or diagnose the underlying disease and recommend appropriate care (e.g., GP, pharmacist, emergency room) <a class="yt-timestamp" data-t="01:16:07">[01:16:07]</a>. In this critical area, trustworthy methods are essential <a class="yt-timestamp" data-t="01:16:33">[01:16:33]</a>.

### Challenges with Correlational Approaches
The startup initially used a disease model, a probabilistic graphical model with nodes for risk factors, diseases, and symptoms, and conditional distributions between links <a class="yt-timestamp" data-t="01:16:43">[01:16:43]</a>. The standard diagnostic approach involved finding the disease with the highest likelihood or posterior given observed symptoms <a class="yt-timestamp" data-t="01:17:19">[01:17:19]</a>. However, this correlational approach presented significant problems <a class="yt-timestamp" data-t="01:17:40">[01:17:40]</a>.

*   **Correlation vs. Causation**: Doctors aim to identify diseases *causing* symptoms so that treating the disease will reduce symptoms <a class="yt-timestamp" data-t="01:17:47">[01:17:47]</a>. Relying on correlation alone can lead to incorrect diagnoses <a class="yt-timestamp" data-t="01:18:02">[01:18:02]</a>.
*   **Example: Chest Pain and Type 2 Diabetes**: When patients presented with chest tightness and pain, the model often indicated type 2 diabetes as the most likely disease <a class="yt-timestamp" data-t="01:18:08">[01:18:08]</a>. Medical professionals, however, confirm that type 2 diabetes does not cause chest pain <a class="yt-timestamp" data-t="01:18:20">[01:18:20]</a>, and there was no direct causal link in the model's graphical structure <a class="yt-timestamp" data-t="01:18:25">[01:18:25]</a>. This correlation arose because chest pain is associated with being overweight, and being overweight is associated with type 2 diabetes, making "being overweight" a confounder <a class="yt-timestamp" data-t="01:18:37">[01:18:37]</a>.

### Solution: Counterfactual Reasoning
The diagnosis problem was reframed as a counterfactual reasoning task using a Pearlian approach <a class="yt-timestamp" data-t="01:19:05">[01:19:05]</a>. This involved asking: "Given the observed symptoms (factual evidence), what would happen to those symptoms if a specific disease were cured (intervened upon and turned off)?" <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>.

*   **Improved Accuracy**: This counterfactual approach significantly improved accuracy. Compared to 44 doctors, the counterfactual method was as good as the top 25% of doctors, whereas the traditional correlational method was only as good as the top 50% <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>. This represented a doubling of accuracy simply by adopting a [[Causal inference and its applications | causal inference]] <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a> perspective <a class="yt-timestamp" data-t="01:49:51">[01:49:51]</a>.
*   **Model Unchanged**: Crucially, the underlying disease model (probabilistic graphical model and parameters) remained exactly the same; only the question asked of the model changed <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>. This demonstrated the power of [[Causal inference concepts and applications | causal inference]] <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a> in making better predictions and inferring future impacts <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

## Causal Inference in Astronomy

After his work in industry, Dr. Lee returned to physics, specifically astronomy, maintaining an honorary position at University College London (UCL) <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

### Why Causal Inference in Astronomy?
Traditional physics often relies on controlled experiments <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. However, in fields like astronomy, controlled experiments are not possible <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>. Observing the night sky means data is observational, necessitating [[Causal inference methods and applications | causal inference]] <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a> to disentangle processes and determine cause-and-effect relationships <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.

### Research Question: Nature vs. Nurture in Galaxy Evolution
A long-standing question in astronomy is whether "nature" (the environment of galaxies) or "nurture" (internal galactic processes) is more important for galaxy evolution <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>. These factors are often entangled <a class="yt-timestamp" data-t="03:48:42">[03:48:42]</a>.

The specific project aimed to address whether the environment of a galaxy influences its star formation rate <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.

*   **Galaxy Types**: There are two main classes of galaxies:
    *   **Big, Red, Massive Galaxies**: Generally, stars do not form in these <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>. They often appear together in clusters, indicating a different environment <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.
    *   **Younger, Blue Galaxies**: Stars actively form in these <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>. They are usually found on their own <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>.

The research sought to determine if this clustering behavior (environment) causally affects the star formation rate, or if it's merely an association due to a common cause <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.

### Methodology and Findings
Researchers developed a causal DAG (Directed Acyclic Graph) based on extensive astronomy literature and domain knowledge to map out causal arrows between different processes <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>. Using data simulations, they identified confounders between the galaxy environment and star formation rate. By controlling for these confounders, they found a "sufficient adjustment set" to ensure that any remaining association was a causal effect, assuming the DAG was correct <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.

*   **Environmental Suppression**: It was found that a denser galaxy environment generally suppresses star formation <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.
*   **Early Universe Anomaly**: A significant discovery was that in the early universe, the environment actually *enables* star formation, a finding not previously known <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>. However, over time, this effect reverses to suppression <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.

These findings highlight how [[Causal inference methods and applications | causal inference]] <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a> can be used to answer fundamental questions about physical and astronomical systems, especially where controlled experiments are impossible <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.

## Building Trust in Causal Models

A common concern about [[Causal inference concepts and applications | causal methods]] <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a> is the reliance on assumptions <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>. However, Dr. Lee views having to explicitly make these assumptions as a benefit, as it forces deep thought about the data generation process <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

### Addressing Assumption Violations
*   **Confounder Control**: While it's impossible to know if all relevant confounders are captured, domain knowledge can help <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. Experts can identify the most important confounders. By understanding how strongly this influences the result, one can set bounds on how much the causal effect estimate might change if other, less important, unmeasured confounders were included <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.
*   **Bounding Causal Effects**: Even if point identification of the causal effect isn't possible, upper and lower bounds can be set <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. If these bounds do not intersect zero, it's possible to confidently state that a causal effect exists and is non-zero <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. This approach leverages the assumptions and their potential violations to still gain confidence in the insights <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.

### Avoiding Naive Controls
A key challenge in [[Industrial applications of causal inference | causal machine learning engineering]] <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a> is the temptation to add all potential confounding variables <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>. However, controlling for too many variables, especially those that are not true confounders (e.g., colliders), can lead to worse estimates <a class="yt-timestamp" data-t="01:4:00">[01:4:00]</a>. It's crucial to first think deeply about the DAG and which variables should be in the adjustment set before implementing engineering solutions <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.

## Surprising Learnings from Industrial Applications

One surprising lesson from applying [[Industrial applications of causal inference | causal modeling in industry]] <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a> is that even if correlations between different actions and an outcome seem consistent, the *relative orderings* of these actions based on their impact can completely flip after controlling for confounding <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>. Actions with small correlations might have larger causal effects than those with strong correlations <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. This highlights that simply selecting the best treatment based on raw correlations is often misleading, as controlling for confounders can vary significantly between treatments <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.