---
title: Running AI models locally with Docker and open web UI
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

Running AI models locally provides significant advantages, particularly for privacy and offline capability <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. This method allows users to leverage powerful models without sending sensitive data to external servers <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

## Why Run Models Locally?

One primary reason to run AI models locally is to maintain control over your data <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>. When using online services like DeepSeek.com, your data is hosted in regions like China, subject to their local rules and regulations <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>. For sensitive business or personal information, this poses a risk as the data may not belong to a region where you have control <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>. By running models locally, your data remains on your machine, ensuring privacy <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

Additionally, local hosting enables offline use, allowing you to run models even when flying on a plane <a class="yt-timestamp" data-t="03:20:00">[03:20:20]</a>.

## Key Tools for Local AI Model Hosting

To run AI models locally, the recommended setup involves:
*   **Docker**: A platform for developing, shipping, and running applications in containers <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>.
*   **Open Web UI**: A user interface that looks similar to ChatGPT, designed to interact with local and API-connected models <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>.
*   **Ollama**: A tool for downloading and managing various open-source AI models locally <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>.

## Setting Up Your Local Environment

### 1. Install Docker Desktop
Download and install Docker Desktop from Docker.com <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>. Choose the version appropriate for your operating system (e.g., Apple silicon for M-series Macs) <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. Once installed, Docker will run in the background, indicated by its dashboard <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>.

### 2. Set Up Open Web UI with Docker
Open Web UI's quick start guide provides two essential terminal commands:
1.  **Pull the Container**: This downloads the Open Web UI Docker image to your machine <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.
    ```bash
    docker pull ghcr.io/open-webui/open-webui:main
    ```
2.  **Run the Container**: This command starts the Open Web UI application within a Docker container <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.
    *   For most users (e.g., Mac or Linux):
        ```bash
        docker run -d -p 3000:8080 --add-host host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
        ```
    *   For NVIDIA GPU users (on PC):
        ```bash
        docker run -d -p 3000:8080 --add-host host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always --gpus all ghcr.io/open-webui/open-webui:main
        ```
        The `--gpus all` flag takes advantage of your GPU for more efficient local model execution <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.
    After running the command, Open Web UI will be accessible in your web browser at `localhost:3000` <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. For single-user mode, a sign-in is not required <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.

### 3. Install Ollama and Download Models
Download and install Ollama from `ollama.com` <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>. Ollama allows you to download and manage AI models locally <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. Once installed, you'll see a small llama icon in your system tray, indicating it's running <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>.

From the Open Web UI interface, navigate to the admin panel (via the user icon at the bottom left) <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. In the settings area, under "Connections" (cloud icon), the Ollama API should already be configured <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.

To download models:
*   Click the "plus" button next to "Add model" <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.
*   Type the name of the model you want (e.g., "deep seek" for DeepSeek R1) <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.
*   If not already available, select the option to "pull from Ollama.com" <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. This will download the model directly to your machine <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. Models can be several gigabytes in size <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.

## Using Locally Hosted Models

Once models are downloaded via Ollama and connected in Open Web UI, you can select them from the model dropdown when starting a new chat <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. Locally running models will often be identified by a `colon latest` suffix <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.

When using a local model, all processing occurs on your computer, consuming local resources like RAM <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.

### Model Performance and Distillation

The performance of local models can vary based on their size and architecture:
*   **Larger Models**: Models with a higher parameter count (e.g., 600 billion parameters) have more "intelligence" but take longer to process <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>. The results are generally very detailed and human-level <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>.
*   **Distilled Models**: These are smaller, more efficient versions that run faster but may not provide the same depth of reasoning or detail as their full counterparts <a class="yt-timestamp" data-t="07:17:00">[07:17:17]</a>. An example is the distilled Llama 70B model <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>. The choice depends on the specific use case and desired output <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>.

### Tweak Model Output with Temperature

In Open Web UI, you can adjust the "temperature" setting in the control section <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.
*   **Lower Temperature (e.g., 0)**: Reduces "hallucinations" and makes the model adhere more strictly to instructions, useful for logical reasoning tasks like code generation <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.
*   **Higher Temperature (e.g., 1)**: Increases creativity, making the model more prone to generate imaginative or "out of the box" responses, suitable for creative writing or non-logical reasoning <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>. It's recommended to experiment with different temperatures to see how they affect your output <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>.

## Comparing Local Hosting with Cloud APIs

While running models locally is beneficial for privacy and offline access, using API providers like Fireworks AI or Groq offers an alternative to directly using services hosted in other countries <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. These providers host models in regions like North America, allowing your data to reside within specific legal jurisdictions <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>. You can connect to these APIs through Open Web UI by adding their base URL and API key <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

However, a key difference is that API endpoints from Fireworks or Groq may not include built-in web search capabilities, which DeepSeek.com provides <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

## Local AI on Mobile Devices

It's also possible to run AI models directly on mobile devices using applications like Apollo (available on app stores) <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>. Apollo allows you to download models locally onto your phone, similar to Ollama <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>. The app indicates which models are compatible with your device's memory <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>. Models optimized for Apple hardware, like those using Apple's MLX infrastructure, can run very efficiently on devices <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. This enables offline AI capabilities directly on your phone, opening up opportunities for on-device applications like emergency assistance or specialized communication tools <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>.

This flexibility underscores the importance of choosing the right tool for the job, as the most powerful model isn't always necessary for every use case <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.

## Conclusion

Running AI models locally using Docker, Open Web UI, and Ollama provides a powerful and private way to leverage advanced reasoning models <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>. This setup ensures your data remains in your control <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>. Experimenting with different models and settings is encouraged to discover new applications and potential [[using_ai_models_for_practical_applications_and_startups | startup]] ideas <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>. The field of AI is rapidly advancing, and local model hosting is becoming increasingly accessible <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.