---
title: The role and treatment of engineers in organizations
videoId: Z9ftpRhRiJE
---

From: [[lennyspodcast]] <br/> 

Engineers are often treated like children within organizations, being sheltered from critical problems and responsibilities [00:00:00]. This approach, while sometimes intended to protect them, can hinder their growth and ability to thrive as adults [00:00:05].

## Shifting Dynamics in the Engineering Landscape

Historically, especially during the "zero interest rate era" (ZIRP), the market for engineers was characterized by rapid growth and high demand [00:04:19]. This led to a significant focus on hiring, with engineering managers spending half or more of their time on recruitment, sometimes conducting six back-to-back interviews in a day [00:05:06]. This high demand meant engineers held significant leverage within companies [00:06:29].

However, the current market is very different [00:04:22]. The shift has led to:
*   **Reduced Hiring Focus** Engineering managers now conduct far fewer interviews, sometimes as few as two a month or even zero [00:05:27].
*   **New Competencies Required** Top-performing engineering directors, previously valued primarily for their hiring prowess, now need to demonstrate skills in leading teams, delving into details, and understanding appropriate team sizing and allocation [00:05:37].
*   **Team Restructuring** Unlike the growth-focused ZIRP era, teams are now disappearing, getting cut down, or being consolidated [00:06:17].

This transformation means that engineers' historical leverage over companies has changed significantly [00:06:36].

## Treating Engineers as Peers and Leaders

The current market presents an opportunity to redefine the [[role_of_engineers_in_the_future | role of engineers]] within organizations, moving away from coddling and towards treating them as peers ready for senior leadership [00:00:20].
*   **Accountability for Growth** In the past, middle management often "coddled" engineers to ensure retention, which was a key performance indicator [00:07:40]. This was detrimental to engineers and overall organizational efficiency [00:07:50]. The new environment allows for greater accountability, enabling engineers to be placed in senior roles and pursue career paths they've long sought, but which were previously limited by the need to retain talent at all costs [00:08:00].
*   **Solving Hard Problems** Engineers can now be given genuinely challenging problems and be held accountable for their solutions [00:08:00]. This allows them to grow and take on more significant responsibilities [00:07:12].

## Engineering Strategy and Accountability

A common issue across many functions, including engineering, is the lack of a clearly written strategy [00:16:51]. While a strategy always exists implicitly, documenting it allows for improvement, debugging, and consistent application across the organization [00:18:22].

Good engineering strategy is often "boring" but highly effective [00:19:07]. Examples include:
*   **Standardized Tooling** Using only existing tools and programming languages prevents engineers from expending energy on building different tooling or experimenting with new technologies [00:19:20]. This focuses effort on building innovative features for users, as seen with Stripe's Ruby monolith policy [00:23:40].
*   **Infrastructure Decisions** A strategy to run everything in proprietary data centers, as Uber did, allowed for rapid global expansion into geopolitically constrained areas without relying on cloud providers [00:22:07].

Such strategies, though sometimes unpopular with engineers, dictate how limited capacities and capabilities are invested in problems the company values [00:24:00]. The core of good strategy lies in understanding and addressing constraints [00:24:28].

To improve [[engineering_leadership_and_management_strategies | engineering leadership and management strategies]] and overall strategy, recommended resources include:
*   *Good Strategy Bad Strategy* by Richard Rumelt [00:21:35]
*   *The Crux* by Richard Rumelt [00:21:40]
*   *Thinking in Systems* by Donatella Meadows (relevant for [[systems_thinking_and_its_application_in_engineering | systems thinking]]) [00:25:48]
*   *Technology Strategy Patterns* by Evan Hitt [01:05:59]
*   *The Value Flywheel Effect* by Anderson, McCon, and O'Connell [01:06:07]
*   *The Phoenix Project* by Kimber, Spafford, and Humble [01:06:13]

## Relationships Between Engineering and Product Management

Challenges often arise in [[engineering_and_product_management_integration | engineering and product management integration]] due to:
*   **Misaligned Incentives** Product managers (PMs) might prioritize actions (e.42:11) for their own promotion, while engineering managers (EMs) might resist due to technical debt or team capacity [00:41:44]. These incentives need to be understood and navigated honestly [00:41:50].
*   **Lack of Mutual Understanding** More commonly, EMs and PMs argue without fully understanding each other's needs [00:42:57]. Deeply understanding the "true needs" of each party can often lead to compromise solutions [00:43:27].

To address misaligned incentives, one approach is to tie the performance ratings of EM-PM pairs together, meaning they generally receive the same performance review rating [00:44:06]. This forces them to share accountability for the entire set of constraints and outcomes, not just their functional ones [00:45:15]. This approach can extend to business leadership as well, creating a "trifecta" of shared accountability [00:45:02].

A key point for PMs to understand about EMs is the pressure to provide their teams with "interesting work" [00:47:06]. This invisible constraint can lead to EMs prioritizing technical rewrites or new programming languages, making them seem unreliable to PMs focused on shipping features [00:47:50]. Understanding this underlying stress can foster more honest conversations [00:48:08].

## Measuring Engineering Productivity

Measuring engineering productivity is a growing concern, especially with companies reducing team sizes and venture capitalists pushing for efficiency [00:48:47].

Common approaches include:
*   **Benchmarking Funding** Comparing R&D and engineering spending against industry benchmarks provides a defensible answer to boards but doesn't offer actionable insights for internal organizational improvement [00:49:13].
*   **Talking to Engineers** Engineers often know if their teams are effective and can articulate the reasons for inefficiencies, providing valuable "crumbs" for leaders to investigate [00:50:31].
*   **Aligning with Business Goals** Engineering evaluation should be tied directly to product and business goals, demonstrating accountability for customer support rather than just novel system building [00:51:30].
*   **Showcasing Roadmap Impact** Regularly presenting a roadmap of meaningful, high-impact achievements from the last six months helps demonstrate productivity to stakeholders [00:52:03].

While metrics like Sprint points are often "totally fake" [00:54:06], and complex metrics like Dora metrics (lead time, incident remediation time, failure rate) are great for diagnosis, they are not perfect for overall performance evaluation [00:53:30]. The key is to:
*   **Measure imperfectly** Don't avoid measuring because no single metric is perfect [00:54:41].
*   **Educate Stakeholders** Use imperfect metrics as an opportunity to educate those consuming them about the nuances and underlying reality of the data [00:54:59].

## Engineers and Company Values

Company values should be:
1.  **Honest** They must reflect what the company *actually* does, not just what it aspires to be [00:57:07]. A value like "users first" is only effective if decisions consistently prioritize users [00:56:58].
2.  **Applicable** Values should be usable in daily work and guide decision-making [00:57:33]. For example, a value around "optimizing globally" (for the organization) versus "optimizing for your team" (which can be a natural tendency) provides clear guidance [00:57:44].
3.  **Reversible** A good value should imply an opposite that a company could realistically choose, even if it's undesirable [00:59:01]. Vague "identity values" like "we build good software" or "we solve customer problems that matter" are not useful because no company would claim the opposite [00:59:05]. Values should also serve as a hiring filter, clearly delineating who would or would not fit the company culture [01:01:06].

## Lessons from Failure: The Dig Rewrite

The story of Dig's version 4 rewrite offers profound lessons in [[lessons_from_failure_in_engineering_projects | engineering projects]].
*   **The Rewrite Trap** Dig faced pressure to add social functionality to compete with emerging social networks like Twitter and Facebook [01:03:12]. The decision was made to undertake a complete rewrite, a decision that "never works out for anyone" [01:03:51].
*   **Launch Disaster** The new system, launched around 2012, was deeply unstable. Upon deployment, servers crashed repeatedly, requiring a complete re-imaging and over a month to regain full functionality, even with an emergency caching system built from scratch [01:04:41]. For much of that month, basic user functionality was broken, and the site was largely read-only [01:08:43].
*   **A "Silly" Bug** The core bug causing system crashes every 12 hours was an "incredibly simple issue" related to how Python initiates variables used as default parameters, overlooked by a developer new to Python and missed in code review [01:05:51].
*   **Learning from Crisis** Despite the business eventually failing, the experience was a "tremendous amount" of learning [01:07:04]. It shaped the engineering team's resilience and provided an opportunity for individuals, like Will Larson, to take on senior leadership roles out of necessity, which would not have been available otherwise [01:07:16]. These challenging moments, especially when overcome with a respected team, can be transformative [01:08:16].

The challenges at Dig were exacerbated by an earlier SEO change that drastically reduced traffic and monetization, putting the company "on fire" even before the ill-fated launch [01:10:13].