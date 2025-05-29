---
title: Application of quantum physics principles in causal AI
videoId: CzL0pV6LyRk
---

From: [[causalpython]] <br/> 

Dr. Kieran Gilligan Lee, Head of the Advanced [[causal_ai_and_its_application_in_different_sciences | Causal Inference]] Lab at Spotify, has a background in quantum physics and has explored the intersection of quantum physics and [[causality_in_ai | causality]] <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. His work includes research published in Nature journals and accepted at top machine learning conferences <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. He chose to study quantum physics to maintain his "joy of building" that he developed from loving Lego as a child <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Early Work: Quantum Physics and Causality

Dr. Gilligan Lee's early work focused on applying [[causality_in_ai | causal inference]] to quantum physics, aiming to understand phenomena at a deeper level <a class="yt-timestamp" data-t="00:28:47">[00:28:47]</a>. This inspiration came from Judea Pearl's early work, which used [[causal_models_in_biology_and_ai | causal modeling]] frameworks like Directed Acyclic Graphs (DAGs) to explain apparent statistical paradoxes such as Simpson's Paradox and Lord's Paradox <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>. In quantum physics, there are also seemingly paradoxical phenomena like Schrödinger's Cat and "spooky action at a distance" <a class="yt-timestamp" data-t="00:28:33">[00:28:33]</a>.

### Bell's Theorem and the Glove Analogy
A significant paradox considered was Bell's Theorem, developed by Irish physicist John Bell <a class="yt-timestamp" data-t="00:29:03">[00:29:03]</a>. Bell's work commented on a paper by Einstein, Podolsky, and Rosen, which introduced the concept of "spooky action at a distance," where measuring or intervening on one of two very distant physical systems can instantly reveal information about the other <a class="yt-timestamp" data-t="00:29:18">[00:29:18]</a>. This phenomenon seems counter to the principle that information cannot travel faster than light <a class="yt-timestamp" data-t="00:29:40">[00:29:40]</a>.

Bell illustrated this with a simple analogy: if a person takes a left-handed and a right-handed glove, puts each into a separate box, and gives them to two friends traveling to different parts of the world, when one friend opens their box and finds, for example, the right-handed glove, they instantly know the other friend has the left-handed glove <a class="yt-timestamp" data-t="00:30:07">[00:30:07]</a>. In this classical example, the association is explained by a common cause – the initial preparation of the gloves into the boxes <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>.

However, Bell showed that this classical common cause explanation is insufficient for quantum correlations <a class="yt-timestamp" data-t="00:30:59">[00:30:59]</a>. If the common cause were a classical object or random variable, the quantum correlations would violate constraints predicted by the DAG model <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>. This suggested that a different causal explanation was needed <a class="yt-timestamp" data-t="00:31:28">[00:31:28]</a>.

The starting point for Dr. Gilligan Lee's paper was to formalize the language of [[causality_in_ai | causality]] within a quantum setup, addressing how to define relationships via a quantum variable <a class="yt-timestamp" data-t="00:31:59">[00:31:59]</a>.

### Quantum Causal Models
Quantum causal models involve finding quantum analogies for the mathematical objects used in standard Structural Causal Models (SCMs) with classical random variables <a class="yt-timestamp" data-t="00:33:18">[00:33:18]</a>.
*   **Deterministic Operations**: In quantum physics, unitary maps serve as the analogue of deterministic functions <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>.
*   **Conditional Distributions**: Channel operators are the quantum equivalent of conditional distributions <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>. These operators are large matrices where the diagonal terms represent conditional distributions, and the off-diagonal terms describe the superposition or coherence between different quantum states <a class="yt-timestamp" data-t="00:35:37">[00:35:37]</a>.

A smooth transition from the quantum level to the macro scale (structural causal models) can be explained through the process of decoherence <a class="yt-timestamp" data-t="00:35:58">[00:35:58]</a>. As a system undergoes decoherence, losing information to the environment, the off-diagonal terms in the channel operators go to zero <a class="yt-timestamp" data-t="00:36:08">[00:36:08]</a>. This leaves only the diagonal terms, which are precisely the conditional distributions seen in standard SCMs <a class="yt-timestamp" data-t="00:36:17">[00:36:17]</a>. Similarly, unitary maps become deterministic maps during this process <a class="yt-timestamp" data-t="00:36:23">[00:36:23]</a>.

## Reichenbach's Principle
The discussion of correlations and causality in quantum physics ties into Reichenbach's Principle <a class="yt-timestamp" data-t="00:24:17">[00:24:17]</a>. This philosophical principle states that if two things are correlated, there must be an explanation <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>.
*   **Common Cause**: There could be a common cause in their mutual past that explains the association <a class="yt-timestamp" data-t="00:24:26">[00:24:26]</a>.
*   **Statistical Fluctuation**: Alternatively, if the number of data points is small, the correlation could just be a random statistical fluctuation <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.

In quantum physics, Bell's Theorem demonstrates that quantum correlations cannot always be explained by classical common causes in line with Reichenbach's Principle <a class="yt-timestamp" data-t="00:31:02">[00:31:02]</a>.

## Future Applications of Causal Inference
Dr. Gilligan Lee believes that [[causality_in_ai | causal inference]] has a lot to offer beyond merely quantifying the effects of interventions <a class="yt-timestamp" data-t="00:50:23">[00:50:23]</a>. He aims to push the use of [[causal_ai_and_its_application_in_different_sciences | causal AI]] to drive decisions and build new products <a class="yt-timestamp" data-t="00:50:04">[00:50:04]</a>.

One promising area is [[causal_reasoning_in_artificial_intelligence | causal representation learning]] <a class="yt-timestamp" data-t="00:53:27">[00:53:27]</a>. In big tech companies like Spotify, embeddings (representations) of users or products are typically learned from co-occurrence data, which relies on correlations <a class="yt-timestamp" data-t="00:53:31">[00:53:31]</a>. Since recommendation engines aim to find "treatments" (content) to "cause" an outcome (enjoyment), using embeddings based solely on correlations might not be optimal <a class="yt-timestamp" data-t="00:53:57">[00:53:57]</a>. Learning a causal representation of users could identify the underlying factors that explain why users are similar or why they enjoyed certain content, potentially leading to improved recommendations <a class="yt-timestamp" data-t="00:54:10">[00:54:10]</a>.

If successful in a "lower-stakes" environment like music recommendations (where a bad song choice is not critical), this approach could be extended to higher-stakes domains like [[causal_ai_in_medicine | medicine]] <a class="yt-timestamp" data-t="00:53:03">[00:53:03]</a>.