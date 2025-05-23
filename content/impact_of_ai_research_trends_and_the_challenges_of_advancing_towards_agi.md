---
title: Impact of AI research trends and the challenges of advancing towards AGI
videoId: UakqL6Pj9xo
---

From: [[dwarkesh | The Dwarkesh Podcast]]

The pursuit of Artificial General Intelligence (AGI) faces significant hurdles, influenced by current research trends and fundamental unsolved problems in creating truly intelligent systems. This article explores these dynamics, drawing on insights from AI researcher François Chollet and Zapier co-founder Mike Knoop.

## The Current AI Research Landscape: Impact on AGI Progress

Recent shifts in the AI research environment have raised concerns about the pace and direction of progress towards AGI.

### The Trend Towards Closed Research

A significant concern is the increasing closure of frontier AI research. François Chollet argues that OpenAI "basically set back progress to AGI by five to ten years," partly by causing a "complete closing down of frontier research publishing." Mike Knoop echoes this, noting that major publications like the GPT-4 and Gemini papers lacked significant technical details. This contrasts sharply with the open innovation that led to foundational technologies like transformers. Chollet observes that around four years prior, "everything was just openly shared... This is no longer the case," attributing this shift largely to OpenAI's influence. Knoop views this trend as a bet on individual labs over the broader ecosystem, despite the [[open_source_ai_models_and_their_implications | internet and open source]] being powerful innovation engines.

### Dominance of Large Language Models (LLMs)

The rise of LLMs has led to a concentration of resources and research focus. Chollet states that LLMs "have essentially sucked the oxygen out of the room, like everyone is doing LLMs." He elaborates that OpenAI's actions "triggered this initial burst of hype around LLMs," leading to a situation where "all these new resources are actually going to LLMs instead of everything else they could be going to." Chollet even views LLMs as "more of an off-ramp on the path to AGI" [[limitations_of_large_language_models_llms_in_solving_novel_tasks]].

### Impact on Exploring Diverse AI Directions

This dominance and closure has led to a narrowing of research exploration. Chollet contrasts the current environment with 2015-2016, when "the rate of progress was higher because people were exploring more directions." Now, "everyone is very much doing some variation of the same thing." The pressure to publish positive results also means that when "big labs also tried their hand on ARC, but because they got bad results they didn't publish anything," further stifling diverse approaches [[progress_towards_artificial_general_intelligence_agi]].

## Fundamental Challenges in Achieving Artificial General Intelligence (AGI)

Beyond research trends, core conceptual and technical challenges remain in building AGI.

### Distinguishing Skill from True Intelligence

A central challenge is the distinction between acquired skill and genuine intelligence.
*   **The Limits of Memorization:** Chollet describes LLMs as "big interpolative memory," scaled by cramming "as much knowledge and patterns as possible into them." He argues that scaling up such a "database" increases skill and usefulness, but "you are not increasing the intelligence of the system one bit... skill is not intelligence." True intelligence, for Chollet, is "the ability to adapt to things you've not been prepared for," not just "reciting what you've seen before." This is crucial because "you can never pre-train on everything that you might see at test time because the world changes all the time."
*   **The Inadequacy of Current Benchmarks:** Most current LLM benchmarks are seen as "memorization-based benchmarks." Even those testing reasoning can often be solved by memorizing "a finite set of reasoning patterns" or "static programs," effectively using "program fetching" rather than "on-the-fly program synthesis." This applies to benchmarks like GSM8K and even traditional IQ tests, which Chollet suggests can be improved upon through training and memorization. Benchmarks like MMLU and MATH, which "got totally saturated," are also categorized as "tests of memorization." [[arc_as_a_benchmark_for_machine_intelligence_and_its_resistance_to_memorization]]

### The Critical Role of Novelty and Adaptation

The ability to handle novelty is a hallmark of intelligence. Chollet states he would "change my mind about LLMs" if he saw models consistently "adapt on the fly" to "something it has not seen before." This "ability to adapt to novelty on the fly and pick up new skills efficiently" is what he considers being "on the path to AGI." The human species developed intelligence precisely because its environment was not static or predictable. Humans are "born with the ability to learn very efficiently and to adapt in the face of things that we've never seen before." The psychologist Jean Piaget's definition, "intelligence is what you use when you don't know what to do," is cited to underscore this point [[differentiation_between_skill_and_intelligence_in_agi_research]].

### The Need for New Architectural Ideas

Simply scaling existing models is unlikely to achieve AGI.
*   **Beyond Scaling: The Limits of Current Paradigms:** Chollet has consistently maintained that while scaling deep learning pays off in terms of skill, "this will not lead to AGI." He posits that "memory and intelligence are separate components. We have the memory. We don't have the intelligence yet." Referencing genetic influences on human intelligence, he argues, "you really need a better architecture. You need a better algorithm. More training data is not in fact all you need." [[role_of_memory_in_learning_and_understanding]]
*   **Program Synthesis as a Promising Avenue:** Approaches that show promise on difficult generalization tasks like ARC lean "more towards discrete program search, program synthesis." Chollet contrasts deep learning models (differentiable parametric curves, compute-efficient but data-inefficient, local generalization) with program synthesis (discrete graphs of operators, data-efficient but compute-inefficient). He believes "the path forward is going to be to merge the two," creating a hybrid system where "the outer structure is going to be a discrete program search system" guided by deep learning's "intuition in program space." This mirrors System 1 (pattern recognition via deep learning) and System 2 (planning/reasoning via program search) thinking. A system that could truly solve ARC through such means would represent "an entirely new paradigm for software development" based on synthesizing programs from few examples [[the_role_of_deep_learning_and_discrete_program_search_in_ai_development]].

## The ARC Benchmark and Prize: A Catalyst for New Directions

The Abstraction and Reasoning Corpus (ARC) and its associated prize aim to address these challenges and steer research towards more robust forms of intelligence.

### ARC: Testing for Generalization and Inspiring Innovation

ARC was "intended as a kind of IQ test for machine intelligence," specifically "designed to be resistant to memorization." Each puzzle is novel and requires only "core knowledge" (e.g., objectness, counting, basic physics). The benchmark's difficulty for current AI, despite its simplicity for humans, is meant to be "a source of inspiration," prompting researchers to ask why these systems struggle. ARC "requires you to try new ideas" because "existing technology has reached a plateau" in handling such novelty. Its resilience against LLMs, even though released before their prominence, underscores its design against memorization [[arc_as_a_benchmark_for_machine_intelligence_and_its_resistance_to_memorization]].

### The ARC Prize: Fostering Open Research and Breakthroughs

The million-dollar ARC Prize, a collaboration involving Chollet and Knoop, aims to stimulate progress. Knoop was motivated by the "very little objective progress" on ARC despite its importance as a "globally, singularly unique AGI eval." The prize is intended to increase awareness and incentivize work on ARC, especially since hard benchmarks often don't gain traction quickly.
A key goal is to counteract the trend of closed research by "requiring that in order to win the prize money, you put the solution or your paper out into the public domain." The competition is structured to be interactive, with knowledge sharing to "re-baseline the community" annually. Ultimately, "the goal is to accelerate progress towards AGI. A key part of that is that any meaningful bits of progress need to be shared." The prize also serves as a test for ARC itself; if it's easily "hacked," it indicates flaws in the benchmark. A successful, generalizable solution to ARC would be "a huge milestone on the way to AGI." The prize will be increased if ARC "survives three months from here," further incentivizing efforts [[progress_towards_artificial_general_intelligence_agi]].