---
title: Smart Contracts with Solidity and OpenZeppelin
videoId: meTpMP0J5E8
---

From: [[fireship]] <br/> 

A smart contract is a self-executing contract where the terms of the agreement are directly written into lines of code <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. These contracts are stored on a blockchain network and automatically execute when specific conditions are met. This article focuses on building smart contracts using [[object_oriented_programming_with_typescript | Solidity]] and OpenZeppelin, specifically for creating [[building_a_web3_nft_app | Non-Fungible Tokens (NFTs)]].

## Understanding NFT Collections and Smart Contracts

NFTs are unique digital assets, most commonly representing artwork, but can also represent domain names or physical items <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. NFT collections, like CryptoPunks or Bored Ape Yacht Club, consist of graphics created by combining various base layers (e.g., hair, eyes, clothing) randomly, resulting in unique images with different rarity levels <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

A smart contract functions like a "vending machine in the cloud" for an NFT collection <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. When a user sends cryptocurrency to the contract's wallet address, it mints a unique NFT and transfers it to the user's wallet <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Creators can also configure their smart contracts to receive royalty payments whenever the NFT is resold on a secondary market <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Storing NFT Data Off-Chain

The actual image data and JSON metadata for an NFT are typically too large to be stored efficiently directly on the blockchain <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. Instead, this data is stored "off-chain" on systems like the InterPlanetary File System (IPFS) <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

IPFS is a decentralized file system that ensures content addressability: any uploaded file receives a unique identifier that changes if the file is modified <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. This allows for verification of the authenticity of graphics associated with an NFT <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. When an NFT is minted, only a link to this file's content identifier needs to be stored on the blockchain <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Tools like Pinata can be used to upload files and directories to IPFS <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

## Building a Smart Contract with Solidity

[[object_oriented_programming_with_typescript | Solidity]] is the programming language used to write smart contracts that interact with the blockchain <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. A key purpose of these contracts is to accept payments, then mint and transfer NFTs to a user's wallet <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

### Challenges with Randomness

It is extremely difficult to handle randomness directly within a smart contract <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. Most NFT collections avoid this by generating all images and their metadata at once, uploading them to IPFS, and then minting them after the fact <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. For true on-chain randomness, external solutions like Chainlink are recommended <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

### Using OpenZeppelin for Standard Contracts

Instead of building a smart contract from scratch, which can be a significant undertaking, developers can use OpenZeppelin <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. OpenZeppelin provides a wizard to automatically generate reliable, industry-standard contract code <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

The Ethereum ecosystem defines standard interfaces for common contract requirements:
*   **ERC-20:** Used for creating fungible tokens (like a custom cryptocurrency coin) <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   **ERC-721:** Used for creating non-fungible tokens <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. This standard includes built-in methods like `balanceOf` (to check an owner's balance), `ownerOf` (to see who owns a token), and methods to transfer tokens <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

When configuring an ERC-721 contract with the OpenZeppelin wizard, key options include:
*   **Mint:** Adds a method that allows a privileged account to create a new token <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.
*   **Auto Increment IDs:** Automatically increments token IDs <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   **URI Storage:** Allows associating an IPFS upload (the metadata reference) when a token is minted <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
*   **Base URI:** Points to IPFS to ensure proper URI formatting <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

### Extending the ERC-721 Contract

To allow any user to mint a token by transferring Ethereum, the base ERC-721 contract can be extended. A custom function, such as `payToMint`, can be created <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. This function takes a recipient address and the metadata content ID, then mints a new token <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

Key aspects of the `payToMint` function:
*   **Payable:** Marked as a `payable` function, meaning users can transfer money into the contract when calling it <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
*   **Validation (`require`):** The `require` keyword is used for validation:
    *   Checks if the URI has already been minted to prevent duplicate NFTs <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.
    *   Validates that the user has paid a sufficient amount of Ether (e.g., `msg.value` is greater than a minimum) <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
*   **Minting Logic:**
    *   Creates a new item ID using OpenZeppelin's counter <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.
    *   Updates a mapping to track existing minted URIs <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
    *   Calls the built-in `_mint` method with the recipient's wallet address <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.
    *   Sets the token URI for that ID <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.
*   **`isContentOwned` function:** A helper function can be created to check if a specific URI has already been minted <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
*   **`count` function:** A function can be added to retrieve the current count of minted tokens <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

## Testing Smart Contracts

Before [[using_react_and_ethers_for_web3_apps | building a Web3 application]], it's highly recommended to test smart contracts <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. Hardhat provides tools for this <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. Testing helps detect bugs and issues early in development <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

Steps for testing:
1.  **Start a mock network:** Run `npx hardhat node` in the terminal to create a local blockchain network with fake accounts for testing <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
2.  **Deploy contract:** Use `ethers` within the test to deploy the contract <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
3.  **Use fake wallets:** Copy a public key from the hardhat node output to use a fake wallet with test Ether <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.
4.  **Call methods:** Use `ethers` to call methods on the deployed smart contract, such as `balanceOf` to check a user's NFT balance or `payToMint` to simulate a minting transaction <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.
5.  **Assert outcomes:** Use assertion libraries (like Waffle, which is installed as an npm dependency <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>) to confirm expected results, such as a balance changing after minting or a validation error if conditions are not met <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.

## Deploying Smart Contracts

After development and testing, smart contracts can be deployed to a blockchain network. For testing purposes, deployment to a testnet is common <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.

Steps for deployment using Hardhat and Alchemy:
1.  **Set up Alchemy:** Create an application on Alchemy, choosing a chain (e.g., Polygon) and a testnet (e.g., Polygon Mumbai Network) <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>. Alchemy provides platforms that make decentralized apps more reliable <a class="yt-timestamp" data-t="00:21:33">[00:21:33]</a>.
2.  **Configure Hardhat:**
    *   Add a new network entry in `hardhat.config.js` pointing to the Alchemy network URL <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>.
    *   Provide the private key of the account that will deploy the contract <a class="yt-timestamp" data-t="00:22:17">[00:22:17]</a>. This key can be exported from MetaMask after switching to the chosen testnet <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.
3.  **Get test funds:** Acquire free test cryptocurrency (e.g., Matic for Polygon Mumbai) from a faucet by providing your public wallet address <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.
4.  **Deploy:** Run the Hardhat deploy script, specifying the configured network (e.g., `npx hardhat run scripts/sample-script.js --network Matic`) <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>.
5.  **Update Frontend:** Copy the deployed contract's address and update it in your frontend code (e.g., `main.jsx` in a React app) <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>.

This process establishes a smart contract running on a public testnet, allowing interaction as it would in a real-world scenario <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. The same fundamental steps apply for deployment to a mainnet, although it would incur real costs <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.