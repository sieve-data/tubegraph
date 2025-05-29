---
title: APIs that require serverside execution in React
videoId: v1cg7b-Oaxs
---

From: [[swarajmakesstuff]] <br/> 

A common [[misconception_about_react_server_components | misconception about React Server Components]] is that they constantly require a running server [00:00:06]. Dan Abramov himself has expressed confusion over why people believe this to be true [00:00:11]. The core idea behind Server Components is to allow developers to utilize APIs that can only run on the server side, typically during the build process, rather than requiring a persistent server connection at runtime for every client request [00:04:02].

## Client-Side vs. Server-Side Operations

[[clientside_vs_serverside_components_in_react | Client components]] run on the user's local machine, such as a laptop [00:00:56]. They are essential for providing instantaneous interactivity, such as range sliders or clicks, where zero delay is critical [00:01:29]. Operations that run client-side compile or render directly on the user's device [00:01:02].

However, there are many operations that cannot be performed on the client side. For example, a component needing to read the content of another file (like an MDX file) to count its words [00:01:50]. A user's laptop typically doesn't have access to the project's entire file system data [00:02:12]. Attempting to call such APIs directly on the client side would result in errors and prevent functionality [00:05:14].

## The Role of Server-Side APIs

Certain APIs are designed to run exclusively on the server side. These are often related to file system access, database queries, or other operations that require privileged access or large datasets not available to the client. An example mentioned is calling an MDX or MD file to read its data and count the length [00:02:37]. This type of operation cannot execute on the client because the client's computer does not possess the necessary files [00:03:22].

## How Server Components Utilize Server-Side APIs

Server Components are designed to enable the use of these server-side-only APIs, such as `fs.readFile` [00:05:04]. When a Server Component is processed, it executes the code that interacts with these APIs. However, this execution doesn't typically happen on a live server every time a user requests a page. Instead, it occurs during the build process [00:03:15].

For example, when a blog post is deployed, the [[static_file_generation_during_build_time_in_react | static components generated from Server Components]] are compiled and stored within the build file [00:03:36], [00:04:02]. These compiled files become static HTML or basic DIVs and sections, similar to an image or any other static asset [00:04:12], [00:04:23]. The resulting output is essentially pre-rendered HTML that doesn't need to dynamically fetch data from the server or re-run server-side APIs every time a page is reloaded [00:03:45].

This approach allows developers to leverage powerful server-side capabilities for data fetching and processing while still delivering fast, static content to the user, without the need for constant server communication for every page view [00:01:13].