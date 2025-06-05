---
title: Setting up a Nodejs and Express environment
videoId: -MTSQjw5DrM
---

From: [[fireship]] <br/> 

An Application Programming Interface (API) allows two computers to communicate with each other <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Most APIs follow the **Representational State Transfer (REST)** principles, which have been the de facto standard for API development since the early 2000s <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. A RESTful API organizes data entities, or resources, into unique Uniform Resource Identifiers (URIs) <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

This guide focuses on setting up a RESTful API from scratch using [[building_and_deploying_a_nodejs_full_stack_application | Node.js]] and Express.js, a popular and minimal framework for building RESTful APIs in [[nodejs_runtime_and_basic_operations | Node.js]] <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## Prerequisites

To get started, you will need:
*   VS Code (or another code editor) <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>
*   [[installing_and_setting_up_nodejs | Node.js]] version 12 or higher installed <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>

## Initializing a Node.js Project

1.  **Open VS Code** to an empty directory <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
2.  **Initialize a new [[nodejs_runtime_and_basic_operations | Node.js project]]**:
    Run `npm init -y` in your terminal <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. This command creates a `package.json` file, which provides context for [[understanding_nodejs_modules_and_packages | installing packages]] <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
3.  **Install Express**:
    Run `npm install express` <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. This adds Express to your dependencies in `package.json` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## Setting Up the Basic Express Application

1.  **Create `index.js`**: Create a file named `index.js` in your project directory <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
2.  **Define the Express app**:
    At the top of `index.js`, declare a variable `app` which represents the API you are building. Its value is an import of the Express package, initialized as a function <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>:

    ```javascript
    const express = require('express');
    const app = express();
    const PORT = 8080; // Define a port for your API
    ```
3.  **Listen for requests**:
    Tell the app to listen on a specific port using `app.listen()` <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. An optional second argument can be a callback function to indicate when the API is ready <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>:

    ```javascript
    app.listen(
      PORT,
      () => console.log(`It's live on http://localhost:${PORT}`)
    );
    ```

## Running and Testing the API

1.  **Run the API**:
    In your terminal, navigate to your project directory and run `node .` (or `node index.js`) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. You should see the console log message indicating the API is live <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
2.  **Initial browser test**:
    If you paste `http://localhost:8080` into your browser, you will likely get a "Cannot GET" message <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. This happens because no API endpoints are set up yet <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. The server will respond with a `404` status code (Not Found) <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
3.  **Using API testing tools**:
    Debugging APIs in a browser is not ideal <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. Tools like **Insomnia** or **Postman**, or command-line utilities like `curl`, provide better ways to make requests and view responses <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

## [[creating_api_endpoints_with_express | Creating API Endpoints]]

Express provides methods corresponding to HTTP verbs (GET, POST, PATCH, DELETE, etc.) on the `app` instance to [[creating_api_endpoints_with_express | create different endpoints]] <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

### GET Endpoint

To add a GET endpoint, use `app.get()`. The first argument is the URI, and the second is a callback function to handle the request <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. This function provides `request` (incoming data) and `response` (data to send back) objects <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

```javascript
// Example GET endpoint
app.get('/tshirt', (req, res) => {
    res.status(200).send({
        product: 'T-shirt',
        size: 'large'
    });
});
```

*   `res.status(200)` sets the HTTP status code to `200` (OK) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
*   `send()` with a JavaScript object automatically sends the data back as JSON <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### POST Endpoint with Dynamic URL Parameters

For a POST request, the user typically wants to create new data <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. You can define dynamic URL parameters using a colon (`:`) followed by the parameter name in the URI, e.g., `/tshirt/:id` <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. These parameters are available on the `request.params` object <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

```javascript
// Example POST endpoint with dynamic ID
app.post('/tshirt/:id', (req, res) => {
    const { id } = req.params; // Get ID from URL parameters
    const { logo } = req.body; // Get logo from request body

    if (!logo) {
        // Send error response if logo is missing
        res.status(418).send({ message: 'We need a logo!' });
    } else {
        // Send success response with received data
        res.status(200).send({
            tshirt: `👕 with your ${logo} and ID of ${id}`,
        });
    }
});
```

## [[using_middleware_and_parsing_json_in_express | Using Middleware and Parsing JSON]]

By default, Express does not parse JSON in the request body <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This means `req.body` will be undefined when a client sends a JSON payload. To fix this, you need to set up [[using_middleware_and_parsing_json_in_express | middleware]] that tells Express to parse JSON before the request hits your endpoint handler function <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

**Middleware** is shared code that runs before every endpoint callback you've defined <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. Express provides built-in middleware for this purpose.

```javascript
const express = require('express');
const app = express();
const PORT = 8080;

// Apply middleware to parse JSON in the request body
app.use(express.json()); // This converts the body to JSON <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>

// ... your endpoint definitions (GET, POST, etc.) ...

app.listen(
    PORT,
    () => console.log(`It's live on http://localhost:${PORT}`)
);
```
With `app.use(express.json())`, `req.body` will now correctly contain the JSON payload from incoming requests.

## Open API Specification

For serious API development, the **Open API Spec** (originally part of the Swagger framework) provides a standard way to describe an API in YAML <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. This specification allows you to:
*   Document your API in a human and machine-understandable format <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
*   Automatically generate client-side or server-side code <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
*   Upload configurations to tools like AWS API Gateway or Google Cloud, where the API can be secured, monitored, and connected to backend infrastructure <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.