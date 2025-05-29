---
title: Alternative distance metrics in math including padic metrics
videoId: XFDM1ip5HdU
---

From: [[3blue1brown]] <br/> 

The concept of "distance" in mathematics can be re-evaluated and redefined, leading to new and counter-intuitive results, such as the infinite sum 1 + 2 + 4 + 8... equaling -1 <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Understanding this requires exploring alternative ways of defining how "close" numbers are <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

## Convergent Infinite Sums (Standard Definition)

Historically, mathematicians wrestled with defining infinite sums <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. A classic example is the sum ½ + ¼ + ⅛ + ₁⁄₁₆ + ... up to infinity, which equals 1 <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This can be visualized by imagining an object moving from 0 towards 1 on a number line, halving the remaining distance with each step <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. The numbers the object touches form a list of partial sums: ½, ½ + ¼, ½ + ¼ + ⅛, and so on <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Defining "Approach" and "Equal"

For infinite sums, the definition of "approach" is crucial <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. It's not just that the distance between each number in the partial sum list and the limit (e.g., 1) gets smaller <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. The key insight is that the numbers can get *arbitrarily close* to the limit <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This means no matter how small a desired distance (e.g., 1/100, 1/1,000,000), if you go far enough down the list of partial sums, all subsequent numbers will fall within that tiny distance of the limit <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. This formal definition of an infinite sum "equaling" a number `x` means that the list of finite partial sums approaches `x` in this arbitrarily close sense <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### Generalizing Infinite Sums

This idea can be generalized. If an interval is repeatedly cut into pieces of size `p` and `1-p` (where `p` is between 0 and 1), the sum of the `1-p` portions will equal 1 <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. This leads to the formula:
`(1-p) + p(1-p) + p²(1-p) + ... = 1` <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>
Dividing by `(1-p)`, we get the geometric series formula:
`1 + p + p² + p³ + ... = 1 / (1-p)` <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>

A popular example derived from this is 0.9 repeating equals 1 <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. This arises from cutting an interval into 9/10 and 1/10 proportions repeatedly <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## Divergent Sums and "Nonsense"

While the formula `1 + p + p² + p³ + ... = 1 / (1-p)` makes sense for `p` values between 0 and 1, plugging in other values can yield "nonsensical" results under the traditional definition of infinite sums <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

*   **Plugging in p = -1**: The equation becomes `1 - 1 + 1 - 1 + ... = 1/2` <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. The partial sums (1, 0, 1, 0...) don't approach a single value in the standard sense <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **Plugging in p = 2**: The equation becomes `1 + 2 + 4 + 8 + ... = -1` <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. The partial sums (1, 3, 7, 15, 31...) clearly grow larger and larger, not approaching -1 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

Under the rigorous definition of convergent infinite sums, these results are ignored because their partial sums do not "approach" anything <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. However, a mathematician, not a robot, might seek to make sense of this "nonsense" <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

## The Need for Alternative Distance Metrics

The limitation in making sense of sums like 1 + 2 + 4 + 8... = -1 lies in our traditional definition of distance between rational numbers <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Our familiar number line imposes a specific way of organizing numbers <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

A "distance function" is essentially a function that takes two numbers and outputs a value indicating how far apart they are <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. To be useful, a new distance function should share some properties with the familiar one <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. One crucial property is **shift invariance**: the distance between two numbers shouldn't change if the same amount is added to both <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. For example, the distance between 0 and 4 should be the same as between 1 and 5 <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

## The p-adic Metrics

To make sense of 1 + 2 + 4 + 8... = -1, mathematicians needed to redefine distance in a way that would make powers of two approach zero <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. This was a profound shift in thinking, taking until the 20th century to be discovered <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

One such redefinition organizes numbers into a hierarchy of "rooms, subrooms, sub-subrooms, and so on" <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

### The 2-adic Metric

In the context of powers of two, the idea is that 0 is considered to be in the same "room" as all powers of two greater than one, in the same "sub-room" as powers of two greater than two, and so on <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. This hierarchy extends infinitely <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

Applying shift invariance, the structure of these "rooms" for other numbers can be deduced <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. For example, since 0 is in smaller and smaller rooms with powers of two, -1 must be in smaller and smaller rooms with numbers that are one less than a power of two (1, 3, 7, 15...) <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

This leads to the definition of the **2-adic metric**, where the "distance" between two numbers is determined by the size of the smallest "room" they share <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.
*   Numbers in different large yellow rooms are a distance of 1 apart <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
*   Numbers in the same large room but different orange sub-rooms are a distance of ½ apart <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
*   Numbers in the same orange sub-room but different sub-sub-rooms are a distance of ¼ apart <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.
This continues, using reciprocals of increasingly larger powers of 2 to indicate closeness <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.

The 2-adic metric is a perfectly legitimate notion of distance that satisfies properties like the triangle inequality <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. It is part of a general family of distance functions called **p-adic metrics**, where `p` is any prime number <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. These metrics give rise to completely new types of numbers, neither real nor complex, and are fundamental in modern number theory <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.

### Resolution of the "Nonsense"

Using the 2-adic metric, the sum 1 + 2 + 4 + 8... = -1 actually makes sense <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>. The partial sums (1, 3, 7, 15, 31, etc. – which are all one less than a power of two <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>) genuinely approach -1 under this alternative distance measure <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. This highlights how redefining fundamental concepts, such as distance, can profoundly change mathematical outcomes and reveal new, useful areas of study <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

[[Concept of duality in math|The process of mathematical discovery]] often involves nature presenting ill-defined or nonsensical observations, which then prompt the definition of new concepts to make them sensible, leading to the creation of genuinely useful math that broadens traditional notions <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.