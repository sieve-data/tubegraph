---
title: Introduction to Nextjs
videoId: Sklc_fQBmcs
---

From: [[fireship]] <br/> 

Next.js is a framework that allows developers to build [[React Hooks explanation | React]] applications that are optimized for speed and search engines, often with zero configuration <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It addresses major drawbacks of traditional client-side [[React Hooks explanation | React]] applications by rendering content in advance on the server <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Drawbacks of Traditional Client-Side Rendering

In a traditional [[React Hooks explanation | React]] application, the browser starts with an empty HTML shell, then fetches JavaScript to render content and make it interactive <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This approach has two main issues:
1.  **SEO and Social Media Bots**: Content is not reliably indexed by all search engines or read by social media link bots <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
2.  **Performance**: It can take longer to reach the "first contentful paint," which is when a user first sees meaningful content on the page <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Next.js Approach

Next.js combines the best of both worlds <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>:
*   It renders content on the server so that the initial page seen by users or search bots is fully rendered HTML <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   After the initial page is received, client-side rendering takes over, and the application functions like a traditional [[React Hooks explanation | React]] app, providing highly interactive content <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
*   This approach ensures fully rendered content for bots and highly interactive content for users <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Setting Up a Next.js Project

To start a new Next.js application, use the following command in your terminal:
```bash
npx create-next-app [your-app-name]
```
<a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>
Once the project is set up, navigate into the project directory. To run the application in development mode, execute:
```bash
npm run dev
```
<a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>
This will typically run the app on `localhost:3000` <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

## Project Structure

A Next.js project has a specific directory structure:

*   **`pages` directory**: This is where all pages and routes for the application are defined <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Each JavaScript file within this directory exports a [[React Hooks explanation | React]] component that represents a route <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. The file structure directly mirrors the URLs a user will navigate to <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
    *   **`_app.js`**: This file acts as the main entry point into the application, serving as a template for every individual page <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
    *   **`index.js`**: This file defines the component for the root URL (`/`) <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
    *   **`api` directory**: A special part of Next.js for setting up server-only routes <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. Code here does not increase the client-side JavaScript bundle <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

## Routing

Next.js provides its own router for seamless navigation <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### File-System Based Routing
To create a new route, simply create a new JavaScript file in the `pages` directory. For example, creating `hello.js` that exports a default [[React Hooks explanation | React]] component will make the content available at `/hello` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. Every file or page must have one default export <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### [[Dynamic routing in Nextjs | Dynamic Routes]]
For routes with variable segments (e.g., `/cars/tesla` or `/cars/ford`), [[Dynamic routing in Nextjs | dynamic routing]] can be implemented by creating a file named `[paramname].js` inside a directory (e.g., `pages/cars/[id].js`) <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. The brackets make the route dynamic <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

To access the dynamic parameter (e.g., `id`), the `useRouter` [[React Hooks explanation | hook]] from `next/router` can be used within the component <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

## Styling

Next.js supports CSS modules, which allows for defining styles that apply only to a specific route or component, avoiding global naming conflicts <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Global styles can be defined in a `globals` file (e.g., `styles/globals.css`) <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Styles from a module are imported and referenced as if they were a JavaScript object <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

## [[Data fetching strategies in Nextjs | Data Fetching]] Strategies

Next.js's most valuable feature is its ability to perform multiple server rendering strategies from a single project <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This ensures faster rendered content for users and reliable crawling by search bots <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### [[Static generation and prerendering in Nextjs | Static Generation (Pre-rendering)]]
[[Static generation and prerendering in Nextjs | Static generation]] involves generating all HTML at build time <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. The generated HTML files can be uploaded to a storage bucket or static host and delivered efficiently via a CDN <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

*   **`getStaticProps`**: This function is implemented in a page or component to fetch data at build time <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. The fetched data is then passed as props to the component <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. Next.js automatically calls this function when building the site <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   **`getStaticPaths`**: For [[Dynamic routing in Nextjs | dynamic routes]], Next.js needs to know all possible IDs in advance to pre-render those pages <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. This function fetches data (e.g., a list of IDs) and returns a `paths` object containing an array of every route for the dynamic URL <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.

Static generation is best suited for data that doesn't change often and for sites with a relatively low number of pages, such as a blog <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. The main trade-offs are that data can become stale if not rebuilt and redeployed, and it can be slow to pre-render millions of pages <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

### Server-Side Rendering (SSR)
With SSR, content is generated on a server each time it's requested by a user <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

*   **`getServerSideProps`**: This function is implemented in a component to fetch data at request time <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. It fetches the latest data on the server with every new request <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

SSR is ideal for pages with rapidly changing data, ensuring users always get the latest information <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. However, it's less efficient than static generation because it requires a server to respond to every request, unlike static content that can be cached on a global CDN <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

### Incremental Static Regeneration (ISR)
ISR offers a middle ground by allowing Next.js to regenerate a page whenever a new request comes in within a certain time interval, by simply adding a `revalidate` option to `getStaticProps` <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

## Search Engine Optimization (SEO)

Next.js makes it easy to add SEO-friendly titles and meta tags to the head of the document using the `Head` component imported from `next/head` <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. Anything placed inside this component will be rendered to the document's head <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.