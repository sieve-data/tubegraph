---
title: Polars data manipulation library
videoId: jU8Ghp7tRCU
---

From: [[hu-po]] <br/> 

Polars is a high-performance DataFrame library for [[Using Python for data processing with Polars | Python]] that specializes in processing tabular data quickly <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It is designed to be a faster alternative to [[Comparison between Polars and Pandas | Pandas]], a widely used framework for data science and machine learning workflows in [[Using Python for data processing with Polars | Python]] <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Core Features and Advantages

Polars is primarily written in [[Rust programming language and Polars | Rust]], a systems programming language known for its focus on safety, performance, and concurrency <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This choice of language allows Polars to achieve speed and control comparable to low-level languages like C and C++ <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

Key features contributing to Polars' [[performance_optimization_in_data_processing_with_polars | performance optimization]]:
*   **Lightning-Fast DataFrames**: Designed for speed, leveraging all available CPU cores through multi-threading or multi-processing <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Memory Efficiency**: Polars is engineered to be memory efficient, minimizing unnecessary memory allocations and data copies <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. It optimizes queries to reduce unneeded work and efficiently manages memory cache <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Parallelism**: Unlike libraries like Dask, which parallelize existing single-threaded libraries, Polars is built from the ground up to process data in chunks and reuse memory allocations, minimizing contention in parallel operations <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Lazy and Eager Execution**: Polars offers both eager and lazy APIs <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. The eager API allows for line-by-line execution similar to a standard [[Using Python for data processing with Polars | Python]] script. The lazy API, when initiated with `.lazy()` and ended with `.collect()`, builds an optimized query plan before execution <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>. This allows Polars to perform query optimizations, reorder operations, and choose the fastest algorithms based on the entire query context <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

## Comparison with Pandas

Polars aims to provide a DataFrame API similar to [[Comparison between Polars and Pandas | Pandas]], making it relatively easy for [[Comparison between Polars and Pandas | Pandas]] users to transition <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. Both libraries use similar abstractions like Series and DataFrames, and support reading/writing various file formats such as CSV, JSON, and Parquet <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.

### Performance Benchmarks
Benchmarking shows Polars generally outperforms [[Comparison between Polars and Pandas | Pandas]], especially for complex data processing tasks:
*   **CSV Reading**: For a small CSV file (Iris dataset), Polars was marginally faster than [[Comparison between Polars and Pandas | Pandas]] <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
*   **Filtering Operations**: When performing filtering, grouping, and aggregation on a small dataset (Iris dataset), Polars was significantly faster than [[Comparison between Polars and Pandas | Pandas]], showing an order of magnitude improvement <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. The lazy API of Polars can further improve performance for such operations <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.
*   **Large Dataframes (Filtering & Joining)**: For operations on large datasets (e.g., 1 million rows), Polars demonstrates its superior performance by effectively utilizing multiple CPU cores <a class="yt-timestamp" data-t="00:29:32">[00:29:32]</a>. In contrast, [[Comparison between Polars and Pandas | Pandas]] operations are typically limited to single CPU utilization, leading to slower execution times <a class="yt-timestamp" data-t="00:29:08">[00:29:08]</a>. This multi-core utilization is a key advertised feature of Polars <a class="yt-timestamp" data-t="00:29:57">[00:29:57]</a>.

### API Similarities and Differences
While the APIs are similar, there are minor differences. For example, filtering syntax might vary, and [[Comparison between Polars and Pandas | Pandas]] often requires setting an index for certain operations like joins <a class="yt-timestamp" data-t="00:31:27">[00:31:27]</a>. Generative AI tools like ChatGPT are capable of assisting with these API differences, providing equivalent code snippets for both Polars and [[Comparison between Polars and Pandas | Pandas]] <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

## Installation and Basic Usage

To get started with Polars, you can install it using pip:
```bash
pip install polars <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>
```
The common import convention is `import polars as pl` <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

### Example: Reading CSV, Filtering, and Grouping
```python
import polars as pl
import time

# --- Using eager API ---
start_time = time.time()
df = pl.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv") <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>
filtered_df = df.filter(pl.col("sepal.length") > 5.0).group_by("species").agg(pl.all().sum()) <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>
eager_duration = time.time() - start_time

# --- Using lazy API ---
start_time = time.time()
ldf = pl.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv").lazy() <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>
lazy_filtered_df = ldf.filter(pl.col("sepal.length") > 5.0).group_by("species").agg(pl.all().sum()).collect() <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>
lazy_duration = time.time() - start_time

print(f"Eager API duration: {eager_duration:.4f} seconds")
print(f"Lazy API duration: {lazy_duration:.4f} seconds")
```
For local files, `scan_csv` or `lazy_csv_reader` can be used for lazy operations <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

## Conclusion
Polars provides a robust and significantly faster alternative to [[Comparison between Polars and Pandas | Pandas]] for [[Using Python for data processing with Polars | Python]] data manipulation, especially when dealing with large datasets and operations that can benefit from multi-core processing <a class="yt-timestamp" data-t="00:36:36">[00:36:36]</a>. Its [[Rust programming language and Polars | Rust]] backend ensures high performance and memory efficiency, while its largely familiar API makes it an accessible tool for data professionals <a class="yt-timestamp" data-t="00:36:39">[00:36:39]</a>.