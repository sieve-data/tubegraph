---
title: Centralized vs embedded analytics teams
videoId: D4PDb_C8Dww
---

From: [[lennyspodcast]] <br/> 

Jessica Lax, Vice President of Analytics and Data Science at DoorDash, discusses her perspective on structuring data teams, advocating for a centralized model over an embedded one. She emphasizes that analytics should be a business impact-driving function, not merely a service function [00:00:05].

## The Centralized Model at DoorDash

Lax believes that analytics should have a "seat at the table" alongside engineering, product, and business operations [00:05:04]. Her "contrarian perspective" is that a centralized analytics organization, or a "Center of Excellence," is superior to embedding analytics professionals directly within business units [00:06:00].

### Defining the Models
The distinction between centralized and embedded models primarily concerns **reporting lines** [00:06:45]. In a centralized model, like DoorDash's, analytics teams report up through a central analytics organization (e.g., to Jessica Lax), rather than reporting into a specific marketing or product department [00:07:01].

However, even within DoorDash's centralized structure, the team is divided into "pods" that align perfectly with product, engineering, operations, and marketing structures [00:08:22]. This means the analytics team members are *de facto* embedded with their partner teams [00:08:38], sharing the same goals and aligning incentives [00:08:58]. This approach avoids a "siloed data team" or a "service org" mentality, where the analytics team only responds to requests [00:09:29]. Instead, they act as business partners and thought partners, bringing data-driven insights, deep dives, and opportunities to the table to earn their seat [00:09:50].

### Benefits of a Centralized Analytics Organization
Lax highlights several key advantages of a centralized analytics model:

*   **Consistent and High Talent Bar**
    *   A centralized team allows for a uniform standard for evaluating talent, ensuring consistency in technical and soft skills [00:11:06]. This leads to more consistent and higher-quality hires [00:11:36].
*   **Growth Opportunities and Talent Retention**
    *   Being part of a larger, central organization provides more diverse [[balancing_micromanagement_and_team_autonomy | growth opportunities]] for individuals [00:11:41]. Data professionals aren't siloed within one business unit, enabling them to explore new problem areas (e.g., moving from marketing to merchant analytics) or pursue management roles within the broader analytics function [00:11:56]. This helps keep talent engaged and improves retention [00:12:05].
*   **Consistency of Methodologies and Metrics**
    *   A centralized approach ensures that metrics (e.g., "sales") are defined and used consistently across the company [00:12:48]. This prevents different teams from having their own definitions or from "recreating the wheel" on similar models (e.g., churn prediction models), fostering shared learning and improved methodologies [00:12:51].
*   **Improved Scaling and Foresight**
    *   Seeing similar problems across different teams allows the centralized organization to identify systemic issues, automate processes, or proactively improve systems, helping the business "see around corners" as it scales [00:13:24].
*   **Stronger Team Culture and Brand**
    *   A central team fosters a unique culture of learning and sharing, where members can collaborate, peer-review work, and find like-minded "data nerds" [00:13:46]. This collective identity is especially beneficial for recruiting top talent externally and building internal pride [00:13:46].

## Cultivating Proactivity and Ownership
Lax stresses the importance of fostering a proactive analytics team that not only answers questions but also identifies opportunities and informs what to build [00:15:16].

### Balancing Reactive and Proactive Work
It's crucial to intentionally set aside time for exploratory work and deep dives, as there are always more immediate questions than hours in the day [00:15:50]. DoorDash implements:
*   **Goal Setting:** Teams are given specific goals related to finding insights through self-directed work [00:16:06].
*   **Hackathons:** Carving out dedicated days for the team to investigate interesting problems and uncover opportunities [00:16:49]. For instance, a hackathon deep dive into referral channels revealed significant fraudulent behavior, leading to recommendations for better fraud checks and referral caps that improved the efficiency of the marketing channel [00:17:35].
*   **Communicating Trade-offs:** To avoid continuously saying "no" to ad-hoc requests, analytics leaders must establish clear operating models and consistently communicate trade-offs to business partners. By showing that taking on a new task means dropping another, partners can help prioritize [00:21:26].

### Extreme Ownership
A core cultural tenet at DoorDash, instilled from the top, is [[balancing_micromanagement_and_team_autonomy | extreme ownership]] of outcomes [00:41:17]. This means analytics professionals are expected to do whatever is necessary to solve a problem, even if it falls outside their typical job description [00:41:20]. For example, data scientists might pick up the phone and call customers to gather qualitative insights when quantitative data alone isn't sufficient to understand why a new feature isn't working as expected [00:42:10]. This willingness to engage in "product management work" or "engineering work" makes the job interesting and helps team members explore other career paths within the company [00:43:37].

## Metrics and Incentives
Lax emphasizes the critical role of defining the right metrics to align incentives and drive desired outcomes [00:44:22].

### Key Learnings for Metrics:
*   **Short-Term Proxies for Long-Term Outcomes:** Instead of directly setting goals on long-term outputs like retention, which are hard to move in the short term, identify measurable short-term inputs that reliably drive the desired long-term results [00:44:51]. Experimentation confirms these linkages [00:45:24].
*   **Simplicity Over Perfection:** Avoid complex, composite metrics with coefficients that nobody truly understands [00:45:38]. A simpler metric, even if not "perfect," is far more effective if people can intuitively grasp it and discuss it across the company [00:46:07].
*   **Common Currency:** Quantify the impact of different business levers (e.g., lowering price, improving delivery times, signing a new restaurant) in terms of a common currency, such as Gross Order Value (GOV) or volume [00:46:40]. This enables clear trade-off decisions and allows teams to strategically allocate resources to the most impactful initiatives [00:47:07].
*   **Focus on Edge Cases and Fail States:** While averages are important, actively set goals and create metrics around critical edge cases and "fail states" that lead to terrible customer experiences (e.g., "never delivered" orders) [00:55:29]. Even if rare, these issues are costly, lead to customer churn (which is hard to observe in average data), and can be significant drivers of lost business [00:58:21].

## Hiring Philosophy and Global Teams
Lax believes in hiring for curiosity and a problem-solving mindset, and she sees significant value in diverse backgrounds.

### What to Look for in Hires
Beyond technical skills, which are "table stakes," Lax prioritizes:
*   **Curiosity and Self-Motivation:** The ability and drive to "pull on threads" and proactively investigate anomalies or areas of interest, rather than just answering the immediate question [00:24:51]. This can be tested by presenting cases with subtle errors or asking for examples of past self-directed investigations [00:25:44].
*   **Problem-Solving Under Ambiguity:** Interview cases are designed to assess how candidates break down problems, handle imperfect information, and react to being challenged or told they are wrong [00:27:16]. The ability to make a decision and have a point of view without complete information is highly valued [00:28:24].
*   **Non-Traditional Backgrounds:** Lax herself comes from a non-traditional background (investment banking, social gifting startup, art portfolio) and became a data scientist out of necessity [00:29:00]. This experience has made her open to hiring individuals from diverse fields (e.g., engineering, operations, marketing, finance), who bring different expertise and foster a unique learning environment within the team [01:06:03]. This mix of technical depth (e.g., PhDs in statistics) and business acumen drives business impact [00:30:31].
*   **Diversity in Company Stage Experience:** Hiring individuals from both startups and larger, more mature companies provides a mix of "hustle and grit" with foresight into scaling challenges [01:08:04].

### Managing a Global Data Organization
While currencies, languages, and regulations add complexity to global operations, Lax finds more similarities than differences in managing data teams across countries [01:00:37]. Problems often reoccur, allowing for informed instincts, but new challenges keep the work exciting and open to different solutions [01:01:31].

### AI's Role in Productivity
DoorDash is leveraging AI to enhance team productivity, particularly through tools like "Ask Data AI" [01:04:52]. This internal chatbot helps non-technical users write and edit SQL queries, reducing reliance on the analytics team and freeing up their bandwidth [01:04:05].

> "Sleep can solve lots of problems" <a class="yt-timestamp" data-t="01:12:45">[01:12:45]</a>
— Jessica Lax, citing John Steinbeck