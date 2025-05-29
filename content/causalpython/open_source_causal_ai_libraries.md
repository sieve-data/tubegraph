---
title: Open source causal AI libraries
videoId: Vz5n5SamDAc
---

From: [[causalpython]] <br/> 

The field of [[causal_ai_and_its_application_in_different_sciences | causal analysis]] is increasingly recognized as crucial for robust decision-making and understanding the world, moving beyond mere correlation to true causation <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This shift is driven by the need for clearer assumptions and confidence in analytical outcomes <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

## The Dy Library

The Dy Library is a foundational open-source project designed to broaden the usage of [[causal_ai_and_its_application_in_different_sciences | causal analysis approaches]] <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. Initially conceived as a pedagogical example for tutorials by Dr. Emre Kiciman and Amit Sharma, it aimed to provide a library for coding examples to educate more people about these methods <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

Dy is structured around four essential stages of [[causal_ai_and_its_application_in_different_sciences | causal analysis]] <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>:
1.  **Model and Assumption Generation**: Coming up with causal models and their underlying assumptions <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
2.  **Causal Estimand Identification**: Analyzing models to identify a causal estimand and determining an approach to answer a causal question <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.
3.  **Statistical Estimation**: Performing statistical estimation to calculate values from data <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
4.  **Assumption Validation/Refutation**: Validating or attempting to refute initial assumptions <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.

This four-step process applies regardless of the specific [[causal_ai_and_its_application_in_different_sciences | causal estimation methods]] used <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>. As Dy gained practical utility, its development became more robust, leading to a broader initiative with many contributors <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.

## The Piy Organization

Dy's evolution led to its transition into the Piy organization <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. Originally an open-source project under Microsoft's GitHub, the move to an independent organization was driven by the desire to continue growing and fostering the [[causal_ai_and_its_application_in_different_sciences | causal inference]] community <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. This allowed for significant contributions from other major entities, including Amazon, MIT, Columbia, and Carnegie Mellon, which contributed the `causal-learn` package (the Python version of the TETRAD algorithms) <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>, as well as contributions from Wise <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>.

This collaboration between competitors like Microsoft and Amazon in an open-source tool highlights the shared belief that empowering the community with [[causal_ai_and_its_application_in_different_sciences | causal analysis]] makes data and computing more valuable for everyone <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.

## Challenges and Future Directions

Despite significant [[advancements_in_causal_modeling_and_ai | advancements in causal modeling and AI]], challenges remain in the broader adoption and development of [[causal_ai_and_its_application_in_different_sciences | causal AI]].

### Challenges
*   **Widespread Deployment**: Getting [[causal_ai_in_business_applications | causal methods deployed]] more widely across industries and society for decision-making <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
*   **Education**: Improving understanding of basic [[causal_ai_and_its_application_in_different_sciences | causal Concepts]] and how to work with them <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Complex Modeling**: Developing approaches for more complex physical processes, especially those with feedback loops over time <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Accessibility of Advanced Concepts**: Making concepts like partial identification, sensitivity analysis, and proximal learning more accessible to users, as they are currently underutilized despite their potential impact on applied [[causal_ai_and_its_application_in_different_sciences | causal inference]] <a class="yt-timestamp" data-t="00:37:45">[00:37:45]</a>.

### Future Directions for Piy and Causal AI
*   **Integration with Large Language Models (LLMs)**: An exciting project is `Piy-LLM`, an experimental library focused on incorporating LLMs into the [[causal_ai_and_its_application_in_different_sciences | causal analysis]] process <a class="yt-timestamp" data-t="00:40:35">[00:40:35]</a>. This includes using LLMs to:
    *   Generate [[causal_ai_and_its_application_in_different_sciences | causal graphs]] <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.
    *   Critique causal assumptions <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.
    *   Suggest potential missing data and confounders <a class="yt-timestamp" data-t="00:40:54">[00:40:54]</a>.
    *   Potentially assist with identification-style analyses (e.g., identifying instrumental variables) and even code generation for analyses <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>.
*   **Modeling Complex Physical Systems**: Exploring how Foundation Models can help better model complex physics-style systems, potentially opening up [[causal_ai_and_its_application_in_different_sciences | causal models]] to a broad set of applications <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a>.
*   **Improving Community Resources**: The [[causal_ai_and_its_application_in_different_sciences | causal Python]] community, including libraries like `causal-py`, is healthy, but continued focus on solving real-world problems through broad approaches (algorithms, software engineering, documentation) is needed to make the technology more useful and applicable <a class="yt-timestamp" data-t="00:35:35">[00:35:35]</a>.

The development of open-source libraries like Dy and its evolution into Piy underscore a collaborative effort to make [[causal_ai_and_machine_learning_intersection | causality and machine learning]] more accessible and impactful.