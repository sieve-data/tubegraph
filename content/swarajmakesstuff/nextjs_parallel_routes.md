---
title: Nextjs Parallel Routes
videoId: 9AMlt2ThybU
---

From: [[swarajmakesstuff]] <br/> 

Next.js introduces powerful routing features, including [[Nextjs Parallel Routes | parallel routes]] and intercepting routes, to enhance web application interactivity <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. These features allow for more dynamic and context-aware user experiences <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## What are Parallel Routes?

[[Nextjs Parallel Routes | Parallel routes]] enable the simultaneous conditional rendering of one or more pages within the same layout <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. They function similarly to `children` props in a React component, allowing multiple independent routes to be rendered side-by-side within a shared layout <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a> <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This means you can render different parts of your application, such as `/XYZ` and `/ABC`, in parallel within the same layout <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Implementation

In Next.js, a typical application structure includes an `app` directory with a `page.tsx` and a `layout.tsx` <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. The `layout.tsx` component is responsible for rendering its `children` <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

To implement [[Nextjs Parallel Routes | parallel routes]], you treat them as additional children props passed to your layout <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a> <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

```typescript
// Example: layout.tsx
import React from 'react';

export default function Layout({
  children,
  parallel, // This could be named anything, e.g., 'modal', 'name'
}: {
  children: React.ReactNode;
  parallel: React.ReactNode; // For TypeScript, specify React.ReactNode type
}) {
  return (
    <section>
      {children}
      {parallel} {/* Render the parallel route alongside children */}
    </section>
  );
}
```
<a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a> <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a> <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a> <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a> <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a> <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>

### Example Usage

An example application provided by Next.js for testing, similar to an Instagram application, showcases how [[Nextjs Parallel Routes | parallel routes]] can be used <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a> <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

### Default.js in Parallel Routes

When using [[Nextjs Parallel Routes | parallel routes]], particularly in combination with intercepting routes, the `default.js` or `default.tsx` file is crucial <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. If this file is missing, Next.js may encounter a 404 error because it cannot recover the active state of the current URL, especially upon a direct reload <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a> <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a> <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a> <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. The `default.js` page acts as a fallback while Next.js attempts to load the complete page or maintains its state until the full page is available <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a> <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. It is particularly important to include `default.js` when working with TypeScript <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a> <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

## Combined with Intercepting Routes

When [[Nextjs Parallel Routes | parallel routes]] are combined with intercepting routes, it's possible to have a parallel route that contains its own `page.tsx` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a> <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. This allows for complex UI patterns, such as rendering a modal over the current page that shows a different page for the same route without losing the context of the underlying page <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a> <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a> <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.