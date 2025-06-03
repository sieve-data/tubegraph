---
title: Introduction to WebAssembly and its benefits
videoId: fS65mAKFfwc
---

From: [[shivaylamba]] <br/> 

WebAssembly (Wasm) is a low-level language, similar to how assembly works, serving as a compilation target for high-performance programming languages like C++ or Rust <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. It enables functions written in these languages to be converted into WebAssembly bytecode, which can run on web browsers alongside JavaScript <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This is crucial because C++ or Rust functions are not directly supported in web browsers <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Key Characteristics and Benefits

*   **Portability**: WebAssembly is very portable, running with a binding installation format <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Near-Native Speed**: It executes at near-native speed <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   **Performance**: WebAssembly is highly useful for running computationally intensive tasks that might be slower if executed solely with JavaScript <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. This [[Comparison of WebAssembly with JavaScript and other programming languages | comparison of WebAssembly with JavaScript]] highlights its superior performance for such tasks <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Security**: WebAssembly can provide higher [[security_and_performance_benefits_of_webassembly | security benefits]] compared to running serverless functions in Python or JavaScript <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## WebAssembly Beyond the Web

While initially designed for the web, WebAssembly's utility has expanded significantly beyond the browser <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. It is increasingly used [[WebAssembly in ServerSide Programming | on servers]], in cloud-native environments, and for [[Use cases of WebAssembly in cloud and edge computing | edge applications]] <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Integration with Serverless and Edge Functions

WebAssembly can be run as [[webassembly_integration_with_serverless_functions | serverless functions]] and [[WebAssembly support in Vercel Edge Functions | Edge Functions]] <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

A recent announcement by Vercel introduced direct support for running WebAssembly executables as [[WebAssembly support in Vercel Edge Functions | Edge Functions]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This allows for much faster computation due to the benefits of edge functionality <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

Languages like C, Rust, C++, Go, or even PHP can be converted into a WebAssembly executable (.wasm file) and embedded directly into [[WebAssembly support in Vercel Edge Functions | Edge Functions]] <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

#### Technical Implementation on Vercel

To use WebAssembly with Vercel [[WebAssembly support in Vercel Edge Functions | Edge Functions]]:
1.  Load the WebAssembly file into the repository <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
2.  Instantiate it within a TypeScript or JavaScript function <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
3.  WebAssembly operates in a streaming format, meaning execution can begin as soon as data streams are received, without waiting for the entire file to load <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

An example involves compiling a simple "hello world" Rust function into a WebAssembly executable, which is then loaded into an Edge Function <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

#### Edge Functions vs. Serverless Functions

*   **Serverless Functions**: Typically tied to a particular region <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
*   **Edge Functions**: Instituted across all Vercel's Edge Networks, initiating from the geographically nearest Edge node to the user, significantly reducing latency <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

### WebAssembly Runtimes

Projects like Wasmtime, an open-source WebAssembly runtime integrated with the CNCF (Cloud Native Computing Foundation), demonstrate how WebAssembly can be run as a serverless function <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. This is particularly beneficial for highly computational tasks where WebAssembly can outperform Python or JavaScript <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

## Use Cases and Examples

WebAssembly is suitable for tasks requiring significant computation, such as:
*   Image processing, including grayscale conversions <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   [[use_cases_of_webassembly_in_cloud_and_edge_computing | Machine learning inference]], especially on edge nodes, by offloading the inference logic to WebAssembly runtimes from languages like Rust using libraries such as Wasmtime TensorFlow <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   Complex operations like XOR operations <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   Solving computationally intensive problems like maze solvers, where WebAssembly has demonstrated over twice the performance compared to other methods <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

## Growing Ecosystem

The WebAssembly ecosystem is expanding rapidly, with applications on the edge not limited to Vercel. It is also seen with Wasmer and Krustlet, particularly in areas like IoT <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. The ecosystem is no longer confined to just web applications, but rather spans across diverse computing environments <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.