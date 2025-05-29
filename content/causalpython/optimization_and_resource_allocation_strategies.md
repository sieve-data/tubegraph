---
title: Optimization and Resource Allocation Strategies
videoId: xkx1tXLAP-o
---

From: [[causalpython]] <br/> 

At Booking.com, optimization and resource allocation are critical for personalizing user experiences, especially when dealing with promotions and discounts <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The objective is to manage costs while maximizing business growth <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

## Core Problem: Balancing Discounts and Budget Constraints

Promotions and discounts are highly effective in influencing customer behavior, often leading to increased bookings and expanding the customer base <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>, <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. However, these incentives come with a cost, necessitating careful [[optimal_experimentation_in_causal_studies | optimization]] to prevent financial losses <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>, <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

The challenge lies in determining when and what kind of discount to offer <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. The goal is to incentivize customers who would *not* book otherwise, rather than providing discounts to those who would convert regardless <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>, <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. This involves focusing on the [[ab_testing_and_machine_learning_models | counterfactual problem]]: what would happen with and without the discount <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

Promotions often have a "trigger cost," meaning the cost is incurred only if the customer likes the offer and makes a booking <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>, <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. If a customer doesn't book, or if the interaction is bot traffic, no cost is incurred <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>, <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

## Budgeting for Growth

The company's growth strategy aims to utilize as much of the allocated budget as possible, even if it means self-funding campaigns to give more value and discounts to customers <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>, <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. This creates a two-dimensional optimization problem: maximizing incremental volumes (new customers, new reservations) while controlling incremental costs to stay within a predefined budget or return on investment threshold <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>, <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

This problem is likened to a "knapsack problem," where one must select which items (discounts) to "pick" to fit within the "capacity" (budget constraint) <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>, <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

## Challenges in Combining Optimization and Causal Inference

Combining [[optimal_experimentation_in_causal_studies | optimization]] with [[causal_ai_in_supply_chain_management | causal inference]] and recommendation systems presents unique challenges <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>:
*   **Theoretical vs. Applied Solutions** <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>: While problems like the knapsack problem are theoretically NP-hard, practical solutions often rely on approximations, such as sorting outcomes by value-to-weight ratio <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>, <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.
*   **Noisy Data** <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>: Real-world data is noisy, leading to overfitting and seasonality issues <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
*   **Evolving Problems** <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>: Business needs and constraints are dynamic, requiring constant adaptation rather than a one-time "optimal" solution <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>, <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>. Solutions must be robust and reusable across different scenarios <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.
*   **Cost of Online Testing** <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>: Testing models online, especially those involving discounts, can be costly if implemented incorrectly <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>. Therefore, robust offline testing and training are preferred <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.

## Strategies for Robustness and Continuous Improvement

To tackle these challenges, several strategies are employed:
*   **Alignment of Metrics and Data** <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>: Ensure online and offline metrics and data collection processes are aligned <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>, <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.
*   **Continuous Experimentation** <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>: Run tests continuously to monitor the impact of treatments over time and react to changes <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>, <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>.
*   **Portfolio Approach** <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>: Develop multiple, diverse strategies for solutions to ensure that if one method fails, others can still be relied upon <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>, <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>.
*   **Stick to Simple Models** <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>: Simpler models are easier to deploy and maintain, reducing the risk of overfitting due to fluctuating variables <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>, <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>, <a class="yt-timestamp" data-t="00:52:21">[00:52:21]</a>.
*   **Monitor Outcomes and React to Data** <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>, <a class="yt-timestamp" data-t="00:45:31">[00:45:31]</a>: Especially with dynamic environments like pricing, continuous monitoring against a holdout group is essential <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>, <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.

## Optimization with Causal Inference

The approach to optimization involves using [[causal_ai_in_supply_chain_management | causal inference]] techniques like uplift modeling, also known as heterogeneous treatment effect <a class="yt-timestamp" data-t="00:40:48">[00:40:48]</a>, <a class="yt-timestamp" data-t="00:40:50">[00:40:50]</a>. This aims to find the conditional average treatment effect of various treatments, which could be binary (give or not give a discount) or multiple (what kind of discount to offer) <a class="yt-timestamp" data-t="00:40:53">[00:40:53]</a>, <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>.

The process often begins with randomized data from A/B tests <a class="yt-timestamp" data-t="00:41:37">[00:41:37]</a>, <a class="yt-timestamp" data-t="00:42:20">[00:42:20]</a>. When dealing with observational data, debiasing techniques are used <a class="yt-timestamp" data-t="00:41:44">[00:41:44]</a>, <a class="yt-timestamp" data-t="00:41:59">[00:41:59]</a>. The objective is to identify the most suitable customer segments for a given treatment based on their potential outcome with and without the treatment <a class="yt-timestamp" data-t="00:43:49">[00:43:49]</a>, <a class="yt-timestamp" data-t="00:44:05">[00:44:05]</a>. This is typically measured using causal measurements like K-curves to find the optimal threshold for intervention <a class="yt-timestamp" data-t="00:44:56">[00:44:56]</a>, <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>.

!> **Key Lesson:** The most accurate prediction is not always the most beneficial. For instance, while most people book three nights in Paris, recommending a one-night stay might be more effective because it presents a cheaper price and more availability, encouraging users to continue exploring <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>, <a class="yt-timestamp" data-t="00:30:25">[00:30:25]</a>. This highlights the importance of understanding human psychology and focusing on behavioral change <a class="yt-timestamp" data-t="00:30:11">[00:30:11]</a>.