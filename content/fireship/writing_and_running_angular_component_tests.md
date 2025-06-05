---
title: Writing and running Angular component tests
videoId: BumgayeUC08
---

From: [[fireship]] <br/> 

Test-driven development (TDD) is considered the most powerful tool for preventing bugs in applications, leading to higher quality and more maintainable software over the long term <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Angular facilitates testing by including Jasmine and Karma built-in, making it straightforward to get started <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Angular Testing Tooling

When you use the [[introduction_to_angular_commandline_interface_cli | Angular CLI]] to generate an application, it automatically creates boilerplate code for testing <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

*   **`karma.conf.js`**: Karma sets up a web server that automatically runs all your tests every time a file changes <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This file allows for customization of the testing experience <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   **`protractor.conf.js`**: This file is specifically for [[endtoend_testing_with_cypress | end-to-end (E2E) tests]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. E2E testing simulates how an end-user sees the application by using a browser, completely decoupled from the main application code <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. E2E tests are typically located in the `e2e` directory at the project root <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **`test.ts`**: Located in the source directory, this file is required by Karma to load all your spec files <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. Generally, you shouldn't need to modify this file <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Anatomy of a Jasmine Test

The `app.component.spec.ts` file provides a starting point for understanding Angular tests <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

*   **`describe` Block**: This keyword is used in Jasmine to define a test suite, followed by a description of what is being tested <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. All individual tests (specs) for that suite are written inside this block <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **`it` Block**: Each individual test, or spec, starts with the `it` keyword, followed by a description of the behavior being tested <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   **`expect` and Matchers**: Inside an `it` block, an `expect` statement is used with a "matcher" to verify if an expectation is true or false <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. For example, `expect(component).toBeTruthy()` checks if the component evaluates to true in a boolean context <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Jasmine offers many matchers for different types of comparisons (e.g., `toContain`, `toEqual`, `toBeGreaterThan`) <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>, <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

The goal of this structure is to describe and validate code behavior in a way that is easily readable by non-programmers, which helps in reducing bugs <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Setting Up an Angular Component Test

To illustrate, consider an `AlertButtonComponent` with properties like `content`, `severity`, and a `toggle` method to control message visibility <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Initial Setup

1.  **Imports**: Begin by importing Angular's testing utilities <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  **`describe` Suite**: Define the test suite for the component <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
3.  **`fixture`**: Declare a `fixture` variable, which represents the test environment for the component, providing access to the component instance and its `debug element` (rendered HTML) <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
4.  **`beforeEach` and `TestBed`**: Before each spec, set up a `TestBed`, which is an Angular module specifically for the testing environment <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
    *   For an isolated test of the component, declare it in `declarations` within the `TestBed` configuration <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   To compile the component's HTML and CSS, call `TestBed.compileComponents()` <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
    *   After compilation, obtain references to the `component` instance and its `debug element` from the `fixture` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
    *   Run Angular change detection with `fixture.detectChanges()` before most tests, though it can also be tested before change detection <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### Basic Component Property and Method Testing

*   **Component Creation**: Verify the component is created successfully <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
    ```typescript
    it('should create', () => {
      expect(component).toBeTruthy();
    });
    ```
*   **Property Values**: Check if hardcoded properties contain expected strings or numerical values <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
    ```typescript
    it('should have content that contains "warn"', () => {
      expect(component.content).toContain('warn');
    });
    it('should have a severity greater than 2', () => {
      expect(component.severity).toBeGreaterThan(2);
    });
    ```
*   **DOM Rendering**: Use the `debug element` to query the rendered HTML and verify elements and their text content <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
    ```typescript
    it('should have an h1 tag of Alert Button', () => {
      const h1 = debugEl.query(By.css('h1')).nativeElement;
      expect(h1.innerText).toEqual('Alert Button');
    });
    ```
*   **Method Behavior**: Test if a component method correctly modifies properties <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
    ```typescript
    it('should toggle the message boolean', () => {
      expect(component.hideContent).toBeTruthy(); // Hidden by default
      component.toggle();
      expect(component.hideContent).toBeFalsy(); // Toggled to false
    });
    ```

### Asynchronous Testing

For asynchronous changes (e.g., with `rxjs` timers), use `fakeAsync` and `tick` from `@angular/core/testing` <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

```typescript
it('should toggle the message boolean asynchronously', fakeAsync(() => {
  expect(component.hideContent).toBeTruthy();
  component.toggleAsync(); // Calls toggle after 500ms
  tick(500); // Advance time by 500ms
  expect(component.hideContent).toBeFalsy();
}));
```
The `tick()` utility allows you to simulate the passage of time within the `fakeAsync` block <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

## Testing with Services and Third-Party Dependencies

When testing components that rely on services, especially those interacting with external APIs like Firebase, you generally want to simulate the backend data rather than using live data <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

### Stubbing Services

A "stub" is a method that returns predictable and reproducible data, simulating the service's behavior <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

To use a stub:
1.  Define a service stub object that mimics the service's methods and returns the desired mock data (e.g., an observable) <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
    ```typescript
    const serviceStub = {
      getContent: () => of({ message: 'You have been warned' })
    };
    ```
2.  Provide the stub in the `TestBed`'s `providers` array using `useValue` <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
    ```typescript
    TestBed.configureTestingModule({
      declarations: [AlertButtonComponent],
      providers: [
        { provide: MessageService, useValue: serviceStub }
      ]
    }).compileComponents();
    ```
3.  Write a spec that subscribes to the component's observable and asserts the mock data <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
    ```typescript
    it('should have message content defined from an observable', (done) => {
      component.content$.subscribe(data => {
        expect(data.message).toBeDefined();
        expect(data.message).toEqual('You have been warned');
        done(); // Important for async tests with actual observables
      });
    });
    ```
    *Note: When using actual observables, you must use `done()` or a `fakeAsync` block to properly handle the asynchronous nature of the subscription.*

### Using Jasmine Spies

For more control, such as checking if a method was called and with what arguments, use a Jasmine spy <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. Spies allow you to monitor method calls without actually executing the original method's logic <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

1.  Provide the *live* service in the `TestBed` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
2.  Get an instance of the service within the `beforeEach` block <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
3.  Use `spyOn(service, 'methodName')` to create a spy <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
4.  Chain `and.returnValue()` to make the spy return specific mock data, preventing a real request <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

    ```typescript
    beforeEach(() => {
      // ... setup TestBed with actual MessageService ...
      fixture = TestBed.createComponent(AlertButtonComponent);
      component = fixture.componentInstance;
      service = debugEl.injector.get(MessageService); // Get the live service instance
      spy = spyOn(service, 'getContent').and.returnValue(of({ message: 'You have been warned' }));
      fixture.detectChanges();
    });
    ```

5.  Write specs to check the spy's behavior and the component's updated view <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
    ```typescript
    it('should call the service method once and update the view', () => {
      expect(spy).toHaveBeenCalled(); // Check if method was called
      expect(spy.calls.all().length).toEqual(1); // Check call count

      // Verify the view was updated with the mocked data
      const messageBody = debugEl.query(By.css('.message-body')).nativeElement;
      expect(messageBody.innerText).toContain('warn');
    });
    ```
Spies can also check `toHaveBeenCalledWith()` and access call arguments <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## Running Tests

To run your Angular tests, simply execute the command `ng test` in your terminal <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. Karma will launch a browser window showing the test results, which update in real-time as you save changes to your spec files <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.