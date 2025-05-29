---
title: Static file generation during build time in React
videoId: v1cg7b-Oaxs
---

From: [[swarajmakesstuff]] <br/> 

A significant [[misconception_about_react_server_components | misconception about React Server Components]] is the belief that they always require a server to run at runtime [00:00:06]. However, this isn't necessarily true; Dan Abramov himself has expressed confusion over this common misunderstanding [00:00:11]. The actual reason for the "server" in "server components" relates to *when* certain code runs and the types of operations it enables, particularly during the build process.

## Clientside vs. Serverside Components

### Client Components
[[clientside_vs_serverside_components_in_react | Client components]] are designed for instantaneous interactivity and are executed directly on the user's computer (e.g., laptop) [00:00:50]. This means the code compiles or renders on the client's machine [00:01:02]. They are crucial for features requiring immediate reactions, such as a range slider or any click that demands zero delay, where waiting for server-client communication would be impractical [00:01:19].

### Server Components
In contrast, server components are suited for operations that cannot run on the client side, primarily due to data access limitations or the need for [[apis_that_require_serverside_execution_in_react | APIs that require serverside execution in React]] [00:05:01].

Consider an example like a "post preview" component that displays the word count of another article [00:01:47].
*   Your client laptop does not inherently possess the data of other pages or MDX files [00:02:09].
*   There are no network API calls to retrieve these files from a remote source like GitHub just to count words [00:02:23].
*   Instead, the component's logic involves calling or reading the MDX file directly, extracting the data, and counting its length [00:02:37].

## The Role of Build Time in Server Components

The critical distinction for server components lies in *when* this code executes:
*   It does not run on the client whenever a user reloads the page [00:03:02].
*   Instead, the code for such components runs *during the build time* of the application [00:03:12]. For instance, a component displaying a deployment date might have run on January 5, 2024, when the blog post was initially deployed to its web hosting, and this date remains static regardless of client-side reloads [00:03:32].

### Static File Generation
When you implement server components, the APIs and data retrieval they perform are executed when your code is compiled [00:04:12].
*   The results of these server component operations are transformed into static files [00:04:02].
*   These static files are then stored within your build directory [00:04:07].
*   Effectively, your code becomes a static file, akin to an image or a basic HTML file [00:04:17]. A "post preview" component, for example, is no longer a dynamic component at runtime but rather a pre-rendered static HTML structure containing the word count [00:04:27]. This entire process occurs during the application's build phase [00:04:37].

### Why "Server" Components?
The term "server components" likely stems from their ability to utilize [[apis_that_require_serverside_execution_in_react | APIs that require serverside execution in React]] [00:05:04]. Many APIs, such as `readFile` for accessing the file system, can only function on the server side and would cause errors if attempted on the client side [00:05:07]. By allowing these server-only operations to occur during the build process, React Server Components enable developers to integrate such functionalities without requiring a persistent live server connection for every client request [00:05:19].