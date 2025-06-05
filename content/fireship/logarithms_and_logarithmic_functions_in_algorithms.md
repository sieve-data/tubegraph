---
title: Logarithms and logarithmic functions in algorithms
videoId: bOCHTHkBoAs
---

From: [[fireship]] <br/> 

Logarithmic functions are essential abstract mathematical concepts for programmers to understand <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. Understanding them can help engineers think more like true engineers <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Understanding Logarithms

To understand logarithmic functions, consider an analogy: imagine a log that starts at 16 feet and is repeatedly cut in half until it reaches a length of 2 feet <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. When drawing a line through the lengths after each cut, it curves gradually, not perfectly straight <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

Logarithm is the exact opposite of exponentiation <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. If you know how many times the log was cut (e.g., 4 times for a 16-foot log to reach 2 feet), you can raise 2 to the power of that value (2^4) to get the original length (16 feet) <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. Conversely, if you know the original length (16 feet) and want to find out how many times it needed to be cut to reach a length of 2, you could calculate that with a base 2 logarithm on the original length, which would return a value of 4 <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### Types of Logarithms

*   **Binary Logarithm (Base 2)**: When the base of a logarithm is 2, it's called a binary logarithm <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This is particularly relevant in computer science.
*   **Common Logarithm (Base 10)**: In mathematics, it's more common to use base 10, which is called the common logarithm <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## Application in [[Data Structures and Algorithms | Algorithms]]

In computer science, many [[Data Structures and Algorithms | algorithms]] operate in a way that resembles logarithmic functions <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

[!EXAMPLE]
A prime example is [[Data Structures and Algorithms | binary search]] <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This type of [[Data Structures and Algorithms | algorithm]] cuts the search area in half after each iteration, which leads to [[Big O time complexity | logarithmic time complexity]] <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. Understanding how to measure [[Big O time complexity | complexity]] like logarithmic time is essential for technical interviews and general problem-solving <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.