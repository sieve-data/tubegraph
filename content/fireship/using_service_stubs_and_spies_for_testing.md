---
title: Using service stubs and spies for testing
videoId: BumgayeUC08
---

From: [[fireship]] <br/> 

When performing tests in Angular, especially for components that interact with external services or [[using_apis_and_third_party_services | third-party dependencies]] like [[using_apis_and_third_party_services | Firebase]], it is crucial to simulate the behavior of these dependencies rather than relying on live data <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. This ensures predictable and reproducible tests <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. Two common techniques for this are using service stubs and spies.

## Service Stubs

A service stub is a simple method that returns data in a predictable and reproducible way, simulating how backend data would be returned <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. It prevents your tests from making real requests to the backend <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

> [!definition] What is a Stub?
> A stub is a method that returns some data in a way that's predictable and reproducible <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

### Implementation
To use a stub, you create an object that mimics the service's methods and returns the desired mock data <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. For example, if a service has a `getContent` method that returns an observable, the stub would have a `getContent` function that returns an observable of mock data <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

In your Angular `TestBed` setup, you provide this stub instead of the actual live service <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>:
```typescript
TestBed.configureTestingModule({
  // ...other configurations
  providers: [
    { provide: MessageService, useValue: serviceStub }
  ]
});
```
This tells the test environment to use the `serviceStub` whenever `MessageService` is requested <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

### Limitations
While effective for returning mock data, a stub cannot tell you how many times a method has been called <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. This limitation can be addressed using spies.

## Service Spies

A spy is a more advanced testing utility, often provided by testing frameworks like Jasmine, that allows you to monitor calls to existing methods <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. Unlike stubs, spies are often used with the live service itself, but configured to prevent actual external calls.

> [!definition] What is a Spy?
> A spy is a Jasmine utility used to monitor method calls, including how many times a method has been called and with what arguments <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

### Implementation
To use a spy, you typically provide the actual service in your `TestBed` <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. Then, using Jasmine's `spyOn` function, you can monitor a specific method of that service <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

```typescript
// Get the service instance from the injector
service = debugEl.injector.get(MessageService);

// Set up the spy on the service method
spy = spyOn(service, 'getContent');
```
Crucially, you can also tell the spy to return a specific value, preventing the actual method from being executed and thus avoiding real backend requests <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>:
```typescript
spy.and.returnValue(of({ value: 'You have been warned' }));
```
This setup allows you to test both the return value and the interaction with the service.

### Verification
With a spy, you can verify if a method was called and how many times it was called <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>:
```typescript
it('should ensure service method was called once and view is updated', () => {
  // Ensure the service method was called
  expect(spy).toHaveBeenCalled(); // <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>

  // Ensure it was called exactly once
  expect(spy.calls.all().length).toEqual(1); // <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>

  // Also verify that the UI is updated with the mocked data
  // (e.g., checking the inner text of an HTML element)
  const messageBody = fixture.debugElement.query(By.css('.message-body'));
  expect(messageBody.nativeElement.innerText).toContain('warn'); // <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>
});
```
Spies can also tell you the arguments with which a method was called <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. More information on spy capabilities can be found in the Jasmine documentation <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.

By effectively using stubs and spies, developers can create robust [[testing_strategies_in_software_development | testing strategies]] that isolate components and services, leading to more reliable and maintainable software <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.