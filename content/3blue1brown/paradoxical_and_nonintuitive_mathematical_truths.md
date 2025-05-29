---
title: Paradoxical and nonintuitive mathematical truths
videoId: XFDM1ip5HdU
---

From: [[3blue1brown]] <br/> 

Mathematics often presents concepts that initially seem illogical or even false, challenging our conventional understanding. One such concept is the infinite sum of powers of two.

### The Infinite Sum of Powers of Two

Consider the sum $1 + 2 + 4 + 8 + \dots$ continuing indefinitely by adding the next power of 2 up to infinity <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Initially, it might seem "crazy" or "obviously false" that this infinite sum could equal negative 1 <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

### Defining Convergent Infinite Sums

To understand how such a sum might make sense, it's necessary to first understand how mathematicians define infinite sums that *do* converge and appear intuitive <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

Imagine an early mathematician trying to define what it means for the sum $1/2 + 1/4 + 1/8 + 1/16 + \dots$ to equal 1 <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This process involves conceptually moving an object from 0 towards 1, halving the remaining distance with each step <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. The numbers the object touches are $1/2$, $1/2 + 1/4$, $1/2 + 1/4 + 1/8$, and so on <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. Geometrically, these numbers clearly approach 1 <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

Traditionally, one might argue that "you can't add infinitely many things" <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. However, a less rigid approach allows for the definition of infinite sums <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

The key insight is that one never actually performs infinitely many operations <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. Instead, there's a list of numbers generated from perfectly reasonable finite sums <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. The "approach" isn't just about the distance getting smaller, but about the numbers being able to get "arbitrarily close" to a specific value <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This means that no matter how small a desired distance (e.g., one-millionth), by going far enough down the list of partial sums, all subsequent numbers will fall within that tiny distance of the value <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

Thus, an infinite sum equals a number 'x' if the list of finite partial sums approaches 'x' in this "arbitrarily close" sense <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This concept was a clever [[Conceptualizing Mathematical Problems | conceptualization]] <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a> and represents an "invention" of math that justified a fuzzy discovery <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Extending the Formula and Encountering Nonsense

By generalizing the process of repeatedly cutting an interval, a formula for geometric series can be derived:
$$(1-p) + p(1-p) + p^2(1-p) + \dots = 1$$
This leads to the simplified formula:
$$1 + p + p^2 + p^3 + \dots = \frac{1}{1-p}$$
This formula is derived from a process that only makes sense for values of *p* between 0 and 1 <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. Within this range, it explains concepts like $0.999\dots = 1$, where "to approach" and "to equal" mean the same thing for infinite sums <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

However, if *p* is replaced with any other number (except possibly 1), the right-hand side of the formula still makes sense <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   Plugging in $p=-1$: $1 - 1 + 1 - 1 + \dots = 1/2$ <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   Plugging in $p=2$: $1 + 2 + 4 + 8 + \dots = -1$ <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

These results seem nonsensical under the standard definition of infinite sums because the list of partial sums (e.g., 1, 3, 7, 15, 31 for $p=2$) does not approach anything <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

### Redefining Distance: The 2-adic Metric

To make sense of these "nonsensical" sums, mathematicians looked for arbitrary choices made in the original definitions <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. A crucial, yet subtle, choice is the way distance between rational numbers is defined <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. The familiar number line is not the only reasonable way to organize numbers <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

A new notion of distance, called the **2-adic metric**, was developed. This metric satisfies properties expected of a distance function, such as *shift invariance* (the distance between two numbers shouldn't change if the same amount is added to both) <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

In the 2-adic metric, numbers are organized into rooms, sub-rooms, and so on, based on their divisibility by powers of 2 <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
*   Zero is in the same "room" as all powers of two greater than one, in the same "sub-room" as all powers of two greater than two, and so forth <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   Negative one, for example, is in smaller and smaller rooms with numbers one less than a power of two (e.g., with 1, 3, 7) <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

The distance between two numbers is determined by the size of the smallest "room" they share <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.
*   Numbers in different large rooms are distance 1 apart <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
*   Those in the same large room but different sub-rooms are distance $1/2$ apart <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
*   Those in the same sub-room but different sub-sub-rooms are distance $1/4$ apart <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.
*   This continues using reciprocals of larger and larger powers of 2 <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.

Under this 2-adic metric, powers of two (like 2, 4, 8, 16...) genuinely approach zero <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. Consequently, the numbers 1, 3, 7, 15, 31, and so on (the partial sums of $1 + 2 + 4 + \dots$) genuinely approach negative 1 <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>. This new definition of distance makes the seemingly paradoxical sum $1 + 2 + 4 + \dots = -1$ mathematically consistent.

### The Nature of Mathematical Discovery

This journey illustrates a recurring pattern in mathematical discovery <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>:
1.  Nature or existing formulas present something initially ill-defined or nonsensical <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.
2.  New concepts are defined to make this "fuzzy discovery" make sense <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
3.  These new concepts yield genuinely useful mathematics and broaden traditional notions <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

This process suggests that the [[the_relationship_between_mathematical_invention_and_discovery | discovery of non-rigorous truths]] often leads to the construction of rigorous, useful terms, which in turn opens the door for more fuzzy discoveries, perpetuating the cycle <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.