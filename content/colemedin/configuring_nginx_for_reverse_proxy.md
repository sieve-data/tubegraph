---
title: Configuring Nginx for reverse proxy
videoId: 259KgP3GbdE
---

From: [[colemedin]] <br/> 

When deploying applications to the cloud, it's essential to make them accessible and secure for external users <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. [[setting_up_cloud_hosting_with_digital_ocean | Digital Ocean]] is often preferred for general-purpose cloud hosting due to its offerings <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a> <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. Nginx, as a reverse proxy, plays a crucial role in directing external web requests to the correct internal application running on a specific port <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

## Role of Nginx
Nginx is used to set up a reverse proxy, allowing a custom URL to route to a specific port on the hosted machine <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a> <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. This means a user can visit a friendly URL like `n8n.yourdomain.com`, and Nginx will redirect that request to the application, for example, [[how_to_use_n8n_for_web_scraping_without_code | n8n]], running on `localhost:5678` on the server <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a> <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. This configuration is versatile and can be applied to any application running on `localhost` with a port, such as a Streamlit application, Ollama, a Next.js app, or any [[selfhosting_supabase_with_docker | Docker]] container <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a> <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.

## Prerequisites: Firewall and DNS
Before [[setting_up_ssl_and_dns_for_secure_access | setting up SSL and DNS for secure access]] or running containers, it's essential to configure firewall rules <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a> <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

1.  **Enable Firewall**: Ensure the Uncomplicated Firewall (UFW) is enabled on your Ubuntu machine <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a> <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
    ```bash
    sudo ufw enable
    ```
2.  **Open Ports**: Open ports 80 (for HTTP) and 443 (for HTTPS) as these are necessary for SSL setup later <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a> <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
    ```bash
    sudo ufw allow 'Nginx Full'
    ```
3.  **Reload Firewall**: Apply the new firewall rules <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
    ```bash
    sudo ufw reload
    ```
4.  **DNS Configuration**: Set up an A record in your DNS provider (e.g., Namecheap) that points your chosen subdomain (e.g., `n8n.yourdomain.com`) to the IPv4 address of your [[setting_up_cloud_hosting_with_digital_ocean | Digital Ocean]] droplet <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a> <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a> <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

## Installing Nginx
Install Nginx on your Ubuntu droplet using the `apt` package manager <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a> <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
```bash
sudo apt install nginx
```

## Configuring Nginx as a Reverse Proxy
After installation, configure Nginx to route external requests to your application.

1.  **Create Configuration File**: Create a new Nginx configuration file for your application within the `sites-available` directory <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a> <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
    ```bash
    sudo nano /etc/nginx/sites-available/n8n.conf
    ```
2.  **Add Configuration**: Paste the following configuration, replacing `nn.dynamis.ai` with your chosen domain and subdomain:
    ```nginx
    server {
        listen 80;
        listen [::]:80;
        server_name nn.dynamis.ai;

        location / {
            proxy_pass http://localhost:5678;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
    ```
    *   `listen 80;` and `listen [::]:80;` tell Nginx to listen for HTTP requests on port 80 <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
    *   `server_name nn.dynamis.ai;` specifies the domain Nginx should respond to <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
    *   `proxy_pass http://localhost:5678;` routes requests to `localhost:5678`, where [[how_to_use_n8n_for_web_scraping_without_code | n8n]] is running <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
    *   **Important**: Pay close attention to indentation. Use spaces, preferably two spaces per level, as Nginx configurations are nitpicky with tabs and spaces <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. Incorrect spacing can lead to errors <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.
3.  **Save and Exit**: Press `Ctrl + X`, then `Y` to confirm saving, and then `Enter` <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

## Enabling and Testing Nginx Configuration

1.  **Enable Application**: Create a symbolic link from the `sites-available` configuration file to the `sites-enabled` directory to activate it <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.
    ```bash
    sudo ln -s /etc/nginx/sites-available/n8n.conf /etc/nginx/sites-enabled/n8n.conf
    ```
2.  **Test Configuration**: Verify that your Nginx configuration is syntactically correct <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
    ```bash
    sudo nginx -t
    ```
    You should see "syntax is okay" and "test is successful" <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
3.  **Reload Nginx**: Apply the changes by reloading the Nginx service <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
    ```bash
    sudo systemctl reload nginx
    ```

After these steps, Nginx is set up to reverse proxy your custom URL to your application, such as [[docker_setup_for_flowise_and_n8n | n8n]], which runs via [[setting_up_a_docker_compose_for_local_ai_services | Docker Compose]] <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. The next step would be to obtain an SSL certificate using Certbot to enable HTTPS for secure access <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.