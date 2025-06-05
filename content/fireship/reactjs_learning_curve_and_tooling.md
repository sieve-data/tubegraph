---
title: Reactjs learning curve and tooling
videoId: HyWYpM_S-2c
---

From: [[fireship]] <br/> 

Reactjs is described as a "half-baked functional UI library" <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> that gives developers "dozens of weird ways to solve the same problems" <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Learning Curve

[[The challenges and complexity of using Reactjs | Reactjs]] has an "extremely high learning curve" <a class="yt-timestamp" data-t="01:02:02">[01:02:02]</a>. Simple tasks like managing reactive state are made more complicated than necessary <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

A notable example of this complexity is `useEffect`, which was "originally going to be called use foot gun" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a> due to its tendency to introduce infinite loops, performance issues, and difficult-to-debug bugs <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

The library is constantly evolving, with "revolutionary new features to monkey patch all the weirdness nobody saw coming on the previous release" <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>, implying a continuous need to adapt to changes. Achieving "blazingly fast" performance requires implementing "all the weird tricks flawlessly" <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, further highlighting the learning demands.

Getting started typically involves creating a new React app and then entering "the gates of tutorial hell" on Google <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Tooling and Ecosystem

As a library, not a framework <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>, [[Building components with React | React]] requires developers to "find and install hundreds of different packages" <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a> to build applications. Many of these packages were "built by teenagers who stopped maintaining them years ago" <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

Key features and patterns within the [[React ecosystem and libraries | React ecosystem]] include:
*   [[Reactjs functional and classbased components | Functional and Class-based Components]] <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>
*   [[React Hooks explained | Hooks]] <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>
*   Forward ref <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>
*   Higher order components <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>
*   Mix-ins <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>
*   Render props <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>
*   Suspense <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>

Specifically, [[React Hooks explained | Hooks]] are used extensively, performing similar functions to classes but in a "more magical hipstery way" <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

Templating in [[React introduction and history | React]] is handled by JSX, a "non-standard way to write HTML" <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a> that results in UI representation entirely within "non-portable callback hell" <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

For styling, developers are presented with "hundreds of CSS-in-JS libraries" <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a> to address the challenges of styling within React <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. The strict mode feature in React is used to "hide baggage from previous versions of the framework I mean library" <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.