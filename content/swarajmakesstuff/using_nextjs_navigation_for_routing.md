---
title: Using Nextjs navigation for routing
videoId: yEoZ1VimtEU
---

From: [[swarajmakesstuff]] <br/> 

When migrating a T3 Stack application from the Next.js Pages Router to the App Router, several key changes occur in how routing and navigation are handled <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This includes updates to imports, component structure, and API route definitions.

## Navigating in the App Router

The primary change for navigation in the App Router is the shift from `next/router` to `next/navigation` <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

*   **Old way (Pages Router):**
    ```javascript
    import router from 'next/router';
    // ...
    router.asPath;
    ```
*   **New way (App Router):**
    ```javascript
    import { usePathname } from 'next/navigation';
    // ...
    const pathname = usePathname();
    ```
    To obtain the path name in the App Router, you should use `usePathname` instead of `router.asPath` <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.

## Migrating API Routes

API routes also undergo significant changes when moving from the Pages Router to the App Router <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.

### Directory Structure

API routes should be moved into the `app` directory, typically within a `source/app/api` folder <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

### Request and Response Objects

The `Request` and `Response` objects are now imported from `next/server` instead of `next` <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.

### Specifying Request Methods

In the App Router, you must explicitly specify whether an API route handles a GET or POST request by exporting named functions like `GET` or `POST` <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. If an API route needs to handle both GET and POST requests, you can define separate `GET` and `POST` asynchronous functions in the same file <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.

### Accessing Request Body and URL Parameters

*   **Request Body:** To get the body of a request, use `request.body` instead of `request.body.json` <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
*   **URL Parameters:** URL parameters are accessed via `request.url` <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

### Redirection

For redirection, `NextResponse.redirect` is used <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.

### Example for a GET request:

```javascript
import { NextResponse } from 'next/server'; // Or NextRequest

export async function GET(request) {
    // ... logic ...
    const url = request.url; // Get URL parameters
    return NextResponse.redirect('/settings'); // Redirect
}
```

### Example for a POST request:

```javascript
import { NextResponse } from 'next/server'; // Or NextRequest

export async function POST(request) {
    const body = await request.body; // Get the body of the request
    // ... logic ...
    return NextResponse.json({ message: 'Success' });
}
```