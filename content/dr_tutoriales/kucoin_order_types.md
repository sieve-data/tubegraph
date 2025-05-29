---
title: KuCoin order types
videoId: WzwaAMt3rgs
---

From: [[dr_tutoriales]] <br/> 

This tutorial provides a detailed explanation of various order types available on the [[understanding_kucoins_platform_and_interface | KuCoin]] platform, designed to facilitate strategic purchases and sales of cryptocurrencies <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Understanding these orders can simplify your trading life <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

It is recommended to be familiar with the [[understanding_kucoins_platform_and_interface | KuCoin]] platform's interface before proceeding <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Orders are typically placed within the "commercial and spot valet market" section <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

## Order Types

### Market Order
A [[market_orders_in_trading | market order]] is executed in real-time at the current market value of the cryptocurrency <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This means if you place a buy or sell [[market_orders_in_trading | market order]], it will be fulfilled at the exact price the asset is trading at the moment you click <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. For example, if KCS is at 10.687 USDT, a buy order will execute at that value instantly <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### Limit Order
A [[limit_orders_explained | limit order]] allows you to set a specific price at which you want to buy or sell a cryptocurrency <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. The order will only execute when the real market price reaches your predetermined value <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

To place a [[limit_orders_explained | limit order]]:
1.  Enter the desired price <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
2.  Enter the quantity of the cryptocurrency you wish to buy or sell <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

For example, if you believe the price of KCS will drop to 9.984 USDT before rising again, you can set a buy limit order at that price <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. Similarly, if you expect the price to rise to 11.187 USDT (a resistance level) and then fall, you can place a sell limit order at that point <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

Open [[limit_orders_explained | limit orders]] are visible in the "Open Orders" section of the order book <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. These orders can be cancelled at any time if they have not been fully executed <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### Stop-Limit Order
The stop-limit order is more complex and involves two key prices: the 'limit price' and the 'stop price' <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
*   **Limit Price:** The price at which the order begins to execute <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Stop Price:** The price at which the order is fully executed <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

The order executes progressively. When the market price reaches the limit price, the order starts to fill, but it doesn't necessarily execute 100% immediately <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. It continues to fill gradually as the price moves towards the stop price <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. Once the price reaches the stop price, 100% of the order is executed <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

If the price moves past the limit price but *doesn't* reach the stop price (e.g., it reverses), only a partial percentage of the order will have been executed <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This order type is useful for reducing risk in operations, as it prevents losing all capital if the market does not follow the expected pattern <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

### Stop-Market Order
The stop-market order is similar to the stop-limit order but executes at the current [[market_orders_in_trading | market price]] once the 'stop price' is triggered <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>. Instead of setting a specific limit price for execution, the order is fulfilled at the prevailing market rate when the stop condition is met <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

To place a stop-market order:
1.  Set the 'stop price' <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
2.  Specify the quantity to buy or sell <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.

When the market price reaches the stop price, the order executes at 100% at the current market rate <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. These orders can also be viewed and cancelled from the "Stop Orders" section <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. The flexibility allows cancellation even if only a percentage of the order has been executed <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.