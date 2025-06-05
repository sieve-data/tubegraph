---
title: Scaling Pocketbase applications on the cloud
videoId: gUYBFDPZ5qk
---

From: [[fireship]] <br/> 

Pocketbase, a free and open-source backend written in Go, offers user authentication and a real-time database powered by SQLite. A key feature is its ability to compile everything into a single executable, meaning self-hosting only requires one small server <a class="yt-timestamp" data-t="01:05:13">[01:05:13]</a>. The simplicity of [[deploying_pocketbase_to_a_linux_server | Pocketbase]] on a single server raises questions about its scalability <a class="yt-timestamp" data-t="01:17:99">[01:17:99]</a>.

## Cloud Deployment Fundamentals

Deploying Pocketbase to a Linux server in the cloud is the first step towards scaling <a class="yt-timestamp" data-t="01:23:44">[01:23:44]</a>. Providers like Linode, a cloud provider established in 2003, are well-suited for this due to their simplicity and predictable pricing, contrasting with larger cloud providers <a class="yt-timestamp" data-t="01:34:04">[01:34:04]</a>. A Linux server can be quickly set up with a few clicks <a class="yt-timestamp" data-t="01:46:79">[01:46:79]</a>.

The Pocketbase executable can be uploaded to the cloud server and run, making the backend accessible globally, similar to platforms like [[deploying_and_hosting_applications_with_firebase | Firebase]] <a class="yt-timestamp" data-t="02:31:69">[02:31:69]</a>.

## Scaling Strategy: Vertical Scaling

As a web application built with Pocketbase grows and needs to handle more traffic, the primary scaling method is **vertical scaling** <a class="yt-timestamp" data-t="13:05:37">[13:05:37]</a>. This involves increasing the server's CPU and RAM <a class="yt-timestamp" data-t="13:08:92">[13:08:92]</a>. On cloud platforms like Linode, this is easily achieved by resizing the existing server to a larger machine <a class="yt-timestamp" data-t="13:12:96">[13:12:96]</a>.

A single, adequately sized server running Pocketbase can handle tens of thousands of concurrent users, which is sufficient for the vast majority of projects <a class="yt-timestamp" data-t="13:17:15">[13:17:15]</a>. This approach aims to minimize wasted time and money, allowing developers to experiment and fail without significant collateral damage <a class="yt-timestamp" data-t="13:25:01">[13:25:01]</a>.

## Production Readiness Considerations

For a production-ready Pocketbase deployment on the cloud, several additional steps are recommended:

*   **Domain and SSL:** Bringing a custom domain to the cloud provider's DNS manager. Pocketbase utilizes Let's Encrypt to automatically generate an SSL certificate, enabling HTTPS service by adding an extra flag to the serve command <a class="yt-timestamp" data-t="03:33:91">[03:33:91]</a>.
*   **Data Persistence:** Mounting a volume to the `PB_data` directory, where Pocketbase stores all data. A volume acts as its own file system and can be moved between different servers, ensuring data portability and safety <a class="yt-timestamp" data-t="03:48:86">[03:48:86]</a>.
*   **Automatic Restart:** Setting up a systemd service to automatically restart Pocketbase whenever the server reboots, ensuring continuous availability <a class="yt-timestamp" data-t="04:04:12">[04:04:12]</a>.

These considerations contribute to robust deployment and [[cloud_computing_scalability_and_cost_management | cost management]] when scaling applications.