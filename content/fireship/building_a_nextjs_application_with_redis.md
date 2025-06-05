---
title: Building a Nextjs application with Redis
videoId: DOIWQddRD5M
---

From: [[fireship]] <br/> 

This article details how to build a full-text autocomplete search application using [[Next.js]] for the frontend and [[Node.js]] to interact with [[Redis]] on the backend <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. The project leverages the [[Object mapping with Redis Ohm and Nodejs | Redis OM]] SDK for object mapping in [[Node.js]] <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Redis as a Primary Application Database

While commonly known as a fast in-memory database used for caching traditional databases <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, [[Redis]] can also function as a primary application database <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This capability is enabled by a suite of modules that extend core [[Redis]] to handle JSON data, full-text search, graph relationships, and more <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Project Overview: Full-Text Autocomplete Search

The demonstration project is a full-text autocomplete search inspired by services like Algolia or Elasticsearch <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Users can add items to the database and instantly view filtered results <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Data Storage with RedisJSON

Normally, data in [[Redis]] might be saved as a hash data structure, but hashes do not support nested objects <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. To overcome this, the project stores data as native JSON thanks to the RedisJSON module <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### Search Functionality with Redis Search

The autocomplete search feature, which updates results with every keystroke, is made possible by Redis Search <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This powerful module can index all fields on your JSON dataset, enabling complex queries similar to SQL `WHERE` clauses and aggregations like `SUM` and `COUNT` <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Getting Started with Redis

There are several ways to get started with [[Redis]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The easiest option is to sign up for Redis Cloud <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Setting up Redis Cloud

1.  **Create a Subscription**: Choose a free fixed plan to begin <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
2.  **Create a Database**: When creating the database, ensure you add the Redis Search and RedisJSON add-on modules <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
3.  **Connection Details**: Note the public endpoint URL and password for the default user to connect to the database <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

### Redis Insight Tool

It is recommended to download the Redis Insight tool, a GUI for analyzing and managing data in the [[Redis]] database <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
To connect:
1.  Add a new database <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
2.  Paste the public URL from Redis Cloud <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
3.  Enter `default` as the username and the generated password <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### Redis Basics Crash Course

[[Redis]] organizes data into key-value pairs <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **Keys**: Every key is unique and identifies a value <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. Keys can have data types like strings, hashes (for objects), lists, and JSON data <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **SET Command**: To add an item, use the `SET` command, e.g., `SET hello world` <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Time To Live (TTL)**: Data can be set with a TTL, after which it's automatically deleted. Leaving it blank keeps data forever <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **In-Memory Data**: [[Redis]] stores data in memory, making it extremely fast as there's no disk round trip for retrieval <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. On Redis Cloud, this data is also persisted to prevent loss <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   **GET Command**: To read a string, use `GET` followed by the key name, e.g., `GET hello` <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

## Building the Next.js Application

### Initializing the Next.js Project

1.  **Create Next.js App**: Run `npx create-next-app` from the command line <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
2.  **Install Dependency**: Install `redis-om` with `npm install redis-om` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
    *   `redis-om` maps data into a JavaScript class or entity, simplifying schema definition and CRUD operations <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

### Connecting to Redis from Next.js

1.  **Environment Variables**: Create a `.env.local` file with `REDIS_URL` formatted with the username, password, URL, and port of the database <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
2.  **Redis Connection File (`lib/redis.js`)**:
    *   Import `Client` from `redis-om` <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
    *   Connect to the database using `client.open(process.env.REDIS_URL)` <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
    *   Create an async `connect` function to open the connection only if it's not already open (due to [[introduction_to_nextjs | Next.js]]'s workings) <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

### Defining a Data Entity (Schema)

An entity is similar to a database table <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
1.  **Define Class**: Create a class (e.g., `Car`) and extend it with `Entity` from `redis-om` <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
2.  **Schema**: Define properties with specific data types <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
3.  **JSON Data Structure**: To use RedisJSON, add `dataStructure: 'json'` to the entity options, making it behave like a document-oriented database <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### Creating Data

A function `createCar` handles the creation process:
1.  **Connect**: Connects to the database client <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
2.  **Repository**: Creates a `repository` by combining the schema and the client <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
3.  **Create Entity**: Uses `createEntity` with a JavaScript object <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
4.  **Save**: Calls `repository.save` to commit the data to the database <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. [[Redis]] returns an automatically generated unique ID, with the key typically formatted as `car:uniqueid` and the value as JSON data <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### API Route for Data Creation

1.  **Create API Route**: Create `pages/api/cars.js` <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
2.  **Import**: Import the `createCar` function <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
3.  **Handler Function**: Export a default `handler` function that takes `request` and `response` objects <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
4.  **Process Request**: Use `request.body` (JSON data from the form) to call `createCar` <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
5.  **Send Response**: Send a success response back to the client, including the new unique ID <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Frontend Form for Data Creation (`CarForm.js`)

1.  **React Component**: Create `lib/carform.js` as a React component <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
2.  **HTML Form**: Include a standard HTML form with text inputs and a submit button <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
3.  **`handleSubmit` Function**:
    *   Call `event.preventDefault()` to prevent page refresh on submit <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
    *   Convert the form event (`event.target`) to JSON using `FormData` (built into the browser) and `Object.fromEntries` <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. The `name` attribute of form inputs should match the [[Redis]] schema <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
    *   Use the Fetch API to make a `POST` request to the `/api/cars` endpoint <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. Set `Content-Type` to `application/json` and `method` to `POST` <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
    *   Convert the response to JSON and log the result <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

### Displaying the Form and Running the App

1.  **Import Component**: Declare the `CarForm` component in `pages/index.js` <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
2.  **Run App**: Start the [[Next.js]] app by running `npm run dev` <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
3.  **Verify**: Submitting the form should console log the ID created by [[Redis]], and data should be visible in Redis Insight <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

## Querying and Filtering Data with Redis Search

### Creating an Index

To use Redis Search, an index must be created once <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
1.  **`createIndex` Function (`lib/redis.js`)**: Add a `createIndex` function that references the `repository` and calls its `createIndex` method <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
2.  **Full-Text Search Schema Option**: In the schema definition, add `textSearch: true` to any fields (e.g., `description`) where full-text search with fuzzy matching (recognizing typos) is desired <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
3.  **API Route for Index Creation**: Create `pages/api/create-index.js` that imports and calls the `createIndex` function <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. Access `YOUR_APP_URL/api/create-index` in the browser to add the index to the database <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

### Searching for Data

A `searchCars` function (in `lib/redis.js`) handles search queries:
1.  **Input**: Takes a `query` string (user input) <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
2.  **`repository.search`**: Calls the `repository.search` method, which supports various capabilities like pagination, counting, and logical comparisons <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
3.  **`where` Method**: References a property in the JSON data <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
    *   `eq`: For exact equality matches (e.g., `make`).
    *   `or`: To chain multiple search conditions (e.g., `or('model').eq(...)`).
    *   `matches`: For full-text search context on fields with `textSearch: true` (e.g., `description`), returning results even with typos <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
4.  **`returnAll`**: Returns all results from the query <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

### API Route for Search

1.  **Create API Route**: Create `pages/api/search.js` <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
2.  **Handler**: The handler grabs the search query from the URL, calls `searchCars`, and returns an array of cars as the response <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

### Frontend Search Form (`SearchForm.js`)

1.  **React Component**: Create `lib/searchform.js` <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
2.  **Search Input**: An input field triggers a `search` function whenever it changes (on each keystroke) <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
3.  **State**: Uses `useState` to manage the `hits` (search results) as an empty array initially <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
4.  **`search` Function**:
    *   Grabs the current input value and formats it as a URL parameter <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
    *   Executes API calls only if the query length is greater than 2 to prevent excessive calls <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. Debouncing the code is also recommended <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
    *   Uses Fetch API to make a request to the search endpoint (`/api/search`) with the parameters <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
    *   Sets the returned array of cars as the component's state <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.
5.  **Display Results**: Sets up an unordered list and maps each search hit to a list item, using the entity ID as the key and displaying desired data like make, model, and image <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.

This completes the [[building_and_deploying_a_nodejs_full_stack_application | full-stack full-text search feature]] using [[Redis]] and [[Next.js]] <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.