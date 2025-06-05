---
title: NGINX configuration and directives
videoId: JKxlsvZXG7c
---

From: [[fireship]] <br/> 

[[nginx_web_server | NGINX]] acts as a gateway between the internet and a web application's [[backend_development_and_serverside_concepts | backend infrastructure]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. When a request is made to a web app, it first goes to a web server, whose job is to identify the requested resource, locate it on the server, and then return it as a response <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. [[nginx_web_server | NGINX]] is highly popular, especially for high-traffic sites, due to its ability to handle over 10,000 simultaneous connections through its event-driven architecture <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Configuration File Location and Structure

[[nginx_web_server | NGINX]] is typically installed on a [[customizing_linux_through_configuration_files | Linux server]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Its primary [[customizing_linux_through_configuration_files | configuration file]] is commonly found in the `/etc` directory <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. The behavior of the server is customized by defining **directives** <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Directives and Contexts
A directive is a key-value pair <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. If a directive is followed by braces (`{}`), it is known as a **context**, which can contain more directives within it <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

### Global Context
In the global context, settings such as a username or the location for error logs might be specified <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

### HTTP Context
The majority of [[nginx_web_server | NGINX]] configuration is typically done within the `http` context <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This context is where one or more `server` blocks are defined <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Server Configuration

Each `server` block is distinguished by the port it listens to <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. [[nginx_web_server | NGINX]] can track every request to a server and write this information to an access log <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Location Context for [[serving_static_content_with_nginx | Static Content]]
A crucial aspect of [[nginx_web_server | NGINX]]'s role is to [[serving_static_content_with_nginx | serve static content]] like images and [[html_structure_and_syntax | HTML]] files <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Within a `server` block, the `location` context is used to specify where to find the raw files on the server's file system <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

For example:
*   When a user navigates to a domain, a `location` block can direct [[nginx_web_server | NGINX]] to the appropriate [[html_structure_and_syntax | HTML]] file <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   Another `location` block can be set up to match image patterns and direct requests to an `images` directory <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### Other Server Configuration Elements
Common elements often included in a server configuration are:
*   SSL certificates <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
*   Rewrites <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
*   Routing to a [[reverse_proxy_with_nginx | proxy server]] <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>

## [[reverse_proxy_with_nginx | Reverse Proxy]] Configuration
[[nginx_web_server | NGINX]] is frequently used as a [[reverse_proxy_with_nginx | reverse proxy]] <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. In this role, it acts as a traffic director, distributing the load to multiple [[backend_development_and_serverside_concepts | backend servers]] <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. It also enhances security and provides caching for [[nginx_performance_and_capabilities | better performance]] <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

To configure [[nginx_web_server | NGINX]] as a [[reverse_proxy_with_nginx | reverse proxy]], the `root` directive can be replaced with `proxy_pass` <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This allows [[nginx_web_server | NGINX]] to point to a different server, potentially on the internet <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This setup enables capabilities such as caching, anonymity, and load balancing <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.