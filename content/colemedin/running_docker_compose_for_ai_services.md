---
title: Running Docker Compose for AI services
videoId: 259KgP3GbdE
---

From: [[colemedin]] <br/> 

Deploying AI applications to the cloud is essential for making them accessible to other users in a secure way, moving beyond local development environments <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This guide covers how to [[deploying_local_ai_package_to_cloud_instances | deploy local AI packages to cloud instances]], specifically using the local AI starter kit by n8n as an example <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. The principles discussed apply to almost any application running on localhost with a port, such as Streamlit, Next.js, or any [[deploying_and_scaling_ai_agents_with_docker | Docker container]] with a URL <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Local AI Starter Kit Overview

The local AI starter kit by n8n packages together several key components for AI applications <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>:
*   **Olama**: For Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Qdrant**: For a vector database, used in Retrieval-Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **Postgres**: For a SQL database, used for chat memory <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **n8n**: For workflow automations <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

These services run on your local host (e.g., n8n on `localhost:5678`) when set up locally <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. The goal of deployment is to make them accessible via a custom URL (e.g., `n8n.yourdomain.com`) <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

## Choosing a Cloud Provider

For this deployment, Digital Ocean is used as the cloud provider due to its ease of use for most scenarios <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Digital Ocean**: Recommended for general AI applications, Streamlit, or Next.js apps that don't require significant GPU power <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Runpod**: Recommended for powerful machines with high VRAM, necessary for running very large language models (e.g., 3.2 90B) <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

This tutorial aims to be cloud provider agnostic, as long as you have an Ubuntu Linux machine in the cloud <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

## Setting Up the Cloud Instance

1.  **Create a Droplet (Digital Ocean)**:
    *   Sign into Digital Ocean and click "Create" > "Droplet" <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
    *   Select "Docker for Ubuntu" from the marketplace image options <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
    *   Choose a droplet size (e.g., the largest basic plan for good CPU) <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
    *   Set a password and optionally change the hostname <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
    *   Click "Create droplet" and wait for it to be ready (approx. 30 seconds to a minute) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
2.  **Access the Console**: Once ready, click the three dots, "Access console", then "Launch droplet console" to connect to your machine <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

## Preparing the Local AI Starter Kit

1.  **Clone the Git Repository**:
    ```bash
    git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git
    cd self-hosted-ai-starter-kit
    ```
    This clones the local AI starter kit <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
2.  **Edit the `.env` File**:
    *   Open the `.env` file using `nano .env` <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
    *   Configure PostgreSQL username and password (used for n8n credentials) <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
    *   Set n8n security secrets (encryption keys – can be any string) <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
    *   Save and exit: `Ctrl+X`, then `Y`, then `Enter` <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
3.  **Edit the `docker-compose.yml` File**:
    *   Open the `docker-compose.yml` file <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
    *   Add a command to the Olama container to pull desired models at startup (e.g., `nomic-embed-text` for RAG embeddings) <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
    *   Save and exit: `Ctrl+X`, then `Y`, then `Enter` <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## Network and Reverse Proxy Configuration

1.  **Firewall Setup (UFW)**:
    *   Enable UFW (if not already enabled by your cloud provider):
        ```bash
        sudo ufw enable
        ```
        <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>
    *   Open ports 80 (HTTP) and 443 (HTTPS):
        ```bash
        sudo ufw allow 80/tcp
        sudo ufw allow 443/tcp
        ```
        <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>
    *   Reload UFW to apply rules:
        ```bash
        sudo ufw reload
        ```
        <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>
2.  **Install Nginx**:
    *   Install Nginx, which acts as a reverse proxy to route external URL requests to local ports:
        ```bash
        sudo apt install nginx
        ```
        <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>
3.  **Configure Nginx for n8n**:
    *   Create and open a new Nginx configuration file for your application:
        ```bash
        sudo nano /etc/nginx/sites-available/n8n
        ```
        <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>
    *   Paste the following configuration, replacing `n8n.yourdomain.com` with your actual domain. Ensure consistent spacing (e.g., 2 spaces per indent level, then 4 spaces for deeper indents) <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>:
        ```nginx
        server {
            listen 80;
            listen [::]:80;
            server_name n8n.yourdomain.com; # Replace with your domain

            location / {
                proxy_pass http://localhost:5678; # n8n's default port
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
            }
        }
        ```
        *   This config listens on port 80 (HTTP) for `n8n.yourdomain.com` and redirects requests to `localhost:5678` where n8n is running <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. This is the core of how to [[deploying_local_ai_package_to_cloud_instances | deploy local AI packages to cloud instances]] by making any localhost app accessible via a URL <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
    *   Save and exit: `Ctrl+X`, then `Y`, then `Enter` <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
4.  **Enable the Nginx Site**:
    *   Create a symbolic link from `sites-available` to `sites-enabled`:
        ```bash
        sudo ln -s /etc/nginx/sites-available/n8n /etc/nginx/sites-enabled/n8n
        ```
        <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>
5.  **Test Nginx Configuration**:
    *   Verify the configuration syntax:
        ```bash
        sudo nginx -t
        ```
        <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>
6.  **Reload Nginx**:
    *   Apply the new configuration:
        ```bash
        sudo systemctl reload nginx
        ```
        <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>

## DNS and SSL Setup (HTTPS)

1.  **Add DNS A Record**:
    *   Copy your Digital Ocean droplet's IPv4 address <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
    *   Go to your DNS provider's settings (e.g., Namecheap, Bluehost, Squarespace) <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.
    *   Add a new `A` record:
        *   **Host**: `n8n` (or your chosen subdomain) <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>
        *   **Value/IP Address**: Paste your droplet's IPv4 address <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>
2.  **Install Certbot**:
    *   Install Certbot, used to obtain and manage SSL certificates for HTTPS:
        ```bash
        sudo apt install certbot python3-certbot-nginx
        ```
        <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>
3.  **Get SSL Certificate**:
    *   Run Certbot for your domain, replacing `n8n.yourdomain.com` with your actual domain:
        ```bash
        sudo certbot --nginx -d n8n.yourdomain.com
        ```
        <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>
    *   Follow the prompts (enter email, agree to terms, choose to redirect HTTP to HTTPS if prompted) <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
    *   A "Successfully deployed certificate" message confirms success <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.

## Running the Docker Compose Services

1.  **Navigate to the Project Directory**:
    ```bash
    cd self-hosted-ai-starter-kit
    ```
    <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>
2.  **Run Docker Compose**:
    *   Start the services in detached mode (`-d`) so the terminal doesn't hang:
        ```bash
        docker compose up -d
        ```
        <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>
        *   This command initiates [[setting_up_a_docker_compose_for_local_ai_services | setting up a Docker Compose for local AI services]] by pulling images and starting containers.
    *   It will take time for the images to pull the first time <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.
    *   A successful output will show containers running <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.
    *   You can view logs with `docker compose logs` or manage containers with `docker compose down` or `docker compose stop` <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
3.  **Access n8n**:
    *   Open your browser and navigate to your configured URL (e.g., `n8n.yourdomain.com`) <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.
    *   You should now have access to your n8n instance <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.

## Configuring Connections within n8n

Once n8n is running in the cloud, you need to configure its internal connections to Olama, Postgres, and Qdrant. Since all services are within the same Docker Compose network, they can reference each other by their service names from the `docker-compose.yml` file <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.

1.  **Olama Connection**:
    *   In n8n, create new Olama credentials <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.
    *   **Base URL**: `olama` (service name)
    *   **Port**: `11434` <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>
2.  **Postgres Connection**:
    *   In n8n, create new Postgres credentials <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
    *   **Host**: `postgres` (service name) <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>
    *   **Database**: `n8n` <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>
    *   **User/Password**: Use the values set in the `.env` file <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>.
3.  **Qdrant Connection**:
    *   In n8n, select or create Qdrant credentials <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.
    *   **API Key**: Can be anything (not critical for local setup) <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>.
    *   **URL**: `http://qdrant` (service name)
    *   **Port**: `6333` <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>

Once configured, test the connections, for example, by sending a simple chat message to Olama via n8n to ensure it's responding <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. This completes the [[deploying_and_monitoring_ai_agents | deployment and monitoring]] of your AI application, allowing it to run securely and accessibly in the cloud <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.