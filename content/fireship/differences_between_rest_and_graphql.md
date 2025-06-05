---
title: Differences between REST and GraphQL
videoId: 7wzR4Ig5pTI
---

From: [[fireship]] <br/> 

Both [[introduction_to_restful_apis | REST APIs]] and [[introduction_to_graphql | GraphQL APIs]] are used for front-end applications to communicate with back-end applications <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. However, they approach data requests in fundamentally different ways.

## What is REST?
[[introduction_to_restful_apis | REST]] stands for Representational State Transfer <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. It has been the standard for API design for the past 20 years <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

### RESTful API Characteristics
*   **Multiple Endpoints/URLs** <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>: In REST, each piece of data or resource typically has its own unique URL <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. For example, to get components for a sandwich, you might make three separate requests for bread, ham, and cheese, each to a different URL <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
*   **Full Payload Response** <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>: Each response from the server contains the full JSON payload for that resource, even if the front-end application only needs a small portion of that data <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. Any unneeded data must be filtered out on the front-end <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   **Multiple Requests for Related Data** <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>: If additional related data is needed (e.g., a side salad and a drink for the sandwich), it would likely require making additional requests to different unique URLs <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

## What is GraphQL?
[[introduction_to_graphql | GraphQL]] is a query language for APIs <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> and also functions as a runtime for executing queries on the server <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### GraphQL API Characteristics
*   **Single Entry Point** <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>: Instead of multiple URL endpoints, [[introduction_to_graphql | GraphQL]] typically uses a single entry point into the API <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. The actual query sent from the front-end determines what the back-end will return, not a URL or specific mapping <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   **Precise Data Fetching** <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>: A [[introduction_to_graphql | GraphQL]] API will only return the exact fields that were requested in the query <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. For example, to get components for a sandwich, the entire sandwich object with only the requested fields (e.g., bread, ham, cheese) can be requested in a single query <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Reduced Requests for Related Data** <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>: If additional data is needed (e.g., a side salad and a drink for the sandwich), it's a simple matter of updating the existing query, often avoiding multiple requests <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Strongly Typed Schema** <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>: The server defines types for the available data and resolvers to fetch data from databases or other sources <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Because everything on the server is strongly typed, it enables amazing tooling and introspection <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. A front-end developer will always know the exact shape of the data to expect back from the server <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

## Core Differences Summarized

| Feature              | [[introduction_to_restful_apis | REST]]                                         | [[introduction_to_graphql | GraphQL]]                                  |
| :------------------- | :------------------------------------------------------------------- | :--------------------------------------------------------- |
| **Endpoints**        | Multiple unique URLs for different resources                         | Typically a single entry point for all data queries        |
| **Data Fetching**    | Returns full payload; prone to over-fetching                         | Returns only requested fields; precise fetching            |
| **Requests for Data**| May require multiple requests for related resources                  | Can fetch multiple related resources in a single request   |
| **Schema/Types**     | Less rigid schema, typically documented externally                   | Strongly typed schema with introspection capabilities      |
| **Complexity**       | Simpler for small APIs; quick setup                                | Added complexity up front; requires a type system          |
| **Tooling**          | Less built-in tooling for data structure                             | Excellent tooling due to strong typing (e.g., introspection, auto-generation of interfaces) <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a><a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>|

## Advantages and Disadvantages

### [[introduction_to_graphql | GraphQL]] Advantages
*   **Simplifies Data Requests**: It simplifies how front-end code requests data <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Eliminates Over-fetching/Under-fetching**: You only get the data you ask for, no more, no less <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Strong Typing and Tooling**: The strongly typed nature of [[introduction_to_graphql | GraphQL]] leads to amazing tooling, including introspection, which allows consumers to see what data is available <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. When combined with TypeScript, it provides end-to-end type safety, offering an excellent developer experience <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   **Efficient Data Updates**: Changing a query to include more data is simple, often avoiding additional network requests <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Ideal for Complex APIs**: The benefits of [[introduction_to_graphql | GraphQL]] become substantial when multiple developers are working with a large API that needs to integrate various back-end data sources <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### [[introduction_to_graphql | GraphQL]] Disadvantages
*   **Increased Upfront Complexity**: Setting up a [[introduction_to_graphql | GraphQL]] service has more overhead compared to a basic [[introduction_to_restful_apis | RESTful]] service <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. It requires additional dependencies and a type system <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Less Substantial for Simple APIs**: For small teams or relatively simple APIs, the benefits of [[introduction_to_graphql | GraphQL]] might not outweigh the added complexity <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

It is important to note that one is not definitively "better" than the other; the choice depends on the specific project requirements and team size <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
