---
title: Causal analysis and decision making
videoId: Vz5n5SamDAc
---

From: [[causalpython]] <br/> 

[[causal_analysis_and_decision_making | Causal analysis]] is crucial for deriving insights from data and driving effective decision-making processes, moving beyond mere correlation <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>. It provides clearer assumptions and helps recognize the limits of an analysis, allowing for higher confidence in outcomes <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.

## Limitations of Correlational Analysis
Before the widespread adoption of [[causal_analysis_and_decision_making | causal analysis]] approaches, many social science papers, despite being well-grounded in theory and backed by data analysis, would conclude with a disclaimer: "this is observational data, correlation is not causation, anything could be going on, we don't know" <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. This limitation often meant that "beautiful conclusions" were undermined by the inability to establish causation <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

## The Role of Large Language Models (LLMs) in Causal Analysis

While it is debatable whether large language models (LLMs) can truly [[causal_reasoning_in_ai | reason causally]] at present, their embedded knowledge can significantly augment the [[causal_analysis_and_decision_making | causal analysis]] process <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>. They can act as a "common sense database" to provide support for users lacking domain expertise, particularly in setting up causal assumptions <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

### Practical Applications of LLMs in Causal Analysis
LLMs are most useful today in assisting with the initial stages of [[causal_inference_and_decision_theory | causal inference]] and [[causal_discovery_and_learning | causal discovery]] <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.
*   **Generating Causal Assumptions**: For a long time, users had to figure out causal assumptions entirely on their own <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. LLMs can now provide technological support by suggesting plausible causal mechanisms or critiquing existing assumptions, alleviating the burden on domain experts <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>.
*   **Constructing Knowledge Graphs**: LLMs can help speed up the process of constructing knowledge graphs with domain experts <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>. This not only makes the process more efficient but also provides additional motivation for experts to share and critique knowledge, as they are presented with an initial graph <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.

## Current Challenges in Causal Inference

### Practical Challenges
From a practical standpoint, the main challenge is the wider deployment of [[causal_tools_and_methodologies_in_business_applications | causal methods]] in all relevant decision-making contexts <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>. Education remains critical for understanding basic causal concepts <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>.

### Academic Challenges
Academically, there's significant opportunity beyond current algorithms <a class="yt-timestamp" data-t="06:46:00">[06:46:00]</a>. As computers and data become more pervasive, there's a need for more complex modeling of intricate physical processes, especially those involving feedback loops over time <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>.

## Journey to Causality: An Expert's Perspective
Emre Kiciman's personal journey into causality began during his work in computational social science, analyzing large-scale social media data for insights into human behavior <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>. He consistently encountered the "correlation is not causation" dilemma in academic presentations <a class="yt-timestamp" data-t="09:18:00">[09:18:00]</a>. Learning that causal claims could be made from observational data under certain conditions inspired him to delve into [[causal_inference_and_decision_theory | causal inference]] <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>.

His learning path involved:
1.  Attempting to read Pearl's "Causality" book, which he found challenging for a beginner <a class="yt-timestamp" data-t="10:03:00">[10:03:00]</a>.
2.  Studying various papers on causality applications <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>.
3.  Finding clarity through Rosenbaum's paper on propensity scores, which intuitively explained how observational data could hint at causality by simulating a randomized controlled trial <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>. This understanding then allowed him to revisit and comprehend more advanced literature, including Pearl's book <a class="yt-timestamp" data-t="11:20:00">[11:20:00]</a>.

## DoWhy and EconML: Broadening Causal Analysis Usage
The DoWhy and EconML packages were created to broaden the usage of [[causal_analysis_and_decision_making | causal analysis]] methods <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>. The DoWhy library was initially conceived as a pedagogical tool for tutorials, structured around four stages of [[causal_analysis_and_decision_making | causal analysis]] <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>:
1.  **Modeling**: Defining models and assumptions <a class="yt-timestamp" data-t="14:16:00">[14:16:00]</a>.
2.  **Identification**: Analyzing models to identify a causal estimand and an approach to answer the causal question <a class="yt-timestamp" data-t="14:22:00">[14:22:00]</a>.
3.  **Estimation**: Performing statistical estimation to calculate values from data <a class="yt-timestamp" data-t="14:29:00">[14:29:00]</a>.
4.  **Refutation**: Validating or attempting to refute assumptions <a class="yt-timestamp" data-t="14:36:00">[14:36:00]</a>. This last step is inspired by Karl Popper's philosophy that theories cannot be proven, but can be falsified <a class="yt-timestamp" data-t="17:54:00">[17:54:00]</a>. [[root_cause_analysis_in_causal_ai | Causal modeling]] operates at the boundaries of human knowledge, as assumptions can be contradicted by data but never definitively proven <a class="yt-timestamp" data-t="18:22:00">[18:22:00]</a>.

### Evolution to PyWhy
DoWhy, originally an open-source project under Microsoft, transitioned to the independent PyWhy organization <a class="yt-timestamp" data-t="15:57:00">[15:57:00]</a>. This move fostered community growth, with significant contributions from Amazon, MIT, Columbia, and Carnegie Mellon (contributing the CausalLearn package) <a class="yt-timestamp" data-t="16:14:00">[16:14:00]</a>. This collaboration among major entities like Microsoft and Amazon on a single open-source tool highlights the shared goal of empowering the community to make better decisions with causal analysis, making data and computing more valuable <a class="yt-timestamp" data-t="17:01:00">[17:01:00]</a>.

### Future of DoWhy and PyWhy
A key future project is PyWhy-LLM, an experimental library exploring how LLMs can be integrated into the [[causal_analysis_and_decision_making | causal analysis]] process with DoWhy <a class="yt-timestamp" data-t="19:39:00">[19:39:00]</a>. This includes using LLMs to:
*   Generate causal graphs <a class="yt-timestamp" data-t="19:56:00">[19:56:00]</a>.
*   Critique assumptions <a class="yt-timestamp" data-t="19:59:00">[19:59:00]</a>.
*   Support identification analyses (e.g., finding instrumental variables using domain knowledge) <a class="yt-timestamp" data-t="20:08:00">[20:08:00]</a>.
*   Potentially assist with coding analyses <a class="yt-timestamp" data-t="20:20:00">[20:20:00]</a>.

## Causality and Generative Models

[[causal_reasoning_in_artificial_intelligence | Causality]] is at the forefront of discussions about artificial intelligence, especially with models like GPT, Sora, and large world models <a class="yt-timestamp" data-t="20:38:00">[20:38:00]</a>.

### Can Models Learn Causal World Models?
It's plausible that models trained on vast amounts of data, having observed many counterfactual scenarios, could learn to model a true causal model if it were the most efficient representation <a class="yt-timestamp" data-t="21:49:00">[21:49:00]</a>. However, current LLMs are primarily modeling language, not necessarily the world itself <a class="yt-timestamp" data-t="22:49:00">[22:49:00]</a>. The concept of "population support" is critical; extrapolating beyond observed counterfactuals becomes uncertain <a class="yt-timestamp" data-t="22:27:00">[22:27:00]</a>.

### Sora and Physics Simulation
OpenAI's claim that Sora is a "physics simulator" is seen as an overstatement <a class="yt-timestamp" data-t="24:03:00">[24:03:00]</a>. While it might be an approximate local physics simulator, certain videos demonstrate its limitations in truly simulating physics <a class="yt-timestamp" data-t="24:21:00">[24:21:00]</a>. For creative tasks, like generating two pirate ships battling in a coffee cup, violating physics for visual appeal is acceptable <a class="yt-timestamp" data-t="25:51:00">[25:51:00]</a>. However, for accurate modeling of the world, precise controls are needed <a class="yt-timestamp" data-t="26:43:00">[26:43:00]</a>.

### Generative Revolution: Impressiveness vs. Usefulness
The generative revolution is akin to the early commercial internet <a class="yt-timestamp" data-t="27:58:00">[27:58:00]</a>. Much is possible, but significant infrastructure and engineering work are still required <a class="yt-timestamp" data-t="28:46:00">[28:46:00]</a>. The pace of change might be faster than with the internet, but unforeseen complementary technologies (like smartphones for Uber) will also emerge to amplify AI's impact <a class="yt-timestamp" data-t="29:05:00">[29:05:00]</a>.

Impressiveness does not always equate to usefulness. For creative tasks, impressive outputs are useful, but for tasks requiring accuracy (e.g., summarizing a conversation), ungrounded responses or "hallucinations" are not acceptable <a class="yt-timestamp" data-t="27:30:00">[27:30:00]</a>.

### [[causal_reasoning_in_artificial_intelligence | Causal Control]] of Generation
A promising path for generative models is to learn how to causally control generation <a class="yt-timestamp" data-t="31:41:00">[31:41:00]</a>. This involves creating "knobs" to modify specific aspects of an image or output without regenerating it from scratch <a class="yt-timestamp" data-t="31:55:00">[31:55:00]</a>. It leverages other knowledge that cannot be easily expressed in a text command, providing additional control over the model's behavior <a class="yt-timestamp" data-t="32:49:00">[32:49:00]</a>.

Yann LeCun's view that "predicting pixels" is wasteful is rooted in the idea that pixels are not the right representation for learning about the world; latent representations are preferred <a class="yt-timestamp" data-t="42:13:00">[42:13:00]</a>. The most sensible approach involves learning a latent representation of the world from various signals and then implicitly or explicitly learning physics over that representation <a class="yt-timestamp" data-t="43:20:00">[43:20:00]</a>.

## Recommendations for the Causal Python Community
The [[causal_tools_and_methodologies_in_business_applications | Causal Python Community]] is currently healthy with numerous libraries like PyWhy and CausalPy <a class="yt-timestamp" data-t="35:35:00">[35:35:00]</a>. Key advice for progress includes:
*   **Focus on End Goals**: Don't lose sight of the real-world problems users are trying to solve <a class="yt-timestamp" data-t="35:57:00">[35:57:00]</a>.
*   **Broad Approaches**: Progress can come from deep algorithmic work, software engineering improvements (e.g., data ingestion), or better documentation <a class="yt-timestamp" data-t="36:08:00">[36:08:00]</a>.
*   **Accessibility of Advanced Concepts**: Making partial identification, sensitivity analysis, and proximal learning more accessible is crucial <a class="yt-timestamp" data-t="37:45:00">[37:45:00]</a>. These concepts are underutilized but can significantly move forward applied [[causal_inference_and_decision_theory | causal inference]] by allowing optimal decisions even when models cannot be fully specified <a class="yt-timestamp" data-t="38:05:00">[38:05:00]</a>. Many people lack the technical knowledge or time to implement these from scratch <a class="yt-timestamp" data-t="38:42:00">[38:42:00]</a>. PyWhy is beginning to address this by working on graph representations for partial graphs <a class="yt-timestamp" data-t="39:45:00">[39:45:00]</a>.

## Future Endeavors

Emre Kiciman is focusing on two main directions:
1.  **Practical LLM Integration**: Continuing to make it practical to use LLMs to support the standard [[causal_analysis_and_decision_making | causal analysis]] process, such as suggesting causal graphs, identifying missing confounders, and critiquing analyses <a class="yt-timestamp" data-t="40:35:00">[40:35:00]</a>.
2.  **Foundation Models for Complex Systems**: Exploring how Foundation models can help in better modeling complex physics-style systems, which could open up a broad set of exciting applications <a class="yt-timestamp" data-t="41:07:00">[41:07:00]</a>.