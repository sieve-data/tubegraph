---
title: Troubleshooting and debugging machine learning code
videoId: aWMv8W_UgJU
---

From: [[hu-po]] <br/> 

Effective troubleshooting and [[debugging_neural_network_training | debugging neural network training]] are crucial skills in machine learning development. This guide covers general strategies and specific challenges encountered, particularly when working with models like GPT-2 and Mamba.

## Setting Up Your Development Environment

A robust and consistent [[setting_up_a_coding_environment_for_machine_learning | setting up a coding environment for machine learning]] is the first step to minimizing debugging headaches.

### Local Development with Conda
For local development, Conda is a useful tool for managing Python dependencies <a class="yt-timestamp" data-t="00:31:03">[00:31:03]</a>. It allows you to create isolated environments, ensuring that your project uses specific versions of libraries, preventing conflicts with other projects on your system <a class="yt-timestamp" data-t="00:32:41">[00:32:41]</a>.

Key steps for setting up a Conda environment:
*   **Create a new environment:** `conda create -n your_env_name python=3.11` <a class="yt-timestamp" data-t="00:31:08">[00:31:08]</a>
*   **Activate the environment:** `conda activate your_env_name` <a class="yt-timestamp" data-t="00:31:36">[00:31:36]</a>
*   **Install PyTorch and other dependencies:** Specify the CUDA version compatible with your GPU drivers to ensure proper GPU utilization <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>. For example, `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121` <a class="yt-timestamp" data-t="00:33:03">[00:33:03]</a>.
*   **Pinning dependencies:** Always pin exact versions of libraries (e.g., `tiktoken==0.5.2`, `datasets==2.15.0`) to avoid "obscure bugs" caused by version mismatches, especially when combining code from different repositories <a class="yt-timestamp" data-t="00:38:19">[00:38:19]</a>.

### Containerization with Docker
For consistency across different machines or cloud environments, Docker provides a more comprehensive dependency management solution. It simulates an entire computer environment, packaging all dependencies and configurations into a "container" <a class="yt-timestamp" data-t="01:00:05">[01:00:05]</a>.

*   **Dockerfile:** Defines the environment, including the base OS (e.g., Ubuntu), CUDA version, Python installation, and all project dependencies <a class="yt-timestamp" data-t="01:01:05">[01:01:05]</a>.
*   **Docker Ignore:** Similar to `.gitignore`, it tells Docker which files (like large datasets or logs) to exclude when building the image, preventing unnecessary bloat <a class="yt-timestamp" data-t="01:04:09">[01:04:09]</a>.
*   **Building and Running:** Use `docker build -t your_image_name .` to create the image and `docker run --gpus all --rm -it your_image_name bash` to run it, ensuring GPU access <a class="yt-timestamp" data-t="01:03:16">[01:03:16]</a>.

## General Debugging Strategies

*   **Sanity Checks:** After setting up an environment, run a sanity check script (e.g., a `.sh` script) to verify Python, CUDA, and PyTorch installations and confirm that PyTorch can utilize the GPU (`torch.cuda.is_available()`) <a class="yt-timestamp" data-t="00:45:47">[00:45:47]</a>.
*   **Version Control (Git):** Regularly commit changes to track progress, especially before making significant modifications or attempting fixes. Use meaningful commit messages <a class="yt-timestamp" data-t="01:10:50">[01:10:50]</a>.
*   **Integrated Development Environment (IDE):** Use an IDE like VS Code for efficient coding and debugging. Learn shortcuts for common tasks like file navigation, version control views, and debugging controls <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>.
*   **Breakpoints and Debugging:** Set breakpoints in your code and use the IDE's debugger (e.g., VS Code's Python Debugger) to step through execution, inspect variable states, and understand program flow <a class="yt-timestamp" data-t="02:20:03">[02:20:03]</a>.
*   **Resource Monitoring:** Use tools like `nvidia-smi` to monitor GPU VRAM, utilization, and power consumption, and system monitors (e.g., `gnome-system-monitor`) for CPU and RAM <a class="yt-timestamp" data-t="00:33:27">[00:33:27]</a>. This helps diagnose bottlenecks or "out of memory" errors.
*   **Code Style and Organization:** While adapting to an existing codebase's style (e.g., Karpathy's minimalist approach) is beneficial, remember that modern practices often favor explicit typing and consolidated files for easier debugging with tools like ChatGPT <a class="yt-timestamp" data-t="01:36:06">[01:36:06]</a>.

## Common Machine Learning Debugging Challenges

### GPU Memory Management
One of the most frequent issues in machine learning is encountering `CUDA out of memory` errors <a class="yt-timestamp" data-t="00:52:56">[00:52:56]</a>.
*   **VRAM is Key:** The amount of VRAM (Video RAM) on your GPU is often the most critical factor for model development, more so than the GPU generation number (e.g., a 3090 with 24GB VRAM can be more useful than a 4060 with 8GB) <a class="yt-timestamp" data-t="00:42:46">[00:42:46]</a>.
*   **Reduce Batch Size:** The primary solution to `CUDA out of memory` is to reduce the batch size (`B` in the configuration) <a class="yt-timestamp" data-t="00:53:30">[00:53:30]</a>. This directly impacts the amount of data and intermediate activations loaded onto the GPU at any given time.
*   **Micro-batches:** For larger effective batch sizes on smaller GPUs, micro-batching can be used, where gradients are accumulated over several smaller batches before a single optimization step <a class="yt-timestamp" data-t="00:55:50">[00:55:50]</a>.

### Data Loaders and Data Preparation
[[loading_and_preparing_datasets_for_machine_learning_tasks | Loading and preparing datasets for machine learning tasks]] can introduce complex bugs.
*   **Dataset Structure:** Understand how your data is structured (e.g., JSON files, sharded datasets) and ensure your data loader correctly parses and processes it <a class="yt-timestamp" data-t="01:38:04">[01:38:04]</a>.
*   **Variable-Length Sequences:** If your data examples have different lengths (e.g., images of varying sizes or text sequences), you must implement **padding** to make them uniform before batching. This typically involves filling shorter sequences with zeros to match the length of the longest sequence in the batch or a predefined maximum sequence length <a class="yt-timestamp" data-t="02:28:27">[02:28:27]</a>.
*   **Input/Output Shapes:** Ensure that the tensors produced by your data loader (input `X` and target `Y`) have the correct shapes and data types (e.g., `torch.long` for token IDs, `torch.float` for embeddings) for your model's architecture <a class="yt-timestamp" data-t="02:59:45">[02:59:45]</a>.
*   **Training Loop Interaction:** The data loader must correctly interface with the training loop. If the loop expects a fixed number of steps or epochs, the data loader needs to either stop iteration appropriately (`StopIteration`) or be designed to "repeat" data for more epochs <a class="yt-timestamp" data-t="03:15:58">[03:15:58]</a>.

### Model Architecture and Configuration
When [[training_and_finetuning_of_language_models_for_code | training and finetuning of language models for code]], configuration settings are critical.
*   **Hybrid Architectures:** Combining different model blocks (e.g., Transformer and Mamba) requires careful configuration of their respective dimensions and parameters <a class="yt-timestamp" data-t="01:21:47">[01:21:47]</a>. Mismatches can lead to shape errors during forward passes.
*   **Vocabulary Size:** For token-based models, ensure the `vocab_size` in your model's configuration matches the number of unique tokens in your dataset or tokenizer <a class="yt-timestamp" data-t="02:54:33">[02:54:33]</a>.
*   **Sequence Length (`block_size`):** The maximum sequence length the model can process directly impacts memory usage. For Transformer models, memory scales quadratically with sequence length <a class="yt-timestamp" data-t="02:14:40">[02:14:40]</a>. Hybrid models like Mamba may offer more linear scaling <a class="yt-timestamp" data-t="02:15:08">[02:15:08]</a>.

## Example Troubleshooting Flow

When an error occurs, follow these steps:
1.  **Identify the error message:** Read the full traceback. Look for line numbers and specific error types (e.g., `AttributeError`, `RuntimeError: CUDA out of memory`).
2.  **Inspect variables:** Use a debugger to examine the shapes, types, and values of tensors and variables at the point of the error <a class="yt-timestamp" data-t="02:26:27">[02:26:27]</a>.
3.  **Trace the flow:** Understand which parts of the code contribute to the problematic data or operation.
4.  **Consult documentation/community:** For library-specific errors (e.g., PyTorch, Mamba), refer to official documentation or search online forums for similar issues.
5.  **Iterate and test:** Make small, isolated changes and re-run your code to confirm fixes.

By systematically addressing these aspects, you can efficiently troubleshoot and debug your machine learning models.