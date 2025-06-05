---
title: Understanding RESTful APIs
videoId: -MTSQjw5DrM
---

From: [[fireship]] <br/> 

An [[APIs and thirdparty services in web development | Application Programming Interface (API)]] is a method for two computers to communicate with each other <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Using an API is similar to using a website in a browser, but instead of clicking buttons, code is written to explicitly request data from a server <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. For instance, one could use NASA's REST API to request raw JSON data about asteroids, rather than visiting their website <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## What is a RESTful API?

Most APIs are "RESTful," meaning they adhere to a set of rules or constraints known as Representational State Transfer (REST) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. REST has been the de facto standard for API development since the early 2000s <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

A RESTful API organizes data entities or resources into unique Uniform Resource Identifiers (URIs) <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. These URIs differentiate various types of data resources on a server <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## HTTP Request and Response Cycle

A client can obtain data about a resource by making a request to its endpoint over [[Understanding the internet and web infrastructure | HTTP]] <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

### Request Message Format

An [[HTTP request methods and status codes | HTTP request message]] has a specific format <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>:
*   **Start Line**: Contains the URI to be accessed, preceded by an [[HTTP request methods and status codes | HTTP verb]] or request method that signals the intent with the resource <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
    *   `GET`: Used to read data <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
    *   `POST`: Used to create a new resource <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
    *   `PATCH`: Used for updates <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
    *   `DELETE`: Used for removing data <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Headers**: Below the start line, headers contain metadata about the request <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Examples include:
    *   `Accept` header: Specifies the desired data format from the server <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
    *   `Authorization` header: Used to authenticate the request <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Body**: Contains a custom payload of data <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### Response Message Format

The server receives the request, executes code (often reading from a database), and formats a response message <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>:
*   **Status Code**: The top of the message contains an [[HTTP request methods and status codes | HTTP status code]] to inform the client what happened to their request <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
    *   `200` level: Indicates success <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   `400` level: Means something was wrong with the client's request <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
    *   `500` level: Means the server failed <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Response Headers**: Contain information about the server <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Response Body**: Contains the data payload, usually formatted in JSON <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### Statelessness

A crucial aspect of this architecture is its stateless nature <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This means the two parties (client and server) do not need to store information about each other, and every request-response cycle is independent <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This promotes predictable and reliable web applications <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Building a RESTful API

The most popular framework for [[Building a RESTful API with Nodejs and Express | building a RESTful API with Node.js]] is Express.js <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. It is minimal, easy to learn for those with JavaScript knowledge, and has been around for a long time <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### Example with Express.js

To start a new Node.js project, `npm init -y` is run to create a `package.json` file, which manages dependencies <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Express can then be installed using `npm install express` <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. An `index.js` file is created, where the Express application (`app`) is initialized <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

The API is started by calling `app.listen()` on a specific port, e.g., 8080 <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Initially, without any defined endpoints, a browser request to `localhost:8080` will return a `404 Not Found` status <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. Tools like Insomnia or Postman are useful for debugging APIs as they provide a clear way to format requests and view responses <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

#### Defining Endpoints

Endpoints are defined on the `app` instance using [[HTTP request methods and status codes | HTTP verbs]] <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **GET Endpoint**: To add a GET endpoint, for example `/tshirt`, a callback function is passed as the second argument to `app.get('/tshirt', callback)` <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. This function receives `request` and `response` objects <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. The `response` object can be used to send a status code (e.g., `200`) and a JSON data payload <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   **POST Endpoint**: A POST endpoint, such as `/tshirt/:id`, uses a dynamic URL parameter for the ID <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. For a POST request, the ID can be accessed from `request.params.id`, and data from the request body can be accessed from `request.body` <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. Error responses, like `418` (I'm a teapot) can be sent if required data (e.g., a logo) is missing <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.

#### Middleware

Express does not parse JSON in the request body by default <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. To enable this, [[Backend development and serverside concepts | middleware]] must be set up <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. Middleware is shared code that runs before every endpoint callback <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. `app.use(express.json())` applies the built-in Express JSON middleware, which converts the request body to JSON, making it accessible in endpoint callbacks <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

## OpenAPI Specification

The [[OpenAPI Specification and its benefits | OpenAPI Specification]] provides a standard way to describe an API, typically in YAML format <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. Originating from the Swagger framework, it allows APIs to be described in a way understood by both humans and machines <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

Benefits of using OpenAPI:
*   **Documentation**: Provides full documentation, making it easier for end-users <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
*   **Code Generation**: Automatically generates client-side or server-side boilerplate code due to its standard format <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Cloud Integration**: Allows API configurations to be uploaded to tools like API Gateway on AWS or Google Cloud, where they can be secured, monitored, and connected to [[Backend development and serverside concepts | backend infrastructure]] <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.