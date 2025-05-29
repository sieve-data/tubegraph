---
title: Centralized vs embedded data team structures
videoId: D4PDb_C8Dww
---

From: [[lennyspodcast]] <br/> 

Jessica Lax, Vice President of Analytics and Data Science at DoorDash, has built one of the largest and most respected data teams in the tech industry. Her perspective on structuring data teams is considered contrarian, emphasizing that analytics should function as a business impact-driving entity rather than purely a service function [00:05:15]. For Lax, analytics teams should not merely answer "why" but also "what do we do now that we know this?" [00:00:11].

## Defining Data Team Structures
Lax believes that analytics should hold a significant "seat at the table" alongside engineering and product [00:05:07]. This contrasts with traditional analytics teams that might be seen as service functions, answering questions via tickets or building dashboards [00:05:20].

A key point of contention for Lax is whether data teams should be embedded within business units or centrally organized [00:06:00].
*   **Embedded Model**: Analytics personnel report directly into business units (e.g., marketing analytics reporting to marketing) [00:06:03].
*   **Centralized Model**: Analytics is part of a broader, central analytics team, reporting up through a central organization (e.g., to Jessica Lax at DoorDash), while still dividing into "pods" that map to specific business units [00:06:07].

DoorDash operates a [[building_and_scaling_a_data_organization | centralized analytics team]] where individuals are de facto embedded with partner teams like product, engineering, operations, and marketing. This structure ensures that the analytics team shares the same goals as their partner teams, aligning incentives and focusing on the most important initiatives [00:08:22]. Lax emphasizes that this model does *not* create a siloed, service-oriented data team; rather, they are business and thought partners expected to bring data-driven insights and identify opportunities [00:09:48].

## Benefits of a Centralized Data Team Structure
Jessica Lax identifies several significant advantages of a centralized data team model:

*   **Consistent and High Talent Bar** <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>: It allows for a uniform standard in evaluating candidates for technical and soft skills, leading to more consistent and higher-quality talent acquisition.
*   **Growth Opportunities and Talent Retention** <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>: Individuals are not siloed within specific business units. They can explore growth opportunities in other areas of the company, tackling new problems (e.g., moving from marketing to merchant analytics) or pursuing management roles within the broader data organization [00:11:56]. This engagement helps retain talent.
*   **Consistency of Methodologies and Metrics** <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>: A centralized team ensures that all departments use the same definitions and methodologies for key metrics (e.g., "sales"), preventing discrepancies and improving the quality of analysis through shared input [00:12:51]. It also prevents redundant work, such as building the same churn prediction model across different teams [00:13:13].
*   **Scalability and Proactive Problem Solving** <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>: By observing common problems across various teams, the central organization can proactively identify issues that need automation or improvement, helping the business anticipate and address challenges as it scales [00:13:26].
*   **Strong Team Culture and Brand** <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>: Fosters a unique culture of learning and sharing within the analytics team, promoting camaraderie and allowing team members to support each other through challenges and peer review [00:13:59]. This internal brand also aids in external recruiting of top talent [00:13:50].

## Balancing Proactive and Reactive Work
A significant challenge for data teams is balancing exploratory, proactive work with the constant stream of ad-hoc questions and requests [00:15:14]. Lax advises that this balance requires intentional effort:

*   **Carve Out Time** <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>: Teams must be intentional about dedicating time for deep dives and exploratory work, as ad-hoc requests can easily consume all available hours [00:15:53].
*   **Set Goals for Self-Directed Work** <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>: Setting specific goals for finding insights through self-directed work helps hold the team accountable for this type of activity [00:16:09].
*   **Hackathons** <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>: DoorDash uses hackathons to dedicate days specifically for exploring interesting problems and finding opportunities [00:16:52].
    *   **Example**: A hackathon revealed significant referral fraud, which was initially masked by average performance metrics. The deep dive involved team members committing referral fraud themselves by ordering cupcakes to understand the loopholes [00:18:12]. This led to recommendations for better fraud checks and caps on referrals, significantly improving the efficiency of the marketing channel [00:19:59].

## Managing Requests and Prioritization
For data professionals struggling to push back on immediate, smaller requests, Lax offers the following advice:

*   **Leadership's Role** <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>: Leadership must establish a clear operating model and culture that empowers junior team members to decline requests without constantly having to say "no" directly [00:21:19].
*   **Goal Alignment** <a class="yt-timestamp" data-t="00:21:30">[00:21:30]</a>: Because the data team's goals are aligned with their business partners, they can frame discussions around priorities. It becomes a conversation about what work will best help *both* teams achieve their shared goals [00:21:35].
*   **Communicate Tradeoffs** <a class="yt-timestamp" data-t="00:22:19">[00:22:19]</a>: Instead of just saying no, explicitly state what planned work would need to be dropped to accommodate a new request [00:22:21]. This forces partners to understand the implications of their requests and helps make collaborative prioritization decisions [00:22:48].
*   **Build Goodwill** <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>: Occasionally taking on quick, low-effort requests can help build goodwill with partners [00:23:51].

## Hiring for a Data Team
Beyond standard technical skills, Lax looks for specific, less common traits when hiring for her data team:

*   **Curiosity** <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>: An innate desire to "pull on threads" when something seems off, proactively investigating anomalies even when a task is technically complete [00:25:03]. This is difficult to teach but can be identified through interview questions that present an intentionally "not quite right" case study [00:25:44].
*   **Self-Motivation** <a class="yt-timestamp" data-t="00:25:34">[00:25:34]</a>: The drive to delve deeper and solve problems without being explicitly told to do so.
*   **Handling Ambiguity and Being Wrong** <a class="yt-timestamp" data-t="00:27:40">[00:27:40]</a>: During case study interviews, Lax observes how candidates react to being told their assumptions are incorrect or how they pivot with new information. The ability to make a decision or offer a point of view without perfect information is also valued [00:28:12].

Jessica Lax's own non-traditional background (starting in investment banking, founding a startup, and becoming self-taught in SQL and Python out of necessity at DoorDash) informs her hiring strategy [00:29:03]. She values hiring individuals with diverse technical skills (e.g., PhDs in statistics, machine learning experts) who can complement her business-impact-driven pragmatic approach [00:30:51]. This diverse approach also includes seeking individuals with experience at different company sizes – from startups (for hustle and grit) to larger companies (for foresight on scaling problems) [01:08:04].

## [[effective_metrics_and_goal_setting_for_data_teams | Effective Metrics and Goal Setting]]
Lax highlights key lessons learned from past "bad metrics":

*   **Short-Term Proxies for Long-Term Outcomes** <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a>: Find measurable short-term metrics that reliably drive desired long-term outputs. For example, retention is a difficult short-term goal, so focus on the inputs that drive retention and test them through experimentation [00:45:02].
*   **Keep Metrics Simple** <a class="yt-timestamp" data-t="00:45:33">[00:45:33]</a>: Avoid complex, composite metrics with coefficients that nobody understands. Even if a simpler metric isn't "perfect," its understandability and intuitive nature make it far more effective in driving outcomes across the company [00:45:50].
    *   **Example**: Instead of a complex "Merchant Health Score," DoorDash now focuses on simpler, actionable inputs like the percentage of new merchants receiving an order within seven days, photo coverage, and accurate open hours [00:50:56].
*   **Common Currency Across Metrics** <a class="yt-timestamp" data-t="00:46:38">[00:46:38]</a>: Quantify the impact of different levers (e.g., price, delivery times, Dasher mobilization, new restaurant sign-ups) in terms of a common currency, such as Gross Order Value (GOV) or volume [00:48:28]. This enables informed trade-off decisions across different teams (e.g., marketing vs. logistics) and quicker strategic choices [00:47:07].
*   **Focus on Edge Cases and Fail States** <a class="yt-timestamp" data-t="00:55:29">[00:55:29]</a>: While averages are important, actively identify and set concrete goals around eliminating "disaster deliveries" or "never delivered" orders. These rare but costly experiences lead to high churn and significant expenses, and their impact is often missed when only looking at average metrics [00:56:02]. Sometimes, data might not even capture these issues (e.g., login errors mean users don't even enter the system) [00:59:26].

## [[running_a_remote_and_distributed_team_effectively | Managing a Global Data Organization]]
When managing a global data organization with teams across different countries, Lax notes that:

*   **Similarities Outweigh Differences** <a class="yt-timestamp" data-t="01:00:37">[01:00:37]</a>: Despite different currencies, languages, and regulations (e.g., EU vs. non-EU countries), the fundamental problems and the nature of data scientists are surprisingly similar [01:00:51].
*   **Leveraging Past Experience** <a class="yt-timestamp" data-t="01:01:33">[01:01:33]</a>: Problems encountered in one market (e.g., the US) often have analogous situations in new regions, allowing for more informed instincts on potential solutions [01:01:40]. New, unexpected challenges are seen as opportunities to learn and stay agile [01:02:04].

## Promoting Extreme Ownership and Adaptability
A core cultural tenet at DoorDash, instilled by its founders, is "extreme ownership" over outcomes <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>. This means team members are expected to do whatever is necessary to solve a problem, regardless of their defined role or job description [00:34:04].

*   **Beyond Job Descriptions** <a class="yt-timestamp" data-t="00:41:35">[00:41:35]</a>: A data scientist's goal is to understand what's happening and solve the problem, even if it means calling customers, performing qualitative research, or engaging in product management or engineering tasks [00:41:40].
*   **Encouraged and Expected** <a class="yt-timestamp" data-t="00:41:54">[00:41:54]</a>: This cross-functional engagement is not only allowed but actively encouraged, fostering an environment where individuals can gain diverse experiences. This also contributes to talent movement between different departments (e.g., analytics to product, ops, or finance) [00:43:51].

## The Role of AI in Data Teams
Jessica Lax is enthusiastic about using AI to enhance data team productivity and empower non-technical users. DoorDash uses "Ask Data AI" (an internal chatbot) to help non-technical users write and edit SQL queries, reducing the burden on the analytics team and enabling more self-service data exploration [01:04:05].

## Conclusion
Building and scaling a successful data organization involves strategic choices in structure, culture, and metrics. Jessica Lax's experience at DoorDash underscores the benefits of a centralized data team that operates as strategic business partners, driven by curiosity, ownership, and a focus on impactful, yet simple, metrics. This approach, combined with a commitment to continuous learning and cross-functional collaboration, enables the data team to be a powerful engine for business growth and innovation.