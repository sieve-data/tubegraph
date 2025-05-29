---
title: Retention and growth challenges in a datadriven business
videoId: D4PDb_C8Dww
---

From: [[lennyspodcast]] <br/> 

Jessica Lax, Vice President of Analytics and Data Science at DoorDash, emphasizes that analytics should be a business impact-driving function, not just a service function <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The goal of a data team is to find opportunities and offer a point of view on decisions, answering "what do we do now that we know this" <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This approach is crucial for navigating the extreme complexity of a business like DoorDash, which involves multiple sides to its marketplace and significant operational elements <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## Structuring Data Teams for Growth

Jessica Lax advocates for a centralized data team model, or a "Center of Excellence," over embedding analytics professionals directly into business units <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. While understanding the desire of business leaders to have embedded resources for control and direct roadmap influence, she believes a central model offers superior value <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

The DoorDash analytics team is structured into pods that align with product, engineering, operations, and marketing teams. This allows data professionals to be de facto embedded with partner teams while reporting centrally <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. This structure ensures that the analytics team shares the same goals as their partner teams, aligning incentives and focusing on the most important initiatives <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

Key benefits of a centralized data organization include:
*   **Consistent and High Talent Bar** Maintaining a uniform standard for technical and soft skills during hiring leads to more consistent and higher-quality talent <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Growth Opportunities** A central organization provides clearer career paths and opportunities for data professionals to move between different areas of the company (e.g., marketing to merchant analytics) or into management roles, aiding [[hiring_and_developing_growth_leaders | talent retention]] <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
*   **Consistency of Methodologies and Metrics** Prevents different teams from having disparate definitions or models (e.g., "sales" defined differently by different teams), ensuring a single source of truth and enabling better scaling <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Strong Team Culture** Fosters a unique culture of learning and sharing, where team members can support each other, conduct peer reviews, and find like-minded "data nerds" <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.

The data team at DoorDash is not a siloed service organization; they are active business partners and thought partners who bring data-driven insights to the table, identifying opportunities for growth and making recommendations <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

## Identifying Growth Opportunities and Prioritization

To ensure the data team is proactive in finding opportunities rather than just answering questions, it's crucial to be intentional about carving out time for exploratory work and deep dives <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. Hackathons are one method used at DoorDash to dedicate days to investigating interesting problems and uncovering opportunities <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

One example of an insight derived from a hackathon involved analyzing consumer acquisition through referrals. Initial data suggested it was a below-average channel. A deep dive revealed fraudulent behavior, where "referral fraud" was rampant, involving users creating new accounts for free discounts <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>. This led to the discovery of a bimodal distribution: one group of high-quality referrers and a second group exploiting the system. The insight resulted in recommendations for stronger fraud checks and caps on referrals, significantly improving the channel's efficiency <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>. This highlights that "the average can be incredibly misleading," and looking at distributions is essential to find optimization opportunities <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.

To manage incoming requests while allowing for proactive work, it's vital to establish a culture where leadership sets clear operating models and goals <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>. By aligning goals with business partners, data teams can explicitly communicate tradeoffs: "if you want me to do this extra new thing, then one of these other things is going to have to drop" <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>. This transparent conversation ensures the team always works on the most impactful initiatives <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>.

## Selecting Effective Metrics

Jessica Lax has learned valuable lessons about defining metrics, often from "bad metrics" <a class="yt-timestamp" data-t="00:44:45">[00:44:45]</a>.

Key principles for metric selection:
*   **Short-term Proxies for Long-term Outcomes** Avoid directly "goaling" on long-term metrics like retention, as they are difficult to influence meaningfully in the short term. Instead, identify short-term input metrics that drive long-term outputs and use experimentation to validate these relationships <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a>.
*   **Simplicity Over Perfection** Resist the urge to create complex composite metrics with weighted coefficients. Simple, intuitive metrics that are easily understood and discussed across the company are more effective at driving real outcomes, even if not "perfect" <a class="yt-timestamp" data-t="00:45:32">[00:45:32]</a>.
*   **Common Currency for Tradeoffs** Quantify the impact of different business levers (e.g., price changes, delivery times, marketing spend) in a common currency, such as Gross Order Value (GOV) or volume, at DoorDash <a class="yt-timestamp" data-t="00:46:40">[00:46:40]</a>. This allows teams to make informed decisions about where to allocate resources to achieve overarching company goals <a class="yt-timestamp" data-t="00:49:48">[00:49:48]</a>.
*   **Focus on Edge Cases and Fail States** While averages are important, actively identifying and setting goals around "fail states" and edge cases (e.g., "never delivered" orders, login errors) is crucial <a class="yt-timestamp" data-t="00:55:32">[00:55:32]</a>. These rare, negative experiences can lead to significant churn and high costs, even if their frequency is low. Addressing them can have a powerful impact on brand reputation and customer [[customer_acquisition_retention_and_the_role_of_ai_in_growth | retention]] <a class="yt-timestamp" data-t="00:58:20">[00:58:20]</a>. Data may not always capture the full picture of these issues, especially if they prevent users from interacting with the product at all (e.g., login failures) <a class="yt-timestamp" data-t="00:59:26">[00:59:26]</a>.

## Culture of Extreme Ownership

A core aspect of DoorDash's success and its data-driven culture is an emphasis on "extreme ownership" of outcomes <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>. This means team members are expected to figure out how to solve problems, regardless of their specific role <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>. Data scientists, for instance, are encouraged to pick up the phone and call customers to gather qualitative insights when quantitative data falls short <a class="yt-timestamp" data-t="00:42:47">[00:42:47]</a>. This willingness to go "outside the traditional bounds" of a role fosters adaptability and problem-solving <a class="yt-timestamp" data-t="00:43:31">[00:43:31]</a>.

The "WeDash" program, where all employees periodically perform deliveries or customer support, builds empathy with customers and Dashers, helping them understand the product experience firsthand and identify bugs <a class="yt-timestamp" data-t="00:38:30">[00:38:30]</a>.

## Leveraging AI for Efficiency

DoorDash is exploring opportunities to use AI to enhance team productivity <a class="yt-timestamp" data-t="01:03:01">[01:03:01]</a>. One initiative involves using AI to empower non-technical users to edit data queries or analyze data on their own, reducing the burden on the analytics team. An internal chatbot, "Ask Data AI," helps users with SQL queries and data analysis, making data more accessible across the company <a class="yt-timestamp" data-t="01:04:05">[01:04:05]</a>. This demonstrates how AI can [[customer_acquisition_retention_and_the_role_of_ai_in_growth | contribute to growth]] by improving data literacy and efficiency.

## Diverse Backgrounds in Data Teams

Lax herself, with a non-traditional background in art and finance, became a data scientist out of necessity at DoorDash <a class="yt-timestamp" data-t="00:29:03">[00:29:03]</a>. This experience influences her hiring strategy, where she values curiosity and self-motivation in candidates, alongside technical skills <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>. She actively recruits individuals from diverse backgrounds—including operations, marketing, and finance—into the analytics team, creating a "net importer of talent" <a class="yt-timestamp" data-t="01:06:03">[01:06:03]</a>. This blend of expertise (e.g., PhDs in statistics, economists, former consultants) fosters an environment where team members can learn from each other and approach problems with varied perspectives, which is vital for [[company_growth_and_scaling_challenges | scaling]] and [[influence_of_a_datadriven_approach_on_company_growth | growth]] <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>.