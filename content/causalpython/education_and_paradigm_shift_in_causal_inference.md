---
title: Education and paradigm shift in causal inference
videoId: yqKJ9pUQ6Q8
---

From: [[causalpython]] <br/> 

The field of causal inference faces significant [[Communication challenges in causal inference | communication challenges]] and a need for a paradigm shift, particularly in education, to facilitate its broader application and research efficiency <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>.

## Challenges within the Causal Community

There is a noticeable "rift" in the causal community, with different traditions and modes of thinking leading to communication barriers <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>. These include:
*   **Different Languages:** People from various subcommunities, such as the graphical tradition and trialists in epidemiology and economics, often use different terminology to describe the same phenomena <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.
*   **Duplication of Work:** This linguistic and conceptual divide can lead to duplicated research efforts <a class="yt-timestamp" data-t="00:22:33">[00:22:33]</a>.
*   **Misunderstanding of Results:** Disagreements and objections to research findings sometimes stem from fundamental misunderstandings of the underlying concepts or results <a class="yt-timestamp" data-t="00:22:38">[00:22:38]</a>.

Despite these challenges, more individuals are now incorporating graphs into their work <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.

## The Need for a Paradigm Shift in Education

A key barrier to the wider adoption of causal inference is a lack of attention and training in the field <a class="yt-timestamp" data-t="00:34:39">[00:34:39]</a>. This requires a fundamental shift in how causality is understood and taught:

### Reconceptualizing Statistics
Statisticians, traditionally focused on sampling, curve fitting, and data interpolation, often do not recognize the limitations predicted by causal reasoning <a class="yt-timestamp" data-t="00:34:51">[00:34:51]</a>. It is argued that statistics should be considered a "special branch of causal inference" that deals with the lower level of the causal hierarchy (association), while keeping the entire ladder in mind <a class="yt-timestamp" data-t="00:38:05">[00:38:05]</a>. This means:
*   **Redefining Curricula:** Every college should have a causal inference department, or statistics departments should reorient their teaching to reflect the primacy of causality <a class="yt-timestamp" data-t="00:37:51">[00:37:51]</a>.
*   **Moving Beyond Data Fit:** The practice of selecting models based solely on "better fit to the data" (e.g., using Bayesian Information Criterion) is considered "terrible advice" <a class="yt-timestamp" data-t="00:37:08">[00:37:08]</a>. Non-causal models, while fitting data well, may not generalize under distribution shifts, unlike causal models <a class="yt-timestamp" data-t="00:37:33">[00:37:33]</a>.
*   **Emphasizing Meaningful Representation:** Structural equation models (SEMs) are not just parsimonious representations of covariance matrices; they are meaningful because they represent one's causal model or knowledge <a class="yt-timestamp" data-t="00:38:40">[00:38:40]</a>. Knowledge, in this context, is defined as "data plus the ropes behind the data," which is the causal model structure <a class="yt-timestamp" data-t="00:39:22">[00:39:22]</a>.

### Limitations of Randomized Controlled Trials (RCTs)
While RCTs are often taught as the "golden standard for establishing causation," their limitations are frequently overlooked <a class="yt-timestamp" data-t="00:43:16">[00:43:16]</a>.
*   **Population Specificity:** RCTs establish average causal effects for a specific population under experimental conditions <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>. However, people participating in RCTs might differ from the general population <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>.
*   **Non-Transferability:** The results of RCTs do not automatically translate to individual cases or different environments <a class="yt-timestamp" data-t="00:40:26">[00:40:26]</a>. Tools exist today for combining results from multiple experiments and applying them to new environments, but this relies on additional [[Assumptions in causal inference | assumptions]] (e.g., having a graph) that may not be verifiable solely by randomized experiments <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>.
*   **Causal Hierarchy:** RCTs primarily answer interventional questions (level 2 of the causal hierarchy) but cannot answer counterfactual questions (level 3) <a class="yt-timestamp" data-t="00:43:32">[00:43:32]</a>. Questions about causes of effect (e.g., direct vs. indirect cause, necessary vs. sufficient cause) are beyond the reach of statisticians interested only in randomized experiments <a class="yt-timestamp" data-t="00:43:53">[00:43:53]</a>. For instance, an RCT showing "no effect" of a drug cannot distinguish if it truly has no effect on anyone, or if it kills some and saves others <a class="yt-timestamp" data-t="00:44:48">[00:44:48]</a>. [[Causal inference and machine learning | Causal inference]] tools, by combining observational and experimental data, can provide bounds on the probability of harm or benefit for individuals <a class="yt-timestamp" data-t="00:45:13">[00:45:13]</a>.

## Role of Large Language Models (LLMs)

Large language models present a new kind of data environment <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. While they don't learn causal models directly from environmental data, they learn from text produced by people who have causal models of the world, effectively copying or composing these models <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
*   **Limitations:** LLMs can perform well on some causal benchmarks but poorly on others <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. They struggle more with abstract variables than with concrete objects, suggesting they are better at handling the "baby world" <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>. Their behavior is often like a "salad of rumors" about causal models <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
*   **Current Use:** LLMs can be used as functional approximators within a causal inference framework, helping to improve text, find metaphors, and compose expressions <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.
*   **Future Impact:** The Advent of LLMs could either "cover" (bury) or "expose" and "amplify" the results of causal inference <a class="yt-timestamp" data-t="00:47:50">[00:47:50]</a>. Many are becoming aware of LLMs' limitations, inevitably leading them to [[Causal inference and machine learning | causal questions]] for improvement <a class="yt-timestamp" data-t="00:48:24">[00:48:24]</a>.

## Future Directions and Advice for Research

The field should focus on [[challenges_and_future_directions_in_causal_inference | individualized decision-making]] and personalized medicine, including quantifying harm and benefit for specific situations rather than just populations <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.

New areas of exploration include:
*   **Automated Scientists:** Developing AI systems that can decide on the best experiments to conduct next, by applying local perturbations on existing models and experimenting with intervening variables <a class="yt-timestamp" data-t="00:26:20">[00:26:20]</a>.
*   **Free Will:** Understanding the computational advantage of the "illusion of free will" to program systems that act as though they possess it, aiding in human-machine interaction <a class="yt-timestamp" data-t="00:27:03">[00:27:03]</a>.
*   **Learning User Knowledge:** Exploring methods to automatically and efficiently learn a user's knowledge structures <a class="yt-timestamp" data-t="00:49:10">[00:49:10]</a>.

## General Advice for Learning Complex Fields

For those starting in complex fields like mathematics or [[Machine learning and causal inference methodologies | machine learning]], it's advised to:
*   **Start Small:** Do not get into an area that feels too complex <a class="yt-timestamp" data-t="01:00:17">[01:00:17]</a>.
*   **Master a Part:** Find something where you feel you can contribute, master a small part, and then expand from that secure base <a class="yt-timestamp" data-t="01:00:21">[01:00:21]</a>.