---
title: Innovative solutions for decentralized finance liquidity
videoId: 39xuOQnIqYQ
---

From: [[thepipeline_xyz]] <br/> 

Decentralized Finance (DeFi) has faced significant [[challenges_and_strategies_in_improving_liquidity_in_defi | challenges]] related to liquidity, particularly concerning inefficient capital use, trust, and fragmentation. Several projects are developing innovative solutions to address these issues, aiming to create more robust, efficient, and user-friendly financial ecosystems.

## Enhancing Verifiable Credit for Undercollateralized Lending
Accountable is building a platform for verifiable credit to enable a new wave of undercollateralized lending, which faced a 90% contraction in 2022 due to lack of trust <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. The core problem was the inability to verify or monitor the financial statements of counterparties, as exemplified by the $36 million loss with Ortogonal Trading in 2022 <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

### Solutions and Benefits
*   **Data Verification Platform** <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>: This platform serves as a trust layer, enabling lenders to calculate risk-reward and potentially reduce collateral requirements <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
    *   It uses proprietary API connectors, which can run in SGX (Software Guard Extensions) for hardware guarantees, and ZK-TLS (Zero-Knowledge Transport Layer Security) for increased trust <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
    *   The "SED API" (Sensitive Data Sharing API) is proposed as a future industry standard for secure data sharing <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
    *   Borrowers can prove their financial health in a privacy-preserving manner, leading to lower borrowing rates <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   **Capital Formation Layer** <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>: A capital formation layer is being developed to match lenders and borrowers in a privacy-preserving way, covering the full loan lifecycle, including compliance tooling <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Decentralized Credit Desks** <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>: The goal is to replace the old centralized model (e.g., Celsius, BlockFi, Genesis) by decentralizing credit desks with a professional network of specialists who manage retail capital and pass yields back to users <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   **Proof of Reserve Services** <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>: Accountable also offers proof of reserve services for stablecoin issuers, enabling smart contracts to prevent new minting if reserves are insufficient <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

## Recomposing DeFi: Decentralized Lending Exchanges
Amalgam is building a decentralized lending exchange to simplify capital efficiency, moving away from Uniswap V3's design which required users to manage assets across multiple protocols <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.

### Key Innovations
*   **Integrated DEX and Lending Protocol** <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>: Amalgam integrates a lending protocol directly into the DEX, allowing dormant assets to be lent out, showing an estimated 60% increase in capital efficiency <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.
*   **Enhanced Utility** <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>: The platform offers features like shorts, longs, and market making, allowing users to create delta-neutral strategies, leverage positions, or long volatility <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
*   **Autonomous and Manipulation-Resistant** <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>: The system operates autonomously without reliance on oracles, incorporating mechanisms to prevent manipulation and cascading liquidations <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. Price movements are incrementally restricted per block to prevent large trades from manipulating prices <a class="yt-timestamp" data-t="00:25:10">[00:25:10]</a>.
*   **Protocol Revenue** <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>: By taking lending fees, Amalgam expects a 2-3x increase in protocol revenue compared to swap fees alone <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.

## Decentralized Perpetual Exchanges with Onchain Order Books
Drake Exchange aims to combine the best aspects of Automated Market Maker (AMM) and order book models onchain, leveraging Monad's high transaction throughput <a class="yt-timestamp" data-t="01:05:08">[01:05:08]</a>.

### Key Features
*   **Hybrid AMM-Order Book Model** <a class="yt-timestamp" data-t="01:08:51">[01:08:51]</a>: Drake uses an on-demand auction liquidity model, where market makers compete for best price execution, backed by an order book and an AMM layer for guaranteed backstop liquidity <a class="yt-timestamp" data-t="01:07:34">[01:07:34]</a>.
*   **Advanced Trading Features** <a class="yt-timestamp" data-t="01:06:23">[01:06:23]</a>: It includes cross-collateral deposits, margin collateral swap, and customizable perpetual indices <a class="yt-timestamp" data-t="01:06:33">[01:06:33]</a>.
*   **Tokenized Funding Rate Vault** <a class="yt-timestamp" data-t="01:06:43">[01:06:43]</a>: Users can deposit USDC into this vault to earn a delta-neutral yield by collecting funding rate payments, with automated position management <a class="yt-timestamp" data-t="01:06:49">[01:06:49]</a>.
*   **"Lose to Earn" Incentive** <a class="yt-timestamp" data-t="01:10:11">[01:10:11]</a>: To encourage retail trading and disincentivize sybil activity, Drake will heavily compensate negative P&L, offering downside protection for traders <a class="yt-timestamp" data-t="01:10:21">[01:10:21]</a>.

## Credit Default Swaps for Pegged Assets
Cork Protocol is building a novel DeFi primitive: credit default swaps (CDS) for pegged assets, allowing users to price and hedge the risk of depeg events <a class="yt-timestamp" data-t="00:50:27">[00:50:27]</a>.

### Solutions
*   **Oracle-Free, Fully Collateralized CDS** <a class="yt-timestamp" data-t="00:52:10">[00:52:10]</a>: Cork creates a "depeg swap" module for each asset pair (e.g., ETH and stETH). When ETH is sent, two tokens are created: a depeg swap (redeemable for ETH if stETH depegs) and a "cover token" (underwriting the depeg risk) <a class="yt-timestamp" data-t="00:52:38">[00:52:38]</a>.
*   **Liquidity Vaults** <a class="yt-timestamp" data-t="00:57:57">[00:57:57]</a>: These vaults issue depeg swaps and earn yield from selling them, as well as from AMM and protocol fees <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>. This design aims to keep the risk premium for depeg swaps lower than the yield on the pegged assets <a class="yt-timestamp" data-t="00:58:47">[00:58:47]</a>.
*   **Use Cases** <a class="yt-timestamp" data-t="00:54:20">[00:54:20]</a>:
    *   **Liquidation-free lending pools** <a class="yt-timestamp" data-t="00:54:47">[00:54:47]</a>: Collateral can be fully hedged, enabling safer leverage trading.
    *   **Hedging** <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>: Users can earn yield on pegged assets without depeg risk, potentially attracting institutional capital <a class="yt-timestamp" data-t="00:54:09">[00:54:09]</a>.
    *   **Speculation** <a class="yt-timestamp" data-t="00:54:16">[00:54:16]</a>: Traders can speculate on depeg events, which helps in pricing market risk <a class="yt-timestamp" data-t="00:54:25">[00:54:25]</a>.
*   **Market Vision** <a class="yt-timestamp" data-t="00:54:40">[00:54:40]</a>: Cork aims to serve institutional credit markets for pegged assets today, real-world assets tomorrow, and eventually the broader $30 trillion global CDS market <a class="yt-timestamp" data-t="00:54:40">[00:54:40]</a>.

## AMM Rehypothecation for Enhanced Capital Efficiency
Hyperplex is addressing the capital inefficiency of AMMs, where 98% of liquidity often sits idle <a class="yt-timestamp" data-t="01:36:01">[01:36:01]</a>. Their solution, AMM rehypothecation, aims to put idle liquidity to work to earn additional yield <a class="yt-timestamp" data-t="01:36:09">[01:36:09]</a>.

### How it Works
*   **Wrapping Existing AMM Positions** <a class="yt-timestamp" data-t="01:36:31">[01:36:31]</a>: Users deposit their existing AMM positions (e.g., Uniswap) into Hyperplex, which then rehypothecates the dormant assets <a class="yt-timestamp" data-t="01:36:37">[01:36:37]</a>.
*   **Yield Generation** <a class="yt-timestamp" data-t="01:37:02">[01:37:02]</a>: This allows users to earn additional yield without changing their principal risk profile, effectively "free money" for LPs <a class="yt-timestamp" data-t="01:37:02">[01:37:02]</a>.
*   **Gamma Rehypothecation** <a class="yt-timestamp" data-t="01:38:17">[01:38:17]</a>: Hyperplex leverages the unique "negative gamma" (or curvature) of AMM liquidity to create a "positive gamma" position for options traders <a class="yt-timestamp" data-t="01:38:22">[01:38:22]</a>. This allows derivatives protocols to borrow liquidity from Hyperplex, solving their liquidity constraints <a class="yt-timestamp" data-t="01:38:55">[01:38:55]</a>.
*   **Multiple Yield Sources** <a class="yt-timestamp" data-t="01:39:12">[01:39:12]</a>: Users earn not only AMM yield and rehypothecation yield but also yield from derivatives platforms borrowing their liquidity <a class="yt-timestamp" data-t="01:39:18">[01:39:18]</a>. This creates a strong first-mover advantage <a class="yt-timestamp" data-t="01:39:41">[01:39:41]</a>.

## Infinity Pools: Unlimited Leverage with No Liquidations
Infinity Pools aims to enable unlimited leverage on any asset with no liquidations, counterparty risk, or oracles <a class="yt-timestamp" data-t="01:46:11">[01:46:11]</a>. Traditional futures models are problematic due to liquidation penalties and the risk of bad debt, especially for low-cap assets or large positions <a class="yt-timestamp" data-t="01:46:50">[01:46:50]</a>.

### Core Mechanism
*   **Liquidity-Backed Borrowing** <a class="yt-timestamp" data-t="01:48:26">[01:48:26]</a>: Instead of borrowing cash directly, users borrow liquidity positions (LP positions) backed by USDC. This LP position provides both the assets for the trade and the right to swap at a hypothetical liquidation price point <a class="yt-timestamp" data-t="01:48:33">[01:48:33]</a>.
*   **No Liquidations** <a class="yt-timestamp" data-t="01:49:30">[01:49:30]</a>: If the asset price drops, the user can still repay the borrowed liquidity because they hold the right to swap at the initial liquidation price, even if the market price falls to zero <a class="yt-timestamp" data-t="01:49:34">[01:49:34]</a>.
*   **Higher Yields for LPs** <a class="yt-timestamp" data-t="01:51:56">[01:51:56]</a>: LPs providing liquidity to Infinity Pools can achieve structurally higher yields than spot AMMs, generating continuous yield even when their liquidity is out of range <a class="yt-timestamp" data-t="01:52:02">[01:52:02]</a>.
*   **Unified Liquidity** <a class="yt-timestamp" data-t="01:52:20">[01:52:20]</a>: A single Infinity Pools liquidity pool can power multiple markets (spot, overcollateralized borrowing, options, leverage swaps) without fragmenting liquidity <a class="yt-timestamp" data-t="01:52:20">[01:52:20]</a>.

## Risk-Managed Credit Vaults for Market Making
RISK Finance is building risk-managed credit vaults to democratize market making and provide [[crypto_uncorrelated_returns | uncorrelated returns]] to liquidity providers (LPs) <a class="yt-timestamp" data-t="03:25:19">[03:25:19]</a>.

### Solution
*   **LP Deposits and Market Maker Access** <a class="yt-timestamp" data-t="03:25:23">[03:25:23]</a>: LPs deposit capital into the vault, earning from rewards and sophisticated trading strategies run by professional market makers <a class="yt-timestamp" data-t="03:25:32">[03:25:32]</a>.
*   **Cross-Exchange Strategies** <a class="yt-timestamp" data-t="03:25:48">[03:25:48]</a>: Market makers use this capital to execute high-frequency strategies across multiple exchanges simultaneously, improving market efficiency <a class="yt-timestamp" data-t="03:25:48">[03:25:48]</a>.
*   **Counterparty Risk Mitigation** <a class="yt-timestamp" data-t="03:26:23">[03:26:23]</a>: Market makers can run strategies without direct counterparty risk, as they use LP funds via a signing mechanism rather than taking custody <a class="yt-timestamp" data-t="03:36:01">[03:36:01]</a>.
*   **Exchange Integration** <a class="yt-timestamp" data-t="03:26:40">[03:26:40]</a>: Exchanges can integrate with RISK Finance to have decentralized market making, lowering liquidity costs and creating more efficient order books <a class="yt-timestamp" data-t="03:26:40">[03:26:40]</a>. RISK Finance's own exchange will boost LP returns by channeling all generated fees <a class="yt-timestamp" data-t="03:27:41">[03:27:41]</a>.

## Turbocharging Onchain Activity with Trusted Execution Environments
Sauce aims to improve [[trading_user_experience_in_decentralized_finance | the trading user experience]] for advanced traders by building a centralized exchange-like experience onchain, leveraging Trusted Execution Environments (TEEs) <a class="yt-timestamp" data-t="03:39:31">[03:39:31]</a>.

### Key Innovations
*   **One-Click Transactions** <a class="yt-timestamp" data-t="03:39:51">[03:39:51]</a>: Enables one-click transactions into any asset on any chain, including meme coins, perpetuals, prediction markets, and exotic derivatives <a class="yt-timestamp" data-t="03:39:51">[03:39:51]</a>.
*   **Automated Yield for Idle Funds** <a class="yt-timestamp" data-t="03:40:09">[03:40:09]</a>: Automatically directs idle funds into yield-earning protocols <a class="yt-timestamp" data-t="03:40:09">[03:40:09]</a>.
*   **Transaction Automation with TEEs** <a class="yt-timestamp" data-t="03:40:38">[03:40:38]</a>: Leverages TEEs (specifically AWS Nitro) for secure and private transaction automation <a class="yt-timestamp" data-t="03:44:26">[03:44:26]</a>. This enables features like private dollar-cost averaging (DCAs) and off-chain limit orders, addressing traders' concerns about public onchain visibility <a class="yt-timestamp" data-t="03:40:48">[03:40:48]</a>. Only the user has access to the private key within the TEE <a class="yt-timestamp" data-t="03:41:25">[03:41:25]</a>.
*   **Enhanced Security and Efficiency** <a class="yt-timestamp" data-t="03:41:41">[03:41:41]</a>: The infrastructure is designed to be more powerful for power users, offering similar security to centralized exchanges but with greater efficiency <a class="yt-timestamp" data-t="03:41:41">[03:41:41]</a>.

## Agnostic Execution Network for Unified DeFi
Symphony is building an agnostic execution network designed to make DeFi usable, scalable, and accessible by removing friction and unifying liquidity across chains <a class="yt-timestamp" data-t="03:52:21">[03:52:21]</a>. It aims to allow users to transact across all chains without needing to use bridges, manage wallets, or deal with gas fees <a class="yt-timestamp" data-t="03:52:30">[03:52:30]</a>.

### Core Problems Addressed
*   **Complexity for New Users** <a class="yt-timestamp" data-t="03:53:08">[03:53:08]</a>: Crypto onboarding is overwhelming due to concepts like gas, L2s, token addresses, and the need to use various tools (bridges, wallets, chains, protocols) <a class="yt-timestamp" data-t="03:53:08">[03:53:08]</a>. A simple perpetual trade could take over 6 minutes and 73 clicks <a class="yt-timestamp" data-t="03:54:08">[03:54:08]</a>.
*   **Liquidity Fragmentation** <a class="yt-timestamp" data-t="03:54:25">[03:54:25]</a>: Liquidity is scattered across protocols and chains, leading to insufficient liquidity, bad slippage, and poor user experiences <a class="yt-timestamp" data-t="03:54:35">[03:54:35]</a>.

### Symphony's Solution
*   **Cross-Chain, Multi-Protocol Trading** <a class="yt-timestamp" data-t="03:55:22">[03:55:22]</a>: Symphony enables users to perform complex trades (e.g., three cross-chain trades at once) in under 3 seconds <a class="yt-timestamp" data-t="03:55:24">[03:55:24]</a>.
*   **Omni-Chain Collateral and Smart Accounts** <a class="yt-timestamp" data-t="03:55:54">[03:55:54]</a>: Users can lock collateral on any integrated EVM-compatible chain <a class="yt-timestamp" data-t="03:55:57">[03:55:57]</a>. The system uses a custom ERC-4337 based Symphony wallet, a smart account deployed on every EVM chain, ensuring full user custody throughout the trade lifecycle <a class="yt-timestamp" data-t="03:56:50">[03:56:50]</a>.
*   **Permissionless Solver Network (Cortex)** <a class="yt-timestamp" data-t="03:59:54">[03:59:54]</a>: Trade intents are sent to a network of permissionless solvers who compete to find the best liquidity and fees across different perpetual exchanges and chains, potentially sharding large trades across multiple protocols <a class="yt-timestamp" data-t="03:56:15">[03:56:15]</a>.
*   **Benefits for Monad Community** <a class="yt-timestamp" data-t="03:59:01">[03:59:01]</a>: Symphony offers access to billions in liquidity from day one, seamless one-click onboarding, and brings trades to Monad for execution due to its superior performance <a class="yt-timestamp" data-t="03:59:05">[03:59:05]</a>.