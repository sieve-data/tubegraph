---
title: Understanding Supply APY and Stake APR
videoId: pBANahZZqYQ
---

From: [[goingonchain]] <br/> 

This article clarifies the distinction between supply APY and stake APR on [[Staking and Borrowing Strategies on Hundred Finance | Hundred Finance]], addressing common questions about earning strategies and token mechanics <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Supply APY

When you supply a stable or crypto asset to [[Staking and Borrowing Strategies on Hundred Finance | Hundred Finance]], you earn a supply APY <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. Your exposure remains with your supplied assets, and you receive an `hToken` as a receipt <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. For example, supplying [[high_apy_and_staking_mechanics_in_meme_currencies | MEME]] yields `hMEME` as a receipt <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

Consider an example of supplying 500 [[high_apy_and_staking_mechanics_in_meme_currencies | MEME]] on [[Staking and Borrowing Strategies on Hundred Finance | Hundred Finance]]:
*   You will earn only the supply [[understanding_10000_apy_and_its_risks | APY]], which might be around 0.27% <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   You will **not** earn the HND token [[interest_rates_and_yields_on_anchor | APR]] (e.g., 18.89%) by simply supplying <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

### Taking Loans with Supplied Assets
If your objective is to take a loan, you must only supply your assets without staking them <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. For instance, supplying 500 [[high_apy_and_staking_mechanics_in_meme_currencies | MEME]] allows you to borrow up to 50% of your limit, such as 14,000 tokens of Spell <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Stake APR

To earn the HND token [[interest_rates_and_yields_on_anchor | APR]], you must stake your `hToken` receipt (e.g., `hMEME`) <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   You select "stick" (stake) to stake your `hToken` <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   Staking your `hToken` allows you to earn HND <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

### Important Consideration: Staking and Loans
Once you stake your assets, you will no longer be able to take a loan against them <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. If you stake half of your supplied [[high_apy_and_staking_mechanics_in_meme_currencies | MEME]], your supply value drops by half, and consequently, the amount you can borrow also drops by half <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## Collecting HND Rewards

To withdraw your earned HND [[Real Yield in DeFi | rewards]], navigate to the HND section on the platform and click "collect" on the right side of the page <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. This dashboard also provides an overview of your supply [[interest_rates_and_yields_on_anchor | APR]] and staking [[understanding_10000_apy_and_its_risks | APY]] for the HND token <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

## Utilities of HND Tokens

You can lock up your HND tokens to earn more [[Real Yield in DeFi | rewards]] through voting escrow HND (`veHND`) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This is done on the "vote" page <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

### Calculating `veHND`
The amount of `veHND` you receive depends on the lock-up period for your HND tokens <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>:
*   100 HND locked for 4 years yields 100 `veHND` <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   100 HND locked for 2 years yields 50 `veHND` <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   If you add more HND to an existing lock-up, it will follow the previously committed period <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

### Benefits of `veHND`

1.  **Vote for Pool Rewards:** You can use your `veHND` to vote for specific pools. The more votes a pool receives, the higher its average [[interest_rates_and_yields_on_anchor | APR]] on HND [[Real Yield in DeFi | rewards]] <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
2.  **Boost Personal Rewards:** `veHND` allows you to boost your own [[interest_rates_and_yields_on_anchor | APR]] on specific assets, up to a maximum of 2.5x <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. [[Staking and Borrowing Strategies on Hundred Finance | Hundred Finance]] provides a calculator to determine the `veHND` needed for the maximum boost <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

#### Applying a Boost
After locking up HND to get `veHND`, click "apply" to trigger a transaction and activate your boost <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. For example, boosting from 1x to 2.5x can increase your [[interest_rates_and_yields_on_anchor | APR]] on [[high_apy_and_staking_mechanics_in_meme_currencies | MEME]] from 18.87% to 45% initially <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### Epochs and Voting Cycles
You can only vote every 10 days <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. The [[interest_rates_and_yields_on_anchor | APR]] you earn is subject to changes in the next epoch, influenced by the votes received by different pools (e.g., USDC receiving more votes could lower the [[interest_rates_and_yields_on_anchor | APR]] for [[high_apy_and_staking_mechanics_in_meme_currencies | MEME]] in the next epoch) <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. The time remaining until the next epoch's end is displayed on the platform <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.