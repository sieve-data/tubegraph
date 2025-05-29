---
title: Epsilondelta definition of limits
videoId: kfF40MiS7zA
---

From: [[3blue1brown]] <br/> 

The [[introduction_to_limits_in_calculus | idea of a limit]] describes one value getting closer to another <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. While the concept is intuitive, mathematicians developed the epsilon-delta definition to define limits unambiguously and rigorously <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This formal definition is a glimpse into the field of real analysis, making the intuitive ideas of calculus more airtight <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

## The Intuitive Idea of Approach

Consider a function whose graph has a hole at a specific point, such as `(2 + h)³ - 2³` all divided by `h`, which is undefined at `h = 0` <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. As `h` approaches `0`, the corresponding output of this function approaches `12` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

To formalize what "approach" means:
1.  Imagine a range of inputs around the point of interest (e.g., `h = 0`), excluding the point itself <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
2.  Observe the corresponding range of outputs (heights of the graph) above this input range <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
3.  As the input range closes in more tightly around the point of interest, the output range should close in more closely around a specific value <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
4.  Crucially, the size of this output range must be able to be made as small as desired <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

## When a Limit Exists

When a limit exists, the output range can be made as small as one wants <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.
The epsilon-delta definition states that for any given distance `epsilon` (ε), no matter how small, away from the limiting output value, you must always be able to find a corresponding range of inputs, some distance `delta` (δ), around the limiting input point <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. Any input within `delta` of the limiting input (excluding the input itself) must correspond to an output within `epsilon` of the limiting output <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

## When a Limit Does Not Exist

If a limit does not exist, as in a function that "jumps" at a certain point (e.g., approaches `2` from the right and `1` from the left at `h = 0`) <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>:
*   There is no single, clear, unambiguous value that the function approaches <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   Even as the input range around the problematic point shrinks, the corresponding range of outputs does not narrow in on any specific value <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   The range of outputs might never shrink smaller than a certain value, even with an extremely tiny input range <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   In terms of epsilon-delta, this means you can find a sufficiently small `epsilon` such that no matter how small you make `delta`, the corresponding range of outputs is always too big, preventing all outputs from being within `epsilon` of a single limiting output <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

## Connection to Derivatives

The epsilon-delta definition solidifies the [[introduction_to_limits_in_calculus | concept of limits]], which in turn allows for the [[formal_definition_of_derivatives_using_limits | formal definition of a derivative]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a> <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. The use of [[introduction_to_limits_in_calculus | limits]] in defining derivatives helps to avoid the paradoxical idea of [[finite_and_infinite_mathematical_constructs | infinitely small changes]] <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a> <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. For example, in the definition of a derivative, `dx` (or `h`) is considered a non-zero, finitely small "nudge," and the [[introduction_to_limits_in_calculus | limit]] asks what happens as this nudge approaches zero <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a> <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

While the epsilon-delta definition is theoretically crucial for rigor, in practice, [[lhpitals_rule_for_computing_limits | L'Hopital's Rule]] provides a clever trick for actually computing limits that result in indeterminate forms like `0/0` <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a> <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.