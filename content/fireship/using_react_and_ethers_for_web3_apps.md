---
title: Using React and Ethers for Web3 apps
videoId: meTpMP0J5E8
---

From: [[fireship]] <br/> 

Developing decentralized web applications (dApps) on the blockchain involves creating a frontend interface that interacts with smart contracts. This guide focuses on building such applications using [[react_hooks_explanation | React]] for the frontend and Ethers.js for blockchain interaction <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Overview of a Web3 Application <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>

A typical Web3 application, especially one involving NFTs, involves several key components:
*   **Frontend**: Built with a framework like [[react_hooks_explanation | React]] to provide the user interface <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Smart Contracts**: Written in Solidity, these define the logic and rules for blockchain interactions, such as minting NFTs or handling payments <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Blockchain Interaction Library**: Ethers.js facilitates communication between the frontend JavaScript and the smart contracts on the blockchain <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   **Wallet Integration**: Browser plugins like MetaMask allow users to manage their cryptocurrency and approve transactions <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
*   **Off-chain Storage**: For large data like NFT images and metadata, the [[interplanetary_file_system | IPFS]] (InterPlanetary File System) is used <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

## Project Setup <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>

To begin, you can generate a new [[react_hooks_explanation | React]] application using a tool like Vit <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. While other frontend frameworks can be used, [[react_hooks_explanation | React]] is widely adopted in Web3 demos <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

Next, integrate Hardhat into your project by running `npx hardhat` <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. Hardhat provides tools for blockchain backend development, including:
*   A `contracts` directory for Solidity files <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   A `scripts` directory for deploying contracts <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

### Configuration for React Interaction

To allow [[react_hooks_explanation | React]] to access smart contract information, update the `hardhat.config` file to generate contract artifacts (like the Application Binary Interface, or ABI) in the [[react_hooks_explanation | React]] application's source directory <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. The ABI acts as a bridge, enabling JavaScript to communicate with the compiled smart contract <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

Install necessary npm dependencies, including `ethers`, which is crucial for browser-based smart contract interactions <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

## Smart Contract Interaction with Ethers.js <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>

Ethers.js is a JavaScript library that simplifies communication with the Ethereum blockchain and smart contracts <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.

### Key Concepts for Ethers.js

1.  **Contract ABI**: Import the contract's ABI from the `artifacts` directory <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>. This JSON file describes the contract's functions and how to interact with them.
2.  **Contract Address**: Obtain the address where your smart contract is deployed on the blockchain <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.
3.  **Web3 Provider**: Instantiate a Web3 provider (e.g., `new ethers.providers.Web3Provider(window.ethereum)`) to connect to the blockchain via the user's MetaMask plugin <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>. The provider offers methods for interacting with the blockchain <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.
4.  **Signer**: Get a signer from the provider to execute transactions on the blockchain <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>. The signer represents the user's connected wallet.
5.  **Contract Instance**: Instantiate the contract using its address, ABI, and the signer: `new ethers.Contract(contractAddress, contractABI, signer)` <a class="yt-timestamp" data-t="00:18:33">[00:18:33]</a>. This instance allows you to call the contract's methods.

### Example Interactions

*   **Getting Wallet Balance**: Use `provider.getBalance(account)` to retrieve the connected account's balance <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. Ethers.js also provides utilities to format large number values <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

    ```javascript
    import { ethers } from 'ethers';
    // ...
    const getBalance = async () => {
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      const account = accounts[0];
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const balance = await provider.getBalance(account);
      setBalance(ethers.utils.formatEther(balance)); // Update React state
    };
    ```
*   **Calling Smart Contract Methods**:
    *   **Reading Data (e.g., `getCount()`, `isContentOwned()`):**
        To get the current number of minted tokens, call the `count` method on your contract instance <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>.
        To check if an NFT has been minted, call `isContentOwned(uri)` <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>.

        ```javascript
        import { ethers } from 'ethers';
        import ContractABI from './artifacts/contracts/YourContract.json'; // Path to your ABI

        const contractAddress = "YOUR_DEPLOYED_CONTRACT_ADDRESS";

        // ... inside a React component
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const contract = new ethers.Contract(contractAddress, ContractABI.abi, provider); // Use provider for read-only
        const count = await contract.count();
        const isMinted = await contract.isContentOwned(metadataURI);
        ```
    *   **Writing Data (e.g., `payToMint()`):**
        To mint a token, call the `payToMint` method on your contract instance, passing the recipient's address, the metadata URI, and the `value` (amount of Ether to send) <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>. This requires a `signer` for the contract instance.

        ```javascript
        const signer = provider.getSigner();
        const contractWithSigner = new ethers.Contract(contractAddress, ContractABI.abi, signer);

        const transaction = await contractWithSigner.payToMint(recipientAddress, metadataURI, {
          value: ethers.utils.parseEther("0.05") // Example: 0.05 Ether
        });
        await transaction.wait(); // Wait for the transaction to be mined
        ```
        This code is very similar to what you would write in a unit test for your smart contract <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.

## Wallet Integration (MetaMask) <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>

For users to interact with your dApp, they typically need a browser plugin like MetaMask <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.

*   **Checking for MetaMask**: You can check if MetaMask (or a similar Web3 provider) is installed by inspecting the `window.ethereum` object <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
*   **Connecting to MetaMask**: When a user clicks to interact, MetaMask will prompt them to confirm transactions, displaying details like the amount of Ether to transfer <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.

## Deployment to Testnets <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>

Before deploying to the expensive Ethereum mainnet, it's recommended to deploy your dApp to a testnet <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.

*   **Alchemy**: Services like Alchemy can help deploy your contract to a testnet <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>. You can create an application on Alchemy, selecting a chain (e.g., Polygon) and network (e.g., Polygon Mumbai) <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.
*   **Hardhat Configuration**: Update your `hardhat.config` file with a new network entry, including the Alchemy URL and your MetaMask account's private key (needed for deploying the contract) <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>.
*   **Testnet Funds**: Obtain free test cryptocurrency (e.g., Matic for Polygon Mumbai) from a faucet by providing your public wallet address <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.
*   **Deployment Command**: Run `npx hardhat run scripts/sample-script.js --network matic` (or your chosen network name) to deploy your contract to the testnet <a class="yt-timestamp" data-t="00:22:49">[00:22:49]</a>. Copy the deployed contract address and update it in your frontend code <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>.