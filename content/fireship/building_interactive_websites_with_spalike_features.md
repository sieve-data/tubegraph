---
title: Building interactive websites with SPAlike features
videoId: SJeBRW1QQMA
---

From: [[fireship]] <br/> 

Developing websites today involves navigating a complex landscape of [[JavaScript and Frontend Development|JavaScript and frontend development]] frameworks, each with its own trade-offs <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. While [[JavaScript and Frontend Development|JavaScript]] is considered a "nearly perfect" programming language, finding a single framework that meets all needs for website building is a persistent challenge <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article explores a strategic approach to choosing the right tools, including a discussion of a novel library designed to combine the benefits of static sites with the dynamic feel of Single Page Applications (SPAs).

## Choosing a JavaScript Framework: A Flowchart Approach

When starting a new project, a developer might follow a specific decision-making process to select the most appropriate framework <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>:

1.  **Is the project highly interactive?** <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
    *   **No (Regular Website)**: A [[static_site_generators_and_javascript_interactivity|static site generator]] like Hugo or 11ty is often sufficient <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. For minor interactivity, light [[JavaScript and Frontend Development|JavaScript]] libraries like Alpine or Petite-Vue can be dropped in <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Astro is another option that generates static HTML but allows for bringing in interactivity from any framework as needed <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
    *   **Yes (Highly Interactive App)**: Proceed to the next question <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

2.  **Does it need to be search engine friendly (SEO) or render HTML/data on a server?** <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>
    *   **No**: Use a preferred framework to [[building_web_apps_with_various_programming_languages|build a Single Page Application]] (SPA), focusing entirely on the frontend user experience <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
    *   **Yes (Requires SEO)**: Proceed to the next question <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

3.  **How often does the content change?** <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
    *   **Infrequently (e.g., a blog - Jamstack application)**: Pre-render content and cache it on a CDN, allowing a [[JavaScript and Frontend Development|JavaScript]] framework to "hydrate" it after the initial page load <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Frameworks like Next.js and [[using_svelt_for_front_end_development|SvelteKit]] support this in SSG (Static Site Generation) mode, as does Gatsby <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
    *   **Highly Dynamic (constantly changing)**: Full Server-Side Rendering (SSR) is likely needed to regenerate static content on the server with each new request <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Next.js, Nuxt, and [[using_svelt_for_front_end_development|SvelteKit]] are designed for this <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. If uncertainty exists about project evolution, defaulting to a full SSR framework is recommended <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

## The Search for a "Perfect" Fit

The speaker faced a personal project (hosting courses) requiring user authentication, high interactivity, and excellent SEO, with content that doesn't change frequently <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. This points towards a Jamstack application <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

Initial work with [[using_svelt_for_front_end_development|SvelteKit]] proved challenging due to its general-purpose nature and lack of built-in content management features compared to tools like Hugo <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. Re-implementing content management features or relying on external headless CMS solutions (like Contentful, Sanity, or self-hosted Strapi) presented their own complexities and costs <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

The ideal solution was to manage content in Markdown files within a Git repository <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This led back to [[static_site_generators_and_javascript_interactivity|static site generators]], which excel at handling Markdown and templating <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. Astro seemed promising, but a key challenge emerged: sharing data or state between different routes <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. With a full page load on navigation, [[JavaScript and Frontend Development|JavaScript]] reboots, and state (e.g., user authentication with JWTs from Firebase) is lost <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This problem typically leads back to frameworks like Next.js that fully hydrate after the initial page load <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

## "Flamethrower": A Custom SPA-like Router for Static Sites

Faced with these trade-offs, the speaker developed a custom [[JavaScript and Frontend Development|JavaScript]] library, humorously named "Flamethrower," to address the desire for static site benefits combined with SPA-like routing <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. The goal was to share [[JavaScript and Frontend Development|JavaScript]] functionality and data between routes with zero latency on page transitions, without a framework taking over the entire DOM <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

This library has zero dependencies and relies on browser-native technologies like `fetch` <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. It draws inspiration from older libraries like pjax and Turbolinks <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### How it Works

When a link is clicked, the router:
1.  Prevents the default browser navigation <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
2.  Uses `fetch` to retrieve the content of the new page <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
3.  Swaps out the `<body>` of the current page with the new content <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
4.  Updates the `<head>` with only the changes (delta) from the new page <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

This approach means that global [[JavaScript and Frontend Development|JavaScript]] (like a state management library) executed on the previous page does not need to be re-executed on the next page load, preserving state across routes <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

### Incorporating [[using_web_components_in_modern_web_development|Web Components]]

A crucial part of this strategy is the use of [[using_web_components_in_modern_web_development|web components]] <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. These are browser APIs for creating custom elements that encapsulate their own [[JavaScript and Frontend Development|JavaScript]] and CSS <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

*   **Framework Agnostic**: [[using_web_components_in_modern_web_development|Web components]] can be used like regular HTML elements anywhere, even in Markdown, without extra plugins or dependencies <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. They can also be used between different frameworks (e.g., a [[using_svelt_for_front_end_development|Svelte]]-built [[using_web_components_in_modern_web_development|web component]] in a React or Angular app) <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   **Interactivity "Islands"**: This allows using a [[static_site_generators_and_javascript_interactivity|static site generator]] and then adding interactivity to templates by simply declaring custom elements, akin to the "islands architecture" <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
*   **Client-Side Rendering**: It's important to note that [[using_web_components_in_modern_web_development|web components]] are rendered only on the client-side <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. However, server-rendered content can be projected into a [[using_web_components_in_modern_web_development|web component]], which is likely indexable by search engines <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

When [[using_web_components_in_modern_web_development|web components]] are combined with the router, they render instantly between route changes <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This allows data (e.g., from a [[using_svelt_for_front_end_development|Svelte]] store) to persist across routes, similar to a SPA, leading to a much faster page transition feel for the user <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

### Technical Implementation

The demonstration involves an 11ty project with a [[using_svelt_for_front_end_development|Svelte]] app directory configured to compile to custom elements <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. Developers define a tag for each component and export them individually, then initialize the "Flamethrower" router <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### Router Features

"Flamethrower" includes additional features beyond typical link handling:
*   **Automatic Link Pre-fetching**: It finds all visible links on the page and tells the browser to pre-fetch them, downloading pages in the background for immediate rendering upon click <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. This is achieved using `prefetched link` tags and the Intersection Observer API to only pre-fetch links visible on the screen <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Latency Logging**: A timer can be added to fetch operations to measure latency, which typically shows blazing fast results under 100 milliseconds <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Page Transitions API**: The router takes advantage of the new, experimental Page Transitions API, allowing native animations between page transitions, similar to a native mobile app <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Conclusion

This approach allows for creating a "meta-framework" using [[using_svelt_for_front_end_development|Svelte]] compiled to [[using_web_components_in_modern_web_development|web components]], combined with a [[static_site_generators_and_javascript_interactivity|static site generator]] like Hugo for content management. This setup provides excellent CMS features, extremely fast builds, and routing that feels like a Single Page Application <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. While "Flamethrower" is an experimental library and not yet recommended for production <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>, the technique itself is proven and used on large sites like Dev.to with Turbo <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. For serious applications, it's advised to stick to established frameworks like Next.js, [[using_svelt_for_front_end_development|SvelteKit]], and Astro <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.