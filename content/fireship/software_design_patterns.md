---
title: Software design patterns
videoId: tv-_1er1mWI
---

From: [[fireship]] <br/> 

When first becoming a junior developer, code might resemble "Play-Doh snakes" <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. As a developer progresses to a senior role and learns about [[software_engineering_and_development_tools | software design patterns]], their code can evolve to resemble the Sistine Chapel <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. However, a principal engineer might realize that maintaining a "Sistine Chapel" for a simple website is unnecessary, leading to a return to simpler "Play-Doh snakes" <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

[[software_engineering_and_development_tools | Software design patterns]] are reusable solutions to common problems faced by [[programming_concepts_and_paradigms | programmers]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. They are not algorithms that can simply be copied and pasted <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>; instead, they require thought to implement <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Improper use of these patterns can add additional [[common_frustrations_in_software_engineering | complexity]] and boilerplate to a codebase <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. Nevertheless, understanding and implementing recognized [[software_engineering_and_development_tools | design patterns]] can significantly enhance a [[programming_concepts_and_paradigms | programmer]]'s skill level <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

A highly influential book in [[programming_concepts_and_paradigms | programming]] history, "Design Patterns," written by four C++ engineers known as "The Gang of Four," outlines 23 approaches to recurring problems <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Categories of Design Patterns

[[software_engineering_and_development_tools | Design patterns]] are categorized into three main types <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>:
*   **Creational Patterns:** Focus on how objects are created <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Structural Patterns:** Deal with how objects relate to each other <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Behavioral Patterns:** Describe how objects communicate with each other <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

Becoming a proficient [[software_engineering_and_development_tools | software engineer]] is about solving problems, not just memorizing [[programming_concepts_and_paradigms | programming language]] syntax <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Creational Patterns

Creational patterns abstract the instantiation process, making the system independent of how its objects are created, composed, and represented.

### [[singleton_pattern | Singleton Pattern]]

The [[singleton_pattern | Singleton pattern]] ensures that a class has only one instance and provides a global point of access to it <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   **Implementation Example (TypeScript):** A class, such as `Settings` for global app settings, can implement the [[singleton_pattern | Singleton pattern]] by having a static instance property and a private constructor to prevent direct instantiation with `new` <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. A static `getInstance` method checks if an instance already exists, creating one if not, thereby guaranteeing only one object is created <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **JavaScript Nuance:** In JavaScript, simpler object literals or global objects, where objects are passed by reference, can provide similar characteristics without the need for the [[singleton_pattern | Singleton pattern]]'s boilerplate <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The advice is to leverage a [[programming_concepts_and_paradigms | language]]'s built-in features before opting for a [[software_engineering_and_development_tools | design pattern]] <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### [[prototype_pattern | Prototype Pattern]]

The [[prototype_pattern | Prototype pattern]] involves cloning an existing object to create new instances <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **Alternative to Inheritance:** While traditional object-oriented [[programming_concepts_and_paradigms | programming]] often uses class-based inheritance, which can lead to complex hierarchies <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>, the [[prototype_pattern | Prototype pattern]] offers an alternative <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Instead of inheriting from a class, functionality is inherited from an already created object <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **JavaScript and Prototypal Inheritance:** JavaScript naturally supports prototypal inheritance <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>, resulting in a flat prototype chain that simplifies sharing functionality among objects <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. For example, `Object.create()` can be used to create a new object based on an existing "prototype" object (e.g., `zombie`), allowing new properties to be added while still accessing methods from the prototype via the prototype chain <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. While the `__proto__` property can be used to access an object's prototype, `Object.getPrototypeOf()` is the modern best practice <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Extending a class's prototype in JavaScript, though possible, is generally considered a bad practice <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### [[builder_pattern | Builder Pattern]]

The [[builder_pattern | Builder pattern]] constructs a complex object step by step <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Step-by-Step Construction:** Instead of passing all options to a constructor, the [[builder_pattern | Builder pattern]] creates an object using a series of methods <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. The building logic can even be delegated to a separate class <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Method Chaining:** In JavaScript, each method typically returns `this` (a reference to the object instance), enabling method chaining <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This allows for an object to be instantiated, followed by chained method calls to configure it <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. This pattern was frequently seen in libraries like jQuery but has become less prevalent in recent years <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

### Factory Pattern

The Factory pattern uses a function or method to instantiate an object instead of the `new` keyword <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Practical Example:** In a cross-platform application (e.g., iOS and Android) with common interfaces but differing implementations, a factory can determine which specific object (e.g., button type) to instantiate based on the environment <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. This eliminates repetitive conditional logic and improves maintainability <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

## Structural Patterns

Structural patterns concern class and object composition. They describe how to assemble objects and classes into larger structures, while keeping these structures flexible and efficient.

### Facade Pattern

A Facade provides a simplified interface to a complex subsystem <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Hiding [[common_frustrations_in_software_engineering | Complexity]]:** Like the face of a building, a facade hides the internal [[common_frustrations_in_software_engineering | complexity]] and low-level details from the end-user <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.# Software Design Patterns

When first becoming a junior developer, code might resemble "Play-Doh snakes" <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. As a developer progresses to a senior role and learns about [[software_engineering_and_development_tools | software design patterns]], their code can evolve to resemble the Sistine Chapel <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. However, a principal engineer might realize that maintaining a "Sistine Chapel" for a simple website is unnecessary, leading to a return to simpler "Play-Doh snakes" <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

[[software_engineering_and_development_tools | Software design patterns]] are reusable solutions to common problems faced by [[programming_concepts_and_paradigms | programmers]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. They are not algorithms that can simply be copied and pasted <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>; instead, they require thought to implement <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Improper use of these patterns can add additional [[common_frustrations_in_software_engineering | complexity]] and boilerplate to a codebase <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. Nevertheless, understanding and implementing recognized [[software_engineering_and_development_tools | design patterns]] can significantly enhance a [[programming_concepts_and_paradigms | programmer]]'s skill level <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

A highly influential book in [[programming_concepts_and_paradigms | programming]] history, "Design Patterns," written by four C++ engineers known as "The Gang of Four," outlines 23 approaches to recurring problems <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Categories of Design Patterns

[[software_engineering_and_development_tools | Design patterns]] are categorized into three main types <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>:
*   **Creational Patterns:** Focus on how objects are created <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Structural Patterns:** Deal with how objects relate to each other <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Behavioral Patterns:** Describe how objects communicate with each other <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

Becoming a proficient [[software_engineering_and_development_tools | software engineer]] is about solving problems, not just memorizing [[programming_concepts_and_paradigms | programming language]] syntax <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Creational Patterns

Creational patterns abstract the instantiation process, making the system independent of how its objects are created, composed, and represented.

### [[singleton_pattern | Singleton Pattern]]

The [[singleton_pattern | Singleton pattern]] ensures that a class has only one instance and provides a global point of access to it <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   **Implementation Example (TypeScript):** A class, such as `Settings` for global app settings, can implement the [[singleton_pattern | Singleton pattern]] by having a static instance property and a private constructor to prevent direct instantiation with `new` <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. A static `getInstance` method checks if an instance already exists, creating one if not, thereby guaranteeing only one object is created <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **JavaScript Nuance:** In JavaScript, simpler object literals or global objects, where objects are passed by reference, can provide similar characteristics without the need for the [[singleton_pattern | Singleton pattern]]'s boilerplate <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The advice is to leverage a [[programming_concepts_and_paradigms | language]]'s built-in features before opting for a [[software_engineering_and_development_tools | design pattern]] <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### [[prototype_pattern | Prototype Pattern]]

The [[prototype_pattern | Prototype pattern]] involves cloning an existing object to create new instances <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **Alternative to Inheritance:** While traditional object-oriented [[programming_concepts_and_paradigms | programming]] often uses class-based inheritance, which can lead to complex hierarchies <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>, the [[prototype_pattern | Prototype pattern]] offers an alternative <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Instead of inheriting from a class, functionality is inherited from an already created object <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **JavaScript and Prototypal Inheritance:** JavaScript naturally supports prototypal inheritance <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>, resulting in a flat prototype chain that simplifies sharing functionality among objects <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. For example, `Object.create()` can be used to create a new object based on an existing "prototype" object (e.g., `zombie`), allowing new properties to be added while still accessing methods from the prototype via the prototype chain <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. While the `__proto__` property can be used to access an object's prototype, `Object.getPrototypeOf()` is the modern best practice <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Extending a class's prototype in JavaScript, though possible, is generally considered a bad practice <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### [[builder_pattern | Builder Pattern]]

The [[builder_pattern | Builder pattern]] constructs a complex object step by step <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Step-by-Step Construction:** Instead of passing all options to a constructor, the [[builder_pattern | Builder pattern]] creates an object using a series of methods <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. The building logic can even be delegated to a separate class <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Method Chaining:** In JavaScript, each method typically returns `this` (a reference to the object instance), enabling method chaining <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This allows for an object to be instantiated, followed by chained method calls to configure it <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. This pattern was frequently seen in libraries like jQuery but has become less prevalent in recent years <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

### Factory Pattern

The Factory pattern uses a function or method to instantiate an object instead of the `new` keyword <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Practical Example:** In a cross-platform application (e.g., iOS and Android) with common interfaces but differing implementations, a factory can determine which specific object (e.g., button type) to instantiate based on the environment <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. This eliminates repetitive conditional logic and improves maintainability <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

## Structural Patterns

Structural patterns concern class and object composition. They describe how to assemble objects and classes into larger structures, while keeping these structures flexible and efficient.

### Facade Pattern

A Facade provides a simplified interface to a complex subsystem <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Hiding [[common_frustrations_in_software_engineering | Complexity]]:** Like the face of a building, a facade hides the internal [[common_frustrations_in_software_engineering | complexity]] and low-level details from the end-user <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Example:** For systems like plumbing or electrical, a facade class can simplify operations (e.g., combining complex details into a single "turn on/off" method) by containing the low-level systems as dependencies <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. Many JavaScript packages act as facades, with jQuery being a notable example that simplifies annoying low-level JavaScript features <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

### Proxy Pattern

A Proxy acts as a substitute or placeholder for another object, allowing for control over access to the original object <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Interception and Reactivity:** A proxy can intercept operations on a target object, such as getting or setting properties <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. This is utilized in reactivity systems like Vue.js, where the framework replaces original data objects with proxies to intercept changes and automatically update the UI <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. The proxy takes the original object and a handler (with methods like `get` and `set`) as arguments <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. `Reflect` can be used within the handler to update the original object's data <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Memory Efficiency:** Proxies are also useful when dealing with very large objects that would be expensive to duplicate in memory <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

## Behavioral Patterns

Behavioral patterns are concerned with algorithms and the assignment of responsibilities between objects. They describe how objects and classes interact and distribute responsibility.

### Iterator Pattern

The Iterator pattern allows for sequential traversal through a collection of objects without exposing their underlying representation <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Abstractions in Modern [[programming_concepts_and_paradigms | Languages]]:** Modern [[programming_concepts_and_paradigms | languages]] often provide built-in abstractions for the Iterator pattern, such as the `for` loop, which iterates over arrays <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   **Custom Iterator Example (JavaScript):** A custom iterator in JavaScript can be implemented by defining an object with a `next` method <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. This method should return an object containing the current `value` and a `done` property (a boolean indicating if iteration is complete) <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. By adding `Symbol.iterator` to this object, it can then be used directly in a `for...of` loop <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. The Iterator pattern is a "pull-based" system <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

### [[observer_pattern | Observer Pattern]]

The [[observer_pattern | Observer pattern]] allows multiple objects to subscribe to events broadcast by another object, establishing a one-to-many relationship <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. It is a "push-based" system <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
*   **Real-World Application:** This pattern is widely used in [[trends_in_programming_languages_and_web_development | app development]], for example, in Firebase, where client applications subscribe to server data changes and are automatically updated <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   **Implementation Example (RxJS):** Libraries like RxJS provide a `Subject` class to represent the data to be observed <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. Multiple subscriptions can be added to the `Subject`, which tracks them and calls their callback functions when the data changes via the `next` method <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

### Mediator Pattern

A Mediator acts as a middleman or broker to facilitate communication between objects, reducing direct dependencies among them <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
*   **Solving Many-to-Many Relationships:** When multiple objects need to communicate with each other (e.g., airplanes and runways determining clearance), a dangerous many-to-many relationship can emerge <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. A mediator (like an air traffic controller) centralizes coordination and communication, sitting between the objects <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
*   **Practical Example (Express.js Middleware):** In the Express.js [[web development | web framework]], middleware acts as a mediator <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. It intercepts incoming requests, transforming them into the proper format for the response, thus providing separation of concerns and eliminating code duplication <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

### State Pattern

The State pattern allows an object to alter its behavior when its internal state changes, making it appear as if the object has changed its class <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Managing Behavioral Changes:** Rather than using conditional logic or switch statements that can become unscalable <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>, the State pattern provides different functionality based on an object's internal state <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. This concept is related to finite state machines, as seen in libraries like XState, aiming to make an object's behavior predictable based on its underlying state <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
*   **Implementation Example:** Instead of a `Human` class using a switch statement to `think` differently based on `mood` <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>, separate classes can be created for each possible mood state <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. Each state class would have an identical method (`think`) that behaves differently <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. The `Human` class would hold the current state as a property, delegating the method call to its current state object <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. This allows the object's behavior to change without altering its API or relying on extensive conditional logic <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.