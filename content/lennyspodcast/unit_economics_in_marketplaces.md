---
title: Unit economics in marketplaces
videoId: AlTQ6O2qooI
---

From: [[lennyspodcast]] <br/> 

## Understanding Unit Economics
A deep understanding of [[role_of_data_science_in_successful_marketplaces | unit economics]] is a crucial part of understanding a marketplace business <a class="yt-timestamp" data-t="00:29:12">[00:29:12]</a>. While a [[understanding_the_framework_for_finding_productmarket_fit | SaaS business]] often has very low marginal costs, a transactional business typically has high costs of goods sold (COGS) or other significant costs that need to be modeled <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.

In the early stages, most marketplaces tend to have poor or even negative [[role_of_data_science_in_successful_marketplaces | unit economics]] because they are hard to start <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>. For example, Instacart famously lost money on every order, and Uber lost money on every ride in their early days <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>. However, as a marketplace grows, its [[role_of_data_science_in_successful_marketplaces | unit economics]] can improve because supply liquidity enhances the experience <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>. This can lead to a "crazy inversion" where customer acquisition costs (CAC) decrease and lifetime values (LTV) increase over time, making the business better <a class="yt-timestamp" data-t="00:26:11">[00:26:11]</a>.

## Components of Unit Economics in Marketplaces
A [[understanding_the_framework_for_finding_productmarket_fit | growth model]] for a transactional business needs to layer on how retained customers transact, including:
*   Transactions per month <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a>
*   Average Order Value (AOV) <a class="yt-timestamp" data-t="00:28:31">[00:28:31]</a>
*   Unit economics <a class="yt-timestamp" data-t="00:28:33">[00:28:33]</a>

### ROI Equations for Supply and Demand
For marketplaces, it's essential to develop [[role_of_data_science_in_successful_marketplaces | ROI equations]] for acquiring both supply and demand that fully capture the marketplace dynamic <a class="yt-timestamp" data-t="00:36:51">[00:36:51]</a>.

For example, when acquiring a new customer (demand side), the calculation of Customer Acquisition Cost (CAC) should include:
*   The CAC of acquiring the customer <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>
*   The CAC of acquiring the necessary supply for that customer to make a purchase, based on the ratio between demand and supply <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>

Similarly, for the supply side, a business cannot make a sale unless the marketplace also acquires the customer to transact with them <a class="yt-timestamp" data-t="00:37:10">[00:37:10]</a>.

By having these dual-sided [[role_of_data_science_in_successful_marketplaces | ROI equations]], marketplace balance can be somewhat less of a direct focus. Instead, acquisition efforts can be pushed to the comfortable payback period on either side <a class="yt-timestamp" data-t="00:37:17">[00:37:17]</a>.

### Payback Period vs. LTV to CAC
The speed at which a marketplace can recover enough money to acquire another customer is crucial for its [[marketplace_growth_strategy | growth]] <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. Therefore, [[role_of_data_science_in_successful_marketplaces | payback period]] is a better measure of paid marketing performance than the raw LTV to CAC ratio <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

## Pricing and Commission
When setting prices or commissions in a marketplace, especially on the supply side, the sensitivity is complex <a class="yt-timestamp" data-t="00:40:17">[00:40:17]</a>. If suppliers can transact at a rate that allows them to make money, they will likely sign up even with a high commission <a class="yt-timestamp" data-t="00:40:27">[00:40:27]</a>. The more commission a marketplace charges, the more it can fund benefits for its customers <a class="yt-timestamp" data-t="00:40:33">[00:40:33]</a>. For example, if Amazon charges a higher commission, it can fund more returns and faster shipping for its customers <a class="yt-timestamp" data-t="00:40:36">[00:40:36]</a>. The challenge lies in finding the right balance between charging more (which might discourage supply) and providing more benefits to demand (which encourages customer engagement) <a class="yt-timestamp" data-t="00:40:42">[00:40:42]</a>. This relationship is not simple to model with a single curve <a class="yt-timestamp" data-t="00:40:55">[00:40:55]</a>.

## Marketplace Evolution and Commission
Marketplaces have evolved to charge higher commissions over time by doing more work to justify those commissions <a class="yt-timestamp" data-t="00:59:07">[00:59:07]</a>.

*   **Marketplace 1.0 (Lead Generation)**: These primarily aggregate demand, like Zillow and HomeAdvisor. Their commission rates are often low, around 5-10% <a class="yt-timestamp" data-t="00:59:21">[00:59:21]</a>.
*   **Managed Marketplaces**: Platforms like Airbnb or Etsy go beyond lead generation by fundamentally creating trust in transactions and vetting supply. They charge a higher commission as a result of the work required to make transactions trustworthy and safe <a class="yt-timestamp" data-t="00:59:46">[00:59:46]</a>.
*   **Heavily Managed Marketplaces**: These marketplaces perform significant work within the value chain beyond just aggregating demand. For instance, DoorDash and Instacart own logistics, which allowed DoorDash to onboard more restaurants and make delivery more reliable, justifying higher commissions <a class="yt-timestamp" data-t="01:00:13">[01:00:13]</a>. Similarly, Fair underwrites transactions, taking on risk if a transaction fails or a retailer defaults, operating at a more fundamental level in the transaction <a class="yt-timestamp" data-t="01:00:24">[01:00:24]</a>.

As marketplaces continue to evolve, some may tend towards becoming e-commerce models with 100% commission, eventually no longer being a marketplace <a class="yt-timestamp" data-t="01:00:30">[01:00:30]</a>. Examples like OpenDoor operate as e-commerce websites rather than marketplaces, as they own the inventory (houses) and there's no direct transaction between a seller and buyer <a class="yt-timestamp" data-t="01:00:57">[01:00:57]</a>. The key variable in deciding if a marketplace will consolidate or remain in "marketplace mode" is the level of **creativity** in the space <a class="yt-timestamp" data-t="01:01:10">[01:01:10]</a>.

*   If the customer primarily desires a commoditized experience (e.g., a clean car that arrives on time, as in ride-sharing), the market will likely consolidate and evolve away from a marketplace model, especially with the advent of autonomous vehicles <a class="yt-timestamp" data-t="01:01:31">[01:01:31]</a>.
*   If the value is in suppliers bringing amazing, creative new things (e.g., Etsy, Amazon, Steam, Fair), then the businesses will likely remain in marketplace mode longer, as large companies are generally not good at fostering such creativity <a class="yt-timestamp" data-t="01:01:50">[01:01:50]</a>.