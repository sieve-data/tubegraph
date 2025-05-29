---
title: Differences between client side and server side imports in Nextjs
videoId: yEoZ1VimtEU
---

From: [[swarajmakesstuff]] <br/> 

When migrating or developing applications with the Next.js App Router, understanding the distinction between client-side and server-side imports, particularly for data fetching and API interactions, is crucial <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a> <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. Next.js provides specific import paths depending on whether your component is running on the client or the server.

## Overview of API Import Paths <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>

There are generally three main import paths for API utilities, particularly with T3 stack or similar setups:

1.  `API from utils/API` <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>
2.  `API from trpc/server` <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>
3.  `API from trpc/react` <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>

## Import Usage Scenarios

### In the `pages` Directory

For components or pages residing within the traditional `pages` directory, you should import your API utilities using `API from utils/API` <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a> <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

### In the `app` Directory (App Router)

When working with the [[Nextjs Parallel Routes | App Router]] (`app` directory), the import strategy changes <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. You will use either `trpc/server` or `trpc/react` <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

#### Server Components

If your component is a [[Misconception about React Server Components | server component]], you must use `API from trpc/server` for your API imports <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a> <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

*   **Example Use Case**: Fetching data directly within an `async` server component <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a> <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

#### Client Components

For [[Clientside vs Serverside Components in React | client components]], you should import your API utilities using `API from trpc/react` <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a> <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

*   **`"use client"` Directive**: All client components must be explicitly marked with `"use client"` at the top of the file <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a> <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. This ensures that the component runs on the client-side.
*   **Hooks**: Within client components, you can use React hooks like `useQuery` for data fetching, similar to how you would in the `pages` directory <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a> <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

> [!CAUTION] Risky Import Practice
> While `API from utils/API` might occasionally work in client components within the App Router due to caching or specific configurations, it is considered risky and should be avoided <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a> <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. Always use `trpc/react` for client components in the App Router <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

## Related Navigation Changes

*   **`next/router` vs. `next/navigation`**: When migrating to the App Router, imports for routing functionalities shift from `next/router` to [[Using Nextjs navigation for routing | `next/navigation`]] <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a> <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **`usePathname`**: To get the current path in the App Router, instead of `router.asPath`, you would use `usePathname` from `next/navigation` <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a> <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.