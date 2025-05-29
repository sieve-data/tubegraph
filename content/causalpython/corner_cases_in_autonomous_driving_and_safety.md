---
title: Corner cases in autonomous driving and safety
videoId: rHM0mBXubig
---

From: [[causalpython]] <br/> 

Autonomous driving systems face significant challenges related to safety, particularly concerning "corner cases" and unexpected events <a class="yt-timestamp" data-t="00:59:59">[00:59:59]</a>. The current approach often relies on driving millions of kilometers to encounter all possible natural environment events, which is not feasible <a class="yt-timestamp" data-t="01:04:14">[01:04:14]</a>. While simulation can help, it has its own complexity and setup issues <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.

## Addressing the Gap with Causal Models

Daniel Evenha, a guest on the Causal Bandits podcast, suggests that [[causal_models_in_autonomous_driving | causal models]] offer a promising framework to address the gaps in autonomous driving safety <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>. [[causal_models_in_autonomous_driving | Causal models]] are more efficient in describing the parameter space and can incorporate time, although removing time from the equation when possible can lead to greater efficiency <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>. They allow for modeling and playing around with distributions of natural events to answer queries <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.

### Counterfactual Reasoning

[[causal_models_in_autonomous_driving | Causal models]] enable counterfactual reasoning, which is crucial for building effective autonomous agents <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>. While interventions involve manipulating values to certain fixed states <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>, counterfactuals incorporate knowledge from already observed data <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>. This means propagating observed knowledge up to background variables (abduction) to understand how distributions shift under an observation, then forwarding the causal model in that state <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>.

Abduction, or upward propagation, allows updating distributions of ancestral variables based on observations of descendant variables <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>. For instance, observing blonde hair in a grandchild can update the likelihood of certain hair color phenotypes in grandparents <a class="yt-timestamp" data-t="08:08:00">[08:08:08]</a>. This process is central to working with defined Structural Causal Models (SCMs) <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

## Identifying and Managing Corner Cases

Corner cases are challenging scenarios where at least two parameters coincide, and their interaction creates a problematic situation, even if individual parameters are not at extreme values <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. An example is a -1°C temperature with slight rain, which can cause sudden ice on the street, leading to a problem <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>. These are the "missing test cases" that need to be found to make autonomous driving functions safe <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>.

[[causality_robustness_and_fairness_in_ai_models | The causal framework]], particularly using queries and the [[causality_robustness_and_fairness_in_ai_models | joint probability of necessity and sufficiency]], can guide the identification of these corner cases <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>.

### Long Tails in Complex Distributions

Related to corner cases are "long tails" in complex distributions, which can lead to unexpected events <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. These long tails signal areas that need to be investigated for safeguarding autonomous systems <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.

The [[causal_models_in_autonomous_driving | Structural Causal Model (SCM)]] framework can be used to reverse the question: Instead of just observing long tails, one can ask what structures, mechanisms, or distributions, when combined, would produce a long tail in a target variable (e.g., car accident impact) <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>. This approach allows for:
*   **Efficient search guidance:** Pre-filtering the search space <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.
*   **Incorporating expert knowledge:** Experts can provide valuable structural information and insights into mechanisms and coincidences that contribute to long tails <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>.
*   **Narrowing down search space:** For corner cases, which involve multi-dimensional parameter coincidences, this method helps make the search field smaller <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>.

### Practical Considerations

The biggest challenge for industrial use of [[causal_models_in_autonomous_driving | causal models]] is the need for a rich description of the system <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>. This means either investing significant effort to build a fully specified SCM, which can answer any counterfactual query <a class="yt-timestamp" data-t="09:17:00">[09:17:00]</a>, or focusing on specific questions.

For specific questions, [[causality_and_ai_challenges_and_opportunities | identification algorithms]] (e.g., ID, IDC, ID*, IDC*) can determine if a question is answerable from a given causal structure without needing data initially <a class="yt-timestamp" data-t="10:33:00">[10:33:00]</a>. If answerable, they provide a "recipe" for how to calculate the query and indicate which variables require data collection <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>. This allows for a cost-benefit analysis, enabling decisions on whether to collect data or refine the question to a simpler, more feasible one <a class="yt-timestamp" data-t="11:10:00">[11:10:00]</a>.

### Data Challenges

Collecting data for [[causal_models_in_autonomous_driving | causal models]] in autonomous driving is complex. Data is needed for the abduction step, often coming from accidents, records, or synthetic sources <a class="yt-timestamp" data-t="33:30]">[33:30]</a>. Extensive data is also required to find the underlying mechanisms. This can involve using public datasets, expert guidance (e.g., suggesting a quadratic relationship between variables), test field runs, and data from "black boxes" in cars <a class="yt-timestamp" data-t="33:51]">[33:51]</a>. Simulation data can also be a valuable resource to learn mechanisms and fill data gaps <a class="yt-timestamp" data-t="35:01]">[35:01]</a>.

### Iterative Development

Working with [[causal_models_in_autonomous_driving | causal methods]] requires an iterative mindset <a class="yt-timestamp" data-t="18:19:00">[18:19:00]</a>. It's common to start with a complex model, such as a "lane changing assistant" with over 100 nodes <a class="yt-timestamp" data-t="19:47:00">[19:47:00]</a>, only to realize the need to simplify and focus on minimal components <a class="yt-timestamp" data-t="20:01:00">[20:01:00]</a>. This involves:
*   **Defining the target:** Clearly identifying the target variable, e.g., "does a collision happen?" or "how short was the braking distance?" <a class="yt-timestamp" data-t="22:28:00">[22:28:00]</a>.
*   **Iterating on structure and mechanisms:** Continuously refining the causal graph and functional relationships <a class="yt-timestamp" data-t="20:25:00">[20:25:00]</a>.
*   **Prioritizing impact:** Neglecting variables with low causal strength (e.g., visual sensorics having little impact on braking) to simplify the model for initial iterations <a class="yt-timestamp" data-t="23:09:00">[23:09:00]</a>.

This iterative process helps balance accuracy and practicality, avoiding wasted effort on overly complex models or dead ends <a class="yt-timestamp" data-t="23:40:00">[23:40:00]</a>. It allows for experimentation with low effort and guides the project towards the goal by iteratively adding structure and mechanisms <a class="yt-timestamp" data-t="24:24:00">[24:24:00]</a>.

### Overcoming Fear of Incorrect Models

Many people are intimidated by proposing a causal graph (DAG) that might not be correct <a class="yt-timestamp" data-t="24:57:00">[24:57:00]</a>. However, a DAG simply makes assumptions explicit <a class="yt-timestamp" data-t="25:31:00">[25:31:00]</a>. Assumptions are always present in decision-making, whether implicitly or explicitly <a class="yt-timestamp" data-t="25:44:00">[25:44:00]</a>. By making them explicit, they can be scrutinized and improved. Even a wrong assumption, once identified, represents significant progress <a class="yt-timestamp" data-t="26:35:00">[26:35:00]</a>.

Similarly, the fear of unobserved variables or hidden confounding is common <a class="yt-timestamp" data-t="40:29:00">[40:29:00]</a>. However, [[causality_and_ai_challenges_and_opportunities | identifiability]] algorithms specifically address this by determining if a question can be answered from a given structure, even with unobserved variables, and indicate what data needs to be collected <a class="yt-timestamp" data-t="41:07:00">[41:07:00]</a>.

## Conclusion

The application of [[causal_models_in_autonomous_driving | causal models]] and reasoning provides a robust framework for tackling the complex challenges of autonomous driving, particularly in identifying and managing corner cases and long-tail events. By emphasizing iterative development, leveraging [[causality_and_ai_challenges_and_opportunities | identifiability]] algorithms, and understanding the role of abduction, engineers and data scientists can build safer and more efficient autonomous systems.