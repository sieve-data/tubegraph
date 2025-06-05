---
title: Introduction to Jasmine and Karma
videoId: BumgayeUC08
---

From: [[fireship]] <br/> 

Test-driven development (TDD) is a powerful tool for preventing bugs, scientifically proven to lead to better quality and more maintainable software over the long term <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Angular comes with Jasmine and Karma built-in, making it easy to get started with testing <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Setting Up the [[setting_up_angular_testing_environment | Angular Testing Environment]]

When generating a new Angular application using the [[introduction_to_angular_commandline_interface_cli | Angular CLI]], boilerplate code for testing is automatically created <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

### Karma Configuration

Karma sets up a web server to automatically run tests whenever a file changes <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Configuration options are available for customization <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

### Protractor for End-to-End Tests

Angular projects also include a Protractor config file specifically for end-to-end (E2E) tests <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. E2E testing simulates user interaction with the application in a browser, making it decoupled from the main application code <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. These tests are typically located in the `e2e` directory at the root of the project <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### `test.ts` File

Inside the `src` directory, there is a `test.ts` file, which Karma requires to load all spec files <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. Users generally don't need to change anything in this file <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Jasmine Fundamentals

Jasmine is the testing framework used in Angular for writing tests <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### Describing Test Suites (`describe`)

The `describe` keyword is used to define a test suite, taking a string describing what is being tested and a function containing the tests <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### Defining Individual Tests (`it`)

Individual tests within a `describe` block are defined using the `it` keyword, followed by a description of the specific behavior being tested and a function containing the test logic <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### Expectations and Matchers (`expect`)

An expectation verifies whether a statement is true or false using `expect` combined with a matcher <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. This approach helps describe code behavior in a way that non-programmers can easily understand, making testing effective at reducing bugs <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

Some common Jasmine matchers:
*   `toBeTruthsy()`: Checks if something evaluates to true in a boolean context <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This does not mean it is the primitive `true` value <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   `toContain()`: Checks for a substring within a string or an element within an array <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   `toEqual()`: Checks for an exact match <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   `toBeGreaterThan()`: Checks if a numeric value is greater than another <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

For a comprehensive list of matchers, consult the Jasmine documentation <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## Angular Component Testing

To set up component tests, Angular's testing utilities are imported <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

### Test Environment Setup (`TestBed` and Fixture)

*   **Fixture**: Represents the test environment for a component, providing access to the component instance and its `DebugElement` (rendered HTML) <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   **TestBed**: An `NgModule` specific to the testing environment, configured before each spec <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. It can be set up for an isolated test of the component itself <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   **`compileComponents()`**: Called after configuring the `TestBed` if you need to compile the component's HTML and CSS <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
*   **Change Detection**: `detectChanges()` is typically run before each test to ensure Angular's change detection has run <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### Testing Component Properties and DOM

Tests can check component properties directly or their rendered HTML via the `DebugElement` <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **Component Properties**: Verify component properties using `expect` and matchers, e.g., `expect(component.content).toContain('warn')` <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   **DOM Elements**: Use `debug.query()` with CSS selectors to find elements in the rendered DOM and then access their `nativeElement` and `innerText` for validation <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Method Behavior**: Test if a component's method correctly updates properties, e.g., `expect(component.hideContent).toBeFalsy()` after calling a toggle method <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

## Asynchronous Testing

Angular provides helpers for testing asynchronous operations:
*   **`fakeAsync`**: Wraps a test to create a fake Angular zone, allowing for the testing of asynchronous activity <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **`tick()`**: Advances the virtual clock within a `fakeAsync` block by a specified number of milliseconds, simulating the passage of time for asynchronous operations like timers <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

## Testing with Services and Dependencies

When testing components that rely on services or external dependencies (like Firebase), it's crucial not to use live data from a real backend <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. Instead, simulate the backend data using stubs or spies.

### Stubs

A stub is a method that returns predictable and reproducible data, allowing you to mock the behavior of a service without making actual requests <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
*   You can define an object that mimics the service's structure and returns mock data, such as an [[introduction_to_rxjs_and_observables | observable]] <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   This stub is then provided to the `TestBed` in the `providers` array using `useValue` <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
*   This approach is straightforward for testing mock data but doesn't track how many times a method was called <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

```typescript
// Example Stub
const serviceStub = {
  getContent: () => of('You have been warned') // Returns an RxJS Observable
};

TestBed.configureTestingModule({
  providers: [
    { provide: MessageService, useValue: serviceStub }
  ]
});
```

### Spies

Spies, provided by Jasmine, allow you to monitor method calls on a live service without using actual backend data <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.
*   Use `spyOn(service, 'methodName')` to monitor a method <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   Use `and.returnValue()` to make the spy return a specific value, preventing actual requests to the backend <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   Spies can verify if a method was called (`toHaveBeenCalled()`) and how many times it was called (`calls.all().length`) <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
*   They can also reveal which arguments were passed to the method <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

```typescript
// Example Spy setup
let service: MessageService;
let spy: jasmine.Spy;

beforeEach(async () => {
  await TestBed.configureTestingModule({
    imports: [AngularFireModule.initializeApp(firebaseConfig)], // If live service requires AngularFire
    providers: [MessageService]
  }).compileComponents();

  fixture = TestBed.createComponent(AlertButtonComponent);
  component = fixture.componentInstance;
  debugEl = fixture.debugElement;

  service = debugEl.injector.get(MessageService); // Get the live service instance
  spy = spyOn(service, 'getContent').and.returnValue(of('You have been warned')); // Spy on the method and return mock data
  fixture.detectChanges();
});

// Example Spy Test
it('should make sure our service method was called once', () => {
  expect(spy).toHaveBeenCalled(); <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>
  expect(spy.calls.all().length).toEqual(1); <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>
});
```
> [!NOTE] For more advanced uses of spies, refer to the Jasmine documentation <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.