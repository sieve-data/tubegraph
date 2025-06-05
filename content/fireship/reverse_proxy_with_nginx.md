---
title: Reverse proxy with NGINX
videoId: JKxlsvZXG7c
---

From: [[fireship]] <br/> 

[[nginx_web_server | NGINX]] commonly serves as a reverse proxy, acting as a traffic light to distribute the load among multiple backend servers <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. In this role, it also provides security and caching for improved [[nginx_performance_and_capabilities | performance]] <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## How it Works <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>

When a user's request arrives at the [[nginx_web_server | NGINX]] [[nginx_web_server | web server]], its job is to determine where to find the requested resource on the server and send it back as the response <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. As a reverse proxy, [[nginx_web_server | NGINX]] stands between the internet and your backend infrastructure <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Configuration <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>

[[nginx_web_server | NGINX]] is typically installed on a Linux server, with its [[nginx_configuration_and_directives | configuration]] file found in the `/etc` directory <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. The server's behavior is customized by defining [[nginx_configuration_and_directives | directives]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. While some [[nginx_configuration_and_directives | directives]] are set in the global context, most [[nginx_configuration_and_directives | configuration]] occurs in the `http` context <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

To configure [[nginx_web_server | NGINX]] as a reverse proxy, you can route to a proxy server <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This is achieved by replacing the `root` [[nginx_configuration_and_directives | directive]] (used for [[serving_static_content_with_nginx | serving static content]]) with `proxy_pass` <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. The `proxy_pass` [[nginx_configuration_and_directives | directive]] allows [[nginx_web_server | NGINX]] to point to a completely different server on the internet <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Benefits <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>

A reverse proxy configured with [[nginx_web_server | NGINX]] can handle:
*   **Caching** <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>
*   **Anonymity** <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
*   **Load Balancing** <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>