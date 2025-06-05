---
title: Ethical Hacking and Web Security
videoId: v969_M6cWk0
---

From: [[fireship]] <br/> 

Ethical hacking involves finding exploits in web applications before malicious actors do <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. As a web developer, it's crucial to be aware of [[common_web_application_security_risks | 10 common security risks]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. These include database injection, broken authentication, and [[common_web_application_security_risks | cross-site scripting]] <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Historical Exploits

Hackers have been exploiting web vulnerabilities since their inception <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   In 2005, [[common_web_application_security_risks | cross-site scripting]] was famously used to update MySpace pages with "sami is my hero" <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   More recently, the Chinese version of Twitter, Weibo, exposed over 500 million user accounts due to a brute-force attack on their authentication system <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Penetration Testing

To reduce the risk of becoming a victim, developers can run [[penetration_testing_tools_and_techniques | penetration tests]] on their web applications <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. A popular free tool for this is the [[penetration_testing_tools_and_techniques | Burp Suite]] <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

### Burp Suite Functionality

[[penetration_testing_tools_and_techniques | Burp Suite]] acts as a "man in the middle," eavesdropping on or intercepting every request made by a browser when visiting a website <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   Using its proxy tab, an instance of the Chromium browser can be opened to visit a website where permission for [[penetration_testing_tools_and_techniques | penetration testing]] has been granted <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   The tool intercepts requests, allowing users to inspect and optionally modify values before they are sent to the server <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This process helps identify potential requests to exploit <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. For example, by changing the order amount in a post request, a weak server-side validation could lead to an unintended "five-finger discount" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

### Automating Attacks with Intruder

Real-life hacking is rarely simple, often requiring tedious trial and error <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. [[penetration_testing_tools_and_techniques | Burp Suite]]'s Intruder tool can automate brute-force attacks <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. Users can supply username/password combinations that are dynamically added to requests and sent to the server using various attack types <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. After starting the attack, the tool waits for a successful response <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Once access is gained, the same credentials can be used to determine if access can be maintained and sensitive data extracted <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Hacker Hats

The type of "hat" an individual wears depends on their ethical conduct:
*   **White Hat**: Worn by those who have permission to perform testing <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   **Gray Hat**: Worn by those who don't have permission but notify the target of vulnerabilities found <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Black Hat**: Worn by those who sell extracted data (e.g., for Dogecoin on the dark web) <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## Web Security Model: Same-Origin Policy (SOP)

Understanding the [[security_measures_in_frontend_and_backend | web security model]] requires grasping the **Same-Origin Policy (SOP)**, a fundamental principle of web security <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Concept of Origin

An "origin" is defined by a triple: **scheme**, **domain**, and **port** <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   For `https`, the default port is 443 <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   For `http`, the default port is 80 <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   If the scheme, domain, and port are the same, regardless of the path, it is considered the same origin <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   A different subdomain, port, or scheme will constitute a different origin <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

### SOP Purpose and Communication Restrictions

The Same-Origin Policy creates a secure context for websites running in the browser <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   When different origins are loaded in separate tabs, they are isolated and cannot communicate with each other by default <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   This isolation prevents a potentially malicious website from communicating with other websites loaded in the browser <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   It is the browser that enforces the Same-Origin Policy <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

### Exceptions to SOP

While cross-origin communication is generally restricted, certain resources can still be fetched from different origins to enrich a website <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. This includes:
*   Images <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>
*   CSS styles <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>
*   Scripts <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>

For communication to occur between different origins, the target origin must explicitly "whitelist" the requesting origin, indicating it is trustworthy <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

## Same-Origin Policy in Practice

A practical demonstration illustrates how SOP works using two simple Node.js applications:
1.  **Main Application**: Served on `port 8888` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
2.  **External Application**: Simulates an external origin, served on `port 8081` <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>, providing static resources (images, scripts, stylesheets) and an API method <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

### Cross-Origin Resource Fetching

The main application can successfully fetch and apply:
*   External CSS styles from `port 8081` <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
*   Images from `port 8081` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
*   Scripts from `port 8081` <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

### Cross-Origin API Execution

The SOP prevents some API executions:
*   **Internal API Call**: Calling an API endpoint on the *same origin* (main application) is successful, and the response is displayed <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
*   **External API Call**: When the main application attempts to call an API method on the *external origin* (`port 8081`), the request does hit the external server <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. However, the actual response is **blocked by the browser** because the Same-Origin Policy is enforced at the browser level <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. The main origin is not allowed to communicate with the external website to read the result unless explicitly whitelisted <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

In summary, while fetching static resources like images, CSS, and scripts across origins is generally permitted, direct API calls and reading their responses are restricted by the browser's Same-Origin Policy unless specific cross-origin communication rules are established <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. To gain a deeper understanding of the [[security_measures_in_frontend_and_backend | web security model]], including how to prevent [[common_web_application_security_risks | cross-site scripting]] and handle CORS errors, further specialized courses are recommended <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.