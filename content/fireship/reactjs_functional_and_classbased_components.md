---
title: Reactjs functional and classbased components
videoId: HyWYpM_S-2c
---

From: [[fireship]] <br/> 

[[Reactjs overview and history | React.js]] provides various methods for structuring UI logic, including functional and class-based components <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Functional Components

[[Building components with React | Components]] can be written as functions, which is presented as a way to engage in functional programming within [[Reactjs overview and history | React]] <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. A key feature of [[Reactjs overview and history | React]] is the ability to write pure functional code <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. However, performing useful actions typically requires writing imperative functions that incorporate [[state_and_props_in_react | state]] and [[React Hooks explained | effects]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This approach can make simple concepts like reactive [[state_and_props_in_react | state]] unnecessarily complex <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

### [[React Hooks explained | Hooks]]

In modern [[Reactjs overview and history | React]], [[React Hooks explained | Hooks]] are widely used with functional components <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. [[React Hooks explained | Hooks]] offer similar capabilities to what class-based components traditionally provided <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. One notable [[React Hooks explained | Hook]] is `useEffect`, humorously referred to as "use foot gun" due to its potential to introduce infinite loops, performance issues, and difficult-to-diagnose bugs <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Class-Based Components

While functional components are the preferred method, [[Building components with React | components]] can also be created using classes <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. However, the use of class-based components is strongly discouraged <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

## Templating with JSX

Regardless of whether a component is functional or class-based, templating in [[Reactjs overview and history | React]] is handled using JSX <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. JSX is a non-standard way of writing HTML that allows the UI to be represented entirely within non-portable callback-based structures <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.