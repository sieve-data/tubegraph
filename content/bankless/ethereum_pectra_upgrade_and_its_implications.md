---
title: Ethereum Pectra upgrade and its implications
videoId: MqrlFj_5LtY
---

From: [[bankless]] <br/> 

The [[ethereums_pectra_upgrade | Ethereum Pectra upgrade]] went live on the morning of May 7th <a class="yt-timestamp" data-t="01:00:51">[01:00:51]</a>. This upgrade brings a range of new Ethereum Improvement Proposals (EIPs) to the network <a class="yt-timestamp" data-t="01:00:55">[01:00:55]</a>.

## Key Ethereum Improvement Proposals (EIPs)

The primary EIPs highlighted in the Pectra upgrade include:

### EIP 7702: Account Abstraction for EOAs
EIP 7702 is considered a significant upgrade, particularly for user experience (UX) <a class="yt-timestamp" data-t="01:01:34">[01:01:34]</a>.
It enables all Ethereum EOA (Externally Owned Account) wallets to gain smart contract functionality <a class="yt-timestamp" data-t="01:01:06">[01:01:06]</a>. This allows 0x addresses to run one-off contract code, execute it, and then revert to being a vanilla EOA <a class="yt-timestamp" data-t="01:01:50">[01:01:50]</a>.

Key benefits include:
*   **Batch Transactions:** Users can now consolidate multiple transactions, including approvals, into a single one-click experience <a class="yt-timestamp" data-t="01:02:08">[01:02:08]</a>. This removes the need for multiple "approve" popups, addressing a known UX pain point <a class="yt-timestamp" data-t="01:02:03">[01:02:03]</a>.
*   **Reduced Failed Transactions:** This functionality also helps reduce service area for failed transactions <a class="yt-timestamp" data-t="01:02:11">[01:02:11]</a>.
*   **Sponsored Gas Fees:** Apps on the Layer 1 can now pay gas fees for their users, or gas fees can be paid in tokens, primarily stablecoins <a class="yt-timestamp" data-t="01:02:24">[01:02:24]</a>.

### EIP 7691: Expanding Blob Capacity
This EIP doubles the target blob capacity from 3 to 6 blobs <a class="yt-timestamp" data-t="01:01:17">[01:01:17]</a>. While this represents a meaningful percentage increase, in raw terms, it is still considered small compared to other data availability (DA) solutions like Celestia or Ida, which operate at orders of magnitude higher <a class="yt-timestamp" data-t="01:05:05">[01:05:05]</a>. Ethereum currently pushes about 15 kilobytes, whereas Celestia pushes megabytes a second <a class="yt-timestamp" data-t="01:05:39">[01:05:39]</a>.

### EIP 7251: Max Effective Balance
This EIP allows validators to stake a range of ETH, from 32 ETH up to 48 ETH, instead of being limited to a rigid 32 ETH <a class="yt-timestamp" data-t="01:01:29">[01:01:29]</a>. The increase in blob count within the same hard fork is a result of the bandwidth reduction achieved by the max effective balance (Max EB) reduction <a class="yt-timestamp" data-t="01:08:26">[01:08:26]</a>. As validators consolidate their ETH holdings into fewer boxes, there's less network "gossip" and reduced bandwidth overhead, which is then reallocated to allow for more blobs <a class="yt-timestamp" data-t="01:08:43">[01:08:43]</a>. This transition will be gradual, as validators consolidate incrementally over weeks and months <a class="yt-timestamp" data-t="01:09:19">[01:09:19]</a>.

## Implications and Analysis

### Operational Challenges and Lessons Learned
The [[challenges_in_ethereums_upgrade_processes | Pectra upgrade]] took a considerable amount of time to ship and experienced delays, leading to some internal fighting over its contents <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. Some elements of the upgrade are seen as underwhelming in hindsight, and it was not considered the most operationally efficient hard fork for Ethereum <a class="yt-timestamp" data-t="01:03:11">[01:03:11]</a>. However, it's believed that lessons have been learned from this experience <a class="yt-timestamp" data-t="01:03:25">[01:03:25]</a>, influencing future [[ethereum_roadmap | Ethereum roadmap]] goals, such as the aggressive push for Purdosa later in 2024 <a class="yt-timestamp" data-t="01:03:49">[01:03:49]</a>.

### Scalability: Blobs vs. Execution
While Pectra scales blobs, the increase is modest compared to other chains <a class="yt-timestamp" data-t="01:05:26">[01:05:26]</a>. This highlights a debate within the [[ethereum_roadmap | Ethereum roadmap]] regarding the prioritization of Layer 1 (L1) execution scaling versus blob scaling <a class="yt-timestamp" data-t="01:10:37">[01:10:37]</a>. If Ethereum is not aiming to handle a "gazillion transactions" as its endgame <a class="yt-timestamp" data-t="01:10:48">[01:10:48]</a>, then the focus should be on its more valuable markets: premium execution rather than premium data availability <a class="yt-timestamp" data-t="01:11:22">[01:11:22]</a>.

> "I actually think like most of the L1 scaling stuff of like reducing block times um and increasing gas there actually gets you a lot more bang for your buck. Um just because that is just like a much more valuable use of that same commodity that you have." <a class="yt-timestamp" data-t="01:11:43">[01:11:43]</a>

Lowering block times is seen as more important than raising block size, especially for enabling faster trading and leveraging Ethereum's sophisticated MEV mitigation infrastructure for institutions like Wall Street <a class="yt-timestamp" data-t="01:13:09">[01:13:09]</a>.

### UX Improvements and User Adoption
The UX upgrades, especially EIP 7702's account abstraction features, are expected to significantly enhance the Layer 1 user experience <a class="yt-timestamp" data-t="01:02:28">[01:02:28]</a>. The removal of repeated approval pop-ups and the introduction of sponsored gas fees make interactions much smoother <a class="yt-timestamp" data-t="01:02:08">[01:02:08]</a>. The success of these features, however, depends on widespread adoption by wallets <a class="yt-timestamp" data-t="01:03:35">[01:03:35]</a>.