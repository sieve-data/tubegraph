---
title: Human Psychology and Consumer Behavior
videoId: xkx1tXLAP-o
---

From: [[causalpython]] <br/> 

Understanding human psychology and consumer behavior is paramount in the realm of recommendations and marketing, especially when attempting to drive incremental change rather than merely predicting existing patterns <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. Traditional machine learning models often focus on predictive or associative recommendations, aiming for high accuracy based on correlation <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. However, real-world application, particularly in [[Causality in marketing | marketing]] and e-commerce, reveals that accuracy in predicting user preferences doesn't always translate to a *causal* impact on key business metrics <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

## Shifting Focus: From Prediction to Causation
The core challenge is to understand what truly drives consumer behavior change <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. For instance, recommending a destination a user intended to visit anyway won't create incremental impact <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. The objective shifts from identifying the "most suitable" item to identifying what will "incentivize the customer to change their behavior" <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. This requires thinking in terms of [[Causal inference and decision making | counterfactual outcomes]] – "what would happen if I didn't do that?" <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

## Price Sensitivity and Discounting
A significant driver of behavior in travel, for example, is price <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Discounts, promotions, and coupons can substantially change customer behavior, making them a major strategy for extending a customer base and increasing volumes <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. However, this strategy comes with the need for careful [[Applications of causal models in business and marketing | optimization]] to avoid losses <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. The key is to offer discounts only when it's beneficial and changes the customer's behavior in a positive way, not when they would have booked anyway <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

## The Counterintuitive Nature of Human Psychology
One of the most surprising findings about human psychology in this work is its **inconsistency** <a class="yt-timestamp" data-t="00:32:10">[00:32:10]</a>. What works in one context might not in another:
*   An experiment that performs well on a laptop might show inverse results on a mobile app <a class="yt-timestamp" data-t="00:32:38">[00:32:38]</a>.
*   People from different countries may react differently <a class="yt-timestamp" data-t="00:32:54">[00:32:54]</a>.
*   The same person might react differently half a year later <a class="yt-timestamp" data-t="00:32:58">[00:32:58]</a>.

This highlights that human behavior is "not super consistent, it's really hard to predict" <a class="yt-timestamp" data-t="00:33:08">[00:33:08]</a>, often being counterintuitive or even irrational <a class="yt-timestamp" data-t="00:30:11">[00:30:11]</a>. Customers themselves may not consciously understand why they make certain decisions <a class="yt-timestamp" data-t="00:30:55">[00:30:55]</a>.

### Case Study: Paris Nights Recommendation
An internal project aimed to recommend the optimal number of nights for a Paris stay, based on historical booking distributions (e.g., typically two or three nights) <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>. However, this intuitive solution did not improve bookings or user navigation <a class="yt-timestamp" data-t="00:28:37">[00:28:37]</a>. The reason was a side effect related to price and availability:
*   Recommending three nights displayed a higher, potentially off-putting price <a class="yt-timestamp" data-t="00:29:03">[00:29:03]</a>.
*   Recommending one night, while less "accurate" to the typical stay length, showed a much cheaper price and greater availability, encouraging users to continue exploring <a class="yt-timestamp" data-t="00:29:09">[00:29:09]</a>.

This revealed that "not necessarily the most accurate answer is the right one" when the goal is to induce a desired action from the customer <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>. It illustrates the [[Causality in marketing and decisionmaking | beauty of causality]], where hypotheses are tested against the real world <a class="yt-timestamp" data-t="00:29:48">[00:29:48]</a>.

## The Role of Experimentation
The solution to uncovering these often irrational or inconsistent human behaviors lies in extensive [[Personalized Experimental Design | experimentation]], specifically A/B testing <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Operating in a "data-driven" and "experimentation culture" means almost any change, from UI updates to back fixes and machine learning models, is subjected to A/B tests <a class="yt>00:21:43">[00:21:43]</a>. This continuous experimentation allows teams to:
*   Identify what truly "moves the needle" in terms of business metrics <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   Understand the actual causal effect of interventions <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   Discover patterns in human behavior that are not intuitive <a class="yt-timestamp" data-t="00:31:17">[00:31:17]</a>.

However, online testing is costly, making robust offline evaluation and careful monitoring essential <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. The dynamic nature of pricing and promotions, for instance, requires continuous monitoring against a control group to track how effects evolve over time <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.

## Human and Machine Causal Thinking
The parallels between [[Human and Machine Causal Thinking | human and machine causal thinking]] are evident. Just as machines learn from exposure to data and iterate to optimize goals, humans also exhibit patterns and learn from feedback <a class="yt-timestamp" data-t="00:57:10">[00:57:10]</a>. The example of an infant learning that crying is an "optimal treatment" to gain attention illustrates this optimization of behavior to achieve a desired outcome <a class="yt-timestamp" data-t="00:58:04">[00:58:04]</a>.

## Communication with Business Stakeholders
For technical teams, particularly those working in [[Causality in marketing | causal AI and personalization in eCommerce]], effective communication with business stakeholders is crucial <a class="yt-timestamp" data-t="00:23:59">[00:23:59]</a>. The main lesson is to focus on the **expected impact** of the work rather than just the technical accuracy of an algorithm <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>. A highly accurate model (e.g., recognizing toilets in images) is only valuable if its application genuinely moves the business needle or benefits the customer <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>. This requires close collaboration with product managers to connect models with actual product needs <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.

## Advice for Newcomers
For those starting in [[Causality in marketing | causal inference]] or machine learning:
1.  **Keep it Simple**: Don't be afraid of simple solutions, as they often have a huge impact on customer behavior <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>. Focus on the fundamental things shaping the problem <a class="yt-timestamp" data-t="00:51:56">[00:51:56]</a>.
2.  **Understand the Problem First**: Before picking tools or diving into complex architectures, deeply understand the problem to be solved <a class="yt-timestamp" data-t="00:52:04">[00:52:04]</a>.
3.  **Focus on Impact**: Navigate efforts towards what actually moves the needle and changes outcomes for the business and customers, not just fancy technical solutions <a class="yt-timestamp" data-t="00:53:05">[00:53:05]</a>.
4.  **Embrace Evaluation**: Ensure you evaluate the right metrics, consistently and correlated with what you're trying to solve <a class="yt-timestamp" data-t="00:54:42">[00:54:42]</a>.
5.  **Be Humble and Adaptable**: Recognize that human behavior is inconsistent and hard to predict, so validate assumptions frequently and be ready for changes in the environment <a class="yt-timestamp" data-t="00:33:05">[00:33:05]</a>. The fact that something worked before does not guarantee it will work again <a class="yt-timestamp" data-t="00:33:36">[00:33:36]</a>.