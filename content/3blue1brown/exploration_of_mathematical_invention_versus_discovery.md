---
title: Exploration of mathematical invention versus discovery
videoId: XFDM1ip5HdU
---

From: [[3blue1brown]] <br/> 

The question of whether mathematics is primarily invented or discovered is a long-standing debate. This article explores a perspective where the process involves a cyclical interplay between both.

## The Counterintuitive Sum: A Case Study
Consider the infinite sum 1 + 2 + 4 + 8 and so on, continuing indefinitely by adding the next power of 2. While this sum might appear to diverge to infinity, there is a sense in which this [[mathematical_intuition_and_counterintuitive_results | infinite sum]] actually equals negative 1 <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Initially, such a statement might seem strange or patently false <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. To understand how this can be, it's necessary to redefine fundamental mathematical concepts.

## Defining Infinite Sums: From Discovery to Invention
The journey to making sense of such "crazy equations" often begins with understanding more conventional infinite sums, known as convergent infinite sums <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

### The Problem of "Approaching"
Imagine an early mathematician contemplating the sum ½ + ¼ + ⅛ + ₁/₁₆... up to infinity, and intuiting that it equals 1 <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. To convince others, a precise definition of adding infinitely many things is required <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. This often feels like a struggle, akin to being wrong or stuck <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

A thought experiment involves imagining two objects on a number line, one at 0 and the other at 1. If the first object marches towards the second, cutting the distance between them in half with each step, the positions it touches form a sequence of finite sums: ½, ½ + ¼, ½ + ¼ + ⅛, and so on <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. Geometrically, these numbers clearly approach 1 <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### The Formal Definition
A purely formal education might dismiss the idea of adding infinitely many things as ridiculous, as no entity could perform such a task <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. However, a mathematician with a "healthy irreverence" would seek to make sense of this "nonsense" that "nature gave" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

The key lies in dissecting how the fuzzy discovery was made. The infinite sum was never actually performed; instead, a list of finite sums was generated <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. The crucial observation was that these numbers "approach" 1 <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. To define "approach" precisely, it's understood that the numbers can get *arbitrarily close* to 1 <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This means that no matter how small a desired distance (e.g., one hundredth, one millionth), eventually all numbers in the list will fall within that tiny distance of 1 <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

This leads to the formal definition: an infinite sum equals a number 'x' if, when generating a list of numbers by cutting off the sum at finite points, the numbers in this list approach 'x' in the aforementioned arbitrary closeness sense <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This act represents the invention of new mathematics, not by pulling concepts out of thin air, but by justifying an initial intuition provided by the "universe" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

## Generalizing and Confronting Nonsense
By looking for arbitrary decisions made during the initial discovery, mathematicians seek more general truths about infinite sums <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. For example, instead of always cutting an interval in half, any proportion 'p' between 0 and 1 could be chosen <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. This generalization leads to formulas like:

1 - p + p(1 - p) + p²(1 - p) + ... = 1 <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>

Dividing by (1-p) yields the formula for a geometric series:

1 + p + p² + p³ + ... = 1 / (1 - p) <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>

### Embracing "Nonsense"
While this formula makes sense for values of 'p' between 0 and 1 (as seen with 0.9 repeating equaling 1 <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>), plugging in other values of 'p' can yield seemingly nonsensical results <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. For instance:
*   Plugging in p = -1: 1 - 1 + 1 - 1... = ½ <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   Plugging in p = 2: 1 + 2 + 4 + 8... = -1 <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

Rigorous definitions of infinite sums would dictate ignoring these cases because the generated list of numbers does not approach anything <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. However, a true mathematician, unlike a "robot," does not let nonsensical results deter them <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. The partial sums for 1 + 2 + 4 + 8... (1, 3, 7, 15, 31...) are all one less than a power of 2 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. The challenge then becomes how to make these numbers "approach" negative 1, or, by adding 1 to everything, how powers of 2 (2, 4, 8, 16...) can approach 0 <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

## Reimagining Distance: A New Invention
To make sense of these divergent sums, the previously "arbitrary choice" of how distance between rational numbers is defined must be re-examined <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. The familiar number line is not the only reasonable way to organize numbers <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

A notion of distance is a function that indicates how far apart two numbers are, sharing properties with the familiar distance, such as [[mathematical_invariants_and_their_significance | shift invariance]] (the distance between two numbers doesn't change if both are shifted by the same amount) <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. The goal is to find a distance function where powers of two approach zero, and which is shift invariant <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

### The 2-adic Metric
One imaginative way to achieve this is to organize numbers into a hierarchy of "rooms," "sub-rooms," and so on <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>. For example, 0 is in the same "room" as all powers of 2 greater than 1, in the same "sub-room" as powers of 2 greater than 2, and so forth <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. Applying [[mathematical_invariants_and_their_significance | shift invariance]] helps deduce where other numbers fall in this hierarchy <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. Negative 1, for instance, must be in successively smaller rooms with numbers that are one less than a power of 2 <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

This abstract idea of closeness can be formalized into an actual distance function:
*   Numbers in different "large yellow rooms" are a distance of 1 apart <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
*   Numbers in the same "large room" but different "orange sub-rooms" are a distance of ½ apart <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
*   Numbers in the same "orange sub-room" but different "sub-sub-rooms" are a distance of ¼ apart <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

This pattern continues, using the reciprocals of increasing powers of 2 to indicate closeness <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>. This concept, known as the 2-adic metric, is a perfectly legitimate notion of distance, part of the broader family of p-adic metrics (where p is any prime number) <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. These metrics give rise to entirely new types of numbers and are central to modern number theory <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.

Using the 2-adic metric, the sum of all powers of 2 genuinely approaches negative 1, making the seemingly impossible equation 1 + 2 + 4 + 8... = -1 perfectly sensible <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.

## The Cycle of Discovery and Invention
While this explanation is not a historical account, it illustrates a recurring pattern in mathematical development <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>:
1.  **Discovery:** "Nature hands you something that's ill-defined or even nonsensical" <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>. This often involves intuition or observation of patterns.
2.  **Invention:** "You define new concepts that make this fuzzy discovery make sense" <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. This involves rigorous definition, generalization, and often the creation of new mathematical structures. These new concepts are often genuinely useful and broaden understanding of traditional notions <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

This process is a continuous cycle: the discovery of non-rigorous truths leads to the construction of rigorous terms, which in turn opens the door for more fuzzy discoveries <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.