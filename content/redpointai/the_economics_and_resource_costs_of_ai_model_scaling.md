---
title: The economics and resource costs of AI model scaling
videoId: OoL8K_AFqkw
---

From: [[redpointai]] <br/> 

The journey towards advanced AI capabilities, including Artificial General Intelligence (AGI), is profoundly influenced by the economics and resource costs associated with scaling AI models <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. Historically, significant advancements have been directly tied to an increase in computational resources and data <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## Evolution of Training Costs
The cost of training frontier AI models has dramatically increased over time:
*   **GPT-2**: Approximately $5,000-$50,000 <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **GPT-4**: Costs escalated from "thousands to tens of thousands of dollars to hundreds of thousands to millions to tens of millions" <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Some labs may even be spending "hundreds of millions of dollars today" on these models <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

This indicates that simply throwing more money, resources, and data into pre-training continues to yield better models <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### The "Soft Wall" of Cost
While increasing resources improves models, there is an economic limit to this approach <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Scaling models by 10x in capabilities could translate to costs of billions or even tens of billions of dollars <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. At some point, it becomes "no longer economically worth it to push that further" <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. This represents a "soft wall" rather than a hard technical limitation <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

## The Promise of [[scaling_challenges_in_ai_and_test_time_compute | Test-Time Compute]]
A significant shift in focus has been towards [[scaling_challenges_in_ai_and_test_time_compute | test-time compute]] (or inference compute) as a more cost-effective path to enhance model capabilities <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

*   **Cost Efficiency**: While pre-training scaling becomes increasingly difficult, [[scaling_challenges_in_ai_and_test_time_compute | test-time compute]] is still in early stages, offering "a lot of room" for algorithmic improvements and scaling <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Analogy to GPT-2 Era**: The current state of [[scaling_challenges_in_ai_and_test_time_compute | test-time compute]] is compared to the early days of GPT-2, where it was "pretty obvious" that scaling pre-training by 1,000x would lead to a better model <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. A similar opportunity exists for [[scaling_challenges_in_ai_and_test_time_compute | test-time compute]] today <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

> "I thought it would take at least a decade [to scale inference compute generally] it took like 2 or 3 years." <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>

### Potential for Extreme Scaling
Considering the dollar value, a typical ChatGPT query costs about a penny <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. However, for critical problems, people might be willing to pay significantly more, potentially "a million dollars for some of the most important problems that Society cares about" <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. This implies "eight orders of magnitude" of room to push [[scaling_challenges_in_ai_and_test_time_compute | test-time compute]] further, not just by spending more, but through algorithmic improvements <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## Organizational and [[challenges_and_opportunities_in_ai_model_development_and_infrastructure | Development Challenges]]
OpenAI, despite pioneering large-scale pre-training, embraced [[scaling_challenges_in_ai_and_test_time_compute | test-time compute]] research <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. Initially, their motivation for this direction was different—focused on "overcoming the data wall" rather than explicitly scaling [[scaling_challenges_in_ai_and_test_time_compute | test-time compute]] <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. However, the techniques and agendas proved compatible <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

The company's willingness to invest heavily in a "risky Direction" like O1, which was "disruptive to the Paradigm that OpenAI pioneered," demonstrated organizational excellence and adaptability, avoiding the "innovator's dilemma" <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

### Impact on [[infrastructure_changes_for_scaling_ai_models | Hardware]]
The shift towards emphasizing [[scaling_challenges_in_ai_and_test_time_compute | inference compute]] will likely drive significant changes in [[infrastructure_changes_for_scaling_ai_models | hardware]] development <a class="yt-timestamp" data-t="00:35:20">[00:35:20]</a>. Traditionally, the focus was on massive pre-training runs with assumptions of cheap inference costs. This new paradigm creates "an opportunity for a lot of creativity on the hardware side to adapt" <a class="yt-timestamp" data-t="00:35:29">[00:35:29]</a>.

## The "Bitter Lesson" and its Economic Implications
The "Bitter Lesson" from Richard Sutton's essay argues that methods that scale well with more compute and data ultimately outperform approaches that encode human knowledge or rely on complex scaffolding <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>.

*   **Scaffolding vs. Scaling**: Adding "scaffolding and prompting tricks" to models to push their capabilities slightly further is tempting but may not scale well with more data and compute <a class="yt-timestamp" data-t="00:26:48">[00:26:48]</a>.
*   **Long-Term Impact**: Techniques like O1 that inherently scale well with data and compute are expected to become dominant in the long run, making many current scaffolding techniques obsolete <a class="yt-timestamp" data-t="00:27:15">[00:27:15]</a>.
*   **Dilemma for Developers**: Builders, especially startups, face a choice: solve immediate problems with scaffolding, or invest in solutions that align with future scaling trends. Investing heavily in scaffolding for capabilities that soon become "out of the box" in more capable models can be a wasted effort <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.

## [[cost_efficiency_and_accessibility_in_ai | Cost Efficiency and Accessibility]] for Research
The increasing dependence on data and compute resources poses a significant challenge for academic AI research <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>. Academia often incentivizes short-term gains like minor performance improvements on evaluations through clever prompting, which may not translate to impactful long-term research <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>.

Instead, academics are encouraged to:
*   Investigate "novel architectures" or approaches that *demonstrate promising scaling trends* with more data and compute, even if they don't immediately achieve state-of-the-art performance <a class="yt-timestamp" data-t="00:30:21">[00:30:21]</a>.
*   Utilize AI models to run scalable and [[cost_efficiency_and_accessibility_in_ai | cheaper]] experiments in fields like social sciences <a class="yt-timestamp" data-t="00:36:24">[00:36:24]</a>. For example, AI models can simulate human behavior in economic game theory experiments, providing insights at a fraction of the cost and without ethical concerns of human subjects <a class="yt-timestamp" data-t="00:37:07">[00:37:07]</a>.