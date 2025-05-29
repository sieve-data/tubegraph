---
title: Multifactor authentication MFA and its importance
videoId: Edya6gkz6-4
---

From: [[thepipeline_xyz]] <br/> 

## What is MFA?
[[what_is_MFA | Multifactor authentication (MFA)]], also known as two-factor authentication (TFA), provides a second method to verify a user's identity beyond just a password [0:11:14 | 0:11:26]. This second factor ensures that you are who you claim to be when accessing an account [0:11:26].

## Why MFA is Crucial, Especially in Crypto
The crypto space is described as one of the most "ripe ecosystems for exploits and hacks" due to the presence of programmable money [0:02:07]. It combines traditional Web2 attack vectors, such as phishing, web exploits, network issues, and cloud security, with Smart Contract execution issues [0:02:39].

Given this volatile environment, implementing [[what_is_MFA | MFA]] is one of the most critical steps users can take to protect their funds, important data, and access points [0:06:41]. It significantly reduces the possibility of compromise [0:03:03].

## Types of MFA

### Recommended Methods
*   **[[Hardware keys in MFA | Hardware Keys]]**: Physical keys, such as U Keys, serve as a second verification method, making it nearly impossible for an attacker to gain access without physical possession of the key [0:07:59 | 0:08:21].
*   **[[Authenticator apps for MFA | Authenticator Applications]]**: Apps like Google Authenticator generate time-based codes [0:08:28]. Ideally, this software should be on a secondary device, separate from the one actively being used [0:11:50]. Users should back up their codes and store them prudently [0:08:31].
*   **[[Biometric methods in MFA | Biometric Methods]]**: Technologies like Face ID are becoming common means of [[what_is_MFA | MFA]] [0:11:31 | 0:31:32].

### Methods to Avoid
*   **SMS-based MFA**: Using text message codes for [[what_is_MFA | MFA]] is highly dangerous [0:06:53].
    *   If a phone number is compromised via a [[risks_of_using_text_message_codes_for_MFA | SIM swap attack]], attackers gain access to all accounts linked to SMS-based [[what_is_MFA | MFA]], including Google accounts, exchanges, and bank accounts [0:07:01 | 0:07:22].
    *   Access to a Google account with SMS-based [[what_is_MFA | MFA]] can expose password history, login credentials, and search history, effectively giving an attacker a user's entire online life [0:07:27 | 0:07:51].
    *   The ease and simplicity of SMS codes lead users into a dangerous method of authentication [0:12:11 | 0:12:27].

## Risks and Attacks Against MFA
While crucial, [[what_is_MFA | MFA]] is not entirely "bulletproof" against sophisticated social engineering [0:39:03].

*   **Prompt Bombing**: Attackers can continuously spam an authenticator app with approval requests [0:34:10 | 0:34:27]. This can lead to an employee approving a request out of fatigue or confusion, especially when timed with daily routines [0:34:51 | 0:35:10].
*   **Man-in-the-Middle Attacks (Public Wi-Fi)**: Connecting to malicious Wi-Fi access points, such as those disguised as legitimate public Wi-Fi (e.g., Starbucks Wi-Fi), allows attackers to monitor traffic [0:35:50 | 0:36:19]. When a user logs in with their password and [[what_is_MFA | MFA]] code, the attacker can capture these credentials and replay the session, gaining full access to the account [0:36:22 | 0:36:35]. Public Wi-Fi, even with a VPN, is considered dangerous [0:36:37 | 0:37:32].
*   **Service Desk Social Engineering**: Attackers can gather enough information about a user to repeatedly contact service desks (e.g., for Twitter accounts, phone carriers) and impersonate the user [0:37:40 | 0:38:25]. By spamming recovery requests, they can trick inadequately trained service associates into resetting passwords or granting access, leading to a [[risks_of_using_text_message_codes_for_MFA | SIM swap]] or account compromise [0:37:50 | 0:38:25]. It's advisable to set up strong access codes with phone providers and explicitly inform them not to grant access under any circumstances [0:39:09 | 0:39:12].

## General Security Advice for [[data_and_credential_management | Data and Credential Management]]
*   **Self-Audit**: Regularly conduct a critical self-audit to identify all points of failure, including funds, access points, and sensitive [[data_and_credential_management | credentials]] [0:03:25 | 0:04:32]. Create an "attack surface map" and mitigate risks [0:04:36 | 0:04:43].
*   **Password Managers**: If using a password manager, choose a credible one like Bitwarden [0:08:48 | 0:08:53]. Avoid those known for compromises, such as LastPass [0:08:41 | 0:08:47].
*   **Air-gapped Storage**: Strongly consider storing sensitive information, such as recovery codes or keys, air-gapped on physical pieces of paper or in a crypto capsule [0:08:57 | 0:09:04]. Never put private keys online [0:13:47].
*   **Wallet Management**:
    *   Use [[Multisig key compromise | cold wallets]] as much as possible, as their private keys are offline and thus more secure [0:10:00 | 0:13:08].
    *   Avoid storing significant funds on hot wallets, which are always connected to the internet and susceptible to fishing attacks [0:10:05 | 0:10:13].
    *   Consider having a burner wallet, a trading wallet, and a separate storage wallet, in addition to a cold wallet [0:10:13 | 0:10:22].
    *   Back up recovery phrases or keys securely [0:13:42].
*   **Software Updates**: Keep all software up-to-date, including Twitter, Discord, operating systems, and browsers, to avoid vulnerabilities [0:10:42 | 0:11:00]. Enable automatic updates [0:10:59].
*   **Combat Overconfidence**: Overconfidence is a significant risk [0:05:00 | 0:17:25]. Always assume you are a target and that attackers are highly sophisticated [0:17:29 | 0:32:28]. Be "schizophrenic and paranoid" about security [0:00:24 | 0:17:43].
*   **Verify Before Trusting**:
    *   Be cautious of spoofed websites, especially those appearing as ads in search results [0:18:19 | 0:19:14].
    *   Bookmark frequently used, legitimate websites [0:16:34].
    *   Scrutinize domain names for subtle changes (e.g., "rn" for "m", "l" for "I") [0:19:50 | 0:20:14].
    *   Do not click links in emails for password resets; go directly to the official website [0:20:57 | 0:21:09].
    *   Verify sources for any online interaction [0:16:39 | 0:20:38].
*   **Chrome Extensions**: Be careful about downloading Chrome extensions, as they can be malicious and access cookies or credentials [0:21:55 | 0:22:28]. Audit installed extensions and remove any unrecognized ones or those that do not need access [0:22:37 | 0:22:58].
*   **Spear Phishing**: Be wary of unsolicited direct messages (DMs) offering job offers or consultations, especially if they contain links [0:23:03 | 0:23:41]. Never download executables or test games from unknown sources [0:24:20 | 0:24:32].
*   **Malicious Documents**: PDF and Word documents (`.docx`) can contain "macros" that execute malicious code [0:24:42 | 0:25:04]. Use services like DangerZone.rocks to safely process PDFs [0:25:20 | 0:25:28].
*   **Mobile Device Security**: While phones may be less susceptible to some malware due to isolated environments, a compromised iCloud account can lead to complete data loss [0:25:40 | 0:26:10].
*   **Telegram & Discord Security**: Be prudent about who DMs you, especially those impersonating support staff [0:26:27 | 0:26:38]. Verify usernames and be cautious of links in group chats, even if they appear to come from legitimate figures, as accounts can be mimicked [0:27:40 | 0:28:03].
*   **Urgency Exploitation**: Attackers often capitalize on a sense of urgency, prompting users to click links without verification [0:28:51 | 0:29:13]. Take a deep breath and verify before acting [0:29:38 | 0:29:43].
*   **Address Poisoning Attacks**: Be aware of attackers monitoring transactions and sending small amounts to addresses very similar to frequently used ones (e.g., your own wallets) [0:39:28 | 0:40:07]. This can trick users into copying and pasting the malicious address, leading to funds being sent to the wrong place [0:40:07 | 0:40:33]. Always verify the entire address when copying and pasting [0:40:53 | 0:40:57].
*   **User Education**: The crypto space needs better user education on security [0:48:54]. Resources like the "fishing.ether.games" quiz by Tincho Abate (The Red Guild) and security guides by Tavono and Officer CIA are highly recommended for learning about crypto security [0:41:30 | 0:42:26 | 0:49:04 | 0:49:42].
*   **Human Error**: Human error, driven by chasing gains or being tired, is a significant danger [0:45:48 | 0:50:48]. Maintaining emotional regulation and a "Zen" mindset can help prevent mistakes [0:51:02 | 0:51:04].

> "You don't want to be the guy that has his whole life taken away from him or all his money taken away from him because you didn't want to go the extra step." <a class="yt-timestamp" data-t="0:00:29">[0:00:29]</a>
> "In general, like right now what protocols and just people in general should be doing is like you just have to lock down your accounts as much as you can." <a class="yt-timestamp" data-t="0:53:47">[0:53:47]</a>

## Improving User Experience in Crypto
While security is paramount and often requires user vigilance, efforts are being made to improve user experience (UX) to make interactions with blockchains safer and simpler. [[Challenges in Crypto Onboarding and Simplifying User Experience | Account abstraction]], for instance, introduces changes that make interacting with blockchain accounts simpler for end-users, potentially allowing for [[Biometric methods in MFA | Face ID]] sign-ins or other more intuitive verification methods [0:31:08 | 0:31:34]. Fuse Wallet is cited as an example, offering "two points of failure versus one," akin to needing both a key and biometric identification to access a house [0:30:35 | 0:31:01].

However, despite these advancements, the inherent risk in the crypto space remains [0:31:44]. The mindset should be one of constant vigilance, recognizing that you are a target with money online [0:32:10 | 0:32:24]. Attackers are sophisticated and willing to invest significant resources for high returns, making vigilance essential [0:28:24 | 0:28:40].