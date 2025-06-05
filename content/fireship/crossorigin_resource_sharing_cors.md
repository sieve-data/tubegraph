---
title: CrossOrigin Resource Sharing CORS
videoId: v969_M6cWk0
---

From: [[fireship]] <br/> 

[[understanding_same_origin_policy | Cross-Origin Resource Sharing]] (CORS) is a mechanism that helps manage the "Cross Origin Risk of Sharing" <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Its purpose is to address the restrictions imposed by the fundamental principle of web security, the [[understanding_same_origin_policy | Same Origin Policy]] <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## Ethical Hacking and Web Security Risks

Before delving into CORS, it's important to understand the broader context of web application security. Ethical hacking involves finding exploits in web applications before malicious actors do <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Web developers should be aware of [[common_web_application_security_risks | 10 common security risks]], including database injection, broken authentication, and [[common_web_application_security_risks | cross-site scripting]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. These vulnerabilities have been exploited for many years, as seen with a [[common_web_application_security_risks | cross-site scripting]] incident on MySpace in 2005 <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>, and a brute force attack on Weibo in 2022 exposing 500 million user accounts <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

Running penetration tests on web applications can reduce the chances of being a victim <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Tools like Burp Suite can act as a man-in-the-middle to eavesdrop on or intercept every request made by a browser <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. This allows inspection and modification of request values before they reach the server <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. For instance, modifying a shopping cart order amount in a POST request could exploit weak server-side validation <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Automated brute-force attacks can be performed using tools like the "Intruder" in Burp Suite <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

## Understanding the Concept of Origin

To understand CORS, it's crucial to grasp the concept of an "origin" <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. An origin is constituted by the triple of:
1.  **Scheme** (e.g., `https://`) <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>
2.  **Domain** (e.g., `websecurityacademy.com`) <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>
3.  **Port** (e.g., `443` for HTTPS, `80` for HTTP, or explicitly specified) <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>

If the scheme, domain, and port are identical, regardless of the path, it is considered the same origin <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. A different subdomain, port, or scheme will result in a different origin <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## [[understanding_same_origin_policy | Same Origin Policy]]

The [[understanding_same_origin_policy | Same Origin Policy]] creates a secure context for websites running in the browser <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   **Isolation:** If two different origins (e.g., `siteA.com` and `siteB.com`) are loaded in different browser tabs, they are isolated and cannot communicate with each other by default <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   **Browser Enforcement:** The browser is responsible for enforcing the [[understanding_same_origin_policy | Same Origin Policy]] <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   **Restricted Communication:** By default, a website from one origin is not allowed to communicate directly with another origin, preventing potential malicious interactions <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

### Exceptions: Permitted Cross-Origin Resource Loading

While direct communication is restricted, certain resources can still be fetched from different origins to enrich a website:
*   Images <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>
*   CSS styles <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>
*   Scripts <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>

### Enabling Cross-Origin Communication

For one origin (e.g., `Origin A`) to communicate with another (e.g., `Origin B`), `Origin B` must explicitly "whitelist" `Origin A`, thereby indicating that `Origin A` is trustworthy <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. This whitelisting is handled by [[understanding_same_origin_policy | Cross-Origin Resource Sharing]] (CORS).

## Practical Demonstration of [[understanding_same_origin_policy | Same Origin Policy]]

A practical example demonstrates the [[understanding_same_origin_policy | Same Origin Policy]] using two Node.js applications, `app1` (running on port `8888`) and `external-app` (running on port `8081`), simulating different origins <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

### Allowed Actions
*   **Fetching Static Resources:** `app1` can successfully load external CSS files, images, and scripts from `external-app` (on port `8081`) <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. The browser successfully applies external styles and loads images <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. Scripts from external origins can also be imported without issues <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

### Restricted Actions
*   **API Calls:** While an internal API call from `app1` to its own server is successful <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>, an attempt to call an API endpoint on `external-app` (different origin) demonstrates the policy in action <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
    *   The request *does* reach the `external-app` server, which logs that the "external API was called" <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
    *   However, the actual **response** from the `external-app` is **blocked** by the browser due to the [[understanding_same_origin_policy | Same Origin Policy]] enforcement at the browser level <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. This prevents `app1` from reading the result of the cross-origin API call <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

To summarize, external stylesheets, images, and scripts can be executed on a website, but calling an external API is prevented from reading the result unless explicitly allowed by the server with CORS <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. Understanding these concepts is vital for preventing web security vulnerabilities like [[common_web_application_security_risks | cross-site scripting]] <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.