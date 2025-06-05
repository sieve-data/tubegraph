---
title: Static site generators and JavaScript interactivity
videoId: SJeBRW1QQMA
---

From: [[fireship]] <br/> 

For projects that aren't highly interactive web applications, [[javascript_frameworks_and_their_updates | JavaScript frameworks]] are often unnecessary, with static site generators (SSGs) like Hugo or 11ty being a much simpler alternative <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. If [[using_javascript_on_web_and_server_environments | JavaScript]] functionality is required, lightweight options like Alpine or Petite Vue can be dropped in <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. Astro is another solution that generates static HTML but allows for interactivity from any framework as needed <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

## Choosing a Framework Based on Project Needs

When considering a project, a developer might ask:
1.  **Is the project highly interactive?** <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
    *   If "no," a [[javascript_frameworks_and_their_updates | JavaScript framework]] may not be needed <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Static site generators like Hugo or 11ty are more suitable <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. Lightweight [[using_javascript_on_web_and_server_environments | JavaScript]] options like Alpine or Petite Vue can be added if needed <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Astro is also an option, generating static HTML while allowing interactivity from any framework <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
    *   If "yes," consider SEO needs <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
2.  **Does it need to be search engine friendly or render HTML/data on a server?** <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
    *   If "no," a [[building_interactive_websites_with_spalike_features | single-page application (SPA)]] can be built without needing to render content in advance for search bots <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
    *   If "yes," consider how often the content changes <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
        *   **Infrequently changing content (e.g., blog):** This describes a Jamstack application <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. It's often more efficient to [[static_generation_and_prerendering_in_nextjs | pre-render content and cache it on a CDN]], then allow a [[javascript_frameworks_and_their_updates | JavaScript framework]] to hydrate it after the initial page load <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. Frameworks like Next.js and SvelteKit support this in SSG mode, as do dedicated tools like Gatsby <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
        *   **Highly dynamic content:** Full server-side rendering (SSR) is likely needed to regenerate static content on the server with each new request <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Next.js, Nuxt, and SvelteKit are designed for this <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. For uncertain project evolution, defaulting to a full SSR framework is recommended <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

## Challenges with Content Management and Interactivity

For content-driven sites requiring user authentication and good SEO, while content doesn't change frequently, a Jamstack option is suitable <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. While frameworks like SvelteKit are powerful, they may lack content management features compared to tools like Hugo <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

One approach is to handle content as Markdown in a Git repository, with GitHub serving as a free content management system for developers <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. Static site generators excel at handling Markdown and templating <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

A challenge with SSGs like Astro is sharing data or state between different routes <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. Full page loads on navigation mean [[using_javascript_on_web_and_server_environments | JavaScript]] reboots, and state from previous routes (e.g., authentication tokens or real-time data) is lost <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This contrasts with frameworks like Next.js, where a client-side router takes over after the initial load, preserving UI state across routes <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

## Integrating Interactivity with Static Sites

The goal is to enable [[using_javascript_on_web_and_server_environments | JavaScript]] functionality and data sharing between routes on a static site with zero latency during page transitions, without a framework taking over the entire DOM <a class="yt="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. This means creating a [[building_interactive_websites_with_spalike_features | SPA-like]] router for static sites <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Pjax and Turbo Links

An early solution, Pjax, asynchronously fetched HTML fragments to update the DOM without full page reloads <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. This evolved into Turbo Links, which remains popular <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

Turbo Links functions by:
*   Preventing the default link behavior when clicked <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   Using `fetch` to retrieve the new page <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   Swapping out the body of the page <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
*   Updating the `<head>` with any changes on the new page <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   Crucially, if [[using_javascript_on_web_and_server_environments | JavaScript]] (like a global state management library) was already executed on the previous page, it doesn't need to be re-executed on the next page load <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

### Web Components for Interactivity

A different approach, natively supported in browsers, is using Web Components <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. Web Components are a browser API for creating custom elements that encapsulate their own [[using_javascript_on_web_and_server_environments | JavaScript]] and CSS <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   Frameworks like Lit and Stencil are dedicated to building Web Components <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   Major [[javascript_frameworks_and_their_updates | JavaScript frameworks]] can also compile to Web Components <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   They can be used like regular HTML elements anywhere, even in Markdown, without extra plugins <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   They can be used between frameworks; for example, a Svelte-built Web Component can be accessed from React or Angular apps <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   This allows a static site generator to create templates, with interactivity added by simply declaring custom elements <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. This is similar to the "islands architecture," where there are isolated "islands" of interactivity <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   Web Components are client-rendered, not server-rendered <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. However, server-rendered content can be projected into a Web Component, which should be indexable by search engines <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

When Web Components are combined with a router, they render instantly between route changes <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This allows state from a [[using_javascript_on_web_and_server_environments | JavaScript]] store to persist across page navigations, similar to a [[building_interactive_websites_with_spalike_features | single-page application]], and provides a much faster page transition experience <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

### Flamethrower Router

The "Flamethrower" router, built with zero dependencies on browser-native technology like `fetch` <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>, aims to provide a [[building_interactive_websites_with_spalike_features | SPA-like]] router for static sites <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. It's similar to Turbo Links but offers additional features:
*   **Automatic Pre-fetching:** It finds all visible links on a page and automatically instructs the browser to pre-fetch them, downloading pages in the background for immediate rendering upon user click <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. This is made possible by pre-fetched link tags <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
*   **Intersection Observer API:** Used to lazily pre-fetch only the links currently visible on screen, as these are more likely to be clicked <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Latency Logging:** Setting `log` to `true` adds a timer to each `fetch` operation, showing route change latency, which should be under 100 milliseconds <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Page Transitions API:** A bonus feature that leverages the experimental Page Transitions API for native, animated page transitions (e.g., crossfade), similar to a native mobile app <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

This router allows for a meta-framework setup combining Svelte (compiled to Web Components) with Hugo (a static site generator) for strong CMS features, fast builds, and [[building_interactive_websites_with_spalike_features | SPA-like]] routing <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. This technique is used on large sites like dev.to with Turbo <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

However, "Flamethrower" is currently experimental and not recommended for production until it reaches an Alpha stage <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. For serious applications, it's advised to stick with established libraries and [[javascript_frameworks_and_their_updates | frameworks]] like Next.js, SvelteKit, or Astro <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.