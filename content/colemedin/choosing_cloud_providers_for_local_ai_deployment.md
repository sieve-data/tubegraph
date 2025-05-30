---
title: Choosing cloud providers for local AI deployment
videoId: hKrl5Gr7hM0
---

From: [[colemedin]] <br/> 

This article outlines the process of [[deploying_local_ai_package_to_cloud_instances | deploying the local AI package]] to private cloud instances, enabling users to have a robust [[tech_stack_for_local_ai_applications | local AI dream]] without being restricted to a single machine <a class="yt-timestamp" data-t="01:09:09">[01:09:09]</a>. The guide aims to be straightforward and applicable to any Linux machine in the cloud <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.

## Why Deploy Local AI to the Cloud?

Even with a local AI setup, there are several reasons why users might opt to [[deploying_ai_applications_to_the_cloud | deploy it to the cloud]]:
*   **Team Access** For internal teams or multiple users to access your [[local_ai_versus_cloud_ai_benefits | local AI setup]] <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>.
*   **24/7 Operation** To ensure the stack is running continuously without hogging local machine resources <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>.
*   **Hardware Access** To gain access to more powerful hardware (e.g., GPUs) not available locally <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>.

[[deploying_ai_applications_to_the_cloud | Deploying the local AI stack to the cloud]] addresses these issues and is still considered "local" as long as the user manages the cloud instance <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>.

## Cloud Provider Considerations

When [[deploying_ai_applications_to_the_cloud | deploying your local AI setup]] to the cloud, key considerations include hardware requirements (CPU vs. GPU) and budget <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. The process for [[deploying_ai_applications_to_the_cloud | deploying the local AI package]] is largely the same across various Linux-based cloud instances <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

### CPU Instance Providers

For those not running larger local LLMs that require a dedicated GPU, CPU instances offer a more cost-effective solution <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.
*   **DigitalOcean** DigitalOcean provides good options for CPU instances, particularly if you don't need a dedicated GPU <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>. A typical CPU instance with 8GB RAM and 2 CPUs is sufficient for the entire local AI package, unless larger LLMs are intended <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>.
*   **Akamai Cloud (formerly Linode)** This is another viable option for CPU instances <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.

It's common for users to opt for a CPU instance due to lower costs and host LLMs elsewhere (e.g., using an API like OpenRouter) while keeping the rest of their stack private and local <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>.

### GPU Instance Providers

For running larger local LLMs (greater than 7 or 8 billion parameters), a dedicated GPU is necessary, which will incur higher costs <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.
*   **Specialized GPU Platforms**
    *   Lambda Labs <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>
    *   Vultr <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>
    *   Paperspace (part of DigitalOcean, but a separate platform) <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>
*   **Enterprise Cloud Providers** These offer GPU instances suitable for deploying the local AI package:
    *   AWS (Amazon Web Services) <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>
    *   Google Cloud <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>
    *   Microsoft Azure <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>

When selecting a GPU instance platform, it's crucial to research based on individual needs and budget due to the wide range of available options <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.

### Platforms to Generally Avoid (for this Specific Setup)

Some platforms are not ideal for deploying the local AI package due to specific limitations:
*   **Tensor.do** While known for affordable GPUs, Tensor.do doesn't allow users to open all the necessary ports for the local AI package <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.
*   **RunPod & Novita** These platforms are great for deploying everything as containers, but the local AI package involves running containers within containers, which is significantly more complex to set up <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>.

## Essential Configuration for Cloud Deployment

Regardless of the chosen provider, certain steps are crucial for [[setting_up_a_local_ai_cloud_stack | setting up a local AI cloud stack]]:

### Firewall Rules
It's necessary to enable firewall rules and open specific ports for the various local AI services, including:
*   Superbase <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>
*   Flowise <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>
*   Open Web UI <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>
*   n8n <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>

While it's possible to expose CRX-NG or Ollama, these services are not password protected, so it's common practice to keep their ports private for security, allowing only other services on the instance to access them via localhost <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>.

### DNS Records and Subdomains
Setting up DNS records is essential for accessing your services via custom subdomains (e.g., `n8n.yourdomain.com`) <a class="yt-timestamp" data-t="08:19:00">[08:19:00]</a>. This involves:
1.  Copying your cloud instance's IPv4 address <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>.
2.  Creating 'A' type records in your DNS provider, pointing your chosen subdomains (e.g., `yt-n8n`, `yt-superbase`, `yt-openwebui`, `yt-flowise`) to your instance's IP address <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>.
3.  Configuring the `Caddyfile` within the local AI package to match these subdomains and enable managed HTTPS/TLS, ensuring secure endpoints <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. Caddy handles secure endpoints for all services running in the cloud <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.

### Environment Variables
The `.env` file within the local AI package needs to be configured with various environment variables, including:
*   n8n security string <a class="yt-timestamp" data-t="11:03:00">[11:03:00]</a>
*   Superbase PostgreSQL password and dashboard login details <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>
*   Superbase JWT secret, anonymous key, and service role key (often with assistance from a self-host guide) <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>
*   Pool or tenant ID <a class="yt-timestamp" data-t="11:31:00">[11:31:00]</a>
*   Caddy configuration for subdomains and a Let's Encrypt email <a class="yt-timestamp" data-t="11:40:00">[11:40:00]</a>

## Deployment Process Overview

The local AI package simplifies [[incorporating_ai_models_and_databases_in_a_local_setup | the integration of various AI services]] by bundling them for easy installation and configuration <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>. Services included are n8n, Superbase, Ollama, Open Web UI, Flowise, Qdrant, and CRX-NG (with Redis for caching) <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.

After setting up the cloud instance (preferably Ubuntu with Docker pre-installed), configuring firewalls, and DNS records, the deployment involves:
1.  Cloning the local AI package repository <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>.
2.  Copying and editing the `.env.example` file to `.env` with your specific configurations <a class="yt-timestamp" data-t="10:23:00">[10:23:00]</a>.
3.  Running the main Python script (`run.py`) with the appropriate profile (e.g., `cpu-mode` for CPU instances or an Nvidia GPU profile) <a class="yt-timestamp" data-t="13:03:00">[13:03:00]</a>. This script automates pulling and running Docker containers for all components within a single Docker Compose network, allowing them to communicate <a class="yt-timestamp" data-t="14:06:00">[14:06:00]</a>.

Once the script completes, all containers should be up and running, accessible via the configured subdomains from an external browser <a class="yt-timestamp" data-t="14:31:00">[14:31:00]</a>.