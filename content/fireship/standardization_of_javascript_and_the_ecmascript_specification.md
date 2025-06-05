---
title: Standardization of JavaScript and the ECMAScript specification
videoId: Sh6lK57Cuk4
---

From: [[fireship]] <br/> 

The need for standardization in web technologies became apparent as the internet grew rapidly <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. By 1996, two almost identical scripting languages existed: [[the_role_of_netscape_and_brendan_eich_in_javascripts_development | JavaScript]], developed by Netscape, and JScript, Microsoft's reverse-engineered version <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. To address this fragmentation and provide a consistent set of guidelines for implementing the language, Netscape approached Ecma International <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.

## Ecma International and TC39

Ecma International, previously known as the European Computer Manufacturers Association, has acted as a neutral party for setting IT industry standards since 1961 <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. The technical committee responsible for [[basics_of_javascript_and_its_history | JavaScript]]'s standardization is **TC39** <a class="yt-timestamp" data-t="11:18:00">[11:18:00]</a>.

## ECMAScript Versions

### ECMAScript 1 (ES1)

The first version of the standardized language, Ecma-262 (commonly known as ECMAScript), was published by June 1997 <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>. This initial specification provided browser vendors and server-side applications with a consistent guide for implementing [[basics_of_javascript_and_its_history | JavaScript]] <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>. While similar to modern [[basics_of_javascript_and_its_history | JavaScript]], it lacked features like exception handling (try-catch blocks), regular expressions, and the strict equality operator <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>. One peculiar aspect inherited from early development was its lenient equality operator, which allowed a number to equal a string, a decision made to make the language more accessible to non-programmers <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>.

### ECMAScript 3 (ES3)

Released in December 1999, ECMAScript version 3 introduced improvements such as better error handling and, importantly, the strict equality operator to make equality comparisons less ambiguous <a class="yt-timestamp" data-t="05:23:00">[05:23:00]</a>.

### The ES4 Controversy and the "Dark Ages"

After ES3, a significant period without new ECMAScript versions followed <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>. Work on ECMAScript version 4 began in the early 2000s, aiming for features resembling modern TypeScript, including optional type annotations, classes, and interfaces, designed for enterprise-scale [[using_javascript_on_web_and_server_environments | JavaScript]] use <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>. However, Douglas Crockford (creator of JSON) and Microsoft opposed ES4, considering it too large and out of control <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>. This led to two competing proposals: ES 3.1 and ES4 <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>. Ultimately, ES4 was scrapped in 2008, though its concepts later appeared in Adobe's ActionScript for Flash <a class="yt-timestamp" data-t="07:19:00">[07:19:00]</a>.

The early to mid-2000s are considered the "dark ages" for [[basics_of_javascript_and_its_history | JavaScript]] due to this stagnation and fragmentation caused by Microsoft's Internet Explorer, which controlled over 80% of the browser market and often implemented its own [[basics_of_javascript_and_its_history | JavaScript]] extensions instead of adhering strictly to the spec <a class="yt-timestamp" data-t="06:13:00">[06:13:00]</a>.

### ECMAScript 5 (ES5)

A renewed push for standardization occurred around 2009. The parties involved decided to base the next version, ES5, on the simpler ES 3.1 proposal <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>. ES5 was released in December 2009, a decade after the last official spec <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>. It included important features such as JSON support, functional array and object methods, and strict mode <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>.

### ECMAScript 6 / ES2015

Released in 2015, ES6 (also known as ES2015) brought a substantial number of [[new_javascript_features_in_2020 | new JavaScript features]], marking a significant leap forward for developers <a class="yt-timestamp" data-t="10:02:00">[10:02:00]</a>. These features included:
*   Promises <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>
*   `let` and `const` keywords <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>
*   Arrow functions <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>
*   Spread syntax <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>
*   Destructuring <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>

The introduction of these features also popularized transpilers like Babel and TypeScript, which allow developers to write code with modern [[new_javascript_features_in_2020 | JavaScript features]] while ensuring compatibility with older browsers by compiling back to earlier ECMAScript versions like ES3 <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>.

### Continuous Updates

Since ES2015, TC39 has adopted a regular annual release schedule for ECMAScript updates <a class="yt-timestamp" data-t="11:21:00">[11:21:00]</a>. For instance, ES2019 was expected soon after the summer of 2019 <a class="yt-timestamp" data-t="11:24:00">[11:24:00]</a>. This continuous evolution, coupled with a massive and diverse community, reinforces [[basics_of_javascript_and_its_history | JavaScript]]'s ongoing prominence <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a>.