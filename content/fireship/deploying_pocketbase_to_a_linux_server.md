---
title: Deploying Pocketbase to a Linux server
videoId: gUYBFDPZ5qk
---

From: [[fireship]] <br/> 

This article outlines the process of [[building_a_chat_app_with_pocketbase_and_svelte | deploying Pocketbase]] to a Linux server, turning it into a self-hosted backend solution for web applications. The "Spock stack" leverages Pocketbase and Svelte, deployed to a Linux server on Linode for just five dollars <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

Pocketbase is an open-source alternative to [[deploying_and_hosting_applications_with_firebase | Firebase]], written in Go, offering [[realtime_database_and_user_authentication_with_pocketbase | user authentication]] and a real-time SQLite database <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Its key advantage is compiling everything into a single executable, requiring only one small server for self-hosting <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Setting Up a Linux Server with Linode

The first step is to deploy Pocketbase to a Linux server in the cloud <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. Linode is a cloud provider that has been active since 2003, known for its simplicity and flat, predictable pricing <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Steps to Create a Linode Instance
1.  **Register and Access Dashboard**: Navigate to the Linode dashboard after registering <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
2.  **Create New Linode**: Click the button to create a new Linode instance <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
3.  **Choose Image**: Select your preferred Linux distribution image. Debian is used in this example, but Arch Linux is also an option <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
4.  **Select Region and Size**: Choose a data center region and the size of your virtual machine <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
5.  **Set Password**: Assign a strong root password for the server <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
6.  **Create**: Click create to provision your new Linux server <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

Once created, make a note of the server's IP address, as it will be used to access it over the internet <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

## Deploying Pocketbase

With the Linux server running, the next step is to deploy the Pocketbase application.

### Local Setup (Optional)
1.  **Download Pocketbase**: Download the Pocketbase executable for your local operating system (e.g., Linux version for Debian) <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
2.  **Unzip**: Unzip the downloaded file to obtain the single `pocketbase` executable <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
3.  **Run Locally**: You can run it locally by executing `pocketbase serve` <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### Deployment to Linode Server
1.  **Access Server via SSH**: Open your terminal and use Secure Shell (`ssh`) to access the Linode server as the root user, providing the password created earlier <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    ```bash
    ssh root@YOUR_LINODE_IP
    ```
2.  **Create Directory**: Create a new directory on the server to store the Pocketbase executable, for example, `PB` <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
    ```bash
    mkdir /PB
    ```
3.  **Upload Executable**: Use Secure Copy (`scp`) from your local machine's terminal to upload the Pocketbase executable to the newly created directory on the remote server <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
    ```bash
    scp /path/to/local/pocketbase root@YOUR_LINODE_IP:/PB/pocketbase
    ```
4.  **Run Pocketbase on Server**: Go back to the Linode server's terminal (via SSH), navigate to the `PB` directory, and run the Pocketbase serve command. To make it accessible over the internet, use the `--http` flag followed by your server's IP address and Port 80 <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
    ```bash
    cd /PB
    ./pocketbase serve --http YOUR_LINODE_IP:80
    ```
    This command self-hosts your backend, accessible via the IP address <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. It serves a REST API and an admin dashboard (accessible via `/_/` URL) <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

## Production-Ready Considerations

To make your Pocketbase deployment production-ready, consider the following:

1.  **Domain and HTTPS**:
    *   Bring your domain over to Linode and configure it with their DNS manager <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
    *   Pocketbase can use Let's Encrypt to automatically generate an SSL certificate, allowing you to serve your backend over HTTPS <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. Add the `--https` flag to the serve command <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
2.  **Data Persistence with Volumes**:
    *   Mount a volume to the `pb_data` directory, where Pocketbase stores all data <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
    *   A volume is a separate file system that can be easily moved to different servers, ensuring data portability and safety <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Linode allows attaching extra storage for a low cost <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
3.  **Automatic Restarts with Systemd**:
    *   Set up a systemd service to automatically restart Pocketbase whenever the server reboots, ensuring continuous availability <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

## [[scaling_pocketbase_applications_on_the_cloud | Scaling Pocketbase Applications on the Cloud]]

As your website grows, Pocketbase will require [[scaling_pocketbase_applications_on_the_cloud | vertical scaling]] with more CPU and RAM to handle increased traffic <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. This can be easily achieved by resizing your Linode server to a larger instance <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>. A larger server can handle tens of thousands of concurrent users, which is sufficient for most projects <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.