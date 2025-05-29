---
title: Epsilondelta definition of limits
videoId: kfF40MiS7zA
---

From: [[3blue1brown]] <br/> 

The concept of a [[limits_in_calculus | limit]] is fundamental in calculus, intuitively meaning that one value gets closer to another <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. While this intuitive understanding is often sufficient, mathematicians developed a more rigorous way to define "approach" to make calculus "airtight and rigorous" <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. This formal definition is known as the epsilon-delta definition of [[limits_in_calculus | limits]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## The Intuition Behind "Approach"

The idea of a [[limits_in_calculus | limit]] is not entirely new if one understands what "approach" means <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. It can be seen as assigning "fancy notation" to the intuitive idea of one value getting closer to another <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

For instance, consider the function:
$$ \frac{(2+h)^3 - 2^3}{h} $$
This expression arises from the [[derivative_definitions_and_their_relation_to_limits | derivative]] of $x^3$ evaluated at $x=2$ <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. When plotted, its graph appears as a continuous parabola <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. However, at $h=0$, the function is undefined because it results in $0/0$ <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. The graph consequently has a "hole" at this point, often exaggerated for visualization <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

Even with this hole, as $h$ approaches $0$, the corresponding output (the height of the graph) approaches $12$ from both sides <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>, <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. The function is still well-defined for inputs arbitrarily close to $0$ <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

To formalize this "approach," mathematicians consider:
1.  A given range of inputs within some distance of $0$ (excluding $0$ itself) <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
2.  The corresponding range of outputs (heights of the graph) <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
As the input range "closes in more and more tightly around 0," the output range "closes in more and more closely around 12" <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. Crucially, the size of this output range can be made "as small as you want" <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

## Formalizing the Concept: Epsilon-Delta

The perspective of shrinking input and output ranges leads to the epsilon-delta definition of [[limits_in_calculus | limits]] <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

Let's say the [[limits_in_calculus | limiting]] value is $L$ (in the example above, $L=12$).
*   **Epsilon ($\epsilon$)**: This Greek letter denotes an arbitrarily small distance away from the [[limits_in_calculus | limiting]] output value $L$ <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. The intent is that $\epsilon$ can be "as small as you want" <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   **Delta ($\delta$)**: This Greek letter denotes a distance around the [[limits_in_calculus | limiting]] input point (e.g., $h=0$) <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

The definition states that for a [[limits_in_calculus | limit]] to exist, *for any* $\epsilon$ (no matter how small), you must *always be able to find* a $\delta$ such that any input within $\delta$ of the [[limits_in_calculus | limiting]] input corresponds to an output within $\epsilon$ of the [[limits_in_calculus | limiting]] value $L$ <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>, <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

## When a Limit Does Not Exist

Consider a counter-example: a function that "jumps up" at $h=0$, being undefined at that point <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   Approaching $h=0$ from the right, the function approaches $2$ <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   Approaching $h=0$ from the left, it approaches $1$ <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

Since there isn't a single, unambiguous value the function approaches, the [[limits_in_calculus | limit]] is not defined at that point <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. In terms of epsilon-delta:
> [!failure] A limit does not exist when...
> You can find a sufficiently small $\epsilon$ (e.g., $0.4$) such that no matter how small you make your range around the input (no matter how tiny $\delta$ is), the corresponding range of outputs is "always too big" <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>, <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. There is no single [[limits_in_calculus | limiting]] output where everything is within a distance $\epsilon$ of that output <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. The outputs "straddle a range that never shrinks smaller than 1" <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

## Significance

The epsilon-delta definition of [[limits_in_calculus | limits]] is considered "needlessly heavy duty for an introduction to calculus" by some <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. However, it offers "an interesting glimpse into the field of real analysis" <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. It demonstrates how mathematicians provide "airtight and rigorous" definitions for the intuitive ideas of calculus <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

The "big fuss" about [[limits_in_calculus | limits]] is that they allow the formal definition of the [[derivative_definitions_and_their_relation_to_limits | derivative]] without needing to discuss "infinitely small changes" <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>, <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. Instead, they ask what happens as the size of a small change "approaches 0" <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This is also how [[limits_in_calculus | limits]] are used in the fundamental theorem of calculus to give clear meaning to "delicate ideas that flirt with infinity" <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>.

While the epsilon-delta definition defines [[limits_in_calculus | limits]], [[derivative_definitions_and_their_relation_to_limits | derivatives]] (which are themselves defined using [[limits_in_calculus | limits]]) can be used to compute [[limits_in_calculus | limits]] that result in $0/0$ forms, through a method known as [[lhopitals_rule_for_computing_limits | L'Hopital's Rule]] <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>, <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.