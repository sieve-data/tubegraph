---
title: Installing and setting up TypeScript with NPM
videoId: ahCwqrYpIuM
---

From: [[fireship]] <br/> 

[[introduction_to_typescript | TypeScript]] is a tool that can significantly impact a web developer's productivity <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. It functions as a superset of JavaScript, meaning any valid JavaScript code is also valid in [[introduction_to_typescript | TypeScript]] <a class="yt-timestamp" data-t="01:26:06">[01:26:06]</a>. This allows for incremental learning and the use of future JavaScript features that can be transpiled for current environments <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

One of the biggest benefits of [[introduction_to_typescript | TypeScript]] is its tooling, especially within IDEs like VS Code <a class="yt-timestamp" data-t="00:54:27">[00:54:27]</a>. When using [[type_annotations_and_strong_typing_in_typescript | type annotations]] or working with [[type_annotations_and_strong_typing_in_typescript | strongly typed languages]], code is automatically documented in the IDE, reducing the need to refer to online documentation <a class="yt-timestamp" data-t="00:59:08">[00:59:08]</a>. The compiler can also catch bugs in advance, making code refactoring more efficient <a class="yt-timestamp" data-t="01:09:28">[01:09:28]</a>.

## Installation

To get started with [[introduction_to_typescript | TypeScript]], install it globally using Node Package Manager (NPM) <a class="yt-timestamp" data-t="01:46:27">[01:46:27]</a>:

```bash
npm install -g typescript
```

This command provides access to the `tsc` command, which runs the [[using_typescript_compiler_and_setting_ts_config | TypeScript compiler]] <a class="yt-timestamp" data-t="01:50:27">[01:50:27]</a>.

## Compiling TypeScript Code

[[introduction_to_typescript | TypeScript]] code cannot run on its own in environments like browsers or Node.js <a class="yt-timestamp" data-t="02:02:40">[02:02:40]</a>. Instead, the [[using_typescript_compiler_and_setting_ts_config | TypeScript compiler]] is used to convert the [[introduction_to_typescript | TypeScript]] code into vanilla JavaScript <a class="yt-timestamp" data-t="02:09:07">[02:09:07]</a>.

For example, to compile an `index.ts` file:

```bash
tsc index.ts
```

This command will generate an `index.js` file, which contains the compiled JavaScript code runnable in a browser or Node <a class="yt-timestamp" data-t="02:23:07">[02:23:07]</a>. If the `.ts` file contains plain JavaScript, the compiled `.js` file will be identical <a class="yt-timestamp" data-t="02:30:37">[02:30:37]</a>.

By default, [[introduction_to_typescript | TypeScript]] compiles to ES3 <a class="yt-timestamp" data-t="02:36:27">[02:36:27]</a>. This means if you write modern JavaScript features like `async/await`, the compiler will transpile them into more complex JavaScript to ensure compatibility with older environments <a class="yt-timestamp" data-t="02:41:27">[02:41:27]</a>.

## Configuring the TypeScript Compiler

The [[using_typescript_compiler_and_setting_ts_config | TypeScript compiler]] is highly sophisticated and offers many options to customize its behavior <a class="yt-timestamp" data-t="02:53:30">[02:53:30]</a>. While options can be passed via the command line, the standard approach is to create a `tsconfig.json` file <a class="yt-timestamp" data-t="03:00:27">[03:00:27]</a>. This file is automatically detected and used when `tsc` is run <a class="yt-timestamp" data-t="03:06:05">[03:06:05]</a>.

Although `tsconfig.json` can seem overwhelming, only a few options are typically needed <a class="yt-timestamp" data-t="03:09:27">[03:09:27]</a>.

### Key Configuration Options

*   **`target`**: This option specifies the JavaScript flavor your code will be compiled to <a class="yt-timestamp" data-t="03:15:20">[03:15:20]</a>. For example, setting `target` to `esnext` will allow [[introduction_to_typescript | TypeScript]] to compile modern features like `async/await` natively, as it targets the latest JavaScript version <a class="yt-timestamp" data-t="03:20:27">[03:20:27]</a>.

    ```json
    {
      "compilerOptions": {
        "target": "esnext"
      }
    }
    ```

*   **`watch`**: Setting this option to `true` (`"watch": true`) will automatically recompile your code every time a file is saved <a class="yt-timestamp" data-t="03:32:07">[03:32:07]</a>, eliminating the need to manually run the `tsc` command after every change <a class="yt-timestamp" data-t="03:37:37">[03:37:37]</a>.

*   **`lib`**: This option allows you to automatically include typings for specific environments, such as the DOM or ES2017 <a class="yt-timestamp" data-t="03:43:08">[03:43:08]</a>. For web applications, including the `Dom` library enables [[introduction_to_typescript | TypeScript]] to compile code with native DOM classes without errors <a class="yt-timestamp" data-t="03:50:07">[03:50:07]</a>. This provides autocomplete and Intellisense for DOM-related objects, along with integrated documentation and error messages <a class="yt-timestamp" data-t="04:00:27">[04:00:27]</a>.

    ```json
    {
      "compilerOptions": {
        "lib": ["esnext", "dom"]
      }
    }
    ```

## [[integrating_thirdparty_libraries_with_typescript | Integrating Third-Party Libraries]]

When using third-party libraries, some, like Firebase, ship with type declarations automatically <a class="yt-timestamp" data-t="04:40:27">[04:40:27]</a>. However, others, such as Lodash, do not <a class="yt-timestamp" data-t="04:44:27">[04:44:27]</a>. If a library lacks type declarations, [[introduction_to_typescript | TypeScript]] will issue a warning and not provide autocomplete or Intellisense <a class="yt-timestamp" data-t="04:48:27">[04:48:27]</a>.

Fortunately, a large mono-repository exists with community-maintained type declarations for many libraries <a class="yt-timestamp" data-t="04:58:07">[04:58:07]</a>. These can be installed as development dependencies:

```bash
npm install --save-dev @types/lodash
```

Installing these types will provide full autocomplete and Intellisense for the library's functions <a class="yt-timestamp" data-t="05:02:07">[05:02:07]</a>.