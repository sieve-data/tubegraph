---
title: Comparison between hot wallet and cold wallet
videoId: HnWCHbrUHf8
---

From: [[goingonchain]] <br/> 

The debate around using hot versus cold wallets is significant in the crypto community, particularly on platforms like Twitter <a class="yt-timestamp" data-t="01:12:06">[01:12:06]</a>. Understanding the differences between these [[types_of_crypto_wallets | types of crypto wallets]] is crucial for protecting digital assets.

## Wallet Hacking Incidents

Various hacking incidents highlight the risks associated with cryptocurrency wallets:
*   The founder of Defiance Capital lost $1.6 million in a hot wallet hack <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. The founder suspected the exploit was due to phishing and noted that using a hot wallet on a mobile phone was not safe enough <a class="yt-timestamp" data-t="00:27:54">[00:27:54]</a>.
*   Other incidents include compromised laptops, scams, and users signing malicious transactions <a class="yt-timestamp" data-t="00:43:08">[00:43:08]</a>.
*   A MetaMask Chrome extension hack resulted in a loss of 400 ETH <a class="yt-timestamp" data-t="00:52:25">[00:52:25]</a>.
*   A phishing attack led to $1.7 million in NFTs being stolen <a class="yt-timestamp" data-t="01:01:05">[01:01:05]</a>.

## Hot Wallets

Hot wallets are always connected to the internet <a class="yt-timestamp" data-t="01:22:04">[01:22:04]</a>.
*   **Examples:** MetaMask <a class="yt-timestamp" data-t="01:26:34">[01:26:34]</a> and [[trust_wallet_app_risks | Trust Wallet]] <a class="yt-timestamp" data-t="01:29:08">[01:29:08]</a>.
*   **Security Concerns:** Mobile phone hot wallets are generally not considered safe enough <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>. Phishing is a common method for exploiting hot wallets <a class="yt-timestamp" data-t="00:38:09">[00:38:09]</a>.

## Cold Wallets

Cold wallets are not connected to the internet, providing a higher level of [[security_features_of_crypto_wallets | security]] <a class="yt-timestamp" data-t="01:32:02">[01:32:02]</a>.
*   **Examples:** Hardware devices like Ledger, which typically cost around $200+ <a class="yt-timestamp" data-t="02:00:08">[02:00:08]</a>.
*   **Enhanced Security:** When used with a hot wallet like MetaMask, a hardware device turns it into a cold wallet because transactions require signing on the Ledger device <a class="yt-timestamp" data-t="01:37:34">[01:37:34]</a>. This process of signing on the hardware device makes transactions more secure <a class="yt-timestamp" data-t="09:21:49">[09:21:49]</a>.
*   **Limitations:** A hardware device cannot protect against the owner's mistake if they sign a malicious contract <a class="yt-timestamp" data-t="01:51:30">[01:51:30]</a>.

## Multi-Wallet Strategy

Some users employ a strategy of owning multiple wallet addresses to manage risk <a class="yt-timestamp" data-t="02:10:04">[02:10:04]</a>. For example, one might have:
*   A wallet for trading <a class="yt-timestamp" data-t="02:19:15">[02:19:15]</a>
*   A wallet for DeFi activities <a class="yt-timestamp" data-t="02:21:18">[02:21:18]</a>
*   A wallet for buying NFTs <a class="yt-timestamp" data-t="02:24:43">[02:24:43]</a>
*   A wallet for storing assets <a class="yt-timestamp" data-t="02:27:07">[02:27:07]</a>
*   A wallet for testing or demos <a class="yt-timestamp" data-t="02:29:56">[02:29:56]</a>

## Smart Wallets: Argent Example

[[features_of_argent_smart_wallet | Argent]] is an example of a smart contract wallet, which differs from traditional hot or cold wallets <a class="yt-timestamp" data-t="02:44:09">[02:44:09]</a>. It is written on a smart contract, allowing for programmable features <a class="yt-timestamp" data-t="02:54:19">[02:54:19]</a>.

### Features of Argent

*   **Customizable Security:** Users can set up:
    *   **Multisig:** Requiring multiple approvals for transactions <a class="yt-timestamp" data-t="03:09:07">[03:09:07]</a>.
    *   **Transfer Limits:** Setting a maximum amount that can be transferred <a class="yt-timestamp" data-t="03:11:06">[03:11:06]</a>.
    *   **Approved Addresses:** Pre-approving specific addresses for sending funds <a class="yt-timestamp" data-t="03:13:08">[03:13:08]</a>. These options are typically not available on wallets like MetaMask <a class="yt-timestamp" data-t="03:19:02">[03:19:02]</a>.
    *   **Guardians:** Trusted third parties (or multisig signers) can help approve transactions (especially for untrusted addresses), recover the wallet, or instantly lock it if a mobile phone is compromised <a class="yt-timestamp" data-t="04:53:11">[04:53:11]</a>.
    *   **Token Allowance:** Set how much a user can spend <a class="yt-timestamp" data-t="06:01:43">[06:01:43]</a>.
*   **Open Source:** Argent's source code and contracts are open source <a class="yt-timestamp" data-t="03:30:11">[03:30:11]</a>.
*   **Wallet Connect Compatibility:** Works with Wallet Connect <a class="yt-timestamp" data-t="03:37:09">[03:37:09]</a>.
*   **Network Compatibility:** Primarily on Ethereum and zkSync <a class="yt-timestamp" data-t="03:42:06">[03:42:06]</a>.
*   **Integrated DeFi:** Allows users to trade tokens, stake, and invest in index funds or stablecoin yields directly within the wallet, bringing DeFi functionalities to the user rather than requiring them to seek out different protocols <a class="yt-timestamp" data-t="06:39:41">[06:39:41]</a>.

### Downsides of Argent

*   **Fees:** Being a smart contract wallet, it incurs network fees for several actions:
    *   **Activation:** A surcharge is required to activate the wallet, which is essentially deploying a smart contract <a class="yt-timestamp" data-t="02:59:02">[02:59:02]</a>. This fee can be around $44 <a class="yt-timestamp" data-t="04:42:15">[04:42:15]</a>.
    *   **Upgrades:** Upgrading features (e.g., for ERC-1155 support) also requires a network fee <a class="yt-timestamp" data-t="08:00:26">[08:00:26]</a>.
    *   **Wallet Recovery:** Recovering a lost wallet also incurs a fee <a class="yt-timestamp" data-t="08:11:07">[08:11:07]</a>.
    *   **Funding:** Funding the wallet involves moving funds from L1 (Ethereum mainnet) to L2 (zkSync), which incurs network fees depending on the ETH gas price <a class="yt-timestamp" data-t="08:26:07">[08:26:07]</a>.

## General Wallet Security Tips

*   For a more secure hot wallet alternative, consider buying a Ledger hardware device and connecting it to a hot wallet like MetaMask <a class="yt-timestamp" data-t="09:10:04">[09:10:04]</a>.
*   For extreme [[using_and_storing_in_noncustodial_wallets | security]], write down your seed phrase on paper and store it in a secure location <a class="yt-timestamp" data-t="09:29:16">[09:29:16]</a>.