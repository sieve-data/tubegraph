---
title: NGINX web server
videoId: JKxlsvZXG7c
---

From: [[fireship]] <br/> 

NGINX acts as a gateway positioned between the internet and a web application's backend infrastructure <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. When a user accesses a web application, their request first arrives at a web server <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The server's function is to identify the requested resource, locate it on the server, and then return it as a response <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Developers can often observe `nginx` listed as the server in the network tab's server header within Chrome DevTools <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## [[nginx_performance_and_capabilities | Performance and Capabilities]]

NGINX is highly favored by high-traffic websites due to its ability to manage over 10,000 simultaneous connections <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. This impressive capacity is attributed to its efficient event-driven architecture <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Key Roles and Use Cases

### [[reverse_proxy_with_nginx | Reverse Proxy]]

A common application of NGINX is as a [[reverse_proxy_with_nginx | reverse proxy]] <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. In this role, it operates like a traffic light, distributing incoming requests across multiple backend servers <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Beyond load distribution, a [[reverse_proxy_with_nginx | reverse proxy]] also enhances security and provides caching mechanisms for improved [[nginx_performance_and_capabilities | performance]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. When configured as a [[reverse_proxy_with_nginx | reverse proxy]] using `proxy_pass` instead of `root`, NGINX can point to an entirely different server, handling caching, anonymity, and load balancing <a class="yt-timestamp" data-t="01:01:40">[01:01:40]</a>.

### [[serving_static_content_with_nginx | Serving Static Content]]

One of the most crucial functions of NGINX is to [[serving_static_content_with_nginx | serve static content]], such as images and HTML files <a class="yt-timestamp" data-t="01:01:03">[01:01:03]</a>.

## [[nginx_configuration_and_directives | Configuration]]

Typically, NGINX is installed on a Linux server <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, with its [[nginx_configuration_and_directives | configuration]] file located in the `/etc` directory <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. The server's behavior is customized by defining [[nginx_configuration_and_directives | directives]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Directives and Contexts

*   A [[nginx_configuration_and_directives | directive]] is a key-value pair <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   If a [[nginx_configuration_and_directives | directive]] is followed by braces `{}`, it is known as a context <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>, which can contain additional [[nginx_configuration_and_directives | directives]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

### Configuration Contexts

While some settings like username and error log location can be specified in the global context <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>, the majority of the [[nginx_configuration_and_directives | configuration]] is typically done within the `http` context <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

#### HTTP Context

Within the `http` context, one or more `server` blocks are defined <a class="yt-timestamp" data-t="01:01:09">[01:01:09]</a>. Each `server` block is uniquely identified by the port it listens to <a class="yt-timestamp" data-t="01:01:12">[01:01:12]</a>. NGINX tracks every request to the server, and this information can be written to an access log <a class="yt-timestamp" data-t="01:01:17">[01:01:17]</a>.

#### Location Context

Crucially, the `server` block contains `location` contexts <a class="yt-timestamp" data-t="01:01:24">[01:01:24]</a>, which instruct the server where to find the raw files on the file system <a class="yt-timestamp" data-t="01:01:20">[01:01:20]</a>. For example, a `location` block can be set up to direct requests for the domain to the HTML files <a class="yt-timestamp" data-t="01:01:26">[01:01:26]</a>, and another `location` block can match image patterns to an `images` directory <a class="yt-timestamp" data-t="01:01:31">[01:01:31]</a>.

Other common elements configured in a server block include SSL certificates, rewrites, and routing to a [[reverse_proxy_with_nginx | proxy server]] <a class="yt-timestamp" data-t="01:01:36">[01:01:36]</a>.