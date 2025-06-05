---
title: Understanding HTTP verbs and status codes
videoId: -MTSQjw5DrM
---

From: [[fireship]] <br/> 

## Introduction
When [[introduction_to_restful_apis | APIs]] are used for computers to communicate, they employ [[understanding_the_internet_and_the_world_wide_web | HTTP]] verbs (also known as request methods) and status codes to signal intent and outcomes of requests <a class="yt-timestamp" data-t="01:02">[01:02]</a>.

## HTTP Verbs (Request Methods)
An [[understanding_the_internet_and_the_world_wide_web | HTTP]] verb or request method is part of the request message's start line and signals the [[website_access_and_user_interactions | client's]] intent with a resource on the server <a class="yt-timestamp" data-t="01:02">[01:02]</a>.

Common [[understanding_the_internet_and_the_world_wide_web | HTTP]] verbs include:
*   **GET** <a class="yt-timestamp" data-t="01:07">[01:07]</a>: Used to read or retrieve data <a class="yt-timestamp" data-t="01:07">[01:07]</a>.
*   **POST** <a class="yt-timestamp" data-t="01:11">[01:11]</a>: Used to create a new resource on the server <a class="yt-timestamp" data-t="01:11">[01:11]</a>.
*   **PATCH** <a class="yt-timestamp" data-t="01:12">[01:12]</a>: Used for updating existing data <a class="yt-timestamp" data-t="01:12">[01:12]</a>.
*   **DELETE** <a class="yt-timestamp" data-t="01:14">[01:14]</a>: Used for removing data <a class="yt-timestamp" data-t="01:14">[01:14]</a>.

In frameworks like [[using_middleware_and_parsing_json_in_express | Express.js]], these verbs correspond to methods on the `app` instance (e.g., `app.get()`, `app.post()`) for defining [[creating_api_endpoints_with_express | API endpoints]] <a class="yt-timestamp" data-t="05:26">[05:26]</a>.

## HTTP Status Codes
After a server receives and processes a request, it sends a response message that includes a status code <a class="yt-timestamp" data-t="01:43">[01:43]</a>. This code informs the [[website_access_and_user_interactions | client]] about what happened to their request <a class="yt-timestamp" data-t="01:45">[01:45]</a>.

Status codes are categorized by their hundreds digit:
*   **200-level codes**: Indicate that the request was successful and "things went well" <a class="yt-timestamp" data-t="01:47">[01:47]</a>. For example, `200 OK` means the request succeeded <a class="yt-timestamp" data-t="06:24">[06:24]</a>.
*   **400-level codes**: Indicate that "something was wrong with your request" on the [[website_access_and_user_interactions | client's]] side <a class="yt-timestamp" data-t="01:49">[01:49]</a>.
    *   `404 Not Found`: This is a common error indicating the requested page or resource could not be found <a class="yt-timestamp" data-t="03:38">[03:38]</a>.
    *   `418 I'm a teapot`: A specific code used in the transcript to indicate an error where a logo was required but not provided in the request body <a class="yt-timestamp" data-t="08:00">[08:00]</a>.
*   **500-level codes**: Indicate that "the server failed" to fulfill the request <a class="yt-timestamp" data-t="01:53">[01:53]</a>. A `500 Internal Server Error` often means the [[introduction_to_restful_apis | API]] code itself broke <a class="yt-timestamp" data-t="08:32">[08:32]</a>.