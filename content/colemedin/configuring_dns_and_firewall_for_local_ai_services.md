---
title: Configuring DNS and firewall for local AI services
videoId: hKrl5Gr7hM0
---

From: [[colemedin]] <br/> 

When [[deploying_local_ai_package_to_cloud_instances | deploying a local AI package]] to a private cloud instance, it is essential to configure the firewall and DNS records to ensure secure and accessible services <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. This process allows users to access their [[setting_up_a_local_ai_cloud_stack | local AI setup]] remotely and securely <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Firewall Configuration

Before [[setting_up_a_docker_compose_for_local_ai_services | spinning up the local AI package]] services, firewall rules must be enabled and specific ports opened on the Linux machine <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. This process requires privileged access <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a> <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.

Common firewall commands include:
*   Enabling firewall rules.
*   Opening ports for various local AI services:
    *   [[incorporating_ai_models_and_databases_in_a_local_setup | Superbase]] <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>
    *   Flowise <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>
    *   [[configuring_ai_agents_for_cloud_deployment | Open Web UI]] <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>
    *   n8n <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a> <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>
*   Optionally exposing CRX NG for local and private web search (which includes [[incorporating_ai_models_and_databases_in_a_local_setup | Redis]] for caching) <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a> <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a> and [[incorporating_ai_models_and_databases_in_a_local_setup | Olama]] <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a> <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. These are typically not exposed by default because they are not password protected <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   After setting up rules, run `ufw reload` to apply them <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

## DNS Record Setup

Setting up DNS (Domain Name System) records is crucial for accessing your services via custom subdomains <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. This process is generally consistent across different DNS providers <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

1.  **Retrieve IPv4 Address**: Obtain the IPv4 address of your cloud instance <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
2.  **Create A Record**: In your DNS provider's settings, create a new A record <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
    *   **Type**: Set the record type to "A" <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
    *   **Points To**: Paste your cloud instance's IPv4 address <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
    *   **Name**: Define the subdomain you wish to use (e.g., `yt-nn` for n8n) <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
3.  **Repeat for Services**: Create A records for all services you wish to expose, such as:
    *   `yt-nn.yourdomain.com` for n8n <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>
    *   `yt-superbase.yourdomain.com` for [[incorporating_ai_models_and_databases_in_a_local_setup | Superbase]] <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>
    *   `yt-openwebui.yourdomain.com` for [[configuring_ai_agents_for_cloud_deployment | Open Web UI]] <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>
    *   `yt-flowwise.yourdomain.com` for Flowise <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>
    *   This can also be done for CRX NG or [[incorporating_ai_models_and_databases_in_a_local_setup | Olama]] if desired <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

## Integrating with the Local AI Package

The [[setting_up_a_local_ai_cloud_stack | local AI package]] includes `caddy` for managed HTTPS and TLS, which enables secure endpoints for all services running in the cloud <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a> <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. This means you can access services like your n8n instance securely at `n8n.yourdomain.com` <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

After setting up DNS, the next step involves configuring environment variables in the `.env` file of the [[setting_up_a_local_ai_cloud_stack | local AI package]] <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. This includes:
*   Setting up secrets for n8n and [[incorporating_ai_models_and_databases_in_a_local_setup | Superbase]] <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
*   Crucially, uncommenting and updating the `caddy` configuration with the exact subdomains set up in your DNS provider <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a> <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.
*   Specifying an email for Let's Encrypt, which `caddy` uses for SSL certificates <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.

After these configurations, the [[setting_up_a_docker_compose_for_local_ai_services | Docker Compose]] script can be run to deploy all services, establishing secure and accessible endpoints <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.

## Prerequisites

Users should ensure that Nano, Git, and Docker are already installed on their Linux distribution in the cloud instance as these are prerequisites for the installation process <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

Successfully configuring the firewall and DNS is vital for establishing a secure and functional [[setting_up_a_local_ai_cloud_stack | local AI cloud stack]], allowing external access to all integrated services <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.