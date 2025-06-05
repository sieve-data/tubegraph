---
title: Creating API endpoints with Express
videoId: -MTSQjw5DrM
---

From: [[fireship]] <br/> 

An Application Programming Interface (API) is a method for two computers to communicate with each other <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Using an API is comparable to using a website in a browser, but instead of user interaction, code is written to explicitly request data from a server <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. For example, a REST API can be used to request raw JSON data, rather than visiting a website to view information <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## RESTful APIs

Most APIs globally are RESTful, meaning they adhere to a set of rules or constraints known as Representational State Transfer (REST) <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. REST has been the de facto standard for API development since the early 2000s <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. A RESTful API organizes data entities, or resources, into unique Uniform Resource Identifiers (URIs) <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. These URIs differentiate various types of data resources on a server <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

### Client-Server Communication
A client can obtain data about a resource by making a request to its endpoint over HTTP <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

#### Request Message Structure
The request message has a specific format <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>:
*   **Start Line**: Contains the URI to be accessed, preceded by an HTTP verb or request method <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
    *   `GET` requests are for reading data <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
    *   `POST` requests are for creating a new resource <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
    *   `PATCH` is for updates <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
    *   `DELETE` is for removing data <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Headers**: Located below the start line, headers contain metadata about the request <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Examples include:
    *   `Accept` header: Specifies the desired data format from the server <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
    *   `Authorization` header: Used to authenticate the request with the server <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Body**: Follows the headers and contains a custom payload of data <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

#### Response Message Structure
Upon receiving a request, the server executes code (e.g., to read from a database) and formats a response message <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>:
*   **Status Code**: At the top of the message, indicates what happened to the request <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
    *   `200`-level codes: Indicate success <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   `400`-level codes: Indicate an error with the client's request <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
    *   `500`-level codes: Indicate a server-side failure <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Response Headers**: Contain information about the server <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Response Body**: Contains the data payload, typically formatted in JSON <a class="yt="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

#### Stateless Architecture
An important aspect of this architecture is that it is stateless <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This means that neither the client nor the server needs to store information about each other, and every request-response cycle is independent <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This leads to predictable and reliable web applications <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Building APIs with Express.js

The most popular framework for building RESTful APIs in Node.js is Express.js <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. It is known for being minimal and easy to learn for those with JavaScript knowledge <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

### [[setting_up_a_nodejs_and_express_environment | Setting up a Node.js and Express Environment]]
To get started:
1.  Open VS Code in an empty directory <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Node.js (version 12 used in the example) must be installed <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
2.  Initialize a new Node.js project by running `npm init -y` in the command line <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This creates a `package.json` file <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
3.  Install Express using `npm install express` <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. This adds Express to the project's dependencies in `package.json` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
4.  Create an `index.js` file for writing API code <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
5.  In `index.js`, declare an `app` variable to represent the API, initializing it by importing and calling the `express` package <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>:
    ```javascript
    const express = require('express');
    const app = express();
    const PORT = 8080;
    ```
6.  To start the API server, call `app.listen()` on a specific port, such as `8080` <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. An optional callback function can be provided to confirm when the API is ready <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>:
    ```javascript
    app.listen(
      PORT,
      () => console.log(`it's live on http://localhost:${PORT}`)
    );
    ```
7.  Run the API from the terminal using `node .` (or `node index.js`) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Testing the API
When navigating to `localhost:8080` in a browser, a "Cannot GET" message typically appears because no API endpoints are set up yet <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. The server responds with a `404 Not Found` status code <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

For debugging and interacting with APIs, tools like Insomnia or Postman are recommended over the browser <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. These tools provide a structured way to format requests and view responses <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

### Creating GET Endpoints
API endpoints are defined by chaining HTTP verbs to the `app` instance <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. For example, to add a GET endpoint for the `/tshirt` URI, `app.get()` is used <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. A callback function is passed as the second argument, which handles requests to that URI <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. This function receives `request` and `response` objects <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

```javascript
app.get('/tshirt', (req, res) => {
  res.status(200).send({
    tshirt: '👕',
    size: 'large'
  });
});
```
The `res.status(200)` sets a success status code, and `send()` can transmit a data payload <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. If a JavaScript object is passed, it is sent as JSON by default <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. After saving changes, the server must be restarted <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

### Creating POST Endpoints with Dynamic Parameters
To handle varied resources, dynamic URL parameters can be used <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. For instance, a POST endpoint for a t-shirt with a dynamic ID can be defined as `'/tshirt/:id'` <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

```javascript
app.post('/tshirt/:id', (req, res) => {
  const { id } = req.params; // Get ID from URL parameters
  const { logo } = req.body; // Get logo from request body

  if (!logo) {
    res.status(418).send({ message: 'We need a logo!' });
  } else {
    res.status(200).send({
      tshirt: `👕 with your ${logo}`,
      size: id,
    });
  }
});
```
When dealing with a POST request, the user intends to create new data on the server <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   The dynamic `id` parameter is accessible via `req.params.id` <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   Data from the request body (e.g., `logo`) is available via `req.body` <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### [[using_middleware_and_parsing_json_in_express | Using Middleware and Parsing JSON in Express]]
By default, Express does not parse JSON in the request body, which can lead to errors when attempting to access `req.body` <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. To enable JSON parsing, [[using_middleware_and_parsing_json_in_express | middleware]] must be set up <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. Middleware is shared code that runs before every endpoint callback <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

To apply the `express.json()` middleware, use `app.use()`:
```javascript
const express = require('express');
const app = express();
const PORT = 8080;

app.use(express.json()); // This middleware parses incoming JSON requests

// ... (your existing endpoints)
```
With `app.use(express.json())`, every incoming request will first pass through this middleware, converting the body to JSON and making it accessible in the POST callback function <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

## OpenAPI Specification
The Open API Specification provides a standard way to describe an API in YAML <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. Originally part of the Swagger framework, it allows APIs to be described in a format understood by both humans and machines <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

Benefits of using OpenAPI:
*   **Documentation**: APIs become fully documented, making them easier for end-users to work with <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
*   **Code Generation**: Because it follows a standard format, client-side or server-side code can be automatically generated <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. Tools like SwaggerHub can export boilerplate code <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
*   **Gateway Integration**: Describing an API with the OpenAPI spec allows its configuration to be uploaded to tools like API Gateway on AWS or Google Cloud, where it can be secured, monitored, and connected to backend infrastructure <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.