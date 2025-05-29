---
title: Handling API routes in Nextjs app router
videoId: yEoZ1VimtEU
---

From: [[swarajmakesstuff]] <br/> 

Migrating API routes from the Pages Router to the App Router in Next.js involves several key changes, particularly concerning how requests and responses are handled <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.

## Migrating an API Route
To move an API route, such as a LinkedIn callback route, follow these steps:
1.  Copy the existing code from your Pages Router API file into the new App Router API file <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
2.  Adjust the imports and function signatures to align with the App Router's conventions <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.

### Key Changes for API Routes in App Router

#### Request and Response Imports
In the App Router, you import `NextRequest` and `NextResponse` from `next/server` instead of `next` <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>, <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.

#### Specifying HTTP Methods
You must explicitly specify the HTTP method (e.g., GET, POST) for each API route by defining corresponding `async` functions (e.g., `GET`, `POST`) <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.

```typescript
// Example for a GET request
export async function GET(request: NextRequest) {
    // ... logic for GET request
}

// Example for a POST request
export async function POST(request: NextRequest) {
    // ... logic for POST request
}
```
If an API route handles both GET and POST requests, you can define separate `GET` and `POST` functions within the same file <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.

#### Accessing URL Parameters
To get the URL or query parameters from a request in the App Router, use `request.url` <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>, <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.

#### Handling Request Body
When accessing the request body, use `request.json()` for JSON bodies, in contrast to `request.body` which was used in the Pages Router for certain body types <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

#### Redirects
For server-side redirects, use `NextResponse.redirect()` <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.

```typescript
import { NextResponse } from 'next/server';

// ...
return NextResponse.redirect('/settings'); <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>
```

By following these guidelines, you can effectively move your API routes when [[migrating_from_pages_router_to_app_router_in_t3_stack | migrating from the Pages Router to the App Router]].