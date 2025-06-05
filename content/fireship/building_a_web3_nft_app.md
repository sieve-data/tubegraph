---
title: Building a Web3 NFT app
videoId: meTpMP0J5E8
---

From: [[fireship]] <br/> 

This article outlines the complete process of building a [[web3_and_decentralized_internet | Web3]] NFT application from scratch <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It covers the creation of digital artwork, uploading it to a decentralized file system, writing a smart contract, and building a front-end interface <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## What is an NFT Collection?

A Non-Fungible Token (NFT) is a unique digital asset, typically representing artwork like an image, but also potentially domain names or physical items <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. NFTs are often packaged in collections, such as CryptoPunks, Bored Ape Yacht Club, and Doodles <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.

These graphics are created by combining multiple base layers (e.g., hair, eyes, clothing) randomly to generate unique images <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. Traits and attributes within these graphics have varying levels of rarity, making some generated NFTs less likely to possess rare traits <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

A smart contract acts like a vending machine in the cloud for NFT collections <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>. When crypto is sent to its wallet address, it mints a unique token and transfers it to the user's wallet <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. Owning an NFT with rare traits is analogous to getting a rare Pokémon card from a pack <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>.

After purchase, NFTs can be resold on a secondary market like OpenSea <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>. Original creators can configure their smart contracts to receive royalty payments whenever the NFT changes hands in the future <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.

> [!WARNING] Potential Downsides of [[web3_and_decentralized_internet | Web3]]
> Despite the perceived decentralization and trustless nature of [[web3_and_decentralized_internet | Web3]], much of it relies on centralized APIs <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. An example highlighted is an NFT whose appearance changes based on where it's viewed (cool on OpenSea, but like "poop" in the wallet), because the image is hosted off-chain on a web server that displays different images based on the user agent <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.

## Phase 1: Creating NFT Artwork

The first phase involves creating the layers or graphics for the NFT collection <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. This process allows taking a few basic images and combining them to create thousands of unique combinations <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>.

The example uses hand-drawn artwork, digitized and brought into Figma with categories for traits like hair, eyes, nose, mouth, and beard <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. A small script in [[building_and_deploying_a_nodejs_full_stack_application | Node.js]] randomly combines these layers <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>. Many existing tools can generate NFT collections without code, but this tutorial focuses on the code-based approach <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.

### Artwork Generation Process

1.  **Layers Directory**: Contains individual SVG files for each layer (e.g., `i z eyes 1`, `I 2`) <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>. SVG is used, but PNGs are also common <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>.
2.  **`index.js` (Node.js Script)**:
    *   Uses an SVG template with comments as placeholders for layers <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>.
    *   Reads content from layer files using [[building_and_deploying_a_nodejs_full_stack_application | Node.js]] <a class="yt-timestamp" data-t="04:35:00">[04:35:00]</a>.
    *   A `createImage` function generates random numbers to combine layers into an array <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>. This is a recursive function that checks for duplicate combinations <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.
    *   Replaces comments in the SVG template with actual layer content <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.
3.  **Metadata Generation**: Creates a JSON file for each image containing its name, a link to its image on the Interplanetary File System (IPFS), and attributes of its traits <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>. The rarity of traits contributes to an NFT's value <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>.
4.  **File System Output**: Writes image files and JSON metadata to a designated output directory <a class="yt-timestamp" data-t="05:33:00">[05:33:00]</a>. SVGs are also converted to PNGs using the `sharp` [[building_and_deploying_a_nodejs_full_stack_application | Node.js]] package <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.
5.  **Execution**: A `while` loop calls the `createImage` function for the desired number of images <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>. Running the script with `node` generates an `out` directory with images and JSON files <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.

## Storing Files on IPFS

The actual image data and JSON metadata for NFTs are too large for efficient storage on the blockchain <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>. Instead, they are stored off-chain on the Interplanetary File System (IPFS), a decentralized file system similar to BitTorrent <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>.

IPFS handles content addressability, meaning each uploaded file receives a unique identifier <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>. This allows verification of the authenticity of NFT graphics, as a file cannot be modified without changing its content identifier <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>. When minting an NFT, only a link to the file's content identifier needs to be stored <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>.

Pinata is a free solution for uploading files to IPFS, similar to Dropbox <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>. It allows uploading individual files or entire directories, generating a Content Identifier (CID) for each <a class="yt-timestamp" data-t="07:20:00">[07:20:00]</a>. Pinata also offers a [[building_and_deploying_a_nodejs_full_stack_application | Node.js]] SDK for programmatic uploads <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>.

## Building the Full Stack [[web3_and_decentralized_internet | Web3]] Application

The application stack includes Solidity for smart contracts, Hardhat for development tools, and [[using_react_and_ethers_for_web3_apps | React]] for the front end <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>.

1.  **Frontend Setup**:
    *   A new [[using_react_and_ethers_for_web3_apps | React]] app is generated using Vit <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>.
    *   Although other frameworks could be used, [[using_react_and_ethers_for_web3_apps | React]] is prevalent in [[web3_and_decentralized_internet | Web3]] demos <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>.

2.  **Blockchain Backend Setup (Hardhat)**:
    *   `npx hardhat` adds tools for the blockchain backend <a class="yt-timestamp" data-t="07:48:00">[07:48:00]</a>.
    *   It creates a `contracts` directory for Solidity smart contract code <a class="yt-timestamp" data-t="07:56:00">[07:56:00]</a>.
    *   It also creates a `scripts` directory for contract deployment code <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>.
    *   The `hardhat.config` file's `paths` option is updated to create artifacts in the [[using_react_and_ethers_for_web3_apps | React]] app's `source` directory, allowing [[using_react_and_ethers_for_web3_apps | React]] to access smart contract information <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>.
    *   Compiling a smart contract generates an Application Binary Interface (ABI), which acts as a middleman for [[building_a_todo_app_with_different_javascript_frameworks | JavaScript]] to communicate with the compiled smart contract <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>. This ABI is found in the `artifacts` directory <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>.
    *   Dependencies are installed using npm, including Waffle for testing, [[using_react_and_ethers_for_web3_apps | Ethers.js]] for browser interaction with smart contracts, and OpenZeppelin for standard smart contract templates <a class="yt-timestamp" data-t="08:36:00">[08:36:00]</a>.

## Smart Contract Development

The smart contract's purpose is to accept payment, mint a non-fungible token, and transfer it to the user's wallet <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>. Handling randomness for NFT image traits directly in a smart contract is difficult; most collections generate images off-chain, upload to IPFS, and then mint them <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>. Solutions like Chainlink can implement randomness if needed <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>.

The tutorial takes a simpler approach where the smart contract takes an IPFS URL for metadata and some Ethereum to mint a new token <a class="yt-timestamp" data-t="09:29:00">[09:29:00]</a>. Solidity is the programming language used for smart contracts <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>.

### Using OpenZeppelin

Instead of writing a smart contract from scratch, OpenZeppelin provides a wizard to generate reliable, industry-standard code <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>.

*   The ERC 721 standard is used for non-fungible tokens <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a> (ERC 20 is for fungible tokens like custom coins <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>).
*   Base contracts include methods like `balanceOf` (check owner's balance), `ownerOf` (see token owner), and `transfer` functions <a class="yt-timestamp" data-t="10:16:00">[10:16:00]</a>.
*   Customizations via OpenZeppelin wizard:
    *   **Minting**: Adds a method allowing a privileged account to create new tokens <a class="yt-timestamp" data-t="10:35:00">[10:35:00]</a>.
    *   **Auto Increment IDs**: Increments token IDs <a class="yt-timestamp" data-t="10:43:00">[10:43:00]</a>.
    *   **URI Storage**: Associates an IPFS upload (metadata reference) when a token is minted <a class="yt-timestamp" data-t="10:45:00">[10:45:00]</a>.
    *   **Base URI**: Points to IPFS to ensure proper URI formatting <a class="yt-timestamp" data-t="10:56:00">[10:56:00]</a>.

### Customizing the Contract (`PayToMint`)

The generated code is copied into a Solidity file <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>. The contract is extended to allow anyone to mint a token by transferring the appropriate amount of Ethereum <a class="yt-timestamp" data-t="11:22:00">[11:22:00]</a>.

*   A new `payToMint` function is created <a class="yt-timestamp" data-t="11:35:00">[11:35:00]</a>. It takes a recipient and metadata content ID, then mints a new token <a class="yt-timestamp" data-t="11:37:00">[11:37:00]</a>.
*   **Validation**:
    *   A mapping of strings to integers tracks existing minted URIs to prevent duplicate minting <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>.
    *   An `isContentOwned` function checks if a URI already exists <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>.
    *   The `payToMint` function is marked `payable`, allowing money transfer into the contract <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>.
    *   `require` keyword is used for validation:
        *   Checks if the URI has already been minted <a class="yt-timestamp" data-t="12:23:00">[12:23:00]</a>.
        *   Checks if the user has paid enough Ether (e.g., `0.05` Ether, using `msg.value`) <a class="yt-timestamp" data-t="12:36:00">[12:36:00]</a>.
*   **Minting Logic**:
    *   A new `Item ID` is created using OpenZeppelin's counter, incrementing by one for each token <a class="yt-timestamp" data-t="12:53:00">[12:53:00]</a>.
    *   The mapping of existing URIs is updated <a class="yt-timestamp" data-t="13:03:00">[13:03:00]</a>.
    *   The built-in `mint` method is called with the recipient's wallet address <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.
    *   The token URI is set on that ID <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>.
*   A `getCurrentCount` function is added to track minted tokens <a class="yt-timestamp" data-t="13:16:00">[13:16:00]</a>.

## Testing Smart Contracts

Testing smart contracts is crucial before building the [[web3_and_decentralized_internet | Web3]] application <a class="yt-timestamp" data-t="13:28:00">[13:28:00]</a>. Hardhat provides a sample test, and test code is similar to frontend [[building_a_todo_app_with_different_javascript_frameworks | JavaScript]] code <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a>.

*   Tests use [[using_react_and_ethers_for_web3_apps | Ethers.js]] to get and deploy the contract <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.
*   Fake wallets with 10,000 Ether can be created by running `npx hardhat node` in the terminal, which sets up a mock network on localhost <a class="yt-timestamp" data-t="13:57:00">[13:57:00]</a>.
*   Tests call methods on the deployed smart contract, such as `balanceOf` to check a recipient's balance <a class="yt-timestamp" data-t="14:13:00">[14:13:00]</a>.
*   The `payToMint` method can be called with a recipient and metadata URI, and a specified Ether value (e.g., `0.05` Ether) <a class="yt-timestamp" data-t="14:31:00">[14:31:00]</a>.
*   Tests can verify expected outcomes, like a failing test if insufficient Ether is paid, and then pass once the correct amount is provided and the token is mined <a class="yt-timestamp" data-t="14:46:00">[14:46:00]</a>.

## Building the [[web3_and_decentralized_internet | Web3]] Frontend

This phase involves building the [[web3_and_decentralized_internet | Web3]] application with [[using_react_and_ethers_for_web3_apps | React]] that interacts with the smart contract <a class="yt-timestamp" data-t="15:22:00">[15:22:00]</a>.

1.  **Contract Compilation and Deployment**:
    *   The Hardhat sample script is updated with the custom contract name <a class="yt-timestamp" data-t="15:27:00">[15:27:00]</a>.
    *   `npx hardhat node` must be running in the background <a class="yt-timestamp" data-t="15:44:00">[15:44:00]</a>.
    *   `npx hardhat compile` runs the Solidity compiler to convert code into binary and populates the `artifacts` directory with the ABI <a class="yt-timestamp" data-t="15:51:00">[15:51:00]</a>.
    *   `npx hardhat run scripts sample script --network localhost` deploys the contract to the local network <a class="yt-timestamp" data-t="15:59:00">[15:59:00]</a>.
    *   The deployed contract address is copied from the terminal output and set as a global variable in the frontend code <a class="yt-timestamp" data-t="16:09:00">[16:09:00]</a>.

2.  **MetaMask Integration**:
    *   End users interact with smart contracts via browser plugins like MetaMask <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>.
    *   MetaMask needs to be set up with one of Hardhat's testing addresses by importing an account using a private key from the `npx hardhat node` output <a class="yt-timestamp" data-t="16:18:00">[16:18:00]</a>.
    *   The [[using_react_and_ethers_for_web3_apps | React]] app checks for the `window.ethereum` object to determine if MetaMask is installed, rendering different components (`Home` or `Install`) accordingly <a class="yt-timestamp" data-t="16:34:00">[16:34:00]</a>.

3.  **Interacting with Wallet and Contract using [[using_react_and_ethers_for_web3_apps | Ethers.js]]**:
    *   The `WalletBalance` component uses [[using_react_and_ethers_for_web3_apps | Ethers.js]], a [[building_a_todo_app_with_different_javascript_frameworks | JavaScript]] library, to communicate between the smart contract and the user's wallet <a class="yt-timestamp" data-t="17:03:00">[17:03:00]</a>.
    *   **Getting Wallet Balance**:
        *   The `getConnectedAccount` is obtained from `window.ethereum` <a class="yt-timestamp" data-t="17:22:00">[17:22:00]</a>.
        *   A new [[web3_and_decentralized_internet | Web3]] provider is created using [[using_react_and_ethers_for_web3_apps | Ethers.js]] <a class="yt-timestamp" data-t="17:25:00">[17:25:00]</a>.
        *   `provider.getBalance(account)` returns the wallet balance, which is then formatted and displayed <a class="yt-timestamp" data-t="17:29:00">[17:29:00]</a>.
    *   **Interacting with Smart Contract**:
        *   The contract ABI is imported from the `artifacts` directory <a class="yt-timestamp" data-t="18:10:00">[18:10:00]</a>.
        *   A [[web3_and_decentralized_internet | Web3]] provider is instantiated, and `provider.getSigner()` is used to execute blockchain transactions <a class="yt-timestamp" data-t="18:27:00">[18:27:00]</a>.
        *   `new ethers.Contract(address, ABI, signer)` instantiates the contract <a class="yt-timestamp" data-t="18:33:00">[18:33:00]</a>.
        *   The application loops through NFT images, each with a button to mint or view its token URI <a class="yt-timestamp" data-t="18:39:00">[18:39:00]</a>.
        *   `getMCount` function calls the `contract.count` method to know how many tokens have been minted <a class="yt-timestamp" data-t="18:50:00">[18:50:00]</a>.
        *   An `NFTImage` component displays each image, using the Pinata Content ID combined with the token ID to reference the JSON metadata URI <a class="yt-timestamp" data-t="19:10:00">[19:10:00]</a>. Local image references were used due to unreliability of Pinata Cloud Gateway <a class="yt-timestamp" data-t="19:32:00">[19:32:00]</a>.
        *   `getMintedStatus` runs the `isContentOwned` method on the smart contract to check if a metadata URI has been minted <a class="yt-timestamp" data-t="19:42:00">[19:42:00]</a>.
        *   **Minting Logic in Frontend**:
            *   A `mintToken` function connects the contract with the signer to access the recipient's wallet <a class="yt-timestamp" data-t="20:00:00">[20:00:00]</a>.
            *   It calls `contract.payToMint` with the recipient's address, metadata URI, and an object specifying the `value` of Ether to pay (e.g., `0.05` Ether) <a class="yt-timestamp" data-t="20:09:00">[20:09:00]</a>.
            *   The transaction result is awaited, and `getMintedStatus` is called again to update the UI <a class="yt-timestamp" data-t="20:32:00">[20:32:00]</a>.
        *   Conditional logic in JSX shows the image URI if minted, or a placeholder and a "Mint" button if not, otherwise indicating "NFT is taken" <a class="yt-timestamp" data-t="20:42:00">[20:42:00]</a>.
    *   Running `npm run dev` serves the app locally <a class="yt-timestamp" data-t="17:56:00">[17:56:00]</a>.

## Deployment

Deploying the app to a test net allows testing in a real-world scenario without incurring mainnet costs <a class="yt-timestamp" data-t="21:20:00">[21:20:00]</a>. Alchemy is a free tool for this <a class="yt-timestamp" data-t="21:30:00">[21:30:00]</a>, often used alongside Infura by serious [[web3_and_decentralized_internet | Web3]] applications to improve reliability <a class="yt-timestamp" data-t="21:34:00">[21:34:00]</a>.

### Deployment Steps:

1.  **Alchemy Setup**:
    *   Create an Alchemy account and a new application <a class="yt-timestamp" data-t="21:41:00">[21:41:00]</a>.
    *   Select a chain (e.g., Polygon) and network (e.g., Polygon Mumbai Testnet) <a class="yt-timestamp" data-t="21:48:00">[21:48:00]</a>. Polygon is a faster, less expensive Ethereum layer-2 blockchain using MATIC, similar to Ether <a class="yt-timestamp" data-t="21:53:00">[21:53:00]</a>.
    *   Copy the provided network URL <a class="yt-timestamp" data-t="22:04:00">[22:04:00]</a>.
2.  **Hardhat Configuration**:
    *   In `hardhat.config` file, add a new entry under `networks` for the chosen network (e.g., `matic`), pointing to the Alchemy URL <a class="yt-timestamp" data-t="22:08:00">[22:08:00]</a>.
    *   Export the private key from your MetaMask account (switched to the testnet, e.g., Mumbai) and paste it into the Hardhat config <a class="yt-timestamp" data-t="22:16:00">[22:16:00]</a>. This account will deploy the contract <a class="yt-timestamp" data-t="22:27:00">[22:27:00]</a>.
3.  **Get Test Funds**:
    *   Contract deployment is not free. To get free test money (e.g., MATIC), go to the Polygon Faucet and add your public wallet address <a class="yt-timestamp" data-t="22:33:00">[22:33:00]</a>.
4.  **Deploy Contract**:
    *   From the terminal, run `npx hardhat deploy script --network matic` (or your chosen network) <a class="yt-timestamp" data-t="22:47:00">[22:47:00]</a>.
    *   Copy the deployed contract address and update it in your frontend code (e.g., in `main.jsx`) <a class="yt-timestamp" data-t="22:56:00">[22:56:00]</a>.

This completes the deployment of a basic [[web3_and_decentralized_internet | Web3]] application to a testnet <a class="yt-timestamp" data-t="23:01:00">[23:01:00]</a>. The same process can be followed for deploying to the mainnet <a class="yt-timestamp" data-t="23:05:00">[23:05:00]</a>.