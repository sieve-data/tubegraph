---
title: Setting up Docker for machine learning projects
videoId: aWMv8W_UgJU
---

From: [[hu-po]] <br/> 

Docker provides a more comprehensive solution for dependency management compared to Python-specific tools like Conda. It allows you to simulate an entire computer, enabling consistent environments across different machines, whether they are local setups or cloud instances [00:59:19](<a class="yt-timestamp" data-t="00:59:19">[00:59:19]</a>. This eliminates the need to repeatedly install dependencies when moving a project to new environments, such as AWS machines or different home computers [01:00:00](<a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.

## Benefits of Docker for ML

*   **Environment Consistency**: Docker ensures that all dependencies are set up identically, preventing obscure bugs that often arise from version mismatches [02:39:01](<a class="yt-timestamp" data-t="02:39:01">[02:39:01]</a>.
*   **Portability**: A Docker image acts as a "fake computer" that can be run on any machine with Docker installed [01:00:09](<a class="yt-timestamp" data-t="01:00:09">[01:00:09]</a>.
*   **Reproducibility**: By defining the exact environment, Docker makes it easier for others to replicate your results [02:39:01](<a class="yt-timestamp" data-t="02:39:01">[02:39:01]</a>.
*   **Isolation**: Projects are isolated within their containers, preventing conflicts between different project dependencies [00:59:19](<a class="yt-timestamp" data-t="00:59:19">[00:59:19]</a>.

## Docker Setup Steps

The process involves creating a `Dockerfile` to define the container's environment, building a Docker image, and then running it.

### 1. Create a Dockerfile

A `Dockerfile` outlines the steps to build your container image [01:00:25](<a class="yt-timestamp" data-t="01:00:25">[01:00:25]</a>.

```dockerfile
# Start from a base image
FROM nvidia/cuda:12.1-devel-ubuntu22.04

# Install Python 3 and other necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set up Python environment
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1 \
    && update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

# Install PyTorch and other dependencies
# Ensure the CUDA version matches your local GPU or a compatible version
RUN pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 \
    --index-url https://download.pytorch.org/whl/cu121 \
    tiktoken==0.6.0 datasets==2.18.0

# Clone the Mamba repository
# This assumes the Mamba repository is cloned directly into the project structure.
# For local development, this setup allows direct import from the cloned Mamba directory.
WORKDIR /app
RUN git clone https://github.com/state-spaces/mamba.git
WORKDIR /app/mamba
RUN pip install -e .

# Copy your application code into the container
# The '.' indicates copying from the current directory where docker build is run.
WORKDIR /app
COPY . .

# Set the entrypoint or default command if desired
# CMD ["python", "train.py"]
```

### 2. Create a .dockerignore File

Similar to `.gitignore`, a `.dockerignore` file specifies files and directories that should *not* be copied into the Docker image during the build process [01:04:01](<a class="yt-timestamp" data-t="01:04:01">[01:04:01]</a>. This prevents unnecessary data, such as large datasets or log files, from bloating your image.

```
# Ignore directories
.git/
__pycache__/
.vscode/
.ipynb_checkpoints/
logs/
data/ # Example: edu_fineweb10B, hellaswag
mamba/ # We clone this separately in the Dockerfile
.env
.DS_Store

# Ignore files
*.pyc
*.log
Dockerfile
.dockerignore
.gitignore
LICENSE
README.md
```

### 3. Build the Docker Image

Navigate to your project's root directory in the terminal (where your `Dockerfile` and `.dockerignore` reside) and run the `docker build` command. The `-t` flag tags your image with a name (e.g., `karpa_mbathi`), and the `.` specifies the build context (the current directory) [01:03:04](<a class="yt-timestamp" data-t="01:03:04">[01:03:04]</a>.

```bash
docker build -t karpa_mbathi -f Dockerfile .
```

On your first build, this process might take some time as it downloads the base image and installs all dependencies [01:05:16](<a class="yt-timestamp" data-t="01:05:16">[01:05:16]</a>. Subsequent builds are faster due to caching. You can list built images with `docker image ls` [01:06:23](<a class="yt-timestamp" data-t="01:06:23">[01:06:23]</a>.

### 4. Run the Docker Container

Once the image is built, you can run a container from it. Use `docker run` to execute commands inside your container.

```bash
# To run interactively and get a bash shell inside the container
docker run --gpus all --rm -it karpa_mbathi bash
# --gpus all: Grants access to all available GPUs.
# --rm: Automatically removes the container when it exits.
# -it: Provides an interactive terminal.
# karpa_mbathi: The name of your Docker image.
# bash: The command to run inside the container (opens a bash shell).
```

### 5. Sanity Check GPU Access within Container

After entering the container, you can perform checks to ensure your GPU is accessible and PyTorch can utilize it.

```bash
# Inside the container
nvidia-smi
python -c "import torch; print(f'Torch version: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}')"
```

The output for `torch.cuda.is_available()` should be `True` [01:07:54](<a class="yt-timestamp" data-t="01:07:54">[01:07:54]</a>. Note that the CUDA version reported inside the container might differ from your host machine's CUDA version, as it reflects the version installed within the container's base image [01:08:06](<a class="yt-timestamp" data-t="01:08:06">[01:08:06]</a>.

### 6. Running Your ML Script in Docker

To run your machine learning training script directly within the container, you can append the command to your `docker run` statement:

```bash
docker run --gpus all --rm karpa_mbathi python train.py
```

This command will execute `train.py` within the isolated Docker environment, utilizing your GPU [01:08:51](<a class="yt-timestamp" data-t="01:08:51">[01:08:51]</a>. You can monitor GPU utilization with `watch -n 0.5 nvidia-smi` in a separate terminal [00:33:27](<a class="yt-timestamp" data-t="00:33:27">[00:33:27]</a>.

## Important Considerations

*   **GPU Memory (VRAM)**: The amount of VRAM is crucial for [[performance_and_efficiency_in_machine_learning_models | model performance]] and the size of models you can train. More VRAM allows for larger models and batch sizes [00:42:46](<a class="yt-timestamp" data-t="00:42:46">[00:42:46]</a>. A higher VRAM count (e.g., 24GB on an RTX 3090) is generally more important than generation number (e.g., a 4060 with less VRAM) [00:43:52](<a class="yt-timestamp" data-t="00:43:52">[00:43:52]</a>.
*   **Batch Size Tuning**: If you encounter CUDA "out of memory" errors, reduce your batch size in the training script to fit your GPU's VRAM [00:52:57](<a class="yt-timestamp" data-t="00:52:57">[00:52:57]</a>.
*   **Hybrid Architectures**: Combining different model blocks, such as [[developments_in_deep_learning_hardware | Mamba blocks]] and Transformer blocks, can lead to more [[performance_and_efficiency_in_machine_learning_models | efficient]] models [02:15:04](<a class="yt-timestamp" data-t="02:15:04">[02:15:04]</a>. These architectures can sometimes be smaller in terms of parameters [01:27:31](<a class="yt-timestamp" data-t="01:27:31">[01:27:31]</a>.
*   **Data Loading**: For datasets with variable input lengths (ragged tensors), padding is necessary to ensure uniform batch sizes for training [02:28:27](<a class="yt-timestamp" data-t="02:28:27">[02:28:27]</a>.
*   **Fine-tuning vs. Training from Scratch**: For tasks like the Arc Challenge, [[finetuning_machine_learning_models | fine-tuning]] a pre-trained model (e.g., a Mamba model pre-trained on SlimPajama) can yield better results than training from scratch, as it leverages existing intelligence [02:38:49](<a class="yt-timestamp" data-t="02:38:49">[02:38:49]</a>. This requires transforming the specific dataset into a format suitable for language models [02:40:20](<a class="yt-timestamp" data-t="02:40:20">[02:40:20]</a>.
*   **Cloud Computing**: For large-scale training and [[parallelism_and_scalability_in_machine_learning | distributed training]], cloud providers like Lambda Cloud, AWS, Azure, or Google Cloud offer powerful GPUs [01:13:01](<a class="yt-timestamp" data-t="01:13:01">[01:13:01]</a>. These services often provide subsidized pricing or free credits, making it possible to access significant compute resources for experimentation [01:15:01](<a class="yt-timestamp" data-t="01:15:01">[01:15:01]</a>.