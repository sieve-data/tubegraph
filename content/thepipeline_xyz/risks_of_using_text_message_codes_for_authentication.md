---
title: Risks of Using Text Message Codes for Authentication
videoId: jD6P--7rUy8
---

From: [[thepipeline_xyz]] <br/> 

While text message (SMS) codes are a common method for [[introduction_to_multifactor_authentication|MultiFactor Authentication]] (MFA), they are considered a dangerous method due to significant [[risks_of_unauthorized_access_and_social_engineering|vectors for compromise]] <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Although simple and easy to use, allowing for quick logins <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, this method significantly increases the risk of unauthorized access <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## How Text Message Codes Work
Typically, when signing into an account, such as a bank account, after entering a password, a code is sent via text message to a linked phone number <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. This code is then entered to verify the user's identity <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Primary Risks
The primary risk stems from the ease with which bad actors can gain access to these codes <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>:

*   **SIM Swaps**
    A SIM swap involves an attacker convincing a mobile carrier to transfer a victim's phone number to a SIM card they control <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Once the attacker has control of the phone number, they can receive all text messages, including [[introduction_to_multifactor_authentication|MFA]] codes, enabling them to bypass security measures for various accounts <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
*   **Direct Phone Access**
    If an attacker gains direct physical or remote access to a user's phone, they can intercept incoming text message codes <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Consequences of Compromise
When an attacker gains consistent access to these codes, the [[risks_of_unauthorized_access_and_social_engineering|vectors of compromise]] increase exponentially <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This can lead to severe consequences, such as an individual having their entire life or all their money taken away <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

> [!CAUTION]
> Using text message codes as a form of authentication is a "very dangerous method" because the [[risks_of_unauthorized_access_and_social_engineering|vectors for compromise]] can "increase exponentially" through methods like a SIM swap or direct phone access <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

For enhanced security, it is recommended to avoid using text message codes and instead opt for more secure [[introduction_to_multifactor_authentication|MFA]] methods like biometric verification (e.g., Face ID), [[hardware_keys_in_multifactor_authentication|hardware keys]], or dedicated [[authenticator_apps_and_best_practices|authenticator apps]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. These alternatives offer a higher level of protection against [[risks_associated_with_phishing_and_social_engineering_attacks|social engineering attacks]] and unauthorized access.