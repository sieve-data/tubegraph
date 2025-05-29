---
title: Strategies for building products at large companies
videoId: qbZQjprTnrU
---

From: [[lennyspodcast]] <br/> 

Jeff Weinstein, a product leader at Stripe for over six years, has played a pivotal role in scaling Stripe's payment infrastructure and leading various 0-to-1 bets, including Stripe Atlas. His expertise lies in consistently building successful and beloved products within large organizations <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>, drawing lessons from his unique educational background and practical experience <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>.

## Core Philosophy: Go-Go-Go and Long-Term Compounding

Weinstein's core philosophy combines an "optimistic go-go-go" approach with a "long-term compounding, more strategic mindset" <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. He believes in injecting energy to take immediate action, striving to make things "due tomorrow" into "due today" <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>. However, he emphasizes balancing this urgency with a long-term view, recognizing that some large-scale initiatives require layers of infrastructure and partnerships that cannot be solved quickly <a class="yt-timestamp" data-t="11:40:00">[11:40:00]</a>. This means investing in foundational capabilities that will "never regret spending time in," such as improving API latency or reliability <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>.

At Stripe, this mixed approach was crucial when expanding global payment methods. Initially, a "go-go-go" attitude wasn't working, leading to slow progress. The team had to deliberately slow down to build internal platforms and establish payment methods in different regions, leading to a non-linear acceleration from 10 to over 100 accepted payment methods <a class="yt-timestamp" data-t="14:05:00">[14:05:00]</a>.

## Customer-Centric Product Development

A cornerstone of Weinstein's strategy is an intense focus on the customer, aiming to solve "burning problems" that compel people to actively seek solutions <a class="yt-timestamp" data-t="19:18:00">[19:18:00]</a>.

### Talking to Customers Effectively

Weinstein practices [[breaking_into_product_management | direct, unfiltered customer interaction]] to uncover core problems <a class="yt-timestamp" data-t="24:43:00">[24:43:00]</a>:
*   **Active Listening (Silence)**: Instead of pitching a product, he encourages sitting in silence, prompting customers with open-ended questions like "what's in your email?" or "what grinded your gears last week?" to allow them to reveal their most pressing issues <a class="yt-timestamp" data-t="21:17:00">[21:17:17]</a>. This approach builds trust and helps identify "burning needs" <a class="yt-timestamp" data-t="23:15:00">[23:15:00]</a>.
*   **Speed of Response**: When a customer expresses a problem, especially on public platforms like Twitter, it's an "unbelievable gift" <a class="yt-timestamp" data-t="30:25:00">[30:25:00]</a>. He prioritizes responding quickly, even if it's just to acknowledge their message, creating a "secret portal" between the customer and the company <a class="yt-timestamp" data-t="30:41:00">[30:41:00]</a>.
*   **Converting Detractors**: Instead of merely solving a problem for an unhappy customer, the goal is to turn them into a "promoter" <a class="yt-timestamp" data-t="31:33:00">[31:33:00]</a>. An example from Stripe Atlas involved converting a frustrated founder (due to a legal document error) into a consistent product feedback provider <a class="yt-timestamp" data-t="31:57:00">[31:57:00]</a>.
*   **Open Access**: He frequently shares his email and is open to calls, breaking down the perceived "wall" between product managers and customers <a class="yt-timestamp" data-t="24:26:00">[24:26:00]</a>.

### Filtering Customer Feedback

To manage the volume of feedback, especially for widely adopted products like Stripe Atlas, Weinstein employs strategies to focus on the most valuable input <a class="yt-timestamp" data-t="33:36:00">[33:36:00]</a>:
*   **Self-Selection**: Customers who are willing to provide detailed screenshots or videos, or write three to five bullet points about an issue, are often the ones who want to "go deep" and become "product friends for life" <a class="yt-timestamp" data-t="34:37:00">[34:37:00]</a>.
*   **Paying Customers Only**: He advises discounting feedback from friends or non-paying users, as they may not represent the "target customer" who is willing to "exchange money for solving their problems" <a class="yt-timestamp" data-t="38:03:00">[38:03:00]</a>. The act of paying serves as a "forcing function" that reveals true need and value perception <a class="yt-timestamp" data-t="39:27:00">[39:27:00]</a>.
*   **Practice Paying**: He even encourages founders to "practice paying" by sending him a $1 invoice, cementing the physical act of exchanging value <a class="yt-timestamp" data-t="43:54:00">[43:54:00]</a>.

## Leveraging Metrics for Product Success

Weinstein views metrics as essential for [[executing_strategy_effectively_in_product_management | achieving product-market fit]] and making informed decisions <a class="yt-timestamp" data-t="46:00:00">[46:00:00]</a>.

### Defining Impactful Metrics

*   **Quantitative and Qualitative Alignment**: Metrics and customer feedback (tweets) are seen as "deep siblings and equals" <a class="yt-timestamp" data-t="46:25:00">[46:25:00]</a>.
*   **Customer-Centric Value**: The best metrics are "numerical representations of the value we're providing for the customer," measured from *their* perspective, not just internal company activities like logins <a class="yt-timestamp" data-t="46:50:00">[46:50:00]</a>.
*   **Driving Focus and Tradeoffs**: A small number of well-chosen metrics can align a large group of people towards a common goal, preventing endless debates and driving progress <a class="yt-timestamp" data-t="47:51:00">[47:51:00]</a>.
*   **Stripe Atlas Example**: For Stripe Atlas, the key metric became "companies with zero support tickets" through the entire incorporation process (including a two-week buffer post-completion) <a class="yt-timestamp" data-t="50:28:00">[50:28:00]</a>. This metric directly correlated with market share growth, increasing from 15% to 85% <a class="yt-timestamp" data-t="51:48:00">[51:48:00]</a>. This metric was motivating for engineers because it directly linked their work to customer happiness <a class="yt-timestamp" data-t="53:37:00">[53:37:00]</a>.

### The "Users Having a Bad Day" Metric

A highly recommended metric, especially for large-scale businesses, is "users having a bad day" <a class="yt-timestamp" data-t="01:01:05">[01:01:05]</a>. This involves emitting a log line whenever a user encounters a problem (e.g., 404 error, delayed payout, payment declines) <a class="yt-timestamp" data-t="01:01:09">[01:01:09]</a>. This creates an "eye-opening" bar chart of "bad day reasons," allowing teams to see frequencies and make informed decisions on what to prioritize <a class="yt-timestamp" data-t="01:01:40">[01:01:40]</a>. It provides a "background noise counting system for where there are problems" <a class="yt-timestamp" data-t="01:02:47">[01:02:47]</a>.

### Metrics Hygiene and Culture

*   **Motivating Titles**: Metrics should have titles that "make you feel something" and clearly communicate their purpose (e.g., "companies with zero support") <a class="yt-timestamp" data-t="01:05:28">[01:05:28]</a>.
*   **Good Hygiene**: Consistency in significant digits, axis alignment, and discoverability (e.g., `go/metrics` at Stripe) increases the frequency with which teams engage with dashboards <a class="yt-timestamp" data-t="01:06:51">[01:06:51]</a>.
*   **Trust and Ritual**: Consistently viewing and discussing metrics in a common, trusted location (like a dedicated dashboard URL) fosters a data-driven "decision-making culture" and helps teams remain customer-obsessed <a class="yt-timestamp" data-t="01:09:40">[01:09:40]</a>. This also forces teams to narrow down to a small number of essential metrics <a class="yt-timestamp" data-t="01:11:08">[01:11:08]</a>.

## Fostering Product Craft and Quality Internally

While product-market fit is paramount, maintaining craft and quality is crucial for sustained success.

### The Importance of Product-Market Fit First

Weinstein emphasizes that "craft is kind of a dessert that you get after the meal" of solving a real problem that people desperately need <a class="yt-timestamp" data-t="01:09:05">[01:09:05]</a>. Without a burning need, no amount of beauty or delight will make a product successful <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>. His own experience with a startup that built software people "liked but wasn't solving a burning enough problem" taught him this crucial lesson <a class="yt-timestamp" data-t="01:36:18">[01:36:18]</a>.

### [[strategies_for_leading_and_scaling_design_teams | Stripe Study Groups]]

To combat the natural "entropy" that causes products to degrade over time, and to instill empathy for the customer experience, Weinstein started "Stripe Study Groups" <a class="yt-timestamp" data-t="01:13:51">[01:13:51]</a>.
*   **Structure**: Random groups of 4-8 employees (any role) sign up <a class="yt-timestamp" data-t="01:17:10">[01:17:10]</a>. They pretend to be a fictional company with a specific goal, like "dolphin aquarium Industries" <a class="yt-timestamp" data-t="01:17:59">[01:17:59]</a>.
*   **Rules**:
    1.  **"You do not work at Stripe"**: Participants must not use any internal Stripe knowledge or lingo, forcing them to experience the product as an external user <a class="yt-timestamp" data-t="01:18:49">[01:18:49]</a>.
    2.  **"We're not here to solve any problems"**: The focus is purely on practicing empathy and experiencing the product, not critiquing, solutioning, or filing bugs during the session <a class="yt-timestamp" data-t="01:19:36">[01:19:36]</a>.
*   **Impact**: Over 250 people participated in 25+ sessions in early 2024, leading to "deeply eye-opening" realizations about product usability <a class="yt-timestamp" data-t="01:20:01">[01:20:01]</a>. The sessions are "fun" and "non-punitive," making participants more receptive to insights <a class="yt-timestamp" data-t="01:21:42">[01:21:42]</a>.
*   **Outputs**: While not mandated, observations from study groups often lead to high-signal bugs being filed and prioritized through existing formal processes <a class="yt-timestamp" data-t="01:31:54">[01:31:54]</a>. Seeing teammates struggle to use a product is a strong motivator for teams to act <a class="yt-timestamp" data-t="01:32:51">[01:32:51]</a>.

## [[innovating_within_large_organizations | Innovating Within Large Organizations]]

Weinstein has a proven track record of getting new initiatives off the ground within a large, complex company like Stripe.

### Overcoming Internal Hurdles

*   **"Not Having Things Be Your Idea"**: Frame initiatives by deep customer stories and evidence, rather than personal conviction <a class="yt-timestamp" data-t="02:04:10">[02:04:10]</a>.
*   **Storyboarding Unconstrained Visions**: Visually depict the "unconstrained perfect solution" with simple tools like a Sharpie, without getting bogged down by initial limitations <a class="yt-timestamp" data-t="02:05:02">[02:05:02]</a>.
*   **Show Tangible Forward Progress**: Focus on achieving small, quick wins ("proof of existence") to build momentum and trust. For example, demonstrating that a single piece of paper could be sent for an 83b election proved the possibility of automating the entire process <a class="yt-timestamp" data-t="02:05:51">[02:05:51]</a>.
*   **Less Permission, More Action**: Build momentum by taking smaller steps without excessive permission, and once results are shown, trust naturally follows <a class="yt-timestamp" data-t="02:07:09">[02:07:09]</a>.
*   **Cultural Buy-in**: When progress is transparently shown through metrics, internal stakeholders transition from skepticism to actively "rooting for" the initiative <a class="yt-timestamp" data-t="02:07:50">[02:07:50]</a>.

### The Stripe Atlas Example

Stripe Atlas, which allows companies to incorporate in the US in a single day, was born from the "burning problem" of international entrepreneurs needing to fly to the US just to set up a company <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>. It simplifies complex administrative tasks like securing a tax ID, handling equity paperwork, and filing 83b elections <a class="yt-timestamp" data-t="01:44:09">[01:44:09]</a>.

*   **Automating Complexity**: The Atlas team of 10 people focuses exclusively on work that can be automated, avoiding situations that would require manual competition <a class="yt-timestamp" data-t="01:51:12">[01:51:12]</a>. This includes integrating deeply with governments and banking partners, using third-party services for physical tasks like mail, and even having "robots waiting on phones" for hold times <a class="yt-timestamp" data-t="01:52:50">[01:52:50]</a>.
*   **Impact**: One in six new Delaware Corporations are started on Stripe Atlas <a class="yt-timestamp" data-t="01:54:48">[01:54:48]</a>. Companies started through Atlas generate $5 billion in annual revenue <a class="yt-timestamp" data-t="01:50:09">[01:50:09]</a>, with new cohorts achieving revenue faster <a class="yt-timestamp" data-t="01:49:21">[01:49:21]</a>. It has also enabled more solo founders and cross-border founding teams <a class="yt-timestamp" data-t="01:55:21">[01:55:21]</a>.
*   **Competitive Dynamics**: Despite competitors like AngelList initially offering similar services, Stripe's long-term compounding approach, focus on efficiency, and willingness to collaborate (sharing knowledge on legal constructs) led to AngelList eventually directing their users to Atlas <a class="yt-timestamp" data-t="02:11:08">[02:11:08]</a>. This demonstrated that customer focus and specialization can lead to beneficial partnerships even among competitors <a class="yt-timestamp" data-t="02:14:12">[02:14:12]</a>.

## Economic Viability and Long-Term Investment

For any product, especially within a large company, it is "extremely important" to communicate its "economically viable" path <a class="yt-timestamp" data-t="02:09:20">[02:09:20]</a>. Whether it's a customer acquisition tool, a margin generator, or an ecosystem builder, the metrics must clearly demonstrate its economic contribution <a class="yt-timestamp" data-t="02:09:33">[02:09:33]</a>. This financial clarity builds confidence for long-term investment, ensuring the product's sustainability and continued growth <a class="yt-timestamp" data-t="02:10:02">[02:10:02]</a>.