---
title: Common Web Application Security Risks
videoId: v969_M6cWk0
---

From: [[fireship]] <br/> 

As an [[introduction_to_web_development | web developer]], it is crucial to be aware of common [[security_measures_in_frontend_and_backend | security risks]] that can affect web applications <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. These vulnerabilities can be exploited by malicious actors, leading to data breaches and compromised systems <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Key Security Risks

Some of the common security risks include:
*   [[database_options_for_web_applications | Database]] injection <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>
*   Broken authentication <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>
*   Cross-site scripting (XSS) <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>

### Historical Examples of Exploitation

*   In 2005, cross-site scripting was used to update MySpace pages with unwanted content <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
*   In 2022, the Chinese version of Twitter, Weibo, exposed over 500 million user accounts due to a brute force attack on their authentication system <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Mitigation Strategies

To reduce the chances of becoming a victim of such attacks, running penetration tests on web applications is essential <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

### Burp Suite for Penetration Testing

Burp Suite is a popular and free tool used for penetration testing <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. It functions as a "man-in-the-middle" proxy, allowing users to eavesdrop on or intercept every request made by a browser to servers <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

#### How Burp Suite Works
1.  **Proxy Tab**: Access the proxy tab on the Burp Suite dashboard <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
2.  **Chromium Browser**: Open an instance of the Chromium browser through Burp Suite <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
3.  **Website Interaction**: Visit a website for which permission to run penetration testing has been granted <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
4.  **Request Interception**: Burp Suite intercepts every request, enabling inspection and optional modification of values before they are sent to the server <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. This process helps identify potential requests to exploit <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

#### Example Exploitation
If a user submits a form to complete a shopping cart order, Burp Suite can intercept the POST request <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. If the server-side validation is weak, modifying the order amount in the intercepted request could potentially result in an unauthorized "discount" <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

#### Automating Attacks with Intruder Tool
While manual hacking is tedious, the Intruder tool in Burp Suite can automate brute-force attacks <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. It can dynamically add username and password combinations to requests and send them to the server with various attack types, allowing the user to await a successful response <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. Once access is gained, these credentials can be used to maintain access and extract sensitive data <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Ethical Considerations in Hacking
*   **White Hat**: Performing penetration testing with explicit permission <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Gray Hat**: Hacking without permission but notifying the target of vulnerabilities <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Black Hat**: Hacking maliciously, often for personal gain, like selling data on the dark web <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

## Same-Origin Policy (SOP)

The Same-Origin Policy is a fundamental principle of the web security model <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. It creates a secure context for websites running in the browser <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

### Understanding Origin
An "origin" is defined by the triple of scheme (protocol), domain, and port <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **Same Origin**: If the scheme, domain, and port are identical, regardless of the path, it is considered the same origin <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   For HTTPS, the default port is 443 (implicit) <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   For HTTP, the default port is 80 (implicit) <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **Different Origin**: A different subdomain, port, or scheme constitutes a different origin <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

### SOP in Practice
SOP ensures that separate origins loaded in different browser tabs cannot directly communicate with each other; they are isolated <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. However, it is possible to fetch resources like images, CSS styles, or scripts from different origins to enrich a website <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. The browser enforces this policy <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

By default, SOP restricts cross-origin communication between websites because the browser cannot implicitly trust different origins <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. For communication to occur, the target origin must explicitly "whitelist" the requesting origin, declaring it trustworthy <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

#### Practical Demonstration (Node.js and Express.js)
A demonstration using Node.js and Express.js illustrates SOP <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **Main Application**: Served on port 8080 <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
*   **External Application**: Simulates an external origin, served on a different port (e.g., 8081), providing static resources (image, script, stylesheet) and an API method <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

**Observations:**
*   **Successful Resource Fetching**: External CSS, images, and scripts (e.g., a script displaying "I was fetched from external origin") from different origins (different ports) are successfully loaded and executed on the main application <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **API Call Restriction**: While an internal API call on the main application succeeds <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>, attempting to call an API method on the *external* origin shows a different behavior <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
    *   The request *hits* the external server, and the server logs indicate the external API was called <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
    *   However, the actual **response is blocked on the browser level** because SOP prevents reading the result from a different origin unless explicitly allowed <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

In summary, while resources like stylesheets and scripts can be executed across origins, the Same-Origin Policy prevents reading results from cross-origin API calls unless specific permissions (like Cross-Origin Resource Sharing, CORS) are configured <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. Understanding this policy is crucial for efficiently preventing [[firebase_app_vulnerabilities_and_exploitation | cross-site scripting]] and minimizing related risks <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.