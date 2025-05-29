---
title: The role of organizational culture in experimentation success
videoId: hEzpiDuYFoE
---

From: [[lennyspodcast]] <br/> 

[[Role of company culture in product management | Organizational culture]] plays a crucial role in the success of experimentation within a company, influencing everything from the adoption of A/B testing to the interpretation and application of results <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. Rani Kohavi, a world expert on A/B testing and experimentation, emphasizes that building [[trust is the most important element of a successful experiment culture | trust]] in the experimentation platform and its results is paramount <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, <a class="yt-timestamp" data-t="00:51:53">[00:51:53]</a>.

## Embracing a "Test Everything" Philosophy
A core aspect of an experiment-driven culture is the commitment to "test everything" <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This means that any code change or new feature should be introduced within an experiment <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This approach is vital because even small bug fixes or minor changes can have surprising and unexpected impacts <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Accepting and Learning from Failure
A significant cultural shift is required to embrace the reality of high failure rates in experimentation. Data indicates that a large percentage of ideas will not improve the desired metrics:
*   Approximately two-thirds (66%) of ideas failed at Microsoft overall <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.
*   At Bing, a more optimized domain, the failure rate was around 85% <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   In Airbnb's search relevance team, the observed failure rate was 92% of experiments <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>, <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
Other companies like Booking and Google Ads also report failure rates of 80% to 90% <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.

Organizations must be ready to accept that most high-risk, high-reward ideas are likely to fail (around 80% of the time) <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>, <a class="yt-timestamp" data-t="00:22:19">[00:22:19]</a>, <a class="yt-timestamp" data-t="00:43:21">[00:43:21]</a>. Initially, groups often believe they are different and will have a higher success rate, but they are consistently humbled by the data <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>, <a class="yt-timestamp" data-t="00:39:37">[00:39:37]</a>.

### Countering Bias and [[Twyman's Law]]
A strong experimentation culture actively fights the natural human bias towards success. When a result looks "too good to be true," organizations should pause celebrations and investigate <a class="yt-timestamp" data-t="01:01:21">[01:01:21]</a>. This concept aligns with [[Twyman's Law]], which states that any figure that looks interesting or different is usually wrong <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>. In practice, 9 out of 10 times when this law is invoked, a flaw is found in the experiment <a class="yt-timestamp" data-t="01:01:38">[01:01:38]</a>.

## Addressing Concerns: Micro-Optimizations vs. [[Innovating within large organizations | Innovation]]
A common concern is that being too experiment-driven leads only to micro-optimizations and hinders [[Innovating within large organizations | innovation]] <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a>. However, experimentation allows for a balanced portfolio of ideas:
*   **Incremental Changes:** These move the product in a known successful direction <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>.
*   **High-Risk, High-Reward Ideas:** Companies must allocate resources to these "home run" ideas, even if they are most likely to fail <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>. Examples include Bing's social integration effort, which involved a hundred person-years of effort but ultimately failed <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>. Similarly, Netflix and Airbnb experienced failures with social components <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>, <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>.

Experimentation acts as an "Oracle" or "Arbiter," providing data on whether users actually benefit from changes <a class="yt-timestamp" data-t="00:24:27">[00:24:27]</a>, <a class="yt-timestamp" data-t="00:24:35">[00:24:35]</a>. This prevents the "sunk cost fallacy" where teams ship features simply because a lot of effort has been invested <a class="yt-timestamp" data-t="00:37:41">[00:37:41]</a>. If an experiment shows negative or flat results, the feature should not be shipped, as it adds maintenance overhead without value <a class="yt-timestamp" data-t="00:44:50">[00:44:50]</a>.

## The Overall Evaluation Criterion (OEC)
A critical element of a successful experimentation culture is clearly defining the [[Company Culture and Decision Making | Overall Evaluation Criterion]] (OEC) – what the company is optimizing for <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>. This is more complex than simply optimizing for revenue, as short-term revenue gains can hurt the long-term user experience <a class="yt-timestamp" data-t="00:28:38">[00:28:38]</a>. The OEC should be causally predictive of the user's lifetime value <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>.

The OEC often involves a constraint optimization problem, balancing revenue with user experience metrics (e.g., churn, time to success, successful sessions) <a class="yt-timestamp" data-t="00:29:43">[00:29:43]</a>, <a class="yt-timestamp" data-t="00:30:34">[00:30:34]</a>. For example, at Amazon, an OEC for email campaigns balanced revenue from clicks with the long-term cost of unsubscribes, revealing that over half of campaigns were negative when accounting for user lifetime value <a class="yt-timestamp" data-t="00:34:32">[00:34:32]</a>, <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>.

## Building and Maintaining Trust in Results
Maintaining trust in the experimentation platform is crucial <a class="yt-timestamp" data-t="00:52:08">[00:52:08]</a>. Issues like inaccurate statistical calculations (e.g., Optimizely's early real-time p-value monitoring leading to inflated false positive rates) can erode this trust <a class="yt-timestamp" data-t="00:53:31">[00:53:31]</a>.

Key practices for building trust:
*   **Sample Ratio Mismatch (SRM) Detection:** A common problem where the allocation of users to control and treatment groups deviates significantly from the designed ratio. This is a major red flag indicating potential invalidity of results <a class="yt-timestamp" data-t="00:55:53">[00:55:53]</a>. At Microsoft, 8% of experiments suffered from SRM <a class="yt-timestamp" data-t="00:57:24">[00:57:24]</a>.
*   **Transparency:** When an SRM is detected, results should be clearly flagged or even hidden until the issue is resolved, forcing investigation <a class="yt-timestamp" data-t="00:59:21">[00:59:21]</a>.
*   **Understanding P-values:** Misinterpretation of p-values is common. A p-value of 0.05 does not mean there's a 95% probability that the treatment is better than control. The actual false positive risk can be much higher (e.g., 26% at Airbnb search) <a class="yt-timestamp" data-t="01:02:42">[01:02:42]</a>, <a class="yt-timestamp" data-t="01:04:44">[01:04:44]</a>. To counter this, teams may need to set stricter p-value thresholds (e.g., below 0.01) or replicate experiments <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a>.

## [[Leadership and company culture | Cultivating an entrepreneurial culture within organizations | Shifting Company Culture]]
Transitioning to an experiment-driven culture, especially in large organizations, takes time and strategic effort <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Start with a Beachhead:** Identify a team or product area where experimentation is easy to implement and results can be quickly observed. This means focusing on teams that launch frequently (e.g., weekly or daily sprints) rather than those with long release cycles <a class="yt-timestamp" data-t="01:08:37">[01:08:37]</a>.
*   **Share Successes and Learnings:** Once successful, share the surprising results and learnings across the company. This builds momentum and encourages other teams to adopt experimentation <a class="yt-timestamp" data-t="01:08:15">[01:08:15]</a>.
*   **[[Institutional memory]] and Learning:** Actively summarize and document experiment learnings (both successes and failures) <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>. Regular meetings to discuss the most surprising experiments (those with unexpected outcomes, positive or negative) can foster learning and reinforce the culture <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.
*   **Platform Investment:** Investing in a robust experimentation platform is key. A mature platform should reduce the marginal cost of running an experiment to near zero, allowing teams to self-service experiment setup, metric definition, and analysis <a class="yt-timestamp" data-t="00:25:40">[00:25:40]</a>, <a class="yt-timestamp" data-t="01:10:32">[01:10:32]</a>.
*   **Leadership Support:** Strong [[Leadership and company culture | leadership]] support is crucial. At Microsoft, leaders like Satya Nadella and Qi Lu championed the adoption of experimentation across the company <a class="yt-timestamp" data-t="00:41:01">[00:41:01]</a>.

Ultimately, an effective experimentation culture is characterized by humility, a willingness to fail, and a deep commitment to data-driven decision-making grounded in trustworthy results <a class="yt-timestamp" data-t="00:53:57">[00:53:57]</a>, <a class="yt-timestamp" data-t="00:39:37">[00:39:37]</a>.