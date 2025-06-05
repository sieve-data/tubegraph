---
title: Developing web apps with Nextjs
videoId: FQPlEnKav48
---

From: [[fireship]] <br/> 

[[building_and_deploying_a_full_stack_application_with_nodejs_and_express | Next.js]] is a framework that enables the development of full-stack web applications entirely using [[javascript_serverside_with_nodejs | JavaScript]] <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. It is a popular choice among many other [[web application tools for developers | JavaScript-based web application tools for developers]] like njs, Angular Universal, SvelteKit, NestJS, and Adonis <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

## Getting Started

To initiate a new [[building_and_deploying_a_full_stack_application_with_nodejs and_express | Next.js]] project, developers can run the command `npx create next app` <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

## Database Integration

Unlike some other frameworks, [[building_and_deploying_a_full_stack_application_with_nodejs and_express | Next.js]] does not come with built-in database integration <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. This approach is often seen as beneficial in the [[introduction_to_nodejs | JavaScript]] ecosystem, as it allows developers to start with a minimal framework and add their preferred database solution, such as Prisma <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

## Core Features

### Routing

Routing in [[building_and_deploying_a_full_stack_application_with_nodejs and_express | Next.js]] is managed through the file system <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. Each file created within the `Pages` directory corresponds to a distinct URL in the browser <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. For dynamic routes, file names are enclosed in brackets, e.g., `[id].js` <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### User Interface (UI)

Each page file in [[building_and_deploying_a_full_stack_application_with_nodejs and_express | Next.js]] exports a [[reactjs_functional_and_classbased_components | React]] component that defines the UI or view <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. The fundamental integration of [[reactjs_overview_and_history | React]] into the framework significantly enhances developer productivity <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

### Data Fetching

A unique aspect of [[building_and_deploying_a_full_stack_application_with_nodejs and_express | Next.js]] is its ability to execute server-side code within a [[reactjs_overview_and_history | React]] application <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. Functions like `getServerSideProps` run on the server using [[introduction_to_nodejs | Node.js]] <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. Data fetched server-side, for example, using Prisma to retrieve items from a database, can then be passed as props to the [[reactjs_functional_and_classbased_components | React]] component for rendering in the UI <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. This tight coupling of server-side and client-side code, while seemingly a deviation from strict separation of concerns, generally works very effectively <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

## Developer Experience

Overall, [[building_and_deploying_a_full_stack_application_with_nodejs and_express | Next.js]] provides a minimal feel compared to other frameworks mentioned, yet it simplifies many complex and tedious aspects of [[introduction_to_web_development | web development]] behind the scenes <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.