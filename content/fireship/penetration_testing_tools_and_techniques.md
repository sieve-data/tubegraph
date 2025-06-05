---
title: Penetration Testing Tools and Techniques
videoId: v969_M6cWk0
---

From: [[fireship]] <br/> 

[[Ethical Hacking and Web Security | Ethical hacking]] involves finding exploits in web applications before malicious actors can <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. As a web developer, it's crucial to be aware of common security risks and how to identify vulnerabilities.

## Common Web Security Risks

Web developers should be familiar with 10 common security risks <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. These include:
*   Database injection <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>
*   Broken authentication <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>
*   Cross-site scripting (XSS) <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>

Vulnerabilities like cross-site scripting have been exploited since 2005, for instance, to update MySpace pages <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. More recently, in 2023, a brute force attack on the authentication system of Weibo (the Chinese version of Twitter) exposed over 500 million user accounts <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Purpose of Penetration Testing

To reduce the chances of becoming a victim of such attacks, running penetration tests on web applications is recommended <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Penetration testing helps identify weaknesses by simulating attacks.

## Burp Suite: A Popular Tool

The Burp Suite is a popular free tool used for penetration testing <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. It functions as a "man in the middle" that can eavesdrop on or intercept every request made by a browser when visiting a website <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

### Proxy Feature
The Proxy tab in Burp Suite allows users to open an instance of a Chromium browser to visit a website (with permission for penetration testing) <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. The tool intercepts every request, enabling inspection and optional modification of values before they are sent to the server <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This process helps identify potential requests to exploit, such as changing an order amount on a POST request to exploit weak server-side validation <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

### Intruder Tool
Since real-life hacking often involves tedious trial and error <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, the Intruder tool in Burp Suite can automate brute-force attacks <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. It allows adding various username/password combinations dynamically to a request and sending them to the server using different attack types <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. A successful response indicates a successful attack <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. Once access is gained, the same credentials can be used to determine if access can be maintained to extract sensitive data <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## Types of Hackers

The classification of hackers often depends on their intent and authorization:
*   **White Hat:** Wears a white hat if they have permission to conduct the testing <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Gray Hat:** Wears a gray hat if they don't have permission but notify the target of vulnerabilities found <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   **Black Hat:** Wears a black hat if they sell extracted data (e.g., for Dogecoin on the dark web) <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

## Related Web Security Concept: Same-Origin Policy

The Same-Origin Policy (SOP) is a fundamental principle of the web security model <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### Defining "Origin"
An "origin" is constituted by the triple of scheme (protocol), domain, and port <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   For example, `https://websecurityacademy.com` has an implicit port of 443 (default for HTTPS) <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   `http://websecurityacademy.com` has an implicit port of 80 (default for HTTP) <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   Regardless of the path, if the scheme, domain, and port are the same, it's considered the same origin <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   A different subdomain, port, or scheme will result in a different origin <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

### How Same-Origin Policy Works
The Same-Origin Policy creates a secure context for websites running in the browser <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. If `siteA.com` (origin A) and `siteB.com` (origin B) are loaded in different tabs, they are isolated and cannot communicate with each other by default <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. This isolation prevents a potentially evil website from communicating with other origins without explicit permission <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

However, a website *can* fetch resources like images, CSS styles, or scripts from a different origin to enrich its content <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. It's the browser that enforces the Same-Origin Policy <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. For one origin (e.g., origin A) to communicate with another (e.g., origin B), origin B must explicitly whitelist origin A, indicating it's trustworthy <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### Practical Demonstration
A demonstration using Node.js and Express.js shows two applications:
*   A main application served on port 8888 <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
*   An "external" application simulating an external origin served on a different port <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

The demonstration illustrates:
*   **Allowed Cross-Origin Fetches:** External CSS styles, images, and scripts from the external origin (e.g., port 8081) were successfully applied and loaded by the main application <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Restricted API Communication:**
    *   Calling an API endpoint on the *same* origin (e.g., the main application on port 8888) was successful <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
    *   However, when attempting to call an API endpoint on the *external* origin, the request *did* hit the external server (evidenced by a server-side log) <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. But the actual response was *blocked* by the browser because the Same-Origin Policy prevented the main application from reading the result <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. This highlights that API execution is prevented by SOP, while fetching static resources like images/scripts is not <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.