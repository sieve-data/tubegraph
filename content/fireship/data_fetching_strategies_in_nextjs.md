---
title: Data fetching strategies in Nextjs
videoId: Sklc_fQBmcs
---

From: [[fireship]] <br/> 

[[introduction_to_nextjs | Next.js]] is a framework for building [[React Hooks explanation | React]] applications that creates fast, search engine optimized apps with zero configuration <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It addresses major drawbacks of traditional client-side rendering by allowing content to be rendered in advance on the server <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Client-Side Rendering Drawbacks

A traditional [[React Hooks explanation | React]] application is rendered client-side, meaning the browser initially receives an empty HTML page <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The browser then fetches JavaScript files containing the [[React Hooks explanation | React]] code to render content and make the page interactive <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This approach has two main drawbacks:
*   Content is not reliably indexed by all search engines or read by social media link bots <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   It can take longer to reach the "first contentful paint" when a user initially lands on the page <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Next.js Approach to Rendering

[[introduction_to_nextjs | Next.js]] allows you to build a [[React Hooks explanation | React]] app where the content is rendered in advance on the server <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. This means the first thing a user or search bot sees is fully rendered HTML <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. After this initial page is received, client-side rendering takes over, functioning like a traditional [[React Hooks explanation | React]] app <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. This approach offers the best of both worlds: fully rendered content for bots and highly interactive content for users <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

The core of [[introduction_to_nextjs | Next.js]] data fetching capabilities lies in its ability to perform multiple server rendering strategies from a single project <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Static Generation (Pre-rendering)

[[static_generation_and_prerendering_in_nextjs | Static generation]], also known as [[static_generation_and_prerendering_in_nextjs | pre-rendering]], involves generating all the HTML for pages at build time <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. These HTML files can then be uploaded to a storage bucket or static host and delivered with high performance over a CDN <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

### Implementation with `getStaticProps`
Each page or component can implement a function called `getStaticProps` <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. This function might fetch data from a cloud database and then pass that data as props to the component <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. When you build your [[building_a_nextjs_application_with_redis | Next.js application]], this function is automatically called, and its result is sent as props to the component <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

For dynamic routes, the `params` argument in `getStaticProps` provides access to URL parameters <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

### SEO and Head Component
For search engine optimization (SEO), [[introduction_to_nextjs | Next.js]] allows you to add an SEO-friendly title and meta tags to the head of the document by importing the `Head` component from `next/head` <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. Anything inside this component will be rendered to the document's head <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

### Handling Dynamic Routes with `getStaticPaths`
When working with [[dynamic_routing_in_nextjs | dynamic routes]], [[introduction_to_nextjs | Next.js]] needs to know which paths to [[static_generation_and_prerendering_in_nextjs | pre-render]] in advance <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. This is achieved by implementing the `getStaticPaths` function <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. This function fetches data, similar to `getStaticProps`, but its job is to return a `paths` object containing an array with every route for the dynamic URL <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. It also allows for additional options like `fallback` behavior <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

### Benefits of Static Generation
*   **Performance**: Generates static HTML files that can be delivered quickly over a CDN <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
*   **SEO**: Content is fully rendered HTML before JavaScript touches it, which is essential for SEO and social media sharing <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

### Trade-offs of Static Generation
*   **Stale Data**: If the data on the server changes, you need to rebuild and redeploy your site for those changes to be reflected <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Scale**: For websites with millions of pages, [[static_generation_and_prerendering_in_nextjs | pre-rendering]] all of them can be very slow and difficult <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

### Use Cases for Static Generation
This strategy is well-suited for data that doesn't change often and for sites with a relatively low number of total pages, such as a blog <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

## Server-Side Rendering (SSR)

With Server-Side Rendering (SSR), the content is generated on a server each time it's requested by the user <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>, <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

### Implementation with `getServerSideProps`
Similar to `getStaticProps`, data fetching for SSR is implemented using the `getServerSideProps` function <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>, <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. The key difference is that this function runs at *request time* instead of *build time* <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>, <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. This means the page will fetch the latest data on the server each time a new request comes in <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

### Benefits of Server-Side Rendering
*   **Fresh Data**: Ensures the end user always gets the latest and greatest data from the data source <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

### Trade-offs of Server-Side Rendering
*   **Efficiency**: It's less efficient than [[static_generation_and_prerendering_in_nextjs | static generation]] because a server is required to respond to every request, as opposed to caching everything on a global CDN <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

### Use Cases for Server-Side Rendering
SSR is ideal when data changes constantly, such as for an auction website where listings are frequently updated <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>, <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

## Incremental Static Regeneration (ISR)

[[introduction_to_nextjs | Next.js]] also offers Incremental Static Regeneration (ISR), which allows pages to be regenerated whenever a new request comes in, within a certain time interval <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This is implemented by adding a `revalidate` option to the `getStaticProps` function <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Conclusion

The flexibility of [[introduction_to_nextjs | Next.js]] allows developers to apply different data fetching paradigms wherever they are needed in the [[building_a_nextjs_application_with_redis | application]], without being limited to one strategy <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.