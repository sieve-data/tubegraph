---
title: Utilities and evolution of the DoWhy library
videoId: 8yWKQqNFrmY
---

From: [[causalpython]] <br/> 

DoWhy is an open-source Python library designed to simplify causal inference by providing a structured workflow. It was created by Dr. Amit Sharma and Emre Kiciman of Microsoft Research India, motivated by the challenges in applying causal inference techniques from academic literature to real-world problems <a class="yt-timestamp" data-t="00:27:07"></a>.

The library gained significant traction due to its pedagogical approach and user-friendly design, making computational causality accessible to a wider audience <a class="yt-timestamp" data-t="01:02:03"></a>.

## Origin Story

The development of DoWhy stemmed from the personal frustrations of its creators while studying causal inference. Early experiences with established texts, such as Judea Pearl's "Causality," highlighted that while core concepts like backdoor paths were simple, their formal presentation made them difficult to grasp for beginners <a class="yt-timestamp" data-t="00:25:26"></a>. Additionally, the field appeared fragmented, with distinct frameworks like graphical models and potential outcomes often presented as competing rather than complementary <a class="yt-timestamp" data-t="00:26:07"></a>.

The founders realized that graphical models excel at framing problems and communicating assumptions, while potential outcome methods (like propensity score-based techniques) are effective for estimation <a class="yt-timestamp" data-t="00:26:29"></a>. This insight led to the vision of a single tool that integrates these complementary approaches, streamlining the entire causal inference process <a class="yt-timestamp" data-t="00:27:02"></a>. Initially conceived for personal reuse, DoWhy was open-sourced and quickly gained popularity <a class="yt-timestamp" data-t="00:27:36"></a>.

## The Four Steps of Causal Analysis

DoWhy structures causal analysis into four distinct, sequential steps, reflecting a principled approach to scientific inquiry <a class="yt-timestamp" data-t="00:59:59"></a>:

1.  **Model**: Define the causal assumptions by building a causal graph. This step does not require data <a class="yt-timestamp" data-t="00:59:15"></a>. Users should spend the maximum amount of time here, ensuring the graph accurately represents their domain knowledge <a class="yt-timestamp" data-t="01:01:17"></a>.
2.  **Identify**: Determine if the causal effect can be identified from the given data and graph. This step also does not require the actual data <a class="yt-timestamp" data-t="00:59:20"></a>.
3.  **Estimate**: Compute the causal effect using various estimation methods, drawing from the potential outcomes literature <a class="yt-timestamp" data-t="00:59:20"></a>.
4.  **Refute**: Test the robustness of the estimated causal effect against various assumptions and potential biases <a class="yt-timestamp" data-t="00:19:05"></a>. This step is crucial because, like scientific theories, causal estimates can only be disproven, not definitively proven correct <a class="yt-timestamp" data-t="01:00:42"></a>.

This structured workflow helps users understand *why* each step is performed separately, moving from theoretical modeling to empirical estimation and rigorous validation <a class="yt-timestamp" data-t="01:02:52"></a>.

## Key Features and Evolution

DoWhy's initial focus was on effect estimation from observational data, but its development quickly expanded to include robustness checks and verification mechanisms <a class="yt-timestamp" data-t="00:18:08"></a>.

### Robustness Checks and Refutation Tests
The `refute` step in DoWhy incorporates various methods to assess the reliability of causal estimates:
*   **Sensitivity Analysis**: Checks what happens if an unobserved confounder was missed <a class="yt-timestamp" data-t="00:20:05"></a>.
*   **Negative Controls**: Inspired by biomedical literature, these tests involve re-running experiments or analyses after removing elements believed to be irrelevant (e.g., removing a reagent in a lab experiment) <a class="yt-timestamp" data-t="00:20:27"></a>.
    *   **Random Common Cause**: Adds a random common cause to the analysis, which should not significantly alter the causal effect <a class="yt-timestamp" data-t="00:20:59"></a>.
    *   **Placebo Treatment**: Replaces the actual treatment with a random variable, expecting a causal effect of zero <a class="yt-timestamp" data-t="00:21:07"></a>.
    *   **Dummy Outcome**: Randomizes the outcome variable or makes it a function of confounders but not the treatment, expecting a causal effect of zero <a class="yt-timestamp" data-t="00:21:31"></a>.
*   **Overlap Tests**: Checks the overlap of treatment across different confounding variables, indicating where estimates are more trustworthy <a class="yt-timestamp" data-t="00:22:20"></a>.

### Graph Verification
More recently, DoWhy has focused on verifying the causal graph itself, moving beyond just checking the estimation process <a class="yt-timestamp" data-t="00:22:52"></a>. While initial versions tested conditional independencies implied by the graph <a class="yt-timestamp" data-t="00:23:17"></a>, newer statistical tests compare the graph's information content against random graphs, providing confidence in how informative and data-supported the graph is <a class="yt-timestamp" data-t="00:23:36"></a>.

### Community Contributions
DoWhy has evolved into a [[open_source_contributions_in_causal_modeling | community project]], with significant contributions from external researchers and teams, including those from Amazon and MIT <a class="yt-timestamp" data-t="00:24:02"></a>.

## Future Directions and Integration

The future of DoWhy is envisioned as part of a broader ecosystem (`py-why`), aiming for seamless causal inference experiences <a class="yt-timestamp" data-t="00:28:22"></a>.

### The PY Ecosystem
The `py-why` GitHub organization now hosts DoWhy and integrates with other libraries to provide a comprehensive solution for various causal problems:
*   **DoWhy**: Primarily focused on effect estimation <a class="yt-timestamp" data-t="00:28:29"></a>.
*   **CausalLearn**: A package for causal discovery, useful for generating initial graphs when starting only with data <a class="yt-timestamp" data-t="00:28:37"></a>.
*   **EconML**: Focuses on advanced machine learning methods for heterogeneous treatment effects <a class="yt-timestamp" data-t="00:28:46"></a>.

The goal is to create an interoperable environment where users can perform end-to-end causal analysis without needing to switch between different tools, from data input to multi-angle analysis <a class="yt-timestamp" data-t="00:28:55"></a>.

### PY LLM and Non-Expert Accessibility
A new library, `PY LLM`, is being developed as a higher-level abstraction, leveraging Large Language Models (LLMs) to enable [[translating_ai_methods_for_practical_use | causal inference for non-experts]] <a class="yt-timestamp" data-t="00:29:33"></a>.
*   **Text-based Interaction**: The aim is to allow users to ask causal questions using natural language (text input), with text-based outputs, while the underlying advanced libraries handle the computations <a class="yt-timestamp" data-t="00:30:39"></a>.
*   **Domain Knowledge Integration**: LLMs can learn domain knowledge and provide suggestions for building causal graphs or even performing reasoning in situations without direct data <a class="yt-timestamp" data-t="00:33:52"></a>.
*   **Addressing Bottlenecks**:
    *   **Graph Generation**: One of the biggest challenges in causal inference is creating plausible and credible causal graphs <a class="yt-timestamp" data-t="00:32:36"></a>. LLMs can assist in generating initial graphs that experts can then critique and refine <a class="yt-timestamp" data-t="00:33:05"></a>.
    *   **Reputation Test Interpretation**: LLMs can guide users towards the right [[tools_and_frameworks_for_causal_analysis | reputation tests]] to run and help interpret their results, addressing the complexity many users face with numerous options <a class="yt-timestamp" data-t="00:34:39"></a>.

While LLMs may "hallucinate" or find statistical shortcuts, the long-term vision is to expose them to diverse data and axiomatic training to enable robust causal reasoning <a class="yt-timestamp" data-t="00:45:34"></a>.

### Causality's Role in LLM Robustness
Beyond using LLMs for causal inference, research explores how causality can enhance the robustness of LLMs themselves <a class="yt-timestamp" data-t="00:36:39"></a>. This involves "imparting how to learn causal knowledge" to LLMs by training them on fundamental causal axioms (e.g., transitivity, d-separation) <a class="yt-timestamp" data-t="00:38:55"></a>. Initial results show that models trained on synthetic axiomatic data for small graphs can generalize to larger, unseen graphs and even improve performance on standard causal benchmarks like CausalText <a class="yt-timestamp" data-t="00:40:12"></a>. This suggests a pathway to instilling reasoning capabilities without relying solely on memorization <a class="yt-timestamp" data-t="00:41:31"></a>.

## Call to Action

The `py-why` ecosystem operates as an open organization under an MIT license, encouraging contributions from researchers and practitioners <a class="yt-timestamp" data-t="01:09:19"></a>. The community welcomes feedback, method contributions, and real-world use cases to further demonstrate the impact of causality <a class="yt-timestamp" data-t="01:09:44"></a>. The field of causality is experiencing an "explosion" of possibilities, especially with the rise of LLMs and agents, making it an exciting time for new ideas in [[optimization_and_resource_allocation_strategies | agent design]] and [[practical_implementation_of_causal_discovery_using_python | scientific discovery]] <a class="yt-timestamp" data-t="01:06:51"></a>.