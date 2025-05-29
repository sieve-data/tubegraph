---
title: Stop limit orders
videoId: WzwaAMt3rgs
---

From: [[dr_tutoriales]] <br/> 

Stop limit orders are a type of order available on the [[kucoin_order_types|KuCoin]] platform, offering a strategic way to manage buy and sell orders. They are designed to allow users to set a predetermined price at which an order will be placed, and a "stop price" at which the order will fully execute, reducing risk in volatile markets <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

## Components of a Stop Limit Order

A stop limit order involves three key components:
*   **Stop Price** <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>: This is a trigger price that initiates the order <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. When the market price reaches the stop price, a [[limit_orders_explained|limit order]] is then placed on the order book <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. The stop price also defines the point at which the order will be completely executed <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Limit Price** <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>: This is the specific price at which the order is intended to be executed <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. Once the stop price is hit, the [[limit_orders_explained|limit order]] is placed at this price <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **Quantity** <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>: This is the amount of cryptocurrency you wish to buy or sell <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## How Stop Limit Orders Work

When the market price reaches the predetermined limit price, the buy or sell order begins to execute incrementally <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. The order continues to execute gradually as the price moves towards the stop price <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. Once the stop price is reached, 100% of the order will have been executed <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

> [!NOTE] Partial Execution
> If the price does not reach the stop price and reverses direction, only a percentage of the order corresponding to how close it got to the stop price will be executed <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. For instance, if the price hits the limit price but then falls before reaching the stop price, only a partial percentage (e.g., 20%) of the order may be filled <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

This progressive execution mechanism helps to reduce risk, as it prevents the entire order from being filled if the market does not follow the expected pattern <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. This ensures that users do not lose all their money if the price action deviates from their strategy <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

### Stop Limit Buy Example
Imagine the current price of an asset is at 10.687 <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. If you believe the price will drop to 9.984 before rising again, you might set a [[limit_orders_explained|limit order]] to buy at 9.984 <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. For a stop limit buy order, you might set the limit price at 9.96 <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a> and a stop price at 10.368 <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. As the price goes up from 9.96 towards 10.368, percentages of the order will execute, and at 10.368, 100% of the order will be filled <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

### Stop Limit Sell Example
Similarly, for a sell order, you might set a limit price at an anticipated resistance level, such as 11.187 <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. You would set the stop price further up, for example, at 11.041 <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. The orders will execute progressively as the price moves, reaching 100% execution if it crosses the stop price <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. If the price does not follow the desired pattern and continues to rise, only a small percentage might be executed <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

## Comparison to Stop Market Orders

The concept of a stop limit order is similar to a [[stop_market_orders|stop market order]] <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>. However, with a [[stop_market_orders|stop market order]], when the stop price is reached, a [[market_orders_in_trading|market order]] is executed immediately at the current market price, rather than a [[limit_orders_explained|limit order]] being placed <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. This means a [[stop_market_orders|stop market order]] does not give the option to enter a specific price for execution; it happens instantly at the prevailing [[market_orders_in_trading|market order]] rate once the stop is triggered <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.