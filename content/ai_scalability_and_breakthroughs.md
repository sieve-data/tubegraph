---
title: AI scalability and breakthroughs
videoId: Nlkk3glap_U
---

From: [[dwarkesh | The Dwarkesh Podcast]]

The remarkable progress in Artificial Intelligence (AI) has been largely driven by the principle of **scaling**, where increasing computational resources, data, and model size leads to more capable systems. This article explores the nature of AI scaling, its predictability, potential limitations, and the breakthroughs it has enabled, based on a discussion with Dario Amodei, CEO of Anthropic <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Understanding AI Scaling

### Definition and Empirical Nature
Scaling in AI refers to the observation that as you increase inputs like compute power and the volume of data, AI models become more intelligent and capable <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. This phenomenon is primarily an empirical fact, observed through experiments and data, rather than one fully understood from first principles <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. The term specifically highlights how the "loss" of a model—its inability to predict the next token in a sequence—scales smoothly and predictably as model size increases (e.g., from Claude-1 to Claude-2) <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

### The Mystery of Smooth Scaling
While the general idea that more data and compute lead to better performance is intuitive, the smoothness of these scaling laws—how predictably performance improves with added parameters or data—remains a puzzle <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. Amodei notes that "we still don't really know for sure" why this smooth scaling occurs so consistently <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

Theoretical ideas attempt to explain this:
*   **Power Law Correlations:** Inspired by physics, this idea suggests that language, like many natural phenomena, has long-tail or power-law correlations. Initial learning captures common patterns (the "fat part of the distribution"), and each subsequent order of magnitude of scale captures more subtle correlations further down the tail <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>, <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **Fractal Manifold Dimension:** Anthropic's Chief Scientist, Jared Kaplan, has proposed explanations involving the fractal manifold dimension of data <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Bucket Analogy:** A simpler analogy compares parameters to a bucket and data to water, where the size of the bucket should be proportional to the amount of water it can hold, suggesting a linear relationship <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. However, this doesn't fully explain the smoothness.

## Predictability and Emergent Abilities

### Predictable Loss vs. Unpredictable Abilities
While the statistical average of performance, like the loss function, is highly predictable (sometimes to several significant figures, akin to physics) <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>, <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>, the emergence of specific abilities is "much less predictable" <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. It's difficult to foresee at what loss level a particular skill, like arithmetic or coding, will appear <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>, <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### Abrupt Emergence and Underlying Processes
Specific abilities, such as addition, can appear to emerge abruptly <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. Mechanistically, what happens during this "snapping into place" of circuits is still unknown and is a subject of research like mechanistic interpretability [[mechanistic_interpretability_in_ai]] <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>, <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. However, even when a model suddenly seems to master an ability (e.g., consistently getting addition right), there's evidence of a continuous process occurring behind the scenes. The probability of the correct answer might climb gradually from extremely low levels (e.g., one in a million) long before the model reliably produces it <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>, <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. Whether this implies a pre-existing, weak circuit strengthening or a poorly functioning one improving is unclear <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>, <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Abilities Not Guaranteed by Scale
Certain attributes, like alignment and values, are not guaranteed to emerge purely from scaling <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. Models trained on next-word prediction are primarily learning facts and understanding the world to predict what comes next, not what *should* be done or valued <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>, <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Potential Limits and Plateaus of Scaling

Amodei expresses personal unlikelihood that scaling laws will simply stop fundamentally <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. However, progress could slow or plateau due to several factors:

### Practical Issues
*   **Data Exhaustion:** While a naive view suggests we might be close to running out of data, Amodei believes this is unlikely to be a blocker due to various data sources and generation methods [[challenges_and_methodologies_in_ai_training_and_data_usage]] <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>, <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>, <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>, <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **Compute Limits:** We could exhaust available compute resources before reaching desired intelligence levels, slowing subsequent progress [[role_of_compute_in_ai_development]] <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. Amodei wouldn't bet on this happening but acknowledges it as a possibility <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

### Fundamental Issues
*   **Architectural Limitations:** If the current architectures (like Transformers) are not optimal, we might hit a wall. For example, LSTMs or RNNs would have different, likely less favorable, scaling slopes due to their difficulty in attending to distant past information <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>, <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   **Loss Function Inadequacy:** If scaling plateaus unexpectedly, Amodei's primary explanation would be a fundamental issue with the "next word prediction" loss function. It might over-focus on common tokens responsible for most entropy, neglecting rarer but essential tokens crucial for high-level tasks like advanced programming, drowning out the critical signal in noise <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>, <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>, <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

## Alternatives if Current Scaling Methods Plateau

If next-token prediction proves insufficient, alternative training methodologies would be necessary, likely involving some form of Reinforcement Learning (RL) [[reinforcement_learning_from_human_feedback_rlhf]] <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>, <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. These include:
*   RL from human feedback (RLHF) <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>
*   RL against an objective <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>
*   Constitutional AI <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>
*   Methods like amplification and debate, which serve as both alignment and training techniques <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

The primary advantage of next-token prediction is its simplicity and the ready availability of data, making it the "easiest thing in the world" for scaling <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>, <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. Shifting to RL would likely slow down progress due to the added complexity of designing the loss function <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>, <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

## Dario Amodei's Journey with Scaling

Amodei's views on scaling formed gradually between 2014 and 2017 <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
*   **Early Exposure (Baidu):** His first AI experience was at Andrew Ng's Baidu group around 2014, working on speech recognition <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>, <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. Tasked with simply making the best system possible with ample data and GPUs, he experimented with adding layers to RNNs, training longer, and varying data repetition, observing consistent scaling patterns <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>, <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. This was almost "beginner's luck" <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   **Influence of Ilya Sutskever:** A pivotal moment was meeting Ilya Sutskever, who conveyed the idea that "the models, they just want to learn" <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>, <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. This "Zen Koan" helped Amodei realize the phenomenon was broader than just speech recognition <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>, <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. The key is to remove obstacles, provide good data and enough operational space, and avoid numerical conditioning issues <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
*   **Generalization:** Between 2014 and 2017, Amodei saw similar scaling patterns in Dota, robotics, and other areas, reinforcing his belief in its generality <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>, <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. He attributes his focus on this "horizontal" scaling aspect, perhaps randomly, to his persistent obsession with that particular direction, while others focused "vertically" on solving specific problems <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>, <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>, <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.
*   **Language as the Key:** The idea that self-supervised learning via next-word prediction could tap into the immense richness and structure of language was crucial <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>, <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. Predicting the next word effectively forces models to solve complex problems, including theory of mind and mathematics <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>, <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.
*   **GPT-1's Impact:** Alec Radford's work on GPT-1 solidified this conviction. GPT-1 demonstrated not only strong language modeling but also the ability to be fine-tuned for diverse tasks, showing it was "halfway to everywhere" <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>, <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>, <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>, <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.

## Algorithmic Progress and Scaling ("Big Blob of Compute")

Amodei views algorithmic progress not necessarily as discrete leaps but often as removing impediments to the "big blob of compute" <a class="yt-timestamp" data-t="01:39:04">[01:39:04]</a>. In a document (not publicly released), he outlined several factors critical for effective scaling <a class="yt-timestamp" data-t="01:39:28">[01:39:28]</a>:
1.  **Number of Parameters:** Model size matters [[large_language_models_and_transfer_learning]] <a class="yt-timestamp" data-t="01:39:50">[01:39:50]</a>.
2.  **Compute:** The amount of computational power used <a class="yt-timestamp" data-t="01:39:56">[01:39:56]</a>.
3.  **Quantity of Data** <a class="yt-timestamp" data-t="01:39:56">[01:39:56]</a>.
4.  **Quality of Data** <a class="yt-timestamp" data-t="01:39:56">[01:39:56]</a>.
5.  **Loss Function:** Must be rich and incentivize the right things <a class="yt-timestamp" data-t="01:40:05">[01:40:05]</a>.
6.  **Symmetries (Architecture):** Architectures must respect relevant data symmetries (e.g., translational for CNNs, time for LSTMs). A weakness of LSTMs/RNNs is their inability to attend over the whole context, artificially closing off information from the distant past. Transformers, in contrast, allow compute/information ("spice") to flow more freely by enabling attention across far distances <a class="yt-timestamp" data-t="01:40:21">[01:40:21]</a>, <a class="yt-timestamp" data-t="01:40:41">[01:40:41]</a>, <a class="yt-timestamp" data-t="01:40:54">[01:40:54]</a>, <a class="yt-timestamp" data-t="01:41:10">[01:41:10]</a>. Algorithmic progress is thus seen as unblocking the compute <a class="yt-timestamp" data-t="01:42:07">[01:42:07]</a>, <a class="yt-timestamp" data-t="01:42:25">[01:42:25]</a>.
7.  **Conditioning:** Numerical stability of optimization (e.g., Adam optimizer working better than standard SGD) <a class="yt-timestamp" data-t="01:41:22">[01:41:22]</a>, <a class="yt-timestamp" data-t="01:41:33">[01:41:33]</a>. (Amodei mentioned a 7th condition but couldn't recall it immediately <a class="yt-timestamp" data-t="01:41:40">[01:41:40]</a>).

While further algorithmic breakthroughs on the scale of Transformers are possible, Amodei suggests that the current trajectory is already so steep that such an invention would speed it up further, but perhaps not dramatically, as progress is already rapid <a class="yt-timestamp" data-t="01:42:46">[01:42:46]</a>, <a class="yt-timestamp" data-t="01:43:10">[01:43:10]</a>.

## Scaling, Intelligence, and Human-Level Performance

### From Impressive Feats to General Intelligence
A surprising aspect of scaling has been the gap between models performing impressively on specific complex tasks (e.g., acing standardized tests, writing stylized theorems) and achieving broad, human-level general intelligence [[artificial_general_intelligence_and_ai_systems]] <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>, <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>. Amodei admits he was surprised by this; in 2020, he thought models like GPT-3 had grasped the "essence of language" and that further progress might rely more on RL than pure scaling <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>, <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>, <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>. However, scaling continued to yield significant improvements <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.

### Intelligence as a Broad Spectrum
The experience with scaling models has revised the understanding of intelligence. Instead of a narrow spectrum where skills emerge uniformly, it appears the "human range is pretty broad," and models achieve human-level competence in different tasks at different times <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>, <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>. Models might be superhuman at constrained writing (e.g., avoiding a specific letter) while still struggling with relatively simple mathematical proofs or making "dumb mistakes" <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>, <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>. This suggests intelligence comprises many domain-specific expertises and skills (like memory), which, while formed in the "blob" of the model, manifest unevenly <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>. This was not Amodei's expectation a decade prior <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>.

### Human vs. AI Skill Overlap
The skills elicited by AI models trained on internet data largely overlap with human skills, especially those with business applications <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>, <a class="yt-timestamp" data-t="00:22:12">[00:22:12]</a>. However, there are differences:
*   **AI Lacks:** True physical embodiment and interaction with the world (though they learn physical models to some extent) <a class="yt-timestamp" data-t="00:22:33">[00:22:33]</a>.
*   **AI Possesses:** Skills humans don't typically have, like fluency in Base64 <a class="yt-timestamp" data-t="00:22:49">[00:22:49]</a>, <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>.

Amodei anticipates that scaling will continue to improve models "across the board," with a "rising tide lift[ing] all the boats," even in areas like math and programming where progress was slower but has accelerated in recent generations of models [[challenges_and_advancements_in_ai_training_techniques]] <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>, <a class="yt-timestamp" data-t="00:23:49">[00:23:49]</a>, <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>.

### Timelines to Human-Level Performance
Amodei estimates that models achieving a level of capability akin to a "generally well-educated human" (able to converse intelligently for an hour or so) could be "not very far away at all," potentially within two or three years <a class="yt-timestamp" data-t="00:27:55">[00:27:55]</a>, <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>, <a class="yt-timestamp" data-t="00:28:21">[00:28:21]</a>. The main factor that could prevent this is a deliberate slowdown for safety or regulatory reasons [[ai_alignment_and_safety_research]] <a class="yt-timestamp" data-t="00:28:29">[00:28:29]</a>. This threshold, however, may not equate to existential risk, AI research takeover, or major economic disruption, which could follow at various later times <a class="yt-timestamp" data-t="00:28:57">[00:28:57]</a>, <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.

## Scaling and Scientific Discovery

Current models, despite having access to vast human knowledge, have not yet made significant new scientific discoveries <a class="yt-timestamp" data-t="00:35:38">[00:35:38]</a>.
*   **Ordinary Creativity:** Models do display "ordinary creativity," like writing in specific styles or drawing novel connections an ordinary person might <a class="yt-timestamp" data-t="00:36:24">[00:36:24]</a>.
*   **Skill Level:** Amodei attributes the lack of major discoveries partly to the models' skill level not yet being high enough; they are often described as "mid" or "B-minus" performers, though this is changing with scale <a class="yt-timestamp" data-t="00:36:41">[00:36:41]</a>, <a class="yt-timestamp" data-t="00:36:50">[00:36:50]</a>.
*   **Cusp of Discovery:** He suggests models are "just on the cusp" of being able to put vast memorized knowledge together for discovery, particularly in complex fields like biology where knowing many facts is crucial <a class="yt-timestamp" data-t="00:37:09">[00:37:09]</a>, <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>, <a class="yt-timestamp" data-t="00:37:54">[00:37:54]</a>, <a class="yt-timestamp" data-t="00:38:02">[00:38:02]</a>.

## Efficiency of Scaled Models

A notable mystery is the sample inefficiency of current AI models compared to the human brain. Models are often orders of magnitude smaller in parameter count (synapses) yet require orders of magnitude more data (words seen) to reach sub-human levels <a class="yt-timestamp" data-t="00:36:44">[00:36:44]</a>, <a class="yt-timestamp" data-t="00:36:50">[00:36:50]</a>, <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>. This discrepancy makes Amodei skeptical of direct biological analogies, preferring to focus on the empirically observed capabilities of the models themselves <a class="yt-timestamp" data-t="01:37:33">[01:37:33]</a>, <a class="yt-timestamp" data-t="01:38:17">[01:38:17]</a>, <a class="yt-timestamp" data-t="01:38:28">[01:38:28]</a>. While the reason for this inefficiency is unclear (perhaps related to multimodal learning in humans [[neuroscience_and_ai_understanding_intelligence]] <a class="yt-timestamp" data-t="01:37:50">[01:37:50]</a>), he believes it doesn't ultimately impede progress if scaling continues effectively <a class="yt-timestamp" data-t="01:38:46">[01:38:46]</a>.

The journey of understanding and harnessing AI scaling continues, with empirical observations often outpacing theoretical explanations, leading to powerful breakthroughs and new questions about the nature of intelligence itself.