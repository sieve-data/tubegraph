---
title: Performance optimization in data processing with Polars
videoId: jU8Ghp7tRCU
---

From: [[hu-po]] <br/> 

[[polars_data_manipulation_library | Polars]] is a high-[[performance_analysis_and_benchmarks | performance]] data frame library for [[using_python_for_data_processing_with_polars | Python]] that specializes in processing tabular data at high speeds <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It serves as a faster alternative to [[comparison_between_polars_and_pandas | Pandas]], a widely used framework in data science and machine learning workflows <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. [[polars_data_manipulation_library | Polars]] is written in [[rust_programming_language_and_polars | Rust]], a systems programming language known for its focus on safety, [[performance_analysis_and_benchmarks | performance]], and concurrency <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Core Design Principles and [[optimization_techniques_in_surfels | Optimization]]

[[polars_data_manipulation_library | Polars]] is engineered to be highly [[memory_and_computational_efficiency_in_pointbased_methods | memory efficient]] and fast, making it an excellent choice for demanding data processing tasks <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. Its primary goals include:
*   Providing a lightning-fast data frame library <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   Utilizing all available CPU cores (multi-threading/multi-processing) <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>, <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.
*   Optimizing queries to minimize unnecessary work and [[memory_and_computational_efficiency_in_pointbased_methods | memory allocation]] <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   Reducing random data copies <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   Traversing the memory cache efficiently <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   Minimizing contention in parallelism <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   Processing data in chunks and reusing [[memory_and_computational_efficiency_in_pointbased_methods | memory allocations]] <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

Unlike libraries such as Dask, which parallelize existing single-threaded libraries like NumPy and [[comparison_between_polars_and_pandas | Pandas]], [[polars_data_manipulation_library | Polars]] is built from the ground up for concurrent operations <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### Lazy and Eager Execution
[[polars_data_manipulation_library | Polars]] supports both eager and lazy API models <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>, <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>. The eager API allows for line-by-line execution, similar to scripting <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. The lazy API, however, builds a query plan without immediate execution, allowing [[polars_data_manipulation_library | Polars]] to optimize the query and choose the fastest algorithm based on the entire context before execution <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>, <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. This concept is similar to [[performance_and_efficiency_in_machine_learning_models | machine learning]] frameworks like JAX, PyTorch, and TensorFlow, which also implement lazy and semi-lazy paradigms for [[optimization_techniques_in_surfels | optimizing]] compute graphs <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## [[performance_analysis_and_benchmarks | Performance Analysis and Benchmarks]]

[[polars_data_manipulation_library | Polars]] is designed for superior [[performance_analysis_and_benchmarks | performance]]. An H2O.ai DB Benchmark demonstrated that [[polars_data_manipulation_library | Polars]] could complete a task involving 100 million rows and seven columns in 43 seconds, compared to [[comparison_between_polars_and_pandas | Pandas]]'s 628 seconds <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>, <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

### Practical Comparisons

When performing operations like reading CSV files, filtering, and joining data frames, [[polars_data_manipulation_library | Polars]] consistently demonstrates better [[performance_analysis_and_benchmarks | performance]]:

*   **CSV Reading**: For small CSV files like the Iris dataset, [[polars_data_manipulation_library | Polars]] showed a marginal, yet noticeable, speed advantage over [[comparison_between_polars_and_pandas | Pandas]] <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>, <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
*   **Data Frame Filtering**: For filtering operations, especially on larger datasets, [[polars_data_manipulation_library | Polars]] was significantly faster, often showing an order of magnitude improvement compared to [[comparison_between_polars_and_pandas | Pandas]] <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>, <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>. The lazy API can further enhance this [[performance_analysis_and_benchmarks | performance]] <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.
*   **CPU Utilization**: A key reason for [[polars_data_manipulation_library | Polars]]'s superior [[performance_analysis_and_benchmarks | performance]] is its ability to utilize multiple CPU cores <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>. While [[comparison_between_polars_and_pandas | Pandas]] typically utilizes only one CPU at a time for operations, [[polars_data_manipulation_library | Polars]] actively uses all available CPUs, leading to much higher utilization and faster execution times <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>, <a class="yt-timestamp" data-t="00:29:31">[00:29:31]</a>.
*   **Joining Data Frames**: Similar [[performance_analysis_and_benchmarks | improvements]] are observed in join operations, where [[polars_data_manipulation_library | Polars]] again leverages multi-core processing to outperform [[comparison_between_polars_and_pandas | Pandas]]'s single-threaded approach <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>, <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>.

## API Similarities and Differences

[[polars_data_manipulation_library | Polars]] offers an API that is very similar to [[comparison_between_polars_and_pandas | Pandas]], making it relatively easy for existing [[comparison_between_polars_and_pandas | Pandas]] users to transition <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>, <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. Both libraries use similar abstractions like Series and DataFrames, and common functions like `read_csv`, `head`, and `tail` exist in both <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>, <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>, <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.

However, there are subtle differences in syntax and behavior. For example, filtering syntax, aggregate calls, and the handling of data frame indices during joins can differ <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>, <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>, <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>, <a class="yt-timestamp" data-t="00:31:25">[00:31:25]</a>. Notably, advanced AI tools like ChatGPT are aware of both [[comparison_between_polars_and_pandas | Pandas]] and [[polars_data_manipulation_library | Polars]] APIs and can assist in converting code or providing correct syntax for different operations <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>, <a class="yt-timestamp" data-t="00:36:43">[00:36:43]</a>.

## Installation and Usage

To get started with [[polars_data_manipulation_library | Polars]], one can simply install it using pip in a [[using_python_for_data_processing_with_polars | Python]] virtual environment <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>, <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

A simple example involves parsing a CSV file (such as the Iris dataset <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>), filtering it, and performing a group-by operation. The Iris dataset is a classic tabular classification dataset used for organizing plants based on measurements like sepal length, sepal width, petal length, and petal width <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>, <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.