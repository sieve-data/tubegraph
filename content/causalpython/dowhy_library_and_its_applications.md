---
title: DoWhy library and its applications
videoId: 8yWKQqNFrmY
---

From: [[causalpython]] <br/> 

[[The creation and features of CausalLib|DoWhy]] is an open-source Python library for causal inference, designed to make causal analysis more accessible and user-friendly. It was created by Dr. Amit Sharma and Emre Kiciman, initially as a personal tool to simplify causal inference workflows <a class="yt-timestamp" data-t="00:27:36">[00:27:36]</a>. The library bridges the gap between the graphical models framework and the potential outcomes framework, recognizing that both offer valuable lenses for solving causal problems <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>.

## Origin and Philosophy

The genesis of DoWhy stemmed from the founders' frustration with existing fragmented libraries, which often focused on single aspects like matching or specific regression types, requiring users to piece together complex workflows <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a>. Dr. Sharma found seminal texts like Judea Pearl's "Causality" to be conceptually simple but formally presented, making them difficult for beginners <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>. DoWhy aimed to provide a unified tool that guides users through the entire causal inference process <a class="yt-timestamp" data-t="00:27:20">[00:27:20]</a>.

A core philosophy of DoWhy is its pedagogical approach, structuring causal inference into four distinct steps:
1.  **Model**: Explicitly define causal assumptions using a graph <a class="yt-timestamp" data-t="00:59:15">[00:59:15]</a>.
2.  **Identify**: Determine if the causal effect is identifiable from the data without requiring actual data <a class="yt-timestamp" data-t="00:59:20">[00:59:20]</a>.
3.  **Estimate**: Apply various statistical methods to estimate the causal effect from observational data <a class="yt-timestamp" data-t="01:00:20">[01:00:20]</a>.
4.  **Refute**: Perform robustness checks to challenge the obtained estimate and assumptions <a class="yt-timestamp" data-t="01:00:49">[01:00:49]</a>.

This clear, sequential API design allows users to focus on the crucial modeling step, with defaults for subsequent steps, making it easier for non-experts to engage with causality <a class="yt-timestamp" data-t="01:01:17">[01:01:17]</a>.

## Verification and Refutation in DoWhy

A significant contribution of DoWhy is its emphasis on the "refutation" step, which was inspired by methodologies in economics and biomedical literature <a class="yt-timestamp" data-t="01:00:35">[01:00:35]</a>. This step addresses the challenge of verifying causal models and estimates, especially when randomized control trials are not feasible <a class="yt-timestamp" data-t="01:18:19">[01:18:19]</a>.

Key refutation tests in DoWhy include:
*   **Sensitivity Analysis**: Checking what happens if an unobserved confounder was missed <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
*   **Negative Controls**: Drawing from biomedical lab experiments, this involves:
    *   Adding a random common cause to the analysis <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>.
    *   Replacing the treatment with a placebo (random variable) <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>.
    *   Using a dummy outcome that is a function of confounders but not treatment, expecting a zero causal effect <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>.
*   **Graph Verification**: Initially testing conditional independences derived from the graph structure <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a>. More advanced statistical tests compare the graph's information to a random graph, indicating its informativeness and support from data <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>.

These modules have been enhanced by contributions from researchers like Michael Oust and a team at Amazon, highlighting DoWhy's evolution into a community project <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.

## Evolution and Future: The Py Ecosystem

DoWhy has transitioned into a community project under the new GitHub organization "Py", no longer solely associated with Microsoft <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>. The broader vision for Py is to create a seamless causal ecosystem for solving any causal problem <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>.

This ecosystem integrates DoWhy (focused on effect estimation and root cause analysis) with other prominent [[open_source_causal_ai_libraries|open-source causal AI libraries]] such as:
*   [[causal_discovery_algorithms_and_realworld_applications|Causal Learn]]: For [[causal_discovery_algorithms_and_realworld_applications|causal discovery]] when a graph is not explicitly provided <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>.
*   EconML: For advanced estimation techniques <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>.

The aim is to allow users to interact with a unified "Py" interface that orchestrates these libraries behind the scenes, providing comprehensive analysis from raw data to actionable insights <a class="yt-timestamp" data-t="00:29:08">[00:29:08]</a>.

### PY LLM: Enabling Causal Inference for Non-Experts

A particularly exciting new direction is PY LLM, a library focused on higher-level abstraction and integration with Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:29:33">[00:29:33]</a>. This initiative aims to make [[causal_ai_and_its_application_in_different_sciences|causal inference accessible to non-experts]] and the general public <a class="yt-timestamp" data-t="00:29:56">[00:29:56]</a>. Users will be able to pose causal questions in natural language (text input), and the system, leveraging LLMs and the underlying Py libraries, will provide text-based causal answers or guide the user to provide necessary data <a class="yt-timestamp" data-t="00:30:39">[00:30:39]</a>.

This approach addresses key bottlenecks in traditional causal inference:
*   **Graph Generation**: LLMs can help generate plausible or credible causal graphs, which is often the hardest and most feedback-intensive part of the process <a class="yt-timestamp" data-t="00:33:03">[00:33:03]</a>.
*   **Refutation Test Selection and Interpretation**: LLMs can guide users on which reputation tests to run and how to interpret their results, simplifying what can be an overwhelming choice for many <a class="yt-timestamp" data-t="00:34:39">[00:34:39]</a>.

While LLMs can hallucinate, their utility in streamlining the causal modeling process, especially in generating initial graphs and suggesting tests, is significant <a class="yt-timestamp" data-t="00:35:03">[00:35:03]</a>.

## Causality's Role in Improving LLMs

Beyond using LLMs to enhance causal inference, research within Py also explores how causality can make LLMs more robust. This involves:
*   **Learning Axioms**: Instead of directly imparting complex causal knowledge, the focus is on training LLMs to learn basic causal axioms, such as transitivity and d-separation <a class="yt-timestamp" data-t="00:39:44">[00:39:44]</a>.
*   **Generalization**: Models trained on synthetic axiomatic data (e.g., graphs of size 3-6) have shown surprising generalization capabilities to larger graphs (up to size 14) and new causal tasks (like the Cotoc benchmark), with performance jumps of about 20 percentage points <a class="yt-timestamp" data-t="00:41:15">[00:41:15]</a>.
*   **Addressing Statistical Shortcuts**: While LLMs may still learn statistical shortcuts from passive data, the hypothesis is that exposing them to diverse axiomatic data can constrain the space of these shortcuts, eventually guiding them toward genuine causal principles <a class="yt-timestamp" data-t="00:45:56">[00:45:56]</a>. This aligns with the idea of learning [[the_limitations_of_deep_learning_in_realworld_applications|active causal strategies from passive data]] <a class="yt-timestamp" data-t="00:43:06">[00:43:06]</a>.

This approach suggests a new way of imparting reasoning to LLMs without relying on extensive memorization, potentially leading to more robust and accurate models <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>.

## Conclusion and Community

DoWhy, and the broader Py ecosystem, is an [[open_source_causal_ai_libraries|open-source]] initiative under the MIT license, welcoming contributions from researchers and practitioners alike <a class="yt-timestamp" data-t="01:09:19">[01:09:19]</a>. The community encourages contributions of new methods, feedback, and real-world use cases to demonstrate the impact of [[practical_applications_of_causal_methods|causality in diverse fields]] like healthcare and social sciences <a class="yt-timestamp" data-t="01:10:47">[01:10:47]</a>. The integration with LLMs signifies a belief that the future of computing systems will involve natural language interaction, requiring robust systems that can perform complex causal analysis <a class="yt-timestamp" data-t="00:46:37">[00:46:37]</a>.