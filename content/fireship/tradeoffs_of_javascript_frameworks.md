---
title: Tradeoffs of JavaScript frameworks
videoId: SJeBRW1QQMA
---

From: [[fireship]] <br/> 

JavaScript is described as a nearly perfect programming language, but it's often noted for "missing a good framework for building websites" <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Developers often try many [[JavaScript frameworks and their updates | JavaScript frameworks]], each with unique tricks, but all come with inherent [[Pros and cons of different full stack frameworks | trade-offs]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Understanding these trade-offs is crucial for [[Choosing the best JavaScript framework | choosing the best framework]] for a project <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Why Create a New JavaScript Framework?

The speaker highlights the frustration that can lead a developer to create their own [[JavaScript frameworks and their updates | JavaScript framework]] <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The speaker, in a satirical tone, introduces "Flamethrower" – a personal project aimed at creating a "game-changing platform for building blazingly fast highly interactive experiences on the jam stack" <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. This project, while presented humorously, stems from a genuine desire to address specific pain points with existing [[Comparison with other JavaScript frameworks | frameworks]] <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Framework Selection Flowchart

A common flowchart for [[Choosing the best JavaScript framework | choosing a framework]] for a new project involves several key questions <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>:

### Is the project highly interactive?
*   **No (regular website/AI)**: A [[JavaScript trends and frameworks | JavaScript framework]] may not be necessary.
    *   Opt for a static site generator like Hugo or 11ty <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
    *   If some JavaScript is needed, drop in lightweight options like Alpine or Petite Vue, or consider Astro which generates static HTML but allows for framework-based interactivity as required <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Yes (app with user authentication, data manipulation)**: Proceed to the next question <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### Does it need to be search engine friendly (SEO) or render HTML and data on a server?
*   **No**: Use a preferred framework to build a Single Page Application (SPA) <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Focus can be 100% on front-end user experience <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Yes**: Proceed to the next question <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### How often does the content change?
*   **Infrequently (e.g., a blog, Jamstack application)**:
    *   Pre-render content and cache it on a CDN <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   A [[JavaScript frameworks and their updates | JavaScript framework]] then "hydrates" and takes over after the initial page load <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
    *   Frameworks like Next.js and SvelteKit can do this in SSG (Static Site Generation) mode <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. Gatsby is also dedicated to this use case, though its popularity has declined <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **Highly Dynamic (constantly changing)**:
    *   Likely requires full Server-Side Rendering (SSR) to regenerate static content on the server with each new request <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
    *   Tools like Next.js, Nuxt, and SvelteKit are designed for this <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
    *   If unsure how a project will evolve, defaulting to a full SSR framework is recommended <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

## Complex Project Scenario: Course Platform

The speaker's personal project, a course platform, illustrates a complex set of requirements:
*   User authentication <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>
*   Highly interactive <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>
*   Good SEO <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>
*   Content doesn't change often (leaning towards Jamstack) <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>

This scenario initially points to a Jamstack option <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

### Challenges and Considerations

1.  **Content Management**:
    *   **SvelteKit**: While awesome, it's general-purpose and lacks extensive content management features compared to tools like Hugo <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
    *   **Re-implementing features**: Building content management features within SvelteKit is an option, but time-consuming <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
    *   **Performance**: Concerns about frameworks being slow when rendering large amounts of Markdown <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
    *   **Headless CMS**: Paid services like Contentful or Sanity add another expense <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
    *   **Self-hosted CMS**: Strapi is an option, but requires managing a separate server and database <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
    *   **Desired approach**: Write content in Markdown and manage it in a Git repository (GitHub serving as a "free content management system for developers") <a class="yt-timestamp" data-t="00:03:48">[00:03:50]</a>. This points back to static site generators, which excel at handling Markdown and templating <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. Astro seems like a perfect fit for this <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

2.  **State Management Across Routes**:
    *   **Astro**: When navigating, it results in full page loads, causing JavaScript to reboot and state (e.g., from Nano stores or Svelte stores) to be lost <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
    *   **SPA vs. Static**: Unlike Next.js, where a client-side router handles UI rendering with JavaScript after the initial load, static sites require careful consideration for persistent state like authentication tokens or real-time database data <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
    *   This problem leads back to frameworks that fully hydrate after the initial page load, such as Next.js <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
    *   Newer [[Emergence of frameworks and tools in modern JavaScript | cutting-edge frameworks]] like Qwik and SolidStart are also potential future options <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

## "Flamethrower" - The Solution

The speaker's custom library, "Flamethrower," was created to solve the problem of taking a static site and ensuring JavaScript functionality and data persistence between routes with zero latency during page transitions, without a framework taking over the entire DOM <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Essentially, it aims to provide a SPA-like router for static sites <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Inspiration and Mechanics
*   **Pjax and Turbolinks**: The concept is inspired by older libraries like pjax and Turbolinks <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Turbolinks (still popular with many npm downloads) works by preventing default link behavior, fetching HTML fragments asynchronously via `fetch`, swapping the `<body>` content, and updating the `<head>` with only the `delta` (changes) from the new page <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. This means JavaScript already executed on the previous page (like a global state management library) doesn't need to be re-executed on the next page load <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
*   **Why not just Turbolinks?**: The speaker's library is smaller and includes specific desired features <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

### Key Features and Philosophy
*   **Minimal JavaScript for Static UI**: A common annoyance is that 99% of a content-driven site's UI is static HTML, yet it's often managed entirely within a [[JavaScript frameworks and their updates | JavaScript framework]] <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. This requires special tooling (e.g., virtual DOM) and ties the project to a single framework <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
*   **Web Components Integration**: Instead, a different approach uses Web Components, which are natively supported in all browsers <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   They are a browser API for creating custom elements that encapsulate their own JavaScript and CSS <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   Frameworks like Lit and Stencil are dedicated to [[Building a todo app with different JavaScript frameworks | building web components]], and major [[Comparison of popular JavaScript frameworks in 2021 | frameworks]] can compile to them <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
    *   Web components can be used anywhere, like regular HTML elements, even in Markdown, without extra plugins <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
    *   They enable interoperability between frameworks (e.g., a Svelte-built web component used in a React or Angular app) <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
    *   This allows a static site generator to handle templates, while interactivity is added by simply declaring custom elements, akin to the "islands architecture" <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
    *   Web components are client-rendered, but server-rendered content can be projected into them and still be indexable by search engines <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **Web Components + Router Synergy**: Combining web components with the custom router allows them to render instantly between route changes, preserving state (like a Svelte store counter) across page loads, similar to a SPA, but with faster transitions <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   **Zero Dependencies**: The library relies entirely on browser native technology like `fetch` <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **Automatic Link Pre-fetching**: It finds visible links on the page and uses the Intersection Observer API to automatically pre-fetch them, allowing the browser to download pages in the background for instant rendering upon click <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Latency Logging**: A feature to log the time taken for each fetch operation <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Page Transitions API**: Integrates with the experimental Page Transitions API for native-like animations between page transitions, similar to a mobile app <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

## The "Meta Framework"

The speaker's resulting "meta framework" combines:
*   Svelte (compiled to web components) <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>
*   Hugo (as a static site generator for CMS features and fast builds) <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>
*   Flamethrower router (for SPA-like routing) <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>

## Conclusion

While this approach is a "proven technique" used on large sites like dev.to with Turbo, Flamethrower itself is experimental and not recommended for production until it reaches an alpha stage <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. For serious applications, it's advised to stick to established [[Alternatives and complements to JavaScript | libraries and frameworks]] like Next.js, SvelteKit, and Astro <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.