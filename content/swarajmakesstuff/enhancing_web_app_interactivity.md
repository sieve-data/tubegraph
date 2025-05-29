---
title: Enhancing Web App Interactivity
videoId: 9AMlt2ThybU
---

From: [[swarajmakesstuff]] <br/> 

Next.js introduces advanced routing features, **intercepting routes** and **parallel routes**, designed to significantly enhance the interactivity of web applications <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. These features allow for more dynamic user experiences, such as managing multiple pages simultaneously or loading routes without losing the current page's [[handling_page_context_in_nextjs | context]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a> <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Parallel Routes

[[Features and Functionalities of the New Application | Parallel routes]] enable the rendering of one or more pages simultaneously, potentially conditionally, within the same layout <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a> <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. They function similarly to "children" props in a React component, allowing multiple independent segments of the UI to be rendered alongside each other within a given route <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a> <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### Implementation
In code, parallel routes are passed as props to a `layout.tsx` component, much like the standard `children` prop <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a> <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. They are typically named using an "@" prefix, such as `@parallel` or `@modal`, and are typed as `React.ReactNode` in TypeScript applications <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a> <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a> <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

```typescript
// Example layout.tsx structure
interface LayoutProps {
  children: React.ReactNode;
  parallel: React.ReactNode; // Or @modal, @name, etc.
}

export default function Layout({ children, parallel }: LayoutProps) {
  return (
    <>
      {children}
      {parallel}
    </>
  );
}
```
<a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a> <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a> <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>

## Intercepting Routes

[[Features and Functionalities of the New Application | Intercepting routes]] allow a route to be loaded within the current layout without losing the [[handling_page_context_in_nextjs | context]] of the original page <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a> <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This means the application can maintain the state, scroll position, and other details of the underlying page while displaying new content on top of it, such as a modal <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a> <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

A key benefit is the ability to render a completely different page layout based on the user's current position within the application, even for the same URL route <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a> <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. For example, navigating to `/photos/ID` from a 'feed' page might open a photo in a modal, preserving the feed's context, whereas directly visiting `/photos/ID` would display the photo on a standalone page <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a> <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a> <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

## Combining Parallel and Intercepting Routes

The combined use of parallel and intercepting routes allows for highly interactive experiences <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. For instance, an intercepted photo route can be rendered as a parallel route (e.g., a modal) <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a> <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. When a user clicks on a photo from a list, it might appear in a modal, preserving the list's [[handling_page_context_in_nextjs | context]] <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a> <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. However, if the page is reloaded, Next.js will display the photo as a full, standalone page, demonstrating the distinct behavior when directly accessing the route versus intercepting it within an existing flow <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a> <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

Naming conventions for combining these routes involve specific file structures like `(...)` for intercepting segments and `@name` for parallel routes, such as `@modal/(..)photos/[id]` <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a> <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

## The Importance of `default.js`

When implementing parallel and intercepting routes, especially with TypeScript, including a `default.js` (or `default.tsx`) file is crucial <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a> <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. If `default.js` is missing, reloading a page that utilizes an intercepted route can result in a 404 error <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a> <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

Next.js defines `default.js` as a fallback <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. When the application cannot immediately recover the active state of the current URL (e.g., upon a direct reload of an intercepted route), it loads `default.js` <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a> <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a> <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. Once the full page data is available, Next.js will then render the complete page, or retain `default.js` if the full page is not intended <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a> <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. Omitting this file bypasses this recovery step, leading to the 404 error <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.