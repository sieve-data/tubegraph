---
title: Common Methods of Multifactor Authentication
videoId: jD6P--7rUy8
---

From: [[thepipeline_xyz]] <br/> 

[[understanding_multifactor_authentication_and_its_risks | MFA]], or [[introduction_to_multifactor_authentication | multifactor authentication]], is a security measure that adds a second method of verification beyond a password to confirm a user's identity for an account <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This additional step ensures that the person attempting to access an account is truly who they claim to be <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Types of Multifactor Authentication

Several common methods are used for [[understanding_multifactor_authentication_and_its_risks | MFA]]:

### Biometric Verification
This method uses unique physical or behavioral characteristics to verify identity <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
*   **Face ID** is a very common [[biometric_methods_for_authentication | biometric]] means of [[understanding_multifactor_authentication_and_its_risks | MFA]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

### Hardware Keys
This involves using a physical device to authenticate identity <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   A "key" can be used to confirm identity <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

### Authenticator Applications
These applications generate time-sensitive [[security_considerations_for_authentication_codes | codes]] that users provide after entering their password <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
*   Ideally, the authenticated software for generating these [[security_considerations_for_authentication_codes | codes]] should be on a secondary device, not the same phone being actively used <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

### Text Message Codes (SMS)
This is a widely used, yet less secure, method where a [[security_considerations_for_authentication_codes | code]] is sent to a user's phone via text message after they sign in with their password <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   It is considered a very dangerous method <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   The vectors for [[verification_and_compromise_on_digital_platforms | compromise]] increase exponentially if someone gains consistent access to your phone or the [[security_considerations_for_authentication_codes | code]] through methods like a SIM swap <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   Choosing not to use [[risks_of_using_text_codes_for_authentication | text codes]] can prevent significant personal and financial loss <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

> [!warning] Dangers of Text Message Codes
> Using text message [[security_considerations_for_authentication_codes | codes]] for authentication is a very dangerous method due to increased vectors for [[verification_and_compromise_on_digital_platforms | compromise]], such as SIM swaps or direct phone access <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.