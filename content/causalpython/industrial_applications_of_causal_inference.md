---
title: Industrial applications of causal inference
videoId: rHM0mBXubig
---

From: [[causalpython]] <br/> 

The Causal Bandits podcast features Daniel Even, an expert in [[causality_in_science_and_industry | causality]] and machine learning, discussing the industrial applications of [[causal_inference_and_its_applications | causal inference]], particularly in autonomous driving. <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>

## The Problem with Current Autonomous Driving Approaches

The primary issue with current autonomous driving approaches is a lack of a comprehensive strategy. <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a> The prevailing theory suggests that millions of kilometers must be driven to capture all possible natural environment events, which is not feasible. <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a> While simulation can break this down, it introduces complexity issues and difficulties in proper setup, leaving a significant gap. <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>

### Causal Models as a Solution
Daniel Even proposes using [[causal_inference_methods_and_applications | causal models]] to address this gap. <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a> These models efficiently describe the parameter space and can incorporate time, although removing time from the equation can significantly improve efficiency. <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a> By modeling and manipulating distributions of natural events, and combining them using functions, machine learning, or neural networks, the parameter space can be explored more efficiently. <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a> This approach does not require real-time execution, allowing for speed-ups similar to simulation. <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>

## Daniel Even's Journey into Causality

Daniel's interest in [[causality_in_science_and_industry | causality]] began with Judea Pearl's work, particularly his book *The Book of Why*. <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a> He was drawn to the framework's ability to solve widespread industry problems, its testable implications, and its capacity for counterfactual reasoning. <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>

### Inspiring Aspects of Pearl's Framework
*   **Testable Implications**: The framework provides a "safe ground" for exploration. <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>
*   **Counterfactuals**: The ability to ask "what would have been if it would rain" when observations are based on sunny conditions. <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a> This concept of probability of necessity and sufficiency broadens the problem-solving toolset. <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>

### The Causal Ladder and Abduction
The [[causal_inference_concepts_and_applications | causal ladder]] consists of associative, interventional, and counterfactual ranks, with each higher rank incorporating the lower ones. <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>
*   **Interventions**: Involve a manipulator fixing values to certain parameters to predict an outcome. <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>
*   **Counterfactuals**: Incorporate knowledge from observed data through an "abduction step." <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a> This involves propagating knowledge from an observation "up" to background exogenous variables, shifting their distributions. <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a> This approach is considered "mightier" and more usable than simply fixing interventional values. <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>
    *   **Abduction Explained**: Abduction is an upward propagation of knowledge in a causal network. For example, if a grandchild has blonde hair, abduction updates the likelihood of hair colors for their ancestors, shifting distributions towards phenotypes more likely to produce blonde hair, without necessarily setting ancestor hair color to a single value. <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>

## Challenges in Practical Application: Data Richness and Identifiability

One of the greatest challenges for the industrial use of [[causal_inference_methods_and_applications | causal models]] is the requirement for a very rich description of the system and a lot of information. <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>

### Dealing with Data Requirements
There are two main approaches:
1.  **Fully Specified Causal Model**: Requires significant engineering, time, and resources to create a fully specified structural causal model (SCM) with all mechanisms and distributions. <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a> This path is chosen when many diverse questions need to be answered in the future. <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>
2.  **Specific Questions with Identification Algorithms**: For specific questions (e.g., two or three), one can sit down, define a DAG structure, and use identification algorithms (ID, IDC, IDC*). <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a> These algorithms determine if a question is identifiable and, if so, provide a recipe for calculating the query, indicating which data variables are needed. <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a> This allows for a cost-benefit analysis: if collecting data is too cumbersome for a difficult question, a simpler question might suffice. <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>

Ultimately, knowing "what you want to know" and the "price" (effort/data) for each question is crucial for effective [[causal_inference_and_decision_making | decision-making]]. <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>

## Project: Making Autonomous Driving Functions Safe

Since July 2020, Daniel's team has been working on a public-funded project to enhance the safety of autonomous driving functions. <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a> The focus is on identifying and testing "corner cases" – scenarios where at least two parameters coincide to create problematic situations, even if individually the parameters are not extreme. <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a> An example is slight rain at minus one degree Celsius, leading to sudden ice. <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>

### Team Dynamics and Strengths
The team is diverse, comprising PhD physicists, mathematicians, and UX/UI designers. <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>
*   **Physicists**: Bring critical and open-minded thinking, accustomed to challenging assumptions and exploring "uncharted territory" based on the principle of falsifiability. <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>
*   **Mathematicians**: Seek solid mathematical frameworks, proofs, and clear theoretical backgrounds, translating exploratory ideas into concrete algorithms. <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>
This complementary dynamic fosters fruitful development. <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>

### Iterative Workflow in Causal Model Development
An iterative approach is essential when working with [[causal_inference_methods_and_applications | causal models]]. <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>
The team initially attempted a complex "lane changing assistant" model with over 100 nodes, which became too cumbersome. <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a> They then shifted to a simpler "emergency brake assistant," with the target variable being collision occurrence and impact strength. <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>

Key aspects of the iterative workflow include:
*   **Defining the Goal**: Clearly knowing what needs to be modeled. <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>
*   **Iterating on Structure**: Understanding that missing links in a DAG are stronger indications than present ones. <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>
*   **Incorporating Mechanisms**: Mechanisms are difficult to model and require an iterative approach. <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>
*   **Prototyping**: Building a prototype first and then identifying necessary elements to answer specific questions. <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a> For example, they found temperature was a main driver, while visual sensors had negligible impact on target variables, allowing for their omission in early iterations. <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>
*   **Trade-off**: Balancing accuracy/precision with practical applicability. <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a> It's often better to prioritize practicality to avoid investing excessive effort in dead ends. <a class="yt-timestamp" data-t="00:23:49">[00:23:49]</a>

## Overcoming Fears in Causal Modeling

Many people are intimidated by the prospect of drawing a "wrong" Directed Acyclic Graph (DAG) or having unobserved variables. <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>

### DAGs as Explicit Assumptions
Daniel encourages dropping this fear, emphasizing that a DAG simply makes implicit assumptions explicit. <a class="yt-timestamp" data-t="00:25:24">[00:25:24]</a> Assumptions are always present in any data-driven decision-making, and externalizing them through a DAG allows for clarity, revisitation, and immediate improvement if a wrong assumption is identified. <a class="yt-timestamp" data-t="00:25:56">[00:25:56]</a>

### Unobserved Variables and Identifiability
It is common to have unobserved variables or hidden confounding in real-world systems. <a class="yt-timestamp" data-t="00:40:37">[00:40:37]</a> However, the concept of [[causal_inference_concepts_and_applications | identifiability]] is a crucial tool. It tells you whether a specific question can be answered from a given causal structure, even before collecting any data or fitting mechanisms. <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a> If identifiable, it specifies which variables require data collection, allowing teams to weigh effort and cost against the value of the answer. <a class="yt-timestamp" data-t="00:41:41">[00:41:41]</a> This guides [[causal_inference_and_decision_making | decision-making]] by revealing the "price" for obtaining answers. <a class="yt-timestamp" data-t="00:43:07">[00:43:07]</a>

## Development Challenges and Discoveries

### Dead Ends
An initial dead end was attempting to bridge Bayesian models with Structural Causal Models (SCMs). <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a> While Bayesian models were comprehensible and inferable, they were often restricted to discrete data. <a class="yt-timestamp" data-t="00:27:38">[00:27:38]</a> The team sought a more general framework, leading them to SCMs, which can handle discrete, continuous, or mixed data with any functional mechanism. <a class="yt-timestamp" data-t="00:28:19">[00:28:19]</a> An attempt to reparameterize conditional probability tables from Bayesian models into the SCM world proved incompatible. <a class="yt-timestamp" data-t="00:28:51">[00:28:51]</a>

### Biggest Discoveries
1.  **Centrality of Abduction**: The abduction step (upward propagation of observations to background variable distributions) is fundamental to working with defined SCMs. <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a> While simple examples can be done by hand, complex models with many nodes and non-linear relationships make abduction challenging. <a class="yt-timestamp" data-t="00:30:36">[00:30:36]</a>
2.  **Finding an Efficient Abduction Method**: After exploring nine different methods (MCMC sampling, numerical, closed-form integrals) for over a year and a half, the team believes they've found a time-efficient and precise method. <a class="yt-timestamp" data-t="00:31:19">[00:31:19]</a> This method works across various mechanisms, distributions, and noise types (e.g., additive, multiplicative heteroscedastic noise). <a class="yt-timestamp" data-t="00:31:43">[00:31:43]</a> Further research is still needed in this area. <a class="yt-timestamp" data-t="00:32:38">[00:32:38]</a>

### Data Collection for Mechanisms
Collecting data for mechanisms in autonomous driving is complex. Data for the abduction step can come from accident records or synthetic data. <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a> For mechanisms, they utilize:
*   Publicly available large datasets. <a class="yt-timestamp" data-t="00:33:52">[00:33:52]</a>
*   Expert guidance (e.g., knowing a relationship is quadratic helps fit parameters). <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>
*   Test field runs and data black boxes from cars. <a class="yt-timestamp" data-t="00:34:27">[00:34:27]</a>
*   Simulation data to learn mechanisms. <a class="yt-timestamp" data-t="00:34:58">[00:34:58]</a>

## Addressing Long Tails in Autonomous Driving

"Long tails" in complex distributions represent rare but significant unexpected events that pose safety risks in autonomous systems. <a class="yt-timestamp" data-t="00:35:38">[00:35:38]</a> Daniel connects this to the SCM framework by reversing the question: Instead of merely reacting to long tails, the goal is to identify what structures, mechanisms, and distributions, when combined, would *produce* a long tail in a target variable (e.g., car accident impact). <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a> This approach allows for more efficient searching and pre-filtering, enabling experts to identify specific conditions that lead to such extreme events. <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a> This method helps narrow down the search space for critical "corner cases" in multi-dimensional parameter fields. <a class="yt-timestamp" data-t="00:39:39">[00:39:39]</a>

## The Need for Causal Expertise in Industry

There is a definite need for more people with causal expertise in industry. <a class="yt-timestamp" data-t="00:49:04">[00:49:04]</a> Without [[causality_in_science_and_industry | causality]], organizations risk making wrong decisions, having implicit assumptions, and failing to fully understand their data. <a class="yt-timestamp" data-t="00:49:15">[00:49:15]</a> Many models are currently associative, which works for some domains, but eventually leads to errors. <a class="yt-timestamp" data-t="00:49:37">[00:49:37]</a>

A notable example is Google's analysis of the gender pay gap, which, due to a "Simpson's Paradox reverse," led to an erroneous decision to raise men's wages. <a class="yt-timestamp" data-t="00:50:01">[00:50:01]</a> This highlights how even large, data-savvy companies can make mistakes without a causal understanding. <a class="yt-timestamp" data-t="00:50:20">[00:50:20]</a> Every data scientist and decision-maker in complex systems can greatly benefit from a [[causal_inference_and_decision_making | causal mindset]] and [[causal_ai_applications_in_business_and_technology | causal methods]]. <a class="yt-timestamp" data-t="00:50:40">[00:50:40]</a>

## Resources and Advice for Aspiring Causal Practitioners

### Recommended Resources
*   *The Book of Why* by Judea Pearl <a class="yt-timestamp" data-t="00:51:10">[00:51:10]</a>
*   *Causality* by Judea Pearl <a class="yt-timestamp" data-t="00:51:13">[00:51:13]</a>
*   *Causal Inference in Statistics: A Primer* by Pearl, Glymour, and Jewell <a class="yt-timestamp" data-t="00:51:16">[00:51:16]</a>
*   *Elements of Causal Inference: Foundations and Learning Algorithms* by Jonas Peters, Dominik Janzing, and Bernhard Schölkopf (especially chapters on interventional and counterfactual queries). <a class="yt-timestamp" data-t="00:51:22">[00:51:22]</a>
*   Causal toolboxes like DoWhy, which bridge theoretical models with practical processing. <a class="yt-timestamp" data-t="00:51:37">[00:51:37]</a>
*   Paul Hämäläinen's online course on Udemy. <a class="yt-timestamp" data-t="00:49:58">[00:49:58]</a>

### Advice for Starting in Causality
*   **Resilience and Frustration Tolerance**: [[Causal inference methods and applications | Causal inference]] is not easy and requires persistence. <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a>
*   **Experimental Mindset**: Be willing to experiment and play around with models. <a class="yt-timestamp" data-t="00:45:32">[00:45:32]</a>
*   **Playfulness and Curiosity**: Start with small DAGs, iterate, and remain curious. <a class="yt-timestamp" data-t="00:45:39">[00:45:39]</a>
*   **Embrace the "Causal Mindset Virus"**: Once infected, it leads to a lifelong journey of curious exploration, striving for high standards in making sense of things, answering difficult questions, and improving understanding. <a class="yt-timestamp" data-t="00:56:05">[00:56:05]</a>

## Conveying Value to Customers

When discussing [[causal_ai_applications_in_various_industries | causal AI applications in various industries]] with potential customers, the challenge is finding the right language. <a class="yt-timestamp" data-t="00:46:41">[00:46:41]</a> One common theme resonating with manufacturers is "transportability." <a class="yt-timestamp" data-t="00:47:15">[00:47:15]</a> This refers to applying conclusions from one context to another, even when parameters differ (e.g., machine downtime in different climates). <a class="yt-timestamp" data-t="00:47:47">[00:47:47]</a> [[Causal inference and its applications | Causal inference]] helps recognize and account for these differences, preventing misleading "apples to oranges" comparisons. <a class="yt-timestamp" data-t="00:48:45">[00:48:45]</a>