---
title: Challenges and methodologies in AI research and development
videoId: UTuuTTnjxMQ
---

From: [[dwarkesh | The Dwarkesh Podcast]]

This article outlines the challenges and methodologies in AI research and development, drawing insights from a podcast discussion featuring Sholto and Trenton.

## The Nature of AI Research

AI research, particularly in the context of large language models (LLMs), is characterized by a highly empirical and iterative process. It involves generating ideas, conducting experiments at various scales, interpreting results (often with imperfect information), and refining approaches. Learn more about [[large_language_models_and_transfer_learning | LLM development]] and their limitations in [[limitations_of_large_language_models_llms_in_solving_novel_tasks | solving novel tasks]].

### The Core Research Loop

1.  **Idea Generation and Prioritization:**
    Researchers often have extensive lists of ideas they wish to explore
    <a class="yt-timestamp" data-t="00:41:52">[00:41:52]</a>. A critical skill is
    "shot calling" – deciding which ideas to pursue further based on imperfect
    information and early experimental data
    <a class="yt-timestamp" data-t="00:42:11">[00:42:11]</a>. "Ruthless
    prioritization" is highlighted as a separator of quality research
    <a class="yt-timestamp" data-t="00:46:55">[00:46:55]</a>.

2.  **Experimentation and Scaling:**
    Ideas are tested through experiments, often starting at smaller scales before
    being scaled up. The process involves observing scaling law increments,
    where performance at smaller scales is used to estimate performance for
    larger models <a class="yt-timestamp" data-t="00:42:32">[00:42:32]</a>. However, trends observed at smaller scales do not always hold at larger
    scales, making this an area of imperfect information
    <a class="yt-timestamp" data-t="00:42:52">[00:42:52]</a>,
    <a class="yt-timestamp" data-t="00:43:03">[00:43:03]</a>. For every smooth
    scaling curve presented in papers, there's a "graveyard" of failed runs
    <a class="yt-timestamp" data-t="00:43:26">[00:43:26]</a>.

3.  **Interpretation and Iteration:**
    A significant portion of research involves interpreting why certain ideas
    work and others don't, and understanding what goes wrong
    <a class="yt-timestamp" data-t="00:41:41">[00:41:41]</a>. This involves
    introspection and designing experiments to interrogate model behavior
    <a class="yt-timestamp" data-t="00:41:56">[00:41:56]</a>. Good research often
    comes from working backward from the actual problems one wants to solve
    <a class="yt-timestamp" data-t="00:44:21">[00:44:21]</a>. The cycle time for
    experiments, especially at smaller scales, is crucial and separates
    effective researchers <a class="yt-timestamp" data-t="00:48:02">[00:48:02]</a>.

### Empirical and Evolutionary Nature

Machine learning research is described as "so empirical"
<a class="yt-timestamp" data-t="00:48:08">[00:48:08]</a>. The community is likened to
performing a "greedy evolutionary optimization over the landscape of possible
AI architectures" <a class="yt-timestamp" data-t="00:48:20">[00:48:20]</a>. Progress
is often seen as an aggregation of marginal gains found by many researchers,
rather than a single breakthrough algorithm discovered overnight
<a class="yt-timestamp" data-t="01:00:52">[01:00:52]</a>,
<a class="yt-timestamp" data-t="01:01:03">[01:01:03]</a>. This is compared to
scientific discovery, where breakthroughs are often co-discovered by multiple
people around the same time <a class="yt-timestamp" data-t="01:00:11">[01:00:11]</a>.

## Key Bottlenecks in AI Progress

Several factors constrain the pace of AI research and development:

1.  **Compute:**
    Compute is a significant bounding constraint
    <a class="yt-timestamp" data-t="00:34:23">[00:34:23]</a>. Many labs are
    compute-bound, meaning there are always more experiments they could run if
    more compute were available <a class="yt-timestamp" data-t="00:34:45">[00:34:45]</a>.
    It's estimated that a 10x increase in compute could lead to a roughly 5x
    speed-up in a program like Gemini
    <a class="yt-timestamp" data-t="01:51:14">[01:51:14]</a>-
    <a class="yt-timestamp" data-t="01:51:22">[01:51:22]</a>. The need to
    constantly invest in large training runs (to observe emergent properties
    and ensure research paths remain scalable) also consumes significant
    compute resources <a class="yt-timestamp" data-t="00:52:29">[00:52:29]</a>,
    <a class="yt-timestamp" data-t="00:53:01">[00:53:01]</a>. Learn more about the [[role_of_compute_in_ai_development | role of compute in AI development]].

2.  **"Taste" and Imperfect Information:**
    "Taste," or the intuition for what the right research directions are, is a
    key bottleneck <a class="yt-timestamp" data-t="00:49:54">[00:49:54]</a>.
    Decisions about which experiments to run and how to interpret early data are
    made with "very imperfect information"
    <a class="yt-timestamp" data-t="00:42:16">[00:42:16]</a>,
    <a class="yt-timestamp" data-t="00:50:01">[00:50:01]</a>. What works at a
    small scale might hurt at larger scales, requiring researchers to make
    educated guesses <a class="yt-timestamp" data-t="00:43:07">[00:43:07]</a>.

3.  **Engineering and Organizational Complexity:**
    Software engineering complexity arises from large codebases supporting many
    researchers simultaneously <a class="yt-timestamp" data-t="00:44:53">[00:44:53]</a>.
    Working with others introduces natural slowdowns
    <a class="yt-timestamp" data-t="00:45:27">[00:45:27]</a>. Scaling research
    organizations effectively is a complex problem
    <a class="yt-timestamp" data-t="00:50:18">[00:50:18]</a>,
    <a class="yt-timestamp" data-t="00:50:48">[00:50:48]</a>. Explore more about [[impact_of_ai_on_software_development_and_productivity | AI's impact on software development]].

4.  **Reliability:**
    For AI agents to become truly effective, they need "nines of reliability"
    <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. The inability to
    chain tasks successively with high probability limits agent capabilities
    <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. This is distinct from
    long-context limitations, though some context is needed for long-horizon
    tasks <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

5.  **Data and Evaluation:**
    Generating high-quality data, especially data that involves reasoning
    (reasoning traces), is crucial for model improvement
    <a class="yt-timestamp" data-t="00:55:12">[00:55:12]</a>,
    <a class="yt-timestamp" data-t="00:56:50">[00:56:50]</a>. Verifying the
    correctness of this reasoning is a challenge, addressed in fields like
    geometry through formal verification
    <a class="yt-timestamp" data-t="00:57:34">[00:57:34]</a>. Creating good
    evaluations, especially for long-context capabilities, is difficult, partly
    due to ensuring the evaluation material is not in the training data
    <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>.

## Methodologies and Approaches

### Scaling Laws and Model Size
Scaling laws, which predict model performance based on size and data, are a
cornerstone of LLM development <a class="yt-timestamp" data-t="00:42:32">[00:42:32]</a>.
There's an expectation that as models get larger, they require more compute for
each generational leap (e.g., two orders of magnitude more effective compute)
<a class="yt-timestamp" data-t="01:01:21">[01:01:21]</a>. Larger models also tend to
become more sample efficient <a class="yt-timestamp" data-t="01:07:13">[01:07:13]</a>,
possibly because they are less underparameterized for the complexity of the
task and can form cleaner representations
<a class="yt-timestamp" data-t="01:07:51">[01:07:51]</a>,
<a class="yt-timestamp" data-t="01:08:09">[01:08:09]</a>. Delve into the topic of [[ai_scalability_and_breakthroughs | AI scalability]] for further insights.

### Long Context Windows
The development of long context windows (e.g., million-token context) is
considered an underhyped but significant unlock
<a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>,
<a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. It allows models to
ingest and integrate vast amounts of information, akin to solving the
"onboarding problem" instantly <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>
and showing perplexity improvements normally associated with huge model scale
increases <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Long context
enables models to learn new, esoteric languages in-context better than human
experts <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Understand more on [[understanding_and_leveraging_long_context_lengths_in_llms | leveraging long context lengths in LLMs]].

### Interpretability
Understanding what happens inside models is a major research area.
*   **Superposition:** Models are thought to be dramatically underparameterized for
    the complexity of internet-scale data
    <a class="yt-timestamp" data-t="01:07:51">[01:07:51]</a>. They learn a
    compression strategy called superposition to pack more features than they
    have parameters, especially when data is high-dimensional and sparse
    <a class="yt-timestamp" data-t="01:08:23">[01:08:23]</a>,
    <a class="yt-timestamp" data-t="01:08:40">[01:08:40]</a>. This makes neurons
    polysemantic (firing for multiple unrelated concepts)
    <a class="yt-timestamp" data-t="00:42:52">[00:42:52]</a> (Trenton implies
    neurons in MOE might be polysemantic if not properly disentangled),
    <a class="yt-timestamp" data-t="01:09:35">[01:09:35]</a>. Learn more about [[superposition_and_feature_representation_in_neural_networks | superposition and feature representation]].
*   **Dictionary Learning / Sparse Autoencoders:** Techniques like dictionary
    learning (or using sparse autoencoders) aim to find "monosemantic"
    features by projecting activations into a higher-dimensional sparse space
    <a class="yt-timestamp" data-t="01:09:56">[01:09:56]</a>,
    <a class="yt-timestamp" data-t="01:10:05">[01:10:05]</a>. This is an
    unsupervised method <a class="yt-timestamp" data-t="02:37:41">[02:37:41]</a>.
*   **Feature Splitting:** The number and specificity of learned features depend on
    the capacity given to the (autoencoder) model. More capacity can lead to
    splitting general features (e.g., "bird") into more specific ones (e.g.,
    "raven," "eagle") <a class="yt-timestamp" data-t="02:12:13">[02:12:13]</a>,
    <a class="yt-timestamp" data-t="02:36:43">[02:36:43]</a>. This suggests a
    hierarchical organization that could be exploited for scalable
    interpretability (e.g., depth-first search of feature space)
    <a class="yt-timestamp" data-t="02:40:57">[02:40:57]</a>.
*   **Automated Interpretability:** The goal is to use models to help interpret
    other models, such as labeling features or searching for specific types of
    circuits (e.g., deception circuits)
    <a class="yt-timestamp" data-t="02:35:19">[02:35:19]</a>,
    <a class="yt-timestamp" data-t="02:53:03">[02:53:03]</a>. Discover the potential of [[mechanistic_interpretability_in_ai | mechanistic interpretability in AI]].

### The Role of Data
*   **Synthetic Data:** The generation of high-quality synthetic data, especially
    data embodying reasoning, is seen as a crucial ingredient for model
    progress <a class="yt-timestamp" data-t="00:53:42">[00:53:42]</a>,
    <a class="yt-timestamp" data-t="00:56:50">[00:56:50]</a>. The verifiability
    of this reasoning (e.g., in geometry proofs) is key
    <a class="yt-timestamp" data-t="00:57:34">[00:57:34]</a>. Understand the implications of [[open_source_ai_models_and_their_implications | open-source AI models]] and their role.
*   **Reasoning Traces:** Data that includes the "reasoning traces" behind an
    output is considered highly valuable for training
    <a class="yt-timestamp" data-t="00:55:12">[00:55:12]</a>.
*   **Multimodality:** Training on diverse data types (text, code, images) is
    believed to enable positive transfer, where learning in one modality helps
    in others (e.g., code training improves language reasoning
    <a class="yt-timestamp" data-t="01:32:24">[01:32:24]</a>, math fine-tuning
    improves entity recognition <a class="yt-timestamp" data-t="01:31:17">[01:31:17]</a>).

### Curriculum Learning
Organizing training data in a curriculum, from simpler to more complex
concepts, is mentioned as an approach used in Gemini
<a class="yt-timestamp" data-t="02:27:41">[02:27:41]</a>. The effectiveness of
fine-tuning could be seen as a form of curriculum learning, where the final
training stages have a disproportionate impact
<a class="yt-timestamp" data-t="02:27:44">[02:27:44]</a>.

## The Role of Researchers and Teams

### Key Qualities of Effective Researchers
*   **Agency and Proactiveness:** Taking initiative, not getting blocked easily, and
    pursuing solutions end-to-end ("vertical agency") are crucial
    <a class="yt-timestamp" data-t="01:37:39">[01:37:39]</a>,
    <a class="yt-timestamp" data-t="01:39:04">[01:39:04]</a>,
    <a class="yt-timestamp" data-t="01:40:59">[01:40:59]</a>. This includes fixing
    problems outside one's direct responsibility if it helps the overall
    project <a class="yt-timestamp" data-t="02:03:53">[02:03:53]</a>.
*   **Pragmatism and Broad Toolset:** Effective researchers expand their toolbox,
    drawing ideas from various fields (RL, optimization, systems) rather than
    being tied to a specific academic background
    <a class="yt-timestamp" data-t="00:47:29">[00:47:29]</a>,
    <a class="yt-timestamp" data-t="01:41:18">[01:41:18]</a>. Discover the role of [[reinforcement_learning_from_human_feedback_rlhf | RLHF]] in expanding these toolsets.
*   **Fast Iteration Speed:** The ability to try experiments "really, really,
    really, really, really fast" is a key differentiator
    <a class="yt-timestamp" data-t="00:48:02">[00:48:02]</a>.
*   **Deep Caring:** Caring intensely about the problem, the details, and the
    entire stack leads to thoroughness and a better understanding of potential
    failure modes <a class="yt-timestamp" data-t="02:03:04">[02:03:04]</a>.
*   **High-Leverage Problem Selection:** Identifying and tackling problems that are
    high-impact and perhaps underserved due to structural or organizational
    factors <a class="yt-timestamp" data-t="01:40:33">[01:40:33]</a>.
*   **Understanding the System-Algorithm Interplay:** A deep understanding of how
    systems constrain algorithms and vice-versa is highly valuable
    <a class="yt-timestamp" data-t="01:47:33">[01:47:33]</a>.

### Hiring and Talent Development
*   **Unconventional Paths:** Success stories highlight hiring individuals with high
    enthusiasm and agency, even without traditional ML backgrounds, and pairing
    them with strong mentors <a class="yt-timestamp" data-t="01:46:43">[01:46:43]</a>,
    <a class="yt-timestamp" data-t="01:49:39">[01:49:39]</a>. Examples include
    hiring from consultancy (Sholto
    <a class="yt-timestamp" data-t="01:43:11">[01:43:11]</a>) or based on strong
    independent research/projects (Andy Jones, Simon Boehm
    <a class="yt-timestamp" data-t="02:00:24">[02:00:24]</a>), or even cold emails
    (Chris Olah <a class="yt-timestamp" data-t="01:58:38">[01:58:38]</a>).
*   **Mentorship:** Dedicated mentorship from experienced engineers can rapidly
    accelerate the development of new talent
    <a class="yt-timestamp" data-t="01:46:51">[01:46:51]</a>. 
*   **Looking for Signal:** Recruiters and senior researchers look for signals like
    world-class independent work, insightful questions online, or strong blog
    posts <a class="yt-timestamp" data-t="01:46:17">[01:46:17]</a>,
    <a class="yt-timestamp" data-t="01:59:48">[01:59:48]</a>. Standard interview
    processes are still common but references and external signals play a large
    role <a class="yt-timestamp" data-t="02:01:27">[02:01:27]</a>. Explore more on [[talent_spotting_and_evaluation_in_various_domains | talent spotting and evaluation]] techniques.

## Future of AI Research

### AI Assisting AI Research
The prospect of AI significantly speeding up AI research is a key consideration
for a potential "intelligence explosion."
*   **Augmenting Researchers:** AI could act as a "fantastic Copilot," dramatically
    speeding up coding and other software engineering tasks for researchers
    <a class="yt-timestamp" data-t="00:34:34">[00:34:34]</a>,
    <a class="yt-timestamp" data-t="00:54:10">[00:54:10]</a>. This would allow
    them to run more experiments and iterate faster
    <a class="yt-timestamp" data-t="00:37:41">[00:37:41]</a>. Discover the implications of [[ais_potential_impact_on_software_and_application_development | AI's potential impact on software development]].
*   **Synthetic Data Generation:** AI itself could be a crucial ingredient in model
    capability progress through the generation of high-quality synthetic data
    <a class="yt-timestamp" data-t="00:53:42">[00:53:42]</a>.
*   **Bottlenecks Remain:** Even with AI assistance, compute remains a bottleneck.
    The process of recursive self-improvement would still involve retraining
    new, larger, and more expensive models, acting as a damping mechanism
    <a class="yt-timestamp" data-t="00:38:50">[00:38:50]</a>,
    <a class="yt-timestamp" data-t="00:39:09">[00:39:09]</a>. Gain deeper insights about [[recursive_selfimprovement_and_ai_capabilities | recursive self-improvement in AI]].

### Openness and Academic Contribution
There's a concern that as cutting-edge research becomes concentrated in a few
labs, the signal for academic research on what directions are promising diminishes
<a class="yt-timestamp" data-t="03:07:37">[03:07:37]</a>. Fields like
interpretability, where labs like Anthropic publish openly, are suggested as
highly impactful areas for academic focus that don't require massive resources
<a class="yt-timestamp" data-t="03:08:19">[03:08:19]</a>. There's a call for more
academic work on disentangling neurons in open-source models like Mixtral
<a class="yt-timestamp" data-t="02:45:58">[02:45:58]</a>.

## Conclusion
AI research and development is a dynamic and rapidly evolving field characterized
by empirical methodologies, significant computational and intellectual
challenges, and a strong reliance on the agency and collaborative efforts of
researchers. As models become more capable, the methodologies for understanding,
improving, and ensuring their safety are also under active development, with
[[mechanistic_interpretability_in_ai | interpretability]] and the strategic use of AI itself playing increasingly
important roles.