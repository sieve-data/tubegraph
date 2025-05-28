---
title: Loading and preparing datasets for machine learning tasks
videoId: aWMv8W_UgJU
---

From: [[hu-po]] <br/> 

## Overview
Preparing and loading datasets is a crucial step in [[Training and data preparation methodologies | machine learning training]]. This process involves not only acquiring the data but also transforming it into a format suitable for model consumption, often necessitating careful [[Computational Challenges in Training Large Models | memory management]] and handling of diverse data structures <a class="yt-timestamp" data-t="01:33:04">[01:33:04]</a>.

## Initial Data Setup and Challenges
For the `train.py` script, which is inspired by Karpathy's GPT-2 implementation, the initial dataset used is `edu_fine_web` <a class="yt-timestamp" data-t="01:34:16">[01:34:16]</a>. This dataset is sharded and can be quite large, with one instance observed at 20 GB <a class="yt-timestamp" data-t="00:50:38">[00:50:38]</a> <a class="yt-timestamp" data-t="00:51:02">[00:51:02]</a>. To prevent large data files from being committed to version control, a `.git_ignore` file is used <a class="yt-timestamp" data-t="00:51:47">[00:51:47]</a>.

### Adjusting for GPU Memory
When running machine learning models, especially large language models (LLMs), [[Computational Challenges in Training Large Models | GPU memory]] (vRAM) is a critical resource <a class="yt-timestamp" data-t="00:42:46">[00:42:46]</a>. The initial `train.py` script attempts to allocate 12 GB, leading to an "out of memory" error on a 24 GB GPU <a class="yt-timestamp" data-t="00:52:57">[00:52:57]</a>. To mitigate this, the `batch_size` parameter in the training script needs to be reduced <a class="yt-timestamp" data-t="00:53:30">[00:53:30]</a>.

Experiments with batch sizes demonstrated the impact on vRAM usage:
*   Batch size 2: ~3 GB vRAM <a class="yt-timestamp" data-t="00:54:15">[00:54:15]</a>
*   Batch size 8: ~7 GB vRAM <a class="yt-timestamp" data-t="00:54:46">[00:54:46]</a>
*   Batch size 16: ~12 GB vRAM <a class="yt-timestamp" data-t="00:55:08">[00:55:08]</a>
*   Batch size 32: Reached 22 GB vRAM, but still encountered "out of memory" errors later in the process <a class="yt-timestamp" data-t="00:55:35">[00:55:35]</a> <a class="yt-timestamp" data-t="00:56:28">[00:56:28]</a>.

A batch size of 16 was eventually settled upon for the available GPU <a class="yt-timestamp" data-t="00:56:37">[00:56:37]</a>. The concept of "micro batches" was also mentioned, where gradients are accumulated over smaller chunks to simulate a larger effective batch size, which is useful when GPU memory is limited <a class="yt-timestamp" data-t="00:56:09">[00:56:09]</a>.

## Implementing Data Loaders for [[Abstract Reasoning Challenge (ARC) Corpus | ARC Challenge]]
The goal shifted to adapting the `train.py` script for the [[Abstract Reasoning Challenge (ARC) Corpus | ARC challenge]] dataset <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. This involved creating a new data loader, `ArcDataLoader`, which would be integrated into the existing `train.py` file <a class="yt-timestamp" data-t="01:35:27">[01:35:27]</a>.

The [[Abstract Reasoning Challenge (ARC) Corpus | ARC dataset]] is notably smaller and designed for quick download and training, making it suitable for local development <a class="yt-timestamp" data-t="01:38:22">[01:38:22]</a>.

### Data Structure and Processing
The [[Abstract Reasoning Challenge (ARC) Corpus | ARC dataset]] consists of JSON files, where each file represents a "task" <a class="yt-timestamp" data-t="01:38:04">[01:38:04]</a>. Each task contains:
*   `demonstration` (training data): A list of input/output pairs for the model to learn from <a class="yt-timestamp" data-t="02:00:54">[02:00:54]</a>.
*   `test` (evaluation data): A list of input/output pairs, where the model must predict the output for the given input <a class="yt-timestamp" data-t="02:10:15">[02:10:15]</a>.

A key challenge identified was the variable length of input and output grids within the tasks <a class="yt-timestamp" data-t="02:09:23">[02:09:23]</a>. For example, some inputs were 30x30, while others were smaller <a class="yt-timestamp" data-t="02:02:37">[02:02:37]</a> <a class="yt-timestamp" data-t="02:09:56">[02:09:56]</a>. This variability caused issues when creating batches for the model, as [[Implementing data augmentation and padding in datasets | PyTorch]] expects tensors of equal size <a class="yt-timestamp" data-t="02:28:12">[02:28:12]</a>.

To address this, the data needs to be padded to a maximum sequence length <a class="yt-timestamp" data-t="02:28:27">[02:28:27]</a>. This padding typically involves filling the shorter sequences with zeros to match the longest sequence in a batch <a class="yt-timestamp" data-t="02:35:33">[02:35:33]</a>. The values in the grids are integer indices representing colors (0-9 values) <a class="yt-timestamp" data-t="02:33:26">[02:33:26]</a>. These integer values are then converted into PyTorch LongTensors, similar to how text tokens are handled <a class="yt-timestamp" data-t="02:51:34">[02:51:34]</a> <a class="yt-timestamp" data-t="02:52:28">[02:52:28]</a>.

The data loader ultimately provides an `X` (input) and `Y` (target) for the model <a class="yt-timestamp" data-t="02:17:51">[02:17:51]</a>. In this context, `X` is formed by flattening and concatenating all demonstration inputs, demonstration outputs, and the test case input <a class="yt-timestamp" data-t="02:11:04">[02:11:04]</a> <a class="yt-timestamp" data-t="02:13:35">[02:13:35]</a>. `Y` is the corresponding test case output <a class="yt-timestamp" data-t="02:11:44">[02:11:44]</a>.

### Data Loader Implementation Details
*   **Shuffling:** Data is shuffled for the training split but not for the evaluation split <a class="yt-timestamp" data-t="01:53:41">[01:53:41]</a>.
*   **Iterator:** The `DataLoader` object is wrapped in an `iter()` call to allow calling `next()` on it for batch retrieval <a class="yt-timestamp" data-t="02:27:31">[02:27:31]</a>.
*   **Vocab Size:** The number of unique values in the dataset (colors) determines the `vocab_size` for the model's output layer, set to 10 in this case <a class="yt-timestamp" data-t="02:54:33">[02:54:33]</a> <a class="yt-timestamp" data-t="02:54:53">[02:54:53]</a>.
*   **Sequence Length:** The `block_size` (or sequence length) of the model was increased to accommodate the flattened inputs, from 1024 to 4096 <a class="yt-timestamp" data-t="02:14:27">[02:14:27]</a>. While Transformers have quadratic complexity with sequence length, the hybrid Mamba architecture's linear scaling helps manage this <a class="yt-timestamp" data-t="02:14:40">[02:14:40]</a>.
*   **Epochs vs. Steps:** The training script is designed to run for a hardcoded number of steps. If the `DataLoader` runs out of data before these steps are complete, it hits a `StopIteration` error. A hacky solution is to re-initialize the `DataLoader` from the dataset when this occurs, effectively creating more "epochs" <a class="yt-timestamp" data-t="03:17:13">[03:17:13]</a> <a class="yt-timestamp" data-t="03:22:35">[03:22:35]</a>.

## Data Augmentation Considerations
[[Implementing data augmentation and padding in datasets | Data augmentation]] is a technique to add noise to data, improving model generalization <a class="yt-timestamp" data-t="02:47:17">[02:47:17]</a>. While common in image tasks (e.g., flipping, rotating images of cats), it is more challenging for the [[Abstract Reasoning Challenge (ARC) Corpus | ARC task]] due to its fragile nature <a class="yt-timestamp" data-t="02:47:39">[02:47:39]</a>. Possible augmentations might include horizontal or vertical flipping, provided they maintain the validity of the task <a class="yt-timestamp" data-t="02:48:36">[02:48:36]</a>. Randomly changing grid colors would likely invalidate the examples <a class="yt-timestamp" data-t="02:48:46">[02:48:46]</a>.

## Development Environment for Data Preparation
For local development, a `conda` environment is used for Python-specific dependency management <a class="yt-timestamp" data-t="02:57:07">[02:57:07]</a>. For reproducible and portable environments, Docker is preferred, as it simulates an entire computer with all dependencies pre-configured <a class="yt-timestamp" data-t="02:59:59">[02:59:59]</a>. A `Dockerfile` defines the environment, including the base operating system (e.g., Ubuntu), CUDA version, and Python packages <a class="yt-timestamp" data-t="01:01:05">[01:01:05]</a>. A `.dockerignore` file is used to specify files and folders that should not be copied into the Docker image, such as large datasets <a class="yt-timestamp" data-t="01:04:31">[01:04:31]</a>. Sanity checks are performed within both `conda` and Docker environments to ensure PyTorch can access the GPU correctly <a class="yt-timestamp" data-t="01:07:37">[01:07:37]</a>.