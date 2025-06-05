---
title: Testing strategies in software development
videoId: Jv2uxzhPFl4
---

From: [[fireship]] <br/> 

Software testing is a crucial practice in modern application development, focusing on writing code to validate the requirements and functionality of the main application code <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Knowing how to test code is considered one of the most powerful ways to level up as a developer <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. When done effectively, testing can help reduce bugs and improve the maintainability of a codebase in the long run <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Introduction to [[Introduction to TestDriven Development TDD | Test-Driven Development (TDD)]]

[[Introduction to TestDriven Development TDD | Test-driven development]] is a technique where developers describe the behavior of their code before implementing it <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. While many developers typically write tests after a feature is working or sometimes not at all, especially in front-end development due to frequently changing UI requirements <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, [[Introduction to TestDriven Development TDD | TDD]] advocates writing the test first <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This approach can be particularly helpful in technical interviews, providing time and demonstrating proficiency <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

### The Red-Green-Refactor Cycle

A common mantra in [[Introduction to TestDriven Development TDD | Test-Driven Development]] is "red green refactor" <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>:
1.  **Red**: Write a failing test first <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
2.  **Green**: Write code to make the test pass <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
3.  **Refactor**: Optimize or refactor the code while ensuring the test remains green <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

This cycle is not always practical but can significantly improve productivity for projects with clear requirements <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Types of Testing Strategies

Software testing can be categorized into various strategies, each adding different layers of value to a codebase <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

### Unit Testing

Unit testing is the lowest level of testing, aiming to validate the behavior of individual functions, methods, or small units of code <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. They are designed to be fast and simple <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. Jest is a popular testing framework used for implementing unit tests <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

### Integration Testing

Integration testing involves testing multiple units of code together to ensure they work correctly in combination <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. For example, testing a React component and a hook to fetch data to see if they interact as expected <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### End-to-End (E2E) Testing

End-to-end testing runs the application in a simulated environment, emulating actual user behavior <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. These tests are typically longer and more complex than unit tests because they simulate a full user journey <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. Cypress is a tool commonly used for E2E testing, featuring a browser-based test runner that allows programmatic testing of user actions like clicking buttons or filling forms, and asserting UI changes <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

### Other Testing Terms

Beyond the core three, several other terms are used in software testing:
*   **Acceptance Testing**: Ensures the software meets all client requirements <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   **System Testing**: Ensures everything works correctly on actual servers or hardware <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   **Sanity/Smoke Tests**: On large applications with thousands of tests, a smoke test runs a few of the most important tests first to quickly determine if the application is fundamentally broken before running the full suite <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Non-functional Tests**: These assess aspects other than functionality, such as:
    *   **Performance**: Testing the application's speed and responsiveness <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
    *   **Usability**: Evaluating the ease of use <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
    *   **Security**: Assessing vulnerabilities and protection <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
    *   **Stress Testing**: Pushing the system to its limits to test capabilities <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
    *   **Failover Testing**: Testing how the system handles failures in its infrastructure <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Practical Implementation with Jest (Unit Testing Example)

To demonstrate [[Introduction to TestDriven Development TDD | TDD]] and unit testing, consider implementing a stack data structure (last-in, first-out) without using a JavaScript array <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Project Setup
1.  Initialize a project (e.g., with Vite's vanilla JavaScript option) <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
2.  Install Jest: `npm install jest` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. Jest looks for files ending in `.test.js` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
3.  Create a `test` directory and a `stack.test.js` file <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
4.  Configure an `npm test` script in `package.json` to run `jest --watchAll --verbose` <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
5.  (Optional but recommended) Add Jest types for Intellisense: `npm install @types/jest` and create `jsconfig.json` <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

### Writing Unit Tests with Jest

Tests are defined using the `describe` function to group related tests for a specific component (e.g., a "Stack") <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. Inside `describe`, individual tests are written using `test` or `it` <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

#### Example: Initializing an Empty Stack (Red-Green Cycle)
1.  **Red (Write Failing Test)**: Define the test and an expectation that the stack should be instantiated with a `top` property of -1 (empty) and `items` as an empty object <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
    ```javascript
    describe('Stack', () => {
        test('should be created empty', () => {
            const stack = new Stack(); // Stack class doesn't exist yet
            expect(stack.top).toBe(-1); // Expecting -1
            expect(stack.items).toEqual({}); // Expecting an empty object
        });
    });
    ```
    This will initially fail with a `ReferenceError: Stack is not defined` <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
2.  **Green (Implement Code to Pass Test)**:
    *   Define the `Stack` class <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. This will lead to a failure stating `top` is undefined <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
    *   Add a constructor to initialize `top` to -1 and `items` to an empty object <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
    ```javascript
    class Stack {
        constructor() {
            this.top = -1;
            this.items = {};
        }
    }
    ```
    This will make the test pass for the `top` property.
    *   **Matcher Note**: When comparing objects for value equality (like `{}` to `{}`), use `toEqual` instead of `toBe`. `toBe` checks for referential equality, which would fail even if both are empty objects because they are different in memory <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

#### Test Setup and Teardown
Jest provides helper functions for setup and teardown, such as `beforeEach` <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>. This hook runs before each test, allowing you to re-initialize shared variables (like a `Stack` instance) to avoid code duplication and ensure each test starts with a clean state <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

#### Code Coverage Reports
You can generate a code coverage report by adding the `--coverage` flag to the Jest command in `package.json` <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. This report indicates the percentage of your source code covered by tests <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. However, 100% code coverage does not guarantee a good test suite and can provide a false sense of security <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

## End-to-End Testing with Cypress

Cypress is a powerful tool for writing end-to-end tests that simulate real user interactions in a browser <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

### Setup
1.  Install Cypress: `npm install cypress` <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. This downloads a browser for running tests <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
2.  Add an `e2e` script to `package.json` that runs `cypress open` <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. This opens the Cypress test runner <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

### Writing E2E Tests
Cypress tests are structured similarly to Jest, using `describe` and `it` <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. Cypress provides a jQuery-like syntax to interact with DOM elements (e.g., `cy.get('input').type('text')`) and assert their properties using `should` (e.g., `should('have.value', 'text')`) <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. E2E tests are particularly valuable for testing complex user flows and ensuring the entire application functions as expected in a production-like environment <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>, often utilizing mock databases and authentication <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

## [[Testdriven development benefits | Benefits and Challenges of TDD]]

### [[Testdriven development benefits | Benefits of Testing]]
*   Reduces bugs <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   Improves code maintainability <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   Enhances [[problemsolving_skills_in_software_development | debugging skills]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   Provides a clearer understanding of code behavior <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   Can improve productivity when requirements are clear <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### [[Benefits and challenges of TDD | Challenges and Considerations]]
*   Testing can be a complete waste of time if not applied judiciously <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   A high code coverage percentage doesn't necessarily mean a good test suite <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
*   Tests themselves can have bugs, and there are no tests for tests <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   Running thousands of tests can take a long time and delay work <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.