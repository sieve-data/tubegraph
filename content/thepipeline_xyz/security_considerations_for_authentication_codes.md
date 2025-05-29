---
title: Security Considerations for Authentication Codes
videoId: jD6P--7rUy8
---

From: [[thepipeline_xyz]] <br/> 

[[Introduction to Multifactor Authentication | Multifactor authentication]] (MFA) involves adding a second method beyond a password to verify a user's identity for an account <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This supplementary verification ensures that the person attempting to access an account is indeed the rightful owner <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## [[Common Methods of Multifactor Authentication | Common Authentication Methods]]

Several methods are used for MFA to enhance account security:
*   **Biometric Authentication** Face ID is a widely used biometric method for MFA <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
*   **Hardware Keys** Physical keys can be used to confirm identity as part of the authentication process <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Authenticator Applications** These applications generate codes that users provide after entering their password <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Ideally, this authenticated software should reside on a secondary device, separate from the one actively being used for login <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## [[Risks of Using Text Codes for Authentication | Risks of SMS-Based Authentication]]

While convenient, receiving authentication codes via text message (SMS) is considered a dangerous method for MFA <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Many users are unaware of the significant security risks associated with this common practice <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

The ease of use, such as automatically filling a text code on an iPhone, belies the inherent vulnerabilities <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The vectors for compromise increase exponentially if an attacker gains consistent access to these codes <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This can occur through methods like a SIM swap or direct access to the user's phone <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Relying on text message codes puts personal and financial security at significant risk <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.