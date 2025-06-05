---
title: Nhost and Hasura for GraphQL backend
videoId: SXmYUalHyYk
---

From: [[fireship]] <br/> 
Nhost and Hasura for GraphQL Backend
---

Nhost is an open-source alternative to Firebase that incorporates [[introduction_to_graphql | GraphQL]] capabilities <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

### Powered by Hasura
Nhost is built on top of [[https://www.youtube.com/watch?v=0k1L2Gg02n8 | Hasura]] <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. Hasura is a platform that can transform a relational database into a [[introduction_to_graphql | GraphQL]] API <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

### Pricing <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>
Nhost offers a free tier for experimentation. For more serious projects, pricing begins at $25 per month <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### Popularity <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>
While Nhost's npm downloads may not be extensive, its underlying platform, Hasura, is extremely popular, which means the download metric doesn't fully represent its reach <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### User Interface <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>
The Nhost UI is intuitive, allowing users to visualize all their database records directly in the browser <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### GraphQL Integration <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>
A key feature of Nhost is that its Postgres database also functions as a [[introduction_to_graphql | GraphQL]] API <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. This enables users to directly interact with [[introduction_to_graphql | GraphQL]] queries and mutations within the browser <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. However, for certain tasks like updating database permissions and security rules, direct access to the Hasura dashboard is required, as not everything can be managed from the Nhost dashboard <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. The documentation for these processes is comprehensive <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

### Development Experience <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>
Nhost provides first-class support for React, including hooks for performing authentication with a single line of code <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

For database queries, the process is more involved compared to Firebase due to the use of [[introduction_to_graphql | GraphQL]] and Apollo Client <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. While these are powerful technologies, they introduce a learning curve and tend to result in more verbose code <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

#### Workflow for Data Fetching <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>
1.  **Schema Definition:** Add the table and columns to the [[graphql_query_language_and_schema | GraphQL schema]] in Hasura <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
2.  **Permissions:** Define permissions to allow data access <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
3.  **Query Testing:** Test the [[introduction_to_graphql | GraphQL]] query in the [[introduction_to_graphql | GraphQL]] Explorer before integrating it into the codebase <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
4.  **Code Integration:** Run the query using the `useQuery` hook provided by Apollo Client <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

While this workflow offers a more robust coding experience, it can introduce more friction for rapid prototyping compared to simpler solutions like Firebase <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

### Comparison and Potential <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>
Nhost is considered a strong competitor to Superbase <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. For developers who prefer [[introduction_to_graphql | GraphQL]], Nhost's approach is likely to be favored <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.