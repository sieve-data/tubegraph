---
title: New JavaScript features in 2020
videoId: f0DrPLKf6Ro
---

From: [[fireship]] <br/> 

Predicting the future of JavaScript is challenging, especially for developers who will be spending their careers in its evolving landscape <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article explores new features arriving in the language, the current state and new releases of front-end [[javascript_frameworks_and_their_updates | frameworks]], and [[disruptive_trends_in_the_javascript_ecosystem | disruptive trends]] that could reshape the ecosystem in 2020 <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Core JavaScript Language Features

Eight finished proposals were slated for publication in 2020, many of which are already available in browsers, Node.js, and TypeScript <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. The process for new features to enter the language is managed by Technical Committee 39 (TC39) <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

### Dynamic Imports

This feature allows modules to be imported lazily at runtime, meaning imports are no longer restricted to static declarations at the top of a file <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Modules can be loaded asynchronously from anywhere in the code, improving performance by delaying non-essential dependencies <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. For example, a module could be awaited as a promise when a user clicks a button <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### Optional Chaining (`?.`)

Also known as the "Elvis operator," optional chaining allows access to deeply nested object properties without throwing an error if an intermediate parent property is `undefined` <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. It's a useful replacement for functions like `lodash.get` and prevents runtime errors when working with APIs or databases that return complex, potentially incomplete, nested objects <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### Nullish Coalescing Operator (`??`)

Similar in appearance to optional chaining, the nullish coalescing operator sets a default value for a property only when it is `null` or `undefined` <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Unlike the logical OR (`||`) operator, which can be problematic because it coerces `0` or empty strings (`""`) to `false`, the nullish coalescing operator provides more predictable code when setting default values <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### BigInt

JavaScript is introducing a new primitive data type: `BigInt` <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. It can represent numbers beyond JavaScript's `MAX_SAFE_INTEGER` value, which is limited to 64 bits <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. A `BigInt` can be created by appending `n` to a regular integer or by using the `BigInt` constructor <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. While not needed by most developers, it's useful for extremely precise timestamps or geometric calculations <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## [[disruptive_trends_in_the_javascript_ecosystem | Disruptive Trends]] and Ecosystem Updates

### TypeScript Growth

TypeScript, which first appeared on the 2016 Stack Overflow survey used by less than 0.5% of developers, has become a top ten language, used by over 20% of developers within three years <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. It is widely adopted and well-regarded by both front-end and back-end developers across various [[javascript_frameworks_and_their_updates | frameworks]] <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### Web Components

While Web Components saw increased adoption in 2019, it was not as significant as predicted and faced considerable criticism <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. However, tools like Stencil and Lit Element (a Google-sponsored project) are dedicated to building Web Components and have been gaining momentum <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

### [[javascript_frameworks_and_their_updates | Front-End Framework Updates]]

*   **Svelte:** Svelte 3, released in April 2019, generated significant excitement due to its elegant, easy-to-learn package, high performance, and lack of runtime dependencies <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. Its npm downloads tripled over the past year <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   **React:** React remains a dominant force in terms of adoption and job openings <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. A significant experimental feature is **Concurrent Mode**, which allows the [[javascript_frameworks_and_their_updates | framework]] to handle multiple state updates simultaneously <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This opens the door for a new built-in component called **Suspense**, enabling declarative handling of loading states by waiting for asynchronous activity (e.g., API calls, dynamic imports of React components) to finish <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   **Angular:** The major update in Angular 9 is **Ivy**, an entirely new compiler enabled by default <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. Additionally, a static site generator for Angular was expected to release an alpha version, allowing comparison with tools like Gatsby and VuePress <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Vue:** A significant new feature for Vue is the **Composition API** <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. This set of tools aims to improve code reusability in complex Vue applications by exposing core capabilities like reactive state as functions, enabling composition of more complex components that are easier to strongly type with TypeScript <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

### Web Platform Enhancements

The web platform itself gained new features that extend the types of applications that can be built:

*   **Web Authentication API (WebAuthn):** This API enables web applications to use hardware-based authenticators for biometric authentication <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Native File System API:** This API can grant web applications access to a user's local files, a long-desired capability for web developers <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. It is currently available in Chrome with a flag <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **`loading` Attribute for Images and Iframes:** This new HTML attribute natively supports lazy loading for images and iframes, eliminating the need for JavaScript libraries for this functionality <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### Node.js Updates

[[using_javascript_on_web_and_server_environments | JavaScript is not limited to the browser]]; Node.js continues to evolve:

*   **Worker Threads:** This is a significant new feature for Node.js, addressing the long-standing limitation of JavaScript being single-threaded <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. Worker threads allow JavaScript to execute in parallel <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   **ES Modules Support:** Node 13 shipped with support for ES modules, allowing the use of `import` and `export` statements instead of `require` <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **NestJS:** One of the fastest-growing back-end tools for Node, NestJS leverages TypeScript to build scalable and developer-friendly server-side applications <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. It also facilitates integration with GraphQL <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   **GraphQL:** This trend has been growing for several years and continues to expand <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   **Backend as a Service:** Many web applications no longer require custom backends <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. Tools like AWS Amplify and Firebase continue to grow, providing comprehensive solutions for mobile application development and scaling, allowing teams to focus on the front-end user experience <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

### Mobile JavaScript Frameworks

*   **React Native, Ionic, NativeScript:** These frameworks for mobile applications remained relatively flat in npm downloads over the past year <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. React Native added improvements like fast refresh, and Ionic now supports React in addition to Angular <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

### Emerging Non-JavaScript Technologies and WebAssembly

*   **SwiftUI:** Released by Apple in June 2019, SwiftUI offers a declarative UI building approach similar to React, but using the Swift programming language, aiming to enhance the iOS developer experience <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   **Flutter:** For cross-platform iOS and Android development, Flutter is a major disruptive force <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. It uses the Dart programming language, which is syntactically similar to JavaScript <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. In 2019, Dart was the fastest-growing programming language, and Flutter was one of the hottest open-source projects on GitHub <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. It also supports the web as a target in beta <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
*   **WebAssembly:** An even greater disruption to the [[disruptive_trends_in_the_javascript_ecosystem | JavaScript ecosystem]] is WebAssembly <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. It officially became the fourth language of the web (alongside JavaScript, HTML, and CSS) just prior to 2020 <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. WebAssembly complements JavaScript, enabling the creation of a wider variety of higher-quality applications, rivaling desktop apps <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. Figma, for instance, uses React as its shell, but its high-performance design tool is powered by WebAssembly <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
    *   Currently, languages like C, C++, and Rust can compile to WebAssembly <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
    *   Microsoft's new **Blazor** [[javascript_frameworks_and_their_updates | framework]] leverages WebAssembly to allow building web applications using C#, HTML, and CSS <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
    *   The future is expected to see more languages elegantly interoperating with JavaScript <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

### Other Notable Tools

The broader JavaScript world also sees advancements in various tools:

*   **Cypress:** Changing how applications are tested <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Gatsby:** Altering how JavaScript applications are built <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
*   **XState:** Offering new approaches to state management <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.