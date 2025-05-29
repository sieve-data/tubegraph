---
title: The role of trust in successful experimentation
videoId: hEzpiDuYFoE
---

From: [[lennyspodcast]] <br/> 
The role of [[The importance of trust and collaboration in team environments | trust]] in successful experimentation is paramount. An experimentation platform serves as both a safety net and an oracle, providing data to guide decisions [00:52:06]. For this system to be effective, its results must be [[Trust Building and Impact Focus in Product Management | trustworthy]] [00:52:48]. Building this [[Creating a culture of experimentation in a company | trust]] is crucial, as it is easily lost [00:52:43].

### Trust as a Safety Net
The platform acts as a safety net by enabling quick abortion of bad launches, ensuring "safe deployments" and "safe velocity" [00:52:18]. By identifying and stopping issues, the platform helps prevent negative impacts on users and the business.

### Trust as an Oracle
The platform's role as an oracle is to provide clear, reliable results on key metrics and guardrail metrics after an experiment [00:52:27]. This allows teams to make data-driven decisions confidently.

### Maintaining Trust in Results
To maintain [[Trust Building and Impact Focus in Product Management | trust]], it is vital that the platform's outputs are accurate. When something is wrong with an experiment, the system should stop and alert users [00:53:14].

#### Common Issues Affecting Trust
Several factors can undermine the [[Trust Building and Impact Focus in Product Management | trustworthiness]] of experimental results:

*   **Statistical Naivete in Early Platforms**: Some early experimentation platforms, like Optimizely in its initial days, were statistically naive [00:53:31]. They offered real-time P-value computations and allowed users to stop experiments when a P-value appeared statistically significant [00:53:37]. This practice significantly inflates the Type I error (false positive rate), potentially leading to a 30% error rate instead of the expected 5% [00:54:02]. Such inaccuracies caused users to question the platform's reliability, as claimed positive revenue increases weren't observed over time [00:54:24]. A famous example, documented in a post titled "Optimizely almost got me fired," involved an A/A test (where A and B groups are identical) showing statistically significant differences too many times, directly eroding [[Trust Building and Impact Focus in Product Management | trust]] [00:54:30].
*   **Sample Ratio Mismatch (SRM)**: This is the most common issue causing experiment invalidity [00:55:53]. If an experiment is designed to send 50% of users to control and 50% to treatment, any significant deviation (e.g., 50.2% vs. 49.8% in a large experiment) is a red flag indicating something is wrong [00:56:01]. This probability can be calculated to determine if the split could have happened by chance [00:56:43]. At Microsoft, 8% of experiments suffered from SRM [00:57:24].
    *   **Causes of SRM**: Common causes include bots hitting control/treatment groups in different proportions or issues within the data pipeline [00:57:51].
    *   **Addressing SRM**: Initially, banners were used to warn users about SRM, but people often ignored them [00:59:23]. Later, scorecards were blanked out with an "OK" button to debug, and eventually, every number was highlighted with a red line to ensure visibility even in screenshots [00:59:37].
*   **[[Challenges and failures in experimentation | Twyman's Law]]**: This principle states that "if any figure that looks interesting or different is usually wrong" [01:00:56]. When results seem "too good to be true" (e.g., a 10% movement when typical movements are under 1%), it warrants investigation [01:01:13]. In approximately nine out of ten cases, a flaw is found [01:01:41].
*   **P-value Misinterpretation**: Many people incorrectly interpret a P-value (e.g., 0.02) as the probability that the treatment is 98% better than the control [01:02:42]. The P-value actually assumes the null hypothesis is true and computes the probability of observing the data [01:03:11]. To get the desired probability of the hypothesis given the data, Bayes' Rule is needed, incorporating the prior probability of success [01:03:30]. This reveals a much higher "false positive risk" [01:04:06]. For instance, at Airbnb search, where the success rate was only 8%, a statistically significant result (P-value < 0.05) had a 26% chance of being a false positive, not 5% [01:04:44]. To mitigate this, teams should aim for lower P-values (e.g., < 0.01) and consider replication for high-stakes experiments [01:05:01].

### Building a [[Building and optimizing an experimentation platform | Trustworthy Platform]]
To foster [[Trust Building and Impact Focus in Product Management | trust]] and enable efficient experimentation, investing in a robust platform is key [01:11:41]. A well-developed platform should:
*   Minimize the marginal [[The importance of experimentation and longterm experiments in growth | cost of running an experiment]] to near zero [01:34:36].
*   Provide self-service capabilities for experiment setup, metric definition, and analysis [01:10:39].
*   Automate analysis to reduce dependence on data scientists [01:11:46].
*   Implement rigorous checks for issues like SRM, stopping experiments and providing debugging tools when problems arise [00:53:07].
*   Utilize variance reduction techniques (e.g., capping metrics, CUPED) to get statistically significant results faster and reduce the need for more users [01:13:04].

By prioritizing [[Trust Building and Impact Focus in Product Management | trust]] through robust [[Building and optimizing an experimentation platform | platform]] development and understanding statistical nuances, organizations can ensure their experimentation efforts lead to reliable insights and continuous [[The importance of experimentation and longterm experiments in growth | growth]].