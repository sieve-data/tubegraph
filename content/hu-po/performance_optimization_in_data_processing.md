---
title: Performance optimization in data processing
videoId: jU8Ghp7tRCU
---

From: [[hu-po]] <br/> 

[[Polars]] is a lightning-fast data frame library for Python, designed to handle tabular data efficiently <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. It serves as a faster alternative to [[Pandas]], which has historically been the most popular framework for tabular data in Python's data science and machine learning workflows <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>, <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Why Polars is Fast

[[Polars]] achieves its speed through several key architectural and implementation choices:

*   **Written in Rust**
    [[Polars]] is written entirely in [[Rust programming language|Rust]], a systems programming language known for its focus on safety, performance, and concurrency <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>, <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. Rust aims to provide the speed and control of low-level languages like C/C++ while preventing common programming errors that lead to crashes and security vulnerabilities <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

*   **Multi-Core Utilization**
    A primary goal of [[Polars]] is to provide a data frame library that utilizes all available CPU cores, enabling [[Multithreading and memory efficiency in data manipulation|multi-threading and multi-processing]] <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>, <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This contrasts with [[Pandas]], which is often limited to single-threaded operations <a class="yt-timestamp" data-t="00:29:08">[00:29:08]</a>, <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>.

*   **Optimized Queries and Memory Management**
    [[Polars]] optimizes queries to reduce unneeded work and focuses on efficient memory allocation <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>, <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. It goes to great lengths to:
    *   Reduce random copies <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
    *   Traverse memory cache efficiently <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>
    *   Minimize contention in parallelism <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>
    *   Process data in chunks <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>
    *   Reuse memory allocations <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>

*   **Apache Arrow Integration**
    [[Polars]] utilizes [[Apache Arrow]] for data transmission, which is a columnar memory format that enables efficient data processing <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>, <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

*   **Lazy and Semi-Lazy Execution**
    [[Polars]] supports both eager and lazy APIs <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. In lazy mode, a query plan is built, but nothing is executed until explicitly requested (e.g., by calling `.collect()`) <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>. This allows [[Polars]] to have the entire context of the query, enabling query optimization and choosing the fastest algorithm <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>, <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This concept is similar to how deep learning frameworks like JAX, PyTorch, and TensorFlow optimize computational graphs <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Performance Benchmarks Against Pandas

Benchmarking demonstrates [[Polars]]' significant performance advantages over [[Pandas]], particularly for larger datasets and complex operations.

### Official Benchmarks

*   **Reading CSV (100 million rows, 7 columns):**
    *   [[Pandas]]: 628 seconds <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>
    *   [[Polars]]: 43 seconds <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>

### Practical Code Comparisons

Using the Iris dataset and a custom large dataset for testing:

*   **Reading CSV (Iris dataset):**
    *   [[Polars]] showed marginally faster performance than [[Pandas]], though sometimes the difference was negligible <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>, <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.

*   **Filtering Operations (Iris dataset):**
    *   [[Polars]] was significantly faster than [[Pandas]] <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.
    *   Using lazy execution for filtering in [[Polars]] provided approximately a 2x speedup compared to eager [[Polars]] on this small dataset <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>, <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.

*   **Filtering and Grouping (Large Custom Dataset - 1 million rows):**
    *   **[[Pandas]]:** Demonstrated single-threaded CPU utilization, where only one CPU core was actively used at a time <a class="yt-timestamp" data-t="00:29:08">[00:29:08]</a>, <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>.
    *   **[[Polars]]:** Showed significant multi-core utilization, engaging all available CPUs for the operation, leading to substantial speedups <a class="yt-timestamp" data-t="00:29:32">[00:29:32]</a>, <a class="yt-timestamp" data-t="00:35:19">[00:35:19]</a>.

*   **Joining DataFrames (Large Custom Dataset - 1 million rows):**
    *   Similar to filtering, [[Pandas]] exhibited single-threaded CPU usage <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>.
    *   [[Polars]] leveraged multiple CPU cores, resulting in faster join operations <a class="yt-timestamp" data-t="00:35:19">[00:35:19]</a>.

## Migration and Usability

The APIs for [[Polars]] and [[Pandas]] are very similar, making the transition between the two libraries relatively straightforward for users <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>, <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>, <a class="yt-timestamp" data-t="00:36:37">[00:36:37]</a>. Tools like ChatGPT are also aware of both [[Pandas]] and [[Polars]] APIs, assisting users in rewriting code and understanding syntax for different operations <a class="yt-timestamp" data-t="00:36:43">[00:36:43]</a>.

This makes [[Polars]] a highly recommended choice for performance-critical data processing tasks in Python, especially when dealing with large datasets where [[Multithreading and memory efficiency in data manipulation|multi-core utilization]] and [[Optimizing computation in neural rendering|memory efficiency]] are crucial.