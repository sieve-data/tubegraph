---
title: Hono web framework for edge deployments
videoId: Cbwq8lUeyLk
---

From: [[amiteshanand]] <br/> 

Hono is a lightweight web framework optimized for Edge and Serverless deployments <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. It is designed to have a very low bundle size <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Key Features

Hono provides features common in modern JavaScript frameworks out of the box, including:
*   Server-Side Rendering <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>
*   TypeScript support <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>

It allows developers to utilize Node.js-based npm modules, providing a server-like experience without needing a dedicated Node.js server, similar to how Next.js operates <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Deployment Options

Hono can be easily deployed with various platforms:
*   Cloudflare Workers <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   Vercel Edge <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   Deno <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>
*   Bun <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>
*   Cloudflare Pages (for Hono projects) <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>

The `wrangler.toml` file is used for deploying Hono projects with Cloudflare Workers or Pages, allowing configuration for Cloudflare features like Key Value storage or R2 bucket storage <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

## Application Example

In an example application, Hono JS was used to build a retrieval augmented generation (RAG) application focused on finding similar planets in the Star Wars universe <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. The `index.tsx` TypeScript file within the Hono app handles the main logic, including connecting to the Couchbase database and performing vector searches <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.