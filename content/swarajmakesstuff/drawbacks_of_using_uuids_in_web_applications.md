---
title: Drawbacks of using UUIDs in web applications
videoId: toszy9D3kgE
---

From: [[swarajmakesstuff]] <br/> 

The conventional wisdom that [[comparison_of_uuids_cuids_and_nanoids | UUIDs]] are the best way to generate unique identifiers for web applications is challenged, with arguments made against their continued use <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. While [[comparison_of_uuids_cuids_and_nanoids | UUIDs]] are widely used and excel at preventing duplicates, they present significant drawbacks when applied to modern web environments <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## What are UUIDs?

[[comparison_of_uuids_cuids_and_nanoids | UUIDs]], or Universally Unique Identifiers, are 128-bit labels used to store information, primarily within operating systems <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. They are designed to be extremely unique, with a very low probability of duplication even when generating millions of IDs <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Reasons to Avoid UUIDs in Web Applications

Despite their uniqueness, [[comparison_of_uuids_cuids_and_nanoids | UUIDs]] have several serious drawbacks that make them unsuitable for modern web applications <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>, <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

### Excessive Length and Space Consumption
[[comparison_of_uuids_cuids_and_nanoids | UUIDs]] are notably long, which leads to several issues:
*   **Database Space**: They consume significant space in databases <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>, <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **User Interface and URLs**: Their length makes URLs cumbersome and difficult to share, read, write, or type <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>, <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This results in a complex and messy user experience <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

### Not Designed for Web Applications
A crucial point is that [[comparison_of_uuids_cuids_and_nanoids | UUIDs]] were not originally created for web applications <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>, <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. Their primary purpose was for operating systems and network protocols, where the size and format of identifiers are less critical <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>, <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

For web applications, factors like performance, readability, scalability, and identifier size are paramount <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>, <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. [[comparison_of_uuids_cuids_and_nanoids | UUIDs]] simply do not meet these modern web development requirements <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Alternatives to UUIDs

Given these limitations, modern web applications benefit from alternatives like [[introduction_to_cuids_as_an_alternative_to_uuids | CUIDs]] and [[benefits_of_using_nanoids_over_uuids | Nanoids]] <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>, <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. These options offer innovative ways to generate unique identifiers while overcoming the limitations of [[comparison_of_uuids_cuids_and_nanoids | UUIDs]] <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>, <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

*   [[introduction_to_cuids_as_an_alternative_to_uuids | CUIDs]] (Collision-resistant Unique Identifiers) are designed to be meaningful and short, incorporating a timestamp, fingerprint, random string, and counter <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>, <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>, <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. They offer advantages in readability, compactness, scalability, performance efficiency, and security <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>, <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   [[benefits_of_using_nanoids_over_uuids | Nanoids]] generate unique identifiers of fixed length using predefined alphabets, providing a high degree of collision resistance with much shorter lengths than [[comparison_of_uuids_cuids_and_nanoids | UUIDs]] <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>, <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>, <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>, <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

For those using Prisma, [[introduction_to_cuids_as_an_alternative_to_uuids | CUIDs]] can be directly generated <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. For custom setups, the Nano ID package is available <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>, <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.