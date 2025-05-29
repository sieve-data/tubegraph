---
title: Introduction to MultiFactor Authentication
videoId: jD6P--7rUy8
---

From: [[thepipeline_xyz]] <br/> 

[[importance_of_multifactor_authentication_mfa | MultiFactor Authentication]] ([[importance_of_multifactor_authentication_mfa | MFA]]) is a security measure designed to verify a user's identity beyond a simple password <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It involves using a second method to confirm that you are who you claim to be when accessing an account, such as a Gmail or bank account <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Types of MultiFactor Authentication

Various methods can be employed for [[importance_of_multifactor_authentication_mfa | MFA]]:

*   **[[Biometric Methods for MFA | Biometric]] Authentication**
    *   This includes features like Face ID, which has become a very common means of [[importance_of_multifactor_authentication_mfa | MFA]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
*   **[[Hardware Keys in MultiFactor Authentication | Hardware Keys]]**
    *   Physical keys can be used to confirm identity <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **[[Authenticator Apps and Best Practices | Authenticator Apps]]**
    *   These apps provide a code that users supply after entering their password <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Ideally, the authenticator software should be on a secondary device to prevent compromise if the primary device is accessed <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   **Text Message Codes**
    *   While widely used and seemingly convenient, this method involves receiving a code via text message, for example, when signing into a bank account <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

### Risks of Using Text Message Codes for Authentication

Using text message codes for authentication is considered a very dangerous method <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. The vectors for compromise increase exponentially if someone gains consistent access to these codes, possibly through a SIM swap or direct access to your phone <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. Not taking the extra step to avoid text message codes can lead to significant financial or personal data loss <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.