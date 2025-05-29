---
title: Causal models in autonomous driving
videoId: rHM0mBXubig
---

From: [[causalpython]] <br/> 

Current approaches to autonomous driving face significant challenges, notably the impracticality of driving millions of kilometers to encounter all possible natural environment events, and the complexity issues associated with simulation [00:01:00]. This creates a "gaping gap" in the development process [00:01:23].

## The Role of [[Causality and Causal Models | Causal Models]]

[[Causality and Causal Models | Causal models]] are proposed as a solution to this gap, offering a framework that efficiently describes the parameter space [02:04]. They allow for the modeling and playing around with distributions of natural phenomena and answering queries [01:51]. While [[Causality and Causal Models | causal models]] can incorporate time, it's often more efficient to exclude time from the equation if its impact is not obvious, focusing instead on the distribution of natural events [02:20]. These models can utilize functions, complex functions, [[causal_ai_and_machine_learning | machine learning]], and neural networks to model relationships, allowing for more efficient combination of the parameter space without needing real-time processing or simulation speed-up [03:01].

Daniel's journey into [[Causality in Artificial Intelligence | causality]] was inspired by Judea Pearl's work, particularly his framework's ability to solve industry problems and its "testable implications" [03:21].

### Counterfactuals and Their Necessity

[[Causality and Causal Models | Causal models]] are inspiring due to their "testable implications" and their ability to handle "counterfactual things" [04:27]. Counterfactuals allow for understanding "what would have been if it would rain" when data was collected in sunny conditions, broadening the toolset to tackle problems [04:49].

Counterfactuals are considered vital for building autonomous agents that can act effectively in the world [05:11]. They sit at the top of the "causal ladder," incorporating both associative and interventional aspects [05:31]. The key difference between interventions and counterfactuals is that interventions involve a manipulator fixing values, while counterfactuals incorporate knowledge from already observed data through an "abduction step" [05:58].

#### Abduction
Abduction is an "upward propagation" of knowledge in a causal network [07:36]. For example, observing a grandchild with blonde hair allows for updating the distributions of their grandparents' hair color, shifting likelihoods towards certain phenotypes without necessarily setting them to a single value [08:08]. This allows the model to incorporate knowledge from observations to understand how background exogenous variables shift their distributions [06:40].

## Practical Challenges and Solutions

Developing [[Causality and Causal Models | causal models]] for industrial use presents challenges, primarily the need for a rich description of the system and extensive information [09:01].

### Fully Specified [[structural_causal_models_and_machine_learning | Structural Causal Models]] (SCMs)
One approach is to invest significant engineering effort to create a fully specified [[structural_causal_models_and_machine_learning | Structural Causal Model]] (SCM) [09:17]. SCMs are the most general framework as they incorporate any functional relationship [09:28]. This high effort is justified if the goal is to answer any counterfactual query without prior specificity [09:51].

### Focusing on Specific Questions with Identification Algorithms
Alternatively, if only specific questions need answering, one can define a structure (DAG) and use "identification algorithms" (like ID, IDC, ID*, IDC*) [10:20]. These algorithms can determine if a question is answerable (identifiable) from the given structure and provide a recipe for calculating the query [10:41]. This also indicates which variables require data collection, allowing for a cost-benefit analysis and the option to simplify questions if data collection is too cumbersome [11:10].

### Iterative Development and Prototyping
Working with [[Causality and Causal Models | causal methods]] often necessitates an "iterative culture" [18:16]. It's crucial to define what needs to be modeled and what questions need answering [20:10]. One can start with a "Frankenstein structure" (substructure) and iteratively refine it [21:08]. The goal is to build a prototype idea first and then determine which elements are necessary to answer the questions [21:29]. For example, a project initially focused on a "lane changing assistant" was later refined to an "emergency break assistant" with the target variable being "does a collision happen" and "how strong was it" [21:57]. This iterative process also allows for neglecting variables with low causal strength to simplify the model [23:07]. The key is to balance accuracy and practical utility, preferring a "practical side" to avoid getting lost in high standards of accuracy prematurely [23:40].

### Data Collection
Data is needed for the abduction step and, more critically, for finding mechanisms [33:31]. This can be sourced from:
*   Publicly available, large datasets [33:52].
*   Expert guidance on functional relationships (e.g., quadratic relationships) [34:00].
*   Test runs and data from "black boxes" in cars [34:27].
*   Simulation data and synthetic data, which can be useful for learning mechanisms [34:58].

## Addressing Corner Cases and Long Tails

"Long tails" represent unexpected events in complex distributions that pose significant risks in autonomous systems [35:42]. Daniel suggests that by using the [[structural_causal_models_and_machine_learning | structural causal model]] framework, one can "reverse the question" [36:38]. Instead of just observing long tails, the question becomes: what structures, mechanisms, and distributions, when combined, will produce a long tail in a target variable (like the impact of a car accident)? [36:40]

This approach allows for more efficient guidance of the search, pre-filtering possibilities, and leveraging expert knowledge about structural information and coincidences [37:06]. For instance, experts can identify how specific mechanisms and distributions (like -1°C temperature and slight rain) interact to create a "corner case" like sudden ice on the street, which individually are not extreme [39:10]. This narrows down the search space for identifying these difficult scenarios [39:39].

## The Importance of Identifiability

[[evaluating_causal_models_in_practice | Identifiability]] is a "very basic idea in [[Causality in Artificial Intelligence | causality]]" [40:16]. It addresses the common fear of having unobserved variables or hidden confounding in a system [40:32]. The concept of [[evaluating_causal_models_in_practice | identifiability]] tells you whether a specific question can be answered from a given [[Causality and Causal Models | causal structure]], even without fitting mechanisms or collecting data at first [41:07]. It also specifies which variables require data collection, allowing for a practical assessment of effort and cost [41:39]. This enables making informed decisions about whether to pursue a difficult question or opt for easier, proxy questions [42:08].

## Team and Mindset
The team working on this project is diverse, including PhD physicists, mathematicians, and UX/UI designers [15:31]. Physicists bring a critical and open-minded approach, challenging assumptions [16:34], while mathematicians seek solid, provable frameworks [17:04]. This combination fosters both exploration and grounding in mathematical rigor [17:29].

For those starting in [[Causality in Artificial Intelligence | causal inference]], Daniel advises resilience, frustration tolerance, an experimental mindset, and playfulness [44:52]. The iterative nature of [[Causality and Causal Models | causal models]] means starting with a small DAG, experimenting, and gradually building complexity [45:39].

## Market Challenges and Future Outlook
Conveying the value of [[Causality and Causal Models | causal models]] to customers is a challenge, requiring finding the right language [46:44]. One common theme where the solution finds a match is "transportability" [47:15]. This refers to taking conclusions from one context (e.g., a surfboard shop in Los Angeles) and applying them to another (e.g., New York), identifying what parameters are similar and what are diverse to avoid comparing "apples with peas" [48:13].

There is a growing need for [[Causality in Artificial Intelligence | causal expertise]] in industry because, without it, organizations risk making wrong decisions, having implicit assumptions, and failing to understand their data [49:10]. A famous example is Google's gender pay gap analysis, which, due to a "Simpson Paradox reverse," led to raising men's wages instead of addressing the underlying issue [50:01]. [[Causality and Causal Models | Causal methods]] are crucial for making "good decisions" in complex systems [50:37].

Daniel recommends several resources for learning about [[Causality in Artificial Intelligence | causality]]:
*   *The Book of Why* by Judea Pearl [51:10].
*   *Causality: Models, Reasoning and Inference* by Judea Pearl (the standard work) [51:13].
*   *Causal Inference in Statistics: A Primer* by Judea Pearl [51:16].
*   *Elements of Causal Inference: Foundations and Learning Algorithms* by Jonas Peters, Dominik Janzing, and Bernhard Schölkopf (especially chapters on interventional and counterfactual queries) [51:25].
*   Toolboxes like PGM (PyTorch Geometric Models) [51:38].

Daniel encourages the [[Causality in Artificial Intelligence | causal community]] to "stay curious, stay experimental," and embrace the "causal mindset" as a "good virus" that leads to a lifelong journey of making sense of things and answering difficult questions [55:57].