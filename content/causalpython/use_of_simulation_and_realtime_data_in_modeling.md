---
title: Use of simulation and realtime data in modeling
videoId: rHM0mBXubig
---

From: [[causalpython]] <br/> 

The use of simulation and real-time data is critical in developing and evaluating complex systems, particularly in fields like [[causal_models_in_autonomous_driving | autonomous driving]] <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. While both provide valuable information, they also present significant challenges.

## Challenges with Current Approaches <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>

The current approach to [[causal_models_in_autonomous_driving | autonomous driving]] often involves driving millions of kilometers to capture all possible events in a natural environment, which is simply not feasible <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Simulation can break down this problem, but it comes with its own complexities and issues in proper setup <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

One major concern in complex distributions are "long tails," which can lead to unexpected events <a class="yt-timestamp" data-t="00:35:42">[00:35:42]</a>. These are test cases where at least two parameters coincide to create a problematic scenario, even if individual parameters aren't extreme <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>. For example, slight rain at minus one degree Celsius can cause sudden ice, a "corner case" that individually mild conditions wouldn't predict <a class="yt-timestamp" data-t="00:39:19">[00:39:19]</a>. Such long tails signal potential issues in safeguarding [[causal_models_in_autonomous_driving | autonomous systems]] and require careful attention during testing <a class="yt-timestamp" data-t="00:35:59">[00:35:59]</a>.

## Role of Causal Models <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>

[[probabilistic_modeling_and_bayesian_frameworks | Causal models]] are proposed as a framework to address the gaps in existing approaches <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. They are more efficient in describing the parameter space <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a> and can incorporate time, though often time can be excluded for greater efficiency <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. This allows for more efficient combination of the parameter space, rather than relying solely on real-time or even speeded-up simulation <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

Specifically, [[evaluating_causal_models_in_practice | counterfactual]] reasoning within [[probabilistic_modeling_and_bayesian_frameworks | causal models]] allows agents to act effectively by incorporating knowledge from observed data through an "abduction step" <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. This allows models to answer "what if" questions, like what would happen if it rained, even if observations were only during sunny conditions <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. This is more powerful than simple "interventions," which fix input values without incorporating observed data <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

[[evaluating_causal_models_in_practice | Causal models]] are crucial for finding "corner cases" by using queries like probability of necessity and sufficiency to guide the search for missing test cases <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. They can also help address long tails by reversing the question: instead of reacting to long tails, identify what structures, mechanisms, and distributions would *constitute* a long tail in the target variable (e.g., car accident impact) <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>. This approach can guide the search more efficiently and pre-filter possibilities <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>.

## Data Collection and Modeling Challenges <a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>

A significant [[challenges_in_deploying_causal_models_in_industry | challenge in deploying causal models in industry]] is the requirement for a rich description of the system and a lot of information <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. Data is needed to fit the mechanisms within the causal model, and it's not always easy to acquire <a class="yt-timestamp" data-t="00:34:49">[00:34:49]</a>.

Strategies to deal with data collection challenges include:
*   **Publicly Available Datasets**: Utilizing large, existing datasets <a class="yt-timestamp" data-t="00:33:52">[00:33:52]</a>.
*   **Expert Guidance**: Experts can provide insights into relationships between variables (e.g., a quadratic relationship), informing the form of mechanisms and reducing the need to fit all parameters from scratch <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>.
*   **Real-time Data from Vehicles**: Collecting data from "black boxes" in cars during test runs <a class="yt-timestamp" data-t="00:34:30">[00:34:30]</a>. This data needs to be coherent and causally appropriate for incorporation into models <a class="yt-timestamp" data-t="00:34:41">[00:34:41]</a>.
*   **Simulation Data**: Simulation can be a valuable tool for gathering data, especially for specific scenarios, to learn mechanisms and fill data gaps <a class="yt-timestamp" data-t="00:35:01">[00:35:01]</a>.

Even with unobservable variables or hidden confounding, the concept of [[evaluating_causal_models_in_practice | identifiability]] can determine if specific questions can be answered from a given causal structure without requiring all data or mechanisms to be fitted initially <a class="yt-timestamp" data-t="00:40:37">[00:40:37]</a>. This provides a "price tag" for answers, indicating the effort needed to collect necessary data, allowing for optimal decision-making and efficient resource allocation <a class="yt-timestamp" data-t="00:42:52">[00:42:52]</a>.