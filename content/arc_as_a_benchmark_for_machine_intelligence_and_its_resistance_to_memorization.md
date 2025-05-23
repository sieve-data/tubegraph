---
title: ARC as a benchmark for machine intelligence and its resistance to memorization
videoId: UakqL6Pj9xo
---

From: [[dwarkesh | The Dwarkesh Podcast]]

The Abstraction and Reasoning Corpus (ARC) is a benchmark designed by François Chollet, an AI researcher at Google and creator of Keras, to serve as a type of "IQ test for machine intelligence" [00:01:12]. Its primary distinction from many other AI benchmarks, particularly those used for Large Language Models (LLMs), is its design to be resistant to memorization [00:01:18]. ARC aims to measure an AI's ability to adapt to novel situations and synthesize solutions on the fly, rather than its capacity to recall or interpolate from vast training data.

## Key Characteristics of ARC

ARC puzzles are designed with specific properties to test for genuine problem-solving capabilities.

### Novelty of Puzzles
Each puzzle presented in the ARC benchmark is intended to be novel, meaning it's something a system (or human) has likely not encountered before, even if it has processed the entire internet [00:02:02] [00:02:08]. This novelty is crucial because it requires the solver to reason from scratch for every puzzle, rather than fetching a pre-existing solution from memory [00:08:35].

### Reliance on Core Knowledge
ARC problems do not require extensive specialized knowledge. Instead, they are designed to be solvable using "core knowledge" [00:01:43]. This includes fundamental concepts such as:
*   Objectness (understanding what constitutes an object) [00:01:50] [00:08:02]
*   Counting [00:01:50] [00:08:02]
*   Basic physics (e.g., elementary concepts of how objects interact) [00:01:43]
*   Geometry and Topology [00:08:02]
*   Symmetries [00:08:02]

This is the type of knowledge that a typical four or five-year-old child possesses [00:01:54]. LLMs are considered to possess this core knowledge as well [[limitations_of_large_language_models_llms_in_solving_novel_tasks | limitations of large language models (LLMs) in solving novel tasks]] [00:08:10].

### Resistance to Memorization
A core design principle of ARC is its resistance to memorization-based solutions [00:01:18] [01:05:29]. Chollet argues that many LLM benchmarks can be solved by systems that memorize a finite set of reasoning patterns or "static programs" and then fetch the appropriate program when presented with a similar problem [00:18:13] [00:18:39]. ARC attempts to circumvent this by ensuring each task is unique, thus requiring on-the-fly program synthesis [00:11:13].
If a model were to be trained on millions or billions of ARC-like puzzles, improved performance might still be attributed to memorization due to overlap between training and test tasks [00:02:57] [00:03:09]. However, the intent is that the core test set, being novel, should resist this. Chollet acknowledges that no benchmark is perfect and that with enough scale, it might be possible to "cheat" by brute-forcing the task space [00:40:47] [01:30:16].

## Structure of an ARC Puzzle
An ARC puzzle typically presents:
1.  A few demonstration input-output pairs [00:07:08].
2.  Each pair consists of two grids: an input grid and the corresponding output grid that should be produced [00:07:13].
3.  These demonstration pairs illustrate the nature of the task.
4.  A new test input grid is then provided.
5.  The solver's job is to produce the correct test output grid by inferring the underlying rule from the demonstration pairs [00:07:33].

The grids are small and use a limited set of symbols (10 possible symbols) [00:10:01] [00:10:14].

## Performance of AI Systems on ARC

### Large Language Models (LLMs)
LLMs have generally not performed well on ARC [00:02:17]. Chollet posits this is due to their fundamental reliance on interpolation and pattern matching from their training data [00:01:24]. The "unfamiliarity aspect" of ARC tasks is the primary blocker [00:10:57], as LLMs struggle to synthesize new solution programs on the fly for tasks they haven't seen variants of before [[artificial_intelligence_vs_human_intelligence | Artificial Intelligence vs Human Intelligence]] [00:11:05] [00:26:23]. Even very large models, when first encountering ARC tasks without specific ARC-like pre-training, performed poorly; for example, GPT-3 scored zero on public ARC data around its release [01:25:31].

### Alternative and Hybrid Approaches
Approaches that show more promise on ARC tend towards:
*   **Discrete Program Search/Program Synthesis:** These methods attempt to build programs from a set of primitive operations to solve tasks [00:02:23]. This was state-of-the-art before the Jack Cole approach and involves no deep learning [01:28:32].
*   **Test-Time Fine-Tuning (e.g., Jack Cole's approach):** This involves pre-training an LLM on millions of generated ARC-like tasks and then, crucially, fine-tuning a version of the LLM on-the-fly for *each specific test problem* [00:14:29] [00:15:08]. Chollet views this as a form of program synthesis, where the LLM's learned building blocks are assembled to match the task at test time [[the_role_of_deep_learning_and_discrete_program_search_in_ai_development | the role of deep learning and discrete program search in AI development]] [01:14:39]. This method has achieved scores around 35% with a relatively small (240 million parameter) model [00:13:58].

Chollet suggests the most promising path forward involves merging the deep learning paradigm (for providing building blocks, intuition, and common sense knowledge) with the discrete program search paradigm (for explicit reasoning and on-the-fly synthesis) [[prospects_and_milestones_in_agi_progress | Progress towards Artificial General Intelligence (AGI)]] [00:51:37] [01:29:22].

## Distinguishing Skill from Intelligence
A central theme in Chollet's discussion of ARC is the distinction between skill and intelligence. He argues that scaling LLMs (increasing model size, data, and compute) primarily increases their *skill*—their ability to perform a wider range of tasks based on patterns they've memorized or can interpolate [00:19:25] [00:23:55]. However, this does not necessarily increase their *intelligence*, which he defines as the ability to adapt to novelty, learn efficiently from little data, and solve problems one has not been specifically prepared for [00:04:57] [00:19:30] [00:24:06]. ARC is designed to measure this latter quality [[differences_between_skill_intelligence_and_generalization_in_ai | differences between skill, intelligence, and generalization in AI]].

## The ARC Prize and Future of ARC
To incentivize progress on ARC, a million-dollar prize pool has been launched, with $500,000 for the first team to reach an 85% benchmark on a private test set [00:00:19] [00:50:00] [01:09:35]. The prize also includes annual progress prizes [01:10:06].

ARC itself is not considered perfect. Chollet acknowledges potential flaws, such as some redundancy in tasks or tasks that might be structurally similar to online content [00:40:18] [01:22:33]. Plans exist to release an ARC 2.0 version to address these issues and further refine its ability to measure intelligence robustly [01:22:54]. The original Kaggle competition for ARC in 2020 was partly to test if the dataset was "hackable" [01:25:13], and it largely resisted simple shortcuts at the time [01:25:37].

The ultimate goal of solving ARC, particularly with methods that genuinely adapt using core knowledge rather than brute-force memorization of the task space, is seen as a significant milestone towards Artificial General Intelligence (AGI) [[the_geopolitical_stakes_of_agi_development | The geopolitical stakes of AGI development]] [01:26:08]. It would represent the ability to synthesize problem-solving programs from very few examples, a paradigm shift for software development itself [01:26:26] [[impact_of_ai_on_software_development_and_productivity | Impact of AI on software development and productivity]].