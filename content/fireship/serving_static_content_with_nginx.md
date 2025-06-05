---
title: Serving static content with NGINX
videoId: JKxlsvZXG7c
---

From: [[fireship]] <br/> 

[[NGINX web server | NGINX]] acts as a gateway situated between the internet and your backend infrastructure <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. When a request is made to a web application, it first reaches a web server like [[NGINX web server | NGINX]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Its function is to identify the requested resource, locate it on the server, and then return it as a response <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Often, if you inspect the server header in Chrome's developer tools, you'll find [[NGINX web server | NGINX]] listed <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

[[NGINX web server | NGINX]] is highly favored for high-traffic websites because of its ability to manage over 10,000 concurrent connections, attributed to its event-driven architecture <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. It is also commonly utilized as a [[reverse_proxy_with_nginx | reverse proxy]], directing traffic to multiple backend servers, and enhancing [[NGINX performance and capabilities | performance]] through security and caching <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## NGINX Configuration

Typically, [[NGINX web server | NGINX]] is installed on a Linux server, with its [[NGINX configuration and directives | configuration]] file located in the `/etc` directory <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. The server's behavior is customized by defining [[NGINX configuration and directives | directives]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. A [[NGINX configuration and directives | directive]] is a key-value pair, or, if followed by braces, it forms a *context* that contains more [[NGINX configuration and directives | directives]] <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

While global contexts might specify details like usernames or error log locations <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>, the majority of your [[NGINX configuration and directives | configuration]] will be within the `http` context <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Serving Static Content

One of the essential functions of [[NGINX web server | NGINX]] is to serve static content such as images and HTML files <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. This is managed within the `http` context, where you define one or more servers <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>. Each server is identified by the port it listens to <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

[[NGINX web server | NGINX]] can keep a record of all requests to the server, which can be written to an access log <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>. Crucially, you must inform the server where to locate the raw files <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>. This is achieved using the `location` context <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>.

For instance, when a user accesses your domain, [[NGINX web server | NGINX]] uses the `location` context to find the HTML files on the file system <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>. You might also set up a separate `location` to map any image pattern to a specific images directory <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

Beyond basic static file serving, your server [[NGINX configuration and directives | configuration]] can include other common functionalities like SSL certificates, URL rewrites, and routing to a [[reverse_proxy_with_nginx | proxy server]] <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. By replacing `root` with `proxy_pass`, you can direct requests to an entirely different server on the internet, effectively creating a [[reverse_proxy_with_nginx | reverse proxy]] capable of caching, anonymity, and load balancing <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.