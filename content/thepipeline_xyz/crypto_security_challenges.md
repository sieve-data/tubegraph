---
title: Crypto security challenges
videoId: Edya6gkz6-4
---

From: [[thepipeline_xyz]] <br/> 

The crypto space is one of the most susceptible ecosystems globally for exploits and hacks, making it a prime target for malicious actors [00:02:07]. It combines traditional Web2 attack vectors with unique blockchain-specific vulnerabilities, placing users between "two massive pillars and constantly getting crushed" if not careful [00:02:52]. Omar, a former pentester and red teamer specializing in open-source intelligence gathering, and a former blockchain security engineer at Coinbase, highlights that individuals should assume they are targets and be as "schizophrenic and paranoid as possible" when navigating the on-chain world [00:00:24].

## Attacker Targets

Attackers typically target three core areas [00:03:30]:
*   **Funds**: Whatever is stored on-chain, centralized exchanges (CEXes), or wallets [00:03:35].
*   **Access**: The ability to use a compromised individual as an interception point to people around them, such as colleagues, friends, or family [00:03:44]. For public figures, this access can be leveraged for spear phishing campaigns [00:04:03].
*   **Data**: Sensitive credentials stored anywhere that require rigorous auditing [00:04:16].

## Major Risks to the Average Crypto User

Statistically, phishing is the most common and versatile attack vector [00:14:57]. Omar emphasizes that overconfidence, fatigue, or being "tilted" (emotionally compromised) can lead to critical mistakes [00:05:00].

### Phishing and Spoofing Attacks
*   **Website Spoofing**: Attackers create websites that look nearly identical to legitimate ones to trick users into approving malicious transactions or entering credentials [00:18:22]. They often purchase ad space on search engines (e.g., Google) so their spoofed sites appear as top results for common searches like "Uniswap" [00:18:48].
*   **Domain Spoofing**: Attackers create similar-looking domain names by swapping characters (e.g., lowercase 'r' and 'n' to look like 'm', or 'l' and 'I') to trick users into thinking they are interacting with official sources [00:19:50]. This can happen in email links or comments on official social media posts [00:20:14].
*   **Spear Phishing**: Highly targeted attacks, often through DMs on platforms like Twitter or Discord, offering job opportunities, consulting, or meeting invites [00:23:05]. These often include malicious links or executables [00:23:41].
    *   **Case Study: Y22 Trader**: A notable trader's Twitter account was mimicked by an attacker, including post history and follower count, to direct users to a fake Telegram group. This group prompted users to verify on a desktop browser, leading to the compromise of hot wallets [00:26:50]. Attackers even used fake "gold check marks" to appear legitimate [00:28:06].

### Smart Contract Execution Risk
Vulnerabilities in smart contracts pose a significant risk, especially for users interacting frequently with decentralized applications [00:15:39]. Users unfamiliar with code should be extremely cautious about the contracts they transact with and avoid taking unnecessary risks [00:16:01].

### Outdated Software and Malicious Extensions
*   **Operating System/Browser Vulnerabilities**: Not updating operating systems, browsers, or applications can leave users susceptible to known exploits and zero-day vulnerabilities [00:16:52].
*   **Malicious Chrome Extensions**: Extensions can be malicious, gaining access to cookies or credentials [00:22:01]. Attackers may pay influencers or create positive reviews to hide their malicious intent [00:22:11]. Users should audit and remove any unrecognized extensions [00:22:37].

### Malicious Documents
Email attachments like `.docx` or PDF files can contain macros that execute malicious code upon opening [00:24:47]. A tool like [dangerzone.rocks](dangerzone.rocks) can help check PDFs for safety [00:25:22].

### Public Wi-Fi and QR Codes
*   **Public Wi-Fi**: Using public Wi-Fi networks (e.g., at Starbucks or airports) is highly risky [00:32:57]. Attackers can set up malicious access points that mimic legitimate networks, intercepting login credentials and MFA codes through man-in-the-middle attacks [00:36:02]. Even with a VPN, this practice is compared to "standing in like a massive burning bonfire" [00:33:36].
*   **QR Codes**: Scanning random QR codes, particularly in public places like airports, is also a dangerous practice [00:32:51].
*   **Crypto Conferences**: These are "very dangerous targets" for attackers [00:37:09]. Users should be extra cautious about Wi-Fi connections and device security [00:37:17].

### Address Poisoning Attacks
This occurs when an attacker sends a small transaction to a user's wallet from an address that looks very similar to one the user frequently interacts with (e.g., their own secondary wallet) [00:39:28]. The attacker manipulates the first and last few characters of the address to closely match the legitimate one, hoping the user will copy the wrong address from their transaction history when sending funds [00:40:05].

## Practical Steps for Enhanced Crypto Security ([[best_practices_for_crypto_security | Best Practices for Crypto Security]])

### 1. Multi-Factor Authentication (MFA)
*   **Implement MFA Everywhere**: All accounts holding funds, important data, or access should have MFA enabled [00:06:47].
*   **Avoid SMS-Based MFA**: SMS-based MFA is highly vulnerable to SIM swap attacks, where attackers gain control of your phone number and, subsequently, your accounts (Google, exchanges, bank accounts) [00:06:57].
*   **Prioritize Hardware-Based MFA**: Use physical security keys like YubiKeys. This ensures that even if compromised via SIM swap, an attacker cannot access your accounts without the physical key [00:07:55].
*   **Use Authenticator Apps**: If hardware MFA isn't possible, use apps like Google Authenticator, ideally on a secondary device [00:08:28]. Back up your codes securely [00:08:31].
*   **Understand MFA Compromises**: MFA is not bulletproof [00:39:03].
    *   **Prompt Bombing**: Attackers can spam an authenticator app with requests, hoping the user accidentally approves one, especially when fatigued or distracted [00:34:10].
    *   **Man-in-the-Middle on Public Wi-Fi**: As described above, attackers can intercept MFA codes along with usernames and passwords on compromised public networks [00:36:19].
    *   **Social Engineering Service Desks**: Attackers gather information on targets and then use it to impersonate them to service desk employees (e.g., phone carriers, social media support) to gain access or reset passwords [00:37:44].

### 2. Wallet Strategy
*   **Prioritize [[best_practices_for_crypto_security | Cold Wallets]]**: A cold wallet stores private keys offline, making them immune to online hacks [00:13:01]. All significant trading and long-term storage should be done on cold wallets [00:13:29].
*   **Minimize [[best_practices_for_crypto_security | Hot Wallet]] Usage**: Hot wallets are online and convenient for quick transactions but are much riskier [00:13:20]. Never keep substantial funds on a hot wallet [00:14:23].
*   **Segregate Funds**: Ideally, use a burner wallet, a trading wallet, and a storage wallet, with cold wallets in the background [00:10:17].
*   **Secure Recovery Phrases**: Always back up recovery phrases/keys for cold wallets, never online [00:13:42]. Store them physically in a safe, fireproof place [00:13:51].

### 3. General Security Practices
*   **Critical Self-Audit**: Regularly inventory all potential points of failure in your digital life (funds, access, data, credentials) [00:03:25].
*   **Secure Recovery Methods**: Lock down account recovery methods with phone providers (e.g., access codes) to prevent SIM swaps [00:09:13].
*   **Password Managers**: If using a password manager, choose a credible one like Bitwarden [00:08:53]. Consider air-gapping credentials by storing them on physical paper [00:08:57].
*   **Regular Updates**: Keep all software (operating system, browser, applications like Twitter, Discord) automatically updated to patch vulnerabilities [00:10:40].
*   **Verify Before Trusting**: Always check the source of links, emails, and information [00:20:38]. If unsure, copy and paste links for dissection, or navigate directly to official websites instead of clicking embedded links [00:20:48].
*   **Caution with Downloads**: Never download or execute untrusted files, especially games or executables from unknown sources [00:24:20].
*   **Be Paranoid**: Maintain a mindset that you are a target and attackers are highly sophisticated. Humility in security is crucial [00:17:25].

> [!NOTE] Resources for Further Learning
> *   **Lumos**: [chainlight.io](http://chainlight.io/) for visualizing attack vectors [00:14:45].
> *   **Danger Zone**: [dangerzone.rocks](http://dangerzone.rocks/) for safely analyzing PDFs [00:25:22].
> *   **Phishing Quiz**: [therkt.games](http://therkt.games/) (by Tincho Abate of The Red Guild) offers a practical quiz on crypto phishing [00:41:46].
> *   **Crypto Security Guides**: Tavallino (via Medium) and Officer CIA (for OSINT, Telegram, Discord security) provide excellent resources [00:49:04].

## Evolution and Future of Crypto Security

The crypto industry is maturing, and there are ongoing efforts to improve user experience (UX) and security, particularly through **Account Abstraction** [00:48:50]. This technology aims to simplify interactions with blockchain accounts, offering features like multi-factor authentication (e.g., face ID) as a second verification method, akin to having multiple keys to a house [00:30:22]. Fuse Wallet is an example of a project implementing such improvements, providing more points of failure for attackers than traditional single-key hot wallets [00:30:35].

Despite these innovations, Omar emphasizes that users should **always remain vigilant and terrified** of potential threats [00:31:57]. The fundamental nature of crypto involves programmable money, making it inherently attractive to malicious actors, including nation-states like North Korea's Lazarus Group, who are "advanced persistent threats" [00:53:00]. The industry's constant interaction with money means the likelihood of compromise is significantly higher than in traditional web security [00:54:48].

> [!CAUTION] Human Error is Understated
> The psychological aspect of security, such as chasing "dopamine" from quick gains or insider scoops, can lead to human error. Regulating emotions and maintaining a "Zen" approach is crucial to avoid impulsive, risky actions [00:50:48].