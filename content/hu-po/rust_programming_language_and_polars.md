---
title: Rust programming language and Polars
videoId: jU8Ghp7tRCU
---

From: [[hu-po]] <br/> 

This article explores [[polars_data_manipulation_library | Polars]], a fast data frame library, and its foundation in the Rust programming language, often drawing comparisons to [[comparison_between_polars_and_pandas | Pandas]] for data manipulation in [[using_python_for_data_processing_with_polars | Python]].

## Introducing Polars

[[polars_data_manipulation_library | Polars]] is described as a "lightning fast data frame library" for [[using_python_for_data_processing_with_polars | Python]] <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Data frames primarily deal with tabular data <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Traditionally, [[comparison_between_polars_and_pandas | Pandas]] has been the most popular framework for tabular data and data processing in [[using_python_for_data_processing_with_polars | Python]], widely used in data science and machine learning workflows <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. [[polars_data_manipulation_library | Polars]] aims to be a faster alternative to [[comparison_between_polars_and_pandas | Pandas]], written in Rust <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Rust Programming Language

Rust is a systems programming language known for its focus on safety, performance, and concurrency <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. It seeks to provide the speed and control of low-level languages while preventing common programming errors that lead to crashes and security vulnerabilities <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. The speaker understands Rust to be a faster version of C <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

[[polars_data_manipulation_library | Polars]] is a data manipulation and analysis library written entirely in Rust <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This choice of language contributes to its speed and performance <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Key Goals and Features of Polars

The primary goals of [[polars_data_manipulation_library | Polars]] include:
*   Providing a "lightning fast data frame library" <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   Utilizing all available CPU cores (multi-threading/multi-process) <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>, <a class="yt-timestamp" data-t="00:30:03">[00:30:03]</a>.
*   Optimizing queries to minimize unneeded work and memory allocation <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   Reducing random copies, efficiently traversing memory caches, minimizing contention in parallelism, processing data in chunks, and reusing memory allocations <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   Leveraging Apache Arrow for data interchange <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

Unlike tools such as Dask, which parallelize existing single-threaded libraries like NumPy and [[comparison_between_polars_and_pandas | Pandas]], [[polars_data_manipulation_library | Polars]] is built from the ground up for performance <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### Lazy and Semi-Lazy Execution

[[polars_data_manipulation_library | Polars]] supports both eager and lazy/semi-lazy execution models <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. The eager API allows line-by-line execution like a [[using_python_for_data_processing_with_polars | Python]] script <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. The lazy API, on the other hand, builds a query plan and executes nothing until explicitly told to `collect` <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>, <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>. This allows [[polars_data_manipulation_library | Polars]] to have the "entire context of the query," enabling better optimizations and choosing the fastest algorithm <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. This concept is similar to how deep learning frameworks like JAX, PyTorch, and TensorFlow optimize code over time by creating a more optimal compute graph <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

The query optimization in [[polars_data_manipulation_library | Polars]] involves keeping track of the query in a logical plan, which is then optimized and reordered before execution, resembling a "just-in-time compilation" process <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

## Performance Benchmarks and Comparisons

[[polars_data_manipulation_library | Polars]] is noted as "one of the best performing solutions available" according to the H2O.ai DB Benchmark <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. For a task involving 100 million rows and seven columns, [[comparison_between_polars_and_pandas | Pandas]] took 628 seconds, while [[polars_data_manipulation_library | Polars]] completed it in 43 seconds <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

Practical demonstrations showcase the performance difference:

*   **Reading CSV:** Reading a small CSV file (Iris dataset) shows [[polars_data_manipulation_library | Polars]] as marginally faster than [[comparison_between_polars_and_pandas | Pandas]] <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>, <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
*   **Filtering DataFrames:** For filtering and grouping operations on the Iris dataset, [[polars_data_manipulation_library | Polars]] is significantly faster than [[comparison_between_polars_and_pandas | Pandas]], showing an order of magnitude improvement <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>, <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>. Using the lazy API for filtering provides a further speed-up, potentially a 2X improvement on smaller datasets <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.
*   **CPU Utilization:** During intensive operations like filtering and joining large dataframes (e.g., 1 million rows), [[comparison_between_polars_and_pandas | Pandas]] typically utilizes only one CPU core <a class="yt-timestamp" data-t="00:29:08">[00:29:08]</a>, whereas [[polars_data_manipulation_library | Polars]] effectively uses multiple CPU cores, demonstrating significant multi-CPU utilization <a class="yt-timestamp" data-t="00:29:32">[00:29:32]</a>, <a class="yt-timestamp" data-t="00:35:19">[00:35:19]</a>. This multi-core usage is a key reason for [[polars_data_manipulation_library | Polars]]'s speed advantage <a class="yt-timestamp" data-t="00:29:57">[00:29:57]</a>.
*   **Joining DataFrames:** Similar performance improvements are observed for join operations, with [[polars_data_manipulation_library | Polars]] leveraging multiple CPUs where [[comparison_between_polars_and_pandas | Pandas]] remains single-threaded <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>.

## Installation and Usage in Python

[[polars_data_manipulation_library | Polars]] can be installed via `pip install polars` <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. The installation process is generally straightforward with few dependencies <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

The API for [[polars_data_manipulation_library | Polars]] is designed to be very similar to [[comparison_between_polars_and_pandas | Pandas]], making it easier for users familiar with [[comparison_between_polars_and_pandas | Pandas]] to adapt <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>, <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. Common operations like `read_csv`, `filter`, `groupby`, `head`, `tail`, `sample`, and `describe` exist in both libraries <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>, <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>. However, there can be slight differences in API calls for specific functionalities, such as `between` for filtering date ranges <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>, <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>.

## AI Assistance for Polars

ChatGPT demonstrates awareness of both [[comparison_between_polars_and_pandas | Pandas]] and [[polars_data_manipulation_library | Polars]] APIs <a class="yt-timestamp" data-t="00:36:47">[00:36:47]</a>. It can provide summaries of what Rust and [[polars_data_manipulation_library | Polars]] are <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, and it can rewrite [[using_python_for_data_processing_with_polars | Python]] code snippets to work with [[comparison_between_polars_and_pandas | Pandas]] when given a [[polars_data_manipulation_library | Polars]] example <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. This capability assists users in transitioning between the two libraries or understanding syntax differences <a class="yt-timestamp" data-t="00:36:50">[00:36:50]</a>.