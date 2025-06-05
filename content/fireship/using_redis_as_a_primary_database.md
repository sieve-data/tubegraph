---
title: Using Redis as a primary database
videoId: DOIWQddRD5M
---

From: [[fireship]] <br/> 

While [[implementing_full_text_search_with_redis | Redis]] is widely recognized as a rapid in-memory database often employed for caching to enhance the speed of conventional databases <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, it can also function as a primary application database <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This capability is enabled by a suite of [[redis_modules_for_advanced_data_handling | Redis modules]] that extend core [[implementing_full_text_search_with_redis | Redis]] with additional data structures and commands <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>, allowing it to handle JSON data, full-text search, and graph relationships <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

This article details how to build a full-text autocomplete search feature, similar to Algolia or Elasticsearch, where users can add items to the database and instantly view filtered results <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. The project is built from scratch using [[building_a_nextjs_application_with_redis | Next.js]] for the front-end (React) and Node.js for back-end interaction with [[implementing_full_text_search_with_redis | Redis]] <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. A new SDK called [[object_mapping_with_redis_ohm_and_nodejs | Redis Ohm]], which supports object mapping in Node.js, is also utilized <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Project Overview

The demonstration involves a form that, upon submission, adds a new item to the [[implementing_full_text_search_with_redis | Redis]] database <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
Normally, data in [[implementing_full_text_search_with_redis | Redis]] might be saved as a hash data structure, but hashes do not support nested objects <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. Instead, data is stored as native JSON thanks to the [[redis_modules_for_advanced_data_handling | Redis JSON]] module <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

After adding items, a search form allows users to type, automatically updating the results in the UI with every keystroke <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This functionality is powered by [[implementing_full_text_search_with_redis | Redis Search]], a powerful module that can index all fields on a JSON dataset <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This enables complex queries, similar to SQL's `WHERE` clauses, and aggregations like `SUM` and `COUNT` <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Getting Started with Redis

There are several ways to begin using [[implementing_full_text_search_with_redis | Redis]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### Redis Cloud

The easiest method is to sign up for [[implementing_full_text_search_with_redis | Redis]] Cloud <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
After signing in, users create a new subscription, choosing a free fixed plan to experiment <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. When creating a database, it's crucial to add the [[redis_modules_for_advanced_data_handling | Redis Search]] and [[redis_modules_for_advanced_data_handling | Redis JSON]] add-on modules <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This provides a scalable cloud database <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. To connect, a public endpoint URL and a password for the default user are provided <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

### Redis Insight

Optionally, the [[implementing_full_text_search_with_redis | Redis]] Insight tool offers a GUI to analyze and manage data <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. After installation, a new database can be added by pasting the public URL, along with "default" as the username and the generated password <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### Redis Basics

[[implementing_full_text_search_with_redis | Redis]] is easy to learn because data is organized into key-value pairs <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

*   **Keys**: Each key is unique and identifies a value <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Data Types**: Keys can have data types such as:
    *   `string` <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>
    *   `hash` (for objects of multiple key-value pairs) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>
    *   `lists` <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>
    *   `JSON` data <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>
*   **TTL (Time To Live)**: Data can be set to automatically delete after a specified time <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **In-Memory vs. Persistence**: [[implementing_full_text_search_with_redis | Redis]] keeps data in memory for extreme speed, avoiding disk round trips <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. However, on [[implementing_full_text_search_with_redis | Redis]] Cloud, this data is also persisted, preventing data loss <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   **Commands**: [[implementing_full_text_search_with_redis | Redis]] has built-in commands like `SET` to add data (e.g., `SET hello world`) <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a> and `GET` to read data (e.g., `GET hello`) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

## Building a Next.js Application with Redis

### Project Initialization

To start, initialize a [[building_a_nextjs_application_with_redis | Next.js]] project using `npx create-next-app` <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. The primary dependency is [[object_mapping_with_redis_ohm_and_nodejs | redis-om]], installed via `npm install` <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. [[object_mapping_with_redis_ohm_and_nodejs | Redis Ohm]] maps data into a JavaScript class or entity, facilitating schema building and simplifying CRUD operations <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

### Connecting to Redis Cloud

Connection details for the cloud database are stored in a `.env.local` file, automatically picked up by [[building_a_nextjs_application_with_redis | Next.js]] <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. This file contains the `REDIS_URL` in the format `username:password@url:port` <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

A `lib/redis.js` file is created to manage the connection. The `client` from [[object_mapping_with_redis_ohm_and_nodejs | redis-om]] is the main entry point for database interaction <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. `client.open(process.env.REDIS_URL)` connects to the database <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. An `async` `connect` function ensures the connection is only opened if it's not already <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

### Defining Data Schema with Redis Ohm

Data entities are defined using classes that extend `Entity` from [[object_mapping_with_redis_ohm_and_nodejs | redis-om]] <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. These classes are given a `schema` with various properties and their data types <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. By default, this represents a hash in [[implementing_full_text_search_with_redis | Redis]] <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. To use the [[redis_modules_for_advanced_data_handling | Redis JSON]] module for a document-oriented approach, the `dataStructure: 'json'` option is added to the schema definition <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

```javascript
// Example schema for a 'Car' entity
class Car extends Entity {}
const carSchema = new Schema(Car, {
  make: { type: 'string' },
  model: { type: 'string' },
  description: { type: 'text', textSearch: true }, // Added later for search
  image: { type: 'string' },
}, {
  dataStructure: 'json', // Use Redis JSON module
});
```

### Creating Data

An `async` function, `createCar`, connects to the database client <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. A `repository` is created by combining the schema and the client <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. New data is created using `repository.createEntity()` with a JavaScript object <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>, and `repository.save()` commits it to the database <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. [[implementing_full_text_search_with_redis | Redis]] returns an auto-generated unique ID, with the key format `car:unique_id` and the value being the JSON data based on the defined schema <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### API Route for Data Creation

A [[building_a_nextjs_application_with_redis | Next.js]] API route, e.g., `pages/api/cars.js`, handles write operations on the backend <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. This route imports the `createCar` function <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. The default `handler` function in a [[building_a_nextjs_application_with_redis | Next.js]] API route receives `req` (incoming data) and `res` (outgoing data) <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. It uses `req.body` (JSON data from the form) to create a new car, then sends a response back with the new unique ID <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

### Front-end Form for Data Creation

A React component, e.g., `components/CarForm.js`, manages user input and makes requests to the API route <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
A standard HTML form with text inputs and a submit button intercepts the `submit` event with a `handleSubmit` function <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
Inside `handleSubmit`, `event.preventDefault()` prevents page refresh <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. Form data is converted to JSON by transforming `event.target` (the HTML form) into a `FormData` class, then into a plain JavaScript object using `Object.fromEntries` <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. The `name` attribute of form inputs must match the [[implementing_full_text_search_with_redis | Redis]] schema <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

The `fetch` API is used to make a `POST` request to the API endpoint (`/api/cars`), with the `JSON.stringify`-ed form data as the `body` and `Content-Type: application/json` <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. The response (the created ID) is then logged <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
The `CarForm` component is then declared in `pages/index.js` <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. Running `npm run dev` starts the [[building_a_nextjs_application_with_redis | Next.js]] app <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. Submitting the form logs the created ID, and the data can be viewed in [[implementing_full_text_search_with_redis | Redis]] Insight <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

## Implementing Full-Text Search with Redis Search

### Creating an Index

To use [[implementing_full_text_search_with_redis | Redis Search]], an index must be created <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. In `lib/redis.js`, a `createIndex` function is added, which simply calls `repository.createIndex()` <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. For fields where full-text search is desired, `textSearch: true` is added to their schema definition, enabling fuzzy matching, typo recognition, and common word handling <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. For example, the `description` field can have `textSearch: true` <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

Since index creation is a one-time operation, a convenience API route, e.g., `pages/api/create-index.js`, is created <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. It imports `createIndex` and sends a response <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. The index is added by accessing its URL (e.g., `/api/create-index`) in the browser <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

### Searching Data

In `lib/redis.js`, a `searchCars` function is created to search the database based on a query <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. This function utilizes `repository.search()`, which offers capabilities like pagination, retrieving first/last items, item counts, and logical comparisons (e.g., greater than, less than) <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

*   The `where()` method references a property in the JSON data <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   `eq()` checks for exact equality <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   Multiple conditions can be chained with `or()` <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
*   For text fields with `textSearch: true`, `match()` performs full-text search, returning results even with typos <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
*   Finally, `returnAll()` retrieves all results from the query <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

```javascript
// Example search logic
async function searchCars(query) {
  await connect();
  const repository = new Repository(carSchema, client);
  return repository.search()
    .where('make').eq(query)
    .or('model').eq(query)
    .or('description').match(query)
    .returnAll();
}
```

### API Route for Search

Another [[building_a_nextjs_application_with_redis | Next.js]] API route, `pages/api/search.js`, handles search requests <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. It extracts the search query from the URL parameters, calls `searchCars`, and returns the results (an array of cars) to the client <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

### Front-end Search Form

A React component, `components/SearchForm.js`, makes calls to the search endpoint <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. It has an input that triggers a `search` function on `onChange` (every keystroke) <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. The component uses `useState` to manage the `hits` (search results) as an empty array <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

In the `search` function:
1.  The current input value is grabbed and formatted as a URL parameter <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
2.  The code executes only if the query length is greater than 2, preventing excessive API calls <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. Debouncing is also recommended to limit calls per keystroke <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
3.  The `fetch` API makes a request to the search endpoint (`/api/search`) with the query parameters <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.
4.  The returned array of cars is set as the component's state <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
5.  Results are displayed in an unordered list, mapping each `hit` to a list item using the entity ID as the key, showing desired data like make, model, and image <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.

This completes the construction of a full-stack full-text search feature using [[implementing_full_text_search_with_redis | Redis]] and [[building_a_nextjs_application_with_redis | Next.js]] <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.