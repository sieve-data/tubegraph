---
title: Tokenizing intellectual property on blockchain
videoId: Hf4EOUhRKXM
---

From: [[bankless]] <br/> 

Story Protocol is a new blockchain aiming to [[tokenization_of_content | tokenize the world's intellectual property (IP)]] and put it on-chain <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Its broader vision is to unlock future creative potential and enable a new era of human creativity, effectively becoming the IP layer for the internet <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This approach is distinct from prior blockchain constructions <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Understanding Intellectual Property (IP)

Intellectual property, as an asset class, is estimated to be worth multi-trillions of dollars, growing from $61 trillion in 2023 to $70 trillion currently, according to the World Intellectual Property Organization <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a> <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. It consists of various forms:
*   **Copyright** Creative works like songs, characters, or movies <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. This is Story Protocol's primary focus today <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Trademarks** Brands such as Louis Vuitton <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
*   **Patents** New inventions, processes, and drug discoveries <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. The world's most valuable companies often rely on patents <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. Block, for instance, holds hundreds of patents, and Jack Dorsey has 123 patents <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.

The market for IP is described as nebulous, undefined, and squishy <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>. Annually, licensing and royalty markets alone can reach a trillion dollars <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.

## Challenges of Traditional IP Management

Accessing IP is often more difficult than accessing debt, treasury bills, or real estate <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. The current IP system is characterized by:
*   **High Friction and Cost** Making a simple transaction, like licensing a Darth Vader lunchbox, is prohibitively expensive, requiring lawyers and extensive negotiations <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a> <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Reliance on Intermediaries** Layers of lawyers and agents negotiate deals, taking a cut and leaving the ultimate creator with very little <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.
*   **Subjectivity** The boundaries of what constitutes IP are often unclear and determined by lawyers in courtrooms on an as-needed basis <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. This means almost every IP interaction involves some subjectivity <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.

## Story Protocol's Solution: Tokenizing IP

Story Protocol aims to transform IP into a programmable asset, making the market more efficient <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. It leverages blockchain to:
*   **Automate Licensing** By putting IP on-chain, terms and conditions can be embedded directly, allowing for licensing via a simple API call or smart contract <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a> <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. This enables creators to define terms like upfront fees and revenue shares on-chain <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
*   **Streamline Royalties** Revenues can be streamed on-chain for everyone to audit <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   **Provide Clarity and Rigidity** Creators can set the granularity of their IP definition, uploading entire books or individual chapters <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
*   **Attestation Service** Story Protocol includes a "story attestation service" that checks new assets against existing ones on-chain or common infringed assets (e.g., Dua Lipa songs, Mickey Mouse) <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. It provides on-chain attestations indicating potential infringement, offering more clarity and rigidity than before <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>. AI is used in this service to filter out 99.9% of edge cases that previously required manual review <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
*   **Legal Framework Integration** For every dollar invested in tech, Story Protocol invests in building a legal framework called the "programmable IP license" <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>. This links the on-chain system with the legal system, ensuring that if something goes wrong, users can still resort to court, with the on-chain terms reflected in a legal contract <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. This approach aims to make IP more efficient and reduce transaction costs <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Two-Sided Marketplace** Story Protocol acts as a decentralized IP system, connecting IP holders (creators, studios) who supply IP with applications and partners that demand IP for licensing <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.

The process of on-ramping IP to Story Protocol involves dragging and dropping files, setting simple licensing terms (either manually or using presets), and registering them on-chain <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>. This generates a legal license for purchase, allowing for the creation of a secondary market for rights <a class="yt-timestamp" data-t="00:26:06">[00:26:06]</a>.

## Why a Purpose-Built Blockchain?

Story Protocol chose to build a purpose-built chain rather than a general-purpose blockchain or Layer 2 solution for several reasons:
*   **Custom Compute for Attestation** To decentralize the attestation service, Story Protocol wanted validators to run the compute, which wasn't easily achievable on existing Layer 2s <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.
*   **Cost Efficiency for Royalty Flow** Traversing the graph of parent-child IP relationships and flowing royalties up the tree becomes very expensive on standard EVM chains <a class="yt-timestamp" data-t="00:23:34">[00:23:34]</a>.
*   **Specialized Block Space** The thesis is that block space should be specialized, similar to how the internet evolved with specialized protocols <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>.
*   **Microservice Model** Story Protocol aims to be an IP microservice, allowing Web2 and Web3 applications to plug into it via an API for IP functionalities, while building payments on other chains like Base or ZK Sync <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.

## Go-to-Market Strategy for IP Tokenization

The strategy involves:
1.  **Bootstrapping Supply** Starting by bringing high-quality IPs on-chain to attract demand <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>. Examples include Justin Bieber's "Peaches" (via Arya protocol), Sabrina Carpenter songs, BTS songs, and Hollywood creators like David Guyer (creator of *The Dark Knight* trilogy) <a class="yt-timestamp" data-t="00:27:11">[00:27:11]</a>.
2.  **Zero-to-One Phase** [[tokenization_of_private_companies | Tokenizing existing "trad IP"]] to gain legitimacy and interest <a class="yt-timestamp" data-t="00:28:20">[00:28:20]</a>.
3.  **One-to-Ten Phase** Fostering the creation of net-new IP that is built to be decentralized and built upon, similar to the evolution of YouTube content <a class="yt-timestamp" data-t="00:27:57">[00:27:57]</a>.

## Addressing Skepticism: IP and Nation-States

A common critique is that IP is inherently a nation-state legal system construct, while blockchains aim to exist above nation-states <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>.

> "IP is inherently a nation state legal system construct and blockchains are not meant to cooperate necessarily with nation states. They are meant to be a layer higher than nation states and so it's weird to me that we are taking this nation state concept and trying to imbue it into a blockchain." <a class="yt-timestamp" data-t="00:29:05">[00:29:05]</a>

Story Protocol addresses this by adopting a "stablecoin approach" <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>. Just as stablecoins extend the US dollar by putting it on-chain to enable programmability, Story Protocol extends existing IP law by bringing it on-chain to make it more efficient <a class="yt-timestamp" data-t="00:33:07">[00:33:07]</a>. This pragmatic approach aims to make people comfortable with "code as law" <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>, eventually leading to a world where on-chain systems are preferred over traditional legal systems <a class="yt-timestamp" data-t="00:34:19">[00:34:19]</a>.

While Story Protocol doesn't guarantee perfect enforcement of all IP (which would require a surveillance state) <a class="yt-timestamp" data-t="00:40:30">[00:40:30]</a>, it significantly improves the status quo by:
1.  **Declaring Rights** Making it easy to establish provenance and attribution for IP <a class="yt-timestamp" data-t="00:41:09">[00:41:09]</a>.
2.  **Infringement Detection** The attestation service helps detect when IP is being used improperly <a class="yt-timestamp" data-t="00:42:36">[00:42:36]</a>.
3.  **Strengthening Legal Arguments** Having on-chain declaration and infringement detection makes any subsequent legal action a lot stronger, as US copyright law offers more damages if copyright is registered <a class="yt-timestamp" data-t="00:43:24">[00:43:24]</a>.

The goal is to integrate the registration process with governmental copyright offices worldwide <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>, leveraging the existing global harmonization of copyright law principles (e.g., the Berne Convention of 1886) <a class="yt-timestamp" data-t="00:46:40">[00:46:40]</a>. Story Protocol aims to be an "IP settlement network" and a shared standard across legal jurisdictions, akin to Visa or Mastercard for payments <a class="yt-timestamp" data-t="00:47:29">[00:47:29]</a>.

Another critique is the "age of abundance" argument, suggesting IP is useless when AI can generate content abundantly <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>. Story Protocol's view is that while content becomes abundant, truly novel or inspiring original ideas become *more* valuable <a class="yt-timestamp" data-t="00:36:04">[00:36:04]</a>. IP needs to be upgraded to scale with the internet and incentivize new creation, as civilizations with property rights tend to progress faster <a class="yt-timestamp" data-t="00:36:32">[00:36:32]</a>. The focus is on incentivizing creators to produce meaningful work for society's benefit, rather than just protecting individual ownership <a class="yt-timestamp" data-t="00:54:12">[00:54:12]</a>.

## The Role of the IP Token

Beyond traditional network security, gas, and governance functions, the IP token also acts as a bearer of demand <a class="yt-timestamp" data-t="00:52:57">[00:52:57]</a>. While users can pay for licenses in stablecoins or fiat, all revenue is converted to IP tokens on the back end, which then settle every IP transaction <a class="yt-timestamp" data-t="00:52:45">[00:52:45]</a>. This mechanism aims for all IP transactions globally to use the IP token "under the hood" <a class="yt-timestamp" data-t="00:53:07">[00:53:07]</a>.

## Conclusion: Incentivizing Creativity

Story Protocol is building an [[intersection_of_blockchain_technology_and_traditional_ip_law | innovation layer for human creativity]] <a class="yt-timestamp" data-t="00:55:54">[00:55:54]</a>. The goal is to provide incentives for creators to make meaningful contributions, recognizing that without such incentives, even AI models might eventually run out of original data to learn from <a class="yt-timestamp" data-t="00:55:16">[00:55:16]</a>. This approach supports human expressivity and creativity, especially as robotics and automation intelligence advance <a class="yt-timestamp" data-t="00:56:27">[00:56:27]</a>.