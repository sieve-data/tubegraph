---
title: JavaScript language quirks
videoId: aXOChLn5ZdQ
---

From: [[fireship]] <br/> 

[[javascript_basics_and_history | JavaScript]] is described as an "embarrassing toy language" <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a> primarily used to build things it was not intended for <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Origins and Early Reception

[[javascript_basics_and_history | JavaScript]] was created by Brendan Eich in 1995 <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. He was tasked with building a language similar to Java, but specifically for "words" <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. It took him only seven days to complete the initial execution <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Despite its rapid development, it was initially perceived as an "overnight dumpster fire" <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

A significant shift occurred in 2005 when Ryan Dahl brought [[javascript_basics_and_history | JavaScript]] to the server with Node.js <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Ryan Dahl later expressed regret for his invention, comparing himself to Alfred Nobel and dynamite <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>, stating "it's my fault and I'm very sorry" <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Intended vs. Modern Use

The language was originally designed solely for "annoying people with browser pop-ups" <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. However, today it is widely used for:
*   Memory-intensive desktop applications with Electron <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>
*   "Janky" mobile applications with React Native <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>
*   Unreliable APIs with Express.js <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>

## Ecosystem and Proliferation of Libraries

Regardless of the development goal, there are "hundreds of different game-changing next-gen libraries" available <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. When a [[javascript_basics_and_history | JavaScript]] developer encounters a problem, their instinct is to create a new framework and upload it to GitHub <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The sheer volume of NPM packages is so vast that it's humorously linked to climate change predictions <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

An example of a popular package is `is-odd`, which simply checks if a number is odd and receives over 400,000 downloads per week <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## Type Coercion and Quirks

[[javascript_basics_and_history | JavaScript]] is characterized as a "Loosely typed language" <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>, meaning it is "completely detached from reality" <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

Examples of its unusual type coercion:
*   Adding an array to an object results in the string "object object" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   Switching the order (object + array) predictably returns `0` <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   Adding two objects together yields "object object object object" <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   Adding two arrays results in an empty string <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

The following equivalencies are noted:
*   The number `0` is equivalent to an empty array (`[]`) <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   The number `0` is equivalent to a string of `"0"` <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   Logically, this would imply that a string of `"0"` is equivalent to an empty array, but "amazingly it's not" <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

The perceived rationale for some of these behaviors stems from a 1990s Netscape focus group with "homeless web developers" who believed `2 + 2` should equal `22` <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Consequently, `2 - 2` still equals `0` <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

## Module Systems and Tooling Challenges

[[javascript_basics_and_history | JavaScript]] has multiple module systems, such as CommonJS and ESM, which can lead to uncertainty about whether an installed package will work <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Building applications with [[javascript_basics_and_history | JavaScript]] also often requires learning module bundling tools like Webpack, which can be a deterrent <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

## Conclusion

Despite its numerous perceived problems and its history, the speaker acknowledges that [[javascript_basics_and_history | JavaScript]] has evolved into an "awesome language in 2022" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a> and expresses enjoyment in programming with it <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. It is also recognized as a language that provides a livelihood for developers <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.