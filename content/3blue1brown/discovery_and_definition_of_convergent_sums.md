---
title: Discovery and definition of convergent sums
videoId: XFDM1ip5HdU
---

From: [[3blue1brown]] <br/> 

The idea of adding an [[concept_of_infinite_sums_in_mathematics | infinite series]] of numbers might seem illogical or "crazy" <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. For instance, the sum 1 + 2 + 4 + 8, continued indefinitely by adding the next power of 2, can surprisingly equal -1 in a specific mathematical sense <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. To understand this, it's necessary to first define what [[concept_of_infinite_sums_in_mathematics | convergent infinite sums]] truly mean <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## The Genesis of Convergent Sums

### An Imagined Discovery
Imagine being an early mathematician discovering that the sum ½ + ¼ + ⅛ + 1/16, continued to infinity, equals 1 <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. To define what it means to add infinitely many things, one might ponder the nature of distances between objects <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

Consider placing two objects on a number line, one at 0 and the other at 1 <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. If the first object marches towards the second, cutting the distance between them in half with each step <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>, the numbers it touches would be ½, then ½ + ¼, then ½ + ¼ + ⅛, and so on <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. Each number in this sequence is a slightly longer sum containing another power of 2 <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Geometrically, these numbers clearly approach 1 <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This leads to the temptation to state that 1 and this infinite sum are the same <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

### Defining "Approach"
Traditionally, adding infinitely many things seems impossible <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. However, the process above didn't involve infinite operations <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. Instead, it generated a list of numbers from finite sums <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. The key observation is that these numbers "approach" 1 <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

The crucial insight is that numbers "approach" 1 not just because the distance between them and 1 gets smaller, but because they can get *arbitrarily close* to 1 <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This means that no matter how small a desired distance (e.g., 1/100, 1/1,000,000) <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>, by going far enough down the list of sums, the numbers will eventually fall within that tiny distance of 1 <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. This seemingly obvious solidification of "approach" is, in fact, an incredibly clever invention <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Formalizing the Infinite Sum
This leads to the formal definition of an [[concept_of_infinite_sums_in_mathematics | infinite sum]] equaling a number *x*:
> An [[concept_of_infinite_sums_in_mathematics | infinite sum]] equals *x* if, when generating a list of numbers by cutting off the sum at finite points, the numbers in this list approach *x* <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This means that no matter how small the distance chosen, all numbers eventually fall within that distance of *x* at some point down the list <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

This definition represents an act of mathematical invention, but one that feels like justifying what was "given" by the universe <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

## Generalizing and Challenging Definitions

### The Repeating Decimal Example
This new understanding allows for more general truths about [[concept_of_infinite_sums_in_mathematics | infinite sums]] <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Instead of cutting an interval in half, one could cut it into pieces of 9/10 and 1/10 <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. Continuing this process, one finds that 9/10 + 9/100 + 9/1000... equals 1 <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This is famously expressed as 0.9 repeating = 1 <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. With infinite sums, "to approach" and "to equal" mean the same thing <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

### The Universal Geometric Series Formula
More generally, if an interval is cut into proportions `p` and `1-p` (where `p` is between 0 and 1) <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>, the resulting infinite sum is `(1-p) + p(1-p) + p^2(1-p) + ... = 1` <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. Dividing by `(1-p)` yields the geometric series formula: `1 + p + p^2 + p^3 + ... = 1 / (1 - p)` <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

This formula, discovered through a specific geometric process, can be applied to values of `p` outside the 0 to 1 range <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>:
*   **Plugging in p = -1**: The equation becomes 1 - 1 + 1 - 1... = ½ <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Plugging in p = 2**: The equation becomes 1 + 2 + 4 + 8... = -1 <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

In traditional mathematical rigor, these results are considered nonsensical because the sequence of finite sums does not approach any value (it diverges) <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. However, a mathematician, unlike a robot, might not let "nonsensical" stop them <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### Beyond Conventional Convergence
Consider the sum 1 + 2 + 4 + 8 + ..., which is 1 less than a power of 2 for each partial sum (1, 3, 7, 15, etc.) <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. If we "humor the universe" and pretend these numbers approach -1, then adding 1 to everything means the powers of 2 (2, 4, 8, 16...) would approach 0 <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. For this to make sense, the formula must be generalized beyond `p` between 0 and 1 <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. This requires reconsidering the fundamental definition of "distance" between numbers <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

## Redefining Distance: The 2-adic Metric

### The Need for a New Perspective
The conventional way of organizing rational numbers on a line may not be the only valid one <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. A "distance" is a function that takes two numbers and outputs how far apart they are <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. For a new distance function to be useful, it should share properties with the familiar distance, such as "shift invariance" <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. This means the distance between two numbers shouldn't change if the same amount is added to both <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a> (e.g., the distance between 0 and 4 is the same as between 1 and 5) <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. Other properties like the triangle inequality are also important <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

### Organizing Numbers by "Rooms"
To make powers of two approach zero, a new frame of mind is needed <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. One could organize numbers into a hierarchy of "rooms," sub-rooms, sub-sub-rooms, and so on <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
*   Zero is in the same room as all powers of two greater than one <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   It's in the same sub-room as all powers of two greater than two <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
*   It's in the same sub-sub-room as powers of two greater than four <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
This process continues infinitely <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

Shift invariance dictates how other numbers fall into these rooms <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. For example, negative one must be in smaller and smaller rooms with numbers one less than a power of two (1, 3, 7, etc.), because zero is in smaller rooms with the powers of two <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

### The 2-adic Metric Explained
To turn this into an actual distance function, the crucial idea is that the distance between two objects depends *only* on the size of the smallest room they share <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>:
*   Numbers in different large yellow rooms are a distance of 1 from each other <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
*   Those in the same large room but different orange sub-rooms are a distance of ½ <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
*   Those in the same orange sub-room but different sub-sub-rooms are a distance of ¼ <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.
This continues, using reciprocals of increasingly larger powers of 2 to indicate closeness <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.

This concept describes a perfectly legitimate distance function known as the **2-adic metric** <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. It's part of a broader family of distance functions called **p-adic metrics** (where 'p' is any prime number) <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. These metrics lead to new types of numbers and are central to modern number theory <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.

Using the 2-adic metric, the statement that the sum of all powers of 2 equals -1 makes sense <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>, because the partial sums (1, 3, 7, 15, etc.) genuinely approach -1 within this new metric <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

## Math as Invention and Discovery
While this narrative is not historically accurate, it illustrates a recurring pattern in the [[exploration_of_mathematical_invention_versus_discovery | discovery of math]] <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>:
1.  Nature presents something ill-defined or nonsensical <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.
2.  New concepts are defined to make this fuzzy discovery make sense <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
3.  These new concepts yield genuinely useful math and broaden traditional notions <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

This suggests that the [[exploration_of_mathematical_invention_versus_discovery | discovery of non-rigorous truths]] often leads to the [[exploration_of_mathematical_invention_versus_discovery | construction of rigorous terms]] that are useful, perpetuating a cycle of further fuzzy discoveries <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.