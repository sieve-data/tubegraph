---
title: Object mapping with Redis Ohm and Nodejs
videoId: DOIWQddRD5M
---

From: [[fireship]] <br/> 

[[Redis modules for advanced data handling | Redis Ohm]] is a brand new SDK released by Redis that supports object mapping in [[Introduction to Nodejs | Node.js]] applications <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This library helps map your data into a JavaScript class or entity <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

## Benefits of Redis Ohm
[[Redis modules for advanced data handling | Redis Ohm]] provides several advantages for developers:
*   **Consistent Schema**: It makes it easy to build a consistent schema around your data <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **Simplified Operations**: It simplifies many of the Create, Read, Update, and Delete (CRUD) operations you'll perform on the database <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

## Getting Started with Redis Ohm

### Installation
The project requires `redis-om` as a dependency, which can be installed using npm <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

### Connecting to Redis
To connect to your Redis database, you'll use the `Client` from `redis-om`, which serves as the main entry point for interaction <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
The connection is established by calling `client.open()` with your Redis URL <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. It's recommended to create an asynchronous function, like `connect`, that ensures the connection is only opened if it's not already established <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

```javascript
// lib/redis.js
import { Client } from 'redis-om';

const client = new Client();

export async function connect() {
  if (!client.isOpen()) {
    await client.open(process.env.REDIS_URL);
  }
}
```
<a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>

The `REDIS_URL` can be stored as an environment variable (e.g., in `.env.local` for [[Building a Nextjs application with Redis | Next.js]]) formatted with the username, password, URL, and port of the database <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### Defining an Entity (Schema)
An entity in [[Redis modules for advanced data handling | Redis Ohm]] is comparable to a database table <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. You define an entity by extending a JavaScript class with `Entity` from `redis-om` and providing a schema with properties and their data types <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

By default, this represents a Hash data structure in Redis <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. However, to work with JSON data more like a document-oriented database, you can specify `dataStructure: 'json'` in the schema options <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. This leverages the RedisJSON module <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

```javascript
// lib/redis.js
import { Entity, Schema } from 'redis-om';

class Car extends Entity {}
export const carSchema = new Schema(Car, {
  make: { type: 'string' },
  model: { type: 'string' },
  description: { type: 'string', textSearch: true }, // Enable full-text search on description
  year: { type: 'number' },
  image: { type: 'string' }
}, {
  dataStructure: 'json' // Store data as JSON
});
```
<a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a> <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a> <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>

## Data Operations with Redis Ohm

### Creating Data
To create new data, you first connect to the database and then create a `Repository` by combining the schema and the client <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. New data can be created using the `createEntity()` method with a JavaScript object matching your schema, followed by `repository.save()` to commit it to the database <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. Redis will return an automatically generated unique ID <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

```javascript
// lib/redis.js
import { Client, Entity, Schema } from 'redis-om';
// ... client and connect function defined above ...

// ... carSchema defined above ...

export async function createCar(data) {
  await connect();
  const repository = client.fetchRepository(carSchema);
  const car = repository.createEntity(data); // `data` would come from form input
  return await repository.save(car);
}
```
<a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>

### Indexing for Search
Before performing searches, especially full-text searches, you need to create an index <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. This is typically a one-time operation. You can enable full-text search on specific fields in your schema by adding `textSearch: true` to their definition <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. This allows for fuzzy matching and recognition of typos <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

```javascript
// lib/redis.js
// ... imports and carSchema (with textSearch: true on description) ...

export async function createIndex() {
  await connect();
  const repository = client.fetchRepository(carSchema);
  await repository.createIndex(); // This should only be called once
}
```
<a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>

### Searching Data
To search for data, you use the `repository.search()` method, which offers various capabilities like pagination, counting items, and logical comparisons (e.g., greater than, less than) <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. You can use the `.where()` method to filter by properties, `.eq()` for exact equality, and `.or()` to chain multiple conditions <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. For full-text search, use `.matches()` on fields indexed with `textSearch: true` <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. Finally, `.returnAll()` retrieves all results matching the query <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

```javascript
// lib/redis.js
// ... imports and carSchema ...

export async function searchCars(query) {
  await connect();
  const repository = client.fetchRepository(carSchema);

  return await repository.search()
    .where('make').eq(query)
    .or('model').eq(query)
    .or('description').matches(query) // Full text search on description
    .returnAll();
}
```
<a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>

By integrating [[Redis modules for advanced data handling | Redis Ohm]] with [[Building a Nextjs application with Redis | Next.js]] and [[Introduction to Nodejs | Node.js]], developers can build full-stack applications with robust data handling and [[Implementing full text search with Redis | full text search]] capabilities using [[Using Redis as a primary database | Redis as a primary application database]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.