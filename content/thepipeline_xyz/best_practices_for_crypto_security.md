---
title: Best practices for crypto security
videoId: Edya6gkz6-4
---

From: [[thepipeline_xyz]] <br/> 

The crypto space is highly susceptible to exploits and hacks due to the nature of programmable money <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>. It combines traditional Web2 attack vectors like phishing, web exploits, network issues, and cloud security, with Web3-specific issues like smart contract execution vulnerabilities <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>. As such, users should be extremely prudent and paranoid to avoid compromise <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.

## General Principles for Security

The most crucial step is a critical self-audit to understand your own vulnerabilities <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>. Attackers typically target three main areas:
*   **Funds**: Whatever is stored on-chain, exchanges, or wallets <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>.
*   **Access**: Using your accounts as an interception point to compromise colleagues, friends, or family <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>.
*   **Data**: Sensitive credentials and where they are stored <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>.

Users should map out all potential points of failure to identify and mitigate risks <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>. A common mistake is overconfidence, assuming familiarity with scams, which can lead to mistakes when new varieties emerge or when tired <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>. Always assume you are a target, and maintain a humble mindset regarding your knowledge compared to attackers <a class="yt-timestamp" data-t="0:21:25">[0:21:25]</a>.

## Key Security Measures

### Multi-Factor Authentication (MFA)
Enable MFA on every account that holds funds, important data, or access <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>.
*   **Avoid SMS-based MFA**: If your phone number is compromised (e.g., via a SIM swap attack), attackers gain access to accounts with SMS MFA, including Google, exchanges, and bank accounts <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>.
*   **Prefer Hardware-based MFA**: Use U2F keys (YubiKeys) for the highest level of security, as they provide a physical second verification method <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>.
*   **Authenticator Apps**: If hardware keys aren't feasible, use apps like Google Authenticator, ideally on a secondary, separate device <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>. Back up your codes securely and prudently <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>.

### Secure Recovery Methods
Ensure all accounts are recoverable and recovery methods are locked down <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>. For SIM cards, set an access code and inform your phone provider not to allow access or changes without it <a class="yt-timestamp" data-t="09:41:00">[09:41:00]</a>.

### Password Management
*   **Password Managers**: Use a credible password manager like Bitwarden <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>. Avoid those with known compromises like LastPass <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>.
*   **Air-Gapped Storage**: For highly sensitive information, consider storing it air-gapped on physical paper or in a crypto capsule, ideally in a fireproof location <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>. Never put recovery phrases or keys online for a cold wallet <a class="yt-timestamp" data-t="13:47:00">[13:47:00]</a>.

### Wallet Strategy
*   **Cold Wallets**: Use [[best_practices_for_wallet_security | cold wallets]] as much as possible, especially for significant funds. Private keys are offline, making them highly secure <a class="yt-timestamp" data-t="10:00:00">[10:00:00]</a>.
*   **Hot Wallets**: Minimize funds kept on [[best_practices_for_wallet_security | hot wallets]] because they are constantly connected to the internet, increasing their vulnerability <a class="yt-timestamp" data-t="10:05:00">[10:05:00]</a>.
*   **Segregated Wallets**: Maintain a burner wallet, a trading wallet, and a separate storage wallet. Ideally, conduct all operations from multiple [[best_practices_for_wallet_security | cold wallets]] <a class="yt-timestamp" data-t="10:13:00">[10:13:00]</a>.
*   **Multisig Wallets**: If using a multisig, ensure keys are not all accessible in one place and are stored on different hardware wallets <a class="yt-timestamp" data-t="44:21:00">[44:21:00]</a>.

### Software and System Updates
Keep all software and systems up to date, including Twitter, Discord, operating systems, and browsers <a class="yt-timestamp" data-t="10:40:00">[10:40:00]</a>. Enable automatic updates to avoid browser or operating system vulnerabilities, and protect against zero-day exploits <a class="yt-timestamp" data-t="10:57:00">[10:57:00]</a>.

## Understanding Attack Vectors

[[crypto_security_challenges | Crypto security challenges]] are diverse and constantly evolving.

### Phishing Attacks
Phishing is the most common attack vector, with threat actors becoming increasingly sophisticated, creating full-scale businesses around it <a class="yt-timestamp" data-t="14:59:00">[14:59:00]</a>.
*   **Spoofed Websites**: Be wary of websites that look legitimate but are fake <a class="yt-timestamp" data-t="18:19:00">[18:19:00]</a>. Attackers buy ad space, so clicking the first search result for a crypto service (e.g., Uniswap) can lead to a spoofed site <a class="yt-timestamp" data-t="18:48:00">[18:48:00]</a>. Always bookmark official websites and use those <a class="yt-timestamp" data-t="16:34:00">[16:34:00]</a>.
*   **Domain Spoofing**: Attackers mimic official domains using subtle visual tricks (e.g., 'rn' for 'm', 'l' for 'i') in links or email addresses <a class="yt-timestamp" data-t="19:21:00">[19:21:00]</a>. Always verify the exact domain <a class="yt-timestamp" data-t="20:19:00">[20:19:00]</a>.
*   **Email Links**: For actions like password resets, go directly to the service's website rather than clicking links in emails, even if they seem official <a class="yt-timestamp" data-t="20:57:00">[20:57:00]</a>.
*   **Spear Phishing**: Targeted attacks, often using job offers or meeting invites, can lead to malicious links that compromise your device or accounts <a class="yt-timestamp" data-t="23:03:00">[23:03:00]</a>.
*   **Malicious Downloads**: Never download executables (e.g., "test this game") <a class="yt-timestamp" data-t="24:20:00">[24:20:00]</a>. Be cautious with documents (PDFs, DOCX) as they can contain macros that execute code. Use tools like dangerzone.rocks to safely inspect PDFs <a class="yt-timestamp" data-t="24:42:00">[24:42:00]</a>.

### Smart Contract Execution Risk
Vulnerabilities in smart contracts pose a significant risk <a class="yt-timestamp" data-t="15:39:00">[15:39:00]</a>. If unfamiliar with code, be extremely prudent about which contracts you interact with <a class="yt-timestamp" data-t="15:56:00">[15:56:00]</a>.

### Address Poisoning Attacks
Attackers monitor transactions and send small amounts of crypto to addresses that look very similar to legitimate ones (matching first/last characters) <a class="yt-timestamp" data-t="39:28:00">[39:28:00]</a>. If you're not paying close attention, you might accidentally copy the malicious address from your transaction history when sending funds, leading to losses <a class="yt-timestamp" data-t="40:12:00">[40:12:00]</a>. Always use the direct source for addresses and verify them character by character <a class="yt-timestamp" data-t="40:48:00">[40:48:00]</a>.

### MFA Bypass Attacks
Even MFA can be compromised through sophisticated methods:
*   **Prompt Bombing**: Attackers repeatedly send MFA requests to your authenticator, hoping you'll approve one out of annoyance or confusion <a class="yt-timestamp" data-t="34:08:00">[34:08:00]</a>.
*   **Man-in-the-Middle (MITM) Attacks**: On public Wi-Fi (e.g., Starbucks, airports), attackers can set up malicious access points that mimic legitimate ones <a class="yt-timestamp" data-t="35:57:00">[35:57:00]</a>. When you connect and try to log in, they intercept your username, password, and MFA code, allowing them to replay your login <a class="yt-timestamp" data-t="36:11:00">[36:11:00]</a>. Avoid public Wi-Fi for crypto activities <a class="yt-timestamp" data-t="36:37:00">[36:37:00]</a>.
*   **Service Desk/SIM Swaps**: Attackers gather information about you and impersonate you to service desks (e.g., Twitter support, phone carriers) to gain control of accounts or SIM cards <a class="yt-timestamp" data-t="37:40:00">[37:40:00]</a>.

## Specific Platform/Scenario Advice

*   **Chrome Extensions**: Malicious extensions can have access to your cookies and credentials <a class="yt-timestamp" data-t="22:01:00">[22:01:00]</a>. Only download credible and trusted extensions, and regularly audit and remove any you don't recognize or that don't need access <a class="yt-timestamp" data-t="22:33:00">[22:33:00]</a>.
*   **Mobile Devices**: While phones are generally less susceptible to certain compromises due to their isolated environment, a compromised iCloud account can grant attackers access to your entire digital life <a class="yt-timestamp" data-t="25:40:00">[25:40:00]</a>.
*   **Telegram/Discord**: These platforms are rife with impersonation attempts, especially from fake support personnel <a class="yt-timestamp" data-t="26:25:00">[26:25:00]</a>. Always verify usernames and be suspicious of DMs. Never click links or download files from unverified sources <a class="yt-timestamp" data-t="26:38:00">[26:38:00]</a>.
*   **QR Codes**: Avoid scanning QR codes in public places like airports, as they can lead to malicious sites or actions <a class="yt-timestamp" data-t="32:51:00">[32:51:00]</a>.

## Recommended Resources
*   **Lumos (chainlight.io)**: A website that tracks different attack vectors in crypto <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>.
*   **Fishing.therktgames.com**: A crypto phishing quiz by Tincho Abate (The Red Guild) to test your knowledge and identify common phishing techniques <a class="yt-timestamp" data-t="41:28:00">[41:28:00]</a>.
*   **Tavano**: An "OG of crypto security" with incredible resources, including a Medium article on securing crypto <a class="yt-timestamp" data-t="49:04:00">[49:04:00]</a>.
*   **OfficerCIA**: Provides extensive resources on Telegram and Discord security <a class="yt-timestamp" data-t="49:29:00">[49:29:00]</a>.

## Mindset for Safety
*   **Verify Before Trusting**: Always verify the source and legitimacy of any link, email, or request before interacting with it <a class="yt-timestamp" data-t="20:38:00">[20:38:00]</a>. Take extra steps like asking someone or dissecting the link <a class="yt-timestamp" data-t="20:48:00">[20:48:00]</a>.
*   **Emotional Regulation**: Attackers capitalize on urgency and the desire for quick profits (e.g., "quick 23x" or "alpha") <a class="yt-timestamp" data-t="28:51:00">[28:51:00]</a>. Take a deep breath and verify; 15-30 seconds of due diligence won't significantly impact your P&L <a class="yt-timestamp" data-t="29:35:00">[29:35:00]</a>.
*   **Human Error**: Be aware that human error, especially when tired or chasing dopamine, is a significant vulnerability <a class="yt-timestamp" data-t="50:48:00">[50:48:00]</a>. Avoid making financial decisions when not fully focused, such as trading at 2 AM <a class="yt-timestamp" data-t="50:40:00">[50:40:00]</a>.
*   **Continuous Education**: Given that [[challenges_in_crypto_onboarding_and_simplifying_user_experience | user education in crypto]] is not yet where it needs to be, constantly educating yourself is crucial for improving your security <a class="yt-timestamp" data-t="48:54:00">[48:54:00]</a>.

While [[technology_and_user_experience_in_crypto_wallets | user experience and retention in crypto]] improvements like account abstraction (e.g., Fuse Wallet) are making interactions simpler and adding layers of security like two-factor verification, the fundamental truth remains: the crypto space is filled with malicious actors <a class="yt-timestamp" data-t="30:22:00">[30:22:00]</a>. Embrace a paranoid mindset and strive to reduce your risk of compromise as much as possible, as an attack will likely occur at some point <a class="yt-timestamp" data-t="31:57:00">[31:57:00]</a>.