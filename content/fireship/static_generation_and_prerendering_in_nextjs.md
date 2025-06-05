---
title: Static generation and prerendering in Nextjs
videoId: Sklc_fQBmcs
---

From: [[fireship]] <br/> 

[[Introduction to Nextjs | Next.js]] is a framework that allows you to build React applications while rendering content in advance on the server <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This means the first thing a user or search bot sees is the fully rendered HTML <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. After this initial page is received, [[clientside_rendering_vs_serverside_rendering | client-side rendering]] takes over, functioning like a traditional React app <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

One of the multiple [[data_fetching_strategies_in_nextjs | server rendering strategies]] offered by [[Introduction to Nextjs | Next.js]] is **Static Generation**, also known as **Pre-rendering** <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## What is Static Generation?
Static Generation allows you to render your pages at **build time** <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a> <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. This process involves generating all the HTML files when the application is built <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. These generated HTML files can then be uploaded to a storage bucket or static host <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a> and delivered with high performance over a CDN (Content Delivery Network) <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

## Benefits
The primary benefits of static generation include:
*   **Faster First Contentful Paint:** The end user gets rendered content quicker <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
*   **SEO Optimization:** The content can be reliably crawled by search bots and social media link bots <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a> <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. The fully rendered HTML, including title and pre-rendered content, is visible before JavaScript interactivity is added <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   **Performance:** Pages can be easily cached by a CDN, leading to very high performance <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a> <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

## Trade-offs and Use Cases
While highly beneficial, static generation has trade-offs:
*   **Stale Data:** If the data on the server changes, you need to rebuild and redeploy your site for those changes to be reflected <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
*   **Scalability:** For websites with a very large number of pages (e.g., millions), pre-rendering all of them can be slow and difficult <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

Static generation is most well-suited for:
*   Data that doesn't change often <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   Sites with a relatively low number of total pages <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   A good example is a blog, which might have a few hundred pages that don't change daily <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

## Implementing Static Generation

### `getStaticProps`
Each page or component in a [[Introduction to Nextjs | Next.js]] project can implement a function called `getStaticProps` <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a> <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   This function runs automatically when you build your site <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   It can fetch data from a cloud database or API <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a> <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   The data fetched by `getStaticProps` is then passed as `props` to the component itself <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a> <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   The component then uses these props to render the HTML <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

```javascript
// Example of getStaticProps
export async function getStaticProps(context) {
  // Access dynamic parameters from the URL
  const { id } = context.params; 

  // Fetch data for a specific car based on ID
  const res = await fetch(`http://localhost:3000/cars/${id}.json`);
  const car = await res.json();

  // Return the fetched data as props
  return {
    props: { car },
  };
}
```
*   The `context` object in `getStaticProps` provides access to parameters (`params`) from the URL, which is useful for [[dynamic_routing_in_nextjs | dynamic routes]] <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   The function must return an object with a `props` property <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

### `getStaticPaths` (for [[dynamic_routing_in_nextjs | Dynamic Routes]])
When working with [[dynamic_routing_in_nextjs | dynamic routes]], [[Introduction to Nextjs | Next.js]] needs to know which specific paths to pre-render <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. This is because [[Introduction to Nextjs | Next.js]] cannot automatically determine all possible dynamic IDs in advance <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   The `getStaticPaths` function is implemented to provide this information <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.
*   It can fetch data from an API or database <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
*   Its job is to return a `paths` object that contains an array with every route for the dynamic URL <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   This array maps the dynamic values (e.g., car IDs) to objects with `params` property <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

```javascript
// Example of getStaticPaths
export async function getStaticPaths() {
  // Fetch all possible IDs
  const res = await fetch('http://localhost:3000/ids.json');
  const ids = await res.json();

  // Map IDs to paths
  const paths = ids.map(id => ({
    params: { id: id.toString() }, // Ensure ID is a string
  }));

  // Return paths along with fallback behavior
  return {
    paths,
    fallback: false, // Or true, or 'blocking' for different fallback behaviors
  };
}
```
*   The `fallback` option determines how paths not returned by `getStaticPaths` are handled. `false` means 404 for unknown paths, `true` or `'blocking'` enables fallback behavior for new paths <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

## Incremental Static Regeneration (ISR)
[[Introduction to Nextjs | Next.js]] also offers **Incremental Static Regeneration** as an option that falls between static generation and [[clientside_rendering_vs_serverside_rendering | server-side rendering]] <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. By simply adding a `revalidate` option to `getStaticProps`, [[Introduction to Nextjs | Next.js]] can regenerate a page whenever a new request comes in within a specified time interval <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This allows for updated content without needing a full rebuild and redeploy for every change.