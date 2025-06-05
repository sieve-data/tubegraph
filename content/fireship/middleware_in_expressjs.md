---
title: Middleware in Expressjs
videoId: -MTSQjw5DrM
---

From: [[fireship]] <br/> 

[[Building a RESTful API with Nodejs and Express | Express.js]] is a popular and minimal framework for [[Building a RESTful API with Nodejs and Express | building RESTful APIs]] in [[JavaScript serverside with Nodejs | Node.js]] <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. It is easy to learn for those familiar with [[JavaScript serverside with Nodejs | JavaScript]] <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## What is Middleware?

Middleware in [[Building a RESTful API with Nodejs and Express | Express.js]] refers to shared code that executes before each endpoint callback function that has been defined in the API <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. Common middleware is often built directly into [[Building a RESTful API with Nodejs and Express | Express]] itself <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

## Purpose and Use Case

By default, [[Building a RESTful API with Nodejs and Express | Express]] does not automatically parse [[APIs and thirdparty services in web development | JSON]] data contained within the body of an incoming request <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This is because not all [[Building a RESTful API with Nodejs and Express | Express]] applications are designed to [[Building a RESTful API with Nodejs and Express | build JSON APIs]] <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

To enable [[Building a RESTful API with Nodejs and Express | Express]] to parse [[APIs and thirdparty services in web development | JSON]] in the request body, middleware must be configured <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. This middleware will process the incoming data *before* it reaches the specific function designed to handle the request <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

## Implementing Middleware

Middleware is applied to an [[Building a RESTful API with Nodejs and Express | Express]] application using the `app.use()` method <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

```javascript
// Declare a variable for Express
const express = require('express');
const app = express();

// Apply the express.json() middleware
app.use(express.json()); <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>
```

When `express.json()` middleware is applied using `app.use()`, every incoming request will first pass through this middleware <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. It converts the request body into a [[APIs and thirdparty services in web development | JSON]] object, making it accessible within the subsequent request handling functions <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. This prevents errors when attempting to access properties like `logo` from the request body <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

### Example of Middleware in Action

Consider a POST endpoint for a t-shirt resource that expects a `logo` in the request body <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>:

```javascript
// Assuming 'app' and 'express' are initialized and express.json() middleware is applied
app.post('/t-shirt/:id', (req, res) => {
    const { id } = req.params; <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>
    const { logo } = req.body; <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>

    if (!logo) { <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>
        res.status(418).send({ message: 'We need a logo!' }); <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>
    } else {
        res.status(200).send({
            tshirt: `👕 with your ${logo} and ID of ${id}`
        }); <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>
    }
});
```

Without the `express.json()` middleware, an attempt to destructure `logo` from `req.body` would result in a runtime error because `req.body` would not be parsed as a [[APIs and thirdparty services in web development | JSON]] object <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. With the middleware, the request body is successfully parsed, allowing the application logic to correctly validate and process the `logo` data <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.