---
title: Using Python for data processing with Polars
videoId: jU8Ghp7tRCU
---

From: [[hu-po]] <br/> 

[[polars_data_manipulation_library | Polars]] is a lightning-fast DataFrame library designed for use in Python, primarily for handling tabular data <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. It serves as a modern, high-performance alternative to traditional Python data manipulation tools like Pandas <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Introduction to [[polars_data_manipulation_library | Polars]]

Historically, Pandas has been the most popular framework for dealing with tabular data in Python within data science and machine learning workflows <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. [[polars_data_manipulation_library | Polars]] emerges as a faster alternative, built using the [[rust_programming_language_and_polars | Rust programming language]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

[[rust_programming_language_and_polars | Rust]] is a systems programming language renowned for its focus on safety, performance, and concurrency <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. It aims to provide the speed and control of low-level languages while preventing common programming errors that lead to crashes and security vulnerabilities <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. By leveraging [[rust_programming_language_and_polars | Rust]], [[polars_data_manipulation_library | Polars]] is designed to be memory-efficient and fast, making it an excellent choice for demanding data processing tasks <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

[[polars_data_manipulation_library | Polars]] is built completely in [[rust_programming_language_and_polars | Rust]] and utilizes Apache Arrow for data interchange, which can sometimes introduce dependencies that might affect installation <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Key Features of [[polars_data_manipulation_library | Polars]]

The primary goals of [[polars_data_manipulation_library | Polars]] include:
*   **Lightning-Fast Performance**: Utilizing all available CPU cores for computations <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Optimized Queries**: Reducing unnecessary work and memory allocations <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **Memory Efficiency**: Going to great lengths to reduce random copies, efficiently traverse memory caches, minimize contention in parallelism, process data in chunks, and reuse memory allocations <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This directly addresses common issues in interactive data analysis environments like Jupyter notebooks, where inefficient memory management can significantly slow down workflows <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **Lazy and Semi-Lazy Execution**: Allows users to specify when to execute queries. In lazy mode, a query plan is built, but nothing is executed until explicitly requested via a `.collect()` call <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>. This provides [[polars_data_manipulation_library | Polars]] with the full context of the query, enabling significant [[performance_optimization_in_data_processing_with_polars | optimizations]] and the selection of the fastest algorithms <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. This approach is similar to "just-in-time compilation" seen in machine learning frameworks like JAX, PyTorch, and TensorFlow, where Python code is transformed into a faster, lower-level computational graph <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.

## [[comparison_between_polars_and_pandas | Polars vs. Pandas]]

[[polars_data_manipulation_library | Polars]] provides a DataFrame API that is very similar to Pandas <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>, making it relatively easy for Pandas users to transition. Despite the API similarities, [[polars_data_manipulation_library | Polars]] aims for superior performance, particularly in operations involving large datasets.

A benchmark comparing various data processing solutions for 100 million rows and seven columns showed Pandas taking 628 seconds for a basic query, while [[polars_data_manipulation_library | Polars]] completed it in 43 seconds <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

### API Similarities
Both libraries utilize similar abstractions like Series and DataFrames, and common functions such as `read_csv`, `head`, `tail`, and `sample` exist in both, often with analogous syntax <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>. However, there are subtle differences in API calls, particularly for aggregation and filtering operations, which require minor adjustments when migrating code <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

## Practical Application and Performance Testing

To illustrate [[polars_data_manipulation_library | Polars]]'s capabilities, a practical demonstration was conducted covering installation, reading CSV files, data filtering, and joining DataFrames.

### Installation
[[polars_data_manipulation_library | Polars]] can be easily installed using pip: `pip install polars` <a class="yt-timestamp" data-t="00:25:24">[00:25:24]</a>. The installation process is typically straightforward with minimal additional dependencies <a class="yt-timestamp" data-t="00:33:53">[00:33:53]</a>.

### Reading CSV Files
For simple CSV reading operations, [[polars_data_manipulation_library | Polars]] generally shows marginal speed improvements over Pandas, or sometimes a comparable performance, indicating it's "a wash" for smaller datasets <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.

### Data Filtering and Grouping
When performing more complex operations like filtering and grouping, [[polars_data_manipulation_library | Polars]] demonstrates significant speed advantages. Using a 100-million-row dataset, a filtering and grouping operation showed [[polars_data_manipulation_library | Polars]] being an order of magnitude faster than Pandas <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>.

#### CPU Utilization
A key factor in [[polars_data_manipulation_library | Polars]]'s [[performance_optimization_in_data_processing_with_polars | performance]] is its ability to utilize multiple CPU cores. During Pandas operations, often only a single CPU core is fully utilized, leaving others idle <a class="yt-timestamp" data-t="00:29:08">[00:29:08]</a>. In contrast, [[polars_data_manipulation_library | Polars]] intelligently distributes work across all available cores, leading to much higher CPU utilization and faster execution times <a class="yt-timestamp" data-t="00:29:32">[00:29:32]</a>.

### Joining DataFrames
Similar [[performance_optimization_in_data_processing_with_polars | improvements]] were observed when joining two large DataFrames (e.g., 1 million rows). Pandas again showed single-threaded operation, whereas [[polars_data_manipulation_library | Polars]] leveraged multiple cores, resulting in a noticeable speed-up <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>.

### Lazy vs. Eager API
[[polars_data_manipulation_library | Polars]] offers both eager and lazy execution APIs. While the eager API is straightforward for line-by-line execution, the lazy API allows for query optimization before execution, potentially offering further [[performance_optimization_in_data_processing_with_polars | performance]] gains, especially for complex operations. Converting an eager query to lazy often involves adding `.lazy()` at the start and `.collect()` at the end <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>. On smaller datasets, the lazy API might provide about a 2x speedup for filtering, but its full benefits are more apparent with larger datasets where its query optimization capabilities can be fully leveraged <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.

## Conclusion

[[polars_data_manipulation_library | Polars]] appears to be a strong contender for data processing in Python, offering significant speed improvements over Pandas, particularly for filtering, grouping, and joining large datasets <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. Its [[rust_programming_language_and_polars | Rust]] backend enables efficient multi-core utilization and memory management, crucial for [[performance_optimization_in_data_processing_with_polars | performance optimization in data processing with Polars]].

The API similarities to Pandas make it relatively easy for existing users to adopt, and the availability of AI tools like ChatGPT can assist in translating Pandas syntax to [[polars_data_manipulation_library | Polars]] API calls <a class="yt-timestamp" data-t="00:36:47">[00:36:47]</a>.

Example code used in this demonstration is available on the "better" repo on GitHub <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.