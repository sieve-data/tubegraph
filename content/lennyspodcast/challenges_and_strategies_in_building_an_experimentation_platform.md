---
title: Challenges and strategies in building an experimentation platform
videoId: hEzpiDuYFoE
---

From: [[lennyspodcast]] <br/> 

Developing a robust experimentation platform is crucial for organizations aiming to become data-driven and optimize product development. While not "easy" to build, a well-implemented platform can significantly reduce the marginal cost of running experiments, enabling continuous improvement and informed decision-making <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.

## Why Build an Experimentation Platform?

The primary motivation behind building an experimentation platform is to drive the marginal cost of running experiments down to zero <a class="yt-timestamp" data-t="01:10:34">[01:10:34]</a>. At Microsoft, for instance, once the platform matured, the cost of running experiments became so low that it was unquestioned for everything to be experimented with <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.

Key benefits of a mature platform include:
*   **Self-Service Capabilities** The platform should allow users to easily set up and run experiments, define targets, and select metrics without extensive manual intervention <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.
*   **Automated Analysis** To reduce reliance on data scientists, the platform should automate analysis, providing scorecards quickly after an experiment concludes <a class="yt-timestamp" data-t="01:11:51">[01:11:51]</a>, ideally within a day <a class="yt-timestamp" data-t="01:12:57">[01:12:57]</a>.
*   **Scalability** As the number of experiments grows (e.g., 20,000-25,000 annually at Microsoft <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>), the platform must efficiently manage and analyze vast amounts of data <a class="yt-timestamp" data-t="01:11:01">[01:11:01]</a>.
*   **Institutional Memory** A platform helps document and organize experiment history, enabling teams to search by keywords and learn from past successes and failures, fostering [[the_role_of_organizational_culture_in_experimentation_success | institutional learning]] <a class="yt-timestamp" data-t="01:17:04">[01:17:04]</a>.

## Challenges in Building and Adopting a Platform

Organizations often face several [[challenges_and_strategies_in_startup_growth | challenges]] when building and adopting an experimentation platform:

*   **Initial Investment and Maturity**: Building a platform requires significant investment and is not easy, especially at early stages <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>. Less mature platforms, like Airbnb's at one point, require more analysts to interpret results <a class="yt-timestamp" data-t="03:07:08">[03:07:08]</a>, increasing costs.
*   **Organizational Resistance**: There can be denial or resistance to embracing data-driven approaches, especially when early [[experimentation_and_datadriven_decision_making | data]] reveals high failure rates for ideas (e.g., "we have better PMs here") <a class="yt-timestamp" data-t="00:40:22">[00:40:22]</a>.
*   **Maintaining Trust**: Trust is the most important element for a successful experimentation platform and culture <a class="yt-timestamp" data-t="00:52:08">[00:52:08]</a>.
    *   **Statistical Naivety**: Early implementations by third-party vendors (like Optimizely) demonstrated how statistically naive approaches could inflate [[experimentation_and_longterm_impact_measurement | false positive rates]] (e.g., 30% instead of 5%) <a class="yt-timestamp" data-t="00:54:05">[00:54:05]</a>, leading to a loss of trust in the platform's results <a class="yt-timestamp" data-t="00:54:51">[00:54:51]</a>.
    *   **Sample Ratio Mismatch (SRM)**: A common issue where the observed distribution of users to control and treatment groups deviates from the expected random split (e.g., 50/50) <a class="yt-timestamp" data-t="00:55:53">[00:55:53]</a>. This often indicates underlying issues like bot traffic or data pipeline problems <a class="yt-timestamp" data-t="00:59:04">[00:59:04]</a>. If undetected, it invalidates experiment results <a class="yt-timestamp" data-t="00:57:01">[00:57:01]</a>. Microsoft initially found 8% of experiments suffered from SRM <a class="yt-timestamp" data-t="00:57:22">[00:57:22]</a>.
    *   **Twyman's Law**: This states that "if any figure that looks interesting or different is usually wrong" <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>. If an experiment yields a surprisingly large positive result (e.g., 10% movement vs. normal 1%) <a class="yt-timestamp" data-t="01:01:21">[01:01:21]</a>, it's often due to a flaw that needs investigation <a class="yt-timestamp" data-t="01:01:36">[01:01:36]</a>. Nine out of ten times, such "too good to be true" results are flawed <a class="yt-timestamp" data-t="01:01:41">[01:01:41]</a>.
    *   **Bias Towards Success**: People naturally want to see positive results, sometimes leading them to ignore warnings or push through invalid experiments <a class="yt-timestamp" data-t="01:00:34">[01:00:34]</a>. Organizations must be disciplined to fight this bias <a class="yt-timestamp" data-t="01:00:39">[01:00:39]</a>.

## Strategies for Building and Fostering Experimentation

*   **Start Small and Iterate**: Begin building the platform when you have at least tens of thousands of users <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>. Full [[importance_of_ab_testing_and_experimentation | AB testing]] and the detection of smaller, yet significant, changes (e.g., 5-10% impact) require around 200,000 users <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.
*   **Build Trust from the Ground Up**:
    *   **Robust Checks**: Implement checks like SRM detection from the beginning. If an experiment shows issues, blank out the scorecard with a warning, forcing users to acknowledge the problem before viewing potentially flawed results <a class="yt-timestamp" data-t="00:59:40">[00:59:40]</a>.
    *   **Statistical Rigor**: Ensure that the platform's statistical analysis is sound and addresses issues like inflated false positive rates, even recommending replication for less certain results <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a>.
    *   **Transparency**: Highlight problematic results (e.g., with red lines on screenshots) to prevent miscommunication <a class="yt-timestamp" data-t="01:00:18">[01:00:18]</a>.
*   **Define a Clear Overall Evaluation Criterion (OEC)**:
    *   The OEC is the single metric (or composite) that an organization optimizes for <a class="yt-timestamp" data-t="02:28:25">[02:28:25]</a>.
    *   It should reflect long-term value, such as lifetime value of the user <a class="yt-timestamp" data-t="02:29:43">[02:29:43]</a>.
    *   It should include "guardrail" metrics to prevent negative impacts on user experience while optimizing for primary goals (e.g., increasing revenue without hurting user retention) <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.
    *   For example, measuring the cost of "spamming" users by tracking unsubscribe rates and integrating it into the OEC can prevent negative long-term impacts <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>.
    *   The OEC must be directionally agreed upon by all stakeholders; if half the team thinks more time on site is good and the other half thinks it's bad, the OEC is flawed <a class="yt-timestamp" data-t="01:09:55">[01:09:55]</a>.
*   **Cultivate an Experimentation Culture**:
    *   **Strategic Rollout**: Start with a "beachhead" team that launches frequently (e.g., weekly or daily) and where an OEC is easily defined <a class="yt-timestamp" data-t="01:08:42">[01:08:42]</a>.
    *   **Share Learnings**: Once successful, share surprising results across the company to build internal advocacy <a class="yt-timestamp" data-t="01:08:15">[01:08:15]</a>. Cross-pollination of talent from successful experimental teams also helps <a class="yt-timestamp" data-t="01:08:23">[01:08:23]</a>.
    *   **Promote "Test Everything"**: Encourage the mindset that any code change or feature introduction should be part of an experiment <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>. This reveals unexpected impacts, even from small bug fixes <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.
    *   **Embrace Failure**: Organizations must be ready to accept that most ideas will fail (e.g., 66% at Microsoft, 85% at Bing, 92% at Airbnb search) <a class="yt-timestamp" data-t="01:13:20">[01:13:20]</a>. This applies especially to high-risk, high-reward "big bets" that might break out of a local maxima but often fail (e.g., 80% of the time) <a class="yt-timestamp" data-t="02:22:11">[02:22:11]</a>.
    *   **Iterate on Redesigns**: Avoid large, monolithic redesigns that are difficult to undo if they fail <a class="yt-timestamp" data-t="01:16:50">[01:16:50]</a>. Instead, break them into smaller, testable steps to learn and adjust along the way <a class="yt-timestamp" data-t="01:17:05">[01:17:05]</a>.
*   **Optimize for Speed and Efficiency**:
    *   **Variance Reduction Techniques**: Implement methods like capping skewed metrics or using CUPED (Controlled-experiment Using Pre-Experiment Data) to reduce metric variance. This allows for statistically significant results with fewer users, leading to faster experiment cycles <a class="yt-timestamp" data-t="01:13:04">[01:13:04]</a>.
    *   **Build vs. Buy**: Early-stage companies might benefit from using third-party experimentation platforms, which are more mature today than in the past <a class="yt-timestamp" data-t="01:07:34">[01:07:34]</a>. A hybrid approach of building some and buying some components is also common <a class="yt-timestamp" data-t="01:07:06">[01:07:06]</a>.
    *   **Structured Narratives**: Adopt practices like Amazon's structured narratives instead of PowerPoints for product development. This fosters clear communication, encourages honest feedback, and preserves institutional memory within the document itself <a class="yt-timestamp" data-t="01:19:16">[01:19:16]</a>.

By addressing these [[challenges_and_strategies_in_product_management | challenges]] and implementing strategic approaches, organizations can build effective [[experimentation_and_datadriven_decision_making | experimentation]] platforms that foster a culture of [[importance_of_ab_testing_and_experimentation | learning]] and data-driven decision-making, ultimately driving long-term product success.