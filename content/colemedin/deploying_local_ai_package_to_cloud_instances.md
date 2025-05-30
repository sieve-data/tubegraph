---
title: Deploying local AI package to cloud instances
videoId: hKrl5Gr7hM0
---

From: [[colemedin]] <br/> 

The [[local_ai_package_setup | Local AI package]] is described as the easiest way to get an entire local AI stack running for free, including LLMs, databases, automation tools, local web search, and a user interface <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This package can be used to easily spin up local AI environments in the cloud on demand <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Why Deploy to the Cloud?

Even with local AI setups, it's not always ideal to run them on your personal computer <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Reasons for [[deploying_ai_applications_to_the_cloud | deploying your local AI stack to the cloud]] include:
*   **Team Collaboration** You might want internal teams to use your local AI setup <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **24/7 Availability** The stack can run continuously without hogging local machine resources <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   **Hardware Access** Gain access to specialized hardware (e.g., GPUs) you might not own <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

[[deploying_ai_applications_to_the_cloud | Deploying your local AI stack to the cloud]] addresses these issues while still being considered "local" as long as you manage the cloud instance <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This process is straightforward due to new additions to the [[local_ai_package_setup | Local AI package]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Local AI Package Overview

The [[local_ai_package_setup | Local AI package]] is a GitHub repository that bundles various local AI services, allowing for installation and configuration in just a few steps <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. The package was originally created by the n8n team and has been extended to include:
*   n8n <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>
*   Superbase <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>
*   Ollama <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>
*   Open Web UI <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>
*   Flowise <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>
*   Qdrant <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>
*   CRX-NG (for local and private web search, including Redis for caching) <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>
*   Caddy (for managed HTTPS and TLS, enabling secure endpoints and subdomains like `n8n.yourdomain.com`) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>

## Cloud Provider Considerations

When [[choosing_cloud_providers_for_local_ai_deployment | choosing cloud providers]] for local AI deployment, it's essential to consider hardware requirements, especially for LLMs <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

### Recommended Providers

*   **DigitalOcean**: Generally recommended for CPU instances, offering good options if you're not running larger LLMs that require a dedicated GPU <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. They also offer GPU droplets <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Akamai Cloud (formerly Linode)**: Another good option for CPU instances <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **GPU Instance Platforms**: For dedicated GPUs, research options based on your needs and budget. Providers include <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>:
    *   Lambda Labs <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>
    *   Vultr <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>
    *   Paperspace (part of DigitalOcean) <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>
    *   Enterprise-level options: AWS, Google Cloud, Microsoft Azure <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>

### Platforms to Avoid for Local AI Package Deployment

Some platforms are not ideal for [[deploying_ai_applications_to_the_cloud | deploying the local AI package]] <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>:
*   **TensorDock**: Great for cheap GPUs but doesn't allow opening all necessary ports for the [[local_ai_package_setup | Local AI package]] <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **RunPod and Novita**: These platforms deploy everything as containers, making it difficult to run containers within containers, which is necessary for the [[local_ai_package_setup | Local AI package]] <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### CPU vs. GPU Instances

*   A CPU instance (e.g., 8 GB RAM, 2 CPUs for $42/month on DigitalOcean) is sufficient for the entire [[local_ai_package_setup | Local AI package]] unless you want to run larger local LLMs <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   For LLMs larger than 7-8 billion parameters, a dedicated GPU is required, which will significantly increase costs <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   Many users opt for CPU instances and host Ollama elsewhere or use an API like OpenRouter, keeping the rest of their stack private and local <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

## Step-by-Step Cloud Deployment

This guide assumes you are using a Linux machine in the cloud (e.g., Ubuntu with Docker pre-installed) and have privileged access (root) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

### 1. Creating the Cloud Instance

1.  **Choose a Provider**: For this example, DigitalOcean is used <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
2.  **Create Droplet**: Select "Create" then "Droplets" <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
3.  **Choose Region and Plan**: Select a region and an appropriate CPU or GPU instance size based on your needs (e.g., 8 GB RAM, 2 CPUs) <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
4.  **Select Image**: Choose an Ubuntu Docker image from the marketplace <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
5.  **Authentication**: Set up an SSH key or a password for access <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
6.  **Hostname**: Assign a hostname to your droplet <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
7.  **Create**: Create the droplet and wait for it to be ready <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
8.  **Access Console**: Once created, access the droplet console with root privileges <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

### 2. Firewall Configuration

You need to enable firewall rules and open specific ports for the [[local_ai_package_setup | Local AI package]] services <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>:
*   Open ports for Superbase, Flowise, Open Web UI, and n8n <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   CRX-NG and Ollama ports are typically *not* exposed by default because they are not password protected. Keep them private so only other services on the instance can access them via `localhost` <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   After running the commands, apply the rules with `ufw reload` <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   Ensure you have privileged access to run these commands <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### 3. Setting Up DNS Records

This step is crucial for accessing your services via subdomains using Caddy <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
1.  **Copy IP Address**: Get your instance's IPv4 address from your cloud provider (e.g., DigitalOcean) <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
2.  **Add A Records**: In your DNS provider (e.g., Hostinger), create A records for each service:
    *   **Type**: A <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>
    *   **Name**: Your desired subdomain (e.g., `yt-n8n` for `yt-n8n.yourdomain.com`) <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>
    *   **Points to**: Your instance's IPv4 address <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>
3.  Repeat for all services you want to expose (e.g., n8n, Superbase, Open Web UI, Flowise) <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

### 4. Cloning the Repository

1.  **Navigate to Instance**: Access your cloud instance console.
2.  **Clone Repo**: Use `git clone [repository_url]` to clone the [[local_ai_package_setup | Local AI package]] GitHub repository <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
3.  **Change Directory**: Navigate into the cloned directory: `cd local-ai-package` <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
    *   *Prerequisite*: Ensure Git, Nano, and Docker are installed on your Linux distribution <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

### 5. Setting Up Environment Variables

1.  **Copy Example File**: Copy the `.env.example` file to `.env`: `cp .env.example .env` <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
2.  **Edit .env File**: Use `nano .env` to edit the file <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
3.  **Configure Variables**:
    *   **n8n**: Set a strong alphanumeric string for `N8N_ENCRYPTION_KEY` <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
    *   **Superbase**: Set `POSTGRES_PASSWORD`, `SUPERBASE_DB_LOGIN_DETAILS`, and follow the Superbase self-host guide to set `JWT_SECRET`, `ANON_KEY`, and `SERVICE_ROLE_KEY` <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. Set `POOL_OR_TENANT_ID` to a number like `1000` <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
    *   **Caddy**: Uncomment the `CADDY_HOSTS` variables for the services you configured DNS records for <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
    *   **Let's Encrypt**: Set `LETSENCRYPT_EMAIL` to your email address <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
    *   **Hostnames**: Change the `CADDY_HOSTS` values to match your subdomains (e.g., `yt-n8n.automator.ai`) <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
4.  **Save and Exit**: Press `Ctrl+X`, then `Y`, then `Enter` <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

### 6. Running the Deployment Script

The `start.py` script will [[deploying_and_scaling_ai_agents_with_docker | spin up everything with Docker Compose]] <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.
*   **For Nvidia GPU instances**: `python3 start.py --profile nvidia` <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>
*   **For CPU instances (running Ollama on CPU)**: `python3 start.py --profile cpu` <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>
    *   If `python` command fails, try `python3` <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.
*   The script will pull and run Superbase containers, then the rest of the containers (n8n, Open Web UI, Caddy, etc.) within a single Docker Compose network, allowing them to communicate <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. This process can take some time as containers and models are pulled <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

### 7. Verifying Deployment

After the script completes, verify that all containers are running:
*   **List Containers**: Run `docker ps` to see all running containers. Ensure they show "Up" status <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.
*   **Check Logs**: Use `docker logs -f [container_name]` (e.g., `docker logs -f caddy`) to view specific container logs. The `-f` flag allows you to follow logs as they come in <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

## Testing and Accessing Deployed Services

Once all containers are up, you can access your services via the configured subdomains:
*   **n8n**: `yt-n8n.yourdomain.com` (e.g., for the sign-up page) <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>
*   **Superbase**: `yt-superbase.yourdomain.com` (e.g., for the dashboard sign-in) <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>
*   **Open Web UI**: `yt-openwebui.yourdomain.com` <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>

This confirms that the [[setting_up_a_local_ai_cloud_stack | local AI stack is successfully hosted in the cloud]] and accessible externally <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.

This method provides the fastest way to [[deploying_and_testing_ai_agents_quickly | deploy and test AI agents quickly]] by [[deploying_ai_applications_to_the_cloud | deploying your local AI setup to the cloud]] <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>. The [[local_ai_package_setup | Local AI package]] is continuously updated with new services and improvements for [[configuring_ai_agents_for_cloud_deployment | configuring AI agents for cloud deployment]] and [[deploying_and_monitoring_ai_agents | deploying and monitoring AI agents]] <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.