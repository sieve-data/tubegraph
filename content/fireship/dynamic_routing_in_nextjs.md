---
title: Dynamic routing in Nextjs
videoId: Sklc_fQBmcs
---

From: [[fireship]] <br/> 

Next.js provides a powerful routing system that allows for [[introduction_to_nextjs | dynamic routes]] based on the file structure within the `pages` directory <a class="yt-timestamp" data-t="01:01:06">[01:01:06]</a>. This means the file structure directly mirrors the URLs a user will navigate to in the application <a class="yt-timestamp" data-t="01:03:03">[01:03:03]</a>.

## How to Create Dynamic Routes

To implement a [[dynamic_routes_and_child_routing | dynamic route]] in Next.js, you create a file or directory with brackets `[]` around the parameter name <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>.

For example, to create a dynamic route for individual cars:
1.  Create a `cars` directory inside `pages` <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>.
2.  Inside the `cars` directory, add an `index.js` file for the main list of cars (e.g., `/cars`) <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>.
3.  For each individual car, add a component file named `[paramname].js` (e.g., `[id].js`) inside the `cars` directory <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>. The brackets `[]` make this route dynamic <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>.
    *   This means URLs like `/cars/whatever` or `/cars/tesla` will render the component defined in `[id].js` <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>.

## Accessing Dynamic Parameters

Within a [[dynamic_routes_and_child_routing | dynamic route]] component, you can access the query parameters from the URL using the `useRouter` hook from `next/router` <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>.

Example:
```javascript
import { useRouter } from 'next/router';

function Car() {
  const router = useRouter();
  const { id } = router.query; // 'id' corresponds to the [id].js file name
  // ... render content using 'id'
  return (
    <div>
      <h1>Car ID: {id}</h1>
    </div>
  );
}

export default Car;
```

In this example, if the file is named `[id].js`, the value of `id` will be accessible from `router.query.id` <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>.

## [[Static generation and prerendering in Nextjs | Pre-rendering Dynamic Routes]]

When using [[static_generation_and_prerendering_in_nextjs | static generation]] (pre-rendering) with [[dynamic_routes_and_child_routing | dynamic routes]], Next.js needs to know all possible paths in advance to pre-render them <a class="yt-timestamp" data-t="09:26:00">[09:26:00]</a>. This is achieved by implementing the `getStaticPaths` function in your [[dynamic_routes_and_child_routing | dynamic route]] component file <a class="yt-timestamp" data-t="09:38:00">[09:38:00]</a>.

The `getStaticPaths` function:
*   Can fetch data from an API or database <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>.
*   Must return a `paths` object containing an array of every route for that [[dynamic_routes_and_child_routing | dynamic URL]] <a class="yt-timestamp" data-t="09:49:00">[09:49:00]</a>.
*   Each path object in the array should contain a `params` key, where the keys match the [[dynamic_routes_and_child_routing | dynamic segment]] names (e.g., `{ params: { id: 'tesla' } }`) <a class="yt-timestamp" data-t="09:59:00">[09:59:00]</a>.
*   It also allows for additional options, such as `fallback` behavior <a class="yt-timestamp" data-t="10:03:00">[10:03:00]</a>.

Along with `getStaticPaths`, the `getStaticProps` function is used to fetch the data for each specific path at build time <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>. The `params` argument in `getStaticProps` provides the [[dynamic_routes_and_child_routing | dynamic route]] parameter (e.g., `id`) to fetch the correct data for that specific page <a class="yt-timestamp" data-t="08:23:00">[08:23:00]</a>.