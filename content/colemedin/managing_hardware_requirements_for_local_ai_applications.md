---
title: Managing hardware requirements for local AI applications
videoId: hKrl5Gr7hM0
---

From: [[colemedin]] <br/> 

Managing hardware requirements is a significant consideration when working with [[tech_stack_for_local_ai_applications | local AI applications]] <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. While [[setting_up_a_local_ai_cloud_stack | local AI setups]] can run on your own machine, there are times when you might need access to hardware you don't possess <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Deploying your local AI stack to the cloud can solve this by providing access to more robust hardware <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Hardware Considerations

The type of hardware required largely depends on the size and nature of the AI models you intend to run:

*   **CPU Instances**: Sufficient for running the entire [[tech_stack_for_local_ai_applications | local AI package]] unless you plan to run larger Local Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **GPU Instances**: Essential for running LLMs larger than seven or eight billion parameters <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. These instances typically come at a higher cost <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   **Memory (RAM)**: A minimum of 8GB of RAM is suggested for running the full local AI package, assuming no dedicated GPU is used for LLMs <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

Many users opt for CPU instances due to their lower cost, choosing to host [[incorporating_ai_models_and_databases_in_a_local_setup | Ollama]] elsewhere or use external APIs like OpenRouter, while keeping the rest of their stack private and local <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

## Cloud Provider Recommendations for AI Deployment

When [[choosing_cloud_providers_for_local_ai_deployment | choosing cloud providers]] for [[deploying_ai_applications_to_the_cloud | deploying AI applications]], it's crucial to research options based on your specific needs and budget <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

*   **DigitalOcean**:
    *   Recommended for CPU instances if not running larger LLMs that require a dedicated GPU <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
    *   Offers CPU instances with good options, such as 8GB RAM and two CPUs for approximately $42/month, sufficient for the full local AI package without larger LLMs <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
    *   Also provides GPU droplets for more demanding local LLMs <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Akamai Cloud (formerly Linode)**: Another viable option for CPU instances <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **GPU Instance Platforms**:
    *   **Specialized Providers**: Lambda Labs, Vultr, and Paperspace (part of DigitalOcean but a distinct platform) offer GPU instances <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
    *   **Enterprise Solutions**: AWS, Google Cloud, and Microsoft Azure provide GPU instances for larger-scale deployments <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

### Platforms with Limitations

Some platforms are less suitable for deploying the entire local AI package due to specific restrictions:

*   **TensorDock**: Great for cheap GPUs but restricts opening all necessary ports for the local AI package <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **RunPod and Novita**: While good, they deploy everything as containers, making it more challenging to run the local AI package which relies on containers within containers <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

## Setting Up a Cloud Instance

To set up a cloud instance for your [[tech_stack_for_local_ai_applications | local AI stack]]:

1.  **Choose an Instance Type**: Select a CPU or GPU instance based on your LLM requirements <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
2.  **Select an Image**: Opt for an Ubuntu Linux instance with Docker pre-installed, as it's a popular and compatible distribution <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
3.  **Authentication**: Use SSH keys for more secure access or a password for simplicity <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
4.  **Firewall Configuration**: Once the instance is ready, open necessary firewall ports for all local AI services, such as Superbase, Flowise, Open Web UI, and n8n <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. Ports for CRX-NG or [[incorporating_ai_models_and_databases_in_a_local_setup | Ollama]] are typically kept private as they are not password-protected <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
5.  **DNS Records**: Set up A records for subdomains (e.g., `n8n.yourdomain.com`, `superbase.yourdomain.com`) to point to your instance's IPv4 address. This allows secure access to services via Caddy, which handles HTTPS and TLS <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

After these steps, you can proceed with the base installation of the [[tech_stack_for_local_ai_applications | local AI package]] by cloning its repository and configuring environment variables <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. The script will then pull and run the necessary Docker containers, including Superbase, [[extending_local_ai_infrastructure | Ollama]], n8n, Open Web UI, and Caddy, all within a single Docker Compose network for inter-container communication <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.

To run [[incorporating_ai_models_and_databases_in_a_local_setup | Ollama]] on a CPU instance, use the specific command `python3 ./run.py --profile cpu_ollama` <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. If using an Nvidia GPU, use `python3 ./run.py --profile gpu_nvidia` <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

Once deployed, you can verify the status of your containers using `docker ps` and check logs with `docker logs -f [container_name]` <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.