---
title: Migrating from pages router to app router in T3 stack
videoId: yEoZ1VimtEU
---

From: [[swarajmakesstuff]] <br/> 

Migrating a T3 Stack application from the Pages Router to the App Router involves several key steps, focusing on architectural changes, navigation updates, and API route adjustments <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This guide outlines the process, ensuring a smooth transition while allowing both router versions to run concurrently during the upgrade <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Initial Setup and Prerequisites

To begin the migration:

1.  **Install Updates**: Update your Next.js project by installing the latest updates as per the Next.js documentation <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.
2.  **Concurrent Routers**: Ensure both the `pages` and `app` directories can run simultaneously. This allows for a gradual, route-by-route migration, making the process more manageable and convenient <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
3.  **Client-Side Assumption**: Initially, assume every component is client-side and mark them with `"use client"` at the top of the file to prevent errors related to server-side rendering expectations <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a> <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. This can be refined later if specific components truly need to be server components.
4.  **Navigation Imports**: Update all navigation-related imports. Previously, `router` was imported from `next/router`. Now, use `next/navigation` instead <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a> <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>. For example, to get the path name, use `usePathname` from `next/navigation` instead of `router.asPath` <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a> <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>.

## Migrating T3 Stack Architecture (TRPC)

The TRPC architecture needs to be adjusted for the App Router:

### File Structure Changes

*   A new `app` folder should be created under `src` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   TRPC configuration files, specifically those related to server-side setup, will need to be moved or duplicated into this new `app` structure <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

### Server-Side TRPC Adjustments

*   **Asynchronous Components**: Make your server-side TRPC components `async` <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **Headers as Parameters**: In the new architecture, TRPC will pass `headers` as parameters to your server-side TRPC context function <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Update your TRPC output to take `headers` as parameters instead of `response` and `request` objects <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. This means direct access to `clerk` user or `client ID` via `req` or `res` is no longer needed; use the `headers` object <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

### Client-Side vs. Server-Side TRPC Imports

The way you import your TRPC API differs based on whether you are in a client-side or server-side component:

*   **Pages Directory**: When using the Pages directory, import API from `utils/api` <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **App Directory (Server Components)**: For server components within the App directory, import API from `trpc/server` <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **App Directory (Client Components)**: For client components within the App directory, import API from `trpc/react` <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a> <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
    *   Client components can still use `useQuery` hooks as they did previously <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
    *   Remember to add `"use client"` at the top of client components <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

## Migrating API Routes

Migrating API routes from the Pages Router (`pages/api`) to the App Router (`app/api`) involves distinct changes <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>:

1.  **New Structure**: Move existing API routes into the `app/api` directory <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
2.  **Request/Response Imports**: Import `Request` from `next/server` instead of `next` <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. `Response` is also handled differently, often using `NextResponse` for server responses and redirects <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a> <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.
3.  **HTTP Method Specification**: Explicitly define the HTTP method (e.g., `GET`, `POST`) as an `async` function <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. For example:
    ```javascript
    export async function GET(request: Request) { /* ... */ }
    export async function POST(request: Request) { /* ... */ }
    ```
    If an endpoint needs to handle both `GET` and `POST` requests, you can define both functions within the same route file <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.
4.  **URL Parameters**: To get URL parameters, use `request.url` <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a> <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
5.  **Request Body**: To access the request body, use `request.body` instead of `request.body.json()` <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a> <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.

## Migrating Components and Layouts

After adjusting the core architecture and API routes, you can start moving individual components and layouts:

### Implementing Nested Layouts in Next.js App Router

*   To create a nested layout, create a new directory (e.g., `projects`) within your `app` folder <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
*   Inside this directory, add a `layout.tsx` file for the nested layout <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   Folders wrapped in curly brackets (e.g., `(dashboard)`) are not considered routes themselves but are used for organizing parts of the nested layout <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

### Handling Component Libraries without App Router Support

*   If using a component library (e.g., Material Tailwind) that lacks direct App Router support, a workaround may be necessary <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
*   One strategy is to create a top-level `layout.tsx` in the `app` directory that acts as a client component (`"use client"`) <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.
*   This client-side `layout.tsx` can then import and wrap the rest of your application's layout from a separate component, effectively isolating the client-side rendering requirements <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. This allows providers that need cookies (like TRPC providers) to remain in a server component <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a> <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>.

### Migrating Pages

*   When migrating a page, copy its contents to a new file (e.g., `page.tsx`) in the desired App Router location <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.
*   Remove any code specific to the Pages Router (e.g., `getServerSideProps`, `getStaticProps`) <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
*   If the page contains interactive elements or client-side hooks, mark it with `"use client"` <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.
*   Ensure all necessary wrappers (e.g., `ClockWrapper`, `ThemeProvider`) are applied to the new App Router layout structure <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

By following these steps, you can systematically migrate your T3 Stack application from the Pages Router to the App Router, leveraging the new features and improvements offered by the App Router <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.