---
title: Challenges of machine learning integration in business
videoId: xkx1tXLAP-o
---

From: [[causalpython]] <br/> 

Integrating machine learning (ML) solutions into business operations presents unique challenges that extend beyond traditional model accuracy. These challenges stem from the dynamic nature of real-world environments, human behavior, and the complexities of causal inference, particularly in areas like personalization and recommendations <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Technical Challenges

### Costly Online Testing
Experimenting with models online, especially in contexts involving discounts or promotions, can be expensive. If not done correctly, it can lead to sub-optimal results <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>, <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>. Booking.com, for example, runs hundreds or even thousands of A/B tests in parallel for every change, from copywriting to back fixes and ML solutions <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

### Alignment of Metrics and Data
A fundamental challenge is ensuring alignment between online and offline metrics and data collection processes <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>. Differences in data sources, timing, and definitions can lead to significant discrepancies between offline model evaluations and real-world performance <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.

### Noisy and Overfitting Data
In reality, data used for [[challenges_in_causal_machine_learning_compared_to_traditional_methods | causal inference]] is often very noisy, prone to overfitting, and affected by seasonality <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. This makes it difficult to build robust models that perform consistently in production <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.

### Model Complexity and Maintenance
While complex models with many features might show strong offline benchmarking, they often lead to deployment and maintenance problems in production <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>. More moving parts mean more risk of drift and inconsistent effects on outcomes <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>.

### Lack of Ground Truth for Causal Effects
For [[benefits_and_challenges_of_causal_machine_learning | causal models]], it's challenging because you never have the "true" outcome of both scenarios (e.g., giving a coupon versus not) for the same person at the same time <a class="yt-timestamp" data-t="00:37:07">[00:37:07]</a>. This makes model evaluation, explainability, monitoring, and benchmarking much harder than with traditional predictive models <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>.

## Business and Strategic Challenges

### Accuracy vs. Causal Impact
A highly accurate recommender system that predicts what a customer would do anyway might not lead to an incremental impact on business metrics. It might only shift traffic or reveal obvious information <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. The goal is to induce a change in behavior, not just predict existing behavior <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Shifting Customer Behavior
The core challenge lies in understanding how to "shift behavior" and introduce a change that makes customers do something different from what they would have done otherwise <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. This involves thinking in terms of [[integration_of_causal_thinking_in_machine_learning | counterfactual outcomes]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### Budget Constraints and Optimization
When dealing with promotions or discounts, businesses operate under fixed budget constraints <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. The challenge is to optimize incremental volumes (new customers, reservations) while controlling incremental costs and adhering to a predefined budget or return on investment threshold <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. This often becomes a complex optimization problem, akin to a Knapsack problem <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

### Dynamic Environment and Evolving Problems
The business environment is highly dynamic, with continuous changes, new constraints, and evolving problems <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. Solutions need to be robust and reusable across different scenarios, not just theoretically optimal for a fixed problem <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.

### Communication with Stakeholders
Technical teams often need to communicate effectively with business stakeholders <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. A key lesson is to focus on the expected impact of the work on product needs and business outcomes, rather than just optimizing algorithm accuracy <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>.

## Human and Behavioral Challenges

### Human Psychology and Irrationality
[[causal_ai_in_business_applications | Causal AI in business applications]] often intersects with human psychology, which is not always rational <a class="yt-timestamp" data-t="00:30:11">[00:30:11]</a>. What makes people change their minds or take desired actions can be counter-intuitive <a class="yt-timestamp" data-t="00:30:25">[00:30:25]</a>. For example, recommending a cheaper, shorter stay in Paris (one night) might encourage more looking than a more expensive, typical stay (three nights), even if the latter is more common <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>.

### Inconsistent Behavior
Human behavior is often inconsistent. What works on one platform (e.g., laptop) might yield inverse results on another (e.g., mobile app) <a class="yt-timestamp" data-t="00:32:31">[00:32:31]</a>. People from different countries might react differently, and even the same person can show different behavior over time <a class="yt-timestamp" data-t="00:32:54">[00:32:54]</a>.

### Difficulty with Counterfactual Thinking
The concept of [[causal_ai_and_machine_learning_intersection | counterfactuals]] can be hard to grasp, even for experienced professionals <a class="yt-timestamp" data-t="00:36:21">[00:36:21]</a>. It requires an extra level of cognitive load to consider a completely different scenario and its potential outcomes <a class="yt-timestamp" data-t="00:36:44">[00:36:44]</a>.

## Overcoming Challenges

### Continuous Experimentation and Monitoring
Instead of "ship and forget," it's crucial to continuously run experiments and monitor outcomes over time <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>. This helps in understanding how the gap between treatment and no-treatment evolves as the business environment changes <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.

### Robust Solutions and Portfolio Approach
Building robust solutions, sometimes using a portfolio approach with several diverse strategies, helps ensure that there's always a working method even if one breaks <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.

### Prioritizing Simplicity
A key advice is to "keep it simple" <a class="yt-timestamp" data-t="00:51:53">[00:51:53]</a>. Start with simple solutions, even if they're not theoretically optimal, to learn and then gradually introduce complexity <a class="yt-timestamp" data-t="00:47:09">[00:47:09]</a>. Often, the simplest baseline can have a huge impact on results and customer behavior <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>.

### Focus on Impact, Not Just Accuracy
Machine learning scientists should prioritize understanding the use case and how their models will be deployed and affect business outcomes <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>. The goal is to move the needle on important business needs, not just achieve high accuracy scores <a class="yt-timestamp" data-t="00:25:24">[00:25:24]</a>.

### Bridging Disciplinary Gaps
There's a significant "citation gap" and differing terminologies between sub-areas of [[machine_learning_versus_causal_models_in_business | causality]] like economics and healthcare <a class="yt-timestamp" data-t="01:03:01">[01:03:01]</a>. Building bridges and fostering communication between these fields can prevent redundant problem-solving and lead to shared knowledge <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>, <a class="yt-timestamp" data-t="01:05:15">[01:05:15]</a>.

### Understanding the Problem First
Before picking tools or advanced architectures, it's essential to understand the fundamental problem that needs to be solved <a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a>. The evaluation metric is paramount; it needs to be consistent, correlated with the problem, useful, and easy for stakeholders to understand <a class="yt-timestamp" data-t="00:54:42">[00:54:42]</a>.