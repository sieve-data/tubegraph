---
title: Implementing unit and integration tests with Jest
videoId: Jv2uxzhPFl4
---

From: [[fireship]] <br/> 

[[introduction_to_testdriven_development_tdd | Test-driven development (TDD)]] is a technique where you describe the behavior of your code *before* you implement it <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Following this science can help reduce bugs and improve the maintainability of your codebase in the long run <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. For new programmers, knowing how to test code is a powerful way to level up as a developer, teaching you about your code and improving debugging skills <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

Automated testing involves writing code that describes your requirements and validates your main application code <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. While many developers, including the speaker, often write tests only after a feature is working or not at all (especially in front-end development due to changing UI requirements), [[introduction_to_testdriven_development_tdd | TDD]] advocates writing tests *before* the actual code <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

The common mantra in [[introduction_to_testdriven_development_tdd | TDD]] is "red, green, refactor" <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>:
1.  **Red**: Write a failing test first <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
2.  **Green**: Write code to make that test pass <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
3.  **Refactor**: Optimize or refactor the code while keeping the test passing <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

This approach isn't always practical, but for projects with clear requirements, it can improve productivity <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Testing Strategies

[[testing_strategies_in_software_development | Testing strategies]] add value to a codebase <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>:

*   **Unit Testing**
    *   Goal: Validate the behavior of individual functions, methods, or "units" of code <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   This is the lowest level of testing <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   Unit tests are designed to be fast and simple <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

*   **Integration Testing**
    *   Involves testing multiple units of code together <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
    *   Example: Testing a React component and a hook to fetch data from a database to see how well they work together <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

Other [[testing_strategies_in_software_development | testing strategies]] include [[endtoend_testing_with_cypress | End-to-End Testing]], Acceptance Testing, System Testing, and Smoke/Sanity Tests <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. There are also non-functional tests like performance, usability, and security testing (e.g., stress testing, failover testing) <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

## [[setting_up_angular_testing_environment | Setting up the Testing Environment]] with Jest

To get started with Jest:

1.  **Initialize a Project**: The video uses Vite with vanilla JavaScript (e.g., `npm init vite@latest js/app` and select vanilla JavaScript) <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
2.  **Install Jest**: `npm install --save-dev jest` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. Jest looks for files ending in `.test.js` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
3.  **Create Test Directory and File**: Create a `test` directory and add a file like `stack.test.js` <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. The example implements the code and tests in the same file for simplicity <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
4.  **Configure npm Script**: Add a `test` script to `package.json` to run the Jest test runner <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>:
    ```json
    "scripts": {
      "test": "jest --watchAll --verbose"
    }
    ```
    *   `--watchAll`: Jest watches code and reruns tests on changes <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
    *   `--verbose`: Adds extra output to the terminal <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    *   Run with `npm test` <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
5.  **Add Types for Jest (Optional but Recommended)**: This provides IntelliSense for Jest matchers <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
    *   Install types: `npm install --save-dev @types/jest` <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
    *   Create `jsconfig.json` in the project root:
        ```json
        {
          "compilerOptions": {
            "typeAcquisition": {
              "include": ["jest"]
            }
          }
        }
        ```
    *   This allows VS Code to provide IntelliSense for Jest <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
6.  **Wallaby Plugin (Optional Pro Tip)**: A paid VS Code extension with a free trial that shows test passing/failing directly in the editor, boosting productivity <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

## Implementing Unit Tests with Jest

The example demonstrates [[introduction_to_testdriven_development_tdd | TDD]] by implementing a `Stack` data structure without using JavaScript arrays <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Test Structure

*   **`describe` function**: Used to define a test suite, describing the thing being tested (e.g., `Stack`) <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. It takes a callback function as the second argument <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   **`test` or `it` functions**: Used inside `describe` to define individual tests. Both do the same thing <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   **`todo` method**: Can be used to make a test pass temporarily while you figure things out, deferring implementation <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

### Red-Green-Refactor in Practice

**Requirement 1: Stack is created empty** <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>

1.  **Red (Write Failing Test)**:
    *   Instantiate a `Stack` class (which doesn't exist yet).
    *   Use `expect()` to write an expectation: `expect(stack.top).toBe(-1)` and `expect(stack.items).toEqual({})` <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
        *   `toBe()`: Checks for referential equality (e.g., for primitives like -1) <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
        *   `toEqual()`: Checks for value equality (e.g., for objects like `{}`) <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. This is crucial as `toBe()` would fail for two distinct but empty objects in memory <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
    *   Saving the file initially yields "ReferenceError: Stack is not defined" <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

2.  **Green (Write Code to Pass Test)**:
    *   Define the `Stack` class:
        ```javascript
        class Stack {
          constructor() {
            this.top = -1; // Corrected from initial 0 to -1 to match requirement
            this.items = {};
          }
        }
        ```
    *   Saving the file now makes the test pass <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

**Requirement 2: Push items to the top** <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>

1.  **Setup/Teardown with Jest Helpers**:
    *   Instead of initializing `new Stack()` in every test, use `beforeEach` hook to re-initialize a global `stack` variable before each test, reducing code duplication <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
        ```javascript
        let stack;
        beforeEach(() => {
          stack = new Stack();
        });
        ```

2.  **Red (Write Failing Test)**:
    *   Call a `push` method (doesn't exist yet) on the stack.
    *   Expect `stack.top` to be incremented and a `peek` property (also doesn't exist) to return the pushed value <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>:
        ```javascript
        test('can push items to the top', () => {
          stack.push('item 1');
          expect(stack.top).toBe(0);
          expect(stack.peek()).toBe('item 1');
        });
        ```
    *   This will result in failing tests <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

3.  **Green (Write Code to Pass Test)**:
    *   Add `push` and `peek` methods to the `Stack` class:
        ```javascript
        class Stack {
          constructor() {
            this.top = -1;
            this.items = {};
          }
          push(item) {
            this.top++;
            this.items[this.top] = item;
          }
          peek() {
            return this.items[this.top];
          }
        }
        ```
    *   This will make the tests pass. The goal is to get to a passing test as soon as possible, then refactor <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

### Code Coverage

*   Add the `--coverage` flag to the Jest command in `package.json` <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>:
    ```json
    "scripts": {
      "test": "jest --watchAll --verbose --coverage"
    }
    ```
*   Running `npm test` will generate a report showing the percentage of code covered by your tests <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   While useful, 100% code coverage doesn't guarantee a good test suite and can give a false sense of security <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.