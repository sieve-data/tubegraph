---
title: Type annotations and error checking in TypeScript
videoId: ahCwqrYpIuM
---

From: [[fireship]] <br/> 

## Introduction
[[benefits_of_using_typescript_for_web_development | TypeScript]] has significantly impacted developer productivity, even for those initially resistant to learning it <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It became a necessary tool when working with client projects requiring Angular apps <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Although it might require writing a little more code upfront, this investment pays off as a project grows <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

A valuable resource for advanced TypeScript concepts is the free and open-source "TypeScript Deep Dive" book by Basarat Syed <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Core Benefits

### Enhanced Tooling and Automatic Documentation
The biggest advantage of TypeScript comes from its tooling integration within IDEs like VS Code <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. When using type annotations or working with strongly typed libraries, code is automatically documented in the IDE <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. This reduces the need to consult online documentation for libraries <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Early Bug Detection
The TypeScript compiler can catch bugs in advance, which is a more efficient way to refactor code <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. As famously put in a Reddit post: "Would you rather have silly errors during development or insanity inducing errors in production?" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Incremental Learning and Future JavaScript Features
TypeScript has virtually no learning curve if you already know JavaScript, as it is a superset of JavaScript; any valid JavaScript code is also valid TypeScript <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This allows for incremental learning <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. It also enables developers to write code using future JavaScript features without worrying about environment support, because TypeScript can transpile the code to multiple JavaScript flavors <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

## Setting Up and Compiling
To [[getting_started_with_typescript_and_its_installation | get started with TypeScript]], the first step is to install it globally using NPM <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. This grants access to the `tsc` command, which runs the TypeScript compiler <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. (At the time of the video, the version used is 3.1 <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.)

TypeScript code (`.ts` files) cannot run directly in browsers or Node.js environments <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. The TypeScript compiler converts this code into vanilla JavaScript <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. For example, running `tsc index.ts` on a file will create an `index.js` file <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. By default, TypeScript compiles to ES3 <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

### `tsconfig.json` Configuration
While compiler options can be passed via the command line, the standard approach is to create a `tsconfig.json` file, which is automatically picked up by `tsc` <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Key options include:
*   `target`: Specifies the JavaScript flavor the code will be compiled to (e.g., `esnext` for native `async/await` support) <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   `watch: true`: Automatically recompiles code upon file saves <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   `lib`: Allows the inclusion of typings for specific environments like the DOM or ES2017 <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. For web applications, including the DOM library enables TypeScript to compile code with native DOM classes without errors, providing autocomplete and IntelliSense for classes like `URL` <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. Hovering over a class provides integrated documentation and error messages <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. Right-clicking and viewing typings shows every property and method on a class <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

### Working with Third-Party Libraries
Many mainstream libraries, such as Firebase, ship with type declarations automatically <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. For libraries without built-in typings (like Lodash), a large mono-repo provides community-maintained types, which can be installed in the development environment to enable autocomplete and IntelliSense for all functions <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

## Understanding Type Annotations

### Implicit vs. Explicit Typing
TypeScript allows for strong typing either implicitly or explicitly <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. If a variable is assigned a value upon declaration, its type is automatically inferred (e.g., `number` for a numeric value) <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Attempting to assign a value of a different type (e.g., a string to a number variable) will result in an error detected by the compiler before runtime <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

### The `any` Type
Unlike strictly typed languages, TypeScript allows developers to opt out of the type system by annotating a variable with `any` <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. This means the variable can be assigned any value, and the compiler will not type-check it <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. While offering flexibility, it's generally best to avoid `any` when possible <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

If a variable is declared without an initial value or any type annotation, it will be inferred as `any` by default <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. To explicitly annotate a variable with a type, use a colon followed by the type (e.g., `: number`) <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. A general tip is to avoid explicitly strong typing if the type is implicitly inferred <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

### Custom Types
In addition to built-in types, you can create your own types <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. Custom types are typically named in Pascal case <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

#### Union Types
Custom types can be defined using a union, allowing a variable to accept specific values (e.g., `'bold' | 'italic'`) <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. Union types can include different primitive types like strings and numbers <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

#### [[typescript_interfaces_and_custom_types | Interfaces]] for Object Shapes
TypeScript allows enforcing the shape of objects using [[typescript_interfaces_and_custom_types | interfaces]] <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. An [[typescript_interfaces_and_custom_types | interface]] defines the types for each property of an object <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. This [[typescript_interfaces_and_custom_types | interface]] can then be used to strong type objects, function return values, or arguments <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

[[typescript_interfaces_and_custom_types | Interfaces]] can be made less restrictive while maintaining required properties by using an index signature (e.g., `[key: string]: any`), allowing additional arbitrary properties <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

## Functions and Arrays

### Function Type Annotations
Strong typing functions involves annotating both arguments and return values <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. Arguments are annotated similar to variables (e.g., `x: number`), ensuring only specified types are passed <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. The return value type is annotated after the parentheses and before the curly brackets of the function (e.g., `(x: number, y: number): number`) <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. If a function does not return a value or creates a side effect, its return type can be `void` <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

### Array Type Annotations
To strong type an array, specify the element type followed by brackets (e.g., `number[]` for an array of numbers) <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. This is particularly useful when working with arrays of objects to gain IntelliSense while iterating over them <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>, for example, using an existing `Person` [[typescript_interfaces_and_custom_types | interface]] to define the shape of objects in an array <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

### [[typescript_interfaces_and_custom_types | Tuples]]
TypeScript introduces [[typescript_interfaces_and_custom_types | tuples]], which are fixed-length arrays where each item has its own distinct type <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
Items within a tuple can be made optional by adding a question mark after their type (e.g., `[string, number?]`) <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. This optional syntax can also be applied to function arguments <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

## Advanced Typing: [[Object Oriented Programming with TypeScript | Generics]]
[[Object Oriented Programming with TypeScript | Generics]] allow a type to be used internally within a class or function <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. A common example is an RxJS observable, which is a class with an internal observable value <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. A capital `T` (or any single letter) often represents a variable type that can be passed in to strong type the internal value of an observable <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. This enables specifying the internal type later in the code, such as an observable of a number or an observable of a `Person` [[typescript_interfaces_and_custom_types | interface]] <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. TypeScript can also implicitly infer [[Object Oriented Programming with TypeScript | generic]] types <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. While developers more often use [[Object Oriented Programming with TypeScript | generics]] than create them, understanding them is important <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.