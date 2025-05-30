---
title: Deploying AI applications to the cloud
videoId: 259KgP3GbdE
---

From: [[colemedin]] <br/> 

Building AI applications locally is enjoyable, but for real-world use with multiple users, they need to be accessible on the internet securely, which requires [[deploying_local_ai_package_to_cloud_instances | deploying them to the cloud]] <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>. This guide simplifies the often tricky process of deployment, covering custom URLs, HTTPS setup, and connecting services within the cloud environment <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>. The principles discussed apply to deploying virtually anything that runs on localhost with a port, including Streamlit applications, Ollama, Next.js apps, or Docker containers <a class="yt-timestamp" data-t="01:17:18">[01:17:18]</a>.

## Example Deployment: n8n Local AI Starter Kit

The n8n Local AI Starter Kit is used as the primary example for this deployment guide because it is a popular solution <a class="yt-timestamp" data-t="01:10:49">[01:10:49]</a>. This kit packages together several components:
*   **Ollama:** For Large Language Models (LLMs) <a class="yt-timestamp" data-t="02:00:22">[02:00:22]</a>.
*   **Qdrant:** A vector database for Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>.
*   **PostgreSQL:** An SQL database for purposes like chat memory <a class="yt-timestamp" data-t="02:06:01">[02:06:01]</a>.
*   **n8n:** For workflow automations <a class="yt-timestamp" data-t="02:09:07">[02:09:07]</a>.

Locally, these services run on your machine (e.g., n8n on `localhost:5678`) <a class="yt-timestamp" data-t="02:22:15">[02:22:15]</a>. The goal of cloud deployment is to make them accessible via a custom URL (e.g., `n8n.yourdomain.com`) that redirects to the n8n instance running on the cloud machine <a class="yt-timestamp" data-t="02:37:34">[02:37:34]</a>.

## [[choosing_cloud_providers_for_local_ai_deployment | Choosing a Cloud Provider]]

For most use cases, DigitalOcean is a preferred cloud provider due to its ease of use <a class="yt-timestamp" data-t="02:53:13">[02:53:13]</a>. However, for more powerful machines needed to run very large language models (e.g., 3.2 90B models), services like RunPod are recommended as they offer more robust GPU options <a class="yt-timestamp" data-t="03:07:37">[03:07:37]</a>. For smaller models or applications like Streamlit or Next.js apps, DigitalOcean provides suitable offerings <a class="yt-timestamp" data-t="03:25:01">[03:25:01]</a>.

### Setting Up a DigitalOcean Droplet

1.  **Create Droplet:** After signing into DigitalOcean, click "Create" and select "Droplet" <a class="yt-timestamp" data-t="03:41:04">[03:41:04]</a>.
2.  **Image Selection:** Go to the marketplace and choose "Docker for Ubuntu" <a class="yt-timestamp" data-t="04:05:01">[04:05:01]</a>. The steps will be similar for any Ubuntu Linux machine in the cloud, regardless of the provider <a class="yt-timestamp" data-t="04:27:08">[04:27:08]</a>.
3.  **Droplet Size:** Select a basic plan with good CPU (e.g., the largest basic plan available) <a class="yt-timestamp" data-t="04:47:04">[04:47:04]</a>.
4.  **Hostname:** Optionally change the hostname (e.g., "YouTube AI app deploy") <a class="yt-timestamp" data-t="05:04:40">[05:04:40]</a>.
5.  **Create:** Click "Create droplet" and wait for it to be ready (typically 30 seconds to a minute) <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>.
6.  **Access Console:** Once ready, click the three dots on your droplet, select "Access Console," and then "Launch Droplet Console" to connect to your machine <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>.

## Initial Setup and Configuration

All steps are performed from scratch on the newly created machine <a class="yt-timestamp" data-t="05:43:03">[05:43:03]</a>.

1.  **Clone Git Repository:**
    ```bash
    git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git
    ```
    This clones the local AI starter kit <a class="yt-timestamp" data-t="05:58:00">[05:58:00]</a>.
2.  **Change Directory:**
    ```bash
    cd self-hosted-ai-starter-kit
    ```
    Navigate into the new folder <a class="yt-timestamp" data-t="06:07:04">[06:07:04]</a>.
3.  **Edit `.env` File:**
    ```bash
    nano .env
    ```
    Set up PostgreSQL username and password, and n8n security secrets. These secrets should be unique and not shared <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>. Save and exit (`Ctrl+X`, `Y`, `Enter`) <a class="yt-timestamp" data-t="07:02:40">[07:02:40]</a>.
4.  **Edit `docker-compose.yml` File:**
    ```bash
    nano docker-compose.yml
    ```
    Add a command to the Ollama container to pull desired models at runtime, for example, the embedding model `nomic-embed-text`, which is necessary for RAG embeddings <a class="yt-timestamp" data-t="07:18:00">[07:18:00]</a>.
    ```yaml
    # ... (inside olama service)
    command: >
      /bin/sh -c "olama serve &
      olama pull nomic-embed-text &
      wait -n"
    # ...
    ```
    Save and exit (`Ctrl+X`, `Y`, `Enter`) <a class="yt-timestamp" data-t="07:58:00">[07:58:00]</a>.

## Firewall Configuration

Before running containers, configure the firewall.

1.  **Enable UFW:**
    ```bash
    sudo ufw enable
    ```
    This command might not be strictly necessary for DigitalOcean Docker droplets, but it's crucial for many other cloud providers <a class="yt-timestamp" data-t="08:17:00">[08:17:00]</a>.
2.  **Open Ports:**
    ```bash
    sudo ufw allow 80
    sudo ufw allow 443
    ```
    Ports 80 (HTTP) and 443 (HTTPS) must be open for SSL certificate setup later <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>.
3.  **Reload UFW:**
    ```bash
    sudo ufw reload
    ```
    Apply the new firewall rules <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>.

## Setting Up Nginx (Reverse Proxy)

Nginx acts as a reverse proxy, routing user requests from a custom URL to the n8n application running on a specific local port <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>.

1.  **Install Nginx:**
    ```bash
    sudo apt install nginx
    ```
    Confirm with `Y` to continue the operation <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>.
2.  **Create Nginx Configuration File:**
    ```bash
    sudo nano /etc/nginx/sites-available/n8n
    ```
    Paste the following configuration. Be very careful with tabs and spaces; use two spaces for the first level of indentation and four spaces for deeper levels <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>.
    ```nginx
    server {
        listen 80;
        listen [::]:80;

        server_name n8n.dynamis.ai; # Replace with your domain

        location / {
            proxy_pass http://localhost:5678; # n8n's default port
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
    ```
    This configuration tells Nginx to listen on port 80 for requests to `n8n.yourdomain.com` and redirect them to `localhost:5678`, where n8n is running <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>. For other applications (e.g., Next.js on port 3000, Streamlit on port 5601), you would adjust `proxy_pass` accordingly <a class="yt-timestamp" data-t="11:29:00">[11:29:00]</a>. Save and exit (`Ctrl+X`, `Y`, `Enter`) <a class="yt-timestamp" data-t="11:56:00">[11:56:00]</a>.
3.  **Enable Application with Symbolic Link:**
    ```bash
    sudo ln -s /etc/nginx/sites-available/n8n /etc/nginx/sites-enabled/n8n
    ```
    This creates a symbolic link, enabling the Nginx configuration <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>.
4.  **Test Nginx Configuration:**
    ```bash
    sudo nginx -t
    ```
    This command verifies the Nginx configuration syntax. It should report "syntax is okay" and "test is successful" <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>.
5.  **Reload Nginx:**
    ```bash
    sudo systemctl reload nginx
    ```
    Reload Nginx to apply the new configuration <a class="yt-timestamp" data-t="12:43:00">[12:43:00]</a>.

## DNS Settings for SSL Certificate

To set up HTTPS for a secure site, you need to configure your DNS records.

1.  **Copy Droplet IPv4:** Get the public IPv4 address from your DigitalOcean droplet settings <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.
2.  **Add A Record in DNS Provider:** Go to your domain's DNS settings (e.g., Namecheap, Bluehost, Squarespace). Add a new "A record":
    *   **Host:** `n8n` (or your chosen subdomain) <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>.
    *   **IP Address:** Paste the droplet's IPv4 address <a class="yt-timestamp" data-t="13:46:00">[13:46:00]</a>.

## Setting Up SSL (Certbot)

Certbot is used to obtain and manage SSL certificates, enabling HTTPS.

1.  **Install Certbot:**
    ```bash
    sudo apt install certbot python3-certbot-nginx
    ```
    This installs Certbot and its Nginx plugin <a class="yt-timestamp" data-t="14:07:00">[14:07:00]</a>.
2.  **Run Certbot for Your Domain:**
    ```bash
    sudo certbot --nginx -d n8n.dynamis.ai # Replace with your domain
    ```
    Certbot will guide you through the process, asking for your email and agreement to terms <a class="yt-timestamp" data-t="14:26:00">[14:26:00]</a>. A successful deployment will show "Successfully deployed certificate" <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>.

## Running Docker Containers

Now that the environment is set up, you can start the AI application containers.

1.  **Change Directory:**
    ```bash
    cd self-hosted-ai-starter-kit
    ```
    Ensure you are in the directory where `docker-compose.yml` is located <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>.
2.  **Run Docker Compose:**
    ```bash
    docker-compose up -d --build
    ```
    *   `up`: Starts the services defined in `docker-compose.yml`.
    *   `-d`: Runs the containers in detached mode, preventing the terminal from hanging <a class="yt-timestamp" data-t="15:46:00">[15:46:00]</a>.
    *   `--build`: Rebuilds images if changes were made to the Dockerfile or context.
    This command will pull all necessary Docker images (which may take some time initially) and start the containers <a class="yt-timestamp" data-t="15:58:00">[15:58:00]</a>.
    Successful startup will show containers running, with setup-specific containers showing "exited" in green <a class="yt-timestamp" data-t="16:06:00">[16:06:00]</a>.
3.  **View Logs (Optional):**
    ```bash
    docker-compose logs
    ```
    This command displays real-time logs from all running containers <a class="yt-timestamp" data-t="16:22:00">[16:22:00]</a>. Other `docker-compose` commands like `down` (to destroy containers) or `stop` are also available <a class="yt-timestamp" data-t="16:40:00">[16:40:00]</a>.

After these steps, your n8n instance should be accessible via your custom URL (e.g., `n8n.yourdomain.com`) <a class="yt-timestamp" data-t="16:58:00">[16:58:00]</a>.

## Configuring n8n Workflow Connections (Post-Deployment)

Once n8n is accessible, you'll need to configure its connections to the other services running within Docker Compose.

1.  **Ollama Connection:**
    *   In n8n, create new credentials for Ollama.
    *   **Base URL:** Use `ollama` (the service name in `docker-compose.yml`) <a class="yt-timestamp" data-t="18:12:00">[18:12:00]</a>.
    *   **Port:** `11434` <a class="yt-timestamp" data-t="18:29:00">[18:29:00]</a>.
    *   Save, and the connection should be successful <a class="yt-timestamp" data-t="18:33:00">[18:33:00]</a>.
2.  **PostgreSQL Connection:**
    *   Create new credentials for PostgreSQL.
    *   **Host:** `postgres` (the service name in `docker-compose.yml`) <a class="yt-timestamp" data-t="18:41:00">[18:41:00]</a>.
    *   **Database:** `n8n` <a class="yt-timestamp" data-t="18:48:00">[18:48:00]</a>.
    *   **User:** Your configured PostgreSQL username (e.g., `root`) <a class="yt-timestamp" data-t="19:01:00">[19:01:00]</a>.
    *   **Password:** Your configured PostgreSQL password (e.g., `password`) <a class="yt-timestamp" data-t="19:05:00">[19:05:00]</a>.
    *   Save, and the connection should be successful <a class="yt-timestamp" data-t="19:09:00">[19:09:00]</a>.
3.  **Qdrant Connection:**
    *   Select Qdrant credentials.
    *   **API Key:** Can be anything, as it's running locally within the Docker network <a class="yt-timestamp" data-t="19:20:00">[19:20:00]</a>.
    *   **URL:** `http://qdrant` (the service name in `docker-compose.yml`) <a class="yt-timestamp" data-t="19:26:00">[19:26:00]</a>.
    *   **Port:** `6333` <a class="yt-timestamp" data-t="19:30:00">[19:30:00]</a>.
    *   Save, and the connection should be successful <a class="yt-timestamp" data-t="19:34:00">[19:34:00]</a>.

After setting up all connections, you can test your n8n workflows. For example, sending a simple "Hi" message to an LLM (like Llama 3.1 8B) should yield a response, confirming that Ollama and PostgreSQL connections are working <a class="yt-timestamp" data-t="20:00:00">[20:00:00]</a>.

!> While the URL bar might occasionally show "dangerous" due to extensive SSL certificate testing, a typical deployment should result in a valid SSL certificate immediately <a class="yt-timestamp" data-t="20:12:00">[20:12:00]</a>.

This process provides the foundation for [[deploying_ai_applications_without_coding | deploying and monitoring AI agents]] or any local application to the cloud, allowing you to take your AI projects to production <a class="yt-timestamp" data-t="20:50:00">[20:50:00]</a>.