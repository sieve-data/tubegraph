---
title: Introduction to CUIDs as an alternative to UUIDs
videoId: toszy9D3kgE
---

From: [[swarajmakesstuff]] <br/> 

You may have been using UUIDs (Universally Unique Identifiers) for unique identifiers in your web applications, but they come with significant drawbacks for modern web development <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. While they are designed to prevent duplicates, with a very low probability of collision even across millions of generations <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, they are often unsuitable for contemporary web applications <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

Alternatives like CUIDs (Collision-resistant Unique Identifiers) and Nanoids offer more innovative ways to generate unique identifiers that address the limitations of UUIDs <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This article focuses on CUIDs as a preferred alternative.

## Understanding UUIDs

UUIDs are 128-bit labels primarily created for operating systems and network protocols <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. They are designed to store information and ensure uniqueness <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## [[Drawbacks of using UUIDs in web applications | Drawbacks of UUIDs in Web Applications]]

Despite their strong uniqueness guarantee, UUIDs present several problems when used in modern web applications:
*   **Length and Space** UUIDs are too long, consuming excessive space in databases, user interfaces, and URLs <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Readability and Usability** They are challenging to read, write, and type, making URLs complex and messy <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
*   **Original Purpose Mismatch** UUIDs were not designed for web applications <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. Their primary purpose in operating systems and network protocols means the size and format of identifiers don't matter as much as they do in web environments, where performance, readability, scalability, and size are crucial <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. UUIDs do not fit these modern web requirements <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Introducing CUIDs

[[Comparison of UUIDs CUIDs and Nanoids | CUIDs]] stand for Collision-resistant Unique Identifiers <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. They provide a method of generating unique identifiers that are both meaningful and short <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

A typical CUID format includes four key components that contribute to its utility in web applications <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>:
*   A timestamp <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>
*   A fingerprint <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>
*   A random string <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>
*   A counter <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>

## [[Use cases and efficiency of CUIDs and Nanoids | Advantages of CUIDs]] over UUIDs

CUIDs offer several advantages that make them highly suitable for modern web applications <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>:
*   **Readability** They are much easier to read <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Shorter Length** CUIDs are shorter than UUIDs <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Scalability** They are designed with scalability in mind <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   **Performance Efficiency** CUIDs are more performance-efficient <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   **Security and Unpredictability** Like UUIDs, CUIDs are secure and unpredictable, ensuring a very low probability of duplicates <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. They provide unique identifiers while being shorter and more performant <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## CUIDs and Nanoids in Practice

[[Benefits of using Nanoids over UUIDs | Nanoids]] are another alternative that generate unique identifiers with a fixed length and from predefined alphabets <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. For instance, generating 1,000 IDs per second continuously for two years with a 9-character Nanoid only results in a 1% probability of collision <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This is a practical and efficient timeframe compared to UUIDs, which would take 126 years to reach a similar collision probability <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

For those using Prisma, CUIDs are directly supported for generation <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. If you're setting up your own identifier generation, the Nanoid package can be easily installed and used <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.