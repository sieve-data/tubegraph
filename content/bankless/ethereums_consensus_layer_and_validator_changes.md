---
title: Ethereums Consensus Layer and Validator Changes
videoId: WpjcPPrrN2E
---

From: [[bankless]] <br/> 

The [[Ethereum ecosystem and leadership changes | Ethereum roadmap]] is a constantly evolving process, with [[Ethereum upgrades for 2025 | upgrades]] adapted through debate, deliberation, and rough consensus at the All Core Devs (ACD) calls <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>. Tim Beiko, a coordinator of these calls, plays a central role in prioritizing and progressing discussions for [[Ethereum upgrades for 2025 | Ethereum's]] future <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.

## Development Priorities

The foremost priority in [[Ethereum upgrades for 2025 | Ethereum]] development is **security** <a class="yt-timestamp" data-t="06:44:00">[06:44:00]</a>. This robust approach differentiates [[Ethereum ecosystem and leadership changes | Ethereum]] from other chains, ensuring it has never gone down <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>. Updates to [[Ethereum upgrades for 2025 | Ethereum]] must pass through a rigorous security filter, as there are no off-chain mechanisms (like lawyers or legal systems in traditional finance) to fix issues once they are deployed <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>. Major events like Bitcoin's inflation bug or the DAO hack highlight the contentious nature of social interventions, making security paramount to avoid such situations <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>. This emphasis on security is a primary reason why [[Challenges in Ethereums upgrade processes | Ethereum upgrades slowly]], undergoing thorough testing cycles that can take between six and twelve months <a class="yt-timestamp" data-t="11:54:00">[11:54:00]</a>. Many proposed Ethereum Improvement Proposals (EIPs) are rejected or take years to iterate on due to security concerns <a class="yt-timestamp" data-t="12:06:00">[12:06:00]</a>.

Beyond security, the most prominent theme over the past year has been **scaling** <a class="yt-timestamp" data-t="07:40:00">[07:40:00]</a>, both on the execution and consensus layers <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>.

## Naming Conventions for Hard Forks

[[Ethereum upgrades for 2025 | Ethereum hard forks]] are named by combining a Devcon city name (for the execution layer) and a star name (for the Beacon Chain consensus layer) <a class="yt-timestamp" data-t="13:17:00">[13:17:00]</a>. Although they are mashed together for user convenience, they represent changes to both parts of [[Ethereum Layer 1 versus Layer 2 dynamics | Ethereum's]] protocol <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>.

*   **Pectra**: Prague (execution layer) + Electra (consensus layer) <a class="yt-timestamp" data-t="13:47:00">[13:47:00]</a>
*   **Fusaka**: Fulu (star) + Osaka (city) <a class="yt-timestamp" data-t="13:49:00">[13:49:00]</a>
*   **Glamsterdam**: Glam (star, though the specific star isn't recalled in the transcript) + Amsterdam (first Devcon city) <a class="yt-timestamp" data-t="13:53:00">[13:53:00]</a>

## Pectra Hard Fork (Projected May 2024)

Pectra is the next hard fork on the horizon, with a projected activation in May 2024 if testing proceeds smoothly <a class="yt-timestamp" data-t="42:48:00">[42:48:00]</a>. Its primary focuses are on scaling the consensus layer and enhancing account functionality.

### Max EB (Increased Validator Maximum Balance)

A major feature of Pectra is the increase of validators' maximum balance <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a>. Currently, validators are discrete 32 ETH chunks, meaning a large entity like Coinbase with 320 ETH would need to spin up 10 validators, sending 10 times as many messages <a class="yt-timestamp" data-t="16:44:00">[16:44:00]</a>. With Max EB, validators can consolidate up to 2048 ETH into a single validator <a class="yt-timestamp" data-t="15:13:00">[15:13:00]</a>.

*   **Benefits for Large Operators**: This consolidation significantly reduces bandwidth usage on the network by allowing large operators to send one message with a higher weight, instead of multiple messages from many smaller validators <a class="yt-timestamp" data-t="17:58:00">[17:58:00]</a>. This reduction frees up bandwidth for other scaling efforts, particularly for blobs <a class="yt-timestamp" data-t="15:28:00">[15:28:00]</a>.
*   **Benefits for Small Validators**: Smaller validators can now set up a validator with an arbitrary amount of ETH between 32 and 2048 ETH, effectively enabling auto-compounding of their rewards <a class="yt-timestamp" data-t="20:50:00">[20:50:00]</a>.

### Blob Space Increase

In parallel with Max EB, the Pectra hard fork will increase the number of blobs per block by 50% <a class="yt-timestamp" data-t="21:50:00">[21:50:00]</a>. The average number of blobs will go from three to six per block, with a maximum of nine in worst-case scenarios <a class="yt-timestamp" data-t="21:58:00">[21:58:00]</a>. Any bandwidth savings from Max EB, combined with other execution layer bandwidth cuts, can be directly translated into more scale for data, which powers [[The importance of Ethereums layer 1 and layer 2 dynamics | Ethereum's Layer 2s]] <a class="yt-timestamp" data-t="22:23:00">[22:23:00]</a>.

### EIP-7702 (Account Abstraction)

EIP-7702 is the first in-protocol version of account abstraction on [[Ethereum Layer 1 versus Layer 2 dynamics | Ethereum]] <a class="yt-timestamp" data-t="29:17:00">[29:17:00]</a>. This feature allows users to delegate smart contract functionality to their existing Externally Owned Addresses (EOAs) <a class="yt-timestamp" data-t="29:41:00">[29:41:00]</a>.

*   **Plugin Model**: It functions like a "plugin" for an EOA, allowing users to choose and change which smart wallet features (e.g., multi-signature security like a Safe, auto-approvals, social recovery) they want to use without changing their address or private key <a class="yt-timestamp" data-t="30:40:00">[30:40:00]</a>.
*   **Security Considerations**: The design ensures that delegating to a plugin on one chain does not automatically affect assets on other chains, prioritizing security <a class="yt-timestamp" data-t="34:07:00">[34:07:00]</a>.
*   **Future Scope**: While not a "silver bullet," EIP-7702 addresses most user use cases for smart accounts and lays the groundwork for future improvements, such as paying gas with non-ETH tokens or changing private keys <a class="yt-timestamp" data-t="35:52:00">[35:52:00]</a>. It provides a standard for [[The importance of Ethereums layer 1 and layer 2 dynamics | Layer 2s]] which have previously built their own fragmented solutions <a class="yt-timestamp" data-t="36:52:00">[36:52:00]</a>.

### Pectra Timeline

Pectra is currently in the testnet phase <a class="yt-timestamp" data-t="38:49:00">[38:49:00]</a>. Testing on Sepolia and Holesky testnets encountered minor configuration issues that caused delays <a class="yt-timestamp" data-t="39:06:00">[39:06:00]</a>. A new testnet, "Hoodie," was launched to allow staking pools and other complex setups to test the entire lifecycle, ensuring features like Max EB and withdrawal processing work correctly <a class="yt-timestamp" data-t="41:03:00">[41:03:00]</a>. The Petra hard fork on Hoodie is expected by March 26th <a class="yt-timestamp" data-t="41:48:00">[41:48:00]</a>. Assuming smooth testing, the earliest mainnet activation for Pectra is projected for late April, with May being the base case <a class="yt-timestamp" data-t="42:31:00">[42:31:00]</a>.

## Fusaka Hard Fork (Targeted 2025)

The Fusaka hard fork is a major [[Ethereum upgrades for 2025 | Ethereum upgrade]] targeted for 2025, with core development work already underway for over a year <a class="yt-timestamp" data-t="46:48:00">[46:48:00]</a>. There is a strong desire within the community to see a larger blob increase before the end of 2025 <a class="yt-timestamp" data-t="47:27:00">[47:27:00]</a>.

### PIEDAS (Proposer-Builder Separation for Data Availability Sampling)

PIEDAS is a significant qualitative leap for [[Ethereums strategic pivot and scaling layer 1 efforts | Ethereum's scaling]] efforts <a class="yt-timestamp" data-t="26:09:00">[26:09:00]</a>. While blobs provide data that is deleted after a few weeks, PIEDAS aims to change how this data is stored <a class="yt-timestamp" data-t="26:31:00">[26:31:00]</a>.

*   **Subset Storage**: Instead of every node storing all blob data, PIEDAS would allow every node to store only a subset of the data <a class="yt-timestamp" data-t="26:18:00">[26:18:00]</a>.
*   **Cryptographic Verification**: Nodes would use cryptography to check that other nodes on the network possess the remaining data, with high probabilistic guarantees <a class="yt-timestamp" data-t="26:56:00">[26:56:00]</a>.
*   **10x Scaling**: This change would effectively increase data availability by 10x with the same amount of bandwidth, potentially targeting an average of 48 blobs per block, up from 6 in Pectra <a class="yt-timestamp" data-t="27:21:00">[27:21:00]</a>.

### EOF (Ethereum Object Format)

EOF is a major overhaul of the Ethereum Virtual Machine (EVM), described as upgrading the EVM from a "1950s computer" to a "1990s computer" <a class="yt-timestamp" data-t="56:06:00">[56:06:00]</a>.

*   **Code and Data Separation**: A key improvement is the separation of code and data within EVM contracts, which simplifies tooling and analysis <a class="yt-timestamp" data-t="57:06:00">[57:06:00]</a>.
*   **Developer Experience**: It introduces specific opcodes to make writing compilers and programming languages on top of the EVM easier <a class="yt-timestamp" data-t="57:28:00">[57:28:00]</a>.
*   **New Contract Types**: EOF introduces a versioned type of EVM, allowing for new types of contracts to opt-in to these improvements. This enables the removal of problematic old functionalities and better data management without breaking existing contracts <a class="yt-timestamp" data-t="57:58:00">[57:58:00]</a>.
*   **Security and Auditing**: It also aids in security by making it easier to analyze and audit contract behavior, especially in edge cases <a class="yt-timestamp" data-t="59:13:00">[59:13:00]</a>.

### Aggressive Scaling Appetite

There is a "renewed focus" and "accelerating" interest among core developers in more aggressive [[Ethereums strategic pivot and scaling layer 1 efforts | scaling]] efforts <a class="yt-timestamp" data-t="52:43:00">[52:43:00]</a>. Vitalik Buterin has specifically called for Fusaka to ship with PIEDAS and target 48 blobs per block in 2025 <a class="yt-timestamp" data-t="49:20:00">[49:20:00]</a>. This indicates a shift towards prioritizing scaling as one of the few key objectives in the short term <a class="yt-timestamp" data-t="53:08:00">[53:08:00]</a>.

## Glamsterdam and Future Outlook

Glamsterdam is a placeholder name for the hard fork after Fusaka <a class="yt-timestamp" data-t="01:01:48:00">[01:01:48:00]</a>. The goal for future hard forks is to improve parallelization of planning and implementation <a class="yt-timestamp" data-t="01:02:06:00">[01:02:06:00]</a>. The aim is to finalize the scope for a hard fork months in advance so that teams can begin prototyping as soon as the previous fork is shipped, streamlining the upgrade process <a class="yt-timestamp" data-t="01:03:00:00">[01:03:00:00]</a>.

## Scaling the Layer 1 (Execution Layer)

Scaling the [[Ethereum Layer 1 versus Layer 2 dynamics | Ethereum Layer 1]] (execution layer) involves increasing gas throughput or adjusting block times <a class="yt-timestamp" data-t="01:08:52:00">[01:08:52:00]</a>. This is a complex challenge with many variables, unlike the more straightforward scaling of blobs on the consensus layer <a class="yt-timestamp" data-t="01:10:52:00">[01:10:52:00]</a>.

*   **Bottlenecks**: State growth and history growth are identified bottlenecks, with recent research showing state growth might be less of an immediate issue than previously thought <a class="yt-timestamp" data-t="01:09:26:00">[01:09:26:00]</a>.
*   **Repricing Opcodes**: Efforts are being made to reprice opcodes to make certain operations cheaper, allowing for more transactions within the same gas limit <a class="yt-timestamp" data-t="01:10:20:00">[01:10:20:00]</a>.
*   **MEV's Impact**: The increasing role of Maximal Extractable Value (MEV) has led to blocks being built at the last possible second, reducing time for verification. Solutions, such as delaying block verification to the next slot, are being explored to leverage the ecosystem's architecture for L1 scaling <a class="yt-timestamp" data-t="01:12:17:00">[01:12:17:00]</a>.

## Interoperability and Layer 2 Fragmentation

While short-term solutions for [[The importance of Ethereums layer 1 and layer 2 dynamics | Layer 2]] interoperability and fragmentation are largely addressed at the application and wallet levels (e.g., via EIP-7702) <a class="yt-timestamp" data-t="01:14:01:00">[01:14:01:00]</a>, long-term protocol-level solutions are being considered by core developers <a class="yt-timestamp" data-t="01:14:07:00">[01:14:07:00]</a>. Ideas like "native rollups" with common pre-compiles could enable better interoperability and L1 guarantees <a class="yt-timestamp" data-t="01:14:09:00">[01:14:09:00]</a>. However, such changes are highly complex and would take years to design, test, and implement due to the diverse architectures of existing rollups <a class="yt-timestamp" data-t="01:14:25:00">[01:14:25:00]</a>.

## Summer of Protocols

Summer of Protocols is an initiative that funds researchers, teachers, and educators to study and formalize the understanding of "protocols" <a class="yt-timestamp" data-t="01:17:00:00">[01:17:00:00]</a>. The program aims to create a unified explanation of how protocols work, drawing parallels from various domains (e.g., cryptography, wildfire management, plurality voting) <a class="yt-timestamp" data-t="01:17:39:00">[01:17:39:00]</a>. The goal is to provide frameworks for working with protocols, similar to how economics has supply and demand models, and to help better understand [[Ethereum ecosystem and leadership changes | Ethereum]] as a protocol <a class="yt-timestamp" data-t="01:17:56:00">[01:17:56:00]</a>. This initiative, run by Vanites Raal and Timber Shoff in 2025, aims to organize existing knowledge into online courses, books, and classes <a class="yt-timestamp" data-t="01:18:05:00">[01:18:05:00]</a>.