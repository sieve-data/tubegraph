---
title: Using Digital Ocean for cloud deployment
videoId: 259KgP3GbdE
---

From: [[colemedin]] <br/> 

This article outlines the process of [[deploying_ai_applications_to_the_cloud | deploying AI applications to the cloud]], specifically demonstrating the deployment of a local AI starter kit to Digital Ocean, a cloud provider. The steps provided are broadly applicable for deploying almost any application running on `localhost` with a port <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Why Digital Ocean?

Digital Ocean is a preferred cloud provider for most use cases due to its ease of use and good offerings <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>, <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>, <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

However, Digital Ocean may not be the best choice for running very powerful large language models (e.g., 3.2 90B), as its GPU droplet offerings are currently limited <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>, <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. For such needs, services like RunPod are recommended for more powerful machines with abundant VRAM <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>, <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>, <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. For smaller models or applications like Streamlit or Next.js apps, Digital Ocean is a suitable choice <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>, <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

## Creating a Digital Ocean Droplet

1.  **Log In**: Sign in to your Digital Ocean account <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
2.  **Create Droplet**: Click "Create" in the top right corner and select "Droplet" <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>, <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
3.  **Region and Data Center**: Keep default settings <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
4.  **Image Selection**: Go to the marketplace and choose "Docker for Ubuntu" as the image <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>, <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This ensures Docker is pre-installed on an Ubuntu Linux machine, making the subsequent steps largely cloud provider agnostic <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>, <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
5.  **Droplet Size**: Select the largest basic plan for sufficient CPU <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
6.  **Authentication**: Set a password for the droplet <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
7.  **Hostname**: Optionally change the hostname, e.g., "YouTube AI app deploy" <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
8.  **Create**: Click "Create droplet." The process typically takes 30 seconds to a minute <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>, <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

## Connecting to the Droplet

Once the droplet is ready, you can access its console by clicking the three dots next to it, then "Access Console," and finally "Launch Droplet Console" <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>, <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This connects you directly to the machine's command line <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## Initial Application Setup on the Droplet

These steps prepare the environment for [[deploying_local_ai_package_to_cloud_instances | deploying the local AI package]] (n8n's local AI starter kit) but are adaptable for other applications.

1.  **Clone the Git Repository**:
    ```bash
    git clone https://github.com/your-repo-link.git # Replace with actual repo
    ```
    Then, change into the new directory:
    ```bash
    cd self-hosted-ai-starter-kit # Or your specific folder name
    ```
    <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>, <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>

2.  **Edit `.env` File**:
    Use `nano .env` to edit the environment variables, specifically for PostgreSQL username/password and n8n security <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>, <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. Set strong, unshared encryption keys for security <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>, <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Save and exit with `Ctrl+X`, `Y`, then `Enter` <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

3.  **Modify `docker-compose.yml`**:
    Edit the `docker-compose.yml` file, for example, to ensure Ollama pulls necessary models like `nomic-embed-text` upon container startup, which is crucial for RAG (Retrieval Augmented Generation) embeddings <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>, <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>, <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

## Firewall Configuration (UFW)

Before running containers, configure the firewall to allow necessary traffic.

1.  **Enable UFW**:
    ```bash
    sudo ufw enable
    ```
    This command might not be necessary on Digital Ocean droplets but is important for other cloud providers <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>, <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

2.  **Open Ports 80 and 443**:
    ```bash
    sudo ufw allow 80
    sudo ufw allow 443
    ```
    These ports are essential for HTTP and HTTPS, particularly for SSL certificate setup later <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>, <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

3.  **Reload UFW**:
    ```bash
    sudo ufw reload
    ```
    This applies the new firewall rules <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

## Install and Configure Nginx (Reverse Proxy)

Nginx acts as a reverse proxy, routing external URL requests to the correct internal service port (e.g., n8n on `localhost:5678`) <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>, <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>, <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

1.  **Install Nginx**:
    ```bash
    sudo apt install nginx
    ```
    Confirm the installation when prompted <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

2.  **Create Nginx Configuration File**:
    Create a new configuration file for your application (e.g., `n8n.conf`) in `/etc/nginx/sites-available/`:
    ```bash
    sudo nano /etc/nginx/sites-available/n8n.conf
    ```
    Paste the following configuration, adjusting `yourdomain.com` and the `proxy_pass` port as needed. Be mindful of indentation (preferably two spaces per tab level) <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>, <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

    ```nginx
    server {
        listen 80;
        server_name n8n.yourdomain.com; # Replace with your subdomain

        location / {
            proxy_pass http://localhost:5678; # n8n's default port
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
        }
    }
    ```
    This configuration sets up a listener on Port 80 for `n8n.yourdomain.com` and redirects traffic to `localhost:5678` where n8n is hosted <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>, <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>, <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. This pattern allows [[configuring_ai_agents_for_cloud_deployment | configuring AI agents for cloud deployment]] or any local application to be accessed via a URL <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>, <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. Save and exit.

3.  **Enable the Nginx Site**:
    Create a symbolic link from `sites-available` to `sites-enabled` to activate the configuration:
    ```bash
    sudo ln -s /etc/nginx/sites-available/n8n.conf /etc/nginx/sites-enabled/
    ```
    <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>, <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>

4.  **Test Nginx Configuration**:
    ```bash
    sudo nginx -t
    ```
    This command verifies the syntax and success of the configuration <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>. It should output "syntax is okay" and "test is successful" <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.

5.  **Reload Nginx**:
    ```bash
    sudo systemctl reload nginx
    ```
    This applies the new Nginx configuration <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>, <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

## DNS Settings

To point your custom URL to the Digital Ocean droplet, you need to configure your DNS provider.

1.  **Copy Droplet IPv4 Address**: Go to your Digital Ocean droplet settings and copy its IPv4 address <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>, <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
2.  **Add A Record in DNS Provider**: Access your DNS settings (e.g., Namecheap, Bluehost, Squarespace) <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>, <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
    *   Add a new `A` record <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
    *   Set the `Host` to your desired subdomain (e.g., `n8n`) <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
    *   Paste the droplet's IPv4 address as the `Value` or `IP Address` <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.

## SSL Certificate Setup (Certbot for HTTPS)

This step secures your site with HTTPS.

1.  **Install Certbot**:
    ```bash
    sudo apt install certbot python3-certbot-nginx
    ```
    This installs Certbot and its Nginx plugin <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

2.  **Obtain SSL Certificate**:
    ```bash
    sudo certbot --nginx -d n8n.yourdomain.com # Replace with your domain
    ```
    Follow the prompts, including entering your email and agreeing to terms and conditions <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>, <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>. A successful deployment will show messages like "Deploying certificate" and "Successfully deployed the certificate" <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.

## Running Docker Containers

With Nginx and SSL configured, you can now start your application containers. This is a key step in [[setting_up_a_local_ai_cloud_stack | setting up a local AI cloud stack]].

1.  **Navigate to Project Directory**:
    ```bash
    cd self-hosted-ai-starter-kit # Or your project directory
    ```
    <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>

2.  **Run Docker Compose**:
    ```bash
    sudo docker compose up -d
    ```
    The `-d` flag runs the containers in detached mode, preventing the terminal from hanging <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>, <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. Initial runs will involve pulling Docker images, which might take time <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. A successful startup will show containers running, with setup-specific containers showing "exited" in green <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>, <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. This command is fundamental for [[running_docker_compose_for_ai_services | running Docker Compose for AI services]].

3.  **View Logs (Optional)**:
    ```bash
    sudo docker compose logs
    ```
    This command shows real-time logs from all running containers <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>, <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

4.  **Manage Containers (Optional)**:
    Other `docker compose` commands like `down` or `stop` can be used to manage (destroy or stop) the containers <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>, <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>. This is part of [[deploying_and_scaling_ai_agents_with_docker | deploying and scaling AI agents with Docker]].

## Configuring Services within n8n (for Local AI Starter Kit)

Once n8n is accessible via its URL (e.g., `n8n.yourdomain.com`) <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>, you need to configure its internal connections.

1.  **Ollama Credentials**:
    *   In n8n, create new credentials for Ollama.
    *   Set the `Base URL` to `olama` (the service name in `docker-compose.yml`) <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>, <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.
    *   The port is `11434` <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.

2.  **PostgreSQL Credentials**:
    *   Set the `Host` to `postgres` (the service name) <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>.
    *   The `Database` name is `n8n` <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>.
    *   Enter the `User` (e.g., `root`) and `Password` (e.g., `password`) from your `.env` file <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>, <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.

3.  **Qdrant Credentials**:
    *   The `API Key` can be anything as it's running locally <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.
    *   The `URL` is `http://quadrant` <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.
    *   The port is `6333` <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.

After setting up these connections, you can test the application to ensure it functions correctly in the cloud environment <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.

## Conclusion

By following these steps, you can successfully [[setting_up_cloud_hosting_with_digital_ocean | set up cloud hosting with Digital Ocean]] and [[deploying_ai_applications_to_the_cloud | deploy AI applications to the cloud]], making them accessible on the internet securely with HTTPS <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>. This process is crucial for moving applications from a local development environment to production for other users <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>, <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.