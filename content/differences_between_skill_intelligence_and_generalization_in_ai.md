---
title: Differences between skill, intelligence, and generalization in AI
videoId: UakqL6Pj9xo
---

From: [[dwarkesh | The Dwarkesh Podcast]]

Distinguishing between skill, intelligence, and generalization is crucial in the field of Artificial Intelligence (AI), particularly in the pursuit of Artificial General Intelligence (AGI). AI researcher François Chollet emphasizes these distinctions to clarify the capabilities and limitations of current AI models, especially [[article_link | Large Language Models (LLMs)]].

## Defining the Terms

Based on discussions with François Chollet, these concepts can be understood as follows:

### Skill: The Realm of Acquired Proficiencies
Skill, in the context of AI, refers to the ability to perform specific tasks proficiently. For LLMs, skill is often achieved through what Chollet describes as memorization of patterns and knowledge.
*   LLMs are characterized as being very good at memorizing static programs <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> and function as "big interpolative memories" <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   Their capabilities are scaled by "cramming as much knowledge and patterns as possible into them" <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   Performance on benchmarks like GSM8K (grade school math) is seen as a measure of skill, often achieved by memorizing a finite set of reasoning patterns or "static programs" which are then fetched and applied <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>, <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>.
*   Increasing the size of an LLM's "database" (training data) increases its skill and usefulness on memorization-based benchmarks, but this does not equate to an increase in intelligence <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>, <a class="yt-timestamp" data-t="00:19:13">[00:19:13]</a>. Chollet states, "skill is not intelligence" <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.
*   Examples of skill through memorization include LLMs solving Caesar ciphers for common transposition lengths (e.g., 3 or 5) but failing on arbitrary ones (e.g., 9), indicating memorization of specific cases rather than a generalized algorithm <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>. Similarly, high-level chess performance is heavily based on memorization <a class="yt-timestamp" data-t="00:27:56">[00:27:56]</a>.
*   Even if a model like GPT-4 displays a higher degree and range of skills, Chollet argues it may possess the same fundamental degree of (the relevant kind of) generalization as earlier models <a class="yt-timestamp" data-t="00:36:16">[00:36:16]</a>.

### Intelligence: The Capacity for Adaptation and Novelty
Intelligence is defined by the ability to adapt to new, unforeseen situations and to learn efficiently when faced with novelty.
*   Chollet describes "actual intelligence" as the ability to adapt to things one has not been prepared for <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. A key indicator would be a model demonstrating the ability to adapt on the fly to truly novel tasks and pick up new skills efficiently <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>, <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   Human intelligence, according to Chollet, evolved because the world is constantly changing and not a static, predictable environment <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. If it were static, hardcoded behavioral programs would suffice, as seen in many insects <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   Humans possess general intelligence, characterized by being born with little knowledge but a strong capacity to learn efficiently and adapt to the unknown <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   True reasoning, a component of intelligence, involves synthesizing a new problem-solving program on the fly when faced with a puzzle for which no existing program is available in memory <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.
*   Chollet cites developmental psychologist Jean Piaget's definition: "intelligence is what you use when you don't know what to do" <a class="yt-timestamp" data-t="00:58:38">[00:58:38]</a>. It's needed when faced with novelty for which one's experience or evolutionary history has not prepared them <a class="yt-timestamp" data-t="00:58:55">[00:58:55]</a>.
*   The "efficiency of skill acquisition" itself is proposed as a definition of intelligence <a class="yt-timestamp" data-t="01:02:03">[01:02:03]</a>.

### Generalization: Bridging Known and Unknown
Generalization is the ability to apply learned knowledge to new situations. Chollet distinguishes between different types:

*   **Local Generalization (Interpolation):**
    *   LLMs, viewed as "big parametric curves," excel at this type of generalization <a class="yt-timestamp" data-t="00:49:12">[00:49:12]</a>.
    *   This is achieved because LLMs, having finite parameters, must compress their knowledge. They do this by storing reusable bits of programs and expressing new programs in terms of these existing pieces <a class="yt-timestamp" data-t="00:48:22">[00:48:22]</a>, <a class="yt-timestamp" data-t="00:48:34">[00:48:34]</a>. This compression leads to some degree of generalization <a class="yt-timestamp" data-t="00:48:53">[00:48:53]</a>, <a class="yt-timestamp" data-t="00:48:59">[00:48:59]</a>.
    *   This form of generalization is sufficient for tasks that fall within the model's training distribution <a class="yt-timestamp" data-t="00:50:31">[00:50:31]</a>.
    *   The phenomenon of "grokking" in deep learning, where a model transitions from memorization to generalization on a task, is described as an instance of the Minimum Description Length (MDL) principle—essentially memorization plus regularization [[ai_alignment_and_safety_concerns | regularization and AI alignment]] <a class="yt-timestamp" data-t="00:47:04">[00:47:04]</a>, <a class="yt-timestamp" data-t="00:47:43">[00:47:43]</a>. This regularization leads to (local) generalization <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.

*   **Broader/Extreme Generalization:**
    *   This refers to the ability to apply knowledge to truly novel situations, far removed from the training data <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. It is the capacity to "apply your mind to anything at all, to arbitrary things" <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.
    *   Chollet argues that current LLMs largely lack this crucial capability, even as their skill increases <a class="yt-timestamp" data-t="00:36:16">[00:36:16]</a>. Their generalization is "intrinsically limited" because their underlying structure is a parametric curve, suited only for local generalization <a class="yt-timestamp" data-t="00:49:12">[00:49:12]</a>.
    *   This is the type of generalization deemed necessary for AGI and for solving challenges like the ARC benchmark <a class="yt-timestamp" data-t="00:49:25">[00:49:25]</a>.
    *   Achieving it requires moving beyond local interpolation, potentially through different model architectures like discrete program search, which allow for deeper search and adaptation <a class="yt-timestamp" data-t="00:58:11">[00:58:11]</a>.

## The Interplay and Common Confusions

A common pitfall is the confusion between extensive skill and genuine intelligence.
*   **Skill vs. Intelligence:** Chollet emphasizes that high skill across many tasks (being able to "do" many things) is often mistaken for intelligence <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>. However, general intelligence is not merely "task-specific skill scaled up to many skills" because the space of possible skills is infinite <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>. Intelligence is about the *ability to acquire* any new skill efficiently <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>.
*   **Memorization vs. Learning:** There's a debate on whether LLM performance on tasks like algebra represents true "learning" or sophisticated "memorization." The interviewer notes that if a human child solves arbitrary algebra problems, we say they've "learned" algebra, not "memorized" it <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>, <a class="yt-timestamp" data-t="00:42:39">[00:42:39]</a>. Chollet's perspective is that LLMs primarily "fetch" memorized program templates or patterns <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>, <a class="yt-timestamp" data-t="00:26:23">[00:26:23]</a>. He acknowledges humans also use memorization (e.g., learning arithmetic algorithms is memorizing a program <a class="yt-timestamp" data-t="00:42:55">[00:42:55]</a>, and much of school learning is memorization <a class="yt-timestamp" data-t="00:43:34">[00:43:34]</a>), but humans are not limited to it and possess an additional capacity for on-the-fly adaptation.
*   **Scaling Limitations:** While scaling up data and model size demonstrably increases skill and local generalization, Chollet argues this approach alone will not lead to the adaptability characteristic of true intelligence or AGI <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>, [[challenges_and_opportunities_in_deploying_ai_at_scale | challenges in deploying AI]] <a class="yt-timestamp" data-t="00:45:03">[00:45:03]</a>. Differences in human intelligence are suggested to be mostly genetic, implying that a "better architecture" or "algorithm" is needed, not just more training data <a class="yt-timestamp" data-t="01:00:09">[01:00:09]</a>.

## Current AI (LLMs) Through This Lens

*   **Strengths:** LLMs exhibit high skill levels and proficiency in tasks where sufficient training data is available. They possess a degree of local generalization due to the necessity of compressing knowledge <a class="yt-timestamp" data-t="00:48:53">[00:48:53]</a>.
*   **Weaknesses (according to Chollet):**
    *   They struggle with tasks that are truly novel and require adaptation beyond their training, such as those found in the ARC benchmark <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. The reason LLMs don't do well on ARC is attributed to the "unfamiliarity aspect" and the need to [[reinforcement_learning_from_human_feedback_rlhf | synthesize new solution programs]] on the fly <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
    *   Their ability to synthesize new problem-solving programs or significantly adapt existing ones for unfamiliar problems on the fly is considered poor <a class="yt-timestamp" data-t="00:26:23">[00:26:23]</a>, <a class="yt-timestamp" data-t="00:28:17">[00:28:17]</a>. For instance, the Gemini 1.5 example of learning a rare language in context is theorized by Chollet to be a reuse of a pre-mined template from its vast training data <a class="yt-timestamp" data-t="00:28:17">[00:28:17]</a>.
    *   Their performance on tasks like the Caesar cipher (solving it for common but not arbitrary parameters) suggests memorization of specific instances rather than understanding the general algorithm <a class="yt-timestamp" data-t="00:26:52">[00:26:52]</a>.

## The ARC Benchmark: A Test for True Intelligence

The Abstraction and Reasoning Corpus (ARC) benchmark was specifically created by Chollet to measure a system's intelligence by testing its ability to adapt to novelty.
*   It is designed to be resistant to memorization [[arc_as_a_benchmark_for_machine_intelligence_and_its_resistance_to_memorization | and to evaluate machine intelligence]] <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>, <a class="yt-timestamp" data-t="01:05:37">[01:05:37]</a>. Each puzzle is intended to be novel, even if the entire internet has been memorized <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   ARC problems require only "core knowledge" – basic concepts about objectness, counting, elementary physics, etc., possessed by young children <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   The consistent difficulty LLMs face with ARC, despite their vast knowledge, highlights their current limitations in broader generalization and on-the-fly program synthesis <a class="yt-timestamp" data-t="00:26:04">[00:26:04]</a>. If models were truly capable of synthesizing novel programs, however simple, they should be able to solve ARC tasks <a class="yt-timestamp" data-t="00:38:54">[00:38:54]</a>.

## Towards More General AI

Chollet proposes that future progress towards AGI will likely involve a synthesis of different AI paradigms:
*   Current deep learning models, like LLMs, are well-suited for "System 1" type thinking: pattern recognition, intuition, and memorization-based local generalization <a class="yt-timestamp" data-t="00:51:51">[00:51:51]</a>.
*   To achieve "System 2" capabilities like planning, reasoning, and broader generalization, techniques like discrete program search and synthesis are needed <a class="yt-timestamp" data-t="00:51:59">[00:51:59]</a>. Approaches that work well on ARC often lean towards these methods <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   The path forward is envisioned as a hybrid system. This would feature an outer structure of discrete program search, but crucially, deep learning would be leveraged to guide this search, provide intuition, manage common sense knowledge, and overcome the combinatorial explosion typically associated with pure search methods <a class="yt-timestamp" data-t="00:51:37">[00:51:37]</a>, <a class="yt-timestamp" data-t="00:52:37">[00:52:37]</a>, <a class="yt-timestamp" data-t="00:54:21">[00:54:21]</a>. This would enable an on-the-fly synthesis engine capable of true adaptation to novel situations.