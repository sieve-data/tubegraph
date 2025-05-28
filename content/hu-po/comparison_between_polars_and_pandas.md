---
title: Comparison between Polars and Pandas
videoId: jU8Ghp7tRCU
---

From: [[hu-po]] <br/> 

[[polars_data_manipulation_library | Polars]] is a lightning-fast DataFrame library designed for [[using_python_for_data_processing_with_polars | Python]], offering a high-performance alternative to Pandas for handling tabular data <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Pandas has historically been the most popular framework for tabular data in [[using_python_for_data_processing_with_polars | Python]], widely used in data science and machine learning workflows <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. [[polars_data_manipulation_library | Polars]] aims to provide a faster version of Pandas, built on the [[rust_programming_language_and_polars | Rust programming language]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## The Role of Rust

[[polars_data_manipulation_library | Polars]] is written in [[rust_programming_language_and_polars | Rust]] <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. [[rust_programming_language_and_polars | Rust]] is a systems programming language known for its focus on safety, performance, and concurrency <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. It aims to provide the speed and control of low-level languages while preventing common programming errors <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. This foundation in [[rust_programming_language_and_polars | Rust]] allows [[polars_data_manipulation_library | Polars]] to offer C++-like performance and fine-grained control over operations <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Polars Design Goals and Features

The primary goals of [[polars_data_manipulation_library | Polars]] include <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>:
*   **Lightning-fast data frame processing**: Leveraging all available CPU cores for parallel processing <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Optimized queries**: Reducing unneeded work and memory allocations <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **Memory efficiency**: Minimizing random copies, traversing memory caches efficiently, and reusing memory allocations <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Parallel processing**: Processing data in chunks to maximize parallelism <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

Unlike tools such as Dask, which parallelize existing single-threaded libraries like NumPy and Pandas, [[polars_data_manipulation_library | Polars]] is written from the ground up with parallelism in mind <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## API and Execution Paradigms

### Similarities in API
[[polars_data_manipulation_library | Polars]] offers a DataFrame API that is "very similar" to Pandas <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This similarity extends to common operations like importing (e.g., `import polars as pl` compared to `import pandas as pd`) <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>, reading and writing various file formats (CSV, JSON, Parquet) <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>, and viewing data (e.g., `head()`, `tail()`, `sample()`, `describe()`) <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>. This consistency helps users transition between the two libraries <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

### Differences in API
While generally similar, there are slight API differences, particularly in filtering and aggregation operations <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. For example, Pandas might require specific indexing or lambda functions for certain aggregations, whereas [[polars_data_manipulation_library | Polars]] has its own syntax (e.g., `is_between` in Polars versus `between` in Pandas for date filtering) <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>. ChatGPT can be helpful in translating Python code between Pandas and [[polars_data_manipulation_library | Polars]] APIs <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

### Eager vs. Lazy Execution
[[polars_data_manipulation_library | Polars]] supports both eager and lazy execution <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   **Eager Execution**: Allows line-by-line execution, similar to a standard [[using_python_for_data_processing_with_polars | Python]] script, which is convenient for interactive workflows <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Lazy Execution**: Builds a query plan, which is optimized and reordered before execution <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. Nothing is executed until explicitly requested (e.g., with `.collect()`) <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>. This allows [[polars_data_manipulation_library | Polars]] to have the "entire context of the query," enabling better optimizations and algorithm selection <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. This paradigm is similar to how modern deep learning frameworks like Jax, PyTorch, and [[comparison_between_tensorflow_and_pytorch | TensorFlow]] handle computation graphs, allowing for both immediate execution and optimized compilation <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

## Performance Comparison

### Benchmarks
[[polars_data_manipulation_library | Polars]] is advertised as "one of the best performing solutions available" <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
A benchmark involving 100 million rows and seven columns showed [[polars_data_manipulation_library | Polars]] completing a query in 43 seconds, compared to Pandas' 628 seconds <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

### CSV Reading
Initial tests for reading CSV files revealed that [[polars_data_manipulation_library | Polars]] is marginally faster than Pandas, though often appearing as "basically a wash" on smaller datasets <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.

### Data Filtering
For filtering operations, [[polars_data_manipulation_library | Polars]] demonstrated a "significantly faster" performance compared to Pandas <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. When running a filtering operation on a large dataset (millions of rows), Pandas was observed to utilize primarily a single CPU core <a class="yt-timestamp" data-t="00:29:08">[00:29:08]</a>. In contrast, [[polars_data_manipulation_library | Polars]] showed much higher CPU utilization across multiple cores, indicating its ability to leverage parallel processing <a class="yt-timestamp" data-t="00:29:32">[00:29:32]</a>.

### Join Operations
Similar performance gains were observed during join operations on large dataframes. Pandas again demonstrated single-threaded behavior, with only one CPU core peaking <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>. [[polars_data_manipulation_library | Polars]], however, utilized all available CPUs more efficiently, leading to a noticeable speed-up <a class="yt-timestamp" data-t="00:35:21">[00:35:21]</a>.

### Lazy Execution Performance
For small datasets, applying lazy execution to filtering operations in [[polars_data_manipulation_library | Polars]] yielded about a 2x speed-up compared to eager execution, but not a full order of magnitude <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>. For larger datasets, lazy execution might further optimize queries, although the immediate impact can vary.

## Installation and Setup

Installing [[polars_data_manipulation_library | Polars]] is straightforward using pip (`pip install polars`) <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. It generally installs with minimal additional dependencies, primarily `typing` <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. [[polars_data_manipulation_library | Polars]] also utilizes the Apache Arrow format internally <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Conclusion

[[polars_data_manipulation_library | Polars]] appears to be a compelling alternative to Pandas, especially for performance-critical data processing tasks <a class="yt-timestamp" data-t="00:36:36">[00:36:36]</a>. Its [[rust_programming_language_and_polars | Rust]] backend enables significant speed improvements and better utilization of multi-core CPUs, particularly for operations like filtering and joining <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>. While there are minor API differences, the overall syntax is very similar to Pandas, making the learning curve manageable. Furthermore, the availability of both eager and lazy execution paradigms offers flexibility and opportunities for query optimization, echoing trends in modern machine learning frameworks <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.