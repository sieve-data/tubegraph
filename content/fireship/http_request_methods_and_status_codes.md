---
title: HTTP request methods and status codes
videoId: -MTSQjw5DrM
---

From: [[fireship]] <br/> 

When two computers communicate via an [[understanding_restful_apis | API]], they do so by sending messages back and forth <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. These messages, especially in the context of [[understanding_restful_apis | RESTful APIs]], adhere to the Hypertext Transfer Protocol (HTTP) specification <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. A crucial part of this communication involves HTTP request methods (verbs) and HTTP status codes.

## HTTP Request Methods (Verbs)

An HTTP request message includes a URI (Uniform Resource Identifier) indicating the resource the client wishes to access, preceded by an HTTP verb or request method <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. These verbs signal the client's intended action with the resource <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

Common HTTP verbs include:
*   **GET** <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>: Used to read or retrieve data from a server <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
*   **POST** <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>: Used to create a new resource on the server <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, or generally to submit data to be processed to a specified resource <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   **PATCH** <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>: Used for updates or partial modifications to an existing resource <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **DELETE** <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>: Used for removing data or a resource <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

Tools like Insomnia or Postman allow developers to easily change the HTTP verb when making requests to an [[understanding_restful_apis | API]] <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. Frameworks like Express.js, used for [[building_a_restful_api_with_nodejs_and_express | building a RESTful API with Node.js and Express]], provide methods corresponding to these verbs (e.g., `app.get`, `app.post`) to define endpoints <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

## HTTP Status Codes

After receiving and processing a client's request, the server sends back a response message <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. The top of this response message contains a status code, which informs the client what happened to their request <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

HTTP status codes are categorized into ranges, each indicating a general class of response:

*   **200-level codes**: Indicate that the request was successful and everything went well <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   *Example*: A `200 OK` status code means the request was successfully processed and the server is returning the requested data <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
*   **400-level codes**: Indicate that there was an error with the client's request <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
    *   *Example*: A `404 Not Found` status code means the server could not find the requested resource <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. Another example shown is `418 I'm a teapot` which can be used to indicate a specific client-side error, such as a missing required parameter <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **500-level codes**: Indicate that the server failed to fulfill a valid request due to an error on the server's side <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
    *   *Example*: A `500 Internal Server Error` means the server encountered an unexpected condition that prevented it from fulfilling the request <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

Monitoring HTTP status codes is essential for debugging and understanding the flow of communication between clients and servers in [[backend_development_and_serverside_concepts | backend development]] <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.