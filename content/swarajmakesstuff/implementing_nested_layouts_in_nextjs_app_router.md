---
title: Implementing nested layouts in Nextjs app router
videoId: yEoZ1VimtEU
---

From: [[swarajmakesstuff]] <br/> 

When [[migrating_from_pages_router_to_app_router_in_t3_stack | migrating a T3 stack application from the Pages Router to the App Router]], a key step is to implement nested layouts for your application's structure <a class="yt-timestamp" data-t="09:27:03">[09:27:03]</a>. The App Router allows for concurrent use with the Pages directory, which simplifies the migration process by allowing individual routes to be moved simultaneously <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>, <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

Initially, it's recommended to assume each component is client-side and mark it with `'use client'` to prevent errors <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Basic Nested Layout Implementation

For implementing a nested layout, consider a scenario where certain pages, like a "projects" section, require a distinct layout that differs from the main application layout <a class="yt-timestamp" data-t="09:56:00">[09:56:00]</a>.

To achieve this:
1.  Create a new directory within your `app` folder corresponding to the nested route, e.g., `app/projects` <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.
2.  Inside this new directory, create a `layout.tsx` file <a class="yt-timestamp" data-t="10:15:00">[10:15:00]</a>. This `layout.tsx` will define the nested layout for all routes within the `projects` directory.

### Handling Non-Route Nested Parts

If you have a nested directory that is part of the URL structure but is not intended to be a route itself (e.g., a grouping of pages), you can use curly brackets `{}` around the directory name. This indicates that it's a nested part of the structure, not a separate route <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>, <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>, <a class="yt-timestamp" data-t="10:35:00">[10:35:00]</a>.

## Workarounds for Client Component Libraries

Challenges may arise when using component libraries that do not yet have full App Router support. For instance, if a library like Material Tailwind doesn't support the App Router, attempting to wrap your main layout with its components might necessitate making the entire component client-side <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>, <a class="yt-timestamp" data-t="10:52:00">[10:52:00]</a>, <a class="yt-timestamp" data-t="10:55:00">[10:55:00]</a>. This is because the library's `ThemeProvider` might wrap its children, causing the children to be treated as client components if the `ThemeProvider` itself is client-side <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>, <a class="yt-timestamp" data-t="11:15:00">[11:15:00]</a>, <a class="yt-timestamp" data-t="11:18:00">[11:18:00]</a>. This can conflict with server components that might be using server-side features like `trpc` providers that rely on cookies <a class="yt-timestamp" data-t="11:25:00">[11:25:00]</a>, <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>.

### Suggested Workaround:
1.  Wrap your entire application in a structure like `app/[app]/layout.tsx` <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>, <a class="yt-timestamp" data-t="11:39:00">[11:39:00]</a>.
2.  Make this wrapper layout a client component by adding `'use client'` at the top <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>, <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>.
3.  Inside this client-side layout, import your main layout component and pass `children` to it <a class="yt-timestamp" data-t="11:56:00">[11:56:00]</a>, <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>. This allows the inner layout to be client-side while the outer `app/layout.tsx` remains server-side, providing cookies or other server-side context where needed <a class="yt-timestamp" data-t="12:13:00">[12:13:00]</a>.

## Wrapping with Other Providers

After establishing the layout structure, you'll need to wrap your application's layout with other necessary providers such as Clerk wrapper, Lens wrapper, and Theme Provider <a class="yt-timestamp" data-t="12:54:00">[12:54:00]</a>, <a class="yt-timestamp" data-t="13:01:00">[13:01:00]</a>, <a class="yt-timestamp" data-t="13:05:00">[13:05:00]</a>, <a class="yt-timestamp" data-t="13:07:00">[13:07:00]</a>, <a class="yt-timestamp" data-t="13:08:00">[13:08:00]</a>, <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>.

### Next.js Navigation API
During layout migration, ensure you update navigation imports. Instead of importing `router` from `next/router`, you will now import from [[using_nextjs_navigation_for_routing | `next/navigation`]] <a class="yt-timestamp" data-t="01:06:06">[01:06:06]</a>, <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. For obtaining the current path name, use `usePathname()` from `next/navigation` instead of `router.asPath` <a class="yt-timestamp" data-t="14:14:00">[14:14:00]</a>, <a class="yt-timestamp" data-t="14:18:00">[14:18:00]</a>, <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>, <a class="yt-timestamp" data-t="14:22:00">[14:22:00]</a>, <a class="yt-timestamp" data-t="14:24:00">[14:24:00]</a>.