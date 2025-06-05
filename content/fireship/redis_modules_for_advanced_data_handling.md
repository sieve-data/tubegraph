---
title: Redis modules for advanced data handling
videoId: DOIWQddRD5M
---

From: [[fireship]] <br/> 

Redis, commonly known as a fast in-memory database used for caching, can also function as a primary application database thanks to its suite of modules <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. These modules extend core Redis by adding [[framework_features_like_routing_and_database_integration | additional data structures]] and commands, enabling it to handle JSON data, full-text search, graph relationships, and more <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Key Redis Modules

### Redis JSON
Traditionally, Redis stores data as hash data structures, which do not natively support nested objects <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. The Redis JSON module allows data to be stored as native JSON, making Redis operate more like a document-oriented database <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a> <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. This is enabled by setting `dataStructure: 'json'` in the schema when defining an entity <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### Redis Search
Redis Search is a powerful module capable of indexing all fields on a JSON dataset <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. It supports complex queries similar to SQL's `WHERE` clause <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a> and aggregations like `SUM` and `COUNT` <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. Key features include:
*   **Full-Text Search**: Allows for fuzzy matching, recognizing typos and common words while still returning intended results <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. This is enabled by adding `textSearch: true` to specific fields in your schema <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Query Capabilities**: Includes `where`, `eq` (exact equality), `or` for chained conditions, and `matches` for full-text search contexts <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   **Advanced Search Options**: Supports pagination, retrieving first/last items, getting a count of total items, and performing logical comparisons like greater than or less than <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## Building a Full-Text Autocomplete Search with Redis
To demonstrate the capabilities of Redis modules, a full-text autocomplete search feature was built, similar to Algolia or Elasticsearch <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. This project uses [[building_a_nextjs_application_with_redis | Next.js]] for the frontend (React) and backend (Node.js) to interact with Redis <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Users can add items to the database and instantly view filtered results <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. The search updates automatically with every keystroke <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Redis OM (Object Mapping)
Redis has released a new SDK called Redis OM (Object Mapping), which supports object mapping in [[understanding_nodejs_modules_and_packages | Node.js]] <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Redis OM maps data into a [[javascript_objects_and_their_properties | JavaScript class]] or "entity," simplifying the creation of a consistent schema <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. It streamlines common CRUD (Create, Read, Update, Delete) operations <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

### Connecting to Redis with Redis OM
To connect to a Redis database using Redis OM:
1.  **Environment Variables**: Set a `REDIS_URL` environment variable, formatted with the username, password, URL, and port of the database <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
2.  **Client Connection**: Use `client.open(process.env.REDIS_URL)` from the `redis-om` library to establish a connection <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
3.  **Connection Management**: Implement an async function to open the connection only if it's not already open, especially when working with [[building_a_nextjs_application_with_redis | Next.js]] <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

### Defining Entities
An entity in Redis OM is akin to a database table <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. You define a class that extends `Entity` from `redis-om` and specify its schema with properties and their data types <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. By default, this represents a Redis hash, but the `dataStructure: 'json'` option makes it behave like a document-oriented database <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

### Data Creation with Redis OM
To create new data using Redis OM:
1.  **Connect**: Ensure a connection to the database client is open <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
2.  **Repository**: Create a repository by combining the schema and the client <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
3.  **Create Entity**: Use the `createEntity` method with a [[javascript_objects_and_their_properties | JavaScript object]] representing the data <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
4.  **Save**: Call `repository.save()` with the entity data to commit it to the database <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. Redis will return an automatically generated unique ID <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### Indexing for Search
To enable searching with Redis Search, an index must be created once <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. This is done by referencing the repository and calling its `createIndex()` method <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

### Searching Data with Redis OM
To search for data using Redis OM and Redis Search:
1.  **Search Function**: Define a function that takes a query as input <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
2.  **Repository Search**: Call the `repository.search()` method, which offers various capabilities like `where`, `eq`, `or`, and `matches` <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
3.  **Return Results**: Use `.returnAll()` to get all results matching the query <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

## Integration with Next.js
The example project integrates Redis with Next.js using [[framework_features_like_routing_and_database_integration | API routes]] for backend operations and React components for the frontend <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

### API Routes
[[framework_features_like_routing_and_database_integration | Next.js API routes]] are used to handle backend logic. Each [[framework_features_like_routing_and_database_integration | API route]] exports a default `handler` function that takes `request` and `response` objects <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
*   **Creation**: An [[framework_features_like_routing_and_database_integration | API route]] (e.g., `cars.js`) handles POST requests, using `request.body` (JSON data from the form) to call the `createCar` function <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **Indexing**: A dedicated [[framework_features_like_routing_and_database_integration | API route]] (e.g., `create-index.js`) can be used to trigger the `createIndex` function once <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   **Search**: Another [[framework_features_like_routing_and_database_integration | API route]] (e.g., `search.js`) grabs the search query from the URL parameters, calls `searchCars`, and returns an array of results <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

### Frontend Interaction
React components handle user input and interaction with the API routes:
*   **Form Submission**: A standard HTML form uses `handleSubmit` to intercept the submit event <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   **Form Data Handling**: Instead of manually accessing each property, form data can be converted to a `FormData` class, then to a plain [[javascript_objects_and_their_properties | JavaScript object]] using `Object.fromEntries()` <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. The input `name` attribute should match the Redis schema <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **API Calls**: The `fetch` API is used to make requests to the backend [[framework_features_like_routing_and_database_integration | API endpoints]] <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. For POST requests, the `body` is `JSON.stringify`ed form data, and `Content-Type` is set to `application/json` <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Search Input**: A search input triggers a search function whenever it changes, making calls to the search endpoint <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. It often utilizes React's `useState` hook to manage search results <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. To prevent excessive API calls, it's recommended to only execute the search for queries longer than two characters <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a> and to debounce the input <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
*   **Display Results**: Search results are displayed by mapping through the array of retrieved data <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.

> [!NOTE] Setting up Redis Cloud
> To get started with Redis, one easy option is to sign up for Redis Cloud <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. When creating a database, ensure to add the "Redis Search" and "Redis JSON" add-on modules <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. The Redis Insight tool (GUI) can be downloaded to analyze and manage data in the database <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.