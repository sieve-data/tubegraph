---
title: Authenticator Apps and Best Practices
videoId: jD6P--7rUy8
---

From: [[thepipeline_xyz]] <br/> 

[[introduction_to_multifactor_authentication | MultiFactor Authentication (MFA)]] is a security measure where an account, typically protected by a password, requires a second verification method to confirm a user's identity <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

### Types of MFA

Common methods of MFA include:
*   **Biometric authentication** Face ID is a common example of this type of MFA <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
*   **[[Hardware Keys in MultiFactor Authentication | Hardware keys]]** These are physical devices used to verify identity <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   **Authenticator apps** These applications provide a code after a user signs in with their password <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
*   **Text message codes** A common method where a code is sent via text to verify identity <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

### Best Practices for Authenticator Apps

For enhanced security, the code provided by an authenticator app should ideally not reside on the same phone actively being used for the login <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. The authenticated software should ideally be on a secondary device <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

### [[risks_of_using_text_message_codes_for_authentication | Risks of Using Text Message Codes]]

While convenient, using text message codes for authentication is a very dangerous method <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. The vectors for compromise increase exponentially if someone gains consistent access to your code, whether through a SIM swap or direct access to your phone <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. Not taking the extra step to avoid using text message codes can lead to significant personal and financial loss <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.