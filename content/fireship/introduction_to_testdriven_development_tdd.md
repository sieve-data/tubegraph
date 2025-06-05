---
title: Introduction to TestDriven Development TDD
videoId: Jv2uxzhPFl4
---

From: [[fireship]] <br/> 

Test-Driven Development (TDD) is a software development technique where you describe the behavior of your code *before* you go and implement it <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. It's a powerful approach for developers, especially for those new to programming, to level up their skills and improve debugging <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Benefits of TDD
*   **Reduces Bugs:** If you "trust the science," [[testdriven_development_benefits | testing]] helps reduce bugs <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   **Improves Maintainability:** It improves the maintainability of your codebase in the long run <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   **Enhances Understanding:** It can teach you about your code in unexpected ways <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   **Better Debugging:** TDD makes you much better at debugging <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Professional Appearance:** It can make you look like you know what you're doing in a technical interview <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
*   **Potential Productivity Boost:** For projects with very clear requirements, TDD can actually improve productivity <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## The Red Green Refactor Cycle
The core principle of [[benefits_and_challenges_of_tdd | Test-Driven Development]] is the "Red Green Refactor" mantra <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. This cycle involves:
1.  **Red:** Write a failing test first <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
2.  **Green:** Write some code to get the test passing <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
3.  **Refactor:** Go back and optimize or refactor the code while trying to keep your test in the green <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

This process provides psychological satisfaction when moving from a red failing test to a green passing test <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. The general approach is to get to a passing test as soon as possible, then refactor <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

## TDD in Practice
Most developers typically start writing tests only after a feature is working, or they don't write tests at all, especially in front-end development where UI requirements change frequently <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. However, TDD flips this by prioritizing test writing before implementation <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. While not always practical, it's highly effective for projects with clear requirements <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Project Setup for TDD with Jest
To implement TDD, you need a testing framework. The video demonstrates using [[implementing_unit_and_integration_tests_with_jest | Jest]] for JavaScript:

### Project Initialization
1.  Initialize a project (e.g., using Vite with vanilla JavaScript option): `npm init vjs/app` <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

### Installing Jest
1.  Install Jest: `npm install jest` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. Jest looks for files ending in `.test.js` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
2.  Create a `test` directory and add a testing file, e.g., `stack.test.js` <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

### Configuring Jest
1.  Add an npm script in `package.json` to run Jest:
    ```json
    "scripts": {
      "test": "jest --watchAll --verbose"
    }
    ```
    *   `--watchAll`: Watches code and reruns tests on changes <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
    *   `--verbose`: Adds extra output to the terminal <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
2.  Run tests: `npm test` <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

### Adding Types for Intellisense
1.  Install Jest types for Intellisense: `npm install --save-dev @types/jest` <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
2.  Create a `jsconfig.json` file with a `type acquisition` property for Jest:
    ```json
    {
      "compilerOptions": {
        "types": ["jest"]
      }
    }
    ```
    This allows VS Code to provide Intellisense for Jest matchers <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### Optional Plugin: Wallaby
The Wallaby plugin (a paid VS Code extension with a free trial) can show test pass/fail status directly in the editor, providing a productivity boost without needing to check the terminal <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

## Writing Tests in Jest
Jest provides functions to structure and write tests:

*   **`describe` function:** Used to group related tests for a specific "thing" (e.g., a Stack data structure). It takes a description string and a callback function <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   **`test` or `it` function:** Defines an individual test within a `describe` block. Both do the exact same thing <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   **`expect` and Matchers:**
    *   `expect(value)`: Used to write an expectation, making sure the code does what is expected <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
    *   `toBe(expected)`: Checks for referential equality between two objects (i.e., if they are the same object in memory) <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
    *   `toEqual(expected)`: A better choice for objects, as it checks for value equality <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
    *   `todo()`: Marks a test as a "to-do" item, allowing it to pass temporarily while you figure things out <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

### Setup and Teardown
Jest offers helper functions for setup and teardown, which are useful for avoiding code duplication in test suites <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
*   **`beforeEach(callback)`:** Re-initializes a global variable (e.g., a `stack` instance) before each new test, ensuring a clean state <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

## Code Coverage Reports
A code coverage report shows the percentage of your source code covered by your tests <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. You can generate this by adding the `--coverage` flag to the Jest command in `package.json` <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. While it can be useful, 100% code coverage doesn't necessarily mean you have a good test suite; it can sometimes give a false sense of security <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

## TDD and Other [[testing_strategies_in_software_development | Testing Strategies]]
While TDD focuses on the development workflow, the tests themselves fit into broader [[testing_strategies_in_software_development | testing strategies]]:

*   **Unit Testing:** The lowest level of testing, validating the behavior of individual functions, methods, or units of code <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. TDD is often applied here first.
*   **Integration Testing:** Testing multiple units of code together to see how well they interact, like a React component using a hook to fetch data <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   **End-to-End Testing (E2E):** Simulates actual user behavior by running the app in a simulated environment <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. Tools like [[endtoend_testing_with_cypress | Cypress]] (which downloads an actual browser to run tests in a real-world environment) allow programming tests where users click buttons, fill forms, and assert UI changes <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. While unit tests are fast and simple, E2E tests are long and complex due to their simulation of user behavior <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   **Acceptance Testing:** Ensures the software meets all client requirements <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   **System Testing:** Ensures everything works on actual servers or hardware <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   **Sanity/Smoke Tests:** Runs a few of the most important tests first to quickly check if the application is fundamentally working ("not on fire") before running the full test suite <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Non-functional Tests:** Focus on aspects like performance, usability, and security (e.g., stress testing, failover testing) <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. These test the infrastructure rather than the code itself <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

TDD is a valuable practice that helps guide development, but it's important to understand when to apply it, as it "walks a very fine line between being valuable and a complete waste of time" <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.