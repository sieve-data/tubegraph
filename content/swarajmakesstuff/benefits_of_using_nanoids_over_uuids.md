---
title: Benefits of using Nanoids over UUIDs
videoId: toszy9D3kgE
---

From: [[swarajmakesstuff]] <br/> 

While [[drawbacks_of_using_uuids_in_web_applications | UUIDs]] (Universally Unique Identifiers) have been widely used to generate unique identifiers, they present significant drawbacks when applied to modern [[drawbacks_of_using_uuids_in_web_applications | web applications]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These issues make alternatives like [[comparison_of_uuids_cuids_and_nanoids | Nanoids]] a more suitable choice <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.

## Drawbacks of UUIDs

UUIDs are 128-bit labels, commonly seen in a hyphenated format <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. They are excellent for generating unique identifiers, with a very low probability of duplication, even when generating millions <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>. However, their design makes them unsuitable for many modern uses:

*   **Excessive Length and Space** <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>: UUIDs are long, consuming considerable space in databases <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>.
*   **Poor Readability and Usability** <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a>: They result in long and complex URLs that are difficult to read, write, or type <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.
*   **Misaligned Purpose** <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>: UUIDs were primarily created for operating systems and network protocols, where the size and format of identifiers are not critical <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>. This contrasts with [[drawbacks_of_using_uuids_in_web_applications | web applications]] that require consideration for performance, readability, scalability, and size <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. UUIDs generally fail to meet these requirements <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>.

## Introducing Nanoids as an Alternative

[[introduction_to_cuids_as_an_alternative_to_uuids | Nanoids]] (and [[introduction_to_cuids_as_an_alternative_to_uuids | CUIDs]]) are innovative ways to generate unique identifiers that overcome the limitations of UUIDs <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.

[[introduction_to_cuids_as_an_alternative_to_uuids | Nanoids]] are similar to UUIDs but generate unique identifiers with a fixed length and using predefined alphabets <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

## Benefits of Nanoids over UUIDs

[[use_cases_and_efficiency_of_cuids_and_nanoids | Nanoids]] offer several advantages making them highly suitable for [[drawbacks_of_using_uuids_in_web_applications | web applications]]:

*   **Shorter and Fixed Length**: Nanoids generate unique identifiers within a fixed, often shorter, length <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. This makes them more compact and user-friendly for URLs and database storage.
*   **Controlled Collision Probability**: While UUIDs have an extremely low collision probability, the practical collision risk for Nanoids is often negligible given typical usage patterns <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>. For example, generating a 9-character Nanoid at a rate of 1,000 IDs per second continuously for two years results in only a 1% probability of a collision <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>. This is a significantly more practical timeframe than the 126 years it might take for a UUID to experience a similar collision risk <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.
*   **Performance Efficient**: Their design allows for better performance in [[drawbacks_of_using_uuids_in_web_applications | web applications]] where every bit of efficiency matters <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

## Implementation

For those setting up their own applications, [[use_cases_and_efficiency_of_cuids_and_nanoids | Nanoids]] can be easily implemented by installing the `nanoid` library <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>. If using Prisma, [[introduction_to_cuids_as_an_alternative_to_uuids | CUIDs]] are directly supported <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>.

Given the practical advantages in performance, readability, and efficient use of space, it is advisable to consider [[comparison_of_uuids_cuids_and_nanoids | Nanoids]] or [[introduction_to_cuids_as_an_alternative_to_uuids | CUIDs]] over UUIDs for modern [[drawbacks_of_using_uuids_in_web_applications | web applications]] <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>.