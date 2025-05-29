---
title: Properties of Eulers Number e
videoId: m2MIpDrF7Es
---

From: [[3blue1brown]] <br/> 

This article explores the derivatives of exponential functions, highlighting the unique properties of [[why_the_number_e_is_special_in_calculus | Euler's number e]] and its significance in calculus <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Derivatives of Exponential Functions

To understand the derivative of exponential functions, consider a function like 2<sup>t</sup> <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. If we model this as the total mass of a population doubling every day <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>, the rate of growth over a full day (e.g., between day 3 and day 4) equals the population size at the start of that day <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. For example, between day 3 and 4, it grows from 8 to 16, a rate of 8 new creature masses per day, which is the initial population size <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This might suggest the derivative of 2<sup>t</sup> is itself <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

However, for a true derivative, we must consider increasingly smaller changes in time (`dt`) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. The change in the function per unit time is expressed as (2<sup>t+dt</sup> - 2<sup>t</sup>) / dt <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. A core property of exponentials allows us to rewrite 2<sup>t+dt</sup> as 2<sup>t</sup> * 2<sup>dt</sup> <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. This allows factoring out 2<sup>t</sup>, resulting in 2<sup>t</sup> * (2<sup>dt</sup> - 1) / dt <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

As `dt` approaches 0, the term (2<sup>dt</sup> - 1) / dt approaches a constant value, approximately 0.6931 <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. This indicates that the derivative of 2<sup>t</sup> is 2<sup>t</sup> multiplied by this constant <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. Similarly, for a base of 3<sup>t</sup>, the constant is about 1.0986 <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>, and for 8<sup>t</sup>, it's around 2.079 <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. These constants are not random but follow a pattern <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

## The Special Nature of Euler's Number

A key question arises: Is there a base for which this proportionality constant is exactly 1? <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a> The answer is [[why_the_number_e_is_special_in_calculus | Euler's number e]], approximately 2.71828 <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. This is the defining property of [[why_the_number_e_is_special_in_calculus | e]] <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. The derivative of e<sup>t</sup> is e<sup>t</sup> itself <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

Graphically, this means that for any point on the graph of e<sup>t</sup>, the slope of the tangent line at that point is equal to the height of the point above the horizontal axis <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

## Connecting Bases: The Role of Natural Logarithm

This special property of [[why_the_number_e_is_special_in_calculus | e]] helps explain the mystery constants for other bases using the chain rule <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a> <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
The derivative of e<sup>kt</sup> is k * e<sup>kt</sup> <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

Any number, such as 2, can be written as e<sup>ln(2)</sup> <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. Thus, the function 2<sup>t</sup> is equivalent to e<sup>(ln(2) * t)</sup> <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. Applying the chain rule, the derivative of this function is proportional to itself, with the proportionality constant being the natural logarithm of 2 <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. When calculated, ln(2) is approximately 0.6931, which matches the constant found earlier for 2<sup>t</sup> <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

In general, the proportionality constant for the derivative of a base `a` to the power `t` is simply ln(a) <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

## Why e is Preferred in Calculus Applications

In calculus applications, exponential functions are almost always written as e<sup>kt</sup>, rather than some base to the power of t <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. This is because any exponential function like 2<sup>t</sup> or 3<sup>t</sup> can be rewritten in this form <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

The advantage of using [[why_the_number_e_is_special_in_calculus | e]] is that the constant `k` in the exponent carries a meaningful interpretation <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. In natural phenomena where a variable's rate of change is proportional to itself (e.g., population growth, cooling, compound interest) <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>, the function describing that variable over time will be an exponential <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. When expressed as e<sup>kt</sup>, the constant `k` directly represents the proportionality constant between the size of the changing variable and its rate of change <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.