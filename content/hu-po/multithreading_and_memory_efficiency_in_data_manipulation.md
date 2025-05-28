---
title: Multithreading and memory efficiency in data manipulation
videoId: jU8Ghp7tRCU
---

From: [[hu-po]] <br/> 

## Introduction to Polars

[[performance_optimization_in_data_processing | Performance optimization in data processing]] is crucial, especially when handling large datasets. Polars is a lightning-fast data frame library for Python designed for this purpose <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It serves as a faster alternative to Pandas, which has been the most popular framework for tabular data in Python <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>, <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

Polars is written in Rust <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Rust is a systems programming language noted for its emphasis on safety, performance, and concurrency <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. It provides the speed and control of low-level languages while preventing common programming errors that can lead to crashes and security vulnerabilities <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

Polars offers a DataFrame API that is similar to Pandas, enabling users to perform efficient operations on large datasets <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Its design prioritizes [[computational_efficiency_and_memory_usage_in_large_language_models | memory efficiency]] and speed <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. It leverages Apache Arrow internally for data transmission <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Core Goals of Polars

The primary goals of Polars include <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>:
*   Providing a lightning-fast data frame library <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   Utilizing all available CPU cores, enabling multi-threading and multi-process operations <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>, <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   Optimizing queries to reduce unnecessary work and memory allocations <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. This addresses common issues in data manipulation workflows, such as unnecessary data copies and reallocations of large data frames, which can significantly slow down processes <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

Polars is designed from the ground up to achieve C/C++-like performance <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. It goes to great lengths to <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>:
*   Reduce random copies <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   Traverse memory cache efficiently <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   Minimize contention in [[parallelization_and_efficiency_in_lstm_architectures | parallelism]] <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   Process data in chunks <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   Reuse memory allocations <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

Unlike tools such as Dask, which try to parallelize existing single-threaded libraries like NumPy and Pandas, Polars is built for parallelism from its core <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## Eager vs. Lazy Execution

Polars supports both eager and lazy execution <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   **Eager execution** allows users to work line-by-line, similar to writing a Python script <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Lazy execution** allows the system to optimize the code over time, especially for repeated functions <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This paradigm is also adopted by deep learning frameworks like JAX, PyTorch, and TensorFlow, where an optimal compute graph is created over time <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>, <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

In lazy mode, Polars builds a query plan that is not executed until explicitly requested via a `collect()` call <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>. This provides Polars with the entire context of the query, enabling it to perform optimizations and select the fastest algorithm <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.

## Performance Benchmarks

Polars demonstrates significant speed improvements over Pandas, particularly in filtering and joining operations.

### Reading CSV Files

In a test reading a CSV file (the Iris dataset), Polars showed marginal speed improvement over Pandas <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
*   **Pandas `read_csv`**: Approximately 0.14 seconds per operation (average over 10 runs) <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   **Polars `read_csv`**: Marginally faster <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

### Data Filtering

For a filtering operation on a large dataset (e.g., 100 million rows), Polars significantly outperforms Pandas <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.

In a test filtering a large data frame (100 million rows) based on a column value and then grouping by a categorical variable, CPU utilization shows a clear difference:
*   **Pandas**: Primarily utilizes a single CPU core, with other cores largely idling <a class="yt-timestamp" data-t="00:29:08">[00:29:08]</a>, <a class="yt-timestamp" data-t="00:29:17">[00:29:17]</a>.
*   **Polars (Eager)**: Shows much higher CPU utilization across multiple cores, indicating effective multi-threading <a class="yt-timestamp" data-t="00:29:32">[00:29:32]</a>, <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a>. This multi-CPU usage is a key advertised feature of Polars <a class="yt-timestamp" data-t="00:29:57">[00:29:57]</a>.
*   **Polars (Lazy)**: While still leveraging multiple CPUs, the lazy version was observed to be slightly slower in some specific test cases, possibly due to implementation details or overhead on small datasets <a class="yt-timestamp" data-t="00:29:48">[00:29:48]</a>.

### Data Joining

Similar performance benefits are observed in join operations on large data frames.
*   **Pandas**: Again, single-threaded, with only one CPU maxing out while others remain idle <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>.
*   **Polars**: Significantly utilizes all available CPU cores, leading to faster execution <a class="yt="yt-timestamp" data-t="00:35:19">[00:35:19]</a>, <a class="yt-timestamp" data-t="00:35:24">[00:35:24]</a>.

## API Similarities and AI Assistance

The Polars API is very similar to Pandas, making it relatively easy for Pandas users to transition <a class="yt-timestamp" data-t="00:36:37">[00:36:37]</a>, <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. For example, `df.head()`, `df.tail()`, and `df.sample()` functions exist in both libraries <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>, <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>, <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.

Generative AI tools like ChatGPT are capable of understanding and generating code for both Pandas and Polars APIs, assisting users in finding the correct syntax for various queries and operations <a class="yt-timestamp" data-t="00:36:43">[00:36:43]</a>.

## Conclusion

Polars offers a significant speed boost compared to Pandas, primarily due to its efficient use of [[performance_optimization_in_data_processing | multithreading]] and optimized [[computational_efficiency_and_memory_usage_in_large_language_models | memory management]]. While the API is largely familiar, minor differences exist <a class="yt-timestamp" data-t="00:36:39">[00:36:39]</a>.