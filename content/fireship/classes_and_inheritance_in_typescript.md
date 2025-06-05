---
title: Classes and Inheritance in TypeScript
videoId: fsVL_xrYO0w
---

From: [[fireship]] <br/> 

The debate between different programming paradigms, like [[Object Oriented Programming with TypeScript | object-oriented]] and [[Functional Programming with TypeScript | functional programming]], often arises in software development. There's no single correct way to write code, and every decision involves trade-offs <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Object-Oriented Programming with TypeScript

In [[Object Oriented Programming with TypeScript | object-oriented programming]], a class serves as a blueprint for instantiating objects <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

### Defining a Class
A class itself doesn't perform actions but defines the structure and behavior for objects created from it <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. For example, an `Emoji` class instance would be an object with an `icon` property <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### Constructors
The `constructor` method is special because it runs once when an object is instantiated <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. Arguments passed to the constructor are used to set properties on the new object <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
To create an instance of a class, the `new` keyword is used in front of the class name <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

### Public and Private Members
TypeScript provides the concept of `public` and `private` members within classes <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
*   **Public members**: Declaring a property or method as `public` makes it available to the class itself and any instances of the class <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. While convenient, direct mutation of public properties can make code harder to track and test <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. In TypeScript, using the `public` keyword in the constructor argument automatically sets it as a public property on each object <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **Private members**: Marking members as `private` means they can only be used inside the class definition <a class="yt="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. This helps separate the public API from internal logic <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. For example, to make a value immutable, it can be made `private` with a `getter` method for reading but not changing the value <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

### Internal State
Class instances can maintain their own internal state <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. This allows for simple implementation of state changes, such as toggling an emoji <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. A method can mutate the internal properties of an instance, updating its state <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. The end result is a class that encapsulates all logic for its behavior <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. TypeScript also provides [[typescript_interfaces_and_custom_types | interfaces]] and documentation for classes <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

### Static Methods
Classes can define `static` methods, which are unique because they belong to the class itself, not an instance of the class <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. A `static` method can be a [[Functional Programming with TypeScript | pure function]] that performs an operation without relying on instance-specific data <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. The class can then be used as a namespace to run this function <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

> [!NOTE]
> [[prototypal_inheritance_in_javascript | Classes in JavaScript]] are actually syntactic sugar for functions and [[prototypal_inheritance_in_javascript | prototypal inheritance]] <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. When compiled to ES3, a class appears as a function with a closure to prevent local variables from bleeding into the global scope <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

## Inheritance for Code Reusability

[[Composition vs Inheritance in software development | Inheritance]] is a pattern for code reusability where a child class inherits all functionality from a larger base class and then overrides or extends it with custom behaviors <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

### Implementing Inheritance
In TypeScript, the `extends` keyword is used to inherit functionality <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
*   A `Human` class might have a `name` property and a `sayHi` method <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   A `SuperHuman` class can `extend` `Human`, inheriting all its features <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
*   The `super()` keyword must be called within the child class's constructor to execute the parent class's constructor code, typically for initializing inherited properties <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
*   The child class can then define additional methods, such as `superPower` <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
An instance of the child class will have both its own methods and all methods defined in the parent class <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

### Downsides of Inheritance
While beneficial in the right context, it's best to avoid creating deeply nested class hierarchies as they can become very difficult to debug <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

## Composition as an Alternative in Classes

[[Composition vs Inheritance in software development | Composition]], as an alternative to inheritance, breaks interfaces and logic into many small pieces, then builds larger functions or objects by combining these pieces <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
One approach is concatenating objects, often referred to as a "mixin pattern," which is a type of multiple inheritance <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. This decouples properties and behaviors into objects or functions that return objects, which are then merged into a final function <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

### Mixins with TypeScript Classes
TypeScript offers the flexibility to use mixins in a class-based format <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
1.  Define small "behavior classes" that focus on "what something does" rather than "what something is" <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
2.  In the main class, use the `implements` keyword to include multiple behavior classes. When implementing, only the [[typescript_interfaces_and_custom_types | interface]] (shape) is considered, not the underlying code <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
3.  An `applyMixins` function (often from TypeScript documentation) is used to apply the code of these implemented interfaces to the main class <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
4.  This approach may require some boilerplate code, specifically typing the return values on the methods for the combined class <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.
5.  Finally, the `applyMixins` function is called with the base class and the mixed-in classes as arguments <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.