---
title: WebAssembly integration with serverless functions
videoId: fS65mAKFfwc
---

From: [[shivaylamba]] <br/> 

[[Introduction to WebAssembly and its benefits | WebAssembly]] (Wasm) is a low-level language, similar to assembly, that serves as a compilation target for high-performance programming languages like C++, [[Use of Rust and WebAssembly for Edge Computing | Rust]], Go, and PHP <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a> <a class="yt-timestamp" data-t="03:03:03">[03:03:03]</a>. It allows functions written in these languages to be converted into WebAssembly bytecode, which can run efficiently in various environments <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

Key characteristics of [[Introduction to WebAssembly and its benefits | WebAssembly]] include:
*   **Portability:** Highly portable <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Performance:** Runs at near-native speed <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Efficiency:** Useful for highly computational tasks or processes that might be slower if run with JavaScript <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## WebAssembly Beyond the Web

While initially designed for browsers, [[WebAssembly in ServerSide Programming | WebAssembly]] is now increasingly used outside the web, particularly in [[use_cases_of_WebAssembly_in_cloud_and_edge_computing | cloud and edge computing]] environments <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a> <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This includes running on servers, in cloud-native spaces, and as part of edge applications <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## WebAssembly with Vercel Edge Functions

[[WebAssembly support in Vercel Edge Functions | Vercel]] has announced support for running [[WebAssembly support in Vercel Edge Functions | WebAssembly]] executables directly as [[WebAssembly support in Vercel Edge Functions | Edge Functions]] <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a> <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This integration allows for much faster computation and benefits from the low-latency execution environment of [[WebAssembly support in Vercel Edge Functions | Vercel Edge Functions]] <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### Benefits of WebAssembly on Edge Functions
*   **Faster Execution:** Provides much faster execution compared to traditional JavaScript or Python serverless functions, especially for highly computational tasks <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a> <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   **Increased Security:** Offers higher [[security_and_performance_benefits_of_webassembly | security]] compared to running serverless functions in Python or JavaScript <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **Low Latency:** Edge Functions are instantiated from the nearest geographical [[WebAssembly support in Vercel Edge Functions | Edge Network]] node, significantly reducing cold start times and latency <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a> <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

### Implementation on Vercel
To implement, [[WebAssembly]] files (`.wasm` files) are imported into an application and run on [[WebAssembly support in Vercel Edge Functions | Edge Functions]] <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. The process typically involves:
1.  Loading the [[WebAssembly]] file into the repository <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
2.  Instantiating the [[WebAssembly]] module within a TypeScript or JavaScript function <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a> <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
[[WebAssembly]] uses a streaming format, allowing execution to begin as soon as data streams are received, without waiting for the entire file to load <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

An example provided by Vercel showcases compiling a simple [[Use of Rust and WebAssembly for Edge Computing | Rust]] "hello world" function into a [[WebAssembly]] executable and loading it into an [[WebAssembly support in Vercel Edge Functions | Edge Function]] <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

## WebAssembly with General Serverless Functions

[[WebAssembly]] can also be utilized with traditional serverless functions (Function-as-a-Service) <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. While Python and JavaScript are common for serverless functions, [[WebAssembly]] offers a better solution for specific use cases, especially those involving [[Security and Performance Benefits of WebAssembly | highly computational tasks]] <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a> <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

### Wasmtime Runtime
The Wasmtime runtime, an open-source project integrated into the CNCF (Cloud Native Computing Foundation), facilitates running [[WebAssembly]] as serverless functions <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. This runtime is responsible for taking input, executing the [[WebAssembly]] bytecode, and sending out the output <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

## Use Cases
The integration of [[WebAssembly]] with serverless and [[WebAssembly support in Vercel Edge Functions | Edge Functions]] opens up possibilities for various computationally intensive applications:
*   **[[Building machine learning microservices | Machine learning inference]]**: Performing AI inference on edge nodes <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a> <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. For example, a [[Use of Rust and WebAssembly for Edge Computing | Rust]] function running a [[WebAssembly]] TensorFlow interface can perform inference and return prediction labels <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Image Processing**: Tasks like grayscaling an image can be performed very quickly using [[WebAssembly]] serverless functions <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a> <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Complex Computations**: Solving problems like maze solvers where [[WebAssembly]] demonstrates significantly better [[Security and Performance Benefits of WebAssembly | performance]] than other methods <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

## Edge Functions vs. Serverless Functions (Vercel Context)

| Feature            | Serverless Functions (Traditional)                   | [[WebAssembly support in Vercel Edge Functions | Edge Functions]]                                |
| :----------------- | :--------------------------------------------------- | :------------------------------------------- |
| **Region**         | Usually dedicated to a particular region <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a> | Initiated from all different Edge Network locations of Vercel <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a> |
| **Latency**        | May have higher latency if called from far regions   | Initiates from the nearest geographical location to the user, resulting in very low latency <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a> |
| **Use Case**       | General backend logic, APIs                          | Highly computational tasks, low-latency APIs, content manipulation at the edge <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a> |

The ability to run [[WebAssembly]] on both serverless and [[WebAssembly support in Vercel Edge Functions | Edge Functions]] significantly increases its footprint and potential for empowering modern applications <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

## Broader Ecosystem
The [[WebAssembly]] ecosystem is rapidly growing and extends beyond web applications. It's seen in various applications, including [[use_cases_of_WebAssembly_in_cloud_and_edge_computing | edge computing]] (e.g., with Wasmtime and Krustlet for IoT) <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.