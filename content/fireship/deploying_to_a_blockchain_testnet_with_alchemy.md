---
title: Deploying to a blockchain testnet with Alchemy
videoId: meTpMP0J5E8
---

From: [[fireship]] <br/> 

To see how a decentralized application (DApp) would work in the real world, it's possible to deploy it to a testnet, even though deploying to the Ethereum mainnet would be costly <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>.

## Why use a Testnet?
Deploying to a testnet allows developers to test their [[building_a_web3_nft_app | Web3]] applications and smart contracts in an environment that mimics the live blockchain without incurring real financial costs <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.

## Utilizing Alchemy for Deployment
Alchemy is a free tool that helps with deploying to a testnet <a class="yt-timestamp" data-t="00:21:30">[00:21:30]</a>. Serious [[web3_and_decentralized_internet | Web3]] applications often use platforms like Alchemy and Infura to make decentralized apps more reliable <a class="yt-timestamp" data-t="00:21:33">[00:21:33]</a>.

### Step-by-Step Deployment
1.  **Create an Alchemy Account and Application**: Upon creating an account, you will be given the option to create a new application <a class="yt-timestamp" data-t="00:21:45">[00:21:45]</a>.
2.  **Select Blockchain and Network**: For this tutorial, the Polygon chain with the Polygon Mumbai Network was used <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>. Polygon is a blockchain built on top of Ethereum, known for being faster and less expensive <a class="yt-timestamp" data-t="00:21:53">[00:21:53]</a>. Its native token, MATIC, is similar to Ether <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>.
3.  **Obtain Network URL**: Once the application is created, Alchemy provides a link to the network, which needs to be copied <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.
4.  **Configure Hardhat**:
    *   Open the `hardhat.config` file in your source code <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>.
    *   Add a new entry under `networks`, specifically for `matic`, and point it to the URL copied from Alchemy <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.
    *   Include a private key for your account, as this account will be responsible for deploying the contract <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>.
5.  **Set up MetaMask**:
    *   Install MetaMask if not already installed <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.
    *   Switch the MetaMask network to Mumbai <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.
    *   Export your private key from MetaMask by going to Account Details and Exporting it <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.
    *   Paste this private key into the Hardhat config file <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>.
6.  **Acquire Testnet Funds**: Deploying a contract incurs a cost, and initially, your wallet will have zero MATIC <a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>. To get free test money, visit the Polygon faucet and add your public wallet address <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>. After a few minutes, MATIC should appear in your wallet <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.
7.  **Run Deployment Script**: From the terminal, run the Hardhat deploy script, ensuring the network option is set to `Matic` <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>.
    ```bash
    npx hardhat run scripts/sample-script.js --network Matic
    ```
    This will deploy the contract to the Mumbai Network <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>.
8.  **Update Frontend Code**: Copy the deployed contract address and update it in your frontend code, typically in the `main.jsx` file <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>.

After these steps, your [[building_a_web3_nft_app | Web3]] application will be running on the testnet <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>, and the same basic process can be followed for deploying to the mainnet <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.