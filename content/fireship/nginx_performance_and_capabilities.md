---
title: NGINX performance and capabilities
videoId: JKxlsvZXG7c
---

From: [[fireship]] <br/> 

[[NGINX web server | NGINX]] functions as a gateway positioned between the internet and an application's [[backend_development_and_serverside_concepts | backend infrastructure]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. When a web application is accessed, the initial request is directed to a [[backend_development_and_serverside_concepts | web server]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The server's role is to identify the requested resource, locate it on the server, and then return it as a response <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. [[NGINX web server | NGINX]] is commonly identified in the server header of responses in browser developer tools <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## High Performance for High Traffic

[[NGINX web server | NGINX]] is highly favored for high-traffic websites due to its robust performance capabilities <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. It can manage over 10,000 simultaneous connections, thanks to its event-driven architecture <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Versatile Capabilities

### [[reverse_proxy_with_nginx | Reverse Proxy]]

[[NGINX web server | NGINX]] is frequently employed as a [[reverse_proxy_with_nginx | reverse proxy]] <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. In this role, it acts as a traffic controller, distributing the load across multiple [[backend_development_and_serverside_concepts | backend servers]] <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This setup also provides enhanced security and caching for improved performance <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. A [[reverse_proxy_with_nginx | reverse proxy]] configured with [[NGINX web server | NGINX]] can handle caching, anonymity, and load balancing <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### [[serving_static_content_with_nginx | Serving Static Content]]

One of [[NGINX web server | NGINX]]'s primary functions is to [[serving_static_content_with_nginx | serve static content]], such as images and HTML files <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. This is typically configured within the HTTP context, where one or more servers are defined, each listening on a specific port <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. The server's configuration specifies where to locate the raw files on the file system, for instance, by mapping image patterns to an images directory <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

### Other Configurations

Beyond its core roles, [[NGINX web server | NGINX]] server configurations can also manage other features, including:
*   SSL certificates <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
*   Rewrites <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
*   Routing to a [[reverse_proxy_with_nginx | proxy server]] <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>

The behavior of the [[NGINX web server | NGINX]] server is customized by defining [[nginx_configuration_and_directives | directives]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. While some configurations might be in the global context for settings like usernames or error logs, the majority of the configuration is handled within the HTTP context <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. [[NGINX web server | NGINX]] also tracks every request to the server, which can be written to an access log <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.