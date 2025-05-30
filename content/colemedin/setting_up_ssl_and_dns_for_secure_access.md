---
title: Setting up SSL and DNS for secure access
videoId: 259KgP3GbdE
---

From: [[colemedin]] <br/> 

This guide details the process of deploying AI applications to the cloud, specifically focusing on setting up custom URLs, HTTPS (SSL), and connecting services securely. The method is broadly applicable to any application running on localhost with a port, including Streamlit, Next.js apps, Olama, or Docker containers <a class="yt-timestamp" data-t="01:17:17">[01:17:17]</a> <a class="yt-timestamp" data-t="01:23:44">[01:23:44]</a>.

## Why Deploy to the Cloud?

While building AI applications locally is engaging, real-world applications with multiple users require cloud deployment to be accessible over the internet securely <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.

## Cloud Provider Selection

[[using_digital_ocean_for_cloud_deployment | Digital Ocean]] is a preferred choice for most use cases due to its offerings <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. For applications requiring powerful machines with significant vRAM for large language models (e.g., 90B models), services like RunPod are recommended <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>. For smaller models or applications like Streamlit/Next.js, [[using_digital_ocean_for_cloud_deployment | Digital Ocean]] is suitable <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>.

## Droplet Setup on Digital Ocean

1.  **Create Droplet:** In [[using_digital_ocean_for_cloud_deployment | Digital Ocean]], click "Create" and select "Droplet" <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.
2.  **Region and Data Center:** Keep default settings <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>.
3.  **Image:** Go to the marketplace and select "Docker for Ubuntu" <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>. This ensures compatibility with the provided steps, which are largely cloud provider agnostic as long as a Ubuntu Linux machine is used <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.
4.  **Droplet Size:** Choose a suitable basic plan, prioritizing good CPU <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.
5.  **Hostname:** Set a descriptive hostname (e.g., `YouTube-AI-app-deploy`) <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.
6.  **Create Droplet:** Click "Create droplet." The droplet will be ready in approximately 30 seconds to a minute <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>.
7.  **Access Console:** Access the droplet console via the [[using_digital_ocean_for_cloud_deployment | Digital Ocean]] interface <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>.

## Application Configuration and Firewall

The example uses the Local AI Starter Kit by n8n, which bundles Olama (LLMs), Quadrant (vector database), Postgres (SQL database), and n8n (workflow automations) <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. All services initially run on localhost (e.g., n8n on `localhost:5678`) <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

1.  **Clone Repository:** Clone the Local AI Starter Kit Git repository:
    ```bash
    git clone <repository_url>
    ```
    Then, change directory into the cloned folder <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>.
2.  **Edit `.env` File:**
    *   Open `n8n/.env` using `nano n8n/.env` <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>.
    *   Configure PostgreSQL username and password <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>.
    *   Set n8n security secrets (encryption keys) <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>.
    *   Save and exit (`Ctrl+X`, `Y`, `Enter`) <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>.
3.  **Edit `docker-compose.yml` File:**
    *   Open `docker-compose.yml` <a class="yt-timestamp" data-t="07:18:00">[07:18:00]</a>.
    *   Add a command to the Olama container to pull desired models at startup (e.g., `nomic-embed-text` for embeddings) to avoid runtime pulling <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>.
    *   Save and exit <a class="yt-timestamp" data-t="07:58:00">[07:58:00]</a>.

## Firewall Setup

[[configuring_dns_and_firewall_for_local_ai_services | Firewall]] settings ensure secure access.

1.  **Enable UFW:**
    ```bash
    sudo ufw enable
    ```
    (This step may not be strictly necessary for [[using_digital_ocean_for_cloud_deployment | Digital Ocean]] Docker droplets but is good practice for other providers) <a class="yt-timestamp" data-t="08:19:00">[08:19:00]</a>.
2.  **Open Ports:** Allow incoming traffic on ports 80 (HTTP) and 443 (HTTPS), which are essential for SSL setup <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>.
    ```bash
    sudo ufw allow 80/tcp
    sudo ufw allow 443/tcp
    ```
3.  **Reload UFW:** Apply the new firewall rules <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>.
    ```bash
    sudo ufw reload
    ```

## [[configuring_nginx_for_reverse_proxy | Nginx Configuration]]

Nginx acts as a reverse proxy, routing external URLs to internal localhost ports <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>.

1.  **Install Nginx:**
    ```bash
    sudo apt install nginx
    ```
2.  **Create Nginx Configuration File:** Create a new Nginx configuration file for your application (e.g., `n8n.conf`) <a class="yt-timestamp" data-t="10:15:00">[10:15:00]</a>.
    ```bash
    sudo nano /etc/nginx/sites-available/n8n.conf
    ```
    Paste the configuration, ensuring proper indentation (2 spaces per tab, 4 for deeper indents) <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>. The `server_name` should be your domain, and the `proxy_pass` should point to the internal `localhost:port` of your application (e.g., `localhost:5678` for n8n) <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>.
    ```nginx
    server {
        listen 80;
        server_name nn.dynamis.ai; # Replace with your domain

        location / {
            proxy_pass http://localhost:5678; # Replace with your app's localhost:port
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
    ```
    Save and exit <a class="yt-timestamp" data-t="11:56:00">[11:56:00]</a>.
3.  **Enable Site:** Create a symbolic link to enable the Nginx configuration <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>.
    ```bash
    sudo ln -s /etc/nginx/sites-available/n8n.conf /etc/nginx/sites-enabled/
    ```
4.  **Test Nginx Configuration:**
    ```bash
    sudo nginx -t
    ```
    Confirm that "syntax is okay" and "test is successful" <a class="yt-timestamp" data-t="12:28:00">[12:28:00]</a>.
5.  **Reload Nginx:**
    ```bash
    sudo systemctl reload nginx
    ```

## DNS Settings

[[configuring_dns_and_firewall_for_local_ai_services | DNS settings]] are crucial for pointing your domain to the cloud server and are a prerequisite for obtaining an SSL certificate <a class="yt-timestamp" data-t="12:56:00">[12:56:00]</a>.

1.  **Copy Droplet IPv4:** In your [[using_digital_ocean_for_cloud_deployment | Digital Ocean]] droplet settings, copy the IPv4 address <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.
2.  **Add A Record:** Go to your DNS provider (e.g., Namecheap, Bluehost, Squarespace) and navigate to your DNS settings (Advanced DNS, DNS Records, etc.) <a class="yt-timestamp" data-t="13:16:00">[13:16:00]</a>.
    *   Add a new `A` record.
    *   **Host:** Set this to your desired subdomain (e.g., `n8n`) <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>.
    *   **IP Address:** Paste the IPv4 address copied from your [[using_digital_ocean_for_cloud_deployment | Digital Ocean]] droplet <a class="yt-timestamp" data-t="13:46:00">[13:46:00]</a>.

## SSL Certificate with Certbot

Certbot is used to install an SSL certificate, enabling HTTPS for secure access <a class="yt-timestamp" data-t="14:07:00">[14:07:00]</a>.

1.  **Install Certbot:**
    ```bash
    sudo apt install certbot python3-certbot-nginx
    ```
2.  **Run Certbot:** Request and deploy the SSL certificate for your domain <a class="yt-timestamp" data-t="14:25:00">[14:25:00]</a>.
    ```bash
    sudo certbot --nginx -d nn.dynamis.ai # Replace with your domain
    ```
    Follow the prompts (e.g., enter email, agree to terms). A successful message will indicate the certificate has been deployed <a class="yt-timestamp" data-t="14:41:00">[14:41:00]</a>.

## Running Containers

1.  **Navigate to Project Directory:** Change back to your project directory (e.g., `self-hosted-AI-starter-kit`) <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>.
2.  **Run Docker Compose:** Start the application containers in detached mode (`-d`) <a class="yt-timestamp" data-t="15:28:00">[15:28:00]</a>.
    ```bash
    docker compose up -d
    ```
    This will pull and run all necessary Docker images. Success is indicated by containers running or exiting with a green status for setup-only containers <a class="yt-timestamp" data-t="16:06:00">[16:06:00]</a>.
3.  **Monitor Logs (Optional):**
    ```bash
    docker compose logs -f
    ```
    This command displays real-time logs from all containers <a class="yt-timestamp" data-t="16:22:00">[16:22:00]</a>.
4.  **Manage Containers (Optional):** Other Docker Compose commands like `docker compose down` or `docker compose stop` can be used to manage the containers <a class="yt-timestamp" data-t="16:40:00">[16:40:00]</a>.

## Post-Deployment Application Setup (n8n Example)

Once the application is running, access it via your configured URL (e.g., `https://n8n.dynamis.ai`) <a class="yt-timestamp" data-t="16:58:00">[16:58:00]</a>.

1.  **Create Account:** For n8n, set up your initial account <a class="yt-timestamp" data-t="17:11:00">[17:11:00]</a>.
2.  **Import Workflow (Optional):** Import any desired workflows <a class="yt-timestamp" data-t="17:26:00">[17:26:00]</a>.
3.  **Configure Credentials:** Within n8n, configure connections to other services using their Docker Compose service names (e.g., `olama`, `postgres`, `quadrant`) and their respective ports <a class="yt-timestamp" data-t="18:12:00">[18:12:00]</a>.
    *   **Olama:** Host: `olama`, Port: `11434` <a class="yt-timestamp" data-t="18:20:00">[18:20:00]</a>.
    *   **Postgres:** Host: `postgres`, Database: `n8n`, User/Password: (as configured in `.env`) <a class="yt-timestamp" data-t="18:40:00">[18:40:00]</a>.
    *   **Quadrant:** Host: `quadrant`, Port: `6333` <a class="yt-timestamp" data-t="19:26:00">[19:26:00]</a>.
4.  **Test Connections:** Verify that all connections are successful <a class="yt-timestamp" data-t="19:35:00">[19:35:00]</a>.

This comprehensive process enables secure cloud deployment for various local AI services, making them accessible and functional in a production environment <a class="yt-timestamp" data-t="20:50:00">[20:50:00]</a>.