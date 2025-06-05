---
title: Emergence of frameworks and tools in modern JavaScript
videoId: Sh6lK57Cuk4
---

From: [[fireship]] <br/> 

The mid-2000s marked a significant shift for JavaScript, transitioning from what some considered its "dark ages" into a "Renaissance" period <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. Developers faced extreme frustration trying to build web applications that functioned consistently across all browsers <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. This frustration paved the way for the rise of powerful libraries, runtimes, and [[javascript_trends_and_frameworks | frameworks]] designed to simplify development and enhance user experience.

## The Dawn of Modern JavaScript Libraries

### jQuery
A major leap forward occurred in 2006 with the release of jQuery <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. This library is credited for its exceptionally well-done documentation <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>, empowering developers to create more complex and interactive applications that reliably worked across different browsers <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

### Google Chrome and V8 Engine
Another pivotal event happened in 2008 with the launch of Google Chrome and its V8 engine <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. Released on September 2nd, 2008 <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>, V8 fundamentally changed how JavaScript was compiled and interpreted, making it a viable option for high-performance applications in both browser and server environments <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### Node.js
Less than a year later, in May 2009, Ryan Dahl introduced Node.js <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. This server-side runtime for JavaScript was built on top of V8 and featured an event loop, a novel concept at the time <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. Node.js enabled event-driven and non-blocking code, becoming a popular solution for building scalable, real-time web applications <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. It also facilitated the "JavaScript everywhere" paradigm, allowing developers to build their entire web application stack with a single programming language <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

## Rise of Single Page Application Frameworks

Around 2010, [[javascript_trends_and_frameworks | JavaScript frameworks]] specifically designed for Single Page Applications (SPAs) began to emerge <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Backbone.js and AngularJS
Two of the most prominent early SPA [[javascript_trends_and_frameworks | frameworks]] were Backbone.js and AngularJS, both released in October 2010 <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   **Backbone.js** was lightweight and handled DOM updates imperatively <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   **AngularJS** was more comprehensive and utilized a declarative programming style <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
Jeremy Ashkenas, the creator of Backbone, also developed CoffeeScript and Underscore.js <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

### The Importance of Transpiling
CoffeeScript played a significant role in JavaScript history as the first language to popularize transpiling <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. This concept aligns with Brendan Eich's original vision for a malleable programming language <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. Transpilers became crucial with the release of ES6 (ECMAScript 2015) <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>, which introduced numerous [[new_javascript_features_in_2020 | new features]] like `promises`, `let` and `const`, arrow functions, `spread` syntax, and destructuring <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. Tools like Babel and TypeScript are widely used today to allow developers to write code with modern features while ensuring compatibility with older browsers by transpiling back to earlier ECMAScript versions like ES3 <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

### The Rise of React.js
2015 also saw the ascent of React.js <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. React built upon declarative UI concepts seen in AngularJS but improved them with a unidirectional dataflow, immutability, and the use of the virtual DOM <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. React has been instrumental in solidifying modern declarative UI patterns <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

## Expanding Ecosystem: Competing Frameworks and Management Tools

The landscape of [[javascript_frameworks_and_their_updates | JavaScript frameworks]] expanded rapidly, with competitors like Angular, Vue, and Svelte vying for developer mindshare <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

To manage the increasing complexity of these heavyweight JavaScript applications, new tools emerged:
*   **Bundlers**: Rollup and Webpack were developed to bundle dependencies <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.
*   **Type Systems**: TypeScript and Flow were introduced to add static type checking to JavaScript <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   **Functional Programming Aids**: Libraries like Immutable.js and RxJS assist in applying functional patterns to code <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

This proliferation of tools and [[disruptive_trends_in_the_javascript_ecosystem | frameworks]] represents the vast and diverse modern JavaScript ecosystem <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

## The Future: WebAssembly and Continued Evolution
As of 2019, TC39, the committee responsible for ECMAScript, maintains a regular schedule for JavaScript updates <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. A significant development is WebAssembly, a binary format that allows low-level languages like C++ to compile for high-performance web applications <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. While not a replacement for JavaScript, WebAssembly introduces new avenues for web application development and will undoubtedly influence the future of JavaScript <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. The language has consistently evolved from its inception, supported by a massive and diverse community <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.