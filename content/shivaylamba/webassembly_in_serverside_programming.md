---
title: WebAssembly in ServerSide Programming
videoId: TGDuiddxoE8
---

From: [[shivaylamba]] <br/> 

This article discusses how to achieve [[improving_nodejs_performance | high performance in Node.js]] applications using [[use_of_rust_and_webassembly_for_edge_computing | Rust and WebAssembly]], particularly in server-side environments <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

## The Need for Software Performance Improvement

Historically, hardware performance has seen exponential growth, following Moore's Law, with chips becoming increasingly smaller <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. However, there's a physical limit to how many transistors can be packed into a small space <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This has led to a "plattering effect" in performance gains from hardware over the past few years <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

Consequently, to improve overall system performance, the focus must shift equally to software optimization <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. This optimization must be done in a safe and secure manner, without compromising the system's security and overall capabilities <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. [[security_and_performance_benefits_of_webassembly | WebAssembly]] offers a highly secure environment for improving Node.js performance <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

## Why Rust for Node.js Performance?

When considering low-level languages for performance, C++ is a common choice, having been around for over 20-25 years <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. Rust, while newer (around 5-6 years old), is actively maintained by Mozilla and offers significant advantages over C++ <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

One of Rust's biggest strengths is its robust error handling and [[security_and_performance_benefits_of_webassembly | security features]], particularly in memory management <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. C++ is known for issues related to memory management and pointers, which Rust addresses inherently <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. In terms of raw performance, both Rust and C++ are equally capable <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. This makes Rust a preferred language for [[integration_of_rust_with_nodejs | integrating with Node.js]] to offload computationally intensive tasks <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

## What is WebAssembly?

[[introduction_to_webassembly_and_its_benefits | WebAssembly]] (Wasm) is a binary instruction format designed for a virtual machine <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. It is generated when languages like C++, C, or Rust are compiled <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. WebAssembly operates at the machine level, dealing directly with machine code <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

### WebAssembly vs. JavaScript

[[comparison_of_webassembly_with_javascript_and_other_programming_languages | WebAssembly is not intended to replace JavaScript]]; in fact, it cannot perform actions independently <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Instead, it augments JavaScript's capabilities, especially for highly computational tasks <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. For example, tasks like video editing, machine learning inference, or running large models on the web, which are difficult with standard JavaScript, become possible with WebAssembly <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. This is achieved by converting low-level programs (e.g., C++, Rust) that interact directly with the CPU and GPU into WebAssembly, which can then be combined with JavaScript <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

### WebAssembly Beyond the Browser

A common misconception is that WebAssembly is limited to the web browser <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. However, [[use_cases_of_webassembly_in_cloud_and_edge_computing | WebAssembly's applications extend far beyond the browser]], including:
*   **IoT (Internet of Things)** <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>
*   **[[use_cases_of_webassembly_in_cloud_and_edge_computing | Edge Computing]]** <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>
*   **Server-side applications** <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>

This makes it an excellent choice for constrained environments <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

## The Role of WasmEdge Runtime

To run WebAssembly applications, a runtime is required <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. WasmEdge is an open-source project incubated by the CNCF (Cloud Native Computing Foundation) that serves as a runtime for deploying and running WebAssembly applications <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

WasmEdge's popularity stems from its use of ahead-of-time (AOT) compilation, making it one of the fastest WebAssembly runtimes available <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. Crucially, it also provides a highly secure environment for execution <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

## Integrating Rust and WebAssembly with Node.js

To build [[improving_nodejs_performance | highly performant applications]] within Node.js, the strategy involves leveraging JavaScript for its ease of use and wide support, while offloading critical, computationally intensive tasks to Rust <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. This Rust code then runs securely within a WebAssembly virtual machine <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

### Architecture

In a standard Node.js application, the JavaScript code runs on the V8 engine, which uses C++ in the backend <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. For this integrated approach:
*   Regular Node.js tasks continue to use the standard Node.js environment <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
*   [[use_cases_of_webassembly_in_cloud_and_edge_computing | Highly computational tasks]] are processed by a WebAssembly virtual machine <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

Consider a Node.js application performing machine learning inference <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. The inference code itself isn't handled directly by JavaScript or Node.js <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. Instead, Node.js defines API calls that invoke a Rust function responsible for the computational task <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. For example, Node.js handles input parameters (like an image for classification), while the ML inference code is written in Rust <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.

This Rust function is then wrapped inside the WebAssembly virtual machine <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. When Node.js calls the Rust function, the Rust code is converted into WebAssembly bytecode (.wasm) <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. This bytecode executes within the WebAssembly VM, sends the response back to the Node.js server, which can then display it on a front-end application <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

WebAssembly inherently supports accessing hardware resources like GPUs, TPUs, or CPUs, which are essential for high-performance computing tasks <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. Additionally, WASI (WebAssembly System Interface) provides APIs that allow WebAssembly modules to interact with operating system-related tasks, such as file systems or network resources <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.

In essence, the Node.js function becomes a caller for the Rust function, which performs the heavy lifting, gets converted to WebAssembly bytecode, and returns the result <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>.

### Benefits in Edge Computing and Serverless

This architecture is particularly beneficial for [[use_cases_of_webassembly_in_cloud_and_edge_computing | edge computing]] and [[webassembly_integration_with_serverless_functions | serverless functions]], especially on resource-constrained edge devices <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>:

*   **Small Footprint**: A WebAssembly container has a significantly smaller footprint compared to a standard Linux container <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. While a Linux container might be 10-30 MB, a WebAssembly container can be 20 to 1000 times smaller <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
*   **Fast Startup Time**: Standard Linux containers can take 10 milliseconds to several minutes to start, depending on dependencies <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. A WebAssembly container, however, starts almost instantly, within nanoseconds to microseconds <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

These characteristics make this architecture ideal for [[webassembly_support_in_vercel_edge_functions | edge-based applications]] like machine learning on the edge, smart contracts, decentralized applications, and microservices on low-power devices <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

## Getting Started

To get started with this setup, you need to install the following dependencies:
*   **Rust**: For writing the high-performance code <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.
*   **Node.js**: For the main application <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.
*   **WasmEdge Runtime**: The runtime for deploying and running WebAssembly applications <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.
*   **Rust Wasm Compiler Tools**: Responsible for converting Rust code into WebAssembly bytecode <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.
    *   WasmEdge is supported across all major operating systems, with best support on Linux <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

### Starter Code Example

A simple starter code repository can be cloned to begin <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.
The example demonstrates a Node.js function sending a string to a Rust function, which then appends "hello" to it <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>.

#### Rust Function (`src/lib.rs`)

```rust
// Example of a simple Rust function
// The 'wasm_bindgen' attribute is crucial for WebAssembly conversion
#[wasm_bindgen]
pub fn say(name: &str) -> String {
    format!("Hello, {}!", name)
}
```
The `#[wasm_bindgen]` attribute indicates which functions should be converted into WebAssembly bytecode <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>. This is where more complex functions, like a machine learning inference function, would be defined <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.

#### Node.js Application (`node/app.js`)

```javascript
// This file is generated by the WasmEdge project compiler tools
// It acts as a bridge between Node.js and the WebAssembly module
import { say } from 'wasmedge-node-starter'; // This is an auto-generated library <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>

// Main Node.js program
const http = require('http');
const port = 3000;

const server = http.createServer((req, res) => {
    // Extract name from request, e.g., query parameter
    const url = new URL(req.url, `http://localhost:${port}`);
    const name = url.searchParams.get('name') || 'World';

    // Call the Rust function via the generated JavaScript wrapper
    const greeting = say(name); <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>

    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end(greeting);
});

server.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
    console.log(`Try: http://localhost:${port}/?name=NodeJS`);
});
```

When the Rust program is compiled, it generates a `.wasm` WebAssembly executable and a JavaScript starter code file (e.g., `wasmedge-node-starter.js`) <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>. This generated JavaScript code acts as the interface for your main Node.js program to interact with the WebAssembly module <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.