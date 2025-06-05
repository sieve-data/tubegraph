---
title: Building a RESTful API with Nodejs and Express
videoId: -MTSQjw5DrM
---

From: [[fireship]] <br/> 

An [[APIs and thirdparty services in web development|Application Programming Interface]] (API) is a method for two computers to communicate with each other <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Using an [[APIs and thirdparty services in web development|API]] involves writing code to explicitly request data from a server, similar to how a web browser interacts with a website, but without clicking buttons or filling forms <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. For example, instead of visiting the NASA website to view asteroid information, one could use their [[understanding_restful_apis|REST API]] to request the raw JSON data <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

Most [[APIs and thirdparty services in web development|APIs]] globally are [[understanding_restful_apis|RESTful]], adhering to a set of rules or constraints known as Representational State Transfer (REST) <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. REST has been the de facto standard for [[APIs and thirdparty services in web development|API]] development since the early 2000s <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. A [[understanding_restful_apis|RESTful API]] organizes data entities or resources into unique URIs (Uniform Resource Identifiers) <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Clients can retrieve data about a resource by making a request to its endpoint over HTTP <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Request and Response Structure

An HTTP request message has a specific format <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>:
*   **Start Line**: Contains the URI to be accessed, preceded by an HTTP verb or request method that signals the intent with the resource <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
    *   `GET`: Read data <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
    *   `POST`: Create a new resource <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
    *   `PATCH`: Update a resource <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
    *   `DELETE`: Remove data <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Headers**: Contain metadata about the request, such as the `Accept` header (desired data format) or `Authorization` header (permission to make the request) <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **Body**: Contains a custom payload of data <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

Upon receiving the request, the server executes code (e.g., reads from a database) and formats a response message <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>:
*   **Status Code**: Indicates what happened to the request <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
    *   `2xx` level: Success <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
    *   `4xx` level: Client-side error <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
    *   `5xx` level: Server-side error <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Response Headers**: Provide information about the server <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Response Body**: Contains the data payload, usually formatted in JSON <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

A key aspect of [[understanding_restful_apis|RESTful architecture]] is that it is stateless, meaning neither party needs to store information about each other, and each request-response cycle is independent <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This promotes predictable and reliable web applications <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Building a RESTful API with Express.js

[[middleware_in_expressjs|Express.js]] is the most popular framework for [[building_and_deploying_a_full_stack_application_with_nodejs_and_express|building RESTful APIs]] in [[javascript_serverside_with_nodejs|Node.js]] <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. It is minimal, easy to learn for [[javascript_serverside_with_nodejs|JavaScript]] developers, and has been around for a long time <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

### Prerequisites
To get started, you'll need:
*   VS Code (or another code editor) <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>
*   [[introduction_to_nodejs|Node.js]] installed (version 12 was used in the video) <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>
*   npm (Node Package Manager), which comes with [[introduction_to_nodejs|Node.js]] <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>

### Project Setup
1.  **Initialize a new Node.js project**: Open an empty directory in VS Code and run `npm init -y` in the terminal <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This creates a `package.json` file <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
2.  **Install Express**: Run `npm install express` <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. This adds Express to your `package.json` dependencies <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
3.  **Create `index.js`**: Create a file named `index.js` (or similar) where your application code will reside <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

### Setting up the Express Application
In your `index.js` file:
```javascript
const express = require('express'); // Import the express package
const app = express(); // Initialize the express application
const PORT = 8080; // Define the port for the API to listen on

// Start the API server
app.listen(PORT, () => {
    console.log(`It's live on http://localhost:${PORT}`);
});
```
*   `app` represents the actual [[APIs and thirdparty services in web development|API]] being built <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   `app.listen()` tells the server to listen on a specified port <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   The optional callback function lets you know when the [[APIs and thirdparty services in web development|API]] is ready <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

Run the API from the terminal using `node .` (or `node index.js`) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. If you visit `http://localhost:8080` in a browser, you'll see a "Cannot GET" message, indicating no endpoints are set up yet, but Express is responding <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. The browser's network tab will show a 404 status code <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

### Testing the API
While browsers can be used for basic testing, dedicated [[understanding_restful_apis|REST]] clients like Insomnia or Postman offer better formatting and request management <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. From a client, you can create new requests, change HTTP verbs, and view responses in a developer-friendly way <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Defining API Endpoints

Endpoints are defined on the `app` instance using methods corresponding to HTTP verbs (e.g., `app.get()`, `app.post()`) <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. Each method takes the URI as its first argument and a callback function as the second <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. This callback fires when a client requests that URL and provides `request` (`req`) and `response` (`res`) objects <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

#### GET Endpoint Example
To add a GET endpoint for `/t-shirt`:
```javascript
app.get('/t-shirt', (req, res) => {
    // Send a 200 OK status and a JSON payload
    res.status(200).send({
        product: 'T-Shirt',
        size: 'Large'
    });
});
```
This endpoint responds with a JSON object when a GET request is made to `/t-shirt` <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

#### POST Endpoint Example with Dynamic Parameters
To add a POST endpoint for `/t-shirt/:id` (where `:id` is a dynamic URL parameter):
```javascript
// Add this line BEFORE your app.post() endpoint to parse JSON bodies
app.use(express.json()); // Middleware to parse JSON in request body

app.post('/t-shirt/:id', (req, res) => {
    const { id } = req.params; // Get ID from URL parameters
    const { logo } = req.body; // Get logo from request body

    if (!logo) {
        // Send a 418 status if no logo is provided
        res.status(418).send({ message: 'We need a logo!' });
    } else {
        // Send a successful response with the t-shirt details
        res.status(200).send({
            tshirt: `👕 with your ${logo} and ID of ${id}`
        });
    }
});
```
*   `req.params` allows access to dynamic URL parameters <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   `req.body` contains the custom data payload from the incoming request <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

### [[middleware_in_expressjs|Middleware]] for Request Body Parsing
By default, Express does not parse JSON data in the request body <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. Attempting to destructure properties from `req.body` without parsing will result in a 500 runtime error <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. To fix this, you need to set up [[middleware_in_expressjs|middleware]] that tells Express to parse JSON *before* the request reaches your endpoint handler function <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

[[middleware_in_expressjs|Middleware]] refers to shared code that runs before every endpoint callback you've defined <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. The `express.json()` [[middleware_in_expressjs|middleware]] converts the request body to JSON, making it available in your route handlers <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. It's applied using `app.use(express.json())` <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

### OpenAPI Specification (Swagger)
For serious [[APIs and thirdparty services in web development|API]] development, the OpenAPI Specification (originally part of the Swagger framework) provides a standard way to describe an [[APIs and thirdparty services in web development|API]] in YAML <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. This specification allows [[APIs and thirdparty services in web development|APIs]] to be understood by both humans and machines, offering benefits such as:
*   **Full Documentation**: Makes the [[APIs and thirdparty services in web development|API]] easier for end-users to work with <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
*   **Automatic Code Generation**: Enables automatic generation of client-side or server-side code based on the [[APIs and thirdparty services in web development|API]] description <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
*   **Integration with Cloud Tools**: OpenAPI configurations can be uploaded to services like AWS API Gateway or Google Cloud, allowing the [[APIs and thirdparty services in web development|API]] to be secured, monitored, and connected to backend infrastructure <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.