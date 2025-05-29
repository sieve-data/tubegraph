---
title: Misconception about React Server Components
videoId: v1cg7b-Oaxs
---

From: [[swarajmakesstuff]] <br/> 

A common misconception regarding [[server_components_without_a_server | React Server Components]] is that they always require a server to run <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. However, this is not entirely accurate <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Even Dan Abramov has expressed confusion about why people hold this belief <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Client-Side Components vs. Server Components

To understand [[server_components_without_a_server | React Server Components]], it's helpful to first understand [[clientside_vs_serverside_components_in_react | Client Components]]:

### [[clientside_vs_serverside_components_in_react | Client-Side Components]]
[[clientside_vs_serverside_in_react | Client Components]] are designed for instant interactivity <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Execution**: Code for [[clientside_vs_serverside_components_in_react | client components]] runs on the user's own computer, such as a laptop <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This allows for instantaneous updates and reactions <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Use Cases**: They are crucial for elements requiring zero delay, such as range sliders or interactive clicks, where waiting for a server response would hinder the user experience <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

### [[server_components_without_a_server | Server Components]]
In contrast to [[clientside_vs_serverside_components_in_react | client components]], [[server_components_without_a_server | server components]] handle tasks that don't require immediate user interaction <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

#### How They Work: The "Post Preview" Example
Consider a "Post Preview" component that displays the word count of another article <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   **Data Access**: The user's laptop typically doesn't store the data of other articles or MDX files <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. There's no API call made from the client to fetch this data <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Logic**: The component's logic simply involves calling the MDX file, extracting its data, and counting its length <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

#### When [[server_components_without_a_server | Server Components]] Execute
The key insight is when this code actually runs:
*   **Build Time Execution**: The code for [[server_components_without_a_server | server components]] often runs during the **build time** of the application <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. For example, a blog post component calculating word count would run when the blog post is deployed to web hosting, not when a user reloads the page <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Static File Generation**: During the build process, [[server_components_without_a_server | server components]] generate static files <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. These static files are then stored in the build output <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. The final output is essentially a basic HTML file with `divs` and `sections`, no longer containing the original component logic or file directories <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

> "None of this code need to be run on your computer and indeed it couldn't because your computer don't have my files obviously" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>

## Why are they called "Server Components"?

The term "server components" likely comes from their ability to interact with [[apis_that_require_serverside_execution_in_react | APIs that require serverside execution in React]] <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. Many APIs will throw errors or simply not function if called from the client side <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. Therefore, [[server_components_without_a_server | server components]] are necessary for these server-side-only API calls <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.