---
title: Behavioral patterns in programming
videoId: tv-_1er1mWI
---

From: [[fireship]] <br/> 

[[overview_of_software_design_patterns | Software design patterns]] are categorized into three main groups: [[understanding_creational_patterns | creational patterns]], [[structural_patterns_in_software_design | structural patterns]], and behavioral patterns <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Behavioral patterns specifically describe how objects communicate with each other <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Iterator Pattern
The iterator pattern allows you to traverse through a collection of objects <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Modern programming languages often provide built-in abstractions for this pattern, such as the `for` loop, which is an example of the iterator pattern when used to loop over an array <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### Implementation in JavaScript
While JavaScript lacks a built-in `range` function, you can implement a custom iterator <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. This involves defining an object with a `next` method <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. The `next` function must return an object containing a `value` (the current value in the loop) and a `done` property (indicating when to finish iterating) <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. In this custom iterator, the process continues as long as the `start` value is less than the `end` value, incrementing the `start` value by a `step` in each iteration <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. Once the `start` value becomes greater than the `end`, an object with `done` set to `true` is returned, signaling JavaScript to stop <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

By adding `Symbol.iterator` to this object, it can then be used in a regular `for...of` loop <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. The essence of iteration is to define how to move from the beginning to the end of a collection <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. The iterator pattern is considered a pull-based system <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

## Observer Pattern
Unlike the pull-based iterator, the observer pattern is a push-based system <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. This pattern allows multiple objects to subscribe to events broadcast by another object, establishing a one-to-many relationship <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. An analogy is a radio tower broadcasting a signal to many receivers <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

This pattern is widely used in app development; for example, in Firebase, when server data changes, all subscribed client applications are automatically updated <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. Libraries like RxJS can simplify the demonstration of this pattern <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. A `Subject` class (the data to listen to) can have multiple subscriptions added to it <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. The `Subject` tracks these subscriptions and calls their callback functions whenever its data changes <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. When a new value is pushed using the `next` method, every subscription is notified <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

## Mediator Pattern
The mediator pattern involves a "middleman" or "broker" <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. It addresses scenarios where many objects need to communicate, potentially leading to a complex and dangerous many-to-many relationship <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

### Example: Air Traffic Control
Imagine multiple airplanes and runways needing to coordinate landing clearances <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. Instead of direct communication between all planes and runways, a mediator, like an air traffic controller, sits between them to provide coordination <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

### Practical Example: Express.js Middleware
In the Express.js web framework, a middleware system acts as a mediator <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Middleware intercepts incoming requests (like airplanes) and transforms them into the proper format for the response (the runway) <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. This provides a separation of concerns and eliminates code duplication <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

## State Pattern
The state pattern enables an object to behave differently based on a finite number of internal states <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. While traditional methods involve conditional logic or switch statements to handle different possibilities based on application state or data, this approach often doesn't scale well <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

The state pattern allows you to start with one base class and provide it with varying functionality dependent on its internal state <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. This concept is related to finite state machines, aiming to make an object's behavior predictable based on its underlying state <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

### Implementation
Instead of a switch statement to determine behavior based on an object's `mood` (state) <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>, separate classes can be created for each possible state <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. Each state class would have an identical method that behaves differently <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. The main object (e.g., `Human` class) sets its state as a property, delegating method calls to its current state <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. This means the object's behavior changes completely when its state changes, without modifying the API or using extensive conditional logic <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

Knowing how to write recognized [[criticism_and_practical_use_of_design_patterns | design patterns]] will help level up as a programmer <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.