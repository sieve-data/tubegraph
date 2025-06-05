---
title: Creating a new JavaScript framework Flamethrower
videoId: SJeBRW1QQMA
---

From: [[fireship]] <br/> 

JavaScript is described as a nearly perfect programming language, with its only significant missing feature being a robust framework for building websites <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The creator of Flamethrower expressed frustration with the [[emergence_of_frameworks_and_tools_in_modern_javascript | JavaScript Frameworks]] available, noting that while many offer unique advantages, none are "marriage material" due to their inherent [[tradeoffs_of_javascript_frameworks | trade-offs]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This dissatisfaction led to the creation of a new, experimental [[javascript_frameworks_and_their_updates | JavaScript framework]] named Flamethrower <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Introducing Flamethrower

Initially conceived as "Holy JS," the name was changed to "Flamethrower" after finding the former already taken on npm, aiming to capture the essence of JavaScript programming <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Flamethrower is presented as a "game-changing platform" for building "blazingly fast, highly interactive experiences on the JAMstack" <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

> "I stole 99% of my ideas from other tools but I'm going to tell you that everything else sucks, give it an MIT license and then call you out if you try to steal it so one day I might be as successful as remix." <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>

This statement, though partially satirical, highlights the often-iterative nature of framework development <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## The Problem Flamethrower Aims to Solve

The impetus behind Flamethrower stems from a personal project: building a course platform requiring user authentication, high interactivity, and excellent SEO <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Despite the content not changing frequently, leading towards a JAMstack approach, existing solutions presented challenges <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Challenges with Existing Frameworks and Content Management

*   **SvelteKit:** While an "awesome framework," it is general-purpose and lacks extensive content management features compared to tools like Hugo <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. Re-implementing content management features or concerns about performance when rendering large amounts of Markdown were noted <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Headless CMS (e.g., Contentful, Sanity):** Adds another paid service to the stack <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Self-hosted CMS (e.g., Strapi):** Requires managing a separate server and database <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

The ideal solution involved managing content as Markdown in a Git repository, leveraging GitHub as a free content management system for developers <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

### Static Site Generators and State Management

Static site generators excel at handling Markdown and templating <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. Astro was considered a "perfect choice" due to its static HTML generation with optional interactivity from any framework <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. However, a key issue arose: how to share data or state between different routes <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

Static site generators often result in full page loads on navigation, causing JavaScript to reboot and state (like from Nano stores or Svelte stores) to be lost <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This contrasts with frameworks like Next.js, where a client-side router preserves UI state across routes after the initial load, which is crucial for managing authentication state or real-time data <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

This dilemma led back to the need for a framework that fully hydrates after the initial page load, or a solution that could combine the benefits of static sites with SPA-like navigation <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

## Flamethrower's Technical Approach

Flamethrower addresses the challenge of combining static sites with persistent JavaScript functionality and data across routes, aiming for zero-latency page transitions without a heavyweight framework dominating the entire DOM <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Essentially, it functions as an SPA-like router for static sites <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Inspiration and Core Mechanism

Flamethrower is inspired by older libraries like Pjax and Turbolinks <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. These libraries asynchronously fetch HTML fragments and update the DOM instead of full page reloads <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. Turbolinks, still popular today, works by:
1.  Preventing default link behavior <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
2.  Using `fetch` to retrieve the target page <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
3.  Swapping the `<body>` of the page <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
4.  Updating the `<head>` with only the changes (delta) from the new page <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

This approach ensures that JavaScript executed on the previous page, such as a global state management library, doesn't need to be re-executed on the next page load <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. Flamethrower was developed because Turbolinks was deemed too large and contained unnecessary features, and the creator wanted to add specific enhancements <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

### Key Features of Flamethrower

*   **Zero Dependencies:** Relies entirely on browser-native technologies like `fetch` <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **Web Components Integration:**
    *   Addresses the issue of 99% of UI being static HTML, but still managed by [[javascript_frameworks_and_their_updates | JavaScript Frameworks]] <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
    *   Web components are a browser API for creating custom elements that encapsulate their own JavaScript and CSS <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   They can be used like regular HTML elements anywhere, including Markdown, without extra plugins <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
    *   They allow interoperability between [[javascript_frameworks_and_their_updates | Frameworks]]; for example, a web component built with Svelte can be accessed from React or Angular apps <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
    *   This enables adding interactivity to static site generator templates by simply declaring custom elements, akin to the "islands architecture" <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
    *   While web components are client-rendered, projecting server-rendered content within them is believed to be indexable by search engines <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **Router & Web Component Synergy:** When combined, web components render instantly between route changes <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This allows state (e.g., a Svelte store's counter data) to persist across page navigations, similar to a single-page application, resulting in much faster page transitions <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   **Automatic Link Pre-fetching:** The router identifies visible links on the page and automatically uses `prefetched` link tags to tell the browser to download these pages in the background <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. It uses the Intersection Observer API to lazily pre-fetch only visible links, which are more likely to be clicked <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   **Latency Logging:** A debug feature allows logging the latency of fetch operations, showing transition times "well under 100 milliseconds" <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Page Transitions API (Bonus Feature):** Leverages the experimental Page Transitions API to enable native-like animations between page transitions, such as a crossfade animation, which is still under development in browsers <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

### Implementation Example

The Flamethrower setup involves an 11ty project with an `app` directory containing a Svelte app configured to compile to custom elements <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. Developers define a tag for each component and export them individually. The Flamethrower router is then initialized by calling it as a function <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

## Current Status and Recommendations

Flamethrower is currently an experimental proof-of-concept, using a technique proven on large sites like dev.to (with Turbo) <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. However, it is not recommended for production use as it has not yet reached Alpha status <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. For building serious applications, sticking to established [[javascript_frameworks_and_their_updates | Frameworks]] like Next.js, SvelteKit, and Astro is advised <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.