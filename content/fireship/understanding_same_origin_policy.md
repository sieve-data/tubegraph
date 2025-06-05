---
title: Understanding Same Origin Policy
videoId: v969_M6cWk0
---

From: [[fireship]] <br/> 

The Same Origin Policy (SOP) is a fundamental principle of the web security model [02:28], enforced by the browser to create a secure context for websites [03:41]. It governs how documents or scripts loaded from one origin can interact with resources from another origin [03:38].

## What Defines an Origin?

An "origin" is constituted by the triple of:
*   **Scheme (Protocol):** Such as `https` [02:47], where `https` typically defaults to port `443` and `http` to port `80` [03:01].
*   **Domain:** For example, `websecurityacademy.com` [02:50].
*   **Port:** The specific port number [02:50].

If the scheme, domain, and port are identical, regardless of the path, it is considered the same origin [03:14]. A different subdomain, a different port, or a different scheme will result in a different origin [03:22].

## How Same Origin Policy Works

The Same Origin Policy prevents a website from one origin from directly communicating with or accessing sensitive data from another origin without explicit permission [03:48]. This is crucial as it creates an isolated, secure context for each website running in the browser, preventing a malicious website from accessing data from other legitimate sites a user might be logged into [03:41].

### Allowed Cross-Origin Interactions

While SOP restricts direct communication, it allows certain resources to be fetched from different origins to enrich a website:
*   Images [04:08], [04:40], [10:04]
*   CSS styles [04:40], [10:04]
*   Scripts (JavaScript) [04:40], [10:04]

The browser enforces this policy [04:50], binding the origin, its execution, and related scripts within its secure context [04:59].

### Restricted Cross-Origin Interactions

By default, SOP restricts direct programmatic communication between different origins [05:10]. For example, one website is not allowed to communicate with [[site_b_communication | site B]] because the browser needs to prevent potentially malicious websites from interacting with others [05:20], [05:30].

For cross-origin communication to be allowed, the target origin (e.g., origin B) must explicitly "whitelist" the requesting origin (e.g., origin A), declaring it trustworthy [05:39]. This is often managed using [[CrossOrigin Resource Sharing CORS | Cross-Origin Resource Sharing (CORS)]] [02:17].

## Practical Demonstration

A practical demonstration illustrates SOP using two Node.js applications with Express.js [06:12]:
*   **Application 1 (Main Origin):** Served on port `8888` [06:46].
*   **Application 2 (External Origin):** Served on a different port, `8081` [06:53].

### Allowed Cross-Origin Resource Loading
The main application successfully requests and applies external CSS, loads images, and imports scripts from the external origin, confirming that these resource types are allowed under SOP [07:40], [07:55], [08:35].

### Restricted Cross-Origin API Calls
When an API call is made from the main application to an API endpoint on the external origin:
1.  The request successfully *hits the server* of the external origin, and the server processes it [09:36].
2.  However, the *browser blocks the actual response* from being read by the main application [09:43]. This occurs because SOP is enforced at the browser level, preventing the result from being exposed to an untrusted origin [09:46], [09:50], [10:01].

Conversely, an API call to an endpoint within the *same origin* is successful, with both the server processing the request and the browser allowing the response to be read [09:07], [10:15].

## Importance in Web Security

Understanding SOP is critical for web developers as it's a foundational [[Security Measures in Frontend and Backend | security measure]] against many [[Common Web Application Security Risks | common web application security risks]] [02:28]. It helps minimize the risk of issues like [[Common Web Application Security Risks | cross-site scripting]] (XSS) by preventing malicious scripts loaded from one origin from interacting with resources of another [10:52]. This ensures that even if a part of an application is compromised, the damage is contained within its origin, preventing unauthorized access to other applications or user data.