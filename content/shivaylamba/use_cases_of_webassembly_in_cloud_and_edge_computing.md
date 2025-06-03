---
title: Use cases of WebAssembly in cloud and edge computing
videoId: fS65mAKFfwc
---

From: [[shivaylamba]] <br/> 

[[introduction_to_webassembly_and_its_benefits | WebAssembly]] is a low-level language similar to assembly, serving as a compilation target for high-performance programming languages like C++, Rust, and Go <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. It allows functions written in these languages to be converted into WebAssembly bytecode, which can run alongside JavaScript in browsers <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This portability and near-native execution speed make [[introduction_to_webassembly_and_its_benefits | WebAssembly]] ideal for highly computational tasks that might be slower if executed with JavaScript <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

While initially designed for the web, [[introduction_to_webassembly_and_its_benefits | WebAssembly]] is now increasingly used outside the web, particularly on servers, in cloud-native environments, and for [[use_of_rust_and_webassembly_for_edge_computing | edge applications]] <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## [[webassembly_support_in_vercel_edge_functions | WebAssembly Support in Vercel Edge Functions]]

Vercel has announced support for [[webassembly_support_in_vercel_edge_functions | WebAssembly at the Edge]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This allows users to import `.wasm` files directly into their applications and run them as [[use_of_rust_and_webassembly_for_edge_computing | Edge Functions]] <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Benefits of WebAssembly on the Edge
*   **Faster Computation and Execution**: [[webassembly_support_in_vercel_edge_functions | WebAssembly]] enables much faster computation compared to traditional JavaScript functions <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>, delivering near-native speed <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This is because it compiles high-performance languages into bytecode <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Reduced Latency**: [[use_of_rust_and_webassembly_for_edge_computing | Edge Functions]] are instantiated from Vercel's global Edge Network, initiating from the nearest geographical location to the user <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. This significantly reduces latency <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   [[security_and_performance_benefits_of_webassembly | **Enhanced Performance and Security**]]: [[introduction_to_webassembly_and_its_benefits | WebAssembly]] can function better and provide higher security compared to running serverless functions in Python or JavaScript <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

### Implementation on Vercel
Languages like C, Rust, C++, Go, or even PHP can be converted into a `.wasm` executable and embedded directly into [[use_of_rust_and_webassembly_for_edge_computing | Edge Functions]] <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
The process typically involves:
1.  Loading the [[introduction_to_webassembly_and_its_benefits | WebAssembly]] file into the repository <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
2.  Instantiating the module within a TypeScript or JavaScript function <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
3.  [[introduction_to_webassembly_and_its_benefits | WebAssembly]] supports a streaming format, allowing execution to begin as data streams in, without waiting for the entire file to load <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

### Examples of WebAssembly on Vercel Edge Functions
*   **Hello World in Rust**: A simple Rust function compiled into a [[introduction_to_webassembly_and_its_benefits | WebAssembly]] executable and loaded into an Edge function <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   **XOR Operation**: Another example provided by Vercel <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
*   **Maze Solver**: A demonstration showed [[introduction_to_webassembly_and_its_benefits | WebAssembly]] performing more than twice as fast as other methods for solving a maze <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.
*   [[building_machine_learning_microservices | **Machine Learning Inference**]]: Future applications could include implementing [[building_machine_learning_microservices | machine learning inference]] directly on edge nodes <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## [[webassembly_integration_with_serverless_functions | WebAssembly in Serverless Functions]]

Beyond Edge Functions, [[introduction_to_webassembly_and_its_benefits | WebAssembly]] can also be used with traditional [[webassembly_integration_with_serverless_functions | serverless functions]] on Vercel <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. Serverless functions are typically dedicated to a particular region, invoked from that region <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

### Wasmtime Runtime
The Wasmtime runtime, an open-source project integrated into the Cloud Native Computing Foundation (CNCF), facilitates running [[webassembly_integration_with_serverless_functions | WebAssembly as serverless functions]] <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   [[comparison_of_webassembly_with_javascript_and_other_programming_languages | WebAssembly]] offers better performance than Python or JavaScript for highly computational tasks in serverless environments <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   It allows [[integration_of_rust_with_nodejs | Rust functions]] to be converted into [[introduction_to_webassembly_and_its_benefits | WebAssembly]] bytecode, which can then be invoked within a serverless function <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

### Use Cases for Serverless Functions
*   **Image Processing**: [[introduction_to_webassembly_and_its_benefits | WebAssembly]] can be used for tasks like grayscaling images rapidly <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
*   **AI Inference**: Complex AI inference, such as using a [[introduction_to_webassembly_and_its_benefits | WebAssembly]] TensorFlow interface for predictions, can be handled efficiently without relying on JavaScript <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. An example using the MobileNet V2 model was demonstrated <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.

## Broader Ecosystem for [[use_of_rust_and_webassembly_for_edge_computing | WebAssembly at the Edge]]
Beyond Vercel, [[introduction_to_webassembly_and_its_benefits | WebAssembly]] is also being used in other [[use_of_rust_and_webassembly_for_edge_computing | edge computing]] platforms and applications, including:
*   Wasmtime <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>
*   IoT devices <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>
*   Krustlet, which integrates Rust with Kubernetes <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>

The [[use_of_rust_and_webassembly_for_edge_computing | WebAssembly ecosystem]] is expanding rapidly beyond its web origins, enabling highly computational, low-latency applications on the edge <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.