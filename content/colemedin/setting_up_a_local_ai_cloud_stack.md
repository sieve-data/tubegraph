---
title: Setting up a local AI cloud stack
videoId: hKrl5Gr7hM0
---

From: [[colemedin]] <br/> 

The local AI package is described as the easiest way to get an entire local AI stack up and running for free, including LLMs, databases, automation tools, local web search, and a user interface <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This package allows users to [[deploying_local_ai_package_to_cloud_instances | spin up local AI environments]] in the cloud on demand <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Why Deploy Local AI to the Cloud?

Even with local AI, running it on your personal computer isn't always ideal <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Reasons to [[deploying_ai_applications_to_the_cloud | deploy AI applications to the cloud]] include:
*   **Team Collaboration** Allowing internal teams to use your local AI setup <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **24/7 Availability** Running the stack continuously without hogging local machine resources <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   **Hardware Access** Utilizing hardware (e.g., dedicated GPUs) not available on your local machine <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

[[deploying_local_ai_package_to_cloud_instances | Deploying the local AI stack to the cloud]] addresses these issues and is still considered "local" as long as you manage the cloud instance <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Local AI Package Components

The local AI package bundles various local AI services, making installation and configuration straightforward <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. Originally created by the n8n team, it has been extended to include:
*   **n8n** <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>
*   **Superbase** <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>
*   **Ollama** <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>
*   **Open Web UI** <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>
*   **Flowise** <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>
*   **Quadrant** <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>
*   **CRX-NG** (for local and private web search, including Redis for caching) <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>
*   **Caddy** (for managed HTTPS and TLS, enabling secure endpoints for services like `n8n.yourdomain.com`) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>

## [[choosing_cloud_providers_for_local_ai_deployment | Choosing Cloud Providers]] and Hardware

The deployment steps are designed to work with almost any Linux machine in the cloud, including DigitalOcean, Lambda Labs, AWS, your own server, or a data center <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Recommended Providers
*   **DigitalOcean**: Recommended for CPU instances due to good options <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. Also offers GPU droplets <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Akamai Cloud** (formerly Linode): Another good option for CPU instances <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **GPU Instance Platforms**: Lambda Labs, Vultr, PaperSpace (part of DigitalOcean), AWS, Google Cloud, Microsoft Azure <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. These can all be used to [[deploying_local_ai_package_to_cloud_instances | deploy the local AI package]] in the same way as DigitalOcean <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### Providers Not Recommended (for this package)
*   **TensorDock**: Great for cheap GPUs, but does not allow opening all necessary ports for the local AI package <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **RunPod and Novita**: Good platforms, but they deploy everything as containers, making it difficult to run containers within containers, which is needed for the local AI package <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### Hardware Considerations
*   **CPU Instances**: Sufficient for the entire local AI package, but not for larger local LLMs <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. An 8GB RAM, 2 CPU instance is enough for the package without dedicated GPU <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. Many opt for CPU instances to save costs and host Ollama elsewhere or use an API like OpenRouter, keeping the rest of their stack private <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
*   **GPU Instances**: Required for LLMs larger than 7 or 8 billion parameters (e.g., 14, 32, or 70 billion parameters), which will incur higher costs <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

## Setting Up the Cloud Instance (DigitalOcean Example)

1.  **Create a Droplet**: Choose a region and an instance type. For a CPU instance, 8GB RAM and 2 CPUs are typically sufficient <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
2.  **Select Image**: Choose an Ubuntu image with Docker already set up from the marketplace <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
3.  **Authentication**: Set up a password for root access <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
4.  **Hostname**: Assign a descriptive hostname <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
5.  **Launch Console**: Once the instance is ready, launch the droplet console with root access for privileged commands <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

## Pre-Deployment Configuration

### Firewall Setup
You need to enable firewall rules and open specific ports for the various local AI services. Commands for this are provided in the package's README <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
*   Open ports for Superbase, Flowise, Open Web UI, and n8n <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
*   For CRX-NG or Ollama, expose them only if desired, as they are not password protected by default <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. Keeping them private allows internal services to access them via `localhost` without external exposure <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   After adding rules, run `ufw reload` to apply changes <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. All firewall commands require privileged access <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### DNS Records Setup
This process is similar across most DNS providers (e.g., Hostinger) <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
1.  **Copy IPv4 Address**: Obtain your cloud instance's IPv4 address from your provider <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
2.  **Create A Records**: In your DNS provider's settings, create "A" type records <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
3.  **Map Subdomains**: For each service, define a subdomain (e.g., `yt-n8n`, `yt-superbase`, `yt-openwebui`, `yt-flowise`) and point it to your instance's IPv4 address <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. This allows accessing services like `yt-n8n.yourdomain.com` securely in the cloud <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

## Deployment Steps

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/your-repo-link # (Link provided in video description)
    cd local-ai-package-directory
    ```
    <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>

2.  **Configure Environment Variables**:
    *   Copy the `.env.example` file to `.env`:
        ```bash
        cp .env.example .env
        ```
        <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>
    *   Edit the `.env` file using `nano` (or preferred editor):
        ```bash
        nano .env
        ```
        <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>
    *   **Required Variables**:
        *   **n8n**: Set a long alphanumeric string for `N8N_ENCRYPTION_KEY` <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
        *   **Superbase Secrets**: Configure PostgreSQL password, Superbase dashboard login details, JWT secret, Anonymous key, and Service Role Key (refer to Superbase self-host guide for details) <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. Set a `POOL_ID` or `TENANT_ID` (e.g., 1000) <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
        *   **Caddy Configuration**: Uncomment and set hostnames for all subdomains configured in your DNS provider (e.g., `N8N_HOSTNAME=yt-n8n.automator.ai`). Set `LETS_ENCRYPT_EMAIL` to your email <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
    *   Save and exit (Ctrl + X, then Y, then Enter in Nano) <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

3.  **Run the Deployment Script**:
    *   The script uses Docker Compose to spin up all services in a single network, allowing containers to communicate <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
    *   **For Nvidia GPU instances**:
        ```bash
        python3 start_local_ai_stack.py --profile nvidia
        ```
        <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>
    *   **For CPU instances (to run Ollama on CPU)**:
        ```bash
        python3 start_local_ai_stack.py --profile cpu
        ```
        <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>
    *   This process involves pulling Superbase and other containers, setting up CRX-NG, pulling Ollama models, and importing n8n workflows <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.

## Verification and Management

### Checking Container Status
*   **List running containers**:
    ```bash
    docker ps
    ```
    <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>
    Ensure all containers are "Up" <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
*   **View container logs**:
    ```bash
    docker logs -f <container_name>
    ```
    <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>
    The `-f` flag allows following logs as they come in <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

### Browser Testing
Access the deployed services via their configured subdomains:
*   `yt-n8n.automator.ai` (should show n8n sign-up page) <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>
*   `yt-superbase.automator.ai` (should show Superbase dashboard login) <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>
*   `yt-openwebui.automator.ai` (should show Open Web UI) <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>

This confirms that the [[tech_stack_for_local_ai_applications | local AI tech stack]] is successfully hosted and accessible from an external browser <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.
For more information on creating local AI agents using this package, refer to other videos on the channel <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>. The local AI package is continually being updated with new services and improvements <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.