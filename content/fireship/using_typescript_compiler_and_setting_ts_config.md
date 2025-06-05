---
title: Using TypeScript compiler and setting TS config
videoId: ahCwqrYpIuM
---

From: [[fireship]] <br/> 

[[Introduction to TypeScript|TypeScript]] is a tool that significantly impacts web developer productivity, even for those initially resistant to learning it <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It acts as a superset of JavaScript, meaning any valid JavaScript code is also valid in [[Introduction to TypeScript|TypeScript]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This allows for incremental learning and the ability to write code using future JavaScript features that can be transpiled for current environments <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

## [[Installing and setting up TypeScript with NPM|Installing the TypeScript Compiler]]

The first step to use [[Introduction to TypeScript|TypeScript]] is to install it globally via NPM <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This provides access to the `tsc` command, which is the [[Using TypeScript compiler and setting TS config|TypeScript compiler]] <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Basic Compilation

[[Introduction to TypeScript|TypeScript]] code cannot run directly in browsers or Node.js <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. The [[Using TypeScript compiler and setting TS config|TypeScript compiler]] (`tsc`) is used to convert this code into vanilla JavaScript <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

To compile a `.ts` file (e.g., `index.ts`):
1.  Write [[Introduction to TypeScript|TypeScript]] code, which can include plain JavaScript <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
2.  Run `tsc index.ts` in the command line <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
3.  This creates an `index.js` file, which is the runnable JavaScript code <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

By default, [[Using TypeScript compiler and setting TS config|TypeScript]] compiles to ES3, which doesn't support modern features like `async/await` <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. If `async/await` is used, the compiler will transpile it into a more complex JavaScript structure to maintain compatibility <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Customizing Compiler Behavior with `tsconfig.json`

The [[Using TypeScript compiler and setting TS config|TypeScript compiler]] is highly sophisticated and offers many options to customize its behavior <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. While options can be passed via the command line, the standard approach is to create a `tsconfig.json` file <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This file is automatically detected and used when `tsc` is run <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

Although `tsconfig.json` can seem overwhelming, only a few options are typically needed <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### Key `tsconfig.json` Options

*   **`target`**: This option specifies the target JavaScript flavor for compilation <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. For example, setting `target` to `esnext` allows the code to compile with native `async/await` support if the target JavaScript version supports it <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **`watch`**: Setting `watch` to `true` will automatically recompile the code every time a file is saved, saving the effort of manually rerunning `tsc` <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **`lib`**: This option allows for automatically including [[Type annotations and strong typing in TypeScript|typings]] for specific environments like the DOM or ES2017 <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. For web applications, including the `Dom` library enables [[Introduction to TypeScript|TypeScript]] to compile code with native DOM classes without errors, providing autocomplete and IntelliSense for these classes <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

## Benefits of Compiler and Config

Using the [[Using TypeScript compiler and setting TS config|TypeScript compiler]] and its configuration provides significant benefits:
*   **Enhanced Tooling**: Integrated documentation and error messages are available directly in the IDE (e.g., VS Code) when working with [[Type annotations and strong typing in TypeScript|type annotations]] or [[Integrating thirdparty libraries with TypeScript|strong-typed libraries]] <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This reduces the need to constantly refer to online documentation <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **Early Bug Detection**: The compiler can catch bugs in advance, making code refactoring much more efficient <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. This prevents "silly errors during development" from becoming "insanity-inducing errors in production" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

Overall, writing a little more code upfront with [[Introduction to TypeScript|TypeScript]] and its compiler features can pay significant dividends as a project grows <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.