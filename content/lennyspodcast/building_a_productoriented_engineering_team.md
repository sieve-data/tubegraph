---
title: Building a productoriented engineering team
videoId: F0_IKKY3HCk
---

From: [[lennyspodcast]] <br/> 

At Stripe, [[building_and_evolving_a_software_product | product development]] is fundamentally about co-creating solutions with early users <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This approach fosters a highly product-oriented engineering team <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>.

## Core Philosophy

Stripe considers itself a business full of product-minded builders dedicated to simplifying business operations on the internet <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>. This mission attracts individuals who want to take significant agency, deeply understand user problems, and develop their own solutions <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>.

### Engineers as Product Managers

Historically, Stripe's early team was primarily composed of engineers who were "extremely product minded" <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>. Every early team member essentially acted as a Product Manager (PM) <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>. For developer-focused products, the most effective PMs are often technical, many being former or current engineers <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.

This means that every engineer building a product at Stripe possesses and exercises many attributes typically found in PMs at other companies <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.

## Key Practices for Product Orientation

### 1. User Co-creation
The core of Stripe's [[building_and_evolving_a_software_product | product development]] involves finding the right set of early users to co-create products with <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

A prime example is Stripe Billing <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>:
*   Stripe identified existing users like Figma and Slack who had subscription business models <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
*   These companies were "pushing the boundaries" of what was possible <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>.
*   Stripe co-created the product with them through shared Slack channels and regular product demonstrations to gather feedback <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.
*   Only after this initial "alpha group" was extremely satisfied was the product considered ready for a broader audience <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>.

This approach ensures deep personal insights from users are brought into the [[building_and_evolving_a_software_product | product development]] loop <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.

### 2. Operating Principles
Stripe's operating principles, distilled from the behaviors of its most effective employees, guide its product-oriented culture <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.
*   **Users First:** This principle places users at the center of all decisions, emphasizing deep personal relationships with them <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.
*   **Be Meticulous in Your Craft:** This value focuses on sweating the details where it truly matters to users <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. An example is linking API error messages directly to relevant documentation, which significantly helps developers <a class="yt-timestamp" data-t="02:50:00">[02:50:50]</a>.

### 3. Friction Logging
Friction logging is a systematic practice used across product teams to identify areas for meticulous investment <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.
*   **Process:** Individuals adopt the persona of a specific user (e.g., an engineer at Atlassian integrating Stripe Billing) and meticulously document their experience using the product, noting every point of friction <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.
*   **Regular Practice:** Many teams, including senior leaders, regularly perform friction logging to maintain a cohesive user experience across parallel development efforts <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.
*   **Impact:** This helps teams focus their efforts on high-impact areas, like optimizing checkout flows, which has led to significant revenue increases for users <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>.

### 4. UX Reviews ("Walk the Store")
UX reviews are conducted to ensure product quality and a shared understanding of user experience <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.
*   **Approach:** Teams, along with cross-functional partners (e.g., support groups, executives), walk through product flows together, modeling a specific user's experience <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.
*   **Benefits:** This collaborative process helps establish a common standard for craftsmanship and reinforces how products should interoperate at scale <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.
*   **Company-wide:** Occasionally, these walkthroughs are done with the entire company during weekly meetings, fostering a shared language and understanding <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.

### 5. Engineer Occasions
Engineers at Stripe, especially managers, regularly engage in "Engineer Occasions" <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.
*   **Practice:** Clearing several days, individuals join a team to pick up a small feature, taking it from start to finish into production <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>.
*   **Purpose:** This immersion helps them understand the real experience of using developer tools, build infrastructure, code review processes, and documentation quality <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.
*   **Friction Logging during:** It is crucial to maintain a friction log during this process to document findings and aid future prioritization <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>.
*   **Managerial Expectation:** Engineering managers are encouraged to do an Engineer Occasion in their first quarter to six months, and then annually thereafter <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.

### 6. Prioritizing Quality and Reliability
Stripe's products are business-critical, requiring extreme reliability and availability <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.
*   **Automated Testing:** Stripe heavily relies on automated testing, with comprehensive test suites run on every change before it goes to production <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>. Manual testers are not used due to the vast array of API endpoints and configurations <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.
*   **Continuous Deployment:** Changes automatically deploy to production within approximately 45 minutes of being submitted <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>. This enables a rapid feedback loop with users, allowing for problem resolution within a day <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.
*   **Incident Response:** Stripe has robust tools and processes for declaring and resolving incidents quickly. After incidents, they rigorously review what went wrong to prevent similar issues in the future, prioritizing these fixes above other roadmap work <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>.

## Hiring for Product Orientation

Stripe's hiring process is deeply personal and patient <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.
*   **Clear Mission:** Candidates are clearly informed about Stripe's mission to increase the GDP of the internet, ensuring they are excited about the work <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.
*   **Patience:** Especially for critical leadership roles, Stripe is willing to take its time, meeting many candidates and nurturing relationships even if a person isn't immediately available <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>.
*   **Personal Connections:** Hiring managers spend significant time understanding candidates' motivations and how they can find personal fulfillment and opportunity at Stripe <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>.
*   **Learning Opportunities:** Stripe emphasizes the immense learning opportunities within the company, attracting individuals who want to stretch into new areas and deeply understand complex financial systems <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.
*   **Structured Interview Loops:** All roles go through consistent, structured hiring loops with questions that simulate real-world work <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>. For engineers, this includes pair-programming exercises where Google is permitted <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>. For PMs, written exercises tackling real problems are common <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.
*   **References:** Stripe places high importance on references, recognizing that they provide thousands of hours of direct experience and often offer the best conviction on a hire <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.

This comprehensive approach ensures that Stripe's engineers are not just technically proficient but also deeply invested in the product and its users.