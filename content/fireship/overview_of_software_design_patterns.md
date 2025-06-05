---
title: Overview of software design patterns
videoId: tv-_1er1mWI
---

From: [[fireship]] <br/> 

Software design patterns offer established solutions to common problems encountered during software development <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. They are not merely algorithms to be copied, but require thought and understanding for proper implementation <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Becoming a proficient software engineer is more about the ability to [[problemsolving_skills_in_software_development | solve problems]] than memorizing syntax <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## The Gang of Four and Pattern Categories

One of the most influential books on the subject is "Design Patterns," written by four C++ engineers known as "The Gang of Four" <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This book outlines 23 different approaches to address recurring problems faced by programmers <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. These patterns are categorized into three main types:

*   [[understanding_creational_patterns | Creational patterns]]: Focus on how objects are created <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   [[structural_patterns_in_software_design | Structural patterns]]: Deal with how objects relate to each other <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   [[behavioral_patterns_in_programming | Behavioral patterns]]: Address how objects communicate with each other <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

While learning these patterns can significantly level up a programmer's skills <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>, their application can be subjective and controversial <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Improper use can lead to increased complexity and boilerplate code <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. As a developer progresses, they might realize that maintaining overly complex "Sistine Chapel" code for a "silly website" is undesirable, sometimes leading back to simpler "Play-Doh snake" solutions <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. It's crucial to lean on a language's built-in features before implementing a complex design pattern <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Common Design Patterns

### Creational Patterns

#### Singleton Pattern
The Singleton pattern ensures that a class has only one instance and provides a global point of access to it <a class="yt-timestamp" data-t="01:36">[01:36]</a>. For example, a `Settings` class could be implemented as a Singleton to represent global application settings <a class="yt-timestamp" data-t="01:42">[01:42]</a>. This is achieved by making its constructor private and providing a static method to retrieve the single instance <a class="yt-timestamp" data-t="01:47">[01:47]</a>. In JavaScript, simple global objects can often achieve the same characteristics without the extra boilerplate of a formal Singleton pattern <a class="yt-timestamp" data-t="02:11">[02:11]</a>.

#### Prototype Pattern
The Prototype pattern is essentially a "clone" pattern <a class="yt-timestamp" data-t="02:26">[02:26]</a>. It offers an alternative to traditional [[Composition vs Inheritance in software development | inheritance]], allowing new objects to derive functionality from an existing object rather than a class <a class="yt-timestamp" data-t="02:40">[02:40]</a>. This approach can create a "flat prototype chain" that simplifies sharing functionality, especially in dynamic languages like JavaScript which supports prototypal inheritance natively <a class="yt-timestamp" data-t="02:54">[02:54]</a>.

#### Builder Pattern
The Builder pattern constructs a complex object step-by-step using methods instead of a single constructor <a class="yt-timestamp" data-t="03:58">[03:58]</a>. This allows for deferred or delegated construction logic <a class="yt-timestamp" data-t="04:02">[04:02]</a>. In JavaScript, returning `this` from each method enables method chaining, where an object is instantiated and then methods are chained to it <a class="yt-timestamp" data-t="04:07">[04:07]</a>. This pattern is commonly seen in libraries like jQuery <a class="yt-timestamp" data-t="04:18">[04:18]</a>.

#### Factory Pattern
The Factory pattern uses a function or method to instantiate an object instead of the `new` keyword <a class="yt-timestamp" data-t="04:27">[04:27]</a>. This is useful for building cross-platform applications, like one running on iOS and Android, where different platform-specific objects (e.g., buttons) need to be created based on conditions <a class="yt-timestamp" data-t="04:34">[04:34]</a>. A factory can encapsulate the logic to determine which object to instantiate, leading to more maintainable code <a class="yt-timestamp" data-t="04:45">[04:45]</a>.

### Structural Patterns

#### Facade Pattern
A Facade provides a simplified API that hides complex low-level details within a codebase <a class="yt-timestamp" data-t="05:06">[05:06]</a>. For instance, a smart home system might have complex plumbing and electrical systems, but a Facade class could combine their operations into a single method, allowing users to simply turn them on or off <a class="yt-timestamp" data-t="05:27">[05:27]</a>. Many JavaScript packages act as facades, abstracting away annoying low-level features <a class="yt-timestamp" data-t="05:37">[05:37]</a>.

#### Proxy Pattern
The Proxy pattern acts as a substitute for a target object <a class="yt-timestamp" data-t="05:49">[05:49]</a>. It allows for intercepting operations on the original object and performing additional actions. A notable example is the reactivity system in Vue.js, where data objects are replaced with proxies to intercept changes and update the UI automatically <a class="yt-timestamp" data-t="06:01">[06:01]</a>. Proxies can override methods like `get` and `set` to run code when properties are accessed or changed <a class="yt-timestamp" data-t="06:19">[06:19]</a>. They are also useful for large objects that would be expensive to duplicate in memory <a class="yt-timestamp" data-t="06:40">[06:40]</a>.

### Behavioral Patterns

#### Iterator Pattern
The Iterator pattern allows for traversing through a collection of objects <a class="yt-timestamp" data-t="06:47">[06:47]</a>. Modern languages often provide built-in abstractions like the `for` loop, which uses the iterator pattern implicitly when iterating over arrays <a class="yt-timestamp" data-t="06:54">[06:54]</a>. In JavaScript, a custom iterator can be implemented by defining an object with a `next` method that returns an object containing `value` and `done` properties <a class="yt-timestamp" data-t="07:12">[07:12]</a>. This enables custom iteration logic, for example, creating a range function <a class="yt-timestamp" data-t="07:07">[07:07]</a>.

#### Observer Pattern
The Observer pattern is a "push-based" system where many objects (observers) subscribe to events broadcast by another object (the subject) <a class="yt-timestamp" data-t="07:59">[07:59]</a>. It represents a one-to-many relationship <a class="yt-timestamp" data-t="08:06">[08:06]</a>. This pattern is widely used in [[design_techniques_in_app_development | app development]], such as in Firebase, where client applications are automatically updated when data changes on the server <a class="yt-timestamp" data-t="08:15">[08:15]</a>. Libraries like RxJS provide `Subject` classes to implement this pattern, allowing multiple subscriptions to be notified whenever the subject's data changes <a class="yt-timestamp" data-t="08:24">[08:24]</a>.

#### Mediator Pattern
The Mediator pattern introduces a "middleman" or "broker" to manage complex communication between multiple objects, preventing a dangerous many-to-many relationship <a class="yt-timestamp" data-t="09:00">[09:00]</a>. An air traffic controller mediating between airplanes and runways is a real-world analogy <a class="yt-timestamp" data-t="09:20">[09:20]</a>. In programming, the middleware system in the Express.js web framework is a practical example, intercepting and transforming incoming requests before they reach the response <a class="yt-timestamp" data-t="09:31">[09:31]</a>. This pattern provides a separation of concerns and reduces code duplication <a class="yt-timestamp" data-t="09:43">[09:43]</a>.

#### State Pattern
The State pattern allows an object to alter its behavior based on its internal state <a class="yt-timestamp" data-t="09:51">[09:51]</a>. Instead of using extensive conditional logic or switch statements, the State pattern involves creating separate classes for each possible state <a class="yt-timestamp" data-t="10:27">[10:27]</a>. Each state class has identical methods that behave differently. The main object delegates method calls to its current state object, ensuring that its behavior changes predictably with state transitions without modifying its API <a class="yt-timestamp" data-t="10:35">[10:35]</a>. This idea is related to finite state machines used in libraries like XState <a class="yt-timestamp" data-t="10:12">[10:12]</a>.