---
title: Building and scaling a data organization
videoId: D4PDb_C8Dww
---

From: [[lennyspodcast]] <br/> 

Jessica Lax, VP of Analytics and Data Science at DoorDash, discusses her experience building and scaling one of the largest and most impactful data teams in tech. Her insights cover organizational structure, hiring practices, metric definition, and fostering a strong team culture. <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>

## The Role of Analytics: Business Impact Driving Function

For Jessica Lax, analytics is a business impact driving function, not merely a service function that answers questions through Jira tickets or builds dashboards <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. The goal is to find opportunities and offer a point of view on decisions, moving beyond "why" to "what do we do now that we know this?" <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

## Organizational Structure: Centralized vs. Embedded

Jessica strongly advocates for a [[centralized_vs_embedded_data_team_structures | centralized data team model]], or a "Center of Excellence," over embedding analytics teams within business units <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. While Business Leaders may prefer embedded teams for immediate control and camaraderie, a centralized model can address these benefits while offering significant advantages <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

At DoorDash, the centralized analytics team is divided into "pods" that align with how product, engineering, operations, and marketing are structured <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. This means team members are *de facto* embedded with partner teams, sharing the same goals and aligning incentives, even though their reporting structure is centralized <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. This prevents the perception of a siloed service organization, instead positioning the analytics team as business and thought partners <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

### Benefits of a Centralized Data Organization

-   **Consistent and High Talent Bar:** A centralized structure allows for a consistent evaluation bar for technical and soft skills, leading to higher-quality hires <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
-   **Growth Opportunities:** It provides more growth opportunities for individuals to move across different functional areas (e.g., marketing to merchant analytics) or into people management roles, which helps retain talent <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
-   **Consistency of Methodologies and Metrics:** Prevents different teams from having varying definitions of the same metric (e.g., "sales"), ensuring a unified understanding across the company <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. It also allows for collective improvement of methodologies and prevents redundant work like building the same churn prediction model multiple times <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
-   **Scalability:** A centralized team can identify and address common problems across different business units, allowing for automation and improvement initiatives that support [[company_growth_and_scaling_challenges | company growth and scaling challenges]] <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.
-   **Strong Team Culture:** Fosters a unique culture of learning and sharing, where team members can support each other, conduct peer reviews, and find "like-minded data nerds" <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.

## Balancing Proactive Insights and Reactive Requests

It is essential to intentionally carve out time for exploratory work and deep dives, as reactive questions can easily consume all available time <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.

-   **Setting Goals for Self-Directed Work:** Teams should have goals specifically around finding insights through self-directed work to maintain accountability <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.
-   **Hackathons:** DoorDash holds hackathons to dedicate days for teams to investigate interesting areas and identify opportunities <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. Many significant insights that drive future roadmaps have come from these sessions <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.
    -   *Example:* A hackathon deep dive into referral acquisition revealed a bimodal distribution of consumers, where a subset of fraudulent behavior dragged down overall channel efficiency <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>. This led to recommendations for better fraud checks and referral caps, significantly improving the channel's efficiency <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.
-   **Communicating Trade-offs:** When faced with numerous requests, data teams should communicate the trade-offs to business partners. This helps partners understand the impact of new requests on existing priorities and encourages alignment on the most important tasks <a class="yt-timestamp" data-t="00:22:19">[00:22:19]</a>.

## Hiring for Data Teams

Beyond technical skills, which are "table stakes," Jessica looks for specific characteristics when hiring data talent:

-   **Curiosity and Self-Motivation:** The ability to pull on threads, notice anomalies, and proactively investigate without being told <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>. This can be tested in interviews by presenting cases with subtle inconsistencies and observing if candidates notice or how they react when pointed out <a class="yt-timestamp" data-t="00:25:44">[00:25:44]</a>.
-   **Problem-Solving Skills:** Using real-world business cases to assess how candidates break down problems, handle ambiguity, and make decisions without full information <a class="yt-timestamp" data-t="00:27:04">[00:27:04]</a>.
-   **Adaptability to Feedback:** Observing how candidates react to being told they are wrong and their ability to pivot or take new information into account <a class="yt-timestamp" data-t="00:27:56">[00:27:56]</a>.
-   **Point of View:** Encouraging candidates to express a clear opinion or decision even with incomplete information, reflecting real-world business scenarios <a class="yt-timestamp" data-t="00:28:24">[00:28:24]</a>.

## Defining and Picking Metrics

Jessica emphasizes that learning from "bad metrics" is key to picking good ones <a class="yt-timestamp" data-t="00:44:45">[00:44:45]</a>.

-   **Short-Term Proxies for Long-Term Outputs:** Avoid goal-setting on long-term, hard-to-move metrics like retention <a class="yt-timestamp" data-t="00:45:01">[00:45:01]</a>. Instead, identify and test short-term inputs that are known to drive the desired long-term outcomes through experimentation <a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>.
-   **Simplicity Over Perfection:** Simple metrics that are easily understood and intuitively relatable across the company are far more effective than complex composite metrics with coefficients, even if the latter are theoretically "more perfect" <a class="yt-timestamp" data-t="00:45:33">[00:45:33]</a>.
    -   *Example:* A complex "Merchant Health score" that was hard to interpret was replaced with simpler, actionable metrics like "new merchants getting an order within seven days" and "merchant photo coverage" <a class="yt-timestamp" data-t="00:50:56">[00:50:56]</a>. This allows teams to understand what they are trying to move and prioritize efforts effectively <a class="yt-timestamp" data-t="00:52:30">[00:52:30]</a>.
-   **Common Currency for Trade-offs:** Quantify all business levers (e.g., price, delivery times, selection) in a common currency (e.g., gross order value or volume) <a class="yt-timestamp" data-t="00:46:40">[00:46:40]</a>. This enables better decision-making by allowing different teams (e.g., marketing vs. logistics) to compare the impact of their initiatives on overall business goals <a class="yt-timestamp" data-t="00:47:07">[00:47:07]</a>. This is particularly crucial in a multi-sided marketplace with complex trade-off decisions <a class="yt-timestamp" data-t="00:50:21">[00:50:21]</a>.
-   **Focus on Edge Cases and Fail States:** While averages are important, it's crucial to examine and set goals around rare "disaster deliveries" or "fail states" that lead to significant customer churn and high costs (e.g., "never delivered" orders) <a class="yt-timestamp" data-t="00:55:29">[00:55:29]</a>. These "moments of truth" can be incredibly damaging and expensive, even if infrequent <a class="yt-timestamp" data-t="00:58:31">[00:58:31]</a>.
    -   *Important Note:* Data teams should consider "what data don't we have?" especially in cases like login errors, where affected users may not even appear in the data being analyzed <a class="yt-timestamp" data-t="00:59:40">[00:59:40]</a>.

## Fostering a Culture of Extreme Ownership

The culture at DoorDash, instilled by CEO Tony Xu, emphasizes "extreme ownership" over outcomes <a class="yt-timestamp" data-t="00:34:16">[00:34:16]</a>.

-   **Beyond Job Descriptions:** Data scientists are expected to figure out what's happening and act on it, even if it means picking up the phone to call customers for qualitative research, rather than strictly adhering to their job title <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>. This is seen as part of the job to unblock the team and inform future decisions <a class="yt-timestamp" data-t="00:43:05">[00:43:05]</a>.
-   **Customer-First Mentality:** All employees, including analytics staff, are encouraged to engage directly with all customer segments (consumers, Dashers, merchants) <a class="yt-timestamp" data-t="00:36:32">[00:36:32]</a>. DoorDash's "We Dash" program requires all employees to "go dashing" or perform customer support four times a year <a class="yt-timestamp" data-t="00:38:30">[00:38:30]</a>. This builds empathy, provides product insights, and helps catch bugs <a class="yt-timestamp" data-t="00:39:09">[00:39:09]</a>.

## Global Data Organization

Managing a global data organization introduces complexities like different currencies, languages, and regulations (e.g., EU countries) <a class="yt-timestamp" data-t="01:00:51">[01:00:51]</a>. However, many problems encountered are similar across regions, allowing for leverage of past experiences, while new challenges keep things interesting <a class="yt-timestamp" data-t="01:01:28">[01:01:28]</a>.

## Leveraging AI for Productivity

AI offers opportunities to enhance team productivity and empower non-technical users <a class="yt-timestamp" data-t="01:03:01">[01:03:01]</a>.

-   **"Ask Data AI":** DoorDash is building internal tools, like a chatbot named "Ask Data AI" (after their internal Slack channel), to help non-technical users edit SQL queries or adjust them for specific business segments (e.g., grocery) <a class="yt-timestamp" data-t="01:04:02">[01:04:02]</a>. This frees up the analytics team's bandwidth and enables self-service <a class="yt-timestamp" data-t="01:04:36">[01:04:36]</a>.

## Recruiting and Building a Diverse Team

Jessica believes in hiring people who may not have a traditional data science background, similar to her own journey from operations to analytics <a class="yt-timestamp" data-t="01:05:41">[01:05:41]</a>.

-   **Importing Talent from Partner Teams:** DoorDash actively encourages transitions from other departments (e.g., engineering, operations, marketing, finance) into the analytics team, becoming a "net importer of talent" <a class="yt-timestamp" data-t="01:06:03">[01:06:03]</a>. These individuals often acquire necessary technical skills on the job or through prior training <a class="yt-timestamp" data-t="01:06:41">[01:06:41]</a>.
-   **Complementary Skills and Diverse Backgrounds:** Building a team with varied expertise—from statisticians and economists to individuals with finance or consulting backgrounds—fosters an environment where everyone can learn from each other and bring unique perspectives <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>.
-   **Diversity of Company Stage Experience:** Hiring individuals from both startups (for hustle and grit) and larger, more mature companies (for understanding scale and anticipating problems) provides a blend of experience that allows the team to "see around corners" <a class="yt-timestamp" data-t="01:08:04">[01:08:04]</a>.

## Personal Philosophy and Advice

-   **Problem-Solving Mindset:** Focus on solving the problem directly in front of you, even if it means learning new skills or stepping outside your defined role <a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>. This organic approach, driven by necessity and a desire to win, can lead to unexpected career paths <a class="yt-timestamp" data-t="00:32:09">[00:32:09]</a>.
-   **Embrace Non-Traditional Paths:** Don't let a lack of formal training deter you from pursuing a field if you have a passion for problem-solving <a class="yt-timestamp" data-t="00:29:28">[00:29:28]</a>. Jessica, with an art background, taught herself SQL and Python out of necessity at DoorDash <a class="yt-timestamp" data-t="00:29:43">[00:29:43]</a>.
-   **Trust in Sleep:** When facing difficult problems or tense communications, stepping away to "sleep on it" can provide a fresh perspective and lead to clearer, less emotional responses <a class="yt-timestamp" data-t="01:11:47">[01:11:47]</a>.

>[!TIP] **Truth Seeking**
>Jessica encourages everyone to "truth seek" – to actively seek out what's fact versus fiction in a world of misinformation <a class="yt-timestamp" data-t="01:18:48">[01:18:48]</a>. This value, deeply ingrained at DoorDash, emphasizes critical thinking and speaking the truth <a class="yt-timestamp" data-t="01:19:06">[01:19:06]</a>.