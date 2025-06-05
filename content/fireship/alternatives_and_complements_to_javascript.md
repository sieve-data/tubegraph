---
title: Alternatives and complements to JavaScript
videoId: f0DrPLKf6Ro
---

From: [[fireship]] <br/> 

While JavaScript is a dominant force in web development, new technologies and approaches are emerging that either complement its capabilities or offer alternatives for specific development needs <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Web Platform Enhancements

The web platform itself is gaining features that extend its capabilities, sometimes reducing the need for custom JavaScript solutions:

*   **Web Authentication API (WebAuthn)**: This API enables web applications to perform hardware-based authentication, including biometric authentication <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Native File System API**: This API allows web applications to access a user's local files, a long-desired feature for web developers <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. It is currently available in Chrome with a flag, but not widely supported <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **`loading` Attribute for Images and Iframes**: A native HTML attribute is now available for lazy loading images and iframes, eliminating the need for many JavaScript lazy loading libraries <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## Mobile Development Alternatives

For mobile applications, alternative programming languages and frameworks are gaining traction:

*   **SwiftUI**: Released by Apple in June 2019, SwiftUI offers a way to build declarative user interfaces similar to React, but using the Swift programming language <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. It aims to significantly enhance the iOS developer experience, though it is exclusive to iOS <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Flutter**: A significant disruptive force for building cross-platform applications for both iOS and Android <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Flutter uses the Dart programming language, which is syntactically very similar to JavaScript <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. In 2019, Dart was the fastest-growing programming language, and Flutter was a top open-source project on GitHub <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. Flutter also supports the web as a target in beta <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

## WebAssembly: A Powerful Complement

WebAssembly (Wasm) is a major disruption in the JavaScript ecosystem <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. As of a few days prior to 2020, WebAssembly became an official fourth language on the web, alongside JavaScript, HTML, and CSS <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

WebAssembly is not intended to replace JavaScript; rather, it complements it, enabling the development of a greater variety of applications and higher-quality applications that perform like desktop apps <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

### Use Cases and Examples

*   **Figma**: A notable example of WebAssembly's use is the design tool Figma. While its shell is built with React, the high-performance design tool within the shell is powered by WebAssembly <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Language Support**: Currently, languages like C, C++, and Rust can compile to WebAssembly <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
*   **Blazor**: Microsoft recently released Blazor, a framework that leverages WebAssembly to allow developers to build web applications using C#, HTML, and CSS <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. More languages are expected to elegantly interoperate with JavaScript in the future <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

## Backend-as-a-Service (BaaS)

For many web applications, building a custom backend is no longer necessary. Tools like AWS Amplify and Firebase continue to grow in popularity, offering a more productive alternative <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. These services provide all the necessary components to grow and scale mobile applications, allowing development teams to focus almost entirely on the frontend user experience <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.