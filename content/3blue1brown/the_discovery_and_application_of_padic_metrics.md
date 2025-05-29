---
title: The discovery and application of padic metrics
videoId: XFDM1ip5HdU
---

From: [[3blue1brown]] <br/> 
The formula `1 + 2 + 4 + 8` continuing to infinity might seem impossible, but there's a mathematical framework where this infinite sum can equal negative 1 <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a> <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This initially feels strange or false <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, as the standard definition of infinite sums doesn't apply; the list of partial sums (1, 3, 7, 15, 31, and so on) doesn't approach any finite value in the traditional sense <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a> <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

To make sense of such a "nonsensical" sum, mathematicians broadened the concept of distance itself, a feat achieved only in the 20th century <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a> <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

## Re-evaluating Distance

A notion of distance is fundamentally a function that takes two numbers and outputs a value indicating how far apart they are <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. To be useful, a new distance function should share some properties with the familiar one:

*   **Shift Invariance**: The distance between two numbers should not change if both are shifted by the same amount <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a> <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. For example, the distance between 0 and 4 should be the same as between 1 and 5 <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Triangle Inequality**: This is another important property that a valid distance function should satisfy <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

The goal was to find a distance definition where powers of two approach zero <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

## The 2-adic Metric

To conceptualize this new distance, imagine numbers organized in a hierarchy of "rooms," "sub-rooms," and "sub-sub-rooms," continuing infinitely <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a> <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

In this system:
*   Zero is considered to be in the same "room" as all powers of two greater than one.
*   It's in the same "sub-room" as all powers of two greater than two.
*   It's in the same "sub-sub-room" as powers of two greater than four, and so on <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

Applying shift invariance, other numbers must fall into specific rooms. For instance, negative one (`-1`) must be in smaller and smaller rooms with numbers that are one less than a power of two (e.g., 1, 3, 7), because zero is in smaller and smaller rooms with the powers of two (e.g., 2, 4, 8) <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a> <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

This conceptual organization leads to a formal definition where the "distance" between two numbers is determined by the size of the smallest room they share <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>:

*   Numbers in different large "yellow" rooms are a distance of 1 from each other <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
*   Those in the same large room but different "orange" sub-rooms are a distance of ½ <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
*   Those in the same orange sub-room but different sub-sub-rooms are a distance of ¼ <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.
*   This continues, using reciprocals of increasingly larger powers of two to indicate closer proximity <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.

This is known as the **2-adic metric** <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. It's a perfectly legitimate notion of distance, satisfying properties like the triangle inequality <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a> <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.

## Application and Significance

The 2-adic metric is part of a general family of distance functions called **p-adic metrics**, where 'p' represents any prime number <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a> <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>. These metrics give rise to entirely new types of numbers, distinct from real or complex numbers, and have become a central concept in modern number theory <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a> <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.

Using the 2-adic metric, the sum `1 + 2 + 4 + 8 + ... = -1` genuinely makes sense. The partial sums (1, 3, 7, 15, 31, etc.) genuinely approach negative 1 in this new metric <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a> <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

This demonstrates a recurring pattern in [[the_relationship_between_mathematical_invention_and_discovery | the discovery of math]]: nature often presents concepts that are initially ill-defined or nonsensical. Mathematicians then define new concepts to make sense of these "fuzzy discoveries," which in turn yield useful math and broaden traditional notions <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a> <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. This suggests that the discovery of non-rigorous truths often leads to the construction of rigorous terms, perpetuating a cycle of [[the_relationship_between_mathematical_invention_and_discovery | invention and discovery]] <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.