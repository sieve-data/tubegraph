---
title: Setting up Angular testing environment
videoId: BumgayeUC08
---

From: [[fireship]] <br/> 

[[writing_and_running_angular_component_tests | Test-driven development]] is considered the most powerful tool for preventing bugs, providing better quality and more maintainable software in exchange for effort and productivity <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. [[Angular]] comes with Jasmine and Karma built-in, making testing easy to start with <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Core Testing Tools

[[Angular]]'s testing tools include:
*   **Jasmine**: A behavior-driven development (BDD) framework for testing JavaScript code <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.
*   **Karma**: A test runner that sets up a web server to automatically run tests every time a file changes <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a> <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   **Protractor**: Specifically used for end-to-end (e2e) tests, simulating how an end-user interacts with the application in the browser <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. End-to-end tests are decoupled from the main application code and are typically found in an `e2e` directory in the project root <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Initial Setup and File Structure

When generating a new [[Angular]] app, the [[introduction_to_angular_commandline_interface_cli | Angular CLI]] automatically generates boilerplate code for testing <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a> <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

Key configuration files and directories include:
*   **`karma.conf.js`**: Contains configuration options for Karma, allowing customization of the testing experience <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a> <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   **`protractor.conf.js`**: Configuration file for Protractor <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **`src/test.ts`**: Required by Karma to load all spec files; typically, no changes are needed in this file <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a> <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **`app.component.spec.ts`**: The first real test file, which the [[Angular CLI]] generates for the root component <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Basics of Writing Tests (Jasmine)

A test is broken down into fundamental parts:
1.  **Describe the test suite**: Use the `describe` keyword, followed by a string describing what is being tested (e.g., `describe('AppComponent')`) <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
2.  **Define individual tests**: Inside the `describe` block, each test starts with the `it` keyword, followed by a description of the specific behavior being tested (e.g., `it('should be awesome')`) <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a> <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
3.  **Write an expectation**: Use `expect` to verify whether the behavior is true or false. This is followed by a Jasmine matcher (e.g., `expect(component).toBeTruthy()`) <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a> <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. The result is a description of code behavior that is easily readable <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Setting Up [[writing_and_running_angular_component_tests | Angular Component Tests]]

To set up a component spec from scratch:
1.  **Import Testing Utilities**: Import [[Angular]]'s testing utilities <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  **Declare Fixture**: Declare a variable for the `fixture`, which is the test environment for the component. It provides access to the component instance itself and its rendered HTML via the `debug element` <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
3.  **Setup TestBed**: Before each spec, set up a `TestBed`, which is an `NgModule` specific to the testing environment <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
    *   For a simple isolated test, declare the component <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   To compile the component's HTML and CSS, call `compileComponents()` after the `TestBed` <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
4.  **Initialize Variables**: After the `TestBed` is compiled, set up variables for testing the component directly or its rendered HTML via the `debug element` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
5.  **Run Change Detection**: Run [[Angular]] change detection before each test using `fixture.detectChanges()` <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### Running Tests

To run tests, use the command `ng test` <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. Karma will bring up a browser window showing passed or failed tests and updates automatically when files change <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

### Common Matchers and Testing Scenarios

*   **`toBeTruthy()`**: Checks if something evaluates to `true` in a boolean context (not necessarily the primitive `true` value) <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a> <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
    *   Example: `expect(component).toBeTruthy()` to check if the component is created <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **`toContain()`**: Checks for a substring in a string or an element in an array <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a> <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.# Setting up Angular Testing Environment

[[writing_and_running_angular_component_tests | Test-driven development]] is considered the most powerful tool for preventing bugs, providing better quality and more maintainable software in exchange for effort and productivity <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. [[Angular]] comes with Jasmine and Karma built-in, making testing easy to start with <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Core Testing Tools

[[Angular]]'s testing tools include:
*   **Jasmine**: A behavior-driven development (BDD) framework for testing JavaScript code <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.
*   **Karma**: A test runner that sets up a web server to automatically run tests every time a file changes <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a> <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   **Protractor**: Specifically used for end-to-end (e2e) tests, simulating how an end-user interacts with the application in the browser <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. End-to-end tests are decoupled from the main application code and are typically found in an `e2e` directory in the project root <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Initial Setup and File Structure

When generating a new [[Angular]] app, the [[introduction_to_angular_commandline_interface_cli | Angular CLI]] automatically generates boilerplate code for testing <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a> <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

Key configuration files and directories include:
*   **`karma.conf.js`**: Contains configuration options for Karma, allowing customization of the testing experience <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a> <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   **`protractor.conf.js`**: Configuration file for Protractor <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **`src/test.ts`**: Required by Karma to load all spec files; typically, no changes are needed in this file <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a> <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **`app.component.spec.ts`**: The first real test file, which the [[Angular CLI]] generates for the root component <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Basics of Writing Tests (Jasmine)

A test is broken down into fundamental parts:
1.  **Describe the test suite**: Use the `describe` keyword, followed by a string describing what is being tested (e.g., `describe('AppComponent')`) <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
2.  **Define individual tests**: Inside the `describe` block, each test starts with the `it` keyword, followed by a description of the specific behavior being tested (e.g., `it('should be awesome')`) <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a> <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
3.  **Write an expectation**: Use `expect` to verify whether the behavior is true or false. This is followed by a Jasmine matcher (e.g., `expect(component).toBeTruthy()`) <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a> <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. The result is a description of code behavior that is easily readable <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Setting Up [[writing_and_running_angular_component_tests | Angular Component Tests]]

To set up a component spec from scratch:
1.  **Import Testing Utilities**: Import [[Angular]]'s testing utilities <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  **Declare Fixture**: Declare a variable for the `fixture`, which is the test environment for the component. It provides access to the component instance itself and its rendered HTML via the `debug element` <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
3.  **Setup TestBed**: Before each spec, set up a `TestBed`, which is an `NgModule` specific to the testing environment <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
    *   For a simple isolated test, declare the component <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   To compile the component's HTML and CSS, call `compileComponents()` after the `TestBed` <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
4.  **Initialize Variables**: After the `TestBed` is compiled, set up variables for testing the component directly or its rendered HTML via the `debug element` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
5.  **Run Change Detection**: Run [[Angular]] change detection before each test using `fixture.detectChanges()` <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### Running Tests

To run tests, use the command `ng test` <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. Karma will bring up a browser window showing passed or failed tests and updates automatically when files change <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

### Common Matchers and Testing Scenarios

*   **`toBeTruthy()`**: Checks if something evaluates to `true` in a boolean context (not necessarily the primitive `true` value) <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a> <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
    *   Example: `expect(component).toBeTruthy()` to check if the component is created <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **`toContain()`**: Checks for a substring in a string or an element in an array <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a> <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **`toBeGreaterThan()`**: Checks if a numeric value is greater than another <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Testing Rendered HTML**: Use `debug element` to query elements in the DOM (e.g., `query(By.css('h1'))`) and get the native HTML element to check its `innerText` <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a> <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   **Testing Functions**: Call a component method and assert its effect on component properties <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Testing Asynchronous Changes**:
    *   Use `fakeAsync` helper from [[Angular]] to create a fake [[Angular]] zone for testing asynchronous activity <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   Use the `tick` utility within `fakeAsync` to simulate the passage of time <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

## Testing with Services and Third-Party Dependencies (e.g., [[deploying_angular_applications_using_firebase | Firebase]])

When testing components that interact with services, especially those fetching data from a backend like [[deploying_angular_applications_using_firebase | Firebase]], it's crucial **not** to use live data <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. Instead, simulate the backend data return using stubs or spies.

### Stubs

A stub is a method that returns predictable and reproducible data, often in the form of an observable <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   **Creating a Stub**: Define an object with a function that mimics the service method's return value (e.g., an observable containing mock data) <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Providing the Stub**: In the `TestBed`'s `providers` array, use `provide` with the actual service class and `useValue` with your service stub <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This tells the test environment to use the stub instead of the live service <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Testing with Stubs**: Subscribe to the observable returned by the stub and place expectations inside the subscribe block <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. Stubs are limited as they don't track how many times a method has been called <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

### Spies (Jasmine)

Spies allow you to monitor method calls on a live service without making real requests, while still providing mock return values <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.
*   **Setup**:
    *   Set up the `TestBed` to import and provide the *actual* service class <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a> <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
    *   Get the service instance using `debug element.injector.get(MessageService)` <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   **Creating a Spy**: Use `spyOn()` from Jasmine, passing it the main service class and the method to monitor (e.g., `spyOn(service, 'getContent')`) <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **Mocking Return Value**: Tell the spy to return a specific value using `and.returnValue()` (e.g., `and.returnValue(of('mocked message'))`) <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. This prevents actual live requests while still allowing monitoring <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   **Assertions with Spies**:
    *   Check if the method was called: `expect(spy).toHaveBeenCalled()` <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
    *   Check the number of calls: `expect(spy.calls.all().length).toEqual(1)` <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
    *   Spies can also track arguments passed to methods <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.