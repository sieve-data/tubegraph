---
title: advancements in causal modeling and AI
videoId: 8yWKQqNFrmY
---

From: [[causalpython]] <br/> 

The "Causal Bandits" podcast, in its second season, is highlighted as a leading resource on [[Causality in AI | causality]] and AI [00:01:38]. Dr. Amit Sharma, creator of the DoWhy library and principal researcher at Microsoft Research India, believes that data tells stories and aims to tell causal ones through his research [00:01:47]. He views [[Causality in AI | causality]] as a goal, even if its achievement is not always clear [00:01:52].

## [[Causality in AI | Causality]] in the Age of Large Language Models (LLMs)
LLMs have rapidly advanced, making it challenging to form concrete thoughts on their implications [00:03:09]. Previously, [[Causality in AI | causality]] was understood to require two main components: domain knowledge, and discovery and reasoning [00:03:26]. The field of causal research largely focused on the latter, assuming domain knowledge would be provided [00:03:35].

LLMs have demonstrated that domain knowledge can be learned, and in many situations, this learned knowledge enables reasoning without requiring data [00:03:50]. While seemingly reasoning, this is often a combination of domain knowledge and generalization [00:04:15]. For the future of [[Causality in AI | causality]] and [[Causal inference | causal inference]], both domain knowledge acquisition and discovery/reasoning must be considered [00:04:26]. Methods for acquiring and integrating domain knowledge into algorithms need to be supercharged [00:04:33].

## [[Causality in AI | Causality]] in the Age of Agents
For agents, the role of [[Causality in AI | causality]] is emerging as very important, especially as agents increasingly interact in the real and web worlds [00:04:43]. Notions such as action, reward, optimizing desired behavior, and penalizing undesired behavior are fundamentally [[Causal abstractions | causal abstractions]] [00:05:05].

In the training phase of agents, [[Causality in AI | causality]] might not be explicitly present, as it may involve standard Reinforcement Learning (RL) focused on reward optimization [00:05:12]. However, once agents begin to interact collaboratively, new [[Causal questions | causal questions]] arise [00:05:21]. These include identifying which agent is most useful and should be rewarded more, and applying counterfactual notions of blame for underperforming agents [00:05:29]. Such considerations are akin to social science but require a deeper understanding of system design to ensure desired agent behavior [00:05:51].

Some interesting papers exist on agents and [[Causal modeling | causal modeling]] [00:06:12]. A paper by Riches and Everett from Google DeepMind proposes a theory for agents to learn robust world models through interventional distributions [00:06:16]. These works show that an agent can learn to mimic an ideal causal agent's behavior by operating in sufficiently diverse environments, even without explicit world models or causal understanding [00:07:27]. They suggest that observing agent actions can even lead to the recovery of their world models [00:07:59]. This highlights the power of diverse data in imparting [[Causality in AI | causality]] [00:08:10]. Research from Schulov's group on exchangeability also suggests that data from multiple distributions can significantly improve [[Causal discovery and inference in AI | causal discovery]] [00:08:18].

A key insight is that there are "multiple ways to reach a causal agent" [00:09:17]. Prior to LLMs, the consensus was that achieving causal actions required defining the right mechanisms, graphs, and inductive biases from causal principles [00:09:21]. However, new results demonstrate alternative paths:
*   Collecting a lot of diverse data can lead to learning causal actions, even without understanding the underlying causal model [00:09:43].
*   Building a foundation on domain knowledge, theorems, and axioms (like physics laws) can enable causal actions by applying known rules, similar to "cheating" by using established knowledge rather than discovering it from first principles [00:10:55]. This approach, similar to how humans learn from books and observation, can be a more attractive way to achieve causal models [00:14:06].

### Challenges with Agents: Verification
One significant missing aspect in contemporary agentic frameworks is robust verification [00:14:42]. Current frameworks often operate in well-controlled environments (e.g., coding with compilers, API calls with clear failure signals) or rely on subjective user feedback [00:14:48]. The challenge lies in applying these frameworks to vague real-world problems where human rewards might be insufficient or unscalable [00:15:25].

There is a need to create verifiers for new domains, starting with outcomes and then extending to individual agent actions [00:15:42]. For example, summarizing a meeting transcript requires verifying precision, recall of important information, and relevance to specific users [00:16:01]. A harder example is in scientific discovery, where agents could suggest experiments, requiring feedback mechanisms to design better experiments [00:16:35]. Developing holistic verification methods is seen as a major leap, involving the art and science of defining verifiable properties and creating [[Causal systems | causal systems]] to prove improvements [00:16:54].

## The Evolution of DoWhy
[[Causal modeling | Causal modeling]] faces the fundamental problem of verification, especially for estimates from observational data without randomized controlled trials [00:17:32].

### Motivation and Genesis
The DoWhy library was created out of frustration with existing tools [00:57:49]. Earlier libraries were fragmented, focusing on single steps like matching, assuming the user had already determined the best method [00:57:51]. Furthermore, identifying and applying the correct reputation tests felt like a "dark art" to beginners [00:58:47]. The goal was to create a unified API that simplifies the causal inference process, making it accessible and reusable [00:59:00].

### Four Steps of DoWhy
DoWhy structures the causal inference process into four distinct steps [00:57:01]:
1.  **Model the Graph**: Define the causal graph representing assumptions [00:59:15]. This step focuses on domain knowledge [01:00:02].
2.  **Identify the Effect**: Determine if the causal effect is identifiable from the graph and data [00:59:21]. This step, along with modeling, does not require data [01:00:04].
3.  **Estimate the Effect**: Apply various methods (e.g., propensity score-based methods) to estimate the identified causal effect using data [00:26:46].
4.  **Refute the Effect**: Critically assess the validity and robustness of the causal estimate through various tests [01:00:49].

This separation, particularly between identification and estimation, was a conscious design choice to allow users to iterate and understand the process better [01:00:29]. The philosophy is that causal estimates, like scientific theories, can only be disproven, not proven correct [01:00:42].

### Reputation Tests in DoWhy
DoWhy's refutation module draws inspiration from economics and biomedical literature [00:19:08]. In economics, studies are rigorously evaluated through feedback and robustness checks [00:19:27]. From biomedical literature, the concept of negative controls was adopted, where experiments are run without the assumed cause to ensure the observed effect is indeed due to the reagent [00:20:25].

DoWhy incorporates:
*   **Sensitivity Analysis**: Checking what happens if an unobserved confounder is missed [00:20:05].
*   **Objective Tests (Significance Tests)**: Giving yes/no answers based on statistical significance [00:20:17]. Examples include adding a random common cause or replacing the treatment with a placebo [00:20:57].
*   **Dummy Outcomes**: Creating an outcome variable known *not* to be caused by the treatment but dependent on confounders; a zero causal effect should be observed [00:21:31].
*   **Overlap Tests**: Assessing the overlap of treatment across confounding variables to understand where estimates can be trusted [00:22:20].
*   **Graph Verification**: Testing the underlying causal graph's assumptions, beyond just conditional independencies [00:22:52]. Recent tests compare the graph's information to a random graph, providing confidence in its informativeness and data support [00:23:36].

### Future of DoWhy: PY Ecosystem and PY LLM
DoWhy has evolved into a community project, no longer solely under Microsoft [00:24:00]. The future vision includes:
1.  **Causal Ecosystem (PY)**: Building a seamless ecosystem for solving any causal problem [00:28:22]. This integrates DoWhy (effect estimation, root cause analysis) with other libraries like CausalLearn (causal discovery) and EconML, allowing them to interoperate [00:28:35]. The goal is a unified experience where users interact with "PY" and the libraries handle the underlying communication [00:29:08].
2.  **PY LLM**: A new library providing a higher-level abstraction, leveraging LLMs for [[Causal discovery and inference in AI | causal discovery]] and acquiring domain knowledge [00:29:33]. The aim is to enable [[Causal inference | causal inference]] for non-experts, such as general citizens [00:29:56]. Users can input questions in text and receive text-based answers, with advanced causal libraries running in the background [00:30:39]. This aligns with a broader view of [[Causality in AI | causality]] that encompasses both literature review and data-driven analysis [00:31:46].

The biggest bottleneck that [[Causal AI and machine learning intersection | LLM integration]] could address is graph generation [00:33:04]. LLMs can help generate plausible causal graphs that experts can then critique and feed into DoWhy [00:33:08]. Another bottleneck is guiding users through the many refutation tests [00:34:17]. LLMs could suggest appropriate tests and help interpret their results [00:34:39]. While LLMs can streamline graph building, challenges like "hallucination" mean full automation is not yet realistic where accuracy is critical [00:35:15].

## [[Causality in AI | Causality]] to Make LLMs More Robust
Research is also exploring how [[Causality in AI | causality]] can make LLMs more robust [00:36:00]. Traditional methods like adding causal regularizers are less effective given the massive scale of LLM data [00:37:30]. Building comprehensive world models for LLMs is also out of reach due to their vast scope [00:37:44].

A promising approach is to imbue LLMs with robustness by teaching them the axiomatic principles of [[Causal reasoning in AI | causal reasoning]] [00:38:12]. The focus shifts from imparting causal knowledge to teaching *how to learn* causal knowledge [00:38:51]. This involves training LLMs on basic axioms, such as transitivity [00:39:48]. Initial results show small transformer models trained on axioms (e.g., graphs of length 3-6) can generalize to longer graphs (up to length 14, with some accuracy drop) and even reverse chains, suggesting they learn to compose axioms [00:40:13]. Similar success has been observed with d-separation [00:41:02].

Further experiments show that Llama models fine-tuned on synthetic axiomatic data for d-separation and transitivity significantly improve performance on new causal tasks like CoTOC, a benchmark for constructing graphs from correlational statements [00:41:29]. This suggests a different way of training LLMs for [[Causality in AI | causality]] and imparting reasoning without relying on memorization [00:43:33]. These results are congruent with Andrew Lampin's work on active causal strategies from passive data, as they involve learning [[Causal reasoning in AI | causal reasoning]] by observing demonstrations of axioms [00:43:13].

A challenge, however, is that models may find statistical shortcuts, even when enforced to implement correct logical reasoning, leading to a tapering off of performance on larger graphs not seen during training [00:44:56]. The hope is that by scaling data and providing enough diverse possibilities, the space of shortcuts will shrink, forcing models to converge on causal principles [00:45:34].

## Main Challenges in [[Causality in AI | Causality]] Today
### Technical Challenge: Model-Free Causality and Diverse Data
A significant technical challenge is to extract the maximum information from datasets in a "model-free" way, similar to model-free reinforcement learning [00:47:57]. Much progress in [[Causality in AI | causality]] has relied on building explicit models of the world (e.g., Bayesian networks, generative models) [00:48:04]. A model-free revolution is needed to achieve scalability, but this requires developing new causal theory and guarantees [00:48:23].

Research on "exchangeable distributions," particularly from Sholuv's group, offers a promising direction [00:49:06]. Instead of assuming Independent and Identically Distributed (IID) data, which limits [[Causal discovery and inference in AI | causal discovery]], assuming data comes from many diverse environments (exchangeable data) can unlock much more [00:49:17]. As the number and diversity of environments increase, it becomes possible to learn causal direction [00:49:51]. More theoretical and empirical work is needed in this area to leverage diverse multi-distribution data for richer identification results [00:50:09]. This could help address the question of why [[Causal inference | causal inference]] is not more widely used [00:50:52].

### Sociological Challenge: The "Bitter Lesson" and Multiple Paths to [[Causality in AI | Causality]]
There's a "bitter lesson" for [[Causality in AI | causality]], akin to Richard Sutton's bitter lesson for ML [00:51:35]. The lesson suggests that [[Causality in AI | causality]] might be an *end result* desired in a system, but not always the *means* to achieve it [00:51:56]. While principled, model-based approaches are valuable, other less obvious methods might also lead to causal outcomes [00:52:38]. For instance, data augmentation, a simple technique, can yield causal benefits despite not being inherently causal [00:52:49].

This connects to the idea of an "invariant core" or "still point" across different distributions or environments, as seen in concepts like exchangeability or contrastive learning [00:52:58]. By forcing a model to find what remains static despite changes (e.g., moving perspective around an object to understand its true structure), it can learn causal principles [00:54:13]. This approach, where causal constraints are used to create loss functions or augment data, allows models to learn effectively even without a full causal model [00:56:07]. This is akin to reversing testable implications to learn [00:56:41].

## Message to the Causal Community
The landscape for [[Causality in AI | causality]] has exploded with the advent of LLMs, making it an exciting time to enter the field [01:06:51]. There are two main avenues for contribution:
1.  **Causality Helping LLMs**: Explore how [[Causality in AI | causality]] can make LLMs more robust [01:07:09]. This includes work on agents, defining appropriate rewards, constraints, and addressing notions of blame in LLM-driven agentic worlds [01:07:20].
2.  **LLMs Helping Science**: Build tools that enable scientists to better utilize their data and literature, and propose experiments more efficiently [01:08:01]. LLMs could potentially generate graphs from scientific literature and plan experiments, accelerating the scientific cycle [01:08:32].

The PY organization is an open-source community where researchers and practitioners can contribute new methods, provide feedback, and engage in discussions about [[Causality in AI | causality]] [01:09:22]. Real-world use cases are particularly valuable for demonstrating the impact of [[Causality in AI | causality]] [01:10:47].