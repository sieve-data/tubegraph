---
title: Introduction to Multifactor Authentication
videoId: jD6P--7rUy8
---

From: [[thepipeline_xyz]] <br/> 

[[Understanding MultiFactor Authentication and Its Risks | Multifactor Authentication]] (MFA) is a security measure that adds a second method of verification beyond a password to confirm a user's identity <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. It ensures that the person attempting to access an account is genuinely who they claim to be <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. For instance, in addition to a password for an account like Gmail, a second verification step is required <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## [[Common Methods of Multifactor Authentication | Common Methods of Multifactor Authentication]]

MFA can be implemented using various methods, including:
*   **[[Biometric Methods for Authentication | Biometric]]** methods, such as Face ID, which is a very common form of MFA <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
*   **Hardware** tokens, like a physical key, that identify the user <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Authenticator applications** that generate a code to be provided after entering a password <a class="yt="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Ideally, this authenticated software should reside on a secondary device, separate from the phone being actively used <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   **Text message (SMS) codes**, where a code is sent to a user's phone after they sign in to an account, such as a bank <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. This method is often perceived as easy and simple, allowing for quick logins <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

### [[Risks of Using Text Codes for Authentication | Risks of Using Text Codes for Authentication]]

While convenient, using text message codes for authentication is considered a very dangerous method <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. The vectors for compromise increase exponentially if an attacker gains consistent access to these codes, potentially through methods like a SIM swap or direct access to the user's phone <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. Neglecting to take the extra step to avoid SMS-based codes can lead to significant financial or personal loss <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.