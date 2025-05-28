---
title: Visualization techniques for understanding the conjecture
videoId: 094y1Z2wpJg
---

From: [[veritasium]] <br/> 

The [[collatz_conjecture_overview | Collatz Conjecture]], also known as the 3N+1 problem, involves a simple set of rules applied to a number: if it's odd, multiply by three and add one; if it's even, divide by two <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>. The conjecture states that every positive integer, when these rules are applied, will eventually enter the "four, two, one" loop <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. To better comprehend the behavior of numbers under these rules, various visualization techniques have been employed.

## Hailstone Numbers as Altitude

One way to conceptualize the numbers in a [[collatz_conjecture_overview | Collatz sequence]] is to imagine them as representing height above the ground in meters <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>. Numbers in a sequence, known as "hailstone numbers," tend to fluctuate, going up and down like hailstones in a thundercloud before eventually "falling down" to one <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. For example, the number 26 starts at 26 meters, rises to 40 meters, and takes 10 steps to reach one <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>. In contrast, 27 climbs to 9,232, higher than Mount Everest, before descending to one in 111 steps <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

## Logarithmic Graphs and Randomness

When plotting the sequence of a large, randomly chosen number, the raw graph peaks and then drops, making it difficult to discern patterns <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>. However, if the logarithm of the numbers is taken, the resulting graph shows a wiggly pattern with a clear downward trend <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>. This resembles a stock market on a bad day, which is no coincidence. Both are examples of [[mathematical_properties_of_3x1_problem | geometric Brownian motion]]. This implies that if the linear trend is removed, the fluctuations are random, similar to flipping a coin at each step (heads for up, tails for down) <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>. While the stock market tends to trend upwards over long periods, [[mathematical_properties_of_3x1_problem | 3x+1]] sequences tend to trend downwards <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>.

## Benford's Law and Leading Digits

Another analytical approach involves examining the leading digit of each number in a sequence <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>. By counting how many numbers in a sequence start with each digit (one through nine) and compiling this data into a histogram for multiple sequences, a stable pattern emerges <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>. For the first billion sequences, the digit "one" is the most common leading digit (30%), followed by "two" (17.5%), and decreasing frequencies for higher digits, with less than 5% starting with "nine" <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>. This distribution is known as Benford's Law and appears in various natural phenomena, from country populations to physical constants <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>. While useful for fraud detection, Benford's Law does not prove whether all numbers will end up in the four, two, one loop <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>.

## Directed Graphs

A common way to visualize the paths of numbers in [[collatz_conjecture_overview | 3x+1]] is through a directed graph, showing how each number connects to the next in its sequence <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>. This graph resembles a tree or a series of small streams flowing into each other <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>. If the [[collatz_conjecture_overview | conjecture]] is true, every positive integer is connected to this graph, meaning every "tiny stream" eventually flows into the "massive river of four, two, one" <a class="yt-timestamp" data-t="09:18:00">[09:18:00]</a>.

## Rotated Graphs (Coral/Seaweed)

A modified visualization of the directed graph involves rotating the graph at each number: anti-clockwise for an odd number and clockwise for an even number <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>. By adjusting the degree of rotation, this technique produces intricate, organic shapes resembling coral or seaweed <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>. This artistic representation highlights the complex yet ordered nature that arises from the simple [[mathematical_properties_of_3x1_problem | Collatz operations]] <a class="yt-timestamp" data-t="20:07:00">[20:07:00]</a>.