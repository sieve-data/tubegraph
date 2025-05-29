---
title: Ethereum Object Format and Developer Experience
videoId: WpjcPPrrN2E
---

From: [[bankless]] <br/> 

The Ethereum Object Format (EOF) is a significant overhaul of the [[ethereum_tech_stack_development | Ethereum Virtual Machine (EVM)]] aimed at improving the developer experience and enhancing the overall security and efficiency of the network <a class="yt-timestamp" data-t="00:46:56">[00:46:56]</a>. It is expected to be a major component of the upcoming Fusaka upgrade <a class="yt-timestamp" data-t="00:46:56">[00:46:56]</a>.

## What is EOF?

The EVM is often analogized to a 1950s computer, and EOF aims to bring it up to the level of a 1990s computer <a class="yt-timestamp" data-t="00:56:06">[00:56:06]</a>. While not bringing it to the "absolute cutting edge of computer science," EOF introduces fundamental improvements that are considered "pretty table stakes" for modern computing <a class="yt-timestamp" data-t="00:56:56">[00:56:56]</a>.

Key aspects of EOF include:
*   **Separation of Code and Data** Today, in Ethereum smart contracts, code and data can be mixed together <a class="yt-timestamp" data-t="00:57:06">[00:57:06]</a>. EOF introduces a clearer separation, making it easier for tooling to analyze and work with contracts <a class="yt-timestamp" data-t="00:57:17">[00:57:17]</a>.
*   **New Opcodes** EOF adds specific operation codes (opcodes) that simplify the process of writing compilers and programming languages that target the EVM <a class="yt-timestamp" data-t="00:57:28">[00:57:28]</a>.
*   **Removal of Problematic Features** EOF provides a "fresh start" where certain operations deemed problematic or less valuable can be banned for new EOF contracts <a class="yt-timestamp" data-t="00:57:41">[00:57:41]</a><a class="yt-timestamp" data-t="00:57:50">[00:57:50]</a>. This helps remove legacy issues that could hinder long-term [[ethereum_roadmap | Ethereum roadmap]] items <a class="yt-timestamp" data-t="00:58:36">[00:58:36]</a>.

EOF works as a "versioned type" of the EVM <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>. This means that smart contracts can opt-in to the EOF format, but existing contracts remain unaffected <a class="yt-timestamp" data-t="00:58:20">[00:58:20]</a><a class="yt-timestamp" data-t="00:58:21">[00:58:21]</a>.

## Impact on Developer Experience

The primary beneficiaries of EOF are developers, particularly those who write compilers and programming languages like Solidity <a class="yt-timestamp" data-t="00:58:50">[00:58:50]</a><a class="yt-timestamp" data-t="00:58:56">[00:58:56]</a>. By improving the fundamental capabilities and structure of the EVM, EOF allows for better tools and a more streamlined development process <a class="yt-timestamp" data-t="00:59:04">[00:59:04]</a><a class="yt-timestamp" data-t="00:59:08">[00:59:08]</a>.

Beyond direct development, EOF also contributes to security:
*   **Enhanced Auditing** It improves the ability to analyze what contracts do, especially in edge cases, which is beneficial for auditing and security analysis <a class="yt-timestamp" data-t="00:59:13">[00:59:13]</a><a class="yt-timestamp" data-t="00:59:21">[00:59:21]</a>.

## Integration into the Ethereum Roadmap

EOF, along with Pias (data availability sampling), was originally planned for the Petra hard fork but was deferred to Fusaka due to the extensive amount of work required <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a><a class="yt-timestamp" data-t="01:01:05">[01:01:05]</a>. The decision to separate them allowed for a more focused approach, ensuring that Fusaka primarily delivers these two significant changes <a class="yt-timestamp" data-t="01:01:07">[01:01:07]</a><a class="yt-timestamp" data-t="01:01:16">[01:01:16]</a>.

The [[ethereum_development_priorities | Ethereum core developers]] are aiming for Fusaka to ship in 2025 <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a><a class="yt-timestamp" data-t="00:47:27">[00:47:27]</a><a class="yt-timestamp" data-t="00:47:34">[00:47:34]</a>. The scope for Fusaka is intended to be kept relatively small, focusing on EOF and Pias, to avoid delays <a class="yt-timestamp" data-t="00:47:46">[00:47:46]</a><a class="yt-timestamp" data-t="00:48:07">[00:48:07]</a><a class="yt-timestamp" data-t="01:00:27">[01:00:27]</a>. While there are still ongoing debates about how to best test and deploy features like EOF, there's a broad agreement on the necessity and desired timeline <a class="yt-timestamp" data-t="00:50:02">[00:50:02]</a><a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a>. EOF represents a substantial upgrade to the EVM, akin to going from a very basic computer system to a more polished, dependable, and developer-friendly one <a class="yt-timestamp" data-t="00:59:35">[00:59:35]</a><a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.