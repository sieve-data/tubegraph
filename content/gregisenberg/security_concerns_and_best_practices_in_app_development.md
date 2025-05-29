---
title: Security concerns and best practices in app development
videoId: 9YPebrSjskU
---

From: [[gregisenberg]] <br/> 

When developing applications, particularly with the aid of AI, several security concerns arise, especially regarding the handling of sensitive information like API keys. Adopting best practices and understanding the underlying principles of secure development are crucial.

## Handling API Keys

### Location of API Keys
A key security concern in app development is where to store and access API keys. Ideally, API keys should reside in the backend of an application and not be hardcoded into the frontend <a class="yt-timestamp" data-t="00:23:52">[00:23:52]</a>. While the transcript mentions, "in theory, this stuff should be living in the back end" <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>, it also notes that for demonstration or speed purposes, keys might sometimes be placed in the frontend <a class="yt-timestamp" data-t="00:23:56">[00:23:56]</a>. This is, however, an acknowledged issue <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>.

The challenge of [[implementing_authentication_and_backend_services_in_saas | implementing authentication and backend services in SaaS]] applications means that robust solutions are needed to protect sensitive credentials.

### Risks of Hardcoding API Keys
Hardcoding API keys into the frontend presents significant risks. An example shared illustrates this danger:
> "We decided to make a tiny tool internally for my other company and it was just like a a small Verscell app, like a tiny Versel app to automate something for the marketing department, but we use cursor and it hardcoded the open router key into the front end... And they racked up like $300 worth of credits in like a day. This was like last week that this happened and I was like, 'Okay, this is really dangerous.'" <a class="yt-timestamp" data-t="00:55:16">[00:55:16]</a>

This incident suggests that bots actively scan publicly accessible applications, including those deployed on platforms like [[using_bolt_for_web_app_development | Vercel]], for exposed API keys <a class="yt-timestamp" data-t="00:55:36">[00:55:36]</a>. This highlights a critical need to avoid embedding [[utilizing_api_tokens_for_application_development | API tokens for application development]] directly in client-side code <a class="yt-timestamp" data-t="00:55:08">[00:55:08]</a>.

## General Development Practices

### Using AI Tools Safely
While [[the_potential_of_ai_in_app_development | AI in app development]] tools like Cursor can significantly accelerate the process of [[building_consumer_mobile_apps | building consumer mobile apps]], they also introduce potential pitfalls, especially for less experienced developers.
> "cursor is a little more dangerous because that thing can really destroy things and it's it's very hard. Like for example, what we saw here was it decided to code all of this stuff in the front end. That is very dangerous because like for example... it hardcoded the open router key into the front end." <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>

For non-developers, it is recommended to use tools with more "guardrails" or built-in checks, such as Replit or Lovable, as they may prevent accidental exposure of sensitive information <a class="yt-timestamp" data-t="00:55:55">[00:55:55]</a>.

### Importance of Programming Fundamentals
Even with powerful AI tools, understanding the basics of programming is crucial for secure and effective development. Developers who are adept at traditional programming will benefit the most from AI tooling <a class="yt-timestamp" data-t="00:53:59">[00:53:59]</a>.

It is advised for all individuals, regardless of their development background, to:
*   Learn some basics of programming <a class="yt-timestamp" data-t="00:56:06">[00:56:06]</a>.
*   Take a couple of courses <a class="yt-timestamp" data-t="00:56:09">[00:56:09]</a>.
*   Use AI as a teacher to get better at fundamental concepts <a class="yt-timestamp" data-t="00:56:11">[00:56:11]</a>.
This foundational knowledge allows developers to identify and correct issues, such as sensitive data being placed in the wrong location, even when using AI for code generation <a class="yt-timestamp" data-t="00:56:14">[00:56:14]</a>.