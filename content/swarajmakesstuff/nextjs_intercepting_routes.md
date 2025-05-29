---
title: Nextjs Intercepting Routes
videoId: 9AMlt2ThybU
---

From: [[swarajmakesstuff]] <br/> 

[[Nextjs Intercepting Routes | Intercepting routes]] are a powerful Next.js feature designed to enhance web application interactivity and user experience by allowing a route to be loaded within the current layout without losing the context of the current page <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This means that the state and context of the originating page are preserved, even when a new route is displayed "above" it <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Core Concept

The primary benefit of [[Nextjs Intercepting Routes | intercepting routes]] is the ability to render a completely different layout based on the user's current position or context, even if the underlying route is the same <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This differs from traditional routing, where navigating to a new route typically replaces the entire page <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Example: Instagram Photo Modal

A common use case for [[Nextjs Intercepting Routes | intercepting routes]] is an Instagram-like photo modal:
*   When a user directly navigates to a photo's URL (e.g., `/photos/:id`), it renders a full dedicated page for that photo <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   However, if the user is browsing their feed (`/feed`) and clicks on a photo, an [[Nextjs Intercepting Routes | intercepting route]] can display that same photo within a modal *on top of the current feed layout*, preserving the feed's scroll position and state <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   The route (`/photos/:id`) is identical in both scenarios, but the rendered user interface (full page vs. modal overlay) changes based on the user's origin <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### Combining with [[nextjs_parallel_routes | Parallel Routes]]

[[Nextjs Intercepting Routes | Intercepting routes]] can be combined with [[nextjs_parallel_routes | parallel routes]] to create even more dynamic user experiences <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. For example, a modal could be implemented as an intercepting route within a [[nextjs_parallel_routes | parallel route]] <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

When viewing an intercepted route:
*   Clicking on it (e.g., a photo modal) shows the page changing dynamically <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   If the application is reloaded while an [[Nextjs Intercepting Routes | intercepted route]] (like a modal) is active, Next.js will push the user to the *full* dedicated page for that route, rather than redisplaying the intercepted modal <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

## Implementation Details

### Naming Conventions

For [[Nextjs Intercepting Routes | intercepting routes]], specific naming conventions are used to indicate the depth of interception:
*   `(...)` for intercepting a route at the same level <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   `..(...)` for intercepting a route one level up <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   `...(...)` for intercepting a route two levels up <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   `(....)` for intercepting a route from the root level <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

For example, to intercept `/photos/:id` with a modal from the feed, the path might look like `...modal/photos/[id]/page.tsx` within the app directory structure <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. This means that from the root, it's intercepting `photos/[id]` to render the modal.

### `default.js` Page

The `default.js` (or `default.tsx` for TypeScript) file is crucial when implementing [[Nextjs Intercepting Routes | intercepting routes]], especially in TypeScript projects <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
*   If `default.js` is not present, reloading a page that is currently displaying an intercepted route can lead to a 404 error <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
*   This happens because when Next.js cannot recover the active state of the current URL during a reload, it defaults to trying to load `default.js` <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   Without `default.js`, Next.js skips a necessary fallback step, resulting in a 404 <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. It's particularly important to include `default.js` when using TypeScript <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.