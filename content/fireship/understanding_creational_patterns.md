---
title: Understanding creational patterns
videoId: tv-_1er1mWI
---

From: [[fireship]] <br/> 

As a junior developer, code may initially resemble "Play-Doh snakes," but with experience and learning about [[overview_of_software_design_patterns | software design patterns]], it can evolve to resemble the "Sistine Chapel." However, a principal engineer might realize that complex "Sistine Chapel" code is not ideal for a "silly website" and revert to simpler "Play-Doh snakes" for maintainability <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article explores various [[overview_of_software_design_patterns | software design patterns]], including their pros and cons, which can be subjective and controversial <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

One of the most influential books in programming history is "Design Patterns" by the "Gang of Four," four C++ engineers <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This book details 23 different approaches to solve common programming problems <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. These patterns are categorized into three main types:
*   **[[object_creation_and_manipulation | Creational patterns]]**: Focus on how objects are created <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   **[[structural_patterns_in_software_design | Structural patterns]]**: Deal with how objects relate to each other <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **[[behavioral_patterns_in_programming | Behavioral patterns]]**: Describe how objects communicate with each other <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

Becoming a proficient software engineer is less about memorizing programming language syntax and more about problem-solving abilities <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. [[overview_of_software_design_patterns | Design patterns]] are not simply algorithms to copy and paste; they require critical thinking for proper implementation <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Improper use of [[overview_of_software_design_patterns | design patterns]] can introduce unnecessary complexity and boilerplate code <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Despite criticisms, understanding recognized [[overview_of_software_design_patterns | design patterns]] can significantly enhance a programmer's skill <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## Creational Patterns

### Singleton Pattern

The Singleton pattern ensures that a type of object can be instantiated only once <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

*   **Implementation Example (TypeScript)**:
    *   A `Settings` class (representing global app settings) can be implemented as a Singleton <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
    *   It includes a static `instance` property <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
    *   Its constructor is made private to prevent direct instantiation using the `new` keyword <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   A static `getInstance` method is created; this method checks if an instance already exists and creates a new one only if it doesn't, ensuring only one object is ever created <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Considerations in JavaScript**: In JavaScript, similar characteristics can be achieved by simply creating a global object due to object literals and objects being passed by reference <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. In such cases, the Singleton pattern might be considered unnecessary boilerplate <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. The advice is to leverage a language's built-in features before implementing a [[overview_of_software_design_patterns | design pattern]] <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

### Prototype Pattern

The Prototype pattern is a way to clone objects <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

*   **Alternative to Inheritance**: Unlike traditional inheritance where a class is extended by a subclass, the Prototype pattern implements inheritance by deriving functionality from an object that has already been created <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Flat Prototype Chain**: This approach creates a flatter prototype chain, simplifying the sharing of functionality between objects <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **Relevance in JavaScript**: JavaScript supports [[prototypal_inheritance_in_javascript | prototypal inheritance]] inherently <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **Example (JavaScript)**:
    *   To create a new object based on an existing "zombie" prototype, `Object.create()` can be used, passing the prototype as an argument and specifying additional properties <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
    *   When such an object is logged, only its direct properties might be visible, but methods from its prototype chain will still work because JavaScript traverses the chain to find methods or properties <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
    *   The prototype of an object can be accessed using `__proto__` (though not a modern best practice) or, preferably, `Object.getPrototypeOf()` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
    *   In JavaScript classes, `prototype` refers to its constructor, allowing functions to be added to a class, though this is generally considered a bad practice <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

### Builder Pattern

The Builder pattern constructs an object step-by-step using methods instead of solely relying on the constructor <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

*   **Deferred Construction**: This allows each step of object creation to be deferred to a later point <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   **Delegation**: The building logic can even be delegated to a completely separate class <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Implementation (JavaScript)**: In JavaScript, methods can return `this` (a reference to the object instance), enabling method chaining. This allows instantiating an object and then chaining methods to it, with the object always being the return value <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Common Use**: This [[overview_of_software_design_patterns | pattern]] was frequently seen with libraries like jQuery, though its use has somewhat declined in recent years <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

### Factory Pattern

The Factory pattern uses a function or method to instantiate an object instead of the `new` keyword <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

*   **Practical Example (Cross-Platform App)**:
    *   In a cross-platform application (e.g., iOS and Android) where both platforms have similar interfaces but require different underlying button implementations, one might initially use conditional checking to determine which button to display <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. This approach is not very maintainable <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
    *   Instead, a subclass or function can be created that determines which object to instantiate <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. The factory then decides which button should be rendered, eliminating repetitive conditional logic <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.