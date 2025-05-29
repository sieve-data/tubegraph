---
title: Intersection of quantum physics and causality
videoId: CzL0pV6LyRk
---

From: [[causalpython]] <br/> 

The intersection of quantum physics and [[causality_and_causal_models | causality]] has been a significant area of Dr. Kieran Gilligan Lee's work, bridging his background in quantum physics with his expertise in [[causality_and_causal_models | causal models]] and [[causality_in_artificial_intelligence | causal AI]] <a class="yt-timestamp" data-t="01:49:50">[01:49:50]</a>. His early research explored this intersection, particularly in relation to the Reichenbach Principle <a class="yt-timestamp" data-t="00:37:50">[00:37:50]</a>.

## Causal Inference and Physical Paradoxes

Similar to how Judea Pearl used [[causality_and_causal_models | causal modeling]] frameworks like Directed Acyclic Graphs (DAGs) to explain statistical paradoxes (e.g., Simpson's Paradox), Dr. Gilligan Lee investigated whether placing quantum phenomena on a firm causal footing could resolve apparent physical paradoxes <a class="yt-timestamp" data-t="02:51:52">[02:51:52]</a>.

### Bell's Theorem and Spooky Action at a Distance

A major focus was Bell's theorem, which addresses Einstein's concept of "spooky action at a distance" <a class="yt-timestamp" data-t="02:59:59">[02:59:59]</a>. This concept describes two widely separated physical systems where measuring or interacting with one instantly reveals information about the other <a class="yt-timestamp" data-t="02:59:59">[02:59:59]</a>. This seems to contradict basic physics principles, as information cannot travel faster than the speed of light <a class="yt-timestamp" data-t="02:59:59">[02:59:59]</a>.

John Bell proposed an analogy using gloves: if two friends take separate boxes, each containing one of a pair of gloves (left-handed or right-handed), when one friend opens their box and finds a right-handed glove, they instantly know the other friend has the left-handed one <a class="yt-timestamp" data-t="03:07:07">[03:07:07]</a>. This seemingly paradoxical immediate knowledge is explained by a common cause: the preparation of the gloves into the boxes <a class="yt-timestamp" data-t="03:07:07">[03:07:07]</a>.

However, Bell demonstrated that this classical common-cause explanation is insufficient for quantum correlations <a class="yt-timestamp" data-t="03:09:59">[03:09:59]</a>. If the common cause were a classical object, quantum correlations would violate constraints on the joint distribution dictated by the DAG, indicating that a classical explanation is not enough <a class="yt-timestamp" data-t="03:09:59">[03:09:59]</a>.

## Quantum Causal Models

This led to formalizing the idea of a Quantum Causal Model <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>. The challenge was to integrate the language of [[causality_and_causal_models | causality]] into a quantum setup, defining how variables are associated via a quantum variable <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>.

### Analogies between Quantum and Structural Causal Models

The key was identifying the quantum analogues of mathematical objects found in standard Structural Causal Models (SCMs):
*   **Deterministic Functions**: In SCMs, these functions, along with hidden variables, generate conditional distributions <a class="yt-timestamp" data-t="03:32:19">[03:32:19]</a>. In quantum mechanics, the analogue of deterministic operations is a **unitary map** <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>, which can give rise to stochastic evolution due to lack of knowledge about the environment <a class="yt-timestamp" data-t="03:41:04">[03:41:04]</a>.
*   **Conditional Distributions**: These are represented by **channel operators** in quantum causal models <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>. A channel operator is a matrix where the diagonal terms are conditional distributions, and the off-diagonal terms describe superposition or coherence between quantum states <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

### Transition from Quantum to Classical

The transition from the micro (quantum) to the macro (classical) realm is described by a process called **decoherence**, which involves losing information to the environment <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>. Mathematically, this means the off-diagonal terms in channel operators go to zero, leaving only the diagonal terms, which are precisely the conditional distributions seen in standard SCMs <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>. Similarly, unitary maps become deterministic maps through decoherence <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>. This provides a clear path for the transition between these two formalisms <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.

## Causality in Macroscopic Physics (Astronomy)

Dr. Gilligan Lee has also applied [[interplay_between_physics_and_causal_inference | causal inference]] to macroscopic physics, specifically astronomy <a class="yt-timestamp" data-t="03:54:56">[03:54:56]</a>. In astronomy, controlled experiments are not possible <a class="yt-timestamp" data-t="03:54:56">[03:54:56]</a>, making [[causality_and_causal_models | causal inference]] an important tool for understanding phenomena like galaxy evolution <a class="yt-timestamp" data-t="03:54:56">[03:54:56]</a>. For example, his work investigated whether the environment of a galaxy causally influences its star formation rate (nature vs. nurture) <a class="yt-timestamp" data-t="03:54:56">[03:54:56]</a>. By developing a DAG based on astrophysics domain knowledge, they identified confounders and showed that a galaxy's environment suppresses star formation, with a surprising finding that it enabled star formation in the early universe <a class="yt-timestamp" data-t="03:54:56">[03:54:56]</a>. This demonstrates the utility of [[interplay_between_physics_and_causal_inference | causal inference]] in physics domains where controlled experiments are not feasible <a class="yt-timestamp" data-t="04:41:40">[04:41:40]</a>.