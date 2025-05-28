---
title: Setting up a coding environment for machine learning
videoId: aWMv8W_UgJU
---

From: [[hu-po]] <br/> 

Setting up an efficient and reliable coding environment is crucial for machine learning development. This involves managing dependencies, configuring hardware, and utilizing various tools to streamline the workflow.

## Version Control with Git

Version control is essential for tracking changes and collaborating on code.
*   Begin by creating a new GitHub repository to house your project <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
*   Use a `.gitignore` file to tell Git which files to ignore, such as compiled artifacts, images, and large data sets <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. This also applies to cloned repositories like Mamba and log folders <a class="yt-timestamp" data-t="00:40:51">[00:40:51]</a>, <a class="yt-timestamp" data-t="00:51:57">[00:51:57]</a>, <a class="yt-timestamp" data-t="00:58:49">[00:58:49]</a>.
*   Common Git commands include `git add` to stage changes, `git commit` to save changes, and `git push` to upload to the remote repository <a class="yt-timestamp" data-t="00:19:13">[00:19:13]</a>.
*   Modern development environments like VS Code integrate Git, allowing for visual staging, committing, and pushing <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

## Dependency Management

[[Troubleshooting and debugging machine learning code | Dependency management]] involves ensuring all necessary libraries and packages are available in the correct versions for your project <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>. This prevents obscure bugs caused by version mismatches <a class="yt-timestamp" data-t="00:38:58">[00:38:58]</a>.

### Local Setup with Conda

Conda is a popular package and environment management system for Python, primarily used for local development <a class="yt-timestamp" data-t="00:31:03">[00:31:03]</a>.
1.  **Create a new environment**: `conda create -n carpa_mamba python=3.11` <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>.
2.  **Activate the environment**: `conda activate carpa_mamba` <a class="yt-timestamp" data-t="00:31:36">[00:31:36]</a>. This isolates your project's dependencies from your system's base Python <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.
3.  **Install PyTorch**: Use `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121` (adjust `cu121` based on your CUDA version) <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>.
4.  **Install other dependencies**: For this project, `pip install tiktoken datasets` were required for the Karpathy codebase <a class="yt-timestamp" data-t="00:37:51">[00:37:51]</a>.
5.  **Pinning versions**: It's good practice to specify exact versions of dependencies (e.g., `tiktoken==0.6.0`) to ensure reproducibility <a class="yt-timestamp" data-t="00:39:07">[00:39:07]</a>.
6.  For external repositories, cloning them directly into your project directory (e.g., the Mamba repo) allows for easier local modification and import <a class="yt-timestamp" data-t="00:39:37">[00:39:37]</a>. Then, install it in editable mode: `pip install -e .` <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>.

### Portable Environments with Docker

Docker provides a more comprehensive [[dependency_management | dependency management]] solution by simulating an entire computer environment <a class="yt-timestamp" data-t="01:00:03">[01:00:03]</a>. This ensures consistent execution across different machines or cloud environments.
1.  **Create a `Dockerfile`**: This file defines the steps to build your Docker image.
    *   `FROM` specifies a base image (e.g., `nvidia/cuda:12.1-devel-ubuntu22.04` for a system with CUDA pre-installed) <a class="yt-timestamp" data-t="01:01:07">[01:01:07]</a>.
    *   `RUN` commands execute terminal commands within the container (e.g., installing Python, PyTorch, and other dependencies) <a class="yt-timestamp" data-t="01:02:24">[01:02:24]</a>.
    *   `COPY` copies files from your local machine into the container <a class="yt-timestamp" data-t="01:03:53">[01:03:53]</a>.
2.  **Use `.dockerignore`**: Similar to `.gitignore`, this file specifies files to exclude from being copied into the Docker image, preventing unnecessarily large image sizes <a class="yt-timestamp" data-t="01:04:08">[01:04:08]</a>.
3.  **Build the Docker image**: `docker build -t carpa_mamba .` <a class="yt-timestamp" data-t="01:03:16">[01:03:16]</a>.
4.  **Run the Docker container**: `docker run --gpus all --rm -it carpa_mamba bash` <a class="yt-timestamp" data-t="01:05:58">[01:05:58]</a>. This command runs the container, grants GPU access, and removes it upon exit.

## GPU and Hardware Considerations

[[Hardware for AI training and deployment | GPU selection]] is paramount for [[training_and_finetuning_of_language_models_for_code | machine learning training]].
*   **Check GPU status**: Use `watch -n 0.5 nvidia-smi` to monitor GPU utilization, memory, and power consumption <a class="yt-timestamp" data-t="00:33:27">[00:33:27]</a>.
*   **VRAM (Video RAM)**: This is the most crucial metric when buying a GPU, as it determines how much of your model and batch data can fit into GPU memory <a class="yt-timestamp" data-t="00:42:46">[00:42:46]</a>. You want to load your entire model and batch into VRAM to avoid slow data transfers between CPU and GPU memory <a class="yt-timestamp" data-t="00:43:35">[00:43:35]</a>.
    *   A 3090 with 24GB VRAM is considered a capable GPU, even if older generation <a class="yt-timestamp" data-t="00:43:56">[00:43:56]</a>.
*   **CUDA Compatibility**: Ensure your PyTorch installation's CUDA version (e.g., `cu121`) is compatible with your GPU's installed CUDA version (e.g., 12.2) <a class="yt-timestamp" data-t="00:35:35">[00:35:35]</a>.
*   **Used GPUs**: Buying used GPUs can be cost-effective, but inquire about their prior use. Gaming GPUs are generally fine, but those used for 24/7 cryptocurrency mining may be worn out <a class="yt-timestamp" data-t="00:44:20">[00:44:20]</a>.
*   **Cloud Computing**: For larger training tasks, cloud GPU providers like Lambda Cloud, AWS, Microsoft, and Google offer powerful hardware <a class="yt-timestamp" data-t="01:13:08">[01:13:08]</a>. Be aware that introductory prices are often subsidized to attract users <a class="yt-timestamp" data-t="01:14:26">[01:14:26]</a>.

## Debugging and Workflow Tools

*   **VS Code**: A popular IDE offering strong integration for Git, Python development, and [[troubleshooting_and_debugging_machine_learning_code | debugging]].
*   **Keyboard Shortcuts**: Learning and using shortcuts can significantly speed up your workflow and improve cognitive flexibility <a class="yt-timestamp" data-t="02:09:59">[02:09:59]</a>. Examples include `Ctrl+Shift+1` to start the Python debugger and `Ctrl+Shift+2` to stop it <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.
*   **System Monitor**: Tools like `gnome-system-monitor` help visualize CPU and RAM usage alongside `nvidia-smi` for GPU metrics <a class="yt-timestamp" data-t="00:57:27">[00:57:27]</a>.
*   **`sanity_check.sh` script**: A simple shell script to verify your environment setup:
    ```bash
    nvidia-smi
    python3 --version
    nvcc --version
    python3 -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
    ```
    This script confirms CUDA version, PyTorch version, and whether PyTorch can access your GPU <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>.
*   **ChatGPT/AI Integration**: Copying your entire code into a single file makes it easier to paste into AI tools like ChatGPT for [[using_ai_integration_in_coding_environments | debugging and assistance]] <a class="yt-timestamp" data-t="01:36:10">[01:36:10]</a>.

## Adjusting Model Parameters for Local Training

When working with large models or limited GPU [[hardware_for_ai_training_and_deployment | hardware]], adjustments are necessary.
*   **Batch Size**: If you encounter CUDA out of memory errors, reduce the `batch_size` <a class="yt-timestamp" data-t="00:52:57">[00:52:57]</a>. Start with small values (e.g., 2) and gradually increase until GPU VRAM is maximized <a class="yt-timestamp" data-t="00:54:11">[00:54:11]</a>.
*   **Model Size**: Reduce `n_layer`, `n_head`, and `n_embd` parameters in the model configuration to create a smaller model suitable for local development <a class="yt-timestamp" data-t="01:58:49">[01:58:49]</a>. This enables faster [[troubleshooting_and_debugging_machine_learning_code | debugging]] and iteration <a class="yt-timestamp" data-t="01:59:06">[01:59:06]</a>.
*   **Sequence Length (Block Size)**: Adjust `block_size` to accommodate the flattened input data for tasks like the [[evaluation_of_ai_coding_through_benchmarks | ARC Challenge]] <a class="yt-timestamp" data-t="02:14:04">[02:14:04]</a>.

## Data Loading for Specific Tasks

For tasks like the [[evaluation_of_ai_coding_through_benchmarks | Abstract Reasoning Corpus (ARC) Challenge]], custom data loaders are often required to correctly format the input for a language model.
*   The ARC dataset consists of JSON files, with each task having "demonstration" (input/output pairs) and "test" (input/output pairs) <a class="yt-timestamp" data-t="01:38:04">[01:38:04]</a>.
*   The data needs to be flattened into a sequence and padded to a uniform `block_size` to accommodate varying input dimensions (e.g., 30x30 grids) <a class="yt-timestamp" data-t="02:12:01">[02:12:01]</a>, <a class="yt-timestamp" data-t="02:28:27">[02:28:27]</a>. Padding fills empty spaces with zeros <a class="yt-timestamp" data-t="02:35:33">[02:35:33]</a>.
*   While [[loading_and_preparing_datasets_for_machine_learning_tasks | fine-tuning]] a pre-trained model (e.g., on SlimPajama) with a text-based representation of the ARC challenge would likely yield better performance, training from scratch on the task is simpler for local experimentation <a class="yt-timestamp" data-t="02:38:30">[02:38:30]</a>.
*   Care must be taken to ensure the data format matches the model's expected input, particularly for vocabulary size and tensor dimensions <a class="yt-timestamp" data-t="02:51:34">[02:51:34]</a>.