---
title: Using middleware and parsing JSON in Express
videoId: -MTSQjw5DrM
---

From: [[fireship]] <br/> 

When [[creating_api_endpoints_with_express | building API endpoints]] with Express.js, it's crucial to understand how to handle incoming request bodies, especially when they contain JSON data. Express does not parse JSON in the request body by default <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

## Understanding Middleware

Middleware in Express refers to shared code that executes before each endpoint's callback function <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. It acts as an intermediary step in the request-response cycle, allowing you to perform actions like parsing data, authentication, or logging before the request reaches its final handler. Common middleware functions are often built directly into Express <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

## The JSON Parsing Problem in Express

When a client sends a `POST` request, the data intended for creation (e.g., a `logo` for a t-shirt resource) is typically contained in the request body as a custom data payload <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. While the request object in Express provides access to various parts of the incoming message like URL parameters and headers, it doesn't automatically parse the JSON body <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

If you attempt to destructure properties (like `logo`) directly from `request.body` without prior parsing, you will encounter a runtime error <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. This is because Express is designed to be minimal, and not all applications require JSON parsing <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

## Implementing JSON Body Parsing with Middleware

To make JSON data available in your request handlers, you need to set up middleware that instructs Express to parse JSON before the request reaches your endpoint's callback function <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

The `express.json()` middleware is specifically designed for this purpose <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>. When applied, every incoming request will first pass through this middleware, which will convert the request body into a JavaScript object if it's in JSON format <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

### Setup Steps

1.  **Initialize your Node.js project**: Ensure you have Node.js installed (version 12 was used in this demonstration) <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. Start a new [[setting_up_a_nodejs_and_express_environment | Node.js project]] by running `npm init -y` in your terminal <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. This creates a `package.json` file, which helps manage [[understanding_nodejs_modules_and_packages | installed packages]] <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
2.  **Install Express**: Install the Express package by running `npm install express` <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
3.  **Create your application file**: Create an `index.js` file (or similar) to write your application code <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
4.  **Require Express and apply middleware**: In your application file, require Express and use `app.use(express.json())` to apply the JSON parsing middleware. This line should come before your endpoint definitions.

```javascript
// index.js
const express = require('express'); // Refactor for clarity
const app = express();
const PORT = 8080;

// Middleware to parse JSON bodies
app.use(express.json()); <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a> <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>

// Define a POST endpoint for t-shirts with a dynamic ID
app.post('/tshirt/:id', (req, res) => {
    const { id } = req.params; <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>
    const { logo } = req.body; <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>

    if (!logo) {
        res.status(418).send({ message: 'We need a logo!' }); <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>
    } else {
        res.status(200).send({
            tshirt: `👕 with your ${logo} and ID of ${id}`,
        }); <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>
    }
});

// Start the server
app.listen(
    PORT,
    () => console.log(`It's live on http://localhost:${PORT}`)
); <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>
```

After implementing `app.use(express.json())` and restarting your server, incoming `POST` requests with JSON bodies will be successfully parsed, allowing you to access the data via `req.body` <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.