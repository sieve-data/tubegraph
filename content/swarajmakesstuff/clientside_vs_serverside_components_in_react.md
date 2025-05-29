---
title: Clientside vs Serverside Components in React
videoId: v1cg7b-Oaxs
---

From: [[swarajmakesstuff]] <br/> 

A significant [[misconception_about_react_server_components | misconception about React Server Components]] is that they always require a server <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This is not entirely true, as confirmed by Dan Abramov, who also notes the confusion surrounding this idea <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The choice between client-side and server-side components depends on the specific needs of the application.

## Client-Side Components

Client-side components are designed to run on the user's computer, such as a laptop <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. They compile or render directly on the client machine <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Use Cases for Client-Side Components
*   **Instantaneous Interactivity:** Client-side components are crucial for elements requiring immediate reactions without any delay <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Zero Delay Views:** They are necessary for interfaces where any delay between client and server communication would be detrimental <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **Examples:** Components like range sliders or other interactive clicks benefit from being client-side <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Server-Side Components

Server-side components, despite their name, don't necessarily execute on a live server during page requests. Their primary characteristic is their ability to access server-only resources.

### The Build-Time Revelation
A key insight into [[server_components_without_a_server | Server Components without a server]] is that their code does not need to run on the client's computer <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. This is because the client's machine typically doesn't possess the necessary files or data for server-side operations <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

Instead, the code for server components runs during the **build time** of the application <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. For example, if a blog post was deployed on January 5, 2024, the server component code related to that post ran at that deployment time, not when a user reloads the page days later <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

### Static File Generation
During the build process, server components generate static files, such as HTML <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. These static files are then stored in the build directory <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This means the output is essentially a static HTML file, not containing active React components like `PostList` or `PostPreview`, but rather basic HTML elements such as `<div>` and `<section>` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. This process occurs entirely during build time <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

### Example: Post Preview Component
Consider a "post preview" component that displays the word count of other posts <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   A client's laptop does not inherently have the data for other MDX files to count their words <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   There's no network API call made from the client to fetch these files to count words <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   The component works by directly calling the MDX or MD file, extracting its data, and then counting the length to determine the word count <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. This operation runs during the build, not on the client.

### Why "Server" Components?
The term "server component" likely originates from their ability to use [[apis_that_require_serverside_execution_in_react | APIs that require serverside execution]] <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. Many APIs, like `fs.readFile`, are designed to run only on the server side and would cause errors or not function if executed on the client side <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. Thus, these components are named "server components" because they leverage server-side only capabilities, even if the execution often occurs at build time rather than runtime on a dedicated server <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.