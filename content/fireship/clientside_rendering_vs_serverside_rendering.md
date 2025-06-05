---
title: Clientside rendering vs Serverside rendering
videoId: Sklc_fQBmcs
---

From: [[fireship]] <br/> 

Web applications can render their content using different techniques, primarily [[Methods of HTML rendering and their impact on SEO | client-side rendering]] or [[Methods of HTML rendering and their impact on SEO | server-side rendering]]. Each method has distinct characteristics that affect performance, user experience, and [[Effective HTML rendering techniques for SEO | search engine optimization (SEO)]].

## Client-Side Rendering (CSR)

In a traditional [[JavaScript and Frontend Development | React]] application, content is rendered client-side <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The browser initially receives a nearly empty HTML page <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It then fetches a [[JavaScript and Frontend Development | JavaScript]] file containing the application's code, which subsequently renders the content and makes the page interactive <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

### Drawbacks of CSR
*   **SEO and Social Media Bots**: Content is not reliably indexed by all search engines or read by social media link bots <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **Performance**: It can take longer to reach the "first contentful paint," which is when a user first sees meaningful content on the web page <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Server-Side Rendering (SSR)

[[Front End and Back End Development | Server-side rendering]] (SSR) involves rendering content on the server *before* it is sent to the browser. When a user or search bot requests a page, they first receive the fully rendered HTML <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. After this initial page is received, [[JavaScript and Frontend Development | client-side rendering]] takes over, making the application interactive, similar to a traditional [[JavaScript and Frontend Development | React]] app <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Benefits of SSR
*   **SEO and Social Media Bots**: Fully rendered content is immediately available for bots to crawl <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   **Performance**: Users get rendered content quicker, improving the "first contentful paint" <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Next.js: A Hybrid Approach

Next.js is a framework that allows developers to build [[JavaScript and Frontend Development | React]] applications while rendering content in advance on the server <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This approach offers the best of both worlds: fully rendered content for bots and highly interactive content for users <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

Next.js provides multiple [[Data fetching strategies in Nextjs | server rendering strategies]] within a single project <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

### Next.js Core Concepts
*   **Pages Directory**: The `pages` directory in a Next.js project defines routes <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>. Each [[Using JavaScript on web and server environments | JavaScript]] file in this directory exports a [[JavaScript and Frontend Development | React]] component that represents a route <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>. The file structure directly mirrors the application's URLs <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>.
    *   **`_app.js`**: This file acts as the main entry point for the application, serving as a template for every individual page <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.
    *   **Dynamic Routes**: Next.js supports dynamic routes using bracket syntax in file names, e.g., `[paramname].js`, which allows the same component to render for variable parts of a URL <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>. The `useRouter` hook can be used to access query parameters from the URL <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>.
*   **API Directory**: The `api` directory is a special part of Next.js for setting up routes that apply only to the server <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>. Code here does not increase the client-side [[JavaScript and Frontend Development | JavaScript]] bundle <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>.
*   **`Head` Component**: Next.js provides a `Head` component to easily add [[Effective HTML rendering techniques for SEO | SEO-friendly]] titles and meta tags to the document's `<head>` section <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.

### [[Static generation and prerendering in Nextjs | Data Fetching Strategies]] in Next.js

Next.js offers two primary [[Data fetching strategies in Nextjs | data fetching]] and rendering options:

#### [[Static generation and prerendering in Nextjs | Static Generation (Pre-rendering)]]
[[Static generation and prerendering in Nextjs | Static Generation]], also known as pre-rendering, builds all HTML pages at *build time* <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. These static HTML files can then be uploaded to a storage bucket or static host and delivered with high performance via a CDN <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>.

*   **`getStaticProps`**: This function is implemented by a page or component to fetch data from a source (e.g., a database) at build time and pass it as props to the component <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.
*   **`getStaticPaths`**: For dynamic routes, Next.js needs to know all possible paths in advance to pre-render them <a class="yt-timestamp" data-t="09:26:00">[09:26:00]</a>. This function returns an array of route paths that Next.js should pre-render <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>.

*   **Trade-offs of Static Generation**:
    *   **Stale Data**: If the underlying data changes, the site needs to be rebuilt and redeployed for changes to be reflected <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>.
    *   **Scalability**: Pre-rendering millions of pages can be slow and difficult <a class="yt-timestamp" data-t="07:20:00">[07:20:00]</a>.
*   **Best Use Case**: [[Static generation and prerendering in Nextjs | Static Generation]] is well-suited for data that doesn't change often and for sites with a relatively low number of total pages, such as a blog <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>.

#### Server-Side Rendering (SSR in Next.js)
With SSR, the HTML content is generated on the server *each time it's requested* by a user <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

*   **`getServerSideProps`**: This function is implemented in a component to fetch data at *request time* <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>. It ensures the page fetches the latest data from the server for every new request <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

*   **Trade-offs of Server-Side Rendering**:
    *   **Efficiency**: Less efficient than static generation because a server is required to respond to every request, rather than serving cached content from a CDN <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>.
*   **Best Use Case**: Ideal when data changes constantly, ensuring users always receive the most up-to-date information, such as an e-commerce auction site <a class="yt-timestamp" data-t="10:40:00">[10:40:00]</a>.

#### Incremental Static Regeneration (ISR)
Next.js also offers a middle-ground approach called Incremental Static Regeneration (ISR). By adding a `revalidate` option to `getStaticProps`, Next.js can regenerate a page whenever a new request comes in, within a specified time interval <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.

The flexibility of Next.js allows developers to apply both static generation and [[Front End and Back End Development | server-side rendering]] paradigms wherever needed within an application <a class="yt-timestamp" data-t="11:32:00">[11:32:00]</a>.