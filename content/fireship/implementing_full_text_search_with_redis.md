---
title: Implementing full text search with Redis
videoId: DOIWQddRD5M
---

From: [[fireship]] <br/> 

[[using_redis_as_a_primary_database | Redis]], commonly known as a fast in-memory database used for caching, can also function as a primary application database thanks to its suite of modules <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. These [[redis_modules_for_advanced_data_handling | Redis modules]] extend core Redis with additional data structures and commands, enabling features like JSON data handling, graph relationships, and full text search <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

This guide explores the implementation of a full text autocomplete search feature, similar to Algolia or Elasticsearch, where users can add items and instantly view filtered results <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. The project is built from scratch using [[building_a_nextjs_application_with_redis | Next.js]] for the frontend (React) and Node.js for backend interaction with Redis <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Core Components for Search

To implement full text search, two key [[redis_modules_for_advanced_data_handling | Redis modules]] are essential:

*   **Redis JSON**: Allows data to be stored as native JSON documents, supporting nested objects, unlike the standard hash data structure <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. When defining an entity with [[object_mapping_with_redis_ohm_and_nodejs | Redis Ohm]], specifying `dataStructure: 'JSON'` enables Redis to operate more like a document-oriented database <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   **Redis Search**: An incredibly powerful module that indexes all fields on your JSON dataset <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This allows for complex queries, similar to SQL's `WHERE` clauses, and aggregations like `SUM` and `COUNT` <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. It enables querying and filtering of data for frontend display <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

## Setting Up Redis for Full Text Search

The easiest way to get started with Redis is by signing up for Redis Cloud <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. When creating a database instance, ensure that the Redis Search and Redis JSON add-on modules are enabled <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

To manage and analyze data, the Redis Insight tool (a GUI) can be downloaded and connected to the Redis Cloud database using the public endpoint URL, default username, and password <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## Data Modeling and Index Creation with Redis Ohm

The project utilizes [[object_mapping_with_redis_ohm_and_nodejs | Redis Ohm]], a new SDK for Node.js that supports object mapping <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. [[object_mapping_with_redis_ohm_and_nodejs | Redis Ohm]] maps data into a JavaScript class or entity, helping to build a consistent schema and simplifying CRUD operations <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

### Defining an Entity and Schema

An entity in [[object_mapping_with_redis_ohm_and_nodejs | Redis Ohm]] is analogous to a database table <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. For example, a `Car` class extending `Entity` can be defined with a schema containing various properties and their specific data types <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. To leverage Redis JSON, the `dataStructure: 'JSON'` option is added to the schema <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

For full text search, specific fields in the schema need to be configured with the `textSearch: true` option. This enables fuzzy matching, allowing the search engine to recognize typos and common words while still returning relevant results <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. For instance, `description` can be set with `textSearch: true` <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

### Creating the Search Index

After defining the schema, a search index must be created. This is a one-time operation <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. The index is created by referencing the repository and calling its `createIndex` method <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. A Next.js API route (e.g., `api/create-index.js`) can be used to trigger this function, accessible via a URL like `api/create-index` <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

## Implementing Search Logic

The backend search logic is encapsulated in a function (e.g., `searchCars`) that takes a query as input <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. This function uses the `repository.search` method, which offers capabilities like pagination, counting total items, and logical comparisons (e.g., greater than, less than) <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

Key methods used in the search query:

*   `where(property)`: References a property in the JSON data <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   `eq(value)`: Checks for exact equality <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   `or(property)`: Chains additional properties to search across <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.
*   `matches(value)`: Used for properties enabled with `textSearch: true`, performing full text search with fuzzy matching <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   `returnAll()`: Retrieves all results from the query <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

### API Route for Search

A Next.js API route (e.g., `api/search.js`) handles incoming search queries <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. This route extracts the search query from the URL, calls the `searchCars` method, and returns an array of car data as a JSON response to the client <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

## Front-end Search Component

On the frontend, a React component (e.g., `SearchForm.js`) contains an input field that triggers a search function on every change (keystroke) <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. This component maintains state for the search results (hits) using the `useState` hook <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

The search function:

1.  Grabs the current value from the form input <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
2.  Formats it as a URL parameter <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.
3.  Executes the search only if the query length is greater than 2 to prevent excessive API calls <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. Debouncing the input is also recommended to limit calls per keystroke <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
4.  Uses the Fetch API to make a request to the search API endpoint with the query parameters <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
5.  Receives an array of cars in the response and updates the component's state, enabling [[realtime_database_implementation | real-time]] display of results <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
6.  Displays the car data in an unordered list, mapping each hit to a list item using the entity ID as the key and showing relevant data like make, model, and image <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.

By combining [[redis_modules_for_advanced_data_handling | Redis modules]] like Redis JSON and Redis Search with [[object_mapping_with_redis_ohm_and_nodejs | Redis Ohm]] and a [[building_a_nextjs_application_with_redis | Next.js]] application, a robust full stack full text search feature can be implemented <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.