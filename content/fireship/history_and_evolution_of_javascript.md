---
title: History and evolution of JavaScript
videoId: Sh6lK57Cuk4
---

From: [[fireship]] <br/> 

The story of JavaScript is one of rapid evolution, transforming from a simple scripting language written in just ten days into a technology that influences nearly every human being on the planet today <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>.

## The Dawn of the Web and Early Browsers

The world's first web browser and web server were developed by Sir Tim Berners-Lee in Switzerland on a NeXT computer system on Christmas Day 1990 <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Initially, the concept of the internet was not widely understood <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

The "internet" is a giant computer network, described as a "computer billboard" made up of several universities joined together, allowing others to access it <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

A significant step towards mainstream internet access came in December 1991 when a bill was introduced that provided funding for Mosaic, the first mainstream browser <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Mosaic was developed by Marc Andreessen and Eric Bina at the University of Illinois, released for UNIX systems in January 1993, with later ports for Macintosh and Windows <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. It was Mosaic that truly began to bring the Internet to the mainstream <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. At this stage, JavaScript did not exist; only the Document Object Model (DOM), which was not yet standardized <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## The Birth of JavaScript

After graduating in 1993, Marc Andreessen co-founded [[the_role_of_netscape_and_brendan_eich_in_javascripts_development | Netscape]] in California <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. Within a couple of years, [[the_role_of_netscape_and_brendan_eich_in_javascripts_development | Netscape]] Navigator controlled about 80% of the browser market share <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Andreessen recognized the need for browsers to become more dynamic, requiring a "glue language" for web designers to make websites more interactive <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

Initially, they considered the Java programming language from Sun Microsystems, but quickly discarded the idea <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Plan B was to recruit [[the_role_of_netscape_and_brendan_eich_in_javascripts_development | Brendan Eich]] with the task of integrating the Scheme programming language into the browser while maintaining a Java-like syntax <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

Only ten days later, the first version of [[basics_of_javascript_and_its_history | JavaScript]] was created <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. It was initially named Mocha, then renamed LiveScript by September 1995 when it shipped in the beta releases of [[the_role_of_netscape_and_brendan_eich_in_javascripts_development | Netscape]] Navigator 2.0 <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. In December of the same year, it was renamed [[basics_of_javascript_and_its_history | JavaScript]] to associate it with the popular Java language <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

Syntactically, Mocha was a curly-bracket language like Java or C <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. Under the hood, it already contained key features of modern [[basics_of_javascript_and_its_history | JavaScript]], such as first-class functions, dynamic typing, and prototypal inheritance, the latter being inspired by the Self programming language from Sun Microsystems <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. [[the_role_of_netscape_and_brendan_eich_in_javascripts_development | Brendan Eich]] intentionally created a flexible, multi-paradigm language rather than one highly specialized for 1990s browsers <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

Early on, [[basics_of_javascript_and_its_history | JavaScript]] made an impact on user experience, often through "annoying pop-up windows" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

## Standardization and Early Challenges

As the internet grew, the need to [[standardization_of_javascript_and_the_ecmascript_specification | standardize JavaScript]] became apparent <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. Microsoft, with its Internet Explorer browser, reverse-engineered [[basics_of_javascript_and_its_history | JavaScript]] and released its own version called JScript <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. This resulted in two nearly identical languages, [[basics_of_javascript_and_its_history | JavaScript]] and JScript, by 1996 <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

To address this, [[the_role_of_netscape_and_brendan_eich_in_javascripts_development | Netscape]] approached the European Computer Manufacturers Association (ECMA), a neutral party for IT industry standards since 1961 <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. By June 1997, the first version of ECMAScript (often referred to as ES) was released <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. This specification provided consistent guidelines for browser vendors and server-side applications implementing the [[basics_of_javascript_and_its_history | JavaScript]] language <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

Early ECMAScript lacked features like exception handling with try-catch blocks, regular expressions, and the strict equality operator <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. One of [[the_role_of_netscape_and_brendan_eich_in_javascripts_development | Brendan Eich]]'s biggest regrets was the initial loose equality, where a number could equal a string, a compromise made for accessibility to non-programmers <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

ECMAScript Version 3, released in December 1999, introduced better error handling and the strict equality operator, making comparisons less ambiguous <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

## The "Dark Ages" and Fragmentation (Early 2000s)

Despite progress, the tech bubble burst in March 2000, with the Nasdaq losing over a trillion dollars in value that month <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. This period saw stagnation in [[standardization_of_javascript_and_the_ecmascript_specification | ECMAScript]] development, with no new version published for ten years <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

[[the_role_of_netscape_and_brendan_eich_in_javascripts_development | Netscape]] was acquired by AOL, and Microsoft's Internet Explorer began to dominate browser market share, controlling at least 80% in the early 2000s <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Microsoft often disregarded the [[standardization_of_javascript_and_the_ecmascript_specification | ECMAScript]] specification, implementing its own extensions for [[basics_of_javascript_and_its_history | JavaScript]] <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. This led to fragmentation, which still impacts supporting legacy versions of Internet Explorer today <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. However, this period also led to revolutionary features like Ajax, which allowed asynchronous [[basics_of_javascript_and_its_history | JavaScript]] implementation, a precursor to modern single-page applications <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

Work on ECMAScript Version 4 (ES4) began in the early 2000s, aiming for features resembling modern TypeScript, such as optional type annotations, classes, and interfaces, designed for enterprise-scale [[basics_of_javascript_and_its_history | JavaScript]] use <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. Douglas Crockford, creator of JSON (2003) and a committee member from Yahoo, expressed concern that the ES4 proposal was becoming too large <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. Microsoft agreed, refusing to participate in the ES4 proposal <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. This resulted in two competing proposals: ES3.1 (a simpler version) and ES4 <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. ES4 was ultimately scrapped in 2008, though some of its concepts found their way into ActionScript, a scripting language for Adobe Flash <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

## The Renaissance of JavaScript (Mid-2000s onwards)

The early to mid-2000s were challenging for [[basics_of_javascript_and_its_history | JavaScript]] developers due to browser inconsistencies <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

### jQuery and V8 Engine

A significant leap occurred in 2006 with the release of jQuery <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. This library provided excellent documentation and empowered developers to build more complex, interactive, and reliable web applications across all browsers <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

Another pivotal moment came in September 2008 with the release of Google Chrome and its V8 engine <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. V8 revolutionized how [[basics_of_javascript_and_its_history | JavaScript]] was compiled and interpreted, making it a viable option for high-performance applications in both browser and [[using_javascript_on_web_and_server_environments | server-side environments]] <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### Node.js and "JavaScript Everywhere"

Less than a year later, in May 2009, Ryan Dahl introduced Node.js <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. This server-side runtime for [[basics_of_javascript_and_its_history | JavaScript]], built on V8, included an event loop that allowed for event-driven and non-blocking code <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. Node.js became known for building scalable real-time web applications and enabled developers to use a single programming language across their entire web application stack, a concept known as the "JavaScript everywhere" paradigm <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

### ECMAScript 5 and Beyond

The [[standardization_of_javascript_and_the_ecmascript_specification | ECMAScript]] committee, TC39, reunited in Oslo, Norway, and decided to use ES3.1 as the foundation for ECMAScript 5 (ES5) <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. ES5 was released in December 2009, exactly ten years after the previous official specification <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. It included important features like JSON support, functional array and object methods, and strict mode <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

The next major release was ECMAScript 2015 (ES6), which brought a wealth of new features, including:
*   Promises <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>
*   `let` and `const` keywords <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>
*   Arrow functions <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>
*   Spread syntax <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>
*   Destructuring <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>

These features represented a huge leap forward, but their adoption was challenging due to a lack of support in many legacy browsers <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. This led to the prolific use of transpilers like Babel and TypeScript, which allow developers to write modern [[basics_of_javascript_and_its_history | JavaScript]] code and compile it to older, more widely supported versions (e.g., ES3) <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. CoffeeScript was one of the first languages to make transpiling mainstream <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>, aligning with [[the_role_of_netscape_and_brendan_eich_in_javascripts_development | Brendan Eich]]'s original vision of a malleable programming language <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

### Frameworks and Tools

From 2010 onwards, [[javascript_trends_and_frameworks | JavaScript frameworks]] specifically designed for single-page applications began to emerge <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. Two early popular ones were Backbone.js and AngularJS, both released in October 2010 <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. Backbone was lightweight and used an imperative style for DOM updates, while AngularJS was more all-inclusive and used a declarative style <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. Jeremy Ashkenas, creator of Backbone, also developed CoffeeScript and Underscore.js <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

By 2015, the [[javascript_trends_and_frameworks | rise of React.js]] began, building on declarative UI concepts from AngularJS but improving them with unidirectional dataflow, immutability, and the use of the virtual DOM <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. Other prominent frameworks include Angular, Vue, and Svelte <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

The increasing complexity of [[basics_of_javascript_and_its_history | JavaScript]] applications led to the [[emergence_of_frameworks_and_tools_in_modern_javascript | development of various tools]]:
*   **Bundlers:** Rollup and Webpack manage and bundle dependencies <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   **Type Systems:** TypeScript and Flow add type safety to [[basics_of_javascript_and_its_history | JavaScript]] code <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   **Functional Programming Aids:** Libraries like Immutable.js and RxJS help apply functional patterns <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

## Current State and Future Trends

As of summer 2019, TC39, the committee in charge of [[standardization_of_javascript_and_the_ecmascript_specification | ECMAScript]], maintains a regular schedule of [[standardization_of_javascript_and_the_ecmascript_specification | updating JavaScript]] <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. A significant development is WebAssembly, a binary format that allows low-level languages like C++ to compile to the web for high-performance applications <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. While not a replacement for [[basics_of_javascript_and_its_history | JavaScript]], WebAssembly offers a new way to build web applications and will undoubtedly [[influence_of_browsers_and_companies_on_javascripts_development | influence JavaScript's future]] <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

[[basics_of_javascript_and_its_history | JavaScript]] has consistently evolved from its inception, supported by a massive and diverse community, making it a language that continues to be a dominant force in technology <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.