---
title: Using web components in modern web development
videoId: SJeBRW1QQMA
---

From: [[fireship]] <br/> 

Web components offer a different approach to [[javascript_and_frontend_development | web development]] by leveraging native browser capabilities <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. They are a browser API designed for creating custom elements that encapsulate their own JavaScript and CSS <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

## Benefits and Features
*   **Native Browser Support**: Web components are natively supported in all browsers <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
*   **Reusability**: They can be used anywhere, much like regular HTML elements <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   **Markdown Compatibility**: Web components can even be used within Markdown without requiring extra plugins or dependencies <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   **Framework Interoperability**: One significant advantage is their ability to be used across different [[javascript_trends_and_frameworks | frameworks]]. For example, a web component built with [[creating_components_and_implementing_reactivity_in_svelte_3 | Svelte]] can be accessed from a [[javascript_and_frontend_development | React]] or [[using_angular_components_and_component_architecture | Angular]] application <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

## Integration with Other Tools
While there are [[javascript_trends_and_frameworks | frameworks]] specifically for building web components, such as Lit and Stencil <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>, all major [[javascript_trends_and_frameworks | JavaScript frameworks]] can also compile to web components <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

Web components can be effectively combined with static site generators to add interactivity to templates by simply declaring custom elements <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. This approach is similar to the "islands architecture," where static HTML pages contain "islands" of interactivity <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

## Limitations
*   **Client-Side Rendering**: Web components are exclusively rendered on the client side and are never server-rendered <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **SEO Consideration**: Although web components themselves are client-rendered, it's possible to project server-rendered content within a web component, which is believed to be fully indexable by search engines <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

## Enhancing User Experience with Routers
When combined with a router, web components can render instantly between route changes <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This means that data from a previous route, such as a counter's state from a [[creating_components_and_implementing_reactivity_in_svelte_3 | Svelte]] store, is not lost during navigation, similar to a single-page application (SPA) <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. This significantly improves the perceived speed of page transitions for the end-user <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

This concept allows for the creation of a "meta framework" that uses [[creating_components_and_implementing_reactivity_in_svelte_3 | Svelte]] compiled to web components alongside a static site generator like Hugo <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. This setup provides content management features, fast builds, and routing that mimics a single-page application experience <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.