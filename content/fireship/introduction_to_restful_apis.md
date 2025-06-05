---
title: Introduction to RESTful APIs
videoId: -MTSQjw5DrM
---

From: [[fireship]] <br/> 

An Application Programming Interface (API) is a method for two computers to communicate with each other <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Using an API is similar to interacting with a website in a browser, but instead of clicking buttons, you write code to explicitly request data from a server <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. For example, one could visit the NASA website to view asteroids, or use their REST API to request the raw JSON data <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## What is a RESTful API?
Most APIs globally are "restful," meaning they adhere to a set of rules or constraints known as Representational State Transfer (REST) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. REST has been the de facto standard for API development since the early 2000s <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

A RESTful API organizes data entities or resources into unique Uniform Resource Identifiers (URIs) <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

### Anatomy of an HTTP Request
A client can retrieve data about a resource by making a request to its endpoint over HTTP <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. An HTTP request message has a specific format <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>:
*   **Start Line**: Contains the URI to be accessed, preceded by an HTTP verb (or request method) that signals intent with the resource <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
    *   `GET`: To read data <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
    *   `POST`: To create a new resource <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
    *   `PATCH`: For updates <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
    *   `DELETE`: For removing data <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Headers**: Located below the start line, headers contain metadata about the request <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Examples include:
    *   `Accept`: Specifies the desired data format from the server <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
    *   `Authorization`: Used to authenticate and permit the request <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   **Body**: Follows the headers and contains a custom payload of data for the server to receive <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### Anatomy of an HTTP Response
After receiving the request message, the server executes code (often reading from a database) and formats a response message <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>:
*   **Status Code**: At the top of the message, indicating the outcome of the client's request <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
    *   `200-level`: Indicates success <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   `400-level`: Means there was an error with the client's request <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
    *   `500-level`: Indicates a server failure <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Response Headers**: Contain information about the server <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Response Body**: Contains the data payload, typically formatted in JSON <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### Statelessness
A crucial aspect of RESTful architecture is its statelessness <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This means neither the client nor the server needs to store information about each other, and every request-response cycle is independent <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This leads to predictable and reliable web applications <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Building a RESTful API with Express.js
Express.js is a popular, minimal, and easy-to-learn framework for [[creating_api_endpoints_with_express | building RESTful APIs]] in Node.js <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### Setup and Basic API
1.  **Initialize Project**: Open VS Code in an empty directory. Ensure Node.js (version 12 used in the video) is installed <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Run `npm init -y` from the command line to create `package.json` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
2.  **Install Express**: Install Express by running `npm install express` <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. This adds Express to `package.json` dependencies <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
3.  **Create `index.js`**: Create an `index.js` file <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. Declare an `app` variable to represent the API, initializing it with `express()` <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
    ```javascript
    const express = require('express');
    const app = express();
    const PORT = 8080;
    ```
4.  **Listen for Requests**: Fire up the API on the server by calling `app.listen()` on a specific port (e.g., 8080) <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. An optional callback can confirm when the API is ready <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
    ```javascript
    app.listen(
      PORT,
      () => console.log(`It's live on http://localhost:${PORT}`)
    );
    ```
5.  **Run API**: Run the API from the terminal using `node index.js` (or `node .`) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. It should log "It's live on localhost 8080" <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. Visiting `http://localhost:8080` in a browser will return "Cannot GET" with a 404 status code because no endpoints are set up yet <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### Accessing the API
While a browser can be used for basic GET requests, dedicated REST clients like Insomnia or Postman are better for debugging <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. These tools allow easy modification of HTTP verbs and provide nicely formatted responses <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

### Creating a GET Endpoint
[[creating_api_endpoints_with_express | Endpoints]] are added by calling an HTTP verb method on the `app` instance (e.g., `app.get()`, `app.post()`) <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Define Endpoint**: Pass the URI (e.g., `/tshirt`) as the first argument <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   **Handle Request**: A callback function is passed as the second argument, which fires when a client requests that URL <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   **Request/Response Objects**: The callback provides `request` and `response` objects. `request` contains incoming data, while `response` is used to send data back <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   **Send Response**: Use `res.status().send()` to send a status code (e.g., 200 for OK) and a data payload <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. Passing a JavaScript object will send it as JSON by default <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

```javascript
app.get('/tshirt', (req, res) => {
    res.status(200).send({
        tshirt: '👕',
        size: 'large'
    });
});
```
After saving and restarting the server, a GET request to `localhost:8080/tshirt` will return a JSON object with a 200 status code <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

### Creating a POST Endpoint
A POST request is typically used to create new data <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   **Dynamic URL Parameters**: Use a dynamic URL parameter (e.g., `/tshirt/:id`) to handle many resources with a single function <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. The parameter's value is available on `req.params.id` <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Request Body**: Data for creation is often in the request body, accessible via `req.body` <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Validation**: Implement checks (e.g., if a `logo` exists in the body) and send appropriate error responses (e.g., 418 status code) <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

```javascript
app.post('/tshirt/:id', (req, res) => {
    const { id } = req.params;
    const { logo } = req.body;

    if (!logo) {
        res.status(418).send({ message: 'We need a logo!' });
    }

    res.status(200).send({
        tshirt: `👕 with your ${logo} and ID of ${id}`,
    });
});
```

### Middleware for Request Body Parsing
By default, Express does not parse JSON in the request body <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Middleware Concept**: Middleware is shared code that runs before every endpoint callback <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
*   **Apply Middleware**: Use `app.use()` to apply middleware, such as `express.json()`, to parse incoming JSON payloads <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. This converts the body to JSON, making it available in endpoint callbacks <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

```javascript
const express = require('express');
const app = express();
const PORT = 8080;

app.use(express.json()); // This line is crucial for parsing JSON request bodies

app.get('/tshirt', (req, res) => {
    // ... (GET endpoint code)
});

app.post('/tshirt/:id', (req, res) => {
    // ... (POST endpoint code)
});

app.listen(
  PORT,
  () => console.log(`It's live on http://localhost:${PORT}`)
);
```
With `express.json()` middleware in place, sending a POST request with a JSON body to `localhost:8080/tshirt/123` will now successfully process the `logo` <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

## OpenAPI Specification (Swagger)
The OpenAPI Specification, originally from the Swagger framework, provides a standard way to describe an API in YAML format <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
*   **Documentation**: It allows describing APIs in a human and machine-understandable format <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>, making them fully documented and easier for end-users <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
*   **Code Generation**: Because it follows a standard format, it can automatically generate client-side or server-side boilerplate code <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Deployment Integration**: Describing an API with the OpenAPI spec enables uploading the configuration to tools like API Gateway on [[introduction_to_amazon_web_services_aws | AWS]] or Google Cloud, where it can be secured, monitored, and connected to backend infrastructure <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.