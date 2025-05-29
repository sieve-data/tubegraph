---
title: Applications of Causal Inference in Science and Medicine
videoId: yqKJ9pUQ6Q8
---

From: [[causalpython]] <br/> 

The "Coal Bandits" podcast's final guest of its first season is Professor Judea Pearl, often referred to as the "Godfather of modern causality" <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. His work is credited by the host with literally changing the course of their life, particularly through the book *The Book of Why* <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>.

## The Genesis of Causal Inference

Judea Pearl's interest in causality began in high school, motivated by a paradox involving smallpox vaccination in 1840s France <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. Data showed that more people died *from* the vaccination itself than from smallpox, leading to protests against vaccination <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. However, this conclusion was flawed, as the low smallpox deaths were *because* of successful vaccination <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. Pearl sought a formal language to rectify such paradoxes, but the available logical tools at the time lacked the ability to express "died from" <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>.

His pursuit of a language for causality intensified in the 1980s, after his book on Bayesian networks was released <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>. He realized Bayesian networks' success stemmed from their construction in the causal direction <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>. This led to the development of structural causal models (SCMs) around 1991, which formalized counterfactuals using deterministic functions <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>. This shift from two decades of probabilistic reasoning to deterministic functions was initially a "trauma" but proved to be the right path <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>.

## Causal Inference in Artificial Intelligence

### Large Language Models (LLMs) and Causal Learning
Large language models (LLMs) possess a unique advantage in their training data: text produced by humans who inherently have [[causal_inference_concepts_and_applications | causal models]] of the world <a class="yt-timestamp" data-t="13:30:00">[13:30:00]</a>. LLMs can "copy" or "compose" these models through associations, forming a "salad of causal rumors" <a class="yt-timestamp" data-t="14:48:00">[14:48:00]</a>. However, this does not mean they learn [[causal_inference_methods_and_applications | causal models]] directly from data, but rather from existing human-authored models <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.

LLMs demonstrate varying performance on [[causal_inference_concepts_and_applications | causal benchmarks]], sometimes performing well and other times poorly <a class="yt-timestamp" data-t="15:11:00">[15:11:00]</a>. Interestingly, LLMs perform significantly worse when dealing with abstract variables compared to concrete objects (the "baby world") <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>.

### Future of AI and Causal Reasoning
A promising future direction for AI involves developing "automatic scientists" that can determine the best experiments to conduct next <a class="yt-timestamp" data-t="26:25:00">[26:25:00]</a>. This also ties into solving the "scandal of science" concerning the illusion of free will <a class="yt-timestamp" data-t="26:56:00">[26:56:00]</a>.

The process of scientific discovery, such as understanding the cause of malaria (shifting from "bad air from swamps" to mosquitoes), can be seen as local perturbations on existing [[causal_inference_methods_and_applications | causal models]] <a class="yt-timestamp" data-t="29:48:00">[29:48:00]</a>. An automated scientist would propose hypotheses for intervention on an existing model and then design simple experiments to observe changes in outcome <a class="yt-timestamp" data-t="32:00:00">[32:00:00]</a>. This requires leveraging the power of metaphors and reasoning by analogy, an area yet to be fully tackled in AI <a class="yt-timestamp" data-t="33:18:00">[33:18:00]</a>.

## Applications in Medicine and Decision Making

A crucial area for future research is **personalized medicine** and individualized decision-making <a class="yt-timestamp" data-t="18:50:00">[18:50:00]</a>. Recent work has made it feasible to answer questions about the probability and quantification of harm or benefit for specific situations, not just for populations <a class="yt-timestamp" data-t="19:08:00">[19:08:00]</a>. This is vital in medicine, political science (e.g., swing states), business, and marketing <a class="yt-timestamp" data-t="19:15:00">[19:15:00]</a>.

### Challenges in Data Collection
One challenge in applying [[causal_inference_methods_and_applications | causal inference]] is sampling from populations <a class="yt-timestamp" data-t="20:04:00">[20:04:00]</a>. People selected for randomized controlled trials (RCTs) may differ significantly from the general population due to factors like consent and incentives <a class="yt-timestamp" data-t="20:39:00">[20:39:00]</a>. However, in many exercises, both observational and experimental data can be derived from the same underlying causal graph, enabling the narrowing of bounds on individual behavior <a class="yt-timestamp" data-t="20:56:00">[20:56:00]</a>. This ability to combine data types for individual-level insights is highly promising <a class="yt-timestamp" data-t="21:26:00">[21:26:00]</a>.

### Limitations of Randomized Control Trials (RCTs)
While RCTs are often considered the "golden standard" for establishing causation, they have limitations <a class="yt-timestamp" data-t="43:16:00">[43:16:00]</a>. RCTs can answer interventional questions (Level 2 of the Causal Hierarchy) but not counterfactual questions (Level 3) <a class="yt-timestamp" data-t="43:32:00">[43:32:00]</a>. For example, an RCT can show if a drug has no effect on a population, but it cannot distinguish if that means no effect on *any* individual or if it *kills some and saves some* <a class="yt-timestamp" data-t="44:42:00">[44:42:00]</a>. Tools exist today that combine observational and randomized studies to derive bounds on the probability of harm or benefit for individuals <a class="yt-timestamp" data-t="45:06:00">[45:06:00]</a>.

### Causes of Effect and Legal Applications
Questions about "causes of effect," such as direct versus indirect causes or necessary versus sufficient causes, fall beyond the scope of statisticians focused solely on randomized experiments <a class="yt-timestamp" data-t="43:53:00">[43:53:00]</a>. These are crucial in legal settings, where questions like "would the injury have occurred but for the actions of the accused?" are constantly asked <a class="yt-timestamp" data-t="46:23:00">[46:23:00]</a>. The tools to formulate and identify these causal relationships are available, but their education is missing in fields like law <a class="yt-timestamp" data-t="46:40:00">[46:40:00]</a>.

## Bridging the Gap: Causal Inference and the Scientific Community

### The Rift in the Causal Community
There is a perceived rift in the [[causal_inference_methods_and_applications | causal community]] between traditions, such as the potential outcome framework and structural causal models (SCMs) <a class="yt-timestamp" data-t="21:44:00">[21:44:00]</a>. While many now use graphs, different traditions sometimes use different languages to describe the same concepts, leading to duplicated work and misunderstandings <a class="yt-timestamp" data-t="22:19:00">[22:19:00]</a>.

A theorem demonstrates that the potential outcome framework is logically equivalent to SCMs <a class="yt-timestamp" data-t="22:52:00">[22:52:00]</a>. The primary difference lies in comfort level when articulating assumptions <a class="yt-timestamp" data-t="23:22:00">[23:22:00]</a>. Many find graphs more intuitive for expressing knowledge and defending assumptions than relying on abstract concepts like "conditional ignorability" <a class="yt-timestamp" data-t="23:44:00">[23:44:00]</a>.

### Barriers to Broader Adoption
Several factors hinder the broader [[industrial_applications_of_causal_inference | industrial applications of causal inference]]:
*   **Funding** <a class="yt-timestamp" data-t="34:28:00">[34:28:00]</a>
*   **Language** <a class="yt-timestamp" data-t="34:32:00">[34:32:00]</a>
*   **Training** <a class="yt-timestamp" data-t="34:37:00">[34:37:00]</a>
*   **Lack of Platforms** <a class="yt-timestamp" data-t="34:37:00">[34:37:00]</a>
*   **Attention:** People often overlook the limitations predicted by [[causal_inference_methods_and_applications | causal reasoning]] <a class="yt-timestamp" data-t="34:42:00">[34:42:00]</a>.

There is a resistance to paradigm shifts, especially as professionals are rewarded for continuing within existing frameworks <a class="yt-timestamp" data-t="35:14:00">[35:14:00]</a>.

### Education and Shifting Paradigms
A significant shift is needed in education <a class="yt-timestamp" data-t="4:34:00">[4:34:00]</a>. Many statistics departments do not explicitly teach causality <a class="yt-timestamp" data-t="37:51:00">[37:51:00]</a>. Pearl suggests that statistics should be seen as a special branch of [[causal_inference_and_its_applications | causal inference]] dealing with the lower levels of the causal hierarchy <a class="yt-timestamp" data-t="38:08:00">[38:08:00]</a>.

Structural equation models (SEMs), often taught as parsimonious representations of covariance matrices, are truly meaningful because they represent one's [[causal_inference_concepts_and_applications | causal model]] or "knowledge" – data combined with the underlying structure <a class="yt-timestamp" data-t="38:40:00">[38:40:00]</a>. Without a causal understanding, fitting a statistical model to data can lead to incorrect conclusions that do not generalize under distribution shifts <a class="yt-timestamp" data-t="37:18:00">[37:18:00]</a>.

Education should also highlight the limitations of RCTs, which are often presented as the "golden standard" without discussing their inability to answer counterfactual questions <a class="yt-timestamp" data-t="43:16:00">[43:16:00]</a>.

### Causal Discovery
Regarding [[causal_discovery_versus_causal_inference | causal discovery]] software, Pearl clarifies that his work has focused on what can be done *with* a causal model, assuming one has it, rather than how to discover it <a class="yt-timestamp" data-t="52:00:00">[52:00:00]</a>. He acknowledges the significant achievements and improvements in [[causal_discovery_versus_causal_inference | causal discovery]], especially in making assumptions less stringent <a class="yt-timestamp" data-t="52:22:00">[52:22:00]</a>.

### The Future of Causal Inference
The rise of large language models presents both a challenge and an opportunity for [[causal_inference_methods_and_applications | causal inference]] <a class="yt-timestamp" data-t="47:50:00">[47:50:00]</a>. While attention might shift to LLMs, [[causal_inference_and_decision_making | causal inference]] provides the foundational framework and tools to ask and answer questions <a class="yt-timestamp" data-t="48:11:00">[48:11:00]</a>. A hybrid approach combining [[causal_inference_and_its_applications | causal inference]] with LLMs as functional approximators is possible today <a class="yt-timestamp" data-t="25:56:00">[25:56:00]</a>. The increasing awareness of LLM limitations is driving a return to fundamental [[causal_inference_concepts_and_applications | causal questions]] <a class="yt-timestamp" data-t="48:26:00">[48:26:00]</a>. The ability to automatically and efficiently learn user knowledge, treating the user as another environment or black box, is a promising area <a class="yt-timestamp" data-t="49:10:00">[49:10:00]</a>.