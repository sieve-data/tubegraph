---
title: Handling Page Context in Nextjs
videoId: 9AMlt2ThybU
---

From: [[swarajmakesstuff]] <br/> 

Next.js introduces powerful routing features like [[Nextjs Parallel Routes]] and [[Nextjs Intercepting Routes]] that significantly enhance how web applications manage and maintain page context <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. These features allow for advanced interactivity, such as rendering multiple pages simultaneously or loading new routes without losing the state of the current page <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## [[Nextjs Parallel Routes]]

[[Nextjs Parallel Routes]] enable the simultaneous and conditional rendering of one or more pages within the same layout <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. They act like additional `children` components within a layout, allowing different routes to be rendered in parallel <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### Implementation
Within a `layout.tsx` file, in addition to the standard `children` prop, you can define and render parallel routes as separate props <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. For example, a layout might include `children` and a `@modal` prop, rendering both simultaneously <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

In code, a parallel route is typically named with an `@` prefix (e.g., `@modal` or `@parallel`) and passed as a prop to the layout component <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. When using TypeScript, these props should be typed as `React.ReactNode`, similar to the `children` prop <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

```typescript
// Example: app/layout.tsx
export default function RootLayout({
  children,
  modal, // This is a parallel route
}: {
  children: React.ReactNode;
  modal: React.ReactNode;
}) {
  return (
    <html>
      <body>
        {children}
        {modal} {/* Renders the parallel route */}
      </body>
    </html>
  );
}
```
<a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>

## [[Nextjs Intercepting Routes]]

[[Nextjs Intercepting Routes]] allow a route to be loaded within the current layout without losing the context of the page you are currently viewing <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This means the state and context of the current page are preserved, and the new route appears "above" or within the existing page <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

### Behavior
The key benefit of [[Nextjs Intercepting Routes]] is their conditional rendering of different layouts or pages for the same URL, based on the user's current location <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

For instance, consider a `/photos/[id]` route:
*   If a user directly navigates to `/photos/123`, it might render a full-page photo view <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   However, if the user is on their `feed` page and clicks on a photo link, an intercepting route can render a modal overlay for `/photos/123` instead, keeping the `feed` context intact <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. This means the same route (`/photos/[id]`) can have two different rendering behaviors depending on how it's accessed <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

## Combining Parallel and Intercepting Routes

When [[Nextjs Parallel Routes]] and [[Nextjs Intercepting Routes]] are combined, they enable complex user interfaces where new content can be displayed seamlessly without full page reloads <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. For example, an intercepted route could render content into a parallel route's slot (like a modal) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

When a user clicks on an element that triggers an intercepting route, the page might visibly change (e.g., a modal appears) <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. However, if the page is reloaded or directly accessed via its URL, Next.js will push to the "actual" full page for that route <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. This mechanism allows for a smooth in-app experience while ensuring direct URL access works as expected <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The ability to click back and retain the original page's context is a significant advantage <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### Naming Conventions for Intercepting Routes
Intercepting routes use specific naming conventions to define how many segments they "intercept":
*   `(.)` catches a segment in the same directory.
*   `(..)` catches a segment in the parent directory.
*   `(..)(..)` catches a segment two directories above.
*   `(...)` catches a segment from the root `/app` directory.

For example, an intercepting route for `photos/[id]` accessed from a `feed` page might be structured as `(.)photos/(.)[id]` relative to its location <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

## Importance of `default.js`/`default.tsx`

When implementing [[Nextjs Parallel Routes]] and [[Nextjs Intercepting Routes]], including a `default.js` (or `default.tsx` for TypeScript projects) file within the parallel route's directory is crucial <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

If `default.js` is missing, Next.js may fail to recover the active state of the current URL, especially upon page reload <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. Without it, the application might redirect to a 404 error page because it cannot immediately recover the state of the reloaded URL <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. The `default.js` page acts as a fallback, loading first until the complete page state can be recovered <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. This is particularly important for TypeScript applications <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.